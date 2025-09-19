# Virus-Bot 🧟‍♂️

O **Virus-Bot** é um bot para Discord criado para gerar conteúdo dinâmico para sessões de RPG com temática apocalíptica / zumbi.

---

## ✨ Funcionalidades

- **Geração de inimigos aleatórios** — cria zumbis com atributos únicos.  
- **Sistema de loot dinâmico** — gera itens aleatórios com quantidades variadas.  
- **Banco de dados SQLite** — armazenamento persistente de dados.  
- **Comandos customizáveis** — sistema flexível de comandos e respostas.

---

## 🚀 Como usar (rápido)

### Pré-requisitos
- Python **3.8+**  
- Conta de desenvolvedor no Discord  
- Token do bot Discord

### Instalação
1. Clone o repositório e entre na pasta:
    
    git clone https://github.com/seu-usuario/virus-bot.git
    cd virus-bot

2. Instale as dependências:

    pip install -r requirements.txt

3. Configure o token (duas opções):
- **Arquivo `TOKEN.txt`**  
    echo "SEU_TOKEN_AQUI" > TOKEN.txt

- **Variável de ambiente**  
  - Linux/macOS:
      
      export DISCORD_BOT_TOKEN="SEU_TOKEN_AQUI"
  - Windows (PowerShell):
      
      $env:DISCORD_BOT_TOKEN="SEU_TOKEN_AQUI"

4. Execute o bot:

    python main.py

---

## ⌨️ Comandos (exemplos)

| Comando               | Descrição                 | Exemplo           |
|-----------------------|---------------------------|-------------------|
| `Gerar zumbi [qtde]`  | Gera zumbis aleatórios    | `Gerar zumbi 3`   |
| `Gerar loot [qtde]`   | Gera itens aleatórios     | `Gerar loot 5`    |
| `Se apresente`        | Bot se apresenta          | `Se apresente`    |

---

## 🏗️ Estrutura do projeto

    virus-bot/
    ├── main.py             # Arquivo principal do bot
    ├── Zumbi.py            # Classe / lógica para geração de zumbis
    ├── Loot.py             # Sistema de geração de loot
    ├── settings.py         # Configurações e constantes
    ├── requirements.txt    # Dependências do projeto
    ├── TOKEN.txt           # Token do bot (não versionado — ignorar no git)
    └── banco_de_dados.db   # Banco de dados SQLite (local)

**Sugestão**: adicione `TOKEN.txt` e `banco_de_dados.db` no `.gitignore` para não comitar credenciais/dados.

---

## 📦 Dependências

- `discord.py` — biblioteca para integração com o Discord  
- `sqlite3` — já incluso no Python (para o DB local)

Instalação: `pip install -r requirements.txt`

---

## 🔧 Configuração adicional

### Permissões / Intents
No painel do Discord Developer Portal, habilite as intents necessárias:
- **Message Content Intent** (se o bot precisa ler o conteúdo das mensagens)
- **Server Members Intent** (se o bot precisa informações sobre membros)

### Arquivos sensíveis
**Nunca** comite o `TOKEN.txt` nem expose o token em repositórios públicos.

---

## 🎨 Exemplos de saída

(Inserir imagens/prints gerados pelo bot aqui — ex.: geração de zumbi, loot, etc.)

Exemplo (markdown para imagem):
![Exemplo Zumbi](https://github.com/user-attachments/assets/42ff9bf0-5255-4373-9ec2-f12c600cfd8f)
![Exemplo Loot](https://github.com/user-attachments/assets/f869d4a2-1a6d-4633-852b-dd34383da6c9)

---

## 🤝 Como contribuir

1. Faça fork do repositório.  
2. Crie uma branch: `git checkout -b feature/NovaFeature`  
3. Commit suas mudanças: `git commit -m "Adiciona NovaFeature"`  
4. Push para a branch: `git push origin feature/NovaFeature`  
5. Abra um Pull Request.

---

## 🐛 Reportar problemas

Abra uma *issue* descrevendo:
- Passos para reproduzir
- Logs / mensagens de erro
- Versão do Python e sistema operacional

---

## 📝 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo `LICENSE` para detalhes.

---

## 💡 Próximas features planejadas

- Sistema de combate  
- Inventário de jogadores  
- Missões aleatórias  
- Sistema de crafting

---

## .gitignore (exemplo)
Adicione no `.gitignore`:

    TOKEN.txt
    banco_de_dados.db
    __pycache__/
    .env

---

