from time import sleep
from game.SpaceInvaders import SpaceInvaders
from controller.keyboard import KeyboardController
from controller.random_agent import RandomAgent
from controller.IA_agent import IA_agent
import sys
import csv
import plot 




def main():

    # if len(sys.argv) < 4:
    #     print("Pas le bon nombre d'argument : Nom_fichier alpha epsilon gamma")
    #     exit()
    # else:
    #     alpha = sys.argv[1]
    #     epsilon = sys.argv[2]
    #     gamma = sys.argv[3]

    filename = 'LearningPlot.csv'
    header = ['score','episode']
    f = open('LearningPlot.csv','w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

    score = 0
    episode = 0

    game = SpaceInvaders(display=True)
    #controller = KeyboardController()
    controller = RandomAgent(game.na)
    #controller = IA_agent(game, alpha, epsilon, gamma)
    game.get_state()
    state = game.reset()
    while True:
        action = controller.select_action(state)
        previous_state = state
        state, reward, is_done = game.step(action)
        score += reward
        episode += 1
        plot.add_score(score,episode)
        #controller.updateQ(previous_state, action, reward, state)
        sleep(0.0001)

if __name__ == '__main__' :
    main()
