from pipeline.versiculos import selecionar_versiculos
from pipeline.prompt import montar_prompt
from llm.devocional_llm import gerar_resposta


def gerar_devocional(tema: str) -> str:
    # 1. Buscar versículos relacionados ao tema
    versiculos = selecionar_versiculos(tema)

    # 2. Montar prompt final
    prompt = montar_prompt(tema, versiculos)

    # 3. Enviar para o LLM (Ollama)
    resposta = gerar_resposta(prompt, versiculos)

    return resposta
