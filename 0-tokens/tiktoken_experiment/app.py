import tiktoken
enc = tiktoken.get_encoding("o200k_base")
sum_tokens = 0
lista = ["Hello, what is your name?", "Olá, qual é o seu nome?", "Vc sabe python?"]

# somente para ver a quantidade de tokens
for t in lista:
    ids = enc.encode(t)
    print(len(ids), [enc.decode([i]) for i in ids], t)



print("\n"* 2)
# simular comportamento de uma conversa.
lista_respostas = ["My name is Dennis", "Meu nome é dennis", "Sim, eu sei Python."]

for i, pergunta in enumerate(lista):
    for idx in range(i + 1):
        print(f"{idx + 1}a pergunta: " + lista[idx])
        print(f"{idx + 1}a resposta: " + lista_respostas[idx])
        ids = enc.encode(lista[idx])
        rds = enc.encode(lista_respostas[idx])
        print(f"Tokens gastos na pergunta: {len(ids)}")
        print(f"Tokens gastos na resposta: {len(rds)}")
        amount_tokens = len(ids) + len(rds)
        sum_tokens += amount_tokens
        print(f"Gastou {amount_tokens} tokens")
        print("******\n")

print(f"No fim da conversa deu {sum_tokens} ao total")