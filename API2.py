class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, preco):
        self.produtos.append({"nome": nome, "preco": preco})

    def calcular_total(self):
        return sum(produto["preco"] for produto in self.produtos)

class Recibo:
    
    def imprimir(produtos, total):
        print("=== RECIBO ===")
        for produto in produtos:
            print(f"{produto['nome']}: R${produto['preco']:.2f}")
        print(f"Total: R${total:.2f}")

class EmailService:
    
    def enviar(cliente, total):
        print(f"E-mail enviado para {cliente}: Seu pedido no valor de R${total:.2f} foi confirmado!")


carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto("Camiseta", 50.0)
carrinho.adicionar_produto("Calça", 120.0)

total = carrinho.calcular_total()
Recibo.imprimir(carrinho.produtos, total)
EmailService.enviar("joao@email.com", total)