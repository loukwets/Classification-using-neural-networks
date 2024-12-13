# WETS Loukas mat.ULB: 000442311
"""
THIS FILE CONTAINS THE CLASS Mlp.
"""
import numpy
from Gui import *
import sys

class Mlp(object):
    def __init__(self, ui):
        self._ui = ui
        self._ui.start.clicked.connect(self.handleButton)

    def handleButton(self):
        """Cette methode s'occupe de lancer crossvalidation avec les
            parametres selectionné au moment ou le boutton start a ete
            clique.
        """
        self._ui.start.setEnabled(False)
        #Paramètres.
        self.num = int(self._ui.ChoixDuChiffre.currentText())
        self.filename = self._ui.choixDuDataset.currentText()
        self.alpha = self._ui.alpha.value()
        self.it_CV = self._ui.Crossvalidation.value()
        self.p = self._ui.PropDropout.value()
        self.epsilon = self._ui.Epsilon.value()
        self.H = self._ui.H.value()
        self.learning_rate = self._ui.LearningRate.value()
        self.max_it = self._ui.Training.value()

        if self.H != 10:
            self._ui.tabWidget.setTabEnabled(1, False)

        self.crossValidation()

        self._ui.start.setEnabled(True)
        self._ui.tabWidget.setTabEnabled(1, True)

    def forwardPass(self,x,W1,W2):
        """Fonction qui effectue une forward pass d’un perceptron sur image x avec
            les matrices de poids W1 et W2.
        """
        z = self.logistic_function(numpy.dot(W1,x))
        z_out = self.logistic_function(numpy.dot(z,W2))
        return (z,z_out,self.logistic_function(z, True), self.logistic_function(z_out, True))

    def evaluate(self, data, W1, W2):
        """Evalue la precision des vecteurs W1 et W2 pour reconnaitre le chiffre digit
            renvoie le nombre de fois que les vecteurs ont bien predit si oui ou non
            le chiffre est present sur l'immage.
            """
        res = 0
        for elem in data:
            y = 1 if elem[0]==self.num else -1
            z_out= self.forwardPass(elem[1:],W1,W2)[1]
            y_hat = 1 if z_out >= 0.5 else -1
            if y_hat == y:
                res += 1
        return res

    def backpropagation(self,x,y,y_hat,z,W1,W2,grad,grad_out):
        """Fonction qui effectue la backpropagation d’un perceptron multicouche.
            Renvoie deux matrices DeltaW1 et DeltaW2 ayant respectivement les mêmes
            tailles que W1 et W2, contenant les valeurs pour la mise à jour des poids.
        """
        e_out = y - y_hat
        delta_out = e_out*grad_out
        delta = delta_out*W2*grad
        DeltaW1 = numpy.outer(delta,x)
        DeltaW2 = delta_out*z
        return DeltaW1, DeltaW2

    def dropout(self, W1):
        """Fonction qui implémente la procédure de dropout avec une probabilité de
            sélection p des neurones a desactiver.
            Renvoie deux listes de booleens qui represente si oui ou non un neurone
            de la couche d'entrée ou intermediaire est activé
        """
        n_hidden,n_input = W1.shape
        D_input, D_middle = (numpy.random.binomial(1,1-self.p,n_input),numpy.random.binomial(1,1-self.p,n_hidden))
        if numpy.sum(D_input) == 0 or numpy.sum(D_middle) == 0:
            D_input, D_middle = self.dropout(W1)
        return D_input, D_middle

    def train(self, data):
        """
        Fonction qui effectue l’entraînement d’un perceptron sur le training set data
        pour reconnaître le chiffre digit. La fonction renvoie les meilleures matrices
        des poids W1,W2 trouvées.
        Le nombre H de neurones de la couche intermédiaire est donné comme paramètre,
        ainsi que le learning_rate utilisé pour la mise à jour des poids Le paramètre
        epsilon est utilisé pour vérifier la convergence de la méthode d’apprentissage
        et max_it est la borne sur le nombre d’itérations lors de l’apprentissage.
        """
        print("Training MLP")
        W1 = self.initWeights(self.H, len(data[0][1:]))
        W2 = self.initWeights(self.H, 1)[:,0]
        bestW1 = W1[:]
        bestW2 = W2[:]

        self._ui.poids.updatePixels(bestW1)

        score = self.evaluate(data, W1, W2)
        best_score = -1

        numpy.random.shuffle(data)

        it = 0
        convergence = False
        done_backpropagation = True
        while it < self.max_it and done_backpropagation and not(convergence) :
            done_backpropagation = False
            for ligne in data:

                D_input, D_middle = self.dropout(W1)
                self._ui.paint.handle(D_input, D_middle)

                x = ligne[1:]
                x = D_input * x
                W2_drop = D_middle * W2

                z, z_out, grad, grad_out = self.forwardPass(x,W1,W2_drop)
                y_hat = 1 if z_out >= 0.5 else -1
                y = 1 if ligne[0]==self.num else -1

                if y_hat != y :
                    DeltaW1, DeltaW2 = self.backpropagation(x,y,y_hat,z,W1,W2_drop,grad,grad_out)
                    W1 += self.learning_rate * DeltaW1
                    W2 += self.learning_rate * DeltaW2
                    done_backpropagation = True
                    convergence = self.convergenceCondition(DeltaW1,DeltaW2)

            score = self.evaluate(data, W1, W2)
            print("Iteration %d - Score: %.3f" % (it+1, (score / len(data))*100))
            if score > best_score:
                bestW1 = W1[:]
                bestW2 = W2[:]
                self._ui.poids.updatePixels(bestW1)
                best_score = score
            it +=1
        return (bestW1, bestW2)

    def initWeights(self, nb_rows,nb_columns):
        """Fonction qui initialise une matrice de poids W de taille nb_rows x nb_columns
            avec des valeurs tirées au hasard selon une distribution normale avec
            moyenne nulle et petit écart type.
        """
        W =  numpy.random.normal(0, 0.0001, (nb_rows, nb_columns))
        return W

    def convergenceCondition(self,DeltaW1,DeltaW2):
        """Fonction qui implémente la condition d’arrêt sur base des matrices
            DeltaW1 et DeltaW2.
        """
        return (numpy.sum(numpy.absolute(DeltaW1)) < self.epsilon) and (numpy.sum(numpy.absolute(DeltaW2)) < self.epsilon)

    def crossValidation(self):
        """Effectue la validation croisée sur le dataset data. Imprime les resultats."""
        print("MLP for digit " + str(self.num))
        data = self.readData()
        size_training_set = int(len(data)*self.alpha)
        total_sigmoid = 0
        total_ReLu = 0
        for i in range(self.it_CV):
            print('Crossvalidation - Round', i+1)
            numpy.random.shuffle(data)  #choix aléatoire d un partie du dataset
            training_set = data[:size_training_set]
            test_set = data[size_training_set:]

            self.sigmoid = 1
            perceptron_sigmoid = self.train(training_set)
            self.sigmoid = 0
            perceptron_ReLu = self.train(training_set)
            score_sigmoid = self.evaluate(test_set, perceptron_sigmoid[0], perceptron_sigmoid[1])
            score_ReLu = self.evaluate(test_set, perceptron_ReLu[0], perceptron_ReLu[1])
            total_sigmoid += score_sigmoid
            total_ReLu += score_ReLu
            print('[INFO] Score for the current CV round with Sigmoid function: ' + str((score_sigmoid/len(test_set))*100))
            print('[INFO] Score for the current CV round with ReLu function: ' + str((score_ReLu/len(test_set))*100))

        print('alpha = '+str(self.alpha)+', it_CV = '+str(self.it_CV)+', max_it = '+str(self.max_it)+', Choix du dataset :'+self.filename)
        print('Taux de réussite moyen avec Sigmoid function: '+ str((total_sigmoid/(len(test_set)*self.it_CV))*100) + '%')
        print('Taux de réussite moyen avec ReLu function: '+ str((total_ReLu/(len(test_set)*self.it_CV))*100) + '%')
        return None

    def logistic_function(self,x,derivative=False):
        if self.sigmoid:
            try:
                output = 1.0/(1.0+numpy.exp(-x))
            except OverflowError:
                if x < 0:
                    output = 0.0000000000000001
                else:
                    output = 0.9999999999999999

            return(output if not derivative else (x*(1.0-x)))
        else:
            return(numpy.maximum(0,x) if not derivative else numpy.heaviside(x,1))

    def readData(self):
        f = open(self.filename)
        L = []
        for line in f:
            elem = [ int(s) for s in line.strip().split(',') ]
            L += [ elem ]
        return L
