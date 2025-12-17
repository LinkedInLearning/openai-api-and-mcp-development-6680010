import os
import dotenv
from colorama import Fore, Style

from openai import OpenAI

dotenv.load_dotenv()


token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"


SYSTEM_MESSAGE = "You are a helpful assistant that can answer queries based on your knowledge. If you don't know an answer, say 'I don\n't know'"
# Get GitHub token from environment variable
github_token = os.getenv("GITHUB_TOKEN")
if not github_token:
    raise ValueError(
        "GITHUB_TOKEN environment variable is not set. "
        "Please set it with: export GITHUB_TOKEN='your_token_here'"
    )

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

messages = [{
    "role": "system",
    
    "content": ("You are a helpful assistant that can answer queries based on your knowledge. If you don't know an answer, say 'I don't know'"),
}]

def main():
    print(Style.BRIGHT + "//==============*****AI Assistant*****===============//" + Style.RESET_ALL)
    print(Fore.CYAN +  "\n-Taper votre question\n–Taper 'quit' pour sortir.\n" + Style.RESET_ALL)
     
    while True:
        user_input = input("Vous: ")

        if user_input.lower() in ("quit", "exit", "q"):
            print(Style.BRIGHT + Fore.CYAN + "Assistant: À bientôt 👋" + Style.RESET_ALL)
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "",
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            temperature=1,
            top_p=1,
            model=model
            )

            print(Style.BRIGHT + Fore.GREEN + response.choices[0].message.content+ Style.RESET_ALL)
     
        except Exception as e:
            print(e)
            continue
    
if __name__ == "__main__":
    main()