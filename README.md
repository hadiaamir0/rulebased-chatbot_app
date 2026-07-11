# Rule-Based AI Chatbot

A simple rule-based chatbot built as **Project 1** of the DecodeLabs AI Engineering Industrial Training Kit (Batch 2026). It demonstrates the foundational logic behind conversational AI — control flow, input sanitization, and deterministic decision-making — before moving on to probabilistic/generative models.

Available in two forms:
- A **terminal (console)** version
- A **Streamlit web app** version

Both share the same core logic, so responses are identical across both interfaces.

## Features

- Continuous input loop that keeps the conversation going until the user exits
- Input sanitization (case-insensitive, whitespace-trimmed) for reliable matching
- Dictionary-based knowledge base for O(1) intent lookup instead of long if-elif chains
- Graceful fallback response for unrecognized input
- Clean exit on `bye`, `exit`, or `quit`


## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/) (only required for the web version)






## Available Commands

| Input                  | Response                                                                 |
|-------------------------|---------------------------------------------------------------------------|
| `hello` / `hi`          | Greeting                                                                   |
| `how are you`           | Status reply                                                              |
| `what is your name`     | Chatbot introduces itself                                                 |
| `what can you do`       | Lists its capabilities                                                    |
| `help`                  | Lists all available commands                                              |
| `thank you` / `thanks`  | Acknowledgement                                                            |
| `bye` / `exit` / `quit` | Ends the conversation                                                     |
| *(anything else)*       | Fallback message prompting the user to type `help`                        |


## Possible Extensions

- Add more intents/responses to `chatbot_logic.py`
- Support partial or fuzzy matching instead of exact matches
- Add persistent chat history across sessions
- Swap the rule-based fallback for an LLM call to handle unrecognized input




