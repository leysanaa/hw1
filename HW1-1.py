class Time:
    def __init__(self, time_str):
        self.time_str = time_str
        self.total_seconds = self.convert_seconds(time_str)

    def convert_seconds(self, time_str):
        minutes = time_str.split(":")[0]
        rest= time_str.split(":")[1]
        seconds = rest.split(".")[0]
        milliseconds = rest.split(".")[1]

        minutes = int(minutes)
        seconds = int(seconds)
        milliseconds = int(milliseconds)

        total_seconds = minutes * 60 + seconds + milliseconds / 1000
        return total_seconds

    def __str__(self):
        return f"Time: {self.time_str}, Total Seconds: {self.total_seconds:.3f}"
    def __lt__(self, other):
        if self.total_seconds< other.total_seconds:
            return True
        else:
            return False


class Athlete:
    def __init__(self,name, team, place, time):
        self.name = name
        self.team = team
        self.place = place
        self.time = time 
    def use_time_method(self,other):
        return self.time < other.time


athlete1= Athlete("ley", "loomis","third","13:97.89" )
athlete2= Athlete("max", "loomis","second","12:21.99" )



string = "12:54.82"
string2 = "15:99.00"
convertor = Time(string)
print(convertor)
print( string<string2)
print(athlete1.time<athlete2.time)