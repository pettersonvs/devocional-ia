import json
import os

CAMINHO_BIBLIA = os.path.join("data", "biblia_arc.json")

# Livros priorizados para cuidado pastoral
LIVROS_PRIORITARIOS = [
    "Salmos",
    "Provérbios",
    "Isaías",
    "Mateus",
    "Marcos",
    "Lucas",
    "João",
    "Romanos",
    "Filipenses",
    "Hebreus"
]

TEMAS = {
    "ansiedade": ["ansioso", "ansiedade", "medo", "aflição", "coração", "paz"],
    "medo": ["medo", "temor", "assombro", "pavor"],
    "tristeza": ["triste", "choro", "lamento", "angústia"],
    "fé": ["fé", "confiança", "esperança", "crer"],
}

PALAVRAS_NEGATIVAS = [
    "maldade",
    "castigo",
    "ira",
    "juízo",
    "destruição",
    "arrependeu-se"
]

FALLBACK = [
    "Salmos 23:1 — O Senhor é o meu pastor; nada me faltará.",
    "Filipenses 4:6-7 — Não andeis ansiosos por coisa alguma, mas em tudo, pela oração..."
]

PALAVRAS_EXCLUDENTES = [
    "ímpios",
    "adversários",
    "inimigos",
    "mal",
    "iniquidade",
    "castigo"
]

PALAVRAS_POSITIVAS = [
    "senhor",
    "confiança",
    "descanso",
    "guardar",
    "refúgio",
    "paz"
]


def carregar_biblia():
    with open(CAMINHO_BIBLIA, "r", encoding="utf-8") as f:
        return json.load(f)


def calcular_score(texto, palavras_chave):
    score = 0

    for p in palavras_chave:
        if p in texto:
            score += 3

    for p in PALAVRAS_POSITIVAS:
        if p in texto:
            score += 2

    for n in PALAVRAS_EXCLUDENTES:
        if n in texto:
            score -= 5

    return score


def selecionar_versiculos(tema, limite=3):
    biblia = carregar_biblia()
    palavras = TEMAS.get(tema.lower(), [])

    candidatos = []

    for v in biblia:
        livro = v.get("livro", "")
        texto = v.get("texto", "").lower()

        if livro not in LIVROS_PRIORITARIOS:
            continue

        score = calcular_score(texto, palavras)

        if score > 0:
            referencia = f"{livro} {v['capitulo']}:{v['versiculo']} — {v['texto']}"
            candidatos.append((score, referencia))

    candidatos.sort(reverse=True, key=lambda x: x[0])

    resultados = [v[1] for v in candidatos[:limite]]

    return resultados if resultados else FALLBACK
