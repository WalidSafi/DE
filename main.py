
D = 5
Np = 100
Cr = 0.9 #(Crossover Date)
F = 0.8 #Scaling Factor
p = [0,1]
best_param = [0]*5
best_fitness = 10000000.0

import numpy as np
import random

def differentialEvolution(population):

    # Loop For each Vector in the population to apply Mutation Crossover and Offspring Selection
    for index in range(0,Np):

        #Initiate variables
        a = 0
        b = 0
        c = 0
        offspring = [0]*D
        distribution = [1 - Cr, Cr]
        target_vector = population[index]

        #Loop untill a,b,c and index are unique
        while a == b or a == c or b == c or a == index or b == index or c == index:
            a = random.randint(0,Np-1)
            b = random.randint(0,Np-1)
            c = random.randint(0,Np-1)

        #initialize vectors with indexes at a,b,c
        vec_a = np.array(population[a])
        vec_b = np.array(population[b])
        vec_c = np.array(population[c])

        vector_scale = np.subtract(vec_c, vec_b)
        vector_scale = vector_scale * F
        vector_scale = np.add(vec_a, vector_scale)

        #loop at every index of the vector
        for j in range(0,D):
            cross = random.choices(p,distribution) # Determines probability of crossover occuring
            if(cross[0] == 1): #Crossover complete, offspring uses trail vector value at index j
                offspring[j] = vector_scale[j]
            else: #No crossover, uses target vectors value at index j
                offspring[j] = target_vector[j]

        if (fitness(offspring) <= fitness(target_vector)): #Checks the fitness of the target vector against the offspring
            population[index] = offspring #population updated with newer and fitter offspring
        else:
            population[index] = target_vector #Population not updated as offspring was more unfit

    #print(population)
    return population

def fitness(individual):

    global best_fitness
    global best_param
    # Random function of x1^2 + x2^2 +x3^2 +x4^2 +x5^2 for testing
    discus = (10**6)*(individual[0]**2) + (individual[1]**2) + (individual[2]**2) + (individual[3]**2) + (individual[4]**2)
    cigar = (individual[0] ** 2) + (10 ** 6)*(individual[1] ** 2) + (10 ** 6)*(individual[2] ** 2) + (10 ** 6)*(individual[3] ** 2) + (10 ** 6)*(individual[4] ** 2)
    hcef = individual[0]**2 + ((10**6)**(0.25))*individual[1]**2 + ((10**6)**(0.5))*individual[2]**2 + ((10**6)**(0.75))*individual[3]**2 + ((10**6)**(1))*individual[4]**2
    rosen = (100*(individual[0]**2+individual[1]**2)**2 + (individual[0] - 1)**2) + (100*(individual[1]**2+individual[2]**2)**2 + (individual[1] - 1)**2) + (100 * (individual[2] ** 2 + individual[3] ** 2) ** 2 + (individual[2] - 1) ** 2) + (100 * (individual[3] ** 2 + individual[4] ** 2) ** 2 + (individual[3] - 1) ** 2)

    if(rosen <= best_fitness):
        best_fitness = rosen
        best_param = individual

    return rosen


def initial(): #generate initial population

    genpop = [0]*Np
    variables = [0]*D

    for x in range(0, Np):
        for i in range(0, D):
            variables[i] = round(random.uniform(-10, 10),4)
        genpop[x] = variables
        variables = [0] * D;

    population = np.asarray(genpop)
    return population

if __name__ == '__main__':

    initialpop = initial()
    print(initialpop)
    newgen = differentialEvolution(initialpop)

    for x in range(0,25):
        print("GENERATION: " + str(x + 1))
        newgen = differentialEvolution(newgen)
        #print(newgen)

    print("Fitness Values are: ")
    print(best_param)
    print(best_fitness)

