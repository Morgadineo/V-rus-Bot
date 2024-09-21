import discord
import pyodbc
from settings import *
from Zumbi import Zumbi
from Loot import Loot


# Client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

dados_de_conexao = (
    "Driver={SQLite3 ODBC Driver};"
    "Server=localhost;"
    "Database=banco_de_dados.db"
)

conexao = pyodbc.connect(dados_de_conexao)
cursor = conexao.cursor()

# Classes
sistemaLoot = Loot(cursor)


@client.event
async def on_ready():
    print("Sem chance para os vivos!")

@client.event
async def on_disconnect():
    """Função chamada quando o Bot é desconectado"""
    print("Morri...")
    cursor.close()
    conexao.close()


# Message events
@client.event
async def on_message(message):
    """Função chamada quando uma mensagem é enviada"""
    content = message.content.capitalize()
    channel = message.channel
    author = message.author
    author_name = author.name  # Nick do autor
    mention = author = author.mention  # Mencionar autor

    quantidade = 1  # Quantidade de execuções do comando
    contentSliced = content.split(' ')  # Conteúdo partido

    if 1 < len(contentSliced) < 4:
        comando = contentSliced[0] + ' ' + contentSliced[1]
        if author_name == "morgadineo":
            try:
                quantidade = int(contentSliced[2])
            except IndexError:
                printarAmarelo("\n~~ IndexWarning: quantidade não informada. Utilizando padrão. ~~\n")
            except ValueError:
                await channel.send(f"### {mention}: Quantidade Inválida!!")
                raise ValueError('Quantidade informada não é um inteiro.')

            # Random generator
            match comando:
                case 'Se apresente':
                    await channel.send(f"{mention}{apresentacao()}")

                case 'Gerar loot':
                    for i in range(quantidade):
                        await channel.send(f"{mention}\n# {sistemaLoot.gerarLootZumbi()}")

                case 'Gerar zumbi':
                    for i in range(quantidade):
                        zumbi = Zumbi(sistemaLoot)
                        await channel.send(f"\n{mention}\n# {zumbi.printarTudo()}\n")

# Bot run and token
# keep_alive()

if __name__ == '__main__':
    client.run('TOKEN')
