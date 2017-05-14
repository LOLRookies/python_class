directions = ['east', 'south', 'west', 'north']

class Passat(object):
    def __init__(self, name, color):
        self.owner = name
        self.miles = 0
        self.age = 0
        self.color = color
        self.speed = 0
        self.direction = 0
        self.started = False

    def start(self):
        self.started = True

    def stop(self):
        self.brake()
        self.started = False

    def brake(self):
        if self.started:
            self.speed = 0

    def turn(self, left_right):
        # left_right: True -> left, False -> right
        if self.started:
            if left_right:
                self.direction -= 1
            else:
                self.direction += 1

            self.direction += len(directions)
            self.direction %= len(directions)

    def get_direction(self):
        return directions[self.direction]

    def reverse(self):
        if self.started:
            self.direction += 2
            self.direction %= len(directions)

    def accelerate(self, speed_difference):
        if self.started:
            self.speed += speed_difference

    def decelerate(self, speed_difference):
        if self.started:
            self.speed -= speed_difference

    @classmethod
    def info(cls):
        print 'Passat is a model of Volkswagen. It is very good.'


yujie_passat = Passat('yujie', 'black') # 1. create Passat object, and assign to yujie_passat var 2. call yujie_passat.__init__()
chi_passat = Passat('chi', 'white')

#print yujie_passat.owner, yujie_passat.color
#print chi_passat.owner, chi_passat.color

#yujie_passat.info()
#chi_passat.info()

Passat.info()
yujie_passat.info()

#yujie_passat.start()
#yujie_passat.accelerate(100)
#yujie_passat.stop()
#yujie_passat.decelerate(50)
#print yujie_passat.speed



#yujie_passat.reverse()
#yujie_passat.reverse()
#yujie_passat.reverse()
#print yujie_passat.direction
#print yujie_passat.get_direction()

#for i in range(10):
#    yujie_passat.turn(True)
#print yujie_passat.get_direction()



#yujie_passat.start()
#chi_passat.start()
#chi_passat.accelerate()