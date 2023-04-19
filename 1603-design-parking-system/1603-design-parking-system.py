class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big
        self.medium =medium
        self.small = small

    def addCar(self, carType):
        if carType==1:
            while self.big:
                self.big -= 1
                return True
            if self.big == 0:
                return False
        if carType==2:
            while self.medium:
                self.medium -= 1
                return True
            if self.medium == 0:
                return False
        if carType==3:
            while self.small:
                self.small -= 1
                return True
            if self.small == 0:
                return False