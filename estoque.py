class Armazenamento:
    def __init__(self) -> None:
        self.estoque = [{'Produto1':250},{'Produto2':110}]

    def add_item(self,lista):
        self.estoque.append(lista)




if __name__ == "__main__":
    arm = Armazenamento()
    print(arm.estoque[0])
    arm.add_item({"Produto3":235})
    print(arm.estoque)