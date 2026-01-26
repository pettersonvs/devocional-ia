def classificar_tema(pergunta: str) -> str:
    texto = pergunta.lower()

    if any(p in texto for p in ["ansioso", "ansiedade", "medo", "aflito", "preocupado"]):
        return "ansiedade"
    if any(p in texto for p in ["triste", "luto", "perda", "dor"]):
        return "luto"
    if any(p in texto for p in ["culpa", "pecado", "errado"]):
        return "culpa"
    if any(p in texto for p in ["desânimo", "cansado", "esperança"]):
        return "esperanca"

    return "geral"
