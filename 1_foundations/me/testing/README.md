# OpenAI Chat Tester

A simple Gradio frontend for testing OpenAI API endpoints.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Running the App

```bash
python mcp.py
```

The app will launch on `http://localhost:7860`

## Features

- Simple chat interface
- Conversation history
- Clear chat functionality
- Error handling for API issues
- Uses GPT-3.5-turbo by default

## Notes

- The app will warn you if the API key is not set
- All errors are displayed in the chat interface
- The conversation history is maintained during the session
