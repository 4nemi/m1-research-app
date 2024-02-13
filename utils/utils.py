import streamlit as st


def display_item(item, step):
    st.image(item["image_url"], width=200)
    st.write(item["name"])
    with st.expander("Show more"):
        st.write(f"ジャンル: {item['genres']}")
        st.write(f"タイプ: {item['type']}")
        st.write(f"エピソード数: {item['episodes']}")
        st.write(f"放送日: {item['aired']}")

    # スライダーを使って評価を入力
    interest = st.slider("興味", 1, 5, 3, key=f"{item['anime_id']}_{step}_interest")
    unknown = st.slider("知らなさ", 1, 5, 3, key=f"{item['anime_id']}_{step}_unknown")
    discovery = st.slider("発見性", 1, 5, 3, key=f"{item['anime_id']}_{step}_discovery")
    return interest, unknown, discovery
