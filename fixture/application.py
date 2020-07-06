from fixture.frontol_reg import FrontolReg
from fixture.transport import Transport
from fixture.scaner import Scaner

class Application:

    def __init__(self, target, scaner_port=None, scaner_boundrate=9600):
        transport = Transport(address=target)
        scaner = None
        if scaner_port != None:
            scaner = Scaner(port=scaner_port, baudrate=scaner_boundrate)

        self.frontol_registration = FrontolReg(transport, scaner)