class Biblioteca:
    def __init__(self):
        self.__itens = []

    def adicionar_item(self, item):
        self.__itens.append(item)
        print(f"Item '{item.get_titulo()}' adicionado com sucesso!")