# ✊✋✌️ pedra-papel-tesoura-py

Um simples jogo de **Pedra, Papel e Tesoura** feito em Python, para ser jogado diretamente no terminal contra o computador. O programa escolhe aleatoriamente e exibe o placar em tempo real até que o jogador deseje encerrar.

---

## 📌 Tópicos

- [🎮 Sobre o Projeto](#-sobre-o-projeto)
- [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [⚙️ Como Executar](#️-como-executar)
- [🛠️ Funcionalidades](#️-funcionalidades)
- [🧠 Explicação do Código](#-explicação-do-código)
- [📄 Licença](#-licença)
- [🤝 Contribuindo](#-contribuindo)

---

## 🎮 Sobre o Projeto

Este projeto é uma implementação simples do clássico jogo Pedra, Papel e Tesoura. O jogador interage via terminal digitando sua escolha, e o computador escolhe aleatoriamente a sua jogada. O jogo contabiliza os pontos e declara o vencedor ao final da partida.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Módulo `random` da biblioteca padrão

---

## ⚙️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/rafaelmoreirax/pedra-papel-tesoura-py.git
cd pedra-papel-tesoura-py
```

2. **Execute o script:**

```bash
python main.py
```

3. **Siga as instruções no terminal:**

- Digite `pedra`, `papel` ou `tesoura`.
- Digite `sair` para encerrar o jogo.

---

## 🛠️ Funcionalidades

- [x] Escolha do usuário via terminal
- [x] Escolha aleatória do computador
- [x] Lógica completa de vitória/empate/derrota
- [x] Placar atualizado a cada rodada
- [x] Mensagem final personalizada
- [ ] Modo multiplayer local (em planejamento)

---

## 🧠 Explicação do Código

- `get_computer_choice()`: retorna aleatoriamente `"pedra"`, `"papel"` ou `"tesoura"`.
- `determine_winner(user, computer)`: define quem venceu com base nas regras do jogo.
- O loop principal permite jogar indefinidamente até que o usuário digite `"sair"`.
- O programa armazena e exibe o placar durante o jogo e mostra o resultado final ao final da execução.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Fork este repositório.
2. Crie uma branch: `git checkout -b minha-melhoria`.
3. Commit suas alterações: `git commit -m 'feat: nova funcionalidade'`.
4. Push para sua branch: `git push origin minha-melhoria`.
5. Abra um Pull Request.

---

## 👤 Autor

Feito com 🕹️ por [Rafael Moreira](https://github.com/rafaelmoreirax)
