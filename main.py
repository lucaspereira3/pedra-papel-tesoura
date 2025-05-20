import random

def get_computer_choice():
    """Seleciona aleatoriamente a escolha do computador."""
    return random.choice(["pedra", "papel", "tesoura"])

def determine_winner(user_choice, computer_choice):
    """Determina o vencedor com base nas escolhas."""
    if user_choice == computer_choice:
        return "Empate!"
    elif (
        (user_choice == "pedra" and computer_choice == "tesoura") or
        (user_choice == "tesoura" and computer_choice == "papel") or
        (user_choice == "papel" and computer_choice == "pedra")
    ):
        return "Você venceu!"
    else:
        return "O computador venceu!"

if __name__ == "__main__":
    print("--- Jogo Pedra, Papel e Tesoura ---")
    user_score = 0
    computer_score = 0

    while True:
        print("\nEscolha: pedra, papel ou tesoura (ou digite 'sair' para terminar)")
        user_choice = input("> ").lower().strip()

        if user_choice == "sair":
            break

        if user_choice not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida. Por favor, digite pedra, papel ou tesoura.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nSua escolha: {user_choice}")
        print(f"Escolha do computador: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Atualiza o placar
        if "Você venceu" in result:
            user_score += 1
        elif "computador venceu" in result:
            computer_score += 1

        print(f"\nPlacar: Você {user_score} - {computer_score} Computador")
        print("---")

    print("\n--- Fim de Jogo ---")
    print("Placar Final:")
    print(f"Você: {user_score}")
    print(f"Computador: {computer_score}")
    if user_score > computer_score:
        print("Parabéns, você foi o grande vencedor!")
    elif computer_score > user_score:
        print("O computador venceu desta vez. Tente novamente!")
    else:
        print("O jogo terminou em empate!")
    print("Obrigado por jogar!")
