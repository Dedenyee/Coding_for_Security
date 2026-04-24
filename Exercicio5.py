# Exercício 5 — Contador de Palavras com Dicionário: Crie um programa que receba um texto do usuário e 
# conte quantas vezes cada palavra aparece, armazenando em um dicionário (palavra como chave, contagem como valor). 
# Converta tudo para minúsculo antes de contar. Ao final, exiba as palavras ordenadas pela frequência 
# (da mais frequente para a menos frequente) e destaque a palavra mais usada.
# Texto para teste:
# texto = "o gato viu o rato e o rato viu o gato e o gato correu"

# Saída esperada:
# === Contagem de Palavras ===
# "o"      → 6 vezes
# "gato"   → 3 vezes
# "rato"   → 2 vezes
# "viu"    → 2 vezes
# "e"      → 2 vezes
# "correu" → 1 vez
#
# Palavra mais frequente: "o" (6 vezes)
# Total de palavras únicas: 6
def main():
    palavras = {}
    print("="*20 + " Contador de Palavras " + "="*20)
    frase = str(input("Digite uma frase -- "))
    palavra = "" # Armazenar a palavra que está sendo lida.

    for i in frase: # For para contagem das palavras
        if i != " ": # Ignora o espaço entre as palavras.
            palavra += i # Juntar aas letras.
        else:
            if palavra != "":  # evita palavra vazia por espaços extras
                palavra = palavra.lower()
                if palavra in palavras:
                    palavras[palavra] += 1
                else:
                    palavras[palavra] = 1
            palavra = ""

    if palavra != "": 
        palavra = palavra.lower()
        if palavra in palavras:
            palavras[palavra] += 1
        else:
            palavras[palavra] = 1

    total_unicas = len(palavras)
    contador_iteracao = 0 

    while len(palavras) > 0:
        maior_contagem = 0
        maior_palavra = ""

        for palavra in palavras:
            if palavras[palavra] > maior_contagem:
                maior_contagem = palavras[palavra]
                maior_palavra = palavra

        if contador_iteracao == 0: 
            palavra_mais_frequente = maior_palavra
            contagem_mais_frequente = maior_contagem

        contador_iteracao += 1

        print(f"{maior_palavra} - {maior_contagem} vezes")
        palavras.pop(maior_palavra)

    print(f"\nPalavra mais frequente - '{palavra_mais_frequente}' ({contagem_mais_frequente} vezes)")
    print(f"Total de palavras únicas - {total_unicas}")
main()