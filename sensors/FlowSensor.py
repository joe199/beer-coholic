from sensors import Sensor

class FlowSensor(Sensor):
    """Sensor class, reads file sensors"""
    def __init__(self, name = "FlowSensor"):
        super(FlowSensor, self).__init__(name)
        #self.arg = arg

    def setup(self):
        print "Prepare the class:"

    def get_data(self, dataread):
        print "Data read by the sensor:", dataread

    def get_cumulative(self):
        print "Response: ", response

    def reset_cumulative(self):
        print "Reset"
