import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Carrega a Bíblia
with open("data/biblia_arc.json", "r", encoding="utf-8") as f:
    biblia = json.load(f)

# Modelo multilíngue (bom em português)
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Textos para embedding
textos = [
    f"{v['livro']} {v['capitulo']}:{v['versiculo']} {v['texto']}"
    for v in biblia
]

print("Gerando embeddings...")
embeddings = model.encode(
    textos,
    batch_size=32,
    show_progress_bar=True
)

# Converte para float32 (FAISS exige)
embeddings = np.array(embeddings).astype("float32")

# Cria índice FAISS
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Salva índice
faiss.write_index(index, "rag/biblia.index")

# Salva metadados
with open("rag/biblia_meta.json", "w", encoding="utf-8") as f:
    json.dump(biblia, f, ensure_ascii=False, indent=2)

print("Embeddings gerados e índice salvo.")
