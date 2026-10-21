from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Avia AI Document Processor",
    description="API para processamento e resumo automatizado de documentos com IA",
    version="1.0.0"
)

class DocumentRequest(BaseModel):
    title: str
    content: str
    max_summary_length: Optional[int] = 150

class DocumentResponse(BaseModel):
    title: str
    summary: str
    key_topics: List[str]
    word_count: int

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "Avia AI Processor"}

@app.post("/summarize", response_model=DocumentResponse)
def summarize_document(doc: DocumentRequest):
    if not doc.content.strip():
        raise HTTPException(status_code=400, detail="O conteúdo do documento não pode estar vazio.")
    
    words = doc.content.split()
    word_count = len(words)
    
    # Simulação de processamento de IA
    summary = " ".join(words[:min(30, word_count)]) + "..."
    topics = list(set([w.strip(".,").capitalize() for w in words if len(w) > 6]))[:5]
    
    return DocumentResponse(
        title=doc.title,
        summary=summary,
        key_topics=topics,
        word_count=word_count
    )
