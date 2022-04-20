from time import sleep
from game.SpaceInvaders import SpaceInvaders
from controller.keyboard import KeyboardController
from controller.random_agent import RandomAgent
from controller.IA_agent import IA_agent
import sys
import csv

def main():

    # Gestion des arguments
    if len(sys.argv) < 5:
        print("Pas le bon nombre d'argument : Nom_fichier alpha epsilon gamma nb_iterations")
        exit()
    else:
        alpha = sys.argv[1]
        epsilon = sys.argv[2]
        gamma = sys.argv[3]
        nb_iterations = sys.argv[4]

    # Gestion écriture CSV
    filename = 'states.csv'
    header = ['score','episode']
    f = open(filename,'w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

    game = SpaceInvaders(display=False)
    #controller = KeyboardController()
    #controller = RandomAgent(game.na)
    controller = IA_agent(game, alpha, epsilon, gamma)
    game.get_state()
    state = game.reset()
    
    # Initialisation des paramètres
    count_episodes = 0
    count_reward = 0
    is_done = False

    # Boucle des épisodes
    while count_episodes < int(nb_iterations):
        
        # Print des paramètres
        print("Episodes : " + str(count_episodes))
        print("Reward : " + str(count_reward))
        controller.print_epsilon()

        # MAJ des paramètres
        count_frames = 0
        count_episodes += 1
        count_reward = 0
        controller.MAJ_epsilon()

        print(len(controller.states))

        # Boucle des frames
        while count_frames < 5000:

            # Choix des actions et MAJ de Q
            action = controller.select_action()
            previous_state = state
            state, reward, is_done = game.step(action)
            controller.updateQ(previous_state, action, reward, state)
            # sleep(0.0001)
            
            # Actualisation des paramètres
            count_reward += reward
            count_frames += 1
            
            # Cas où l'IA perd
            if is_done == True:
                #controller.printStates()
                print(is_done)
                game.reset()
                count_frames = 0
                is_done = False
                break

            # Pour print Q
            """cumul += 1
            if cumul == 100:
                cumul = 0
                controller.printQ()"""

    # Ecriture dans le CSV
    controller.write_Q_CSV(f, filename)

if __name__ == '__main__' :
    main()
