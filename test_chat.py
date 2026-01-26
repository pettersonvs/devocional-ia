from pipeline.classifier import classificar_tema
from pipeline.versiculos import selecionar_versiculos
from pipeline.prompt import montar_prompt
from llm.devocional_llm import gerar_resposta

pergunta = "estou ansioso e com medo"

tema = classificar_tema(pergunta)
versiculos = selecionar_versiculos(tema)
prompt = montar_prompt(pergunta, tema, versiculos)

print("VERSÍCULOS USADOS:")
for v in versiculos:
    print(v)

print("\nRESPOSTA:\n")
resposta = gerar_resposta(prompt)
print(resposta)
