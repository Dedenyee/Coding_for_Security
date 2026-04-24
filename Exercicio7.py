# Exercício 7 — Calculadora Segura com Exceções: Crie uma calculadora que opere em loop (while True) pedindo dois números e uma operação (+, -, *, /). 
# O programa deve tratar com try/except: entrada não numérica (ValueError), divisão por zero (ZeroDivisionError) e operação inválida.
# Use else para exibir o resultado quando não houver erro e finally para exibir "Operação processada." sempre. O usuário pode digitar "sair" para encerrar.

# Sequência de teste:
# Número 1: abc     → "Erro: Digite apenas números!"
# Número 1: 10
# Número 2: 0
# Operação: /       → "Erro: Divisão por zero!"
# Número 1: 10
# Número 2: 3
# Operação: /       → "Resultado: 3.33"
# Número 1: 5
# Número 2: 3
# Operação: %       → "Erro: Operação '%' não suportada. Use +, -, * ou /"
# Número 1: sair    → "Encerrando calculadora."

# Cada interação deve exibir ao final:
# "Operação processada." (via finally)
def main():
    def operror(operacao): #Classifica como erro qualquer oautra operação na qual utiliza outro tipo de caracter especial como erro.
        if operacao not in ["+", "-", "*", "/"]:
            raise ValueError(f"Operação '{operacao}' não suportada. Use +, -, * ou /")


    while True:
        try:
            num = input("Digite um número - ")
            if num == "sair": 
                print("Encerrando calculadora.")
                break
            entrada = float(num)
            num2 = input("Digite Outro número - ")
            if num2 == "sair": 
                print("Encerrando calculadora.")
                break
            entrada2 = float(num2)

            operacao = input("Digite uma operação (+, -, *, /) ou 'sair' para sair - ")
            operror(operacao)

            if operacao == "+":
                resultado = entrada + entrada2
            elif operacao == "-":
                resultado = entrada - entrada2
            elif operacao == "*":
                resultado = entrada * entrada2
            elif operacao == "/":
                resultado = entrada / entrada2
        except ValueError as e:
            print(f"Digite apenas números! {e} ")
            continue

        except ZeroDivisionError as e:
            print(f"Erro: Não é possível dividir por zero! {e}")
            continue

        else:
            print(f"Resultado: {resultado:.2f}") 
        
        finally:
            print("Operação processada. ")
main()