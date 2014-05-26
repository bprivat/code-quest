class Enemy:
    
    def __init__(self, id):
        self.id = id
        
    @classmethod
    def from_xml(cls, xml):
        return cls(0)