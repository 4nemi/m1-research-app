import streamlit as st
import pandas as pd
import os

from utils.utils import display_item


@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df = df[["anime_id", "name", "genres", "type", "episodes", "aired", "image_url"]]
    return df


def download_evaluations(evaluations: dict):
    df = pd.DataFrame.from_dict(evaluations, orient="index").reset_index()
    df.columns = ["file", "anime_id", "interest", "unknown", "discovery"]
    st.download_button(label="ダウンロード", data=df.to_csv(index=False), file_name="evaluations.csv", mime="text/csv")


def main():
    st.set_page_config(
        page_title="Anime Recommender",
        page_icon=":tv:",
        layout="wide",
    )
    csv_files = [
        "explicit.csv",
        "unknown.csv",
        "proposed.csv",
        "random.csv",
    ]

    participant_id = st.text_input("参加者IDを入力してください")
    if participant_id:
        dir_path = f"data/{participant_id}"
        if os.path.exists(dir_path):
            files = [os.path.join(dir_path, file) for file in csv_files]

            if "current_file_index" not in st.session_state:
                st.session_state.current_file_index = 0
            if "evaluations" not in st.session_state:
                st.session_state.evaluations = {}

            # stepを表示
            st.write(f"プロセス: {st.session_state.current_file_index + 1}")

            if st.session_state.current_file_index < 4:
                file_path = files[st.session_state.current_file_index]
                df = load_data(file_path)
                items = df.to_dict(orient="records")
                for i in range(0, len(items), 3):
                    cols = st.columns(3)
                    for col, item in zip(cols, items[i : i + 3]):
                        with col:
                            interest, unknown, discovery = display_item(item, st.session_state.current_file_index)
                            st.session_state.evaluations[(os.path.basename(file_path), item["anime_id"])] = {
                                "interest": interest,
                                "unknown": unknown,
                                "discovery": discovery,
                            }

                if st.button("次へ"):
                    st.session_state.current_file_index += 1
                    st.rerun()
            else:
                st.write("すべての評価が完了しました！ありがとうございました！")
                st.write("以下のボタンをクリックして評価をダウンロードしてください")
                download_evaluations(st.session_state.evaluations)
        else:
            st.write("参加者IDが見つかりませんでした")


if __name__ == "__main__":
    main()
