
class Singleton:
    """
    The Singleton pattern ensures that a class has only one instance 
    and provides a global access point to that instance.

    Why use it?
    - Avoid creating multiple instances of the same class, saving memory.
    - Useful for managing shared resources like database connections, logging, or configuration settings.
    - Ensures consistency by providing a single point of access to shared data or services.
    """
    
    __instance = None #class  private method 
    
    @staticmethod
    def get_instance():
        '''checking if instate was created'''
        if  Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self):
        '''checking if __instance is initialized'''
        if Singleton.__instance != None:
            raise Exception("Single exists already!")
        else:
            Singleton.__instance = self
        

s1 = Singleton.get_instance()
print(s1)
s1.x = 5
s2 = Singleton.get_instance()
print(s1.x)
print(s2.x)
print(s2)
