class Station:
    def __init__(self, name):
        self.name = name
        self.lines = []

    def add_lines(self, line_name):
        if line_name not in self.lines:
            self.lines.append(line_name)

    def __repr__(self):
        return f"Station(name='{self.name}', lines={self.lines})" 
    
    @staticmethod
    def list_stations(stations_dict):
        print("Available Stations:")
        for station in stations_dict:
            print(f"- {station}")
