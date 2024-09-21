# Virus-Bot

O vírus-bot é um bot no discord da qual desenvolvi para gerar conteúdo para sessões de RPG. O RPG não foi a diante, então estou utilizando para ensinar a criação de bots.

## O que ele faz?
Originalmente, a ideia é que ele servisse para gerar itens e encontros com monstros em um RPG de temática apocalíptica.

### Gera inimigos aleatórios.
O bot fica responsável por gerar inimigos com atributos aleatórios e "loots" randômicos, através do comando: *gerar inimigo [qtde]*. Qtde se refere a quantidade de inimigos em sequência que será gerado, caso não seja passado, será gerado apenas 1.

![Inimigo 1](https://github.com/user-attachments/assets/42ff9bf0-5255-4373-9ec2-f12c600cfd8f)

Os inimigos ficam armazenados em um dicionário, onde é possível gerenciar a chance de geração, variação dos atributos e nível de poder. Assim, permitindo que seja fácil adicionar ou modificar inimigos. 

Os inimigos também vem com um sistema de mochila, que aumenta a quantidade máxima de itens que ele pode carregar. As mochilas são separadas por tamanho, onde cada tipo fica armazenado em um dicionário, sendo possível ajustar a CHANCE do inimigo nascer com ela e o MÁXIMO de itens que ela proporciona.

### Gera loots aleatórios.
Outra funcionalidade é a geração de itens aleatórios através do comando. Os itens ficam armazenados em um banco de dados SQLite (Nome do item, Quantidade máxima possível). A quantidade de unidades de um determinado item é gerada aleatóriamente [1, Máximo], onde cada inimigo, com base no nível e na mochila, contém.

![Mochila 1](https://github.com/user-attachments/assets/f869d4a2-1a6d-4633-852b-dd34383da6c9) 

Também é possível gerar loots separadamente através do comando: *gerar loot [qtde]*. Qtde se refere a quantidade de itens diferentes que serão gerados.
