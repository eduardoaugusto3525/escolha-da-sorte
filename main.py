# Inicializar variáveis de pontuação
jogador1_pontos = 0
jogador2_pontos = 0

print("Bem-vindo ao sistema de contagem de pontos!")
while True:
    print("\nPontuação Atual:")
    print(f"Jogador 1: {jogador1_pontos}")
    print(f"Jogador 2: {jogador2_pontos}")

    # Escolher o jogador para adicionar pontos
    jogador = input("Digite '1' para adicionar pontos ao Jogador 1 ou '2' para o Jogador 2 (ou 'sair' para encerrar): ")

    if jogador == '1':
        pontos = int(input("Quantos pontos deseja adicionar para o Jogador 1? "))
        jogador1_pontos += pontos
    elif jogador == '2':
        pontos = int(input("Quantos pontos deseja adicionar para o Jogador 2? "))
        jogador2_pontos += pontos
    elif jogador.lower() == 'sair':
        break
    else:
        print("Escolha inválida, tente novamente.")

# Exibir placar final e determinar o vencedor
print("\nPlacar Final:")
print(f"Jogador 1: {jogador1_pontos} pontos")
print(f"Jogador 2: {jogador2_pontos} pontos")

if jogador1_pontos > jogador2_pontos:
    print("Jogador 1 é o vencedor!")
elif jogador2_pontos > jogador1_pontos:
    print("Jogador 2 é o vencedor!")
else:
    print("É um empate!")
