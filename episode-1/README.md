# Agents From Scratch — Episode 1: What an AI Agent Actually Is (No Hype)

The smallest possible AI agent, built from scratch in ~60 lines with **zero frameworks**.

By the end you'll know exactly what separates an *agent* from a plain chatbot — and you'll have run one yourself.

> **LoopLoopShip** — build real tech, and actually ship it.
> Season 1: **Agents From Scratch** — build real agents, and prove they work.
> → [watch the video](#) · [series playlist](#) · [🔁 subscribe](#)

## The one-line definition

> An **agent** is an LLM in a **loop** that can **take actions** (tools) and **decide when it's done.**

If you hardcode the steps, it's a *workflow*. If the model decides — that's an agent.

## What's in here

| File | What it is |
|------|-----------|
| `00_plain_llm.py` | A plain LLM call. **Not** an agent — it can't *do* anything. The baseline. |
| `agent.py` | The real thing: an LLM + one tool + a loop. This is the whole idea. |

## Setup

```bash
# 1. clone + enter
git clone <this-repo> && cd episode-1

# 2. install
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. add your key
cp .env.example .env      # then paste your key from platform.openai.com/api-keys
```

## Run it

```bash
python 00_plain_llm.py    # the baseline — watch it fail to actually look anything up
python agent.py           # the agent — watch it call the tool, then answer
```

You'll see the agent print `[tool] lookup_order(...)` when it decides to use the tool — and answer directly when it doesn't. That decision is the whole point.

## Where this goes next

- **Episode 2** — Tool calling from scratch: multiple tools, good schemas, and why *tool design* is what makes agents fail.
- **Episode 3** — Your first eval harness: turn "it works" into a number that catches regressions.

The same support-agent codebase grows across the series, so clone once and follow along.

## Model note

Built with the **OpenAI API** (function calling). The code defaults to `gpt-4o`. For cheaper/faster runs while experimenting, swap the `MODEL` line to `gpt-4o-mini`.
