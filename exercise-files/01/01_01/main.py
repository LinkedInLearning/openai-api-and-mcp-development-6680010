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
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

pprint(response)