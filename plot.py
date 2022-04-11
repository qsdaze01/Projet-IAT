import csv
import matplotlib.pyplot as plt 

filename = 'LearningPlot.csv'
header = ['score','episode']
f = open('LearningPlot.csv','w')
writer = csv.writer(f)
writer.writerow(header)
f.close()

def add_score(score,episode):
    #ajoute au fichier csv le double (score, episode)
    f = open('LearningPlot.csv','a')
    writer = csv.writer(f)
    #writer.writerow(header)
    writer.writerow([score,episode])
    f.close()


