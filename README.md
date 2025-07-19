# 🎓 DPPify  
### *Generate beautiful Daily Practice Papers in one click*

---

## ✨ What is DPPify?
DPPify is a lightweight, open-source tool that instantly creates **Daily Practice Problem (DPP)** PDFs for any topic you choose.  
Pick a subject, set the difficulty, and let AI craft a balanced set of questions—ready to print or share with students.

---

## 🚀 Quick Start

1. **Clone & enter the repo**
   ```bash
   git clone https://github.com/your-org/DPPify.git
   cd DPPify
   ```

2. **Create & activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Generate your first DPP**  
   Open the browser tab that appears → enter your API key → choose topic & difficulty → click **Generate PDF**.

---

## 📦 Project Layout

```
DPP_creator/
├── backend/
│   ├── main_agent.py          # Agent orchestration
│   ├── functions/
│   │   └── metadata_to_pdf.py # PDF generation
│   └── prompts/
│       └── dpp_creater_system_prompt.txt
├── dpp_pdfs/                  # Generated PDFs (auto-created)
├── requirements.txt
├── README.md
└── streamlit_app.py           # Front-end
```

---

## 🔐 API Key
DPPify uses the **Cerebras Cloud SDK**. Grab your key from [cloud.cerebras.ai](https://cloud.cerebras.ai) and paste it in the sidebar when prompted.

---

## 🛠️ Tech Stack

| Stack       | Purpose               |
|-------------|------------------------|
| **Streamlit** | Web UI                |
| **Agno**      | Agent framework       |
| **Cerebras**  | LLM backend           |
| **markdown-pdf** | PDF generation   |
| **Pydantic**  | Structured outputs    |

---

## 🤝 Contribute
Found a bug or want to add features?  
Open an issue or send a pull request—contributions are welcome!

---

Made with ❤️ by the DPPify team.
