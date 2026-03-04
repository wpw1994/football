import os

import pandas as pd
import streamlit as st


@st.cache_data
def load_workbook(path: str) -> dict[str, pd.DataFrame]:
    if not os.path.exists(path):
        st.error(f"未找到文件：{path}")
        return {}
    try:
        # 读取所有工作表，返回 {sheet_name: DataFrame}
        return pd.read_excel(path, sheet_name=None, engine="openpyxl")
    except Exception as e:
        st.error(f"读取 Excel 出错：{e}")
        return {}


def main() -> None:
    st.set_page_config(page_title="足球盘口查询", layout="wide")
    st.title("足球盘口查询工具")

    default_path = "ft.xlsx"
    excel_path = st.text_input("Excel 文件路径", value=default_path)

    workbook = load_workbook(excel_path)
    if not workbook:
        st.stop()

    sheet_names = list(workbook.keys())
    league = st.selectbox("选择联赛（工作表）", sheet_names)

    df = workbook[league]

    st.subheader("原始数据预览")
    st.dataframe(df.head(50), use_container_width=True)

    st.markdown("---")
    st.subheader("按盘口信息筛选")

    # 固定使用“盘口.1”这一列进行筛选
    target_column_name = "盘口.1"
    if target_column_name not in df.columns:
        st.error(f"当前工作表中未找到名为「{target_column_name}」的列，请确认列名是否一致。")
        st.stop()

    keyword = st.text_input("输入实时赔率（支持模糊匹配，例如：0.80、0.95 等）")

    if keyword:
        mask = df[target_column_name].astype(str).str.contains(keyword, na=False)
        filtered = df[mask]

        st.write(f"共找到 **{len(filtered)}** 条记录。")
        st.dataframe(filtered, use_container_width=True)

        if not filtered.empty:
            csv_bytes = filtered.to_csv(index=False).encode("utf-8-sig")
            st.download_button(
                label="下载筛选结果（CSV）",
                data=csv_bytes,
                file_name=f"{league}_filtered.csv",
                mime="text/csv",
            )
    else:
        st.info("请输入盘口关键字进行筛选。")


if __name__ == "__main__":
    main()

