from _typeshed import Self
from typing import Set

class Arc:
    def __init__(self, a :str, b:str,label:str = "")->None:
        self.begin = a
        self.end = b
        self.label = label

class Node:
    def __init__(name:str)->None:
        self.name = name
    
class Network:
    def __init__(self, *args)->None:
        N : Set(Node) = set()
        A: Set(Arc) = set()
        
    def __add_fictitious_node(input, output)->None:
        pass
    
    def __mark_arcs()->None:
        pass
    
    def build_fictitious_network()->Network:
        pass

if __name__=="__main__":
    pass