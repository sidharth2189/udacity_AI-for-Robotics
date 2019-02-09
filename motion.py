## Exact Motion

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


def move(p, U):
    q = []
    for index in range(len(p)):
        q.append(p[(index-U)%len(p)]) 
    return q

print (move(p, 1))

## In-Exact Motion
p=[0, 1, 0, 0, 0]
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

# modify move procedure above to accommodate extra probabilities
def move_new(p, U):
    q = []
    for index in range(len(p)):
        q.append(pExact * p[(index-U)%len(p)] + pOvershoot * p[(index-U-1)%len(p)] + pUndershoot * p[(index-U+1)%len(p)]) 
    return q

for run in range(100):
    p = move_new(p,1)
print (p)

# Sense and move
p = [0.2, 0.2, 0.2, 0.2, 0.2]
motions = [1, 1]

for index in range(len(measurements)):
    p = sense(p, measurements[index]) # sense
    p = move_new(p, motions[index]) # inexact motion
    
print (p)

## Ans: [0.21157894736842103, 0.1515789473684211, 0.08105263157894739, 0.16842105263157897, 0.3873684210526316]
## Without looking at anything but the world and measurements, it probably started with grid cell which is second red. So, it started in 2nd red cell by sensing red, moved to right by 1, saw green correctly, moved to rigt by 1
## Now it finds itself, most likely in the last cell with highest probabilty
