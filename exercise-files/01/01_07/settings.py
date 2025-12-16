import streamlit as st

# ----------------------------
# Model catalogs
# ----------------------------
TEXT_MODELS = {
    "GPT-4o Mini (fast)": "gpt-4o-mini",
    "GPT-4o (best quality)": "gpt-4o",
    "GPT-3.5 Turbo (legacy)": "gpt-3.5-turbo",
}

IMAGE_MODELS = {
    "GPT Image 1 (best quality)": "gpt-image-1",
    "GPT Image 1 Mini (cheaper)": "gpt-image-1-mini",
}

def setup_sidebar():
    with st.sidebar:
        st.header("⚙️ Settings")

        text_label = st.selectbox("Text model", list(TEXT_MODELS.keys()), index=0)
        st.session_state["text_model"] = TEXT_MODELS[text_label]

        image_label = st.selectbox("Image model", list(IMAGE_MODELS.keys()), index=0)
        st.session_state["image_model"] = IMAGE_MODELS[image_label]

        st.session_state["temperature"] = st.slider("Temperature", 0.0, 1.5, 0.7, 0.1)
        