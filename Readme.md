# First Agentic AI

This project is a minimal autonomous agent that can:
- Reason about a goal
- Choose actions
- Use tools
- Observe results
- Decide when to stop

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Set this in your .env file:
   OPENAI_API_KEY = "your_key_here"
   USE_FAKE_LLM=True // if you dont have the key and still want to test it 

3. Run the agent:
   python agent.py

## Example Tasks

- List all files and explain their purpose
- Read a log file and summarize errors
- Calculate a complex expression
