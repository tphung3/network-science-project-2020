#Thanh Son Phung (your name here)
#10/26/2020 (date of creation/modification)
#skeleton for importing dataset
#@require panda
#highly suggest installing anaconda if you don't have panda
#@require dataset in same directory
import pandas as pd

#read in the dataset
rating_matrix = pd.read_csv('ratings_small.csv')
#print format of array
print("The first five rows of the dataset is as follows:")
print(rating_matrix[:5])
#print number of ratings in dataset
print("The dataset has "+ ((str) (len(rating_matrix) - 1)) + " rows/ratings.")

#fill your code here
