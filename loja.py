import estoque
import os 
armazenamento = estoque.Armazenamento()



class Loja:
    def __init__(self,name:str = None) -> None:
        self.produto:list[dict] = []
        self.lista_estoque = armazenamento.estoque
        self.name = name


    def add_produto(self,lista:list[dict]) -> list:
        for p in lista:
            armazenamento.add_item(p)
    def clear(self):
        os.system('clear')

        
    def show_list(self):
        self.clear()
        print(f"Itens das lojas {self.name}")
        for i in self.lista_estoque:
            for p,v in i.items():
                print(f'{p} = {v}R$')
        print('-------------')
            
        


if __name__ == "__main__":
    lista_ = [{"produto3":195}]
    casas_bahia = Loja()
    casas_bahia.show_list()
    casas_bahia.add_produto(lista_)
    casas_bahia.show_list()
    