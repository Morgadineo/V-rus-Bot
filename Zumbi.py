from random import randint, choice, uniform
from Loot import Loot


class Zumbi:

    def __init__(self, sistemaLoot):
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        self.probabilidade = 0
        self.variacao = ()
        self.poder = 0
        self.habilidades = []
        self.sistemaLoot = sistemaLoot
        self.lootBonusMochila = 0
        self.qtdeLootMax = 0
        self.loots = []

        self.danoMordida = 0
        self.cdMordida = 0
        self.danoArranhao = 0
        self.cdArranhao = 0
        self.cdInfeccaoMordida = 0
        self.chanceInfeccaoMordida = 0
        self.chanceInfeccaoArranhao = 0

        self.tipoMochila = self.definirMochila()
        self.tipo = self.definirTipo()
        self.calcularAtributos()
        self.vida = self.calcularVida()
        self.definirHabilidades()
        self.definirLoot()

        self.definirMordida()
        self.definirArranhao()

    def definirMordida(self):
        self.danoMordida = f"d8 + ({self.forca})"
        self.cdMordida = f"2d6 + ({self.destreza})"
        self.chanceInfeccaoMordida = 10 + self.poder

    def definirArranhao(self):
        self.danoArranhao = f"d6 + ({self.forca})"
        self.cdArranhao = f"2d6 + ({self.destreza})"
        self.chanceInfeccaoArranhao = 6 + self.poder

    def definirLoot(self):
        qtdeLoot = randint(1, self.qtdeLootMax)
        segredo = randint(1, 100000)
        if segredo == 55555:
            self.loots.append("(1) Frasco com Líquido Desconhecido...")

        for i in range(qtdeLoot):
            self.loots.append(self.sistemaLoot.gerarLootZumbi())

    def definirMochila(self):
        tiposMochilas = {"Nenhuma": (80, 0),
                         "Pequena": (10, 2),
                         "Média": (5, 3),
                         "Grande": (3, 4),
                         "Alpinismo": (2, 5)}
        numero = uniform(0, 100)
        acumulado = 0
        for chave, valor in tiposMochilas.items():
            acumulado += valor[0]
            if numero <= acumulado:
                self.lootBonusMochila = valor[1]
                self.qtdeLootMax = self.lootBonusMochila + 2
                return chave

    def printarTudo(self):
        return f"""Infectado {self.tipo}\n
**Vida**: {self.vida}
**Força:** {self.forca}
**Destreza:** {self.destreza}
**Constituição:** {self.constituicao}
**Inteligencia:** {self.inteligencia}
**Sabedoria:** {self.sabedoria}
**Carisma:** {self.carisma}\n

**Mordida**:   {self.danoMordida} | **CD:** {self.cdMordida}
**Arranhao**: {self.danoArranhao} | **CD:** {self.cdArranhao}

{self.tratarHabilidades()}
**Mochila:** *{self.tipoMochila}*
```{self.tratarLoots()}```
.
.
.
"""

    def tratarLoots(self):
        texto = ""
        for i in self.loots:
            texto += '*' + ' ' + i + '\n'
        return texto

    def tratarHabilidades(self):
        texto = ""
        for i in self.habilidades:
            partido = i.split(":")
            nome = partido[0]
            descricao = partido[1]
            texto += '**' + nome + ':**' + ' *' + descricao.strip() + '*' + '\n'
        return texto

    def definirTipo(self):
        # "Nome": (Probabilidade, Atribut(min, max)
        tipos = {"Comum": (50, (1, 2), 2),
                 "Podre": (30, (-2, 0), 1),
                 "Raivoso": (20, (1, 3), 3)}
        numero = uniform(0, 100)
        acumulado = 0
        for chave, valor in tipos.items():
            acumulado += valor[0]
            if numero <= acumulado:
                self.variacao = valor[1]
                self.poder = valor[2]
                return chave

    def definirHabilidades(self):
        possiveis_habilidades = [
            'Acrobacia (DES) : habilidade de dar saltos mortais, estrelas, saltos acrobáticos,etc. Pode ser usada como defesa em combate.',
            'Armas Brancas (DES ou FOR): perícia genérica que envolve todos os tipos de armas brancas. Dependendo do tipo de aventura, pode-se criar uma perícia específica para cada tipo de arma branca (Espadas, Machados, Adagas, Chicotes, etc.).',
            'Armas de Energia (DES): perícia genérica que envolve todos os tipos de armas de energia (comuns em cenários e aventuras futuristas). Dependendo do tipo de aventura, pode-se criar uma perícia específica para cada tipo de arma de energia (Rifles Laser, Pistolas Laser, Sabres de Luz, etc.).',
            'Armas de Fogo (DES): perícia genérica que envolve todos os tipos de armas brancas. Dependendo do tipo de aventura, pode-se criar uma perícia específica para cada tipo de arma de fogo (Rifles, Pistolas, Armas Automáticas, Bazuca, etc.).',
            'Arte da Fuga (DES): habilidade para escapar de amarras, correntes ou algemas, rastejar por espaços apertados,etc.',
            'Atletismo (DES ou FOR): perícia genérica que abarca todos os tipos de atividade física de grande esforço, correr, nadar, arremessar peso, saltar,etc.',
            'Artes Marciais (DES): perícia genérica que envolve todos os tipos de artes marciais. Dependendo do tipo de aventura, pode-se criar uma perícia específica para cada tipo de arte marcial (Judô, Karatê, Jiu-jitsu, etc.).',
            'Arremessar (DES): habilidade de lançar objetos como lanças, maças, machados, etc.',
            'Bater Carteiras/Punga (DES): Habilidade para roubar sem ser percebido, requer grande destreza com as mãos.',
            'Briga (FOR ou DES) : luta de rua, sem técnica e brutal.',
            'Dirigir (DES): perícia genérica, condução de veículos automotores.',
            'Cavalgar (DES): andar a cavalo ou outro tipo de animal.',
            'Controle da Respiração (CON): habilidade de prender ou controlar a respiração, emoções, reduzir o dano de choques psíquicos ou perda de sanidade.',
            'Correr (DES): treinamento específico de corrida, perde menos PE (pontos de energia e corre mais rápido).',
            'Equilíbrio (DES): ser capaz de se equilibrar em superfícies estreitas, andar em cabo de aço, etc.',
            'Escalar (FOR ou DES): subir superfícies íngremes à uma velocidade igual ao Deslocamento/4.',
            'Esconder-se (DES ou INT): técnica de camuflar, esconder da vista do oponente, se ocultar nas sombras, passar despercebido.',
            'Estrangular (FOR): técnica de usar a força para matar alguém.',
            'Ferreiro (DES): habilidade de criar e reparar armas, escudos e armaduras de metal.',
            'Fugir (DES): habilidade de saber escapar correndo de um perigo.',
            'Furtividade (DES): aproximar-se sem ser notado por um inimigo, perseguir sem ser visto, andar silenciosamente.',
            'Levantamento de Peso (FOR): treinamento específico de atleta para levantar pesos.',
            'Luta Livre (FOR ou DES): arte marcial baseada em agarrões e submissões do oponente.',
            'Natação (FOR ou DES): saber nadar.',
            'Pilotar (DES): perícia genérica, habilidade de pilotar veículos aéreos e aquáticos, pode-se criar perícias específicas para cada tipo de veículo (submarino, navio, lancha, avião comercial, etc.).',
            'Saltar (FOR ou DES): técnica para dar saltos mesmo em condições adversas.',
            'Tolerância (CON): capacidade de resistir dor, fadiga, fome e sede.',
            'Resistência a Venenos (CON): habilidade de resistir os efeitos de venenos.',
            'Administração (INT): conhecimento de gerência, liderança, hierarquia corporativa, etc.',
            'Alquimia (INT): conhecimento alquímico, preparo de poções mágicas, talismãs, etc.',
            'Antropologia (INT): estudo do homem e da cultura humana, estudo de culturas primitivas e contemporâneas.',
            'Arrombamento (INT): saber abrir fechaduras, abrir portas, cofres, etc.',
            'Artilharia (INT): conhecimento de artilharia militar, artilharia antiaérea, etc.',
            'Biologia (INT): conhecimento acadêmico sobre os seres vivos.',
            'Camuflagem (INT): saber como se camuflar, esconder, criar disfarces, etc.',
            'Cartografia (INT): habilidade de criar mapas, de mapear locais desconhecidos, etc.',
            'Ciência Forense (INT): conhecimento técnico e acadêmico sobre causas dos crimes, causas de mortes, autópsias, etc.',
            'Ciências Proibidas/Ciências Ocultas (INT): ocultismo, arcanismo e outras ciências não oficiais, que envolvem temas tabus e proibidos como magia, demonologia, estudo dos espíritos, etc.',
            'Comércio (INT): perícia genérica que envolve barganha, negociação,reconhecer o melhor preço, etc.',
            'Computação (INT): conhecimento acadêmico ou técnico sobre computadores, análise de sistemas, programação, reparo.',
            'Conhecimento (INT): perícia genérica, pode ser usada junto com alguma área de conhecimento, para RPGs que não sejam muito investigativos, como Conhecimento Ciências Humanas, Técnico, Eletrônico, etc.',
            'Coletar Evidência (INT ou SAB): técnica de buscar pistas em cenas de crimes.',
            'Contabilidade (INT): conhecimento de balanço de pagamentos, finanças de empresas, imposto de renda, etc.',
            'Criptografia (INT): conhecimento de como quebrar ou criar códigos secretos.',
            'Criminologia (INT): estudo acadêmico sobre crimes, saber criar um perfil de um assassino, entender as motivações de um crime, etc.',
            'Cultura Popular (INT): conhecimento dos rumores, boatos, acontecimentos do mundo do entretenimento, cultura de massa, novelas, celebridades, etc.',
            'Direito (INT): conhecimento da legislação, conhecimento dos procedimentos legais, de como se defender e atacar em um tribunal, reconhecer ilegalidades.',
            'Disfarces (INT ou CAR): habilidade de criar disfarces, de se fazer passar por outra pessoa.',
            'Economia (INT): conhecimentos de economia, finanças nacionais, problemas econômicos.',
            'Eletrônica (INT): conhecimento de sistemas eletrônicos, criação, projeto, hacking, etc.',
            'Ensino (INT): conhecimento de didática, habilidade de dar aulas, de passar informações.',
            'Espionagem (INT): perícia genérica, conjunto de habilidades relacionadas com espiões, como instalação de câmeras secretas, perseguir sem ser visto, desarmar esquemas de segurança,etc.',
            'Escrever (INT): habilidade de escrever profissionalmente.',
            'Estratégia Militar (INT): conhecimento de táticas militares, capaz de reconhecer táticas militares do inimigo, descobrir pontos fracos, estabelecer táticas de combate eficazes.',
            'Explosivos (INT): armar e desarmar explosivos, criar bombas, etc.',
            'Exorcismo (INT ou CAR): sabe realizar rituais de exorcismo, conhece a ritualística, etc.',
            'Farmácia (INT): conhecimento sobre remédios, drogas, medicamentos.',
            'Falsificação (INT): habilidade de falsificar documentos, objetos de arte, dinheiro, etc.',
            'Finanças (INT): perícia genérica que envolve economia, contabilidade, e áreas que envolvem dinheiro como investimentos, taxas, etc.',
            'Fotografia (INT): habilidade técnica de bater fotos de nível profissional, analisar fotos, ampliar e trabalhar com imagens.',
            'Geologia (INT): estudo do solo, eras geológicas, etc.',
            'Hacking (INT): habilidade para invadir sistemas, criar vírus de computador, tomar controle de redes de telecomunicações, etc.',
            'Hipnose (INT): habilidade para afetar a mente de uma pessoa e torná-la mais fácil de ser manipulada.',
            'História (INT): estudo da história da humanidade, conhecimento de fatos históricos locais ou globais.',
            'Investigação (INT ou SAB): perícia genérica, habilidade técnica de reunir pistas, reunir evidências, deduzir, etc.',
            'Literatura (INT): conhecimento acadêmico de obras literárias, capacidade de interpretação profissional de obras de arte, conhecimento de história da literatura.',
            'Matemática (INT): estudo da ciência da matemática.',
            'Mecânica (INT): habilidade de criar e reparar equipamentos mecânicos, consertar veículos.',
            'Medicina (INT): conhecimento das artes médicas, realizar operações, tratar ferimentos, etc.',
            'Mitos de Cthulhu (INT): conhecimento dos inomináveis horrores cósmicos.',
            'Naturalista (INT): conhecimento acadêmico sobre a vida selvagem.',
            'Navegação (INT): sabe como conduzir uma embarcação, como se orientar em alto mar, etc.',
            'Ofícios (INT): perícia genérica para representar algum tipo de habilidade técnica como artesanato, escultura, ferraria, criação de animais, agricultura, joalheria, etc.',
            'Operar Submarino/Navio/Nave Espacial (INT): perícias específicas sobre como cuidar, operar, pilotar, o veículo indicado.',
            'Paleontologia (INT): estudo das formas de vida existentes no período préhistórico.',
            'Procurar (SAB): habilidade de vasculhar com atenção, notar pequenas diferenças, muito útil para investigadores.',
            'Primeiros Socorros (INT ou SAB): treinamento técnico de como proceder para estancar ferimentos, fazer os primeiros cuidados com os feridos, criar talas de emergência, etc.',
            'Psicologia (INT): conhecimento acadêmico de psicologia, e saber realizar terapias, hipnotizar, analisar e entender as motivações ocultas das ações dos indivíduos.',
            'Psiquiatria (INT): conhecimento acadêmico e técnico de psiquiatria, das doenças, problemas cerebrais, medicamentos, etc.',
            'Química (INT): conhecimento de reações químicas, produção de elementos químicos, etc.',
            'Rastreio (INT): saber rastrear, seguir rastros, perseguir uma presa ou pessoa.',
            'Religião (INT ou SAB): conhecimento teológico, de história das religiões, da ritualística, etc.',
            'Rituais Religiosos (INT): conhecimento de como realizar rituais religiosos.',
            'Senso de Direção (SAB): habilidade para distinguir as direções através do instinto.',
            'Sobrevivência (INT): habilidade de sobreviver em lugares selvagens, encontrar abrigo, caçar, conseguir alimento, reconhecer plantas venenosas.',
            'Sobrevivência Urbana (INT): capacidade de sobreviver em ambiente urbano, saber fontes de comida gratuita, andar pelo submundo, conseguir abrigo, conhecer os perigos da vida urbana dos sem-casa.',
            'Sociologia (INT): estudo das sociedades, de sua organização, estrutura, grupos sociais, ideologias, etc.',
            'Venenos (INT): saber criar, usar, identificar e neutralizar venenos.',
            'Veterinário (INT): tratar ferimentos e doenças de animais, conhecimento de biologia animal.',
            'Vontade (SAB): o personagem tem a Força de Vontade treinada, capaz de resistir ao medo, à hipnose, poderes mentais, etc.',
            'Artista (CAR): atuação em teatro, cinema, filmes, capacidade de atuar, pode ser para atores, dançarinos, artistas de circo, etc.',
            'Convencimento (CAR): convencer, mudar a opinião de outra pessoa.',
            'Contatos (CAR): aliados, amigos e informantes que o personagem pode acessar durante uma aventura, o mestre pede o teste de contatos com modificadores dependendo da familiaridade do personagem com o local onde busca contatos.',
            'Debate (CAR): habilidade de debater e vencer debates, duelos verbais.',
            'Diplomacia (CAR): realizar acordos, convencer pessoas, oferecer propostas e ter reações positivas.',
            'Empatia (CAR): habilidade de sentir e perceber o que os outros estão sentindo.',
            'Lidar com Animais (CAR): habilidade de domar, acalmar e lidar com animais.',
            'Manipulação (CAR): enganar, manipular, mentir de maneira convincente.',
            'Manha (INT ou CAR): Conhecimento das ruas, saber criar contatos, conseguir informações, conhecer o submundo, saber das gírias, dos grupos criminosos, etc.',
            'Mentir (CAR): habilidade de mentir de maneira convincente.',
            'Intimidação (CAR): habilidade para intimidar outras pessoas, causar medo e forçar sua autoridade nos outros.',
            'Falar em Público (CAR): habilidade de lidar com uma plateia e impressionar com suas palavras, sem sentir timidez.',
            'Sentir Motivação (CAR): saber se uma pessoa está mentindo, entender os sentimentos de uma pessoa.',
            'Sedução (CAR): habilidade para seduzir, manipular emocionalmente, fingir sentimentos amorosos de maneira convincente, charme.']
        for i in range(self.poder):
            self.habilidades.append(choice(possiveis_habilidades))

    def calcularAtributos(self):
        min = self.variacao[0]
        max = self.variacao[1]
        self.forca = randint(min, max)
        self.destreza = randint(min, max)
        self.constituicao = randint(min, max)
        self.inteligencia = randint(min, max)
        self.sabedoria = randint(min, max)
        self.carisma = randint(min, max)

    def calcularVida(self):
        bonus = 0
        match self.constituicao:
            case 3:
                bonus = 5
            case 4:
                bonus = 10
            case 5:
                bonus = 15
            case _:
                bonus = 0
        return 10 + self.constituicao + bonus
