import json
from initialise import initialise
from selection import roulette_wheel_selection
from fitness import fitness
from crossover import crossover
from average_fitness import average_fitness
import math

def generation(data):
    #define constants
    pop_size = 50
    num_gen = 500
    num_parents = 2
    n_mutation = 0 #number of mutations
    p_mutation = 0.001 #probability of mutation
    p_cross = 1 #that is every parent must cross
    n_cross = 0 #number of crosses

    #store the list in a variable
    list_of_activities = data["activities"].copy()
    len_act = len(list_of_activities)
    #the duration of intervals
    lchrom = int((int(data["interval_end"])-int(data["interval_start"]))/int(data["slot_dur"]))
    curr_gen = 0
    #average fitness of the population
    avg_fitness = []
    max_fit = []
    gen_list= []
    # initialise a population
    population = initialise(pop_size, lchrom, len_act)
    while curr_gen!=num_gen:
        data2 = data.copy()
        curr_gen += 1
        #select individuals for mating
        parents = roulette_wheel_selection(population, fitness, num_parents,data2,data2["userID"])
        #perform crossover
        children = crossover(population[parents[0]],population[parents[1]],lchrom,n_mutation,p_mutation,p_cross,n_cross)
        
        #update the population
        
        population.append(children[0])
        population.append(children[1])
        
        # add to the fitness of the population
        stats = average_fitness(population,data2,data2["userID"])
        avg_fitness.append(stats[0])
        max_fit.append(stats[1])
        gen_list.append(curr_gen)
    return {"pop":sorted(population,key=lambda x: fitness(x,data2,data2["userID"]))[::-1],"avg":avg_fitness,"max":max_fit}
