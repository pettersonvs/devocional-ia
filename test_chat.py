from pipeline.versiculos import selecionar_versiculos
from llm.devocional_llm import gerar_resposta

pergunta = "estou ansioso e com medo"
versiculos = selecionar_versiculos("ansiedade")
resposta = gerar_resposta(pergunta, versiculos)

print(resposta)
