"""
Episode 1 - Step 1: A plain LLM call.

This is NOT an agent. It's a single request -> single response.
Ask it to look up an order and watch what happens: it has no way to actually
*do* anything, so it either refuses or makes something up. That gap is exactly
what Step 2 (agent.py) fixes.

Run it:  python 00_plain_llm.py
"""

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # reads OPENAI_API_KEY from your .env file

client = OpenAI()
MODEL = "gpt-4o"  # swap to "gpt-4o-mini" for cheaper/faster demo runs


def main():
    user_message = "Can you check the status of order A1001?"

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a support assistant for an online store."},
            {"role": "user", "content": user_message},
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
