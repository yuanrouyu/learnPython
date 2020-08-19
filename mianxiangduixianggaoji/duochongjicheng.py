class animal(object):
    pass
class mammal(animal):
    pass
class bird(animal):
    pass
class  dog(mammal):
    pass
class bat(mammal):
    pass
class parrot(bird):
    pass
class ostrich(bird):
    pass
class runnableMixIn(object):
    def run(self):
        print('running')
class flyanleMixIn(self):
    def fly(self):
        print('flying')
class dog(mammal,runnableMixIn):
    pass
class bat(mammal,flyableMixIn):
    pass


class MyTCPServer(TCPServer, ForkingMixIn):
    pass
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
class MyTCPServer(TCPServer, CoroutineMixIn):
    pass