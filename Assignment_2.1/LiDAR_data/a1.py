import open3d as o3d
import copy
import numpy as np
from scipy.linalg import logm
from scipy.spatial.transform import Rotation as R
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import time

def readData(file):
	"""
	reads the ground truth file
	returns a 2D array with each
	row as GT pose(arranged row major form)
	array size should be 1101*12
	"""
	data = []
	for i in range(77):
		line = file.readline()
		line = line.split()
		arr = np.array(line)
		arr = arr.reshape(3, 4)
		data.append(arr)
	return data

def readPointCloud(filename):
	"""
	reads bin file and returns
	as m*4 np array
	all points are in meters
	you can filter out points beyond(in x y plane)
	50m for ease of computation
	and above or below 10m
	"""
	pcl = np.fromfile(filename, dtype=np.float32,count=-1)
	pcl = pcl.reshape([-1,4])
	return pcl

def convertToWorldFrame(i, points):
    pointsInWorldFrame = []
    for p in points:
        #()transforms[i - 10].astype('float32')
        #()p.astype('float32')
        #()print(type(transforms[i - 10]))
        #()print(transforms[i - 10].shape)
        #()print(transforms[i - 10])
        #()print(type(p))
        #()print(p.shape)
        #()print(p)
        #pointsInWorldFrame.append(np.matmul(float(transforms[i - 10]), float(p)))
        pointsInWorldFrame.append(np.matmul(transforms[i - 10].astype('float32'), p.astype('float32')))
    pointsInWorldFrame = np.array(pointsInWorldFrame)
    print(pointsInWorldFrame.shape)
    return pointsInWorldFrame

#()


if __name__ == "__main__":
    finalPointCloud = []
    txtfile = open("01.txt", "r")
    transforms = readData(txtfile)
    txtfile.close()
    for i in range(10,13):
        loc = "./01/0000" + str(i) + ".bin"
        output = readPointCloud(loc)
        finalPointCloud.append(convertToWorldFrame(i, output))
        #()print(type(output))
        #()print(output.shape)
        #()print(output)
        #()for t in transforms:
        #()		print(t)
    print(type(finalPointCloud))
    # So finalPointCloud is a list with elements as the numpy arrays with points in world frame
    # But these numpy arrays have different shapes so we can not convert the entire thing into a numpy array.
    #()	finalPointCloud = np.array(finalPointCloud)
    #()	print(finalPointCloud.shape)
#print(type(transforms))
#print(transforms)
