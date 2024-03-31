class Town:
    def __init__(self, name: str):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town1 = Town("")
print(town1)  # Town: ExampleTown | Latitude: 0°N | Longitude: 0°E

town1.set_latitude("30°N")
town1.set_longitude("45°E")
print(town1)  # Town: ExampleTown | Latitude: 30°N | Longitude: 45°E
