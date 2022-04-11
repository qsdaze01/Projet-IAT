import numpy as np
import time

class IA_agent():

    def __init__ (self, game, alpha, epsilon, gamma):
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.game = game

        self.nb_invaders = game.get_invaders_X()
        self.Q = []
        self.states = []

    def add_state(self, actual_state):
        self.states.append(actual_state)
        self.Q.append(actual_state)
        index = np.where(self.Q == actual_state)
        time.sleep(1)
        print("aaaaaaaaaa")
        print(index)
        for i in range(4):
            self.Q[index].append(0)

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

        return action 
    
    def updateQ(self, state, action, reward, next_state):
        try :
            max_next_state = np.max(self.Q[next_state])
        except IndexError:
            max_next_state = 0

        self.Q[state][action] = (1. - self.alpha)*self.Q[state][action] + self.alpha*(reward + self.gamma*max_next_state)