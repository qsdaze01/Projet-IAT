import numpy as np
import csv
import math

limite_epsilon = 0.01

class StupidAgent():
    """ 
    A random agent.
    """

    def __init__ (self, game, alpha, epsilon, gamma):
        self.alpha = float(alpha)
        self.epsilon = float(epsilon)
        self.gamma = float(gamma)
        self.epsilon_max = self.epsilon

        self.game = game

        self.Q = []
        self.states = []

    def updateQ(self, state, action, reward, next_state):
        pass

    def select_action(self):
        actual_state = self.game.get_state()

        # Gestion du bug
        if actual_state == 1 :
            return -1
            
        return 2
    
    def printQ(self):
        print(self.Q)

    def printStates(self):
        print(self.states)
    
    def print_epsilon(self):
        print("Epsilon : " + str(self.epsilon))

    def write_states_CSV(self, file, filename):
        file = open(filename, 'w')
        writer = csv.writer(file)
        writer.writerows(self.states)
        file.close()

    def write_reward_CSV(self, file, filename, tab):
        file = open(filename, 'w')
        writer = csv.writer(file)
        print(len(tab))
        for i in range(len(tab)):
            writer.writerow([tab[i]])
        file.close()

    def write_Q_CSV(self, file, filename):
        file = open(filename, 'w')
        writer = csv.writer(file)
        writer.writerows(self.Q)
        file.close()

    def read_Q_CSV(self, file, filename):
        file = open(filename, 'r')
        reader = csv.reader(file)
        i = 0
        for line in reader:
            self.Q.append(line)
            i += 1

    def MAJ_epsilon(self, nb_iteration, count_episode):
        # On fait varier epsilon selon une fonction de la forme de arctan(x)
        pass
