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



## Usage

### Terminal version

```bash
python chatbot.py
```

Example session:

```
Chatbot: Hello! Type 'bye' or 'exit' to end the chat.
You: hello
Chatbot: Hi there! How can I help you today?
You: bye
Chatbot: Goodbye! Have a great day.
```

### Web version (Streamlit)

```bash
streamlit run chatbot_app.py
```


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

## How It Works

1. **Input** — Raw user text is captured from the terminal or the Streamlit chat box.
2. **Sanitization** — Input is lowercased and stripped of extra whitespace so `"Hello"`, `" hello "`, and `"HELLO"` all match the same rule.
3. **Lookup** — The cleaned input is checked against a dictionary of known intents using `.get()`, which handles both the match and the fallback in a single step.
4. **Output** — The matched (or fallback) response is printed to the console or rendered as a chat bubble.

This "dictionary lookup" approach scales better than a long `if-elif` chain: lookups stay fast (O(1)) even as more rules are added, whereas an `if-elif` ladder gets slower and harder to maintain as it grows.

## Possible Extensions

- Add more intents/responses to `chatbot_logic.py`
- Support partial or fuzzy matching instead of exact matches
- Add persistent chat history across sessions
- Swap the rule-based fallback for an LLM call to handle unrecognized input




