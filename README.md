# 🧠 DocuMind AI

An AI-powered document assistant built with Python, Streamlit and Google's Gemini API. Upload PDF documents to generate smart summaries and ask questions directly from their content.

## ✨ Features

- **Smart Summary:** Generates structured summaries of uploaded documents.
- **Document Q&A:** Ask questions and receive answers based on your PDF.
- **PDF Text Extraction:** Extracts text from uploaded PDF files.
- **Text Preview:** Preview extracted document content.
- **Document Information:** Displays document details such as page count and extracted text length.
- **Interactive UI:** Clean, custom-styled Streamlit interface.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyPDF
- python-dotenv

## ⚙️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/pushpakumawat695-web/DocuMind-AI.git
   ```

2. Navigate to the project folder:

   ```bash
   cd DocuMind-AI
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment (Windows):

   ```bash
   venv\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Create a `.env` file in the project directory and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

7. Run the application:

   ```bash
   streamlit run app.py
   ```

## 🔐 API Key

This project uses the Google Gemini API. A valid API key is required to use the AI features.

Never upload your API key or `.env` file to GitHub.

## 👩‍💻 Project

**DocuMind AI** — AI-Based PDF Document Assistant