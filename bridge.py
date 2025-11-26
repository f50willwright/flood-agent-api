
from openai import OpenAI
from openai.types.chat import (
    ChatCompletionUserMessageParam,
    ChatCompletionToolParam,
    ChatCompletionNamedToolChoiceParam
)

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# Define the tool
tools = [
    ChatCompletionToolParam(
        type="function",
        function={
            "name": "get_flood_report",
            "description": "Fetches a flood report for a given latitude and longitude.",
            "parameters": {
                "type": "object",
                "properties": {
                    "lat": {"type": "number"},
                    "lon": {"type": "number"},
                    "usgs_site_id": {"type": "string"}
                },
                "required": ["lat", "lon"]
            }
        }
    )
]

# Define messages
messages = [
    ChatCompletionUserMessageParam(
        role="user",
        content="Generate a flood report for lat 44.4759 and lon -73.2121"
    )
]

# Force tool call using typed param
tool_choice = ChatCompletionNamedToolChoiceParam(
    type="function",
    function={"name": "get_flood_report"}
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice=tool_choice
)

message = completion.choices[0].message

if message.tool_calls and len(message.tool_calls) > 0:
    function_call = message.tool_calls[0]
    print("Tool call detected:", function_call)
    print("Function name:", function_call.function.name)
    print("Arguments:", function_call.function.arguments)
else:
    print("No tool call detected. Model response:", message.content)
