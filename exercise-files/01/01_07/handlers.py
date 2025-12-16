import os
import base64
from pathlib import Path
import tempfile

import streamlit.components.v1 as components  # type: ignore
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -----------------------------------
# Text generation
# -----------------------------------
def generate_chat_completion(
    prompt: str,
    model: str = "gpt-4o-mini",
    temperature: float = 0.7,
) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content


# -----------------------------------
# Image generation
# -----------------------------------
def generate_image(
    prompt: str,
    model: str = "gpt-image-1",
    size: str = "1024x1024",
) -> bytes:
    result = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
    )

    image_base64 = result.data[0].b64_json
    return base64.b64decode(image_base64)


# -----------------------------------
# Audio API (TTS)
# -----------------------------------
def tts_to_mp3_file(
    text: str,
    output_dir: str = "tts",
    filename: str | None = None,
    tts_model: str = "gpt-4o-mini-tts",
    voice: str = "ash",
) -> str:
    if not text.strip():
        raise ValueError("No text to speak.")

    # Always use Path for path joins
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Choose output path
    if filename is None:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3", dir=str(out_dir))
        output_path = Path(tmp.name)
        tmp.close()
    else:
        output_path = out_dir / filename

    # Stream audio to file
    with client.audio.speech.with_streaming_response.create(
        model=tts_model,
        voice=voice,
        input=text[:4096],
        response_format="mp3",
        timeout=5.0,
    ) as response:
        response.stream_to_file(str(output_path))

    if output_path.stat().st_size == 0:
        raise RuntimeError("TTS output file is empty")

    return str(output_path)


def hidden_autoplay_audio(audio_bytes: bytes):
    b64 = base64.b64encode(audio_bytes).decode("utf-8")
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    components.html(audio_html, height=0, width=0)


def enable_audio_autoplay(response_text: str):
    mp3_path = tts_to_mp3_file(
        response_text,
        output_dir="tts",
        filename="reply.mp3",
    )
    with open(mp3_path, "rb") as f:
        audio_bytes = f.read()
    hidden_autoplay_audio(audio_bytes)
