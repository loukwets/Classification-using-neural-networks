__author__ = "WETS Loukas"
__date__ = "12 novembre 2017"

from random import shuffle, randint 

def forwardPass(x, w):
    """Prédiction effectuée sur l image x avec le vecteur poids w.
       Renvoie 1 si w croit qu il a trouve le numero de x, -1 si non.
    """
    somme = 0
    for i in range(784):                #prediction
        somme += x[i]*w[i]
    if somme >= 0 :
        s = 1
    else:
        s = -1
    return s

def train(data, digit, max_wait = 3, max_it = 40) :
    """Phase d'entraînement du perceptron pour le numero digit sur
       le traning set data avec max_it iteration maximum ou si le
       meilleur score n’a pas été amélioré lors des max_wait dernières
       étapes d’entraînements. Renvoi le poids correspondant au meilleur score.
    """
    iteration = 0                       #pour conter les iterations
    wait = 0                            #pour conter meilleur score pas ameliore
    maxScore = 0                        #score maximum
    
    while iteration < max_it and wait < max_wait:  
        score = 0                       #score actuel
        wInter = [0 for i in range(784)]    #creation vecteur null
        shuffle(data)                       #mélanger le training set
        for vec in data:
            if digit == vec[0]:     #numero a entrainer egale au numero vecteur?
                y = 1
            else :
                y = -1
            if y != forwardPass(vec[1:], wInter):  #y != prediction ?
                for j in range(784):                #mise à jour des poids
                    wInter[j] += y*vec[j+1]
            
        for vecteur in data:                    #évaluation de la situation actuel
            if digit == vecteur[0]:
                y2 = 1
            else :
                y2 = -1
            if y2 == forwardPass(vecteur[1:], wInter):
                score += 1

        if score > maxScore:                    #garde le meilleur score le vecteur
            maxScore = score
            w = wInter                      #poids correspondant au meilleur score
            wait = 0
        else :
            wait +=1
        iteration += 1
    return w

def predict(x, L) :
    """Fonction qui effectue la prédiction du chiffre représenté sur l'image x
       avec la liste L des vecteurs poids des dix perceptrons.
       Renvoie le chiffre diggit predit.
    """
    for numVec in range(len(L)):
        somme = 0
        for i in range(784):
            somme += x[i] * L[numVec][i]        #produit scalaire entre x et L
        if numVec==0 or somme >= maxSom:    #choix du perceptron le plus confiant
            maxSom, digit = somme, numVec
    return digit

def crossValidation(data, alpha = 0.5, it_CV = 4, max_wait = 3, max_it = 40) :
    """Effectue la validation croisée sur le dataset data. Imprime les resultats."""
    dataset = readData(data)
    score = 0
    for i in range(it_CV):
        frac = int(len(dataset)*alpha)  #calcule de la fraction alpha du dataset
        training_set = dataset[frac:]
        test_set = dataset[:frac]
        if randint(0,1) == 0:           #choix aléatoire d un partie du dataset
            training_set, test_set = test_set, training_set

        perceptrons = []
        for numPerc in range(10):           #entraînement de chaque perceptron
            perceptrons.append(train(training_set, numPerc, max_wait, max_it))

        for vect in test_set:   #évalue les prédictions effectuées
            digit = vect[0]
            if predict(vect[1:], perceptrons) == digit :
                score +=1

    score_moyen = score/(len(test_set)*it_CV)
    print('alpha = '+str(alpha)+', it_CV = '+str(it_CV)+', max_wait = '+\
          str(max_wait)+', max_it = '+str(max_it))
    print('Taux de réussite moyen : '+ str(round(score_moyen*100, 2)) + '%')
    return None

def readData(filename):
    f = open(filename)
    L = []
    for line in f:
        elem = [ int(s) for s in line.strip().split(',') ]
        L += [ elem ]
    return L

crossValidation('train.csv')
