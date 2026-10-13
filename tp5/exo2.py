class Airplane : 
    fly = False
    def __init__ (self, name : str) :
        self.name = name
        self.fly = False
    def take_off(self):
        self.fly = True
    def land(self):
        self.fly = False
    def __str__(self):
        status = "flying" if self.fly else "ground"
        return f"Airplane {self.name} - {status}"

class MilitaryAircraft(Airplane) :
    def __init__ (self, name : str, mission : str) :
        super().__init__(name)
        self.mission = mission
    def __str__ (self) :
        status = "flying" if self.fly else "ground"
        mission = self.mission if self.mission else "no mission"
        return f"MilitaryAircraft {self.name} - {status} - {mission}"

class CargoAircraft(Airplane) :
    def __init__ (self, name : str, shipment : str) :
        super().__init__(name)
        self.shipment = shipment
    def __str__ (self) :
        status = "flying" if self.fly else "ground"
        shipment = self.shipment if self.shipment else "no shipment"
        return f"CargoAircraft {self.name} - {status} - {shipment}"

class CivilAircraft(Airplane) :
    def __init__ (self, name : str, nb_passenger : int = 0) :
        super().__init__(name)
        self.nb_passenger = nb_passenger
    def passenger_enter(self, nb: int):
        self.nb_passenger += nb
    def passenger_leave(self, nb: int):
        self.nb_passenger = max(0, self.nb_passenger - nb)
    def __str__ (self) :
        status = "flying" if self.fly else "ground"
        if self.nb_passenger > 0 : 
            passengers = f"{self.nb_passenger} passengers"
        else :
            passengers = "no passengers"
        return f"CivilAircraft {self.name} - {status} - {passengers}"

class Airport :
    def __init__(self):
        self.militaryPlanes = []
        self.cargoPlanes = []
        self.civilPlanes = []
    def add_military (self, plane : MilitaryAircraft): 
        self.militaryPlanes.append(plane)
    def add_cargo (self, plane : CargoAircraft) :
        self.cargoPlanes.append(plane)
    def add_civil (self, plane : CivilAircraft) :
        self.civilPlanes.append(plane)
    def __str__(self):
        lines = ["[Airport]"]
        for plane in self.civilPlanes:
            lines.append(str(plane))
        for plane in self.cargoPlanes:
            lines.append(str(plane))
        for plane in self.militaryPlanes:
            lines.append(str(plane))
        return "\n".join(lines)

if __name__ == "__main__":
    airportBaleMulhouse = Airport()
    avion1 = CivilAircraft("Airbus 380", 0)
    avion2 = CargoAircraft("A300", "")
    avion3 = MilitaryAircraft("Mig 21", "")
    print(avion1)
    print(avion2)
    print(avion3)
    airportBaleMulhouse.add_civil(avion1)
    airportBaleMulhouse.add_cargo(avion2)
    airportBaleMulhouse.add_military(avion3)
    avion1.passenger_enter(150)
    avion1.take_off()
    avion4 = MilitaryAircraft("RTX5", "")
    avion4.mission = "rescue hostages"
    avion4.take_off()
    airportBaleMulhouse.add_military(avion4)
    print(airportBaleMulhouse)