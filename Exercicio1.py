# Exercício 1 — Contador de Vogais e Consoantes: Crie um programa que peça uma frase ao usuário e use um laço for 
# para percorrer cada caractere, contando quantas vogais e quantas consoantes existem.
# Ignore números, espaços e caracteres especiais. Exiba o total de cada um ao final.

# # Teste com estas frases:
# testes = [
#     "Python para Seguranca",
#     "Hello World 123!",
#     "aeiou",
#     "",
# ]

# # Saída esperada (frase 1):
# # Frase: "Python para Seguranca"
# # Vogais: 7
# # Consoantes: 11
def main():
    print("="*50)
    frase = input(str("Digite uma frase: "))
    vogais = ["a","e","i","o","u"]
    consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    contador_vogais = 0
    contador_consoante = 0

    for i in frase:
        i = i.lower()
        if i in vogais:
            contador_vogais += 1
        if i in consoantes:
            contador_consoante += 1
    print(f"Número de vogais -- {contador_vogais}, Número de consoantes -- {contador_consoante}")
    print("="*50)
main()



