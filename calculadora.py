while True:
    print("\nCalculadora Simples")
    print("1. (+) Adição")
    print("2. (-) Subtração")
    print("3. (*)Multiplicação")
    print("4. (/)Divisão")
    print("5. Sair")
    escolha = input("Escolha uma operação ( 1(+) / (-)2 / (*)3 / (/)4 / Sair 5): ")

    if escolha == '5':
        print("Saindo do programa...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado: ", int(num1 + num2))
    elif escolha == '2':
        print("Resultado: ",  int(num1 + num2))
    elif escolha == '3':
        print("Resultado: ",  int(num1 + num2))
    elif escolha == '4':
        if num2 == 0:
            print("Erro! Divisão por zero.")
        else:
            print("Resultado: ",  int(num1 + num2))
    else:
        print("Entrada inválida!")