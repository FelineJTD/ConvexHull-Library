# imports
import numpy as np
import pandas as pd

from sklearn import datasets
from myConvexHull import convexHull
import argparse

# arguments
parser = argparse.ArgumentParser(description='Program untuk membuat convex hull.')
parser.add_argument('dataset', choices=['iris', 'wine', 'breast_cancer'])
parser.add_argument('-o', dest='output',
                    default='output.png',
                    help='output file name (default: output.png)')
args = parser.parse_args()

# load data based on argument
if args.dataset == 'iris':
  data = datasets.load_iris()
elif args.dataset == 'wine':
  data = datasets.load_wine()
elif args.dataset == 'breast_cancer':
  data = datasets.load_breast_cancer()
print('checkpoint1')

# create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

# configure which columns to use
x = 0
y = 1
print('checkpoint2')

import matplotlib.pyplot as plt
# plot data and convex hull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title(f'{data.feature_names[x].title()} vs {data.feature_names[y].title()}')
plt.xlabel(data.feature_names[x])
plt.ylabel(data.feature_names[y])
for i in range(len(data.target_names)):
  bucket = df[df['Target'] == i]
  bucket = bucket.iloc[:,[x,y]].values
  hull = convexHull(bucket) #hasil implementasi convexHull
  #ConvexHull Divide & Conquer
  plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
  for j in range (len(hull)-1):
    plt.plot(bucket[[hull[j], hull[j+1]], 0], bucket[[hull[j], hull[j+1]], 1], colors[i])
plt.legend()
plt.savefig(args.output) # save plot