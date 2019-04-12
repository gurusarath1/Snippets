import numpy as np
import scipy.stats as stats
import statistics
import matplotlib.pyplot as plt
import random


aryX = np.array([1,2,3,4,5,6,7,8,9,0,2,2,2,2,11,12,13,14,15,16,99,100,101])
aryX2 = [1,2,3,4,5,6,7,8,9,0,2,2,2,2,11,12,13,14,15,16,99,100,101]

print(aryX, '\n' ,aryX2)
print('===================================================')
print('Mean ', np.mean(aryX))
print('Median ', np.median(aryX))
print('Mode ', stats.mode(aryX)[0][0])
print('variance ', statistics.variance(aryX))
print('standard deviation ', statistics.stdev(aryX))
print('===================================================')
print('Mean ', statistics.mean(aryX2))
print('Median ', statistics.median(aryX2))
print('Mode ', stats.mode(aryX2)[0][0])
print('variance ', statistics.variance(aryX2))
print('standard deviation ', statistics.stdev(aryX2))
print('===================================================')



# Proving central limit theorem 
random_vals = [random.random() * 100 for x in range(1000)]
random_vals_gauss = [random.gauss(50,5) for x in range(10000)]

sample_means = []
NumberOfSamples = 100000
NumberOfelementsInASample = 40
for i in range(NumberOfSamples):

	sample = random.sample(random_vals, NumberOfelementsInASample)
	sample_mean = np.mean(sample)
	sample_means.append(sample_mean)

#bins = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

MeanOfSampleMeans = np.mean(sample_means)
SDOfSampleMeans = statistics.stdev(sample_means)
MeanOfPopulation =  np.mean(random_vals)

print('Mean Of Sample Means', MeanOfSampleMeans)
print('Standard deviation Of Sample Means', SDOfSampleMeans)
print('Mean Of Population', MeanOfPopulation)


random_vals_gauss = [random.gauss(MeanOfSampleMeans , SDOfSampleMeans) for x in range(NumberOfSamples)]
bins = np.linspace(0,101,500)
bins = np.arange(0,100,0.1)
plt.hist(sample_means,bins.tolist())
#plt.hist(random_vals_gauss,bins.tolist(), color='r')
plt.show()