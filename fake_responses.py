def fake_llm_response(messages):
    last_user_message = messages[-1]["content"]

    # VERY basic rule-based behavior (for testing)
    if "list" in last_user_message.lower():
        return {
            "thought": "I should list files to understand the project",
            "action": "list_files",
            "action_input": ""
        }

    if "calculate" in last_user_message.lower():
        return {
            "thought": "This is a math task",
            "action": "calculate",
            "action_input": "25 * 4 + 18"
        }

    if "read" in last_user_message.lower():
        return {
            "thought": "I need to read the specified file",
            "action": "read_file",
            "action_input": "README.md"
        }

    return {
        "thought": "Task seems complete",
        "action": "finish",
        "action_input": "Task completed using fake LLM."
    }
