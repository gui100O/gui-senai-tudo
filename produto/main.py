from produto import Produto

produto1 = Produto("Notebook", 3000.00, 10)

produto1.mostrar_estoque()
produto1.comprar(3)
produto1.mostrar_estoque()
produto1.comprar(10)
produto1.repor(5)
produto1.mostrar_estoque()
