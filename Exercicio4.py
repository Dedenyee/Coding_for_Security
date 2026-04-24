# Exercício 4 — Análise de Notas com Tuplas: Crie um programa que receba as notas de 5 alunos (nome e nota) e armazene cada par como uma tupla dentro de uma lista.
# Depois, usando laços,calcule e exiba: a maior nota e o nome do aluno, a menor nota e o nome do aluno, a média da turma, 
# e quais alunos estão acima da média. Use for para percorrer a lista.

# Saída esperada:
# === Relatório de Notas ===
# Maior nota: Ana - 9.2
# Menor nota: Eduardo - 4.5
# Média da turma: 7.2
#
# Alunos acima da média:
# - Carlos: 8.5
# - Ana: 9.2
# - Diana: 7.8
# Dados para teste (podem ser digitados ou hardcoded):
def main():
    alunos = []
    for i in range(5): # Range 5 para adicionar os 5 alunos. 
        print("="*100)
        nome = input("Digite um nome - ")
        nota = float(input("Digite a nota - "))
        alunos.append((nome,nota))
 
    # Cálculo das notas.
    maiorN_nome = alunos[0][0]
    maior_nota = alunos[0][1]
    menorN_nome = alunos[0][0]
    menor_nota = alunos[0][1]
    soma = 0
    for aluno in alunos:
        nome = aluno[0]
        nota = aluno[1]
        soma += nota
        if nota > maior_nota:
            maior_nota = nota
            maiorN_nome = nome
        
        if nota < menor_nota:
            menor_nota = nota
            menorN_nome = nome
        
    media = soma / len(alunos) # Média

    print("="*50 + "Relatório de notas" + "="*50)
    print(f"Maior nota - {maiorN_nome} -- {maior_nota}")
    print(f"Menor nota - {menorN_nome} -- {menor_nota}")
    print(f"Média da turma - {media}")
    print("="*50)
    print("Alunos acima da média - ")
    for aluno in alunos:
        if aluno[1] > media:
            print(f"- {aluno[0]}: {aluno[1]}")    
main()