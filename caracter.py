def conte_caracter():
    while True:
        print("\n1. Contar o número de palavras")
        print("2. Contar o número de caracteres (sem espaços em branco)")
        print("3. Sair")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == '1':
            texto = input("\nDigite o texto: ")
            palavra = texto.split()
            print(f"\\nO número de palavras no texto é: {len(palavra)}")
            
        elif escolha == '2':
            texto = input("\nDigite o texto: ")
            caracter = texto.replace(" ", "")
            print(f"\nO número de caracteres no texto (sem espaços em branco) é: {len(caracter)}")
            
        elif escolha == '3':
            print("\nFinalizando...")
            break
            
        else:
            print("\nOpção inválida. Por favor, tente novamente.")

conte_caracter()