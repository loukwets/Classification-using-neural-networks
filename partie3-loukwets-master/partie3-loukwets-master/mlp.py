import time
import mlp_functions as if106
import numpy as np

np.random.seed(15151515)
if106.printLogo()
start = time.time()
data = if106.getMNISTData()
if106.crossValidation(data,it_CV=4)
end = time.time()
print("Total Time: " + str(end - start))







