class Notebook:
    def __init__(self, ram, memory, cpu):
        self.ram = ram
        self.memory = memory
        self.cpu = cpu

    def info(self):
        return f"Ноутбук с {self.ram} ГБ оперативной памяти, {self.memory} ГБ внутренней памяти и с {self.cpu} ядрами процессора" 
    
    def add_notebook(self, dic):
        self.dic = dic
        
        return self.dic
           
        
dic={
    "ram": 12,
    "memory": 500,
    "cpu": 4
}
hp = Notebook(dic["ram"], dic["memory"], dic["cpu"])
print(hp.info())
print(hp.add_notebook(dic))