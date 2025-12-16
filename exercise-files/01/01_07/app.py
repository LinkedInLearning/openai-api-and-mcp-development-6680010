import streamlit as st
from handlers import generate_chat_completion, generate_image
from settings import setup_sidebar

st.title("🤖 Chatbot App")

setup_sidebar()

st.caption(
    f"🧠 Text: `{st.session_state.get('text_model','gpt-4o-mini')}` · "
    f"🖼️ Image: `{st.session_state.get('image_model','gpt-image-1')}` · "
    f"🌡️ Temp: `{st.session_state.get('temperature',0.7)}`"
)

tab_chat, tab_image = st.tabs(["💬 Text", "🖼️ Image"])

with tab_chat:
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Type something")
        send = st.form_submit_button("Send")
        
    if send and user_input:
        with st.spinner("Thinking..."):
            completion = generate_chat_completion(
                user_input,
                model=st.session_state["text_model"],
                temperature=st.session_state["temperature"],
            )
        st.write(completion)


with tab_image:
    with st.form("image_form", clear_on_submit=True):
        gen = st.form_submit_button("Generate image")
        user_input = st.text_input("Type something")

    if gen and user_input:
        with st.spinner("Generating..."):
            # Your generate_image() should return either a PIL image, bytes, or base64 -> adapt accordingly
            img = generate_image(user_input, model=st.session_state["image_model"])
            st.image(img, caption=user_input, width='content')
       