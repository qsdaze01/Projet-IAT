import string
import numpy as np
import time
import random
import csv
import math

limite_epsilon = 0.01

class IA_agent():

    def __init__ (self, game, alpha, epsilon, gamma):
        random.seed(time.time())
        self.alpha = float(alpha)
        self.epsilon = float(epsilon)
        self.gamma = float(gamma)
        self.epsilon_max = self.epsilon

        self.game = game

        self.Q = []
        self.states = []

    def add_state(self, actual_state):
        string_actual_state = ""
        for i in range(len(actual_state)):
            string_actual_state += str(actual_state[i])
        self.states.append(string_actual_state)

        self.Q.append(np.zeros(4))

    def select_action(self):
        type_action = random.randrange(1)

        state_in_tab = False

        actual_state = self.game.get_state()
        string_actual_state = ""
        for i in range(len(actual_state)):
            string_actual_state += str(actual_state[i])
            
        # Cas random
        if type_action < self.epsilon:
            for i in range(len(self.states)):
                if self.states[i] == string_actual_state:
                    state_in_tab = True
            if state_in_tab == False:  
                self.add_state(actual_state)
            action = random.randrange(0, 4, 1)

        # Cas où on suit la politique
        else:
            max = 0
            action = -1

            for i in range(len(self.states)):
                if self.states[i] == string_actual_state :
                    state_in_tab = True
                    for j in range(4): 
                        if max < self.Q[i][j]:
                            max = self.Q[i][j]
                            action = j
            
            if state_in_tab == False:
                self.add_state(actual_state)
                action = random.randrange(0, 4, 1)
        
        return action

    
    def updateQ(self, state, action, reward, next_state):
        try :
            string_next_state = ""
            for i in range(len(next_state)):
                string_next_state += str(next_state[i])
            
            index_next = self.states.index(string_next_state)
            max_next_state = np.max(self.Q[index_next])
        except (IndexError, ValueError):
            max_next_state = 0

        string_state = ""
        for i in range(len(state)):
            string_state += str(state[i])

        try:
            index = self.states.index(string_state)
            self.Q[index][action] = (1. - self.alpha)*self.Q[index][action] + self.alpha*(reward + self.gamma*max_next_state)
        except ValueError:
            pass


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
        if self.epsilon > limite_epsilon:
            self.epsilon = (math.atan(-(20*count_episode/nb_iteration - 10)) + math.pi/2)/math.pi
            if self.epsilon > self.epsilon_max:
                self.epsilon = self.epsilon_max
    
    
    
