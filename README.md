📚 StudyPal — AI-Powered Study Assistant

StudyPal is an AI-powered educational assistant designed to help Class 12 students learn, revise, and find useful study resources from one place.

The application combines Retrieval-Augmented Generation (RAG) with Groq-powered AI and YouTube video recommendations to provide students with chapter-specific answers and additional learning resources.

🔗 Live Application: StudyPal
✨ Features
🤖 AI Study Assistant

Ask questions related to your selected chapter and get answers based on the available study material.

📖 Chapter-Based Learning

StudyPal organizes learning material according to Class 12 subjects and chapters.

Currently available: Biology

Chemistry and Physics content are planned for future updates.

🔍 RAG-Based Question Answering

StudyPal uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the study material before generating an answer.

This helps the application provide responses that are grounded in the uploaded educational content rather than relying only on the language model's general knowledge.

🎥 YouTube Learning Resources

StudyPal also searches YouTube for relevant educational videos based on the selected chapter.

Students can use these recommendations for:

Concept explanation
Revision
One-shot lectures
Additional learning resources
⚡ Groq-Powered Responses

The application uses Groq's LLM API to generate fast AI responses.

🌐 Streamlit Web Application

The complete application is deployed using Streamlit, making it accessible directly through a web browser without requiring local installation.
🛠️ Tech Stack
Technology	Purpose
🐍 Python	Core programming language
🎈 Streamlit	Web application
🦜 LangChain	RAG and LLM pipeline
🔎 ChromaDB	Vector database
🤗 Hugging Face	Text embeddings
⚡ Groq	AI/LLM inference
▶️ YouTube Data API	Educational video search
📄 Unstructured	PDF/document processing
🔐 python-dotenv	Environment variable management

🧠 How StudyPal Works
                 ┌─────────────────────┐
                 │       Student       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Select Subject &    │
                 │      Chapter       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Ask a Question   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    RAG Pipeline    │
                 └──────────┬──────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
        ┌─────────────────┐   ┌─────────────────┐
        │ ChromaDB Vector │   │  Groq LLM       │
        │    Retrieval    │   │   Generation    │
        └────────┬────────┘   └────────┬────────┘
                 │                     │
                 └──────────┬──────────┘
                            ▼
                 ┌─────────────────────┐
                 │   AI Generated     │
                 │      Answer        │
                 └─────────────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ YouTube Resources  │
                 └─────────────────────┘

☁️ Deployment

StudyPal is deployed using Streamlit Community Cloud.

🔗 Live Demo: https://studypal-assistent.streamlit.app/

For deployment, API keys are stored securely using Streamlit Secrets rather than being included in the source code.                 

.

🔐 Environment Variables

The application uses the following environment variables:

Variable	       | Description
GROQ_API_KEY       | API key for Groq LLM
YOUTUBE_API_KEY    | API key for YouTube Data API
CLASS_SUBJECT_NAME |	Current subject path
DEVICE	           |Embedding model device, e.g. cpu

🎯 Project Goal

The goal of StudyPal is to create a simple and accessible AI-powered study companion that helps students:

Understand difficult concepts
Ask questions naturally
Find chapter-specific information
Discover useful educational videos
Learn from their study material more effectively