
import time


class TrafficLight:

    __colour = ['red', 'yellow', 'green']

    def get_colours(self):
        return self.__colour

    def running(self):
        current_colour = self.get_colours()[0]
        print(current_colour)
        time.sleep(7)
        current_colour = self.get_colours()[1]
        print(current_colour)
        time.sleep(2)
        current_colour = self.get_colours()[2]
        print(current_colour)
        time.sleep(6)
        return 'Cycle is over'


run_traffic = TrafficLight()
print(run_traffic.running())