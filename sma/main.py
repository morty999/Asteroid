import random
from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("agents", [])
    core.memory("item", [])

    print("Setup END-----------")


def computePerception(agent):
    pass


def computeDecision(agent):
    pass


def applyDecision(agent):
    pass


def run():
    core.cleanScreen()
    
    #Display
    for agent in core.memory("agents"):
        agent.show()
    
    for item in core.memory("item"):
        item.show()
        
    for agent in core.memory("agents"):
        computePerception(agent)
        
    for agent in core.memory("agents"):
        computeDecision(agent)
    
    for agent in core.memory("agents"):
        applyDecision(agent)
    
    
    
    
     
core.main(setup, run)
