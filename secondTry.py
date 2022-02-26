from math import sqrt
import numpy as np

def partition(bucket, indexList, p1, p2):
  left = []
  right = []

  for i in indexList:
    p3 = bucket[i]
    d = p1[0]*p2[1]+p3[0]*p1[1]+p2[0]*p3[1]-p3[0]*p2[1]-p2[0]*p1[1]-p1[0]*p3[1]
    if (d > 0):
      left.append(i)
    elif (d < 0):
      right.append(i)

  return (left, right)

def distance(p1, p2, p3):
  return (abs((p2[0]-p1[0])*(p1[1]-p3[1])-(p1[0]-p3[0])*(p2[1]-p1[1])))/(sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2))

def partConvexHull(hull, bucket, indexList, p1, p2):
  if (len(indexList) == 0):
    pass
  elif (len(indexList) == 1):
    hull.append(indexList[0])
  else:
    # find coordinate with greatest distance
    maxIdx = -1
    maxD = 0
    for i in indexList:
      p3 = bucket[i]
      d = distance(p1, p2, p3)
      if (d >= maxD):
        maxIdx = i
        maxD = d
    
    indexList.remove(maxIdx)
    left, right = partition(bucket, indexList, p1, bucket[maxIdx])
    left1, right1 = partition(bucket, right, bucket[maxIdx], p2)

    # call recursion
    partConvexHull(hull, bucket, left1, bucket[maxIdx], p2)
    hull.append(maxIdx)
    partConvexHull(hull, bucket, left, p1, bucket[maxIdx])
      
def convexHull(bucket):
  hull = []
  indexList = [i for i in range(len(bucket))]

  # tambahkan nilai p1 dan p2 (titik-titik ekstrem) ke dalam hull
  maxIdx = np.argmax(bucket, axis=0)[0]
  minIdx = np.argmin(bucket, axis=0)[0]

  indexList.pop(maxIdx)
  indexList.pop(minIdx)

  left, right = partition(bucket, indexList, bucket[minIdx], bucket[maxIdx])

  
  # call left recursion
  hull.append(maxIdx)
  partConvexHull(hull, bucket, left, bucket[minIdx], bucket[maxIdx])
  hull.append(minIdx)
  # call right recursion
  partConvexHull(hull, bucket, right, bucket[maxIdx], bucket[minIdx])
  hull.append(maxIdx)
  
  return hull