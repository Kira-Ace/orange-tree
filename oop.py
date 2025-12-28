class Land():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
Land = Land(4)
    
people = ["Jazz", "Sofia", "Clem", "Kiko", "Whatchamarit"]
    
for person in people:
    if Land.add_passengers(person):
        print(f"Added {person} to car successf  ully")
    else:
        print(f"No available seats for {person}")