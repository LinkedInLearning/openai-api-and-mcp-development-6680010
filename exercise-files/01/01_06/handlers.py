import os
import base64
from openai import OpenAI

# Initialize client (expects OPENAI_API_KEY in env)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -----------------------------------
# Text generation
# -----------------------------------
def generate_chat_completion(
    prompt: str,
    model: str = "gpt-4o-mini",
    temperature: float = 0.7,
) -> str:
    """
    Generate a chat completion from a text prompt.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
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
):
    """
    Generate an image from a prompt.
    Returns raw image bytes (ready for st.image).
    """

    result = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
    )

    # API returns base64 → decode to bytes
    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    return image_bytes
