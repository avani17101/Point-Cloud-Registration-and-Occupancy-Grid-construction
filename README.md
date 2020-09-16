# Assignment 2


TEAM-ID: 16 <br>
TEAM-NAME: spacex  <br>
YOUR-ID: 2019121004 , 2018102002  <br>
YOUR-NAME: Avani Gupta, Sreeharsha Paruchuri  <br> 

## Libraries used
* Open3d
* numpy

## Work done by each team-member
Both of us discussed and figured a strategy/solution on questions.  <br>
Avani: Coded point cloud registration <br>
Sreeharsha: Coded occupancy map construction <br>

## Task 1 - Point Cloud Registration

### Methodology:
* **Loop through each bin file and read points** <br>
  * **Convertion of points from lidar to camera frame** <br>
Convert the points read from step above to camera frame by rotation matrix obtained by figuring out euler angles. 
  * **Transform points according to poses given** <br>
After converting to camera frame, transform the points according to poses read from 01.txt.
  * **Register point cloud** <br>
Convert the above obtained points to point clouds using opencv function.
  * **Append to global point cloud** <br>
Append point cloud thus obtained to global point cloud(final point cloud containing point clouds obtained from all 77 bins).
* **Save and display global point cloud** 


![README/pc2.png](REPORT/t1.png)


## Task 2 -  Occupancy Map Construction

### Methodology:


![README/figure38.png](REPORT/t2.png)


