class Supplier:
    __name : str
    __address: str
    __phone : str
    __email: str
    __id: int
    
    def __init__(self, id, name, address, phone, email):
        self.__id = id 
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email
        
    def GetId(self):
        return self.__id
        
    def GetName(self):
        return self.__name
    
    def GetAddress(self):
        return self.__address
    
    def GetPhone(self):
        return self.__phone
    
    def GetEmail(self):
        return self.__email
