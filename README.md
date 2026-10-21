# Avia AI Document Processor 🚀

Microserviço em FastAPI desenvolvido para resumo automático de textos, extração de palavras-chave e análise de sentimento com apoio de Inteligência Artificial.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- **NLTK / AI Mock Engine**

## 📋 Funcionalidades
- `POST /summarize`: Recebe documentos de texto e gera resumos estruturados com extração de tópicos principais.
- `GET /health`: Endpoint de verificação de integridade do serviço.

## 🔧 Como Executar Localmente
```bash
# Clonar o repositório
git clone [https://github.com/Denilson1000/avia-ai-document-processor.git](https://github.com/Denilson1000/avia-ai-document-processor.git)

# Instalar dependências
pip install -r requirements.txt

# Executar a aplicação
uvicorn app.main:app --reload
