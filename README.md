# 🤖 Mentor IA: Edital & Materiais

Este é um assistente de estudos inteligente desenvolvido em **Python**. O objetivo é ajudar concurseiros e estudantes a analisarem editais e materiais didáticos de forma rápida usando IA.

## 🚀 Funcionalidades
* **Análise de PDF:** Extração automática de texto de múltiplos arquivos.
* **Chat Inteligente:** Integração com a API do **Google Gemini** para responder perguntas baseadas no conteúdo dos documentos.
* **Organização por Pastas:** Sistema que separa os materiais por concurso ou disciplina.

## 🛠 Tecnologias
* **Python** (Lógica principal)
* **Streamlit** (Interface Web)
* **Google Gemini API** (Inteligência Artificial)
* **PyMuPDF** (Manipulação de PDFs)

## 📖 Como usar
1. Clone o repositório.
2. Crie um arquivo `.env` com sua `GEMINI_API_KEY`.
3. Coloque seus PDFs na pasta `concursos/`.
4. Execute: `streamlit run main.py`
