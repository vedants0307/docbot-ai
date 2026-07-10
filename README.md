# 🤖 DocBot AI

> An AI-powered Knowledge Base Assistant built using **Flask, LangChain, ChromaDB, PostgreSQL, and Google Gemini**. Upload documents, crawl websites, and chat with your own personalized knowledge base using Retrieval-Augmented Generation (RAG).

---

## 📖 Overview

DocBot AI enables users to build a custom AI-powered knowledge base by indexing PDFs, text documents, and websites. The application leverages semantic search with ChromaDB and LangChain to retrieve relevant information before generating responses using Google Gemini.

It features secure JWT authentication, PostgreSQL-backed metadata management, document indexing, website crawling, analytics, and a modern web interface.

---


## 📸 Application Preview

### Landing Page

![Landing Page](screenshots/landing-page.png)

---

### Login Page

![Login Page](screenshots/login-page.png)

---

### Dashboard

![Dashboard](screenshots/dashboard.png)

---

### Upload Documents

![Upload](screenshots/upload-page.png)

---

### Website Crawling

![Website](screenshots/website-crawler.png)

---

### AI Chatbot

![Chatbot](screenshots/chatbot.png)
## ✨ Features

### 🔐 Authentication
- User Registration
- User Login
- JWT Authentication
- BCrypt Password Hashing
- Protected Routes
- Personalized Dashboard Greeting

---

### 📄 Document Management
- Upload PDF Documents
- Upload TXT Files
- Automatic Text Extraction
- Smart Document Chunking
- Semantic Embedding Generation
- Duplicate Document Detection
- Automatic Re-indexing
- Delete Documents
- PostgreSQL Metadata Storage

---

### 🌐 Website Crawling
- Crawl Websites
- Extract Web Content
- Automatic Chunk Generation
- Website Indexing
- Global & Local Website Search

---

### 🤖 AI Chatbot
- Google Gemini Integration
- Retrieval Augmented Generation (RAG)
- Semantic Search using ChromaDB
- Global Knowledge Search
- Local Document Search
- Local Website Search
- Source Citation Support

---

### 📊 Dashboard
- Knowledge Base Overview
- Document Statistics
- Website Statistics
- Storage Information
- AI Model Information
- Personalized Welcome Message

---

### 🛠 Backend Features
- Flask Blueprints
- Modular Service Architecture
- PostgreSQL Integration
- Flask SQLAlchemy
- Flask Migrate
- ChromaDB Vector Database
- LangChain
- REST APIs

---

## 🏗 System Architecture

```
                     User

                       │

                       ▼

                JWT Authentication

                       │

                       ▼

        ┌─────────────────────────────┐
        │         Flask Backend        │
        └─────────────────────────────┘

        │             │             │

        ▼             ▼             ▼

 Upload PDFs     Crawl Website     Chat

        │             │

        ▼             ▼

 Document Loader   Web Crawler

        │             │

        ▼             ▼

      Text Chunking

             │

             ▼

   Embedding Generation

             │

             ▼

         ChromaDB

             │

             ▼

    Semantic Retrieval

             │

             ▼

      Prompt Construction

             │

             ▼

      Google Gemini AI

             │

             ▼

        Final Response
```

---

## 🛠 Tech Stack

### Backend

- Flask
- Python
- Flask SQLAlchemy
- Flask Migrate
- Flask JWT Extended
- Flask Bcrypt

### AI / RAG

- LangChain
- Google Gemini
- ChromaDB
- HuggingFace Embeddings

### Database

- PostgreSQL

### Frontend

- HTML
- CSS
- Bootstrap 5
- JavaScript

---

## 📂 Project Structure

```
docbot-ai/

│

├── app.py

├── config.py

├── extensions.py

│

├── models/

│   ├── document.py

│   └── user.py

│

├── routes/

│   ├── auth.py

│   ├── dashboard.py

│   ├── upload.py

│   ├── website.py

│   ├── sources.py

│   └── chat.py

│

├── services/

│   ├── analytics_service.py

│   ├── auth_service.py

│   ├── dashboard_service.py

│   ├── document_db_service.py

│   ├── document_service.py

│   ├── embedding_service.py

│   ├── llm_service.py

│   ├── prompt_service.py

│   ├── rag_service.py

│   ├── startup_service.py

│   ├── vector_store.py

│   └── website_service.py

│

├── templates/

│

├── static/

│

├── migrations/

│

├── requirements.txt

│

└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/docbot-ai.git

cd docbot-ai
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### PostgreSQL

Create database

```sql
CREATE DATABASE docbot_ai;
```

---

### Configure Environment Variables

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

DATABASE_URL=postgresql://username:password@localhost/docbot_ai

JWT_SECRET_KEY=your_secret_key
```

---

### Database Migration

```bash
flask db upgrade
```

---

### Run Application

```bash
python app.py
```

Application will start at

```
http://127.0.0.1:5000
```

---

## 💬 Workflow

```
Upload Documents

        ↓

Extract Text

        ↓

Chunk Documents

        ↓

Generate Embeddings

        ↓

Store in ChromaDB

        ↓

Ask Question

        ↓

Semantic Retrieval

        ↓

Relevant Context

        ↓

Google Gemini

        ↓

Final Response
```

---

## 🔒 Authentication Flow

```
Register

      ↓

BCrypt Password Hash

      ↓

Store User

      ↓

Login

      ↓

JWT Token

      ↓

Protected Routes

      ↓

Dashboard
```

---

## 📌 Current Features

- JWT Authentication
- BCrypt Password Hashing
- PostgreSQL Integration
- Flask SQLAlchemy
- Document Upload
- Website Crawling
- Semantic Search
- Global Search
- Local Search
- Google Gemini
- ChromaDB
- Analytics Dashboard
- Modern Authentication UI
- Duplicate Document Handling
- Source Citation Support

---

## 🔮 Future Enhancements

- Chat History
- Streaming AI Responses
- Source Preview Cards
- Drag & Drop Upload
- User Profile
- Dark Mode
- Export Chat
- Dashboard Charts
- Multi-user Knowledge Bases
- Cloud Deployment

---

## 👨‍💻 Author

**Vedant Prashant Shinde**

B.Tech Information Technology

Indian Institute of Information Technology, Allahabad

---

## 📄 License

This project is developed for educational and portfolio purposes.