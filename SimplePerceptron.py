ischange = False
table = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
alpha = 0.2
w1 = 0.3
w2 = -0.2
b = 0.4
def getyest(x1, x2):
        res = x1*w1+x2*w2+b
        if res < 0:
            return 0
        else:
            return 1
def deltaweight(e, x):
        return alpha*e*x

def runiteration():


    for row in table:
        x1 = row[0]
        x2 = row[1]
        ydes = row[2]
        yest = getyest(x1, x2)
        error = ydes-yest
        global w1
        global w2
        global ischange
    if error!= 0:
        dwx1 = deltaweight(error, x1)
        dwx2 = deltaweight(error, x2)
        w1 = w1 + dwx1
        w2 = w2 + dwx2
        ischange = True

requiredIteration = 0
while (True):
    requiredIteration += 1
    ischange = False
    runiteration()
    if ischange == False:
        break
print("Final weight = %f and %f " % (w1, w2))
print("Iteration required = %d " % (requiredIteration))
