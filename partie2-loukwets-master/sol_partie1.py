import random

# x : list containg set of data
# w : list of weights
# returns result of a forward pass
def forwardPass(x,w):
    s = sum(x[i]*w[i] for i in range(len(x)))
    return 1 if s >= 0 else -1 

# data : list the training data
# digit : integer in [0,9]
# max_wait : maximum waiting time
# max_it : maximum number of iterations
# returns a list of weights
def train(data,digit,max_wait = 3,max_it = 40):
    w = [0]*(len(data[0])-1)  # initialize weights
    bestw = w[:]
    best_score = 0
    epochs_since_last_improvement = 0
    random.shuffle(data) 
    i = 0
    while i < max_it and epochs_since_last_improvement < max_wait: 
        # training round
        for elem in data:
            # parsing elem
            x = elem[1:]
            y = binaryClass(elem[0], digit) 
            if forwardPass(w, x)!=y: 
                # wrong answer, updating weights                
                for j in range(len(w)):
                    w[j] += y*x[j]
        # evaluation of  the new weights
        score = evaluate(data, w, digit)
        if score > best_score:
            bestw = w[:]
            best_score = score
            epochs_since_last_improvement = 0
        else:     
            epochs_since_last_improvement += 1
    return bestw
   
# x : list containg set of data
# L : list of weigths for digits
# returns the digit predicted for x
def predict(x,L):
    best_prediction = None
    value_prediction = None
    for d in range(10): 
        # computing prediction value for digit d
        res = sum(L[d][i]*x[i] for i in range(len(L[d])))
        if value_prediction==None or res > value_prediction:
            value_prediction = res
            best_prediction = d
    return best_prediction

# x : list containg set of data
# alpha : proportion of inputs to take (at random) from data to create the training set 
# it_CV : number of iterations
# max_wait : maximum waiting time for training
# max_it : maximum number of iterations for training
# returns None ; outputs the average score of the cross validation
def crossValidation(data,alpha = 0.5,it_CV = 4,max_wait = 3,max_it = 40):
    print("starting cross validation ({} rounds)".format(it_CV))
    size_training_set = int(len(data)*alpha)
    total = 0
    for r in range(it_CV):        
        print('round', r+1)
        # random split between training set and test set
        random.shuffle(data)
        data_train = data[:size_training_set]
        data_test = data[size_training_set:]
        # computation of weigths with the training set
        L = trainPerceptrons(data_train,max_wait,max_it)
        score = 0
        # computation of the score with the test set
        for elem in data_test:
            x = elem[1:]
            y = elem[0]
            if predict(x,L) == y: 
                score += 1
        total += score
        print('score:', score/len(data_test))
    print('Average score over', it_CV, 'rounds:', total/(len(data_test)*it_CV))

# filename : name of data file in current directory
# returns a list containing the data
def readData(filename):
    f = open(filename)
    L = []
    for line in f:
        elem = [ int(s) for s in line.strip().split(',') ]
        L += [ elem ]
    return L

# a : digit of data
# digit : value to check for a
# returns the expected validation for a
def binaryClass(a, digit):
    return 1 if a==digit else -1

# data : list of data
# w : list of weiths
# digit : value of the perceptron used
def evaluate(data, w, digit):
    # returns number of correct predictions when using weights w on dataset data
    res = 0
    for elem in data:
        x = elem[1:]
        y = binaryClass(elem[0], digit)
        if forwardPass(w, x)==y: 
            res += 1
    return res
 
# data_train : list of training data
# max_wait : maximum waiting time for training
# max_it : maximum number of iterations for training
# returns a list of weigths for all perceptrons
def trainPerceptrons(data_train,max_wait = 3,max_it = 40):
    L = [] 
    for d in range(10):       
        print("Training perceptron {}".format(d))
        L.append(train(data_train, d, max_wait, max_it))   
    return L

if __name__ == "__main__":
    crossValidation(readData("train_small.csv"))

