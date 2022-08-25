# Singleton, __call__, __repr__, @property, getter, setter, deleter

class My_class:
    __instances = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instances is None:
            cls.__instances = super().__new__(cls)
        return cls.__instances
    
    def __del__(self):
        cls__instances = None
    
    def __init__(self, val_1, val_2):
        self.val_1 = val_1
        self.val_2 = val_2
        
    def __call__(self, *args, **kwargs):
        return self.val_1 + self.val_2
        
    def __repr__(self):
        return f'{self.val_1} and {self.val_2} are features of your instance'
    
    @property
    def some_method(self):
        return self.val_1 * self.val_2
    
    def get_val_1(self):
        return self.val_1
    
    def get_val_2(self):
        return self.val_2
    
    def set_values(self, new_val_1, new_val_2):
        self.val_1 = new_val_1
        self.val_2 = new_val_2        
        
    def clear_values(self):
        self.val_1 = 0
        self.val_2 = 0     
#____________________________________________________ 
class New_class():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name_person(self):
        return self.name
    
    @name_person.setter
    def name_person(self, name):
        self.name = name
    
    @name_person.deleter
    def name_person(self):
        self.name = None
        
if __name__ == '__main__':
    a = New_class("Oleg", 35)
    b = a.name
    print(b)
    a.name = "Alex"
    print(a.name)
    del a.name
    print(a.name)
