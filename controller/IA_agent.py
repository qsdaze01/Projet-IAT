import string
import numpy as np
import time
import random

class IA_agent():

    def __init__ (self, game, alpha, epsilon, gamma):
        random.seed(time.time())
        self.alpha = float(alpha)
        self.epsilon = float(epsilon)
        self.gamma = float(gamma)

        self.game = game

        self.nb_invaders = game.get_invaders_X()
        self.Q = []
        self.states = []

    def add_state(self, actual_state):
        string_actual_state = ""
        for i in range(len(actual_state)):
            string_actual_state += str(actual_state[i])
        self.states.append(string_actual_state)
        #self.Q.append(actual_state)

        self.Q.append(np.zeros(4))

    def select_action(self, state):
        max = 0
        state_in_tab = False
        actual_state = self.game.get_state()
        action = -1

        for i in range(len(self.Q)):
            if self.states[i] == actual_state :
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

        index = self.states.index(string_state)
        #print(self.states)
        #print(string_state)
        #print(index)

        self.Q[index][action] = (1. - self.alpha)*self.Q[index][action] + self.alpha*(reward + self.gamma*max_next_state)