from pipeline.biblia import carregar_biblia

PALAVRAS_TEMA = {
    "ansiedade": ["ansioso", "ansiedade", "medo", "temor", "aflito", "preocupado", "paz"],
    "luto": ["choro", "lamento", "tristeza", "morte", "dor"],
    "esperanca": ["esperança", "confiança", "fé", "promessa"],
}

def selecionar_versiculos(tema, limite=3):
    biblia = carregar_biblia()
    palavras = PALAVRAS_TEMA.get(tema, [])

    encontrados = []

    for item in biblia:
        texto = item.get("texto", "").lower()

        if any(p in texto for p in palavras):
            referencia = f"{item['livro']} {item['capitulo']}:{item['versiculo']}"
            encontrados.append((referencia, item["texto"]))

        if len(encontrados) >= limite:
            break

    return encontrados
