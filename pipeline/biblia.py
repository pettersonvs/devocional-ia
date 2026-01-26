import json

CAMINHO_BIBLIA = "data/biblia_arc.json"

def carregar_biblia():
    with open(CAMINHO_BIBLIA, "r", encoding="utf-8") as f:
        return json.load(f)
