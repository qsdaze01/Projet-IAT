import numpy as np
import csv

class StupidAgent():
    """ 
    A random agent.
    """

    def __init__(self, num_actions):
        self.num_actions = num_actions
        self.epsilon = 1


    def select_action(self, _):
        return 2
    
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
