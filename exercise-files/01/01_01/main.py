from dotenv import load_dotenv
from openai import OpenAI  # type: ignore
from colorama import Fore
import base64

from rich.console import Console  # type: ignore
from rich.pretty import pprint

load_dotenv()

client = OpenAI()
console = Console()
console.rule("[bold green]Generating Content with Responses[/bold green]")

response = client.responses.create(
    model="gpt-3.5-turbo",
    input="Write a two-sentence horror story about a haunted house.", 
    temperature=0.9,
)

print(response.output_text)


response = client.images.generate(
    model="dall-e-3",        
    prompt=response.output[0].content[0].text,
    n=1,
    size="1024x1024",
    response_format="b64_json",  # <-- REQUIRED if you want base64 data
)

pprint(response)

img = response.data[0]


if img.b64_json:
    image_bytes = base64.b64decode(img.b64_json)
    with open("image.png", "wb") as f:
        f.write(image_bytes)

    console.print(Fore.GREEN + "Image saved as image.png")
else:
    console.print(Fore.RED + "No base64 data in response. Try checking response_format or use img.url instead.")
