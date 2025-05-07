def calculadora():
    print("Bem-vindo à Calculadora Simples!")
    print("Operações disponíveis:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potenciação (^)")
    print("6. Sair")

    while True:
        try:
            operacao = input("\nEscolha uma operação (1-6): ")
            
            if operacao == '6':
                print("Obrigado por usar a calculadora!")
                break
                
            if operacao not in ['1', '2', '3', '4', '5']:
                print("Operação inválida! Por favor, escolha uma opção válida.")
                continue
                
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if operacao == '1':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif operacao == '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif operacao == '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif operacao == '4':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida!")
                    continue
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            elif operacao == '5':
                resultado = num1 ** num2
                print(f"Resultado: {num1} ^ {num2} = {resultado}")
                
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    calculadora() 
