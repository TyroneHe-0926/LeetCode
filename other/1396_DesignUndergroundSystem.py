from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.history = defaultdict(dict)
        self.duration = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.history[id] = {
            "station": stationName,
            "time": t
        }

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.history[id]["station"], self.history[id]["time"]
        duration = t - start_time
        key = f'{start_station} {stationName}'
        self.duration[key].append(duration)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = f'{startStation} {endStation}'
        times = self.duration[key]
        return round(sum(times)/len(times), 5)

usystem = UndergroundSystem()
usystem.checkIn(47,'Waterloo',10)
usystem.checkOut(47,'Toronto',25)
usystem.checkIn(47,'Toronto',40)
usystem.checkOut(47,'Waterloo',80)
usystem.checkIn(47,'Waterloo',100)
usystem.checkOut(47,'Toronto',135)
print(usystem.getAverageTime('Waterloo','Toronto'))
print(usystem.getAverageTime('Toronto','Waterloo'))