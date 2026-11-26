import json
import anthropic

client = anthropic.Anthropic()

CATEGORIAS = ["alimentação", "transporte", "moradia", "lazer", "saúde", "outros"]

system = f"""Você categoriza gastos pessoais.
Responda APENAS com um JSON neste formato, sem nenhum texto antes ou depois:
{{"categoria": "...", "confianca": 0.0}}
A categoria deve ser uma destas: {CATEGORIAS}.
"confianca" é um número de 0 a 1."""

gastos = ["UBER *TRIP", "PADARIA PAO QUENTE", "NETFLIX.COM", "DROGASIL 123", "XPTO LTDA"]

for gasto in gastos:
    resposta = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=50,
        system=system,
        messages=[{"role": "user", "content": gasto}],
    )
    texto = resposta.content[0].text
    print("JSON:", texto)
    try:
        dados = json.loads(texto)
        valido = dados["categoria"] in CATEGORIAS
        print(f"{gasto:20} -> {dados['categoria']:12} conf={dados['confianca']}  válido={valido}")
    except (json.JSONDecodeError, KeyError):
        print(f"{gasto:20} -> resposta não era JSON válido: {texto!r}")
    
    print("--------------------------------")