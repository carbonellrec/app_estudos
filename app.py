import streamlit as st
import os
import fitz  # PyMuPDF
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configuração do Modelo
model = genai.GenerativeModel('gemini-1.5-flash')

BASE_DIR = Path(__file__).resolve().parent
CONCURSOS_DIR = BASE_DIR / "concursos"

def extrair_texto_pdf(caminho_pdf):
    texto = ""
    with fitz.open(caminho_pdf) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

st.set_page_config(page_title="Mentor de Estudos", layout="wide")
st.title("🤖 Mentor IA: Edital & Materiais")

# BARRA LATERAL: Organização de Pastas
with st.sidebar:
    st.header("📂 Seus Materiais")
    concursos = [d.name for d in CONCURSOS_DIR.iterdir() if d.is_dir()]
    concurso_sel = st.selectbox("Concurso", ["---"] + concursos)
    
    arquivos_encontrados = []
    if concurso_sel != "---":
        path_pago = CONCURSOS_DIR / concurso_sel
        # Lista todos os PDFs dentro da pasta do concurso
        arquivos_encontrados = list(path_pago.glob("**/*.pdf"))
        st.write(f"📄 {len(arquivos_encontrados)} PDFs encontrados.")

# INTERFACE DE CHAT
if not arquivos_encontrados:
    st.info("💡 Dica: Crie uma pasta em 'concursos/' e jogue seus PDFs lá (Edital, Aulas, Questões).")
else:
    pergunta = st.chat_input("Ex: 'Baseado no Edital, o que é mais importante na Aula 01?'")
    
    if pergunta:
        with st.spinner("Analisando seus PDFs..."):
            # Lógica: Lê o conteúdo de todos os PDFs da pasta para dar contexto
            contexto_completo = ""
            for pdf in arquivos_encontrados:
                contexto_completo += f"\n--- ARQUIVO: {pdf.name} ---\n"
                contexto_completo += extrair_texto_pdf(pdf)
            
            # Envia para o Gemini
            prompt = f"Você é um mentor de concursos. Use o conteúdo abaixo para responder: \n\n{contexto_completo}\n\nPergunta do Fabiano: {pergunta}"
            response = model.generate_content(prompt)
            
            st.chat_message("assistant").write(response.text)
            