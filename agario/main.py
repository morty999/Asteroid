import core
from agario.partie import Partie


def setup():
    print("start setup")
    core.WINDOW_SIZE=[800,600]
    core.fps =60

    core.memory("partie",Partie())
    core.memory("partie").addPlayer()
    core.memory("partie").addBots()
    print("end setup")

def run():
    print("start run")
    core.cleanScreen()
    core.printMemory()
    core.memory("partie").show()
    print("end run")

core.main(setup,run)
