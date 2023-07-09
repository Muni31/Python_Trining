# Abstraction Eg-1
from abc import ABC, abstractmethod

class OS(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass
    
class Windows(OS):
    def start(self):
        return "Opening Windows..."

    def shutdown(self):
        return "Shutting down Windows..."

class Linux(OS):
    def start(self):
        return "Opening Linux..."

    def shutdown(self):
        return "Shutting down Linux..."
    
class Mac(OS):
    def start(self):
        return "Opening MacBook..."

    def shutdown(self):
        return "Shutting down MacBook..."

windows = Windows()
linux = Linux()
mac=Mac()

print(windows.start()) 
print(windows.shutdown())
print(mac.start()) 
print(mac.shutdown())
print(linux.start())  
print(linux.shutdown())  
