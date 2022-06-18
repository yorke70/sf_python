class Client:
    def __init__(self, name, sirname, city, balance):
        self.name = name
        self.sirname = sirname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.name} {self.sirname}. {self.city}. Баланс: {self.balance} руб."

    def get_client(self):
        return f"{self.name} {self.sirname}, г. {self.city}"

client_1 = Client("Иван", "Петров", "Москва", 50)
client_2 = Client('Владимир','Зайцев','Кострома',50)
client_3 = Client('Олеся','Янина','Новосибирск',50)

clients =[client_1, client_2, client_3]

for guest in clients:
    print(guest.get_client())
