# Hamza Resume Chatbot 🤖

This is an interactive, AI-powered chatbot that represents **Hamza Munir**. It can answer questions about Hamza's career, experience, background, and professional skills. The bot is built using **Gradio**, **OpenAI GPT-4o**, and streams responses in real-time.

## 🚀 Features

- ✅ Streams GPT-4o responses in real-time
- ✅ Answers based on Hamza's LinkedIn and resume
- ✅ Professional tone, accurate context
- ✅ Rejects off-topic or irrelevant queries
- ✅ Built with modular, clean Python architecture

## 🛠️ Tech Stack

- [Gradio](https://gradio.app) – for the UI
- [OpenAI API](https://platform.openai.com/) – for GPT responses
- [Python](https://www.python.org) – backend logic
- `dotenv`, `pypdf`, `pydantic` – utility libraries

## 📂 Project Structure
```bash
hamza-resume-chatbot/
├── app/
│ ├── chatbot.py # Main chat + streaming logic
│ ├── evaluator.py # Optional: response evaluation
│ ├── prompts.py # System prompts and context
│ ├── utils.py # Resume/LinkedIn text parsing
│ ├── models.py # Pydantic models
│ └── main.py # Launches Gradio app
├── me/
│ ├── HamzaProfile.pdf # Resume file
│ └── hamza_summary.txt # (optional) career summary
├── .env # Stores OpenAI API key
└── requirements.txt # Dependencies
```

## 🔧 Setup Instructions

1. Clone the repo:
```bash
   git clone https://github.com/your-username/hamza-resume-chatbot.git
   cd hamza-resume-chatbot
```


2. Create .env with your OpenAI key:
```bash
    OPENAI_API_KEY=your_openai_api_key_here
```


3. Install dependencies:
```bash
    pip install -r requirements.txt
```


4. Run the app:

```bash
    python -m app.main
```
Then visit: http://127.0.0.1:7860


## 🤖 Example Prompts
- “What are Hamza’s core skills?”
- “Does Hamza have experience with AI?”
- “Tell me about his work background.”

## 📌 Notes
- All answers are generated **in character as Hamza**, based on resume and profile data.
- Off-topic or unrelated questions are politely rejected.
 

## 📜 License
This project is licensed under the MIT License.

