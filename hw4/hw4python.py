import numpy as np
import h5py
import matplotlib.pyplot as plt
import math
import json

#1a
DATA_FNAME = 'mnist_network_params.hdf5'
data = h5py.File(DATA_FNAME, 'r+')

w1 = data['W1']
w2 = data['W2']
w3 = data['W3']

b1 = data['b1']
b2 = data['b2']
b3 = data['b3']

#1b
DATA2_FNAME = 'mnist_testdata.hdf5'
test_data = h5py.File(DATA2_FNAME, 'r+')

x_test_data = test_data['xdata'][:] #60_000x784
y_test_data = test_data['ydata'][:] #60_000X10

#1c

def relu(x: np.array):
    zeroes = np.zeros_like(x)    
    
    return np.maximum(zeroes, x)

def softmax(x: np.array):
    sum = np.sum(np.exp(x))
    
    return x / sum

#1d

def mlp(x_data):
    
    layer1 = []
    
    for x in x_data:
        layer1.append(relu(np.matmul(w1, np.transpose(x)) + b1))
    
    layer1 = np.array(layer1)
    
    print("layer1 shape")
    print(layer1.shape)
    
    layer2 = []
    
    for x in layer1:
        layer2.append(relu(np.matmul(w2, np.transpose(x)) + b2))
        
    layer2 = np.array(layer2)
    
    layer3 = []
    
    for x in layer2:
        layer3.append(softmax(np.matmul(w3, np.transpose(x)) + b3))
    
    layer3 = np.array(layer3)
    
    return layer3

result =  mlp(x_test_data)





#1e

predicted = np.argmax(result, axis=1)

true_y = np.argmax(y_test_data, axis=1)

print(predicted.shape)
print(true_y.shape)

count = 0

# for part f
correct = {}
incorrect_guess = {}
incorrect_actual = {}

for i in range(10000):
    if predicted[i] == true_y[i]:
        count +=1
        correct[i] = predicted[i]
    
    else:
        incorrect_actual[i] = true_y[i]
        incorrect_guess[i] = predicted[i]

print(count)

print(correct)
print(incorrect_guess)

# sample correct
plt.imshow(x_test_data[0].reshape(28,28)) 
plt.show()
print(correct[0])

plt.imshow(x_test_data[1].reshape(28,28)) 
plt.show()
print(correct[1])

# sample incorrect
plt.imshow(x_test_data[8].reshape(28,28)) 
plt.show()
print("Guess: ", incorrect_guess[8], "Actual: ", incorrect_actual[8])

plt.imshow(x_test_data[115].reshape(28,28)) 
plt.show()
print("Guess: ", incorrect_guess[115], "Actual: ", incorrect_actual[115])

plt.imshow(x_test_data[247].reshape(28,28)) 
plt.show()
print("Guess: ", incorrect_guess[247], "Actual: ", incorrect_actual[247])

#in these cases, the correct class was not obvious, especially for 247

# save data to json here
result_list = result.tolist() #activations

indices = list(range(10000))
activations = result_list
classification = predicted.tolist()

data = []
for i, activation, classif in zip(indices, activations, classification):
    data.append({
        "index": i,
        "activations": activation,
        "classification": classif
    })
    
with open("result.json", "w") as f:
    f.write(json.dumps(data))


