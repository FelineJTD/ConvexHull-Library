import numpy as np

def partConvexHull(hull, bucket, indexList, p1, p2, left):
  if (len(indexList) == 0):
    return (hull)
  elif (len(indexList) == 1):
    return (hull.append(indexList[0]))
  else:
    leftDistance = 0
    rightDistance = 0
    l = -1
    r = -1
    ilL = []
    ilR = []
    for i in indexList:
      p = bucket[i]
      d = (p[0]-p1[0])*(p2[1]-p1[1])-(p[1]-p1[1])*(p2[0]-p1[0])
      if (left): #left
        if (d < 0):
          ilL.append(i)
          if (d < leftDistance):
            leftDistance = d
            l = i

      else: #right
        if (d > 0):
          ilR.append(i)
          if (d > rightDistance):
            rightDistance = d
            r = i

    if (left and l != -1):
      hull.append(l)
    elif (not left and r != -1):
      hull.append(r)

    print("lookie",ilL, ilR)
    hull.append(partConvexHull(hull, bucket, ilL, bucket[l], p1, -1))
    hull.append(partConvexHull(hull, bucket, ilR, bucket[r], p2, 1))
    return hull


def ConvexHull(bucket):
  # Inisiasi hull
  hull = []
  indexList = [i for i in range(len(bucket))]

  # tambahkan nilai p1 dan p2 (titik-titik ekstrem) ke dalam hull
  maxIdx = np.argmax(bucket, axis=0)[0]
  minIdx = np.argmin(bucket, axis=0)[0]

  indexList.pop(maxIdx)
  indexList.pop(minIdx)

  print(indexList)

  hull.append(partConvexHull(hull, bucket, indexList, bucket[minIdx], bucket[maxIdx], True))
  hull.append(partConvexHull(hull, bucket, indexList, bucket[minIdx], bucket[maxIdx], False))
  hull.append(maxIdx)
  hull.append(minIdx)
  print(hull)
  for i in hull:
    print(bucket[i])

  return hull

bucket = [[0,0],[3,2],[5,1]]
hull = ConvexHull(bucket)