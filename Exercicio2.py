# Exercício 2 — Validador de Senha com Regras: Crie um programa que peça uma senha ao usuário repetidamente (usando while) 
# até que ela atenda TODOS os critérios: mínimo 8 caracteres, pelo menos 1 letra maiúscula,
# pelo menos 1 letra minúscula, pelo menos 1 número e pelo menos 1 caractere especial (!@#$%&*).
#  A cada tentativa inválida, informe quais critérios não foram atendidos. Use break para sair quando a senha for válida.
# Teste com estas senhas:
# testes = [
#     "abc",              # Fraca: faltam maiúscula, número, especial, < 8 chars
#     "abcdefgh",         # Faltam maiúscula, número, especial
#     "Abcdefgh",         # Faltam número e especial
#     "Abcdefg1",         # Falta especial
#     "Cyber@2024",       # Válida!
# ]

# Saída esperada (senha "Abcdefgh"):
# Senha inválida! Problemas encontrados:
# - Falta pelo menos 1 número
# - Falta pelo menos 1 caractere especial (!@#$%&*)
# Digite outra senha:
maiuscula = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numero = ["0","1","2","3","4","5","6","7","8","9"]
especial = ["!","@","#","$", "%","&","*","(",")","/","-","+","=","_",">","<"]
def main():
    print("="*100)
    print("Você deve criar uma senha que atenda alguns requisitos\nMínimo 8 caracteres / 1 - Letra Minúscula / 1 - Letra Maiúscula / 1 - Caractere Especial (!@#$%&*)")
    while True:
        senha = input("Digite uma senha: ")
        problemas = []

        if len(senha) < 8:
            problemas.append("- Falta mínimo de 8 caracteres") # Adiciona a problemas e ao mesmo tempo printa na tela.      

        contador_maiuscula = 0
        for letra in senha:
            if letra in maiuscula:
                contador_maiuscula += 1
        if contador_maiuscula == 0:                                   
            problemas.append("- Falta pelo menos 1 letra maiúscula")

        contador_minuscula = 0
        for letra in senha:
            if letra.islower(): # Verifica se a senha é minúscula.
                contador_minuscula += 1
        if contador_minuscula == 0:                                   
            problemas.append("- Falta pelo menos 1 letra minúscula")

        contador_numero = 0
        for letra in senha:
            if letra in numero:
                contador_numero += 1
        if contador_numero == 0:                                      
            problemas.append("- Falta pelo menos 1 número")

        contador_especial = 0
        for letra in senha:
            if letra in especial:
                contador_especial += 1
        if contador_especial == 0:                                    
            problemas.append("- Falta pelo menos 1 caractere especial (!@#$%&*)")

        if len(problemas) == 0:
            print("Senha válida! ")
            break
        else:
            print(f"Senha inválida! Problemas encontrados: {problemas}")
            print("Digite outra senha:\n")
main()
