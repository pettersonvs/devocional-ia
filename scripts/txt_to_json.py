import json
import re

biblia = []

livro_atual = None
capitulo_atual = None

with open("data/biblia_arc.txt", "r", encoding="utf-8") as f:
    for linha in f:
        linha = linha.strip()

        if not linha:
            continue

        # Detecta linha tipo: GÊNESIS 1
        match_livro = re.match(r"^([A-ZÊÉÍÓÚÃÕÇ]+)\s+(\d+)$", linha)
        if match_livro:
            livro_atual = match_livro.group(1).title()
            capitulo_atual = int(match_livro.group(2))
            continue

        # Detecta versículo: 1 Texto...
        match_versiculo = re.match(r"^(\d+)\s+(.*)", linha)
        if match_versiculo and livro_atual and capitulo_atual:
            versiculo = int(match_versiculo.group(1))
            texto = match_versiculo.group(2)

            biblia.append({
                "livro": livro_atual,
                "capitulo": capitulo_atual,
                "versiculo": versiculo,
                "texto": texto
            })

with open("data/biblia_arc.json", "w", encoding="utf-8") as f:
    json.dump(biblia, f, ensure_ascii=False, indent=2)

print(f"Versículos processados: {len(biblia)}")
