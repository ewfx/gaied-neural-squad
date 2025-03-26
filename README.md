# 🚀 Project Name

GenAI Email Classification 

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
This project is to classify Service Requests emails based on Request Type and to identify which emails can be ignored. This solution utilizes LLMs to classify emails.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## ⚙️ What It Does
Takes an email (.eml) file and identifies the request type, sub-request type, intent, and important attributes of the email. It also identifies whether the given email is essential or if it is non-essential and can be ignored.

## 🛠️ How We Built It
LLMs: 
- mistralai/Mistral-7B-Instruct-v0.2 (https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
- google/gemma-3-27b-it (https://huggingface.co/google/gemma-3-27b-it)

## 🚧 Challenges We Faced
- Usage limit on Hugging Face LLM API
- Unable to use models larger than 10GB with HuggingFace LLM API
- Generating output in desired format by LLM

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/your-repo.git
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
- 🔹 Frontend: HTML/CSS
- 🔹 Backend: FastAPI 
- 🔹 LLM: LangChain, HuggingFace

## 👥 Team
- Laxmi Priya Guidvaka - [GitHub](#) | [LinkedIn](#)
- Sneha Ann Reji - [GitHub](#) | [LinkedIn](#)
- Apurva J Paul - 
- Samridh Anand Paatni - [GitHub](https://github.com/The5thAxiom) | [LinkedIn](https://www.linkedin.com/in/samridh-anand-paatni-57a045215/)
