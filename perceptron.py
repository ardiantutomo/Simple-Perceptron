import numpy as np

n_training_data = int(input("Input jumlah training data: ")) #n
n_features = int(input("Input jumlah fitur: ")) #p
training_data = list()
w = list()

for j in range(n_features):
    feature = float(input("Input initial weight(fitur-{}): ".format(j+1)))
    w = w + [feature, ]
w = np.asarray(w)

bias = int(input("Input bias: "))

for i in range(n_training_data):
    target = int(input("Label: ")) # antara 0 dan 1 / 1 dan -1 -> dikodingan ini menggunakan 0 dan 1
    input_data = {
            "p" : list(),
            "t" : target
            }
    for j in range (n_features):
        feature = float(input("Input fitur-{}: ".format(j+1)))
        input_data["p"] = input_data["p"] + [feature, ]
    training_data = training_data + [input_data,]
  
epochs = 0
while(True):
    #step function 0 dan 1
    epochs = epochs + 1
    correct = 0
    print("Epochs - ", epochs)
    print("======================")
    for i in range (n_training_data):
        p = np.asarray(training_data[i]["p"])
        a = 0 if np.matmul(p, w) + bias < 0 else 1
        if a == training_data[i]["t"]:
            correct = correct + 1
        else:
            print("Data ", i+1)
            #update weight
            e = training_data[i]["t"] - a
            w = w + (e*np.transpose(p))
            bias = bias + e
            print("Data: ", i)
            print("Error: ", e)
            print("w-new: ", w)
            print("bias-new: {}\n\n".format(bias))
    if correct == n_training_data:
        break
    
print("Epochs: ", epochs)
print("W :", w)
print("Bias :", bias)
        
        
        
        
        
        
        
        
        
        
        
        
        