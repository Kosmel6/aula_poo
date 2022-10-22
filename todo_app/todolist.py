from user import User
from todoitem import TodoItem

class TodoList:
    def __init__(self, owner: User):
        self.owner = owner
        self.list = []

    def add(self, item: TodoItem):
        tamanho = len(self.list)
        i = 0;
        for i in range(tamanho):
            if self.list[i] == item:
                self.list.remove(item);
                i = tamanho;
        i = 0;
        for i in range(tamanho):
            if self.list[i+1].nivel > item.nivel:
                self.list.insert(i, item);
                i = tamanho;

    def get(self, index):
        return self.list[index]

    def get_owner(self):
        return self.owner

    def complete_item(self, index):
        self.list[index].complete()

    def remove(self, index):
        self.list.pop(index)

    def size(self):
        return len(self.list)

    def find(self, description):
        for item in self.list:
            if item.description == description:
                return item

    def verify(self):
        ordenado = 2;
        for item_array in self.list:
            if (item_array.nivel < valor):
                ordenado = 0;
                return ordenado;
            valor = item_array.nivel
        orneado = 1
        return ordenado;

