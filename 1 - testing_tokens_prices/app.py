import anthropic

client = anthropic.Anthropic()  # lê a chave da variável de ambiente

resposta = client.messages.create(
    model="claude-haiku-5-5",   # modelo pequeno e barato, ótimo pra estudar
    max_tokens=300,             # limite de tokens da SAÍDA
    #temperature=0,              # teste depois com 1
    system="Você deve responder em 2 frases no máximo",
    messages=[
        {"role": "user", "content": "O que é um token em um LLM?"}
    ],
)

print(resposta.content[0].text)
print("---")
print("Tokens de entrada:", resposta.usage.input_tokens)
print("Tokens de saída:", resposta.usage.output_tokens)
print("Motivo de parada:", resposta.stop_reason)