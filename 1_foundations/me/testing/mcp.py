import gradio as gr
import os
from typing import List, Tuple
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file (same as in 1_lab1.ipynb)
load_dotenv(override=True)

# Initialize OpenAI client (same pattern as in 1_lab1.ipynb)
openai = OpenAI()

def chat_with_openai(message: str, history: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[str, str]]]:
    """
    Send a message to OpenAI and return the response along with updated history.
    """
    try:
        # Convert gradio history format to OpenAI messages format
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        
        # Add conversation history
        for user_msg, assistant_msg in history:
            if user_msg:
                messages.append({"role": "user", "content": user_msg})
            if assistant_msg:
                messages.append({"role": "assistant", "content": assistant_msg})
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        # Call OpenAI API
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Using standard OpenAI model name
            messages=messages,
            max_tokens=1000,
            temperature=0.7
        )
        
        assistant_response = response.choices[0].message.content
        
        # Update history
        history.append((message, assistant_response))
        
        return "", history
        
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        history.append((message, error_msg))
        return "", history

def clear_chat():
    """Clear the chat history."""
    return [], []

# Create Gradio interface
with gr.Blocks(title="OpenAI Chat Tester") as demo:
    gr.Markdown("# OpenAI Chat Tester")
    gr.Markdown("Simple interface to test OpenAI API endpoints")
    
    # Check if API key is set (same pattern as in 1_lab1.ipynb)
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        gr.Markdown("⚠️ **Warning:** OPENAI_API_KEY not set - please head to the troubleshooting guide in the setup folder")
    else:
        gr.Markdown(f"✅ **OpenAI API Key loaded and begins:** {openai_api_key[:8]}")
    
    chatbot = gr.Chatbot(
        value=[],
        elem_id="chatbot",
        bubble_full_width=False,
        height=400
    )
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message here...",
            container=False,
            scale=4
        )
        send_btn = gr.Button("Send", scale=1)
    
    with gr.Row():
        clear_btn = gr.Button("Clear Chat")
    
    # Event handlers
    msg.submit(chat_with_openai, [msg, chatbot], [msg, chatbot])
    send_btn.click(chat_with_openai, [msg, chatbot], [msg, chatbot])
    clear_btn.click(clear_chat, [], [chatbot, msg])

if __name__ == "__main__":
    # Check API key before starting (same pattern as in 1_lab1.ipynb)
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    if openai_api_key:
        print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
        print("Starting OpenAI Chat Tester...")
    else:
        print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")
        print("Starting anyway...")
    
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )
