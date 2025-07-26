<h1 align="center">🎓 DPPify</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <a href="https://github.com/cyberytti/DPPify">
    <img src="https://img.shields.io/github/stars/cyberytti/DPPify?style=for-the-badge&logo=github&color=gold" alt="GitHub Stars">
  </a>
</p>

<p align="center">
  <b>Instantly generate beautiful Daily Practice Problem (DPP) PDFs on any topic with AI.</b>
</p>

<!-- Optional: Add a GIF of the app in action here -->
<!-- <p align="center">
  <img src="link_to_your_demo.gif" alt="DPPify Demo" width="800"/>
</p> -->

---

## ✨ Features
DPPify is a lightweight but powerful tool designed for students, teachers, and lifelong learners.

- ✨ **AI-Powered Content:** Leverages powerful LLMs to generate relevant, high-quality questions.
- 📚 **Any Topic, Any Subject:** From "Quantum Physics" to "Shakespearean Sonnets."
- 🎛️ **Total Customization:** Control the topic, difficulty (Easy, Medium, Hard), number of questions, and question types (MCQ, Short Answer, or a mix).
- 🌐 **Multi-Language Support:** Generate DPPs in English, Hindi, Bengali, and more.
- ✍️ **Natural Language Instructions:** Guide the AI with specific requests like "Focus on formulas" or "Include historical context."
- 📄 **Instant PDF Generation:** Get a clean, well-formatted PDF ready for printing or digital sharing in seconds.
- 🚀 **Simple & Fast UI:** Built with Streamlit for a seamless and intuitive user experience.

---

## 🚀 Quick Start

Follow these steps to get DPPify running on your local machine.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/cyberytti/DPPify
    cd DPPify
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Get Your API Key**
    DPPify uses the Cerebras AI platform. Get your free API key from [cloud.cerebras.ai](https://cloud.cerebras.ai).

5.  **Run the Streamlit App**
    ```bash
    streamlit run streamlit_app.py
    ```

6.  **Generate Your First DPP**
    Open the app in your browser, paste your API key into the sidebar, fill in your desired topic and settings, and click **"Generate My DPP PDF"**.

---

## ⚙️ How It Works
DPPify follows a simple yet effective agentic workflow:

1.  **Input:** The user provides the topic, difficulty, question type, and other parameters in the Streamlit UI.
2.  **Prompting:** The `DPPify` agent selects a specialized system prompt tailored to the requested question type (MCQ, SAQ, or both).
3.  **Generation:** `Agno` orchestrates a call to the Cerebras LLM, which generates the DPP content. `Pydantic` models ensure the AI's output is perfectly structured.
4.  **Formatting:** The structured data (topic, instructions, questions) is converted into a clean Markdown string.
5.  **PDF Creation:** The `markdown-pdf` library renders the final, polished PDF document, ready for download.

---

## 📦 Project Structure
The repository is organized to separate the front-end, back-end logic, and generated assets.

```
DPP_creator/
├── backend/
│   ├── functions/
│   │   └── metadata_to_pdf.py   # Converts structured data to a PDF
│   ├── prompts/
│   │   ├── only_mcq_creator_system_prompt.txt
│   │   ├── only_saq_creator_system_prompt.txt
│   │   └── both_questions_creater_system_prompt.txt
│   └── main_agent.py            # Core agent logic using Agno & Cerebras
├── dpp_pdfs/                    # Auto-created directory for generated PDFs
├── streamlit_app.py             # The Streamlit front-end
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Component         | Technology                               | Purpose                               |
|-------------------|------------------------------------------|---------------------------------------|
| **Web Framework** | **Streamlit**                            | Creating the interactive user interface. |
| **Agent Framework**| **Agno**                                 | Orchestrating the AI agent's workflow. |
| **LLM Backend**   | **Cerebras**                             | Generating the educational content.   |
| **PDF Generation**| **markdown-pdf**                         | Converting Markdown to a PDF document.|
| **Data Validation**| **Pydantic**                             | Enforcing a strict structure for AI outputs. |

---

## 🤝 Contributing
Contributions are welcome! Whether it's a bug fix, a new feature, or a UI improvement, feel free to open an issue or submit a pull request.

**Possible ideas for contribution:**
- Adding support for more output formats (e.g., `.docx`, `.txt`).
- Creating more specialized prompt templates for different subjects.
- Improving the visual styling of the generated PDFs.
- Adding a feature to include answer keys.

---

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/cyberytti">cyberytti</a>.
</p>
