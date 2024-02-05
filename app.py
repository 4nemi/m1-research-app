import streamlit as st
import pandas as pd

from utils.utils import set_custom_style, display_item


@st.cache_data
def load_data(participant_id: int):
    df = pd.read_csv(f"data/10000/proposed_{participant_id}.csv")
    df = df[["anime_id", "name", "genres", "type", "episodes", "aired", "image_url"]]
    return df


def main():
    st.set_page_config(
        page_title="Anime Recommender",
        page_icon=":tv:",
        layout="wide",
    )
    participant_id = st.text_input("参加者IDを入力してください", '')
    if participant_id:
        df = load_data(participant_id)
        df = df.sample(8)
        items = df.to_dict(orient="records")

        if "displayed_anime" not in st.session_state:
            st.session_state.displayed_anime = []
        if "interest" not in st.session_state:
            st.session_state.interest = {}
        if "unknown" not in st.session_state:
            st.session_state.unknown = {}

        for i in range(0, len(items), 4):
            cols = st.columns(3)
            for col, item in zip(cols, items[i : i + 4]):
                with col:
                    interest, unknown = display_item(item)
                    st.session_state.interest[item["anime_id"]] = interest
                    st.session_state.unknown[item["anime_id"]] = unknown


if __name__ == "__main__":
    main()
