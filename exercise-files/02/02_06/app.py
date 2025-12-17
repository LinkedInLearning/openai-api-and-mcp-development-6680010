import streamlit as st # type: ignore
import openai
from dotenv import load_dotenv
from settings import setup_sidebar
from handlers import generate_image, downloadFile,  enable_audio_autoplay, moderate_text, flagged_categories
from utils import get_current_weather
import json

load_dotenv()
client = openai.OpenAI()

setup_sidebar()
voice_enabled = st.session_state.get("speak_enabled", False)    
st.markdown(
    """
    <style>
    h1 {
        color: #1f77b4;
        font-size: 3rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 0.5em;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("⛅ What's the Weather like?")


# Constants
MODEL_ENGINE = "gpt-3.5-turbo"
MODEL_ENGINE_1106 = "gpt-3.5-turbo-1106"
messages = [{"role": "system", "content": "You are a helpful assistant. you can use tools to help you answer questions. and add emojis to your answers when asked about weather forecast. match the emoji with the weather conditions for a given city"}]


def generate_response_using_tools(user_input):
    messages.append({"role": "user", "content": user_input})

    resp = client.chat.completions.create(
        model=MODEL_ENGINE_1106,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    msg = resp.choices[0].message

    # IMPORTANT: content may be None when tool_calls are present
    messages.append({
        "role": msg.role,
        "content": msg.content or "",
        "tool_calls": msg.tool_calls,  # keep tool calls if any
    })

    return msg

def generate_response():
    response = client.chat.completions.create(
        model=MODEL_ENGINE,
        messages=messages,
    )
    msg = response.choices[0].message
    messages.append(msg)
    return msg.content


# Tools and Functions
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    }
]


available_functions = {
    "get_current_weather": get_current_weather,
}  # only one function in this example, but you can have multiple


def call_function(tool_calls):
    if tool_calls:
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response
            
            return function_args   


# -----------------------------------
#  Application & Weather App
# -----------------------------------
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type something")
    send = st.form_submit_button("Send")

if send and user_input:
    user_mod = moderate_text(user_input)
    if user_mod["flagged"]:
        st.error(
        f"⚠️ Your message was flagged by moderation: "
        f"{', '.join(flagged_categories(user_mod['categories']))}"
        )
        st.stop()
    messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."): 
        # Step 1: ask and generate response from LLM
        response = generate_response_using_tools(user_input)
          
        # Step 2: check if GPT wanted to call a function and generate an extended response
        if response.tool_calls is None:
            st.write(response)
            
        # Step 3: call the function
        function_args = call_function(response.tool_calls)
        
        print(function_args)
        
        # Step 4: send json and get a new response from LLM extend conversation with assistant's reply
        extended_response = generate_response()
        image = generate_image(f"generate png image from the following description: {extended_response} with postal card style of the given {function_args.get('location')}, do not crop the image, add margins around the image and a white border")
        if extended_response:
            st.write(extended_response)
            st.image(image, caption=extended_response)
            downloadFile(location=function_args.get("location"), image=image)
            if voice_enabled:
                enable_audio_autoplay(extended_response)