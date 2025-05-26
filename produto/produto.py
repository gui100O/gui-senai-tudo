class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def comprar(self, qtd):
        if qtd <= self.estoque:
            self.estoque -= qtd
            print(f"Compra realizada de {qtd} unidade(s) de {self.nome}.")
        else:
            print(f"Estoque insuficiente para {self.nome}.")

    def repor(self, qtd):
        self.estoque += qtd
        print(f"Reposição de {qtd} unidade(s) de {self.nome} realizada.")

    def mostrar_estoque(self):
        print(f"Estoque atual de {self.nome}: {self.estoque} unidades.")
