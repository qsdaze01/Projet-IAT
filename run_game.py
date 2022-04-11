from time import sleep
from game.SpaceInvaders import SpaceInvaders
from controller.keyboard import KeyboardController
from controller.random_agent import RandomAgent
from controller.IA_agent import IA_agent
import sys

def main():

    if len(sys.argv) < 4:
        print("Pas le bon nombre d'argument : Nom_fichier alpha epsilon gamma")
        exit()
    else:
        alpha = sys.argv[1]
        epsilon = sys.argv[2]
        gamma = sys.argv[3]


    game = SpaceInvaders(display=True)
    #controller = KeyboardController()
    #controller = RandomAgent(game.na)
    controller = IA_agent(game, alpha, epsilon, gamma)
    game.get_state()
    state = game.reset()
    cumul = 0
    is_done = False
    while True:
        

        action = controller.select_action()
        previous_state = state
        state, reward, is_done = game.step(action)
        controller.updateQ(previous_state, action, reward, state)
        sleep(0.0001)
        
        if is_done == True:
            #controller.printStates()
            print(is_done)
            game.reset()
            is_done = False
            continue

        # Pour print Q
        """cumul += 1
        if cumul == 100:
            cumul = 0
            controller.printQ()"""

if __name__ == '__main__' :
    main()
