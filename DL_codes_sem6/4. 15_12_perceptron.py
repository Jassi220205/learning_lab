# 2-input perceptron
def perceptron(X, T, name):
    w1 = w2 = b = 0  

    for _ in range(10):   
        for i in range(len(X)):
            x1, x2 = X[i]
            t = T[i]

            y_in = b + w1*x1 + w2*x2

            
            if y_in > 0:
                y = 1
            elif y_in < 0:
                y = -1
            else:
                y = 0

            if y != t:
                w1 += t * x1
                w2 += t * x2
                b  += t

    print(name, ":", w1, w2, b)



def perceptron_not(X, T):
    w = b = 0
    bias = 1

    for _ in range(2):  
        for i in range(len(X)):
            x = X[i]
            t = T[i]

            y_in = b + w * x

            if y_in > 0:
                y = 1
            elif y_in < 0:
                y = -1
            else:
                y = 0

            if y != t:
                w += t * x
                b += t * bias

    print("NOT :", w, b)



X = [(1,1), (1,-1), (-1,1), (-1,-1)]
X_not = [1, -1]


perceptron(X, [ 1,-1,-1,-1], "AND")
perceptron(X, [ 1, 1, 1,-1], "OR")
perceptron(X, [-1, 1, 1, 1], "NAND")
perceptron(X, [-1,-1,-1, 1], "NOR")
perceptron(X, [-1, 1, 1,-1], "XOR")  

perceptron_not(X_not, [-1,1])