import csv
import random

def loadDataset(filename, split, trainingSet = [], testSet = []):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(0, len(dataset) - 1):
            dataset[x] = dataset[x]
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

#with open(r'C:/Users/Christian/Desktop/CS170_Proj2/CS170_SMALLtestdata__102.txt') as csvfile:
 #   lines = csv.reader(csvfile)
  #  for row in lines:
   #     print(', '.join(row))

trainingSet = []
testSet = []
loadDataset(r'C:/Users/Christian/Desktop/CS170_Proj2/CS170_SMALLtestdata__102.txt', 0.66, trainingSet, testSet)
print("Train: " + repr(len(trainingSet)))
print("Test: " + repr(len(testSet)))
