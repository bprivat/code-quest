class Dungeon:
    
    def __init__(self, _hash, start, end, rooms):
        self.hash = _hash
        self.start = start
        self.end = end
        self.rooms = rooms

    @staticmethod
    def from_xml(xml):
        return Dungeon('xml', 0, 0, [])


class Room:
    
    def __init__(self, _id, goal, north, south, east, west, enemies):
        self.id = _id
        self.goal = goal
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.enemies = enemies
        
    @classmethod
    def from_xml(cls, xml):
        return cls(0, 0, -1, -1, -1, -1, [])