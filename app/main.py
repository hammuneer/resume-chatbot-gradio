import gradio as gr
from app.chatbot import chat

def main():
    intro = """
    # Hamza Munir Resume Chatbot
    Welcome! This chatbot represents **Hamza Munir** and can answer questions related to his career, background, skills, and experience based on his LinkedIn profile.
    Please ask only professional or career-related questions.
    """

    with gr.Blocks() as demo:
        gr.Markdown(intro)
        gr.ChatInterface(
            fn=chat,
            type="messages",  # ✅ IMPORTANT for OpenAI-compatible role-based messages
            textbox=gr.Textbox(placeholder="Ask a question about Hamza's professional background")
            )
    
    demo.launch()

if __name__ == "__main__":
    main()
