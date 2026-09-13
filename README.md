# Agents From Scratch 🔁

Code reference for the **LoopLoopShip** series **Agents From Scratch** — build real AI agents, and prove they work. No frameworks, no hype.

> **LoopLoopShip** — build real tech, and actually ship it.
> ▶️ [Series playlist](#) · 🔁 [Subscribe](#)

## Why this exists

Most "AI agent" content stops at "look, it works once." This series is about building agents you can actually trust — which means learning to **measure** and **prove** they work (evals), not just demo them.

## Episodes

| # | Episode | Folder | What you build |
|---|---------|--------|----------------|
| 1 | What an AI Agent Actually Is (No Hype) | [`episode-1/`](./episode-1) | The smallest possible agent: an LLM + one tool + a loop |
| 2 | Tool Calling From Scratch | _coming soon_ | Multiple tools, good schemas, and why tool design makes agents fail |
| 3 | Your First Eval Harness ⭐ | _coming soon_ | Turn "it works" into a number that catches regressions |

## Quick start

```bash
cd episode-1
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # paste your OpenAI key (platform.openai.com/api-keys)
python 00_plain_llm.py    # the baseline (not an agent)
python agent.py           # the agent
```

## A note on secrets

There is **no `.env` in this repo** — only `.env.example`. Copy it to `.env` and add your own key. Your `.env` (and any virtualenv) is git-ignored and stays on your machine.

## Stack

Built with the **OpenAI API** (Python). The *concepts* are provider-agnostic — see the reading list in each episode's script.
