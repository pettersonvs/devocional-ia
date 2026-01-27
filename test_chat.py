from pipeline.classifier import classificar_tema
from rag.semantic_search import buscar_versiculos_semanticos
from pipeline.prompt import montar_prompt
from llm.devocional_llm import gerar_resposta

pergunta = "estou ansioso e com medo"

tema = classificar_tema(pergunta)
versiculos = buscar_versiculos_semanticos(pergunta)
prompt = montar_prompt(pergunta, tema, versiculos)

print("VERSÍCULOS USADOS:")
for v in versiculos:
    print(v)

print("\nRESPOSTA:\n")
resposta = gerar_resposta(prompt)
print(resposta)
