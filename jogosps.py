class Jogos:
    def __init__(self, nome="", modelo="", preco="", ativo=False):
        self.nome = nome
        self.modelo = modelo
        self.preco = preco
        self.ativo = ativo

jogo_Heric = Jogos(nome="Jogo resident evil 4", modelo="Modelo playstation 2", preco="R$200", ativo=False)
jogo_Eduardo = Jogos(nome="Jogo god of war", modelo="Modelo playstation 1", preco="R$150", ativo=True)

jogo_Heric.nome = "Jogo C"
jogo_Heric.modelo = "Modelo Z"
jogo_Heric.preco = "R$200"
jogo_Heric.ativo = False

jogos = [jogo_Eduardo, jogo_Heric]

for jogo in jogos:
    print(f"Nome: {jogo.nome}, Modelo: {jogo.modelo}, Preço: {jogo.preco}, Ativo: {jogo.ativo}")
