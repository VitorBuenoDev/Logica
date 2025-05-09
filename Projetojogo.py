class Jogo:
    def __init__(self, titulo, genero, classificacao_etaria, preco):
        self.titulo = titulo
        self.genero = genero
        self.classificacao_etaria = classificacao_etaria
        self.preco = preco

    def exibir_detalhes(self):
        print("=== Detalhes do Jogo ===")
        print(f"Título: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Classificação Etária: {self.classificacao_etaria}")
        print(f"Preço: R${self.preco:.2f}")


class Jogador:
    def __init__(self, nickname, id_jogador, biblioteca_de_jogos=None, saldo_carteira=0.0):
        self.nickname = nickname
        self.id_jogador = id_jogador
        self.biblioteca_de_jogos = biblioteca_de_jogos if biblioteca_de_jogos is not None else []
        self.saldo_carteira = saldo_carteira

    def exibir_perfil(self):
        print("=== Perfil do Jogador ===")
        print(f"Nickname: {self.nickname}")
        print(f"ID: {self.id_jogador}")
        print(f"Saldo na carteira: R${self.saldo_carteira:.2f}")
        print("Jogos na biblioteca:")
        if self.biblioteca_de_jogos:
            for jogo in self.biblioteca_de_jogos:
                print(f"- {jogo.titulo}")
        else:
            print("Nenhum jogo na biblioteca.")

    
    def adicionar_jogo_biblioteca(self, jogo_comprado):
        self.biblioteca_de_jogos.append(jogo_comprado)
        print(f"O jogo '{jogo_comprado.titulo}' foi adicionado à biblioteca de {self.nickname}.")


    def adicionar_saldo(self, valor):
        if valor > 0:
            self.saldo_carteira += valor
            print(f"Saldo de {self.nickname} foi aumentado em R${valor:.2f}. Novo saldo: R${self.saldo_carteira:.2f}")
        else:
            print("Valor inválido! O valor a ser adicionado deve ser positivo.")


    def debitar_saldo(self, valor):
        if valor > 0 and valor <= self.saldo_carteira:
            self.saldo_carteira -= valor
            print(f"Débito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo_carteira:.2f}")
            return True
        elif valor > self.saldo_carteira:
            print("Saldo insuficiente para o débito.")
            return False
        else:
            print("Valor inválido! O valor a ser debitado deve ser positivo.")
            return False

class PlataformaDeJogos:
    def __init__(self, nome_plataforma, catalogo_de_jogos, jogadores_cadastrados):
        self.nome_plataforma = nome_plataforma
        self.catalogo_de_jogos = catalogo_de_jogos
        self.jogadores_cadastrados = jogadores_cadastrados


    def adicionar_jogo_catalogo(self, jogo):
        self.catalogo_de_jogos.append(jogo)
        print(f"O jogo '{jogo.titulo}' foi adicionado ao catálogo.")

    def adicionar_jogador_(self, jogo):
        self.catalogo_de_jogos.append(jogo)
        print(f"O jogo '{jogo.titulo}' foi adicionado ao catálogo.")



jogo1 = Jogo("Mario Kart", "Corrida", "Livre", 49.90)
jogo2 = Jogo("FNAF", "Terror", "+14", 16.90)

jogador1 = Jogador("Xerebebe13", 3123)

jogador1.adicionar_jogo_biblioteca(jogo1)
jogador1.adicionar_jogo_biblioteca(jogo2)

jogador1.adicionar_saldo(96)
jogador1.debitar_saldo(41)

catalogo_de_jogos = PlataformaDeJogos

catalogo_de_jogos.adicionar_jogo_catalogo(jogo1, jogo2)



jogador1.exibir_perfil()
