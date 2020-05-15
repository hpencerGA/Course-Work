import random
#generate range of individuals in sample
#1-14 20%
#15-64 60%
#65-99  20%

one_to_14 = range(1,15)

fifteen_to_64 = range(15,65)

sixty_five_and_over = range(65,100)

population = []

for num in range (1,101):
    val = random.random () #generate between 0.0 and 1.0
    if val >= 0.8: #consider everything roughly 20%  
        population.append(random.choice(sixty_five_and_over))
    elif val >= 0.2: #consider everything roughly 60% of the time fiften to sixty five age group
        population.append(random.choice(fifteen_to_64))
    else:
        population.append(random.choice(one_to_14)) #1-14 age group


print(population)

count = 0
for age in population:
    if age is >= 80:
        count += 1

print(count)

#to find total number likely to die gie 15% mortality over 80
#find the number over 80
#find 15% of that number

#multiple by sample size by 10





'''
population = range(1,190000)
age_range = 65
population_distribution = 0


if age_range = range(1,14):
    population_distribution = .2
elif age_range = range(15,64):
    population_distribution = .6
else age_range => 65:
    population_distribution = .2

print (population * population_distribution)
'''