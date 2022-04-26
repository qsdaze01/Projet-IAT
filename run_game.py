from re import T
from time import sleep
from game.SpaceInvaders import SpaceInvaders
from controller.keyboard import KeyboardController
from controller.random_agent import RandomAgent
from controller.IA_agent import IA_agent
from controller.stupid_agent import StupidAgent
import sys
import csv

def main():

    # Gestion des arguments
    if len(sys.argv) < 6:
        print("Pas le bon nombre d'argument : Nom_fichier alpha epsilon gamma nb_iterations apprentissage")
        exit()
    else:
        alpha = sys.argv[1]
        epsilon = sys.argv[2]
        gamma = sys.argv[3]
        nb_iterations = sys.argv[4]
        apprentissage = sys.argv[5]

    # Choix du mode de test de l'apprentissage
    if int(apprentissage) == 0:

        filename = 'Q.csv'
        f = open(filename,'r')

        game = SpaceInvaders(display=True)

        controller = IA_agent(game, alpha, epsilon, gamma)

        controller.read_Q_CSV(f, filename)

        game.get_state()
        state = game.reset()

        f.close()

        while(True):
            sleep(0.0001)
            action = controller.select_action()
            state, reward, is_done = game.step(action)
    
    # Choix du mode apprentissage
    else :

        # Gestion écriture CSV
        filename_Q = 'Q.csv'
        header = ['score','episode']
        f_Q = open(filename_Q,'w')
        writer = csv.writer(f_Q)
        writer.writerow(header)
        f_Q.close()

        filename_states = 'states.csv'
        header = ['score','episode']
        f_states = open(filename_states,'w')
        writer = csv.writer(f_states)
        writer.writerow(header)
        f_states.close()

        filename_reward = 'reward.csv'
        f_reward = open(filename_reward,'w')
        writer = csv.writer(f_reward)
        f_reward.close()

        # Lancement du jeu
        game = SpaceInvaders(display=False)
        #controller = KeyboardController()
        #controller = RandomAgent(game.na)
        #controller = StupidAgent(game, alpha, epsilon, gamma)
        controller = IA_agent(game, alpha, epsilon, gamma)
        game.get_state()
        state = game.reset()
        
        # Initialisation des paramètres
        count_episodes = 0
        count_reward = 0
        is_done = False
        tab_reward = []

        # Boucle des épisodes
        while count_episodes < int(nb_iterations):
            
            # Print des paramètres
            print("Episodes : " + str(count_episodes))
            print("Reward : " + str(count_reward))
            controller.print_epsilon()
            
            # MAJ des paramètres
            tab_reward.append(count_reward)
            count_frames = 0
            count_episodes += 1
            count_reward = 0
            controller.MAJ_epsilon(int(nb_iterations), count_episodes)

            # Boucle des frames
            while count_frames < 1000000:

                # Choix des actions et MAJ de Q
                action = controller.select_action()

                # Gestion du bug
                if action == -1 :
                    previous_state = state
                    state, reward, is_done = game.step(3)
                    game.get_state()
                    state = game.reset()
                    count_frames = 0
                    is_done = False
                    break

                previous_state = state
                state, reward, is_done = game.step(action)

                # Cas où l'IA perd
                if is_done == True:
                    print(is_done)
                    controller.updateQ(previous_state, action, -100, state)
                    game.get_state()
                    state = game.reset()
                    count_frames = 0
                    is_done = False
                    break

                controller.updateQ(previous_state, action, reward, state)
                #sleep(0.0001)
                
                # Actualisation des paramètres
                count_reward += reward
                count_frames += 1


        # Ecriture dans le CSV
        controller.write_Q_CSV(f_Q, filename_Q)
        controller.write_states_CSV(f_states, filename_states)
        controller.write_reward_CSV(f_reward, filename_reward, tab_reward)

if __name__ == '__main__' :
    main()
