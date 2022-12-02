import math
import numpy as np

def sigmoid(x):
    z = 1 / (1 + math.exp(-x))
    return z


def perceptron():
    x_input = [1, 1, 0, 1]
    x0 = 1
    o_desired = 1
    w5 = [0.3, -0.2, 0.2, 0.1]  
    w6 = [0.1, 0.4, -0.3, 0.4]  
    theta = [0.2, 0.1]          
    w57 = -0.3
    w67 = 0.2
    theta7 = -0.3

    learning_rate = 0.8         
    i = 0
    iteration = 1
    print("Perceptron Training: \n")
    while i < 3:
        print("Iteration no: " + str(iteration) + "   ", end="")
        I5 = np.dot(x_input, w5) + x0*theta[0]
        I6 = np.dot(x_input, w6) + x0*theta[1]
        o5 = sigmoid(I5)
        o6 = sigmoid(I6)
        I7 = o5 * w57 + o6 * w67 + x0 * theta7
        o7 = sigmoid(I7)

        error7 = o7 * (1 - o7) * (o_desired - o7)
        error6 = o6 * (1 - o6) * error7 * w67
        error5 = o5 * (1 - o5) * error7 * w57

        print("Error: " + str(error7))

        theta7 += (learning_rate * error7)
        theta[0] += (learning_rate * error5)
        theta[1] += (learning_rate * error6)

        k = 0
        for w in w5:
            w += (learning_rate * error5 * x_input[k])
            k += 1

        k = 0
        for w in w6:
            w += (learning_rate * error6 * x_input[k])
            k += 1

        w57 += (learning_rate * error7 * o5)
        w67 += (learning_rate * error7 * o6)

        iteration += 1
        i = i + 1

    print()


perceptron()
