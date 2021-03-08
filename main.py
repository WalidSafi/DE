
# D = 4
# Np = 100 (population)
Cr = 0.9 #(Crossover Date)
F = 0.8 #Scaling Factor
# MAX_NFC (Termination Condition)
# Vector Range = [-10,10]
p = [0,1]

import numpy as np
import random
import matplotlib.pyplot as plt

def differentialEvolution(population):

    for index in range(0,100):

        a = 0
        b = 0
        c = 0
        offspring = [0]*5
        distribution = [1 - Cr, Cr]
        target_vector = population[index]

        while a == b or a == c or b == c or a == index or b == index or c == index:
            a = random.randint(0,99)
            b = random.randint(0,99)
            c = random.randint(0,99)

        vec_a = np.array(population[a])
        vec_b = np.array(population[b])
        vec_c = np.array(population[c])

        #print(target_vector)
        #print(vec_a)
        #print(vec_b)
        #print(vec_c)

        vector_scale = np.subtract(vec_c,vec_b)
        #print(vector_scale)

        vector_scale = vector_scale * 0.8

        vector_scale = np.add(vec_a, vector_scale)

        for j in range(0,5):
            cross = random.choices(p,distribution)
            if(cross[0] == 1):
                offspring[j] = vector_scale[j]
            else:
                offspring[j] = target_vector[j]


        #print(target_vector)
        #print(vector_scale)
        #print(offspring)

        #x = fitness(target_vector)
        #y = fitness(offspring)
        #print("Target Vector: " + str(x))
        #print("Offpsring Vector: " + str(y))

        if (fitness(offspring) <= fitness(target_vector)):
            #print("Offspring is better")
            population[index] = offspring
        else:
            #print("Target Vector is better")
            population[index] = target_vector

    #print(population)
    return population

def fitness(individual):

    #x**2 + y**2 +
    score = (individual[0]**2) + (individual[1]**2) + (individual[2]**2) + (individual[3]**2) + (individual[4]**2)
    #print(score)
    return score

# Press the green button in the gutter to run the script.
def initial():

    genpop = [0]*100
    variables = [0]*5

    for x in range(0, 100):
        for i in range(0, 5):
            variables[i] = round(random.uniform(-10, 10),4)
        genpop[x] = variables
        variables = [0] * 5;

    population = np.asarray(genpop)
    return population

if __name__ == '__main__':

    initialpop = initial()
    print(initialpop)
    newgen = differentialEvolution(initialpop)

    for x in range(0,100):
        print("GENERATION: " + str(x + 1))
        newgen = differentialEvolution(newgen)
        print(newgen)

    test = [0]*2
    test = newgen[0]
    print("Fitness Values are: ")
    print(test)
    print(fitness(test))

