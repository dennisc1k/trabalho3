class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, preco):
        self.produtos.append({"nome": nome, "preco": preco})

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto["preco"]
        return total

    def imprimir_recibo(self):
        print("=== RECIBO ===")
        for produto in self.produtos:
            print(f"{produto['nome']}: R${produto['preco']:.2f}")
        print(f"Total: R${self.calcular_total():.2f}")

    def enviar_email(self, cliente):
        print(f"E-mail enviado para {cliente}: Seu pedido no valor de R${self.calcular_total():.2f} foi confirmado!")


carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto("Camiseta", 50.0)
carrinho.adicionar_produto("Calça", 120.0)
carrinho.imprimir_recibo()
carrinho.enviar_email("victor@email.com")