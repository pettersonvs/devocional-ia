from pipeline.prompt import montar_prompt
import requests
import json

def gerar_resposta(pergunta, versiculos):
    prompt = montar_prompt(pergunta, versiculos)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": True
        },
        stream = True,
        timeout = 600
    )

    resposta_final = ""

    for linha in response.iter_lines():
        if linha:
            data = json.loads(linha.decode("utf-8"))
            resposta_final += data.get("response", "")

            if data.get("done"):
                break

    return resposta_final.strip()