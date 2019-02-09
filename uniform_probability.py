## Uniform distribution
#p = [0.2, 0.2, 0.2, 0.2, 0.2]
#print p

## Generalized uniform distribution
#p = []
#n = 10

#for index in range(n):
#    p.append(1.0/n)

#print p

## So now we are able to initialize the initial belief of the robot

# pHit and pMiss (Robot world with 5 grid cells)

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green'] # actual color of the cell
Z = 'red' # measured color of cell
pHit = 0.6
pMiss = 0.2

#p[0] = p[0]*pMiss
#p[1] = p[1]*pHit
#p[2] = p[2]*pHit
#p[3] = p[3]*pMiss
#p[4] = p[4]*pMiss

#print p
#print sum(p)

# Measurement update : A key function of localization
##def sense(p, Z):
##    q = []
##    normalized_q = []
##    for index in range(len(p)):
##        if Z == world[index]:
##            q.append(p[index] * pHit)
##        else:
##            q.append(p[index] * pMiss)
##
##    for index in range(len(q)):
##        q_index = q[index]/sum(q)
##        normalized_q.append(q_index)
##        
##    return normalized_q # normalized product of input probability
##
##print sense(p, Z)

# Processing any sequence of measurements of any length
measurements = ['red', 'green']

def sense(p, measurement):
    q = []
    for index in range(len(p)):
        if measurement == world[index]:
           q.append(p[index] * pHit)
        else:
           q.append(p[index] * pMiss)        

    s = sum(q)
    
    for index in range(len(q)):
        q[index] = q[index]/s
        
    return q

for index in range(len(measurements)):
    p = sense(p, measurements[index])
print p
