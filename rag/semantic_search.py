from sentence_transformers import SentenceTransformer, util
from pipeline.biblia import carregar_biblia

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def buscar_versiculos_semanticos(pergunta, limite=3):
    biblia = carregar_biblia()

    textos = [item["texto"] for item in biblia]
    embeddings = model.encode(textos, convert_to_tensor=True)

    emb_pergunta = model.encode(pergunta, convert_to_tensor=True)
    scores = util.cos_sim(emb_pergunta, embeddings)[0]

    top_indices = scores.topk(limite).indices.tolist()

    resultados = []
    for idx in top_indices:
        item = biblia[idx]
        ref = f"{item['livro']} {item['capitulo']}:{item['versiculo']}"
        resultados.append((ref, item["texto"]))

    return resultados
