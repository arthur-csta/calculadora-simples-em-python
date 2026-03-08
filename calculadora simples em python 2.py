calculo_final = float(input("Digite o valor inicial da calculadora: "))
continuar = True
# A variável "calculo_final" guarda o resultado acumulado das operações
# O usuário define o valor inicial para evitar problemas em multiplicações e divisões


while continuar:
    acao = int(input(
        "\nQual operação você deseja fazer?\n"
        "1 - Adição\n"
        "2 - Subtração\n"
        "3 - Divisão\n"
        "4 - Multiplicação\n"
        "5 - Potenciação\n"
        "6 - Resultado final\n"
        "Sua escolha: "
    ))
# Definimos a variável "acao" para que a escolha do usuário determine qual operação será realizada
# O comando "input" permite a interação com o usuário, enquanto o "int" limita a resposta a números inteiros


    if acao == 6:
        break
# O comando "break" encerra o loop do "while" caso o usuário queira ver o resultado final


    if acao not in [1, 2, 3, 4, 5]:
        print("Opção inválida! Tente novamente.")
        continue
# Esse bloco funciona como tratamento de erro caso o usuário digite uma opção inexistente


    quantidade = int(input("Quantos números você quer usar nessa operação? "))
# A variável "quantidade" permite que o usuário repita a operação várias vezes


    for i in range(quantidade):
        numero = float(input(f"Digite o número da operação com {calculo_final}: "))
# Os comandos "for", "in" e "range" funcionam juntos para repetir a operação quantas vezes forem necessárias
# A variável "numero" armazena o valor digitado pelo usuário


        if acao == 1:
            calculo_final += numero
        elif acao == 2:
            calculo_final -= numero
        elif acao == 3:
            if numero == 0:
                print("Não é possível dividir por zero.")
                continue
            calculo_final /= numero
        elif acao == 4:
            calculo_final *= numero
        elif acao == 5:
            calculo_final **= numero
# Os comandos "if" e "elif" determinam qual operação matemática será executada


    print("Resultado atual:", calculo_final)
# Esse print mostra ao usuário o resultado parcial após cada operação


    resposta = input("Deseja voltar ao menu inicial? (s/n): ").lower()
    if resposta != "s":
        continuar = False
# A variável "resposta" verifica se o usuário quer continuar usando a calculadora
# Caso a resposta seja diferente de "s", o loop é encerrado


print("\nO resultado final da(s) operação(ões) é:", calculo_final)
# Quando o loop termina, o programa mostra o resultado final acumulado


# Projeto simples de calculadora acumulativa em Python
# Feito por Arthur Costa