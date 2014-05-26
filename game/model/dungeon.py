class Dungeon:
    
    def __init__(self, hash, start, end, rooms):
        self.hash = hash
        self.start = start
        self.end = end
        self.rooms = rooms

    @classmethod
    def from_xml(cls, xml):
        return cls('xml', 0, 0, [])

class Room:
    
    def __init__(self, id, goal, north, south, east, west, enemies):
        self.id = id
        self.goal = goal
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.enemies = enemies
        
    @classmethod
    def from_xml(cls, xml):
        return cls(0, 0, -1, -1, -1, -1, [])