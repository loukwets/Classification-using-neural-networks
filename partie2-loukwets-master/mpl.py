#Matricule : 000442311
__author__ = "WETS Loukas"
__date__ = "12 novembre 2017"
import mlp_functions

if __name__ == "__main__":
    dataset = mlp_functions.readData('train_small.csv')
    mlp_functions.crossValidation(dataset)
