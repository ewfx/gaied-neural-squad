# 🚀 Project Name

Gen AI Orchestrator for Email and Document Triage/Routing 

---

## 🎯 Introduction
Developed a GenAI based Email Classification Solution to identify email request type, sub request type, intent, and extract important attributes. Also identifies whether the email is non-essential and can be ignored. The solution inludes a simple UI for users to upload emails and view responses.

## ⚙️ What It Does
Takes an email (.eml) file and identifies the request type, sub-request type, intent, and important attributes of the email. It also identifies whether the given email is essential or if it is non-essential and can be ignored.

## 🛠️ How We Built It
Frontend:
- HTML, CSS, JS
Backend:
- Python, FastAPI
LLMs: 
- mistralai/Mistral-7B-Instruct-v0.2 (https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
- google/gemma-3-27b-it (https://huggingface.co/google/gemma-3-27b-it)

## 🚧 Challenges We Faced
- Usage limit on Hugging Face LLM API free tier
- Unable to use models larger than 10GB with HuggingFace LLM API free tier
- Generating output in desired format by LLM

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/gaied-neural-squad.git
   ```
2. Install dependencies  
   ```sh
   pip install -r requirements.txt
   ```
3. Run the project  
   ```sh
   python app.py
   ```

## 🏗️ Tech Stack
- 🔹 Frontend: HTML,CSS,JS
- 🔹 Backend: Python, FastAPI 
- 🔹 LLM: LangChain, HuggingFace

## 👥 Team
- Laxmi Priya Guidvaka - [GitHub](https://github.com/Laxmi-Priya-Gudivaka-18) | [LinkedIn](https://www.linkedin.com/in/laxmi-priya-gudivaka-643754233)
- Samridh Anand Paatni - [GitHub](https://github.com/The5thAxiom) | [LinkedIn](https://www.linkedin.com/in/samridh-anand-paatni-57a045215/)
- Sneha Ann Reji - [GitHub](https://github.com/snehaannreji) | [LinkedIn](https://www.linkedin.com/in/sneha-ann-reji/)
- Apurva J Paul - [Github](https://github.com/Apurva-Jyoti-paul) | [LinkedIn](https://www.linkedin.com/in/apurva-jyoti-paul-9179b9202/?originalSubdomain=in)
