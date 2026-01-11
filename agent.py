import json
from openai import OpenAI
from tools import TOOLS
from prompt import SYSTEM_PROMPT
from fake_responses import fake_llm_response  
from dotenv import load_dotenv
import os

load_dotenv(".env.development")

USE_FAKE_LLM = os.getenv("USE_FAKE_LLM", "false").lower() == "true"

USE_REAL_LLM = bool(os.getenv("OPENAI_API_KEY")) and not USE_FAKE_LLM

client = OpenAI() if USE_REAL_LLM else None

MAX_STEPS = 3

def run_agent(goal):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Goal: {goal}"}
    ]

    step = 0

    while step < MAX_STEPS:
        step += 1
        print(f"\n🔁 STEP {step}/{MAX_STEPS}")

        if USE_REAL_LLM:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages,
                temperature=0
            )
            reply = response.choices[0].message.content
        else:
            reply = json.dumps(fake_llm_response(messages))

        print("\nRAW AGENT OUTPUT:\n", reply)

        try:
            data = json.loads(reply)
        except json.JSONDecodeError:
            print("❌ Invalid JSON from agent. Stopping.")
            return

        thought = data.get("thought")
        action = data.get("action")
        action_input = data.get("action_input", "")

        print("🧠 THOUGHT:", thought)
        print("⚙️ ACTION:", action)

        if action == "finish":
            print("\n✅ FINAL ANSWER:\n", action_input)
            return

        if action in TOOLS:
                result = TOOLS[action](action_input)
        else:
            result = f"Unknown action: {action}"

        messages.append({"role": "assistant", "content": reply})
        messages.append({
            "role": "user",
            "content": f"Observation: {result}"
        })
        
        print("\n✅ message:\n", messages)


    # If loop exits due to max steps
    print("\n⛔ MAX STEPS REACHED")
    print("Agent stopped after 3 attempts without finishing.")


if __name__ == "__main__":
    goal = input("Enter your task: ")
    run_agent(goal)
