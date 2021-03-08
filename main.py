
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

    # Loop For each Vector in the population to apply Mutation Crossover and Offspring Selection
    for index in range(0,100):

        #Initiate variables
        a = 0
        b = 0
        c = 0
        offspring = [0]*5
        distribution = [1 - Cr, Cr]
        target_vector = population[index]

        #Loop untill a,b,c and index are unique
        while a == b or a == c or b == c or a == index or b == index or c == index:
            a = random.randint(0,99)
            b = random.randint(0,99)
            c = random.randint(0,99)

        #initialize vectors with indexes at a,b,c
        vec_a = np.array(population[a])
        vec_b = np.array(population[b])
        vec_c = np.array(population[c])

        #print(target_vector)
        #print(vec_a)
        #print(vec_b)
        #print(vec_c)

        #First step of mutation (Difference of two parent vectors)
        vector_scale = np.subtract(vec_c,vec_b)
        #print(vector_scale)

        #scale difference using Scaling Factor defined
        vector_scale = vector_scale * F

        #add the trail vector (Vector_scale) with 3rd parent vector
        vector_scale = np.add(vec_a, vector_scale)

        #loop at every index of the vector
        for j in range(0,5):
            cross = random.choices(p,distribution) # Determines probability of crossover occuring
            if(cross[0] == 1): #Crossover complete, offspring uses trail vector value at index j
                offspring[j] = vector_scale[j]
            else: #No crossover, uses target vectors value at index j
                offspring[j] = target_vector[j]


        #print(target_vector)
        #print(vector_scale)
        #print(offspring)

        #x = fitness(target_vector)
        #y = fitness(offspring)
        #print("Target Vector: " + str(x))
        #print("Offpsring Vector: " + str(y))

        if (fitness(offspring) <= fitness(target_vector)): #Checks the fitness of the target vector against the offspring
            #print("Offspring is better")
            population[index] = offspring #population updated with newer and fitter offspring
        else:
            #print("Target Vector is better")
            population[index] = target_vector #Population not updated as offspring was more unfit

    #print(population)
    return population

def fitness(individual):

    # Random function of x1^2 + x2^2 +x3^2 +x4^2 +x5^2 for testing
    score = (individual[0]**2) + (individual[1]**2) + (individual[2]**2) + (individual[3]**2) + (individual[4]**2)
    #print(score)
    return score


def initial(): #generate initial population

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

