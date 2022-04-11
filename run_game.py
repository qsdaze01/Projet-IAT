from time import sleep
from game.SpaceInvaders import SpaceInvaders
from controller.keyboard import KeyboardController
from controller.random_agent import RandomAgent
from controller.IA_agent import IA_agent

def main():

    game = SpaceInvaders(display=True)
    #controller = KeyboardController()
    #controller = RandomAgent(game.na)
    controller = IA_agent()
    game.get_state()
    state = game.reset()
    while True:
        action = controller.select_action(state)
        state, reward, is_done = game.step(action)
        sleep(0.0001)

if __name__ == '__main__' :
    main()
