import open3d as o3d
import copy
import numpy as np
from scipy.linalg import logm
from scipy.spatial.transform import Rotation as R
from scipy.optimize import fsolve
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
from tabulate import tabulate
#()min x -76.69056120083911 max X 159.71739639855903 min y -74.67544320017304 max y 74.02465032337722

#()
#()
#()

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

finalPointCloud=[]
pointsInWorldFrame=[]
txtfile=open("01.txt","r")
transforms = readData(txtfile)
txtfile.close()

loc = "./01/0000" + str(10) + ".bin"
ar = readPointCloud(loc)
arr = np.array(ar[:,:3])
color = np.array(arr[:,:-1])
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(arr)
tr = np.append(transforms[10],[[0,0,0,1]],axis=0)
o3d.geometry.PointCloud.transform(pcd,tr)
pcdf = pcd
for i in range(10,87):
    loc = "./01/0000" + str(i) + ".bin"
    ar = readPointCloud(loc)
    arr = np.array(ar[:,:3])
    color = np.array(arr[:,:-1])
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(arr)
    R = pcd.get_rotation_matrix_from_zyx((0,-np.pi/2,np.pi/2))
    pcd.rotate(R, (0,0,0))
    tr = np.append(transforms[i-11],[[0,0,0,1]],axis=0)
    o3d.geometry.PointCloud.transform(pcd,tr)
    pcdf += pcd
o3d.io.write_point_cloud("./pcd.ply",pcdf)
points = np.asarray(pcdf.points)
print(points.shape)
occMap = np.zeros((250, 250))
for p in points:
	occMap[int(p[0])][int(p[1])] += 1

#()pt = []

for i in range(250):
	for j in range(250):
		if occMap[i][j] > 0:
			occMap[i][j] = 1
		else:
			occMap[i][j] = 0
			#()pt.append(np.array([i , j]))
cmap = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',['black','white'],256)
bounds=[-1,0.5, 2]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# tell imshow about color map so that only set colors are used
img = plt.imshow(occMap,interpolation='nearest',
                    cmap = cmap,norm=norm,origin='lower')

# make a color bar
plt.colorbar(img,cmap=cmap,
                norm=norm,boundaries=bounds,ticks=[0,1])
#()plt.set_title('Occupancy Map')
plt.show()
#()pt = np.array(pt)
#()print(pt.shape)
#()pcd = o3d.geometry.PointCloud()
#()pcd.points = o3d.utility.Vector3dVector(pt)
#()o3d.io.write_point_cloud("map.ply", pcd)
#()o3d.visualization.draw_geometries([pcd])
#()print(tabulate(occMap))
#()maxX = 0#()
#()maxY = 0
#()minX = 1000
#()minY = 1000
#()for p in points:
    #()print(p)
#()    if maxX < p[0]:
#()        maxX = p[0]
#()    if maxY < p[1]:
#()        maxY = p[1]
#()    if minX > p[0]:
#()        minX = p[0]
#()    if minY > p[1]:
#()        minY = p[1]
    #()print(p[0])
    #()exit(0)
#()print(f"min x {minX} max X {maxX} min y {minY} max y {maxY}")
#()print(points[0])
#()print(points[10])
#()print(points[100])
#()print(points[1000])
