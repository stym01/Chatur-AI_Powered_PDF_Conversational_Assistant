# 🧠 Chatur — AI-Powered PDF Conversational Assistant

**Chatur** is an intelligent assistant that lets you **converse with one or more PDF documents** using natural language. Built with **LangChain**, **FAISS**, and **Gemini Pro**, it allows users to upload documents and ask any question as if talking to a tutor, research assistant, or personal AI reader.

> Upload. Ask. Understand. 📄💬

---

## 🚀 Features

- 📂 Upload single or multiple PDFs
- 🔍 Ask questions in natural language
- 🧠 Uses LangChain + Gemini Pro with RAG (Retrieval-Augmented Generation)
- 📚 Summarizes, extracts info, and answers contextually
- 🌐 Simple Streamlit-based web interface

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **LLM**: Gemini Pro
- **Framework**: LangChain
- **Document Retrieval**: FAISS
- **PDF Parsing**: PyMuPDF (`fitz`)

---

## 📁 Project Structure

```
├── app.py              # Complete Streamlit application logic
├── requirements.txt    # Python package dependencies
├── .env                # Gemini API key environment variable
├── .gitignore          # Ignores .env and other sensitive files
├── README.md           # Project documentation
```

---

## 💻 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/stym01/Chatur-AI_Powered_PDF_Conversational_Assistant
cd Chatur-AI_Powered_PDF_Conversational_Assistant
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

> ✨ The app reads this key using the `os` module, so make sure to keep `.env` private and secure.

### 4️⃣ Run the App

```bash
streamlit run app.py
```

The app will launch in your browser. Upload PDFs and start chatting!

---

## 📸 Preview

Here’s what Chatur can do:

- Answer questions about academic papers
- Summarize long PDFs in simple terms
- Extract definitions, facts, and references
- Work with multiple PDFs at once
- Let you chat freely, not search blindly

---

## ✅ Example Questions

> “What’s the main idea of this document?”  
> “Summarize Section 3 in simple terms.”  
> “List all important terms or definitions.”  
> “What is the conclusion of the paper?”

---

## 🌟 Use Cases

- 👨‍🎓 **Students** — Get summaries and concept explanations from textbooks or notes  
- 🧪 **Researchers** — Understand dense academic papers faster  
- 📊 **Professionals** — Extract key points from reports, contracts, whitepapers  
- 📚 **Lifelong Learners** — Chat with any content-rich document

---

## 🛠️ Future Enhancements

- Add support for scanned/image PDFs using OCR
- Let users download chat history as text
- Enable saving/loadable PDF sessions
- Add GPT-4 and Claude as optional LLM backends

---

## 🤝 Contributing

Pull requests, feature suggestions, or improvements are welcome!  
If you find a bug or have an idea, open an issue or fork the repo.

---

## 📬 Contact

Have questions, feedback, or want to collaborate?

- GitHub: [@stym01](https://github.com/stym01)
- Email: [satyamkesharwani134@gmail.com](mailto:satyamkesharwani134@gmail.com)

---

## 🙌 Closing Note

Thank you for exploring Chatur! If it helped you or inspired your work, consider ⭐ starring the repo. Let’s make working with documents faster, smarter, and more human.
