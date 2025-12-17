import streamlit as st # type: ignore

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
    "Dalle-3 (creative)": "dalle-3"
}

# ----------------------------
# OpenAI TTS voices by gender
# ----------------------------
TTS_VOICES = {
    "Female": ["alloy", "nova", "shimmer", "coral"],
    "Male": ["ash", "echo", "onyx", "sage", "fable"],
}

def setup_sidebar():
    with st.sidebar:
        st.header("⚙️ Settings")
        st.subheader("Models", divider="gray")

        # --- Text model ---
        text_label = st.selectbox("Text model", list(TEXT_MODELS.keys()), index=0)
        st.session_state["text_model"] = TEXT_MODELS[text_label]

        # --- Image model ---
        image_label = st.selectbox("Image model", list(IMAGE_MODELS.keys()), index=0)
        st.session_state["image_model"] = IMAGE_MODELS[image_label]

        # --- Text generation ---
        st.session_state["temperature"] = st.slider("Temperature", 0.0, 1.5, 0.7, 0.1)

        # --- Speech / TTS ---
        st.subheader("🔊 Speech", divider="gray")
   
        st.session_state["speak_enabled"] = st.checkbox(
            "Enable speaking",
            value=st.session_state.get("speak_enabled", False),
        )

        if st.session_state["speak_enabled"]:
            # Gender selection
            gender = st.radio(
                "Voice gender",
                ["Female", "Male"],
                index=0 if st.session_state.get("tts_gender", "Female") == "Female" else 1,
                horizontal=True,
            )
            st.session_state["tts_gender"] = gender

            # Voice selection filtered by gender
            voices = TTS_VOICES[gender]
            voice = st.selectbox(
                "Voice",
                voices,
                index=voices.index(st.session_state.get("tts_voice", voices[0]))
                if st.session_state.get("tts_voice") in voices else 0,
            )
            st.session_state["tts_voice"] = voice

        else:
            # Defaults when disabled
            st.session_state.setdefault("tts_gender", "Female")
            st.session_state.setdefault("tts_voice", "alloy")
            st.session_state.setdefault("tts_format", "mp3")
