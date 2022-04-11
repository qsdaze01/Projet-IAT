## LISTE DES CHOSES A DEFINIR
---


Etat du jeu : 

```
get_playerX(); 
get_playerY() (constante); 
get_invadersX(); 
get_invadersY(); 
get_bullet_state()
```

## I. Méthode de $Q-learning$

On va actualiser dans la méthode de Q learning notre valeur de Q(s,a). Au fur et a mesure que l'on avance notre Q va converger vers une politique optimale. 

$$Q^{\pi^*} \text{tel que la politique optimale est } \pi^* = \underset{a\in\mathcal{A}}{arg}\text{ max } Q(s,a).$$

On part d'un état initial $s_0$ généré par le jeu à son lancement. Puis de manière itérative, on choisit une action à chaque étape. Cette action $a$ génère une observation $r$ et un nouvel état $s'$. 

On parcourt pour ce nouvel état $s'$ les actions et on garde l'action qui maximise $$\underset{a'\in \mathcal{A}}{max} \text{ }Q(s, a').$$

Puis par descente de gradient on va actualiser notre $Q(s,a)$. L'expérience acquise au cours de l'itération est : 

$$r + \gamma \times \underset{a'\in \mathcal{A}}{max} \text{ }Q(s, a').$$


L'observation $r$ définie dans le cadre du sujet est en fait une valeur binaire qui vaut 1 si l'invaders a été tué et 0 sinon. On va définir $\delta$ comme la différence entre la valeur apprise et celle de l'état d'avant : 

$$\delta = r + \gamma \times \underset{a'\in \mathcal{A}}{max} \text{ }Q(s, a') - Q(s,a).$$

On actualise alors $Q(s,a)$ tel que : $$Q(s,a) \leftarrow Q(s,a) + \alpha \delta,$$ où $\alpha$ est le pas d'apprentissage dans la descente de gradient. 

En fait on peut voir $\delta$ comme une dérivée partielle discrete d'ordre 1. On souhaite le faire tendre vers 0. 


```python
Pseudo-code
------------

TABLEAU Q : #initialiser avec des 0 pour les Q_value
[[get_player_X, distance_X, distance_Y, get_bullet_state, action_0, Q_value],
 [get_player_X, distance_X, distance_Y, get_bullet_state, action_1, Q_value],
 [get_player_X, distance_X, distance_Y, get_bullet_state, action_2, Q_value],
 [get_player_X, distance_X, distance_Y, get_bullet_state, action_3, Q_value]] 

eps_init = 1 #valeur de début de epsilon
eps_end = 0.1 #valeur de fin de epsilon
nb_episodes = 10000 #nombre d'épisodes
r = 0.1
gamma = 0.4

alpha = 0.6 #learning rate


while S non terminal : 

    state = get_state()

    p = random(0,1)
    if p<eps :
        action = random(0,1,2,3)
    else :
        max = 0 #valeur max de Q pour toutes les actions 
        action = 0
        for etat in Q :
            if etat[0:4] == state and etat[5]>max : 
            #les cases de Q qui matchent l'état dans lequel on est et dont la  valeur de Q est maximale

                max = etat[5]
                action = etat[4]

    recompense = reward #récupérer le reward généré par l'action
    new_state = get_state() #récupérer nouvel état après action

    delta = 0   

    q_max = 0 #valeur max de Q pour toutes les actions dans le nouvel état
        for etat in Q :
            if etat[0:4] == new_state and etat[5]>q_max : 
            #les cases de Q qui matchent l'état dans lequel on est et dont la  valeur de Q est maximale
                q_max = etat[5]

    delta = r + gamma*q_max - max
    for etat in Q :
        if etat[0:5] == state + [action] : #changer la valeur de Q pour l'état et l'action choisie
            etat[5] = delta*alpha + etat[5]
    


```

Le choix de l'action se fait selon une méthode $\epsilon- greedy$. On choisit avec une probabilité $\epsilon$ une action au hasard parmi celles possibles. Et on choisit avec une probabilité $1-\epsilon$ de suivre le modèle à savoir prendre l'action qui maximise $Q(s,a)$. On va alors regarder dans notre tableaux des $Q$ pour l'état $s$ l'action qui donne la plus grande valeur de Q. 

Il faudra visualiser la courbe d'apprentissage (i.e le score cumulé en fonction du temps). L'idée est qu'au fur et à mesure que l'on joue au jeu, on va rencontrer des paires $(état, action)$. Pour chaque paire on calcule une valeur de $Q(s,a)$ et l'on vient actualiser cette valeur si on a déjà rencontré cette paire au préalable. 

Il faut alors définir clairement ce qu'est un état. Pour implémenter $Q-learning$, il faut un nombre d'états discret. Or a priori, il y a un très grand nombre de paires possibles (l'espace des valeurs prises en $X$ et $Y$ pour le vaisseau et l'invaders est continu). 

Il faut donc discrétiser notre espace de jeu pour faire en sorte de se cantonner à un nombre de paires $(état, action)$ finies. On peut éventuellement discrétiser en taille de bullet. 

Pour la mise à jour de $\epsilon$, elle peut se faire de façon linéaire du un nombre fixe d'épisodes puis être constante sur la fin. Le mieux est de la faire décroître de façon quadratique. Typiquement on la fait varier e 1.0 à 0.1.

En ce qui concerne la courbe d'apprentissage, il faut tracer le score en fonction du temps et / ou du nombre d'épisodes. Mais cette courbe est trop bruitée, elle n'est pas exploitable d'un point de vue statistique. 

Ce qui est plus intéressant est de faire une moyenne mobile 


1) Faire une expérience et lisser la courbe 
2) Faire plusieurs expériences et stocker les résultats dans des csv différents. 
3) Moyenner les résultats de chaque courbe et tracer la région définie par le max, le min et la moyenne.

Cette courbe finale obtenue témoigne de l'éfficacite de l'**algorithme** et non de la politique sous-jacente liée à une éxpérience. Plus notre région est narrow et notre valeur élevée, le meilleur notre algorithme est. On obtient ce genre de courbe : 

![plot]("Projet Gaspard/game/data/plot.png")