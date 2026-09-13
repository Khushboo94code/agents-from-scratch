"""
Episode 1 - Step 2: The smallest possible AI agent.

An agent = an LLM in a LOOP that can (1) call tools and (2) decide when it's done.
That's it. ~70 lines, zero frameworks - just the OpenAI SDK.

Run it:  python agent.py
"""

import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
MODEL = "gpt-4o"  # swap to "gpt-4o-mini" for cheaper/faster demo runs


# --- 1. A fake "database" so our tool has something real to return ---
ORDERS = {
    "A1001": {"status": "shipped", "eta": "2 days", "item": "Blue running shoes"},
    "A1002": {"status": "processing", "eta": "5 days", "item": "Wireless earbuds"},
}


# --- 2. The tool implementation: just a normal Python function ---
def lookup_order(order_id: str) -> str:
    order = ORDERS.get(order_id.upper())
    if order is None:
        return f"No order found with id {order_id}."
    return json.dumps(order)


# --- 3. The tool DESCRIPTION. This is a prompt for the model - write it well.
#        The model reads this to decide *when* and *how* to call the tool. ---
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_order",
            "description": (
                "Look up the status of a customer order by its ID. "
                "Use this whenever the user asks about an order."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The order ID, e.g. A1001",
                    }
                },
                "required": ["order_id"],
            },
        },
    }
]


def run_tool(name: str, tool_input: dict) -> str:
    """Dispatch a tool call to the matching Python function."""
    if name == "lookup_order":
        return lookup_order(**tool_input)
    return f"Unknown tool: {name}"


# --- 4. THE AGENT LOOP - this is the whole idea ---
def run_agent(user_message: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a support assistant for an online store. "
                "Use tools to look things up instead of guessing."
            ),
        },
        {"role": "user", "content": user_message},
    ]

    while True:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
        )
        message = response.choices[0].message

        # No tool calls -> the model answered directly. We're DONE.
        if not message.tool_calls:
            return message.content

        # Otherwise: record the model's turn (it MUST include the tool_calls)...
        messages.append(message)

        # ...run each requested tool and hand the result back...
        for tool_call in message.tool_calls:
            args = json.loads(tool_call.function.arguments)
            print(f"  [tool] {tool_call.function.name}({args})")
            result = run_tool(tool_call.function.name, args)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,  # must match the tool_call's id
                "content": result,
            })

        # ...then loop again so the model can use the results.


if __name__ == "__main__":
    questions = [
        "Hi! Can you check on order A1001?",   # needs the tool
        "What's the weather in Tokyo?",         # no tool for this - watch it just answer
    ]
    for q in questions:
        print(f"\nUser:  {q}")
        print(f"Agent: {run_agent(q)}")
