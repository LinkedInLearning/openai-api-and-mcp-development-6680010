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