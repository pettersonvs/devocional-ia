import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Carrega metadados
with open("rag/biblia_meta.json", "r", encoding="utf-8") as f:
    biblia = json.load(f)

# Carrega índice FAISS
index = faiss.read_index("rag/biblia.index")

# Modelo (o mesmo usado nos embeddings)
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def buscar_versiculos(pergunta, top_k=3):
    # Cria embedding da pergunta
    query_embedding = model.encode([pergunta])
    query_embedding = np.array(query_embedding).astype("float32")

    # Busca no FAISS
    distances, indices = index.search(query_embedding, top_k)

    resultados = []
    for idx in indices[0]:
        versiculo = biblia[idx]
        resultados.append(versiculo)

    return resultados


if __name__ == "__main__":
    pergunta = input("Pergunta: ")
    resultados = buscar_versiculos(pergunta)

    print("\nVersículos encontrados:\n")
    for v in resultados:
        print(f"{v['livro']} {v['capitulo']}:{v['versiculo']}")
        print(v['texto'])
        print("-" * 40)
