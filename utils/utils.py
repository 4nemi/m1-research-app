import streamlit as st


def set_custom_style():
    custom_style = """
    <style>
        /* ページ全体のマージンとパディングを変更 */
        .css-18e3th9 {
            padding: 0px;  /* 例：上下左右のパディングを20pxに設定 */
            margin: 0px;   /* 例：上下左右のマージンを10pxに設定 */
        }
        /* アイテム間のマージンとパディングを変更 */
        .stImage, .stSlider {
            margin: 0px 0;  /* 例：上下のマージンを15pxに設定 */
            padding: 5px;    /* 例：パディングを5pxに設定 */
        }
    </style>
    """
    st.markdown(custom_style, unsafe_allow_html=True)


def display_item(item):
    st.image(item["image_url"], width=200)
    st.write(item["name"])
    with st.expander("Show more"):
        st.write(f"ジャンル: {item['genres']}")
        st.write(f"タイプ: {item['type']}")
        st.write(f"エピソード数: {item['episodes']}")
        st.write(f"放送日: {item['aired']}")

    # スライダーを使って評価を入力
    interest = st.slider("興味", 1, 5, 3, key=f"{item['anime_id']}_interest")
    unknown = st.slider("知らなさ", 1, 5, 3, key=f"{item['anime_id']}_unknown")
    return interest, unknown


"""
def display_item(col, item):
    col.markdown(
        f"<div style='text-align' center'><img src='{item['image_url']}' style='max-width: 100%; height: auto;'></div>",
        unsafe_allow_html=True,
    )

    with col.expander("Show more"):
        col.write(f"ジャンル: {item['genres']}")
        col.write(f"タイプ: {item['type']}")
        col.write(f"エピソード数: {item['episodes']}")
        col.write(f"放送日: {item['aired']}")

    # スライダーを使って評価を入力
    interest = col.slider("興味", 1, 5, 3, key=f"{item['anime_id']}_interest")
    unknown = col.slider("知らなさ", 1, 5, 3, key=f"{item['anime_id']}_unknown")

    return interest, unknown
"""
