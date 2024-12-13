#Matricule : 000442311
__author__ = "WETS Loukas"
__date__ = "12 novembre 2017"
import numpy

def forwardPass(x,W1,W2):
    """Fonction qui effectue une forward pass d’un perceptron sur image x avec
        les matrices de poids W1 et W2.
    """
    z = []
    grad = []
    for i in range(len(W1)):
        s_i = numpy.sum(W1[i]*x)
        z_i = sigmoid(s_i) if s_i != 0 else 0.
        z.append(z_i)
        grad.append(z_i * (1 - z_i))
    somme = 0
    for i in range(len(W2)):
        somme += W2[i][0]*z[i]
    z_out = sigmoid(somme)
    grad_out = z_out * (1 - z_out)
    return (z,z_out,grad,grad_out)

def backpropagation(x,y,y_hat,z,W1,W2,grad,grad_out):
    """Fonction qui effectue la backpropagation d’un perceptron multicouche.
        Renvoie deux matrices DeltaW1 et DeltaW2 ayant respectivement les mêmes
        tailles que W1 et W2, contenant les valeurs pour la mise à jour des poids.
    """
    DeltaW1 = numpy.array([[0.]*len(W1[0])]*len(W1))
    DeltaW2 = numpy.array([[0.]]*len(W2))
    e_out = y_hat - y
    delta_out = e_out * grad_out
    for i in range(len(W2)):
        delta_i = delta_out * W2[i][0] * grad[i]
        for j in range(len(W1[i])):
            DeltaW1[i][j] = delta_i * x[j]
        DeltaW2[i]=delta_out * z[i]
    return (DeltaW1,DeltaW2)

def dropout(W1,p):
    """Fonction qui implémente la procédure de dropout avec une probabilité de
        sélection p des neurones a desactiver.
        Renvoie deux listes de booleens qui represente si oui ou non un neurone
        de la couche d'entrée ou intermediaire est activé
    """
    D_input = [(0 if numpy.random.random() < p else 1) for iter in range(len(W1[0]))]
    D_middle = [([0] if numpy.random.random() < p else [1]) for iter in range(len(W1))]
    if numpy.sum(D_input) == 0 or numpy.sum(D_middle) == 0:
        D_input, D_middle = dropout(W1,p)
    return (D_input,D_middle)

def train(data,digit,p=0.5,epsilon=0.0001,H=10,learning_rate=0.001,max_it=20):
    """
    Fonction qui effectue l’entraînement d’un perceptron sur le training set data
    pour reconnaître le chiffre digit. La fonction renvoie les meilleures matrices
    des poids W1,W2 trouvées.
    Le nombre H de neurones de la couche intermédiaire est donné comme paramètre,
    ainsi que le learning_rate utilisé pour la mise à jour des poids Le paramètre
    epsilon est utilisé pour vérifier la convergence de la méthode d’apprentissage
    et max_it est la borne sur le nombre d’itérations lors de l’apprentissage.
    """
    W1 = initWeights(H, len(data[0][1:]))
    W2 = initWeights(H, 1)
    bestW1 = W1[:]
    bestW2 = W2[:]
    best_score = 0
    done_backpropagation = True
    numpy.random.shuffle(data)
    it = 0
    convergence = True
    while it < max_it and done_backpropagation and convergence :
        done_backpropagation = False
        for ligne in data:
            D_input, D_middle = dropout(W1,p)
            W1_dropout, W2_dropout = desactivationConnections(W1, W2, D_input, D_middle)

            z, z_out, grad, grad_out = forwardPass(ligne[1:],W1_dropout,W2_dropout)
            y_hat = 1 if z_out >= 0.5 else -1
            y = 1 if ligne[0]==digit else -1

            if y_hat != y :
                DeltaW1, DeltaW2 = backpropagation(ligne[1:],y,y_hat,z,W1_dropout,W2_dropout,grad,grad_out)
                W1 = W1 - (learning_rate * DeltaW1)
                W2 = W2 - (learning_rate * DeltaW2)
                done_backpropagation = True
                convergence = convergenceCondition(DeltaW1,DeltaW2,epsilon=0.0001)
        score = evaluate(data, digit, W1, W2)
        if score > best_score:
            bestW1 = W1[:]
            bestW2 = W2[:]
            best_score = score
        it +=1
    return (bestW1, bestW2)

def predict(x, L) :
    """Fonction qui effectue la prédiction du chiffre représenté sur l'image x
       avec la liste L des vecteurs poids des dix perceptrons.
       Renvoie le chiffre diggit predit.
    """
    scores_zout =  []
    for numVec in range(len(L)):
        scores_zout.append(forwardPass(x,L[numVec][0],L[numVec][1])[1])
    digit = numpy.argmax(scores_zout)
    return digit

def initWeights(nb_rows,nb_columns):
    """Fonction qui initialise une matrice de poids W de taille nb_rows x nb_columns
        avec des valeurs tirées au hasard selon une distribution normale avec
        moyenne nulle et petit écart type.
    """
    W =  numpy.random.normal(0, 0.0001, (nb_rows, nb_columns))
    return W

def displayConfusionMatrix(C):
    """Fonction qui effectue l’affichage de la matrice de confusion C."""
    decoupe = [ 0.2, 0.4, 0.6, 0.8, 1]
    diago = [227, 191, 115, 119, 83]
    pas_diago = [227, 221, 215, 209, 203]
    print('','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', sep = ' '*5)
    for i in range(len(C)):
        print(i, end = '  ')
        somme = numpy.sum(C[i])
        for j in range(len(C[i])):
            num = round(C[i][j]/somme, 2)
            inter = 0
            for i in range(len(decoupe)):
                if decoupe[i]<= num:
                    inter = i
            diag= diago if i==j else pas_diago
            endL = '\n' if j == 9 else '  '
            num = str(num)
            if len(num) == 3:
                num += '0'
            print_color(num,"38;5;" + str(diag[inter]), endL)

def convergenceCondition(DeltaW1,DeltaW2,epsilon=0.0001):
    """Fonction qui implémente la condition d’arrêt sur base des matrices
        DeltaW1 et DeltaW2.
    """
    res = True
    if numpy.sum(abs(DeltaW1)) < epsilon and numpy.sum(abs(DeltaW2)) < epsilon :
        res = False
    return res

def crossValidation(data,alpha=0.5,it_CV=4,p=0.5,epsilon=0.0001,H=10,learning_rate=0.001,max_it=20):
    """Effectue la validation croisée sur le dataset data. Imprime les resultats."""
    size_training_set = int(len(data)*alpha)
    score = 0
    for i in range(it_CV):
        matConfusion = numpy.zeros((10, 10), int)
        numpy.random.shuffle(data)  #choix aléatoire d un partie du dataset
        training_set = data[:size_training_set]
        test_set = data[size_training_set:]

        perceptrons = []
        for numPerc in range(10):           #entraînement de chaque perceptron
            perceptrons.append(train(training_set,numPerc,p=0.5,epsilon=0.0001,H=10,learning_rate=0.001,max_it=20))

        for vect in test_set:   #évalue les prédictions effectuées
            digit = vect[0]
            digit_predit = predict(vect[1:], perceptrons)
            matConfusion[digit][digit_predit] += 1
            if digit_predit == digit :
                score +=1
        displayConfusionMatrix(matConfusion)
    score_moyen = score/(len(test_set)*it_CV)
    print('alpha = '+str(alpha)+', it_CV = '+str(it_CV)+', max_it = '+str(max_it))
    print('Taux de réussite moyen : '+ str(round(score_moyen*100, 2)) + '%')
    return None

def print_color(string,color,sep) :
    """Fonction auxiliaire pour l’affichage de la sequence de caractères string
        coloré selon le code couleur ANSI color, également passé comme chaine de
        caractères et terminé avec la sequence de caractères sep.
    """
    print("\x1B[ "+ color+"m"+ string+"\x1B[0m", end = sep)


def desactivationConnections(W1, W2, D_input, D_middle):
    """Met a 0 les connections entrantres et sortantes des neurones désactivés
        celon les vecteurs D_input et D_middle sur les vecteurs W1 et W2.
    """
    W1_dropout = W1*D_middle
    for i in range(len(W1)):
        W1_dropout[i] *= D_input
    W2_dropout = W2 * D_middle
    return W1_dropout, W2_dropout

def sigmoid(x):
    """ Renvoie le resultat de la fonction sigmoid de x"""
    return (1/(1+numpy.exp(-x)))

def evaluate(data, digit, W1, W2):
    """Evalue la precision des vecteurs W1 et W2 pour reconnaitre le chiffre digit
        renvoie le nombre de fois que les vecteurs ont bien predit si oui ou non
        le chiffre est present sur l'immage.
    """
    res = 0
    for elem in data:
        y = 1 if elem[0]==digit else -1
        z_out= forwardPass(elem[1:],W1,W2)[1]
        y_hat = 1 if z_out >= 0.5 else -1
        if y_hat == y:
            res += 1
    return res

def readData(filename):
    f = open(filename)
    L = []
    for line in f:
        elem = [ int(s) for s in line.strip().split(',') ]
        L += [ elem ]
    return L
