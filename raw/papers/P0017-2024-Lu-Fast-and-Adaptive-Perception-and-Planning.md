# FAPP: Fast and Adaptive Perception and Planning for UAVs in Dynamic Cluttered Environments

Minghao $\mathrm { L u ^ { 1 } }$ , Xiyu Fan1, Han Chen2, and Peng Lu1∗ 

Abstract—Obstacle avoidance for Unmanned Aerial Vehicles (UAVs) in cluttered environments is significantly challenging. Existing obstacle avoidance for UAVs either focuses on fully static environments or static environments with only a few dynamic objects. In this paper, we take the initiative to consider the obstacle avoidance of UAVs in dynamic cluttered environments in which dynamic objects are the dominant objects. This type of environment poses significant challenges to both perception and planning. Multiple dynamic objects possess various motions, making it extremely difficult to estimate and predict their motions using one motion model. The planning must be highly efficient to avoid cluttered dynamic objects. This paper proposes Fast and Adaptive Perception and Planning (FAPP) for UAVs flying in complex dynamic cluttered environments. A novel and efficient point cloud segmentation strategy is proposed to distinguish static and dynamic objects. To address multiple dynamic objects with different motions, an adaptive estimation method with covariance adaptation is proposed to quickly and accurately predict their motions. Our proposed trajectory optimization algorithm is highly efficient, enabling it to avoid fast objects. Furthermore, an adaptive re-planning method is proposed to address the case when the trajectory optimization cannot find a feasible solution, which is common for dynamic cluttered environments. Extensive validations in both simulation and realworld experiments demonstrate the effectiveness of our proposed system for highly dynamic and cluttered environments. 

Index Terms—Aerial systems, dynamic environment, point cloud, motion planning, obstacle avoidance 

# SUPPLEMENTARY MATERIALS

Video: https://youtu.be/4DXBuKpqQk4 

# I. INTRODUCTION

HE development of robotics has always aimed at increasing the intelligence of robots and integrating them into our lives. Unmanned aerial vehicles (UAVs) have gained popularity due to their motion flexibility and cost-effectiveness. Recent advancements in aerial autonomy technology have enabled UAVs to excel in various intelligent tasks, including navigation, exploration in static environments [1], [2], and autonomous cinematography [3]. 

However, flying UAVs in complex and dynamic cluttered environments without human command remains a challenging 

1Minghao Lu, Xiyu Fan and Peng Lu are with the Adaptive Robotic Controls Lab (ArcLab), Department of Mechanical Engineering, The University of Hong Kong, Hong Kong, SAR, China (e-mail: minghao0@connect.hku.hk; fanxiyu@connect.hku.hk; lupeng@hku.hk) 

2Han Chen is with Huawei Technologies Co., Ltd, Wuhan, Hubei, China (e-mail: stark.chen@connect.polyu.hk). 

This work was supported by General Research Fund under Grant 17204222, and in part by the Seed Fund for Collaborative Research and General Funding Scheme-HKU-TCL Joint Research Center for Artificial Intelligence. 

and potentially hazardous endeavor. For instance, consider a scenario where a UAV is assigned the task of capturing closeup photography on city sidewalks bustling with pedestrians or in narrow indoor spaces filled with crowds. In such situations, the UAV needs to react intelligently to the ever-changing environment while accomplishing its mission. 

State-of-the-art obstacle avoidance for UAVs mainly focuses on static environments [1], [2], [4], [5]. Dynamic environments introduce more significant challenges in both perception and path planning. The motion blur caused by dynamic objects, especially fast-moving objects, making them difficult to detect using traditional visual sensors. The path planning algorithms must be efficient such that they can avoid fast-moving objects. As such, event-based detection methods have been developed to address fast-moving objects [6]. However, event cameras are expensive and not cost-efficient for low-cost UAVs. Therefore, the challenge of UAVs navigating in dynamic environments remains open. Recently, several methods have been proposed to address dynamic obstacles for UAVs [7]–[10]. However, all of these studies consider the case where the environment is static with only a few (one or two) dynamic objects. They either use constant velocity or acceleration model [7]–[11] to estimate and predict the object’s motion, or let the object walk with a constant velocity [12]. They did not investigate whether the estimation is fast or precise and its effects on the success of dynamic obstacle avoidance. 

In this paper, we consider a more complex environment: a dynamic cluttered environment where dynamic objects are the dominant objects in the environment. This type of environment will aggregate the difficulties in perception and planning. For perception, detecting multiple objects and tracking them is much more challenging than detecting one object. For dynamic obstacle avoidance, it is necessary to estimate and predict the velocity of the objects. This also becomes significantly more challenging as different objects possess different motion models. It is difficult to use one model to estimate the motions of different objects. For planning, it is also more challenging as multiple objects increase the probability of collisions. Furthermore, it may be common that the planning may fail to find a feasible solution in dynamic cluttered environments. All of these challenges make the obstacle avoidance in a dynamic cluttered environment significantly challenging. 

This paper proposes FAPP (Fast and Adaptive Perception and Planning) for UAVs in dynamic cluttered environments. We first propose a novel simple but highly efficient point cloud segmentation strategy that can efficiently distinguish static and dynamic objects. A unique data association method is developed to assign detected dynamic clusters to existing 

clusters. To address multiple dynamic objects, a novel adaptive estimation is proposed to quickly estimate and predict their velocities, which facilitates the avoidance of multiple objects. In terms of path planning, we further improve our previous planning [9] without even using the front-end path searching and safe corridor generation. Furthermore, an adaptive replanning strategy is proposed to address the situation where a feasible path cannot be found, which is common in dynamic cluttered environments. Finally, we perform various simulations and real experimental flight tests to validate the performance of our proposed FAPP, both indoors and outdoors. In summary, the main innovations of this paper are as follows: 

1) A novel and efficient point cloud segmentation strategy is proposed, which can efficiently distinguish static and dynamic objects. 

2) A novel covariance adaptation method is proposed to address multiple dynamic objects with different motions. This method can overcome the limitation of the constant velocity or acceleration assumption made by existing studies. It can quickly estimate and predict the positions and velocities of the objects, which facilitates the avoidance of multiple dynamic objects. 

3) An adaptive re-planning method is proposed to address the situation when no feasible path can be found by the trajectory optimization. This is important for a dynamic cluttered environment in which no feasible solution is common. 

4) To the best of our knowledge, this is one of the first few works that consider the obstacle avoidance of UAVs in highly cluttered and dynamic environments. We validate the performance of our FAPP in various simulation and experimental tests. The whole perception and planning process can be completed within a few milliseconds, which is highly efficient. 

# II. RELATED WORKS

Obstacle avoidance and planning in complex dynamic environments continue to present significant challenges. Existing works have identified two main components of the problem: dynamic object perception and mapping, and vehicle motion planning. However, developing a complete system that can effectively handle real-time perception and obstacle avoidance of any dynamic object remains a formidable task. 

# A. Dynamic environment perception

For the optimal response of a UAV’s motion in a random dynamic environment, precise recognition of the environment is crucial. This includes accurate mapping of the scene and effective segmentation and motion estimation of dynamic objects within the environment. Some recent works use the event-based method [6], [8] to detect moving obstacles for obstacle avoidance. However, event cameras are only sensitive to dynamic targets and it is difficult to build a static local map of the environment in real-time. In [9], [13], the image-based algorithm is used for moving object detection and tracking. However, the current limitations exist where only specific objects can be detected, and the detection is not coupled 

with mapping capabilities. Point cloud-based methods can better handle the problem but are still difficult to meet the requirements of real-time obstacle avoidance. In [14]–[16], the researchers proposed methods to remove dynamic points from the global map, but cannot instantly and accurately detect dynamic objects. Dynamic object segmentation by clustering and motion estimation is also extensively studied over years [7], [11], [12], [17]. However, in these works, the description of dynamic objects, static objects, or occluded objects is not comprehensive enough, which limits their practicality to more complex scenarios. Some learning-based methods can achieve moving object segmentation more accurately [18], [19], but they are difficult to run in real-time on mobile terminals without GPUs. 

# B. Dynamic obstacle avoidance

The obstacle avoidance problem for robots, especially for UAVs, has been widely studied and explored in recent years. Some reactive methods, including velocities obstacles(VO) [11], [20], artificial potential field(APF) [6], [8], [21] have been used for UAV dynamic obstacle avoidance. The approaches only take consideration of current moving obstacles and only compute one-step actions, which can not meet the requirements in environments with dense hybrid (static and dynamic) obstacles. Model predictive control (MPC) is also widely utilized for dynamic obstacle avoidance [7], [10], as it can achieve optimality in the local time domain. However, these approaches lack the advantage of UAVs’ navigation in clustered environments due to their limited description of the complex structures within the environments. Several complete solutions based on optimization in the community have demonstrated fast, robust flights in a clustered static environment, and the motion primitives can be solved in real time [2], [4], [22]. Inspired by the above works, [9], [12] adds the penalty of the dynamic obstacles for the polynomial trajectory optimization. However, [12] did not consider the uncertainty of the moving object prediction and the control effort of the trajectory, while the polygon generation in [9] is complex and very time-consuming in a cluster environment. Moreover, none of the above work considers how the UAV should react autonomously when it is unable to plan to the target point. Due to these problems, these techniques are not flexible and may lead to a decrease in performance in a complex dynamic environment. 

Overall, all these studies on dynamic obstacle avoidance only consider the environment where only one or two dynamic objects are present and none of them has considered the dynamic cluttered environments in which dynamic objects are the dominant objects. 

Furthermore, the motion of the dynamic obstacles considered in the existing studies is rather simple. They either let the object move with a constant velocity [12] or use a constant velocity or acceleration model [7], [9], [11] to estimate and predict their motions. This can hardly be true for dynamic cluttered environments in which many objects possess various motions that does not satisfy the constant velocity or acceleration assumption. Another important issue 

missing in these existing studies is that they did not show how fast and accurate the estimation and prediction of the object’s motion is. Actually, the speed and accuracy of the estimation plays an important role in the success of dynamic obstacle avoidance. 

# III. FAST AND ADAPTIVE PERCEPTION OF DYNAMIC CLUTTERED ENVIRONMENTS

In this section, we will present the first part of FAPP: fast and adaptive perception. Our fast and adaptive perception is a point-cloud-based method to obtain the real-time static local map while segmenting and estimating the motion of the dynamic objects in the environment. The pipeline of the system is shown in Fig.1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/ee4a3094091c21be0d3734018f4d4a5619066d04df8a772a7a32b4db35665f9f.jpg)



Fig. 1. The pipeline of proposed fast and adaptive perception algorithm. The inputs of the algorithm are the sequences of lidar scans and robot poses, and the outputs are static local maps and the states of dynamic objects.


# A. Preliminary

Assuming at the kth timestamp $t _ { k }$ , we can get a 3D point cloud ${ } _ { B } P _ { k }$ from the scan of the sensor in the local frame. We first make an $S E ( 3 )$ transformation $^ W _ { B } T _ { k }$ from the local sensor frame $B$ to the global frame $W$ , and get $w P _ { k }$ . $^ W _ { B } T _ { k }$ can be obtained by using the LIO algorithm such as [23]. Then, we create an incremental kd tree (I-KD Tree) [24] to maintain the latest previous $F$ frames point set $\xi$ by adding and deleting points dynamically, where $\xi \subseteq \{ \mathrm { ~ { ~ \bigcup ~ } ~ } \cup \mathrm { ~ { ~ \xi ~ } ~ } _ { W } P _ { j } \}$ . Using the $j \in [ k - F , k - 1 ]$ I-KD Tree, we can keep the point set $\xi$ a proper size and make the points in $\xi$ uniformly distributed in 3D space, which gives a good representation of the spatial distribution information of obstacles over the previous few frames scan. 

# B. Fast Dynamic Object Segmentation

For dynamic obstacle avoidance, it is important to identify dynamic obstacles. While there exists studies that distinguish static objects and dynamic objects using learning-based approaches, they are computationally intensive and difficult to use for small low-cost UAVs. State-of-the-art UAV dynamic obstacle avoidance filters the point cloud and then clusters it into objects using DBSCAN [25]. By designing a Kalman filter for each cluster, they can detect dynamic objects by estimating their speed [7], [11], [12]. This method is effective for sparse environments. However, this is significantly computationally intensive for cluttered environments with many objects. In this paper, we propose a fast dynamic object detection and tracking algorithm. We first propose a novel efficient algorithm that can segment static and dynamic objects without using neural networks. Then, we only design a tracker for dynamic objects. By doing this, we can efficiently detect and track dynamic objects in cluttered environments. 

In this subsection, we propose a novel and efficient algorithm to identify the point cloud as dynamic or static. First, we use DBSCAN to cluster the point cloud of the current frame $w ^ { P _ { k } }$ , resulting in a set of $m$ clusters $\mathcal { C } _ { k } = \{ C ^ { 1 } , C ^ { 2 } , . . . , C ^ { m } \}$ . For each cluster, we can categorize it into one of three cases: 

• Case 1: Continuously moving object. 

• Case 2: Static object. 

• Case 3: Unknown object. 

For case 3, the unknown object encompasses static objects that were previously occluded by moving objects as well as newly appeared objects within the field of view (FOV). Here, we measure the global nearest distance $d ^ { n }$ from each point $p _ { n }$ in a cluster $C ^ { n }$ with $N$ points in total to the previous point set $\xi$ . Then, we propose to formulate the following two functions to describe the classification of a cluster: 

$$
\mathcal {T} _ {1} = \frac {1}{N} \sum_ {n = 1} ^ {N} d ^ {n}, \tag {1}
$$

$$
\mathcal {T} _ {2} = \frac {1}{N} \sum_ {n = 1} ^ {N} \frac {\left(d ^ {n} - \mathcal {T} _ {1}\right) ^ {2}}{\mathcal {T} _ {1} ^ {2}} \tag {2}
$$

where $\mathcal { T } _ { 1 }$ represents the average minimum distance from the points in the cluster to the previous point set, and $\mathcal { T } _ { 2 }$ represents the normalized average variance of $d ^ { n }$ . For a static cluster that has been observed previously, the average distance $T _ { 1 }$ from its points to the previous cloud should be within a small measurement error. For a continuously moving cluster, the average distance $\mathcal { T } _ { 1 }$ should be large, and the nearest point in $\xi$ of each point in the cluster is the projection of itself that once observed. So the distribution of $d ^ { n }$ will be relatively uniform, while an occluded object or a newly observed object will have an uneven distribution. Thus, the cluster can be classified by two constant thresholds $h _ { 1 }$ and $h _ { 2 }$ as follows: 

• Case 1 (Moving objects): $\mathcal { T } _ { 1 } > h _ { 1 }$ & $\mathcal { T } _ { 2 } < h _ { 2 }$ 

• Case 2 (Static objects): $\mathcal { T } _ { 1 } < h _ { 1 }$ 

• Case 3 (Unknown objects): $\mathcal { T } _ { 1 } > h _ { 1 }$ & $\mathcal { T } _ { 2 } > h _ { 2 }$ 

The description of the process is presented in Fig.2. With the algorithm above, we achieve the point cloud clustering and segmentation of the dynamic objects. The set of $D$ dynamic 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/154d63cc9336672b2c4e5970f0ad1f5d11f8a5e2a9a364ee7b57cdc508ed8c88.jpg)



Case 2: Static Objects


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/1ae8bf526d77972b9aeb7e298b65abfd4c2ba6da08486b1e5f73ec589a91fbb1.jpg)


Case 3: Unknown Objects 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/b553d93bdc41554866fd4ee48b15004bc3f2ee9ad15b13c8773d98957c9b0cc8.jpg)



： Current Points Previous Points



Fig. 2. The illustration of our dynamic object segmentation method. For a continuously moving object, its point cloud is at a greater distance from the previous point cloud set, while the distance distribution is relatively uniform.


clusters at time $k$ is ${ } ^ { d } { \mathcal { C } } _ { k }$ , and the geometric centre of the dth cluster can result in $\mathbf { o } _ { k } ^ { d } = [ o _ { x } ^ { d } , o _ { y } ^ { d } , o _ { z } ^ { d } ] _ { k } ^ { \mathrm { T } }$ [ o dx , o d ] T . The overall dynamic points group in the current frame can be written as $w P _ { d y n , k }$ , which satisfies: 

$$
_ {W} P _ {d y n, k} = \bigcup_ {d \in [ 1, D ]} ^ {d} \mathcal {C} _ {k}, \quad_ {W} P _ {d y n, k} \subseteq_ {W} P _ {k}, \tag {3}
$$

Our proposed segmentation algorithm with the proposed two functions in Eqs. (1) and (2) is highly efficient. It can used in highly cluttered environments. The time efficiency and segmentation results will be demonstrated and compared with state-of-the-art methods in Section VI. 

# C. Dynamic Object Tracking

For dynamic obstacle avoidance, it is necessary to track and estimate the motion states of the moving objects after segmentation. The state estimation and prediction will be used in fast and adaptive planning in Section V. 

1) Motion estimation: Here we describe our motion estimation method. The inter-frame displacements of each object in the world frame are approximated as a constant velocity model in this work, and we adopt the Kalman Filter to estimate the states of the moving objects. We define the state vector of an object as: $X ^ { i } = [ x _ { i } , y _ { i } , z _ { i } , \dot { x } _ { i } , \dot { y } _ { i } , \dot { z } _ { i } ] ^ { \mathrm { T } }$ , so the system model of each object can be formulated as: 

$$
X _ {k + 1} ^ {i} = A _ {k} X _ {k} ^ {i} + \nu^ {i}, \tag {4}
$$

$$
Z _ {k} ^ {i} = H _ {k} X _ {k} ^ {i} + \omega^ {i}, \tag {5}
$$

$$
A _ {k} = \left[ \begin{array}{c c} I _ {3 \times 3} & \Delta t \cdot I _ {3 \times 3} \\ 0 _ {3 \times 3} & I _ {3 \times 3} \end{array} \right], H _ {k} = \left[ \begin{array}{c c} I _ {3 \times 3} & 0 _ {3 \times 3} \\ 0 _ {3 \times 3} & I _ {3 \times 3} \end{array} \right], \tag {6}
$$

where $A$ is the state transition matrix, $H$ is the measurement matrix, $\nu \sim \mathcal { N } ( 0 , Q )$ is the normally distributed process noise with a covariance matrix $Q$ and $\omega \sim \mathcal { N } ( 0 , R )$ is the normally distributed measurement noise with a covariance matrix R. ∆t is the time interval between two adjacent frames of scans. If a cluster is newly observed, a new Kalman Filter tracker will be created, while if a cluster can be associated with the ith tracker, we use the geometric center and its frame differencing of the cluster as the measurement $Z ^ { i } = [ o _ { x } ^ { i } , o _ { y } ^ { i } , o _ { z } ^ { i } , \Delta o _ { x } ^ { i } , \bar { \Delta o _ { y } ^ { i } } , \Delta o _ { z } ^ { i } ] ^ { \mathrm { T } }$ . Then, the Kalman Filter can predict and update in real time. The output is the estimated state $\hat { X ^ { i } }$ . 

2) Data association: In assigning detected dynamic objects to existing trackers, we propose a data association method 

for point cloud. First, we create a $D \times I$ assignment matrix $\mathcal { H }$ for the $D$ detected objects and $I$ trackers. The matrix is expressed based on the Mahalanobis distance $\Omega _ { d , i }$ between each detection o and predicted position ˆo from existing trackers: 

$$
\Omega_ {d, i} = \sqrt {\left(\mathbf {o} ^ {d} - \hat {\mathbf {o}} ^ {i}\right) ^ {T} \sigma_ {i} ^ {- 1} \left(\mathbf {o} ^ {d} - \hat {\mathbf {o}} ^ {i}\right)}, \tag {7}
$$

$$
\mathcal {H} _ {d, i} = 1 - \frac {2}{\pi} \arctan \left(\Omega_ {d, i}\right), \tag {8}
$$

where $\textit { d } = \ ( 0 , 1 , . . . , D )$ and $i \ = \ ( 0 , 1 , . . . , I )$ . $\sigma _ { \mathrm { { 6 } \times 6 } }$ is the covariance matrix between the detection and prediction, which can be obtained by the update process of Kalman Filter. $\mathcal { H } _ { d , i } ~ \in ~ ( 0 , 1 )$ indicates the relevance while a larger value denotes a better match. The assignment is solved optimally using the Hungarian algorithm similar to [26]. Additionally, the match of a pair of detection and tracker will also be rejected if the cost value is less than a constant threshold $t h _ { m i n }$ . 

# D. Static Local Map Output

In the above, we obtain all clusters of the dynamic points of the environment. Next, we eliminate the dynamic points $w P _ { d y n , k }$ from the current frame point cloud $w P _ { k }$ and obtain $W _ { s t a , k }$ , which represents the static points in the environment. The process can be represented as: 

$$
_ {W} P _ {s t a, k} = \quad_ {W} P _ {k} - \quad_ {W} P _ {d y n, k}, \tag {9}
$$

The static point cloud $W _ { s t a , k }$ , which includes the complete information of the free space, is used to build an occupancy grid map that will be used for the obstacle avoidance. 

# IV. ADAPTIVE ESTIMATION AND PREDICTION FOR DYNAMIC CLUTTERED ENVIRONMENTS

For dynamic obstacle avoidance, it is important to estimate and predict the motion of the dynamic objects. In dynamic cluttered environments, there exist multiple dynamic objects with different motions. Existing studies on UAV dynamic obstacle avoidance assume that the velocity or acceleration of the object is constant [7], [9], [11] or let the people walk with a constant velocity [12], and then estimate and predict the position and velocity. The constant velocity or acceleration model works when the velocity or acceleration of the dynamic object does not change rapidly. However, multiple dynamic objects have all sorts of motion (one may suddenly change its direction while maintaining the speed) and it is difficult to use one model to estimate and predict their motion. One solution in dynamic object tracking is to use multiple models with each model representing one motion assumption (constant velocity or constant acceleration). However, this will significantly increase the computational burden as we need an estimator for every dynamic object. 

In this paper, we propose to estimate and predict the motion of dynamic objects using a covariance adaptation method without the use of multiple models. We still use the constant velocity model as mentioned in subsection III.C. This model will yield a wrong estimation when the velocity of the objects 

changes rapidly as the process model is not consistent with the real motion model. Consequently, the innovation of the Kalman filter will significantly deviate from zero-mean. Therefore, we propose to use the innovation sequence to update the covariance of the process noise covariance matrix $Q _ { k }$ to obtain a better estimation and prediction. 

For the Kalman Filter of each dynamic object, we can compute its innovation sequence at time step $k$ as follows: 

$$
\gamma_ {k} = Z _ {k} - H _ {k} \hat {X} _ {k | k - 1} \tag {10}
$$

where $\hat { X } _ { k | k - 1 }$ denotes the prediction (a prior estimation) of $X _ { k }$ . By using the innovation sequence, we can compute its actual covariance as follows: 

$$
C _ {\gamma , k} = \frac {1}{W} \sum_ {l = k - W + 1} ^ {k} \gamma_ {l} \gamma_ {l} ^ {\mathrm {T}} \tag {11}
$$

where $W$ is the size of the sliding window. Meanwhile, we can also compute the theoretical innovation covariance using the Kalman Filter. By making use of the covariance matching property, we can obtain the following: 

$$
H _ {k} \hat {Q} _ {k} H _ {k} ^ {\mathrm {T}} = C _ {\gamma , k} - H _ {k} A _ {k - 1} P _ {k - 1 | k - 1} A _ {k - 1} ^ {\mathrm {T}} H _ {k} ^ {\mathrm {T}} - R _ {k} \tag {12}
$$

Then, we could obtain the estimate $\hat { Q } _ { k }$ as follows: 

$$
\hat {Q} _ {k} = C _ {\gamma , k} - A _ {k - 1} P _ {k - 1 \mid k - 1} A _ {k - 1} ^ {\mathrm {T}} - R _ {k} \tag {13}
$$

where $P _ { k - 1 | k - 1 }$ denotes the estimation error covariance matrix at the previous time step $k - 1$ . Finally, to guarantee the positiveness of the covariance matrix [27], we use the following matrix to update $Q _ { k }$ to prevent numerical errors: 

$$
Q _ {k} = \operatorname {d i a g} \left(\max  \{0, \widetilde {Q} _ {k} (1, 1) \}, \dots , \max  \{0, \widetilde {Q} _ {k} (6, 6) \}\right). \tag {14}
$$

By updating the process noise covariance matrix $Q _ { k }$ using the adaptation method, we can obtain a fast and satisfactory estimation of the object’s motion even when its motion changes significantly, which will be shown in Section VI. To quickly and accurately estimate and predict the motion of the dynamic objects is vital for dynamic obstacle avoidance. Slow and wrong estimation could easily lead to collisions with the dynamic object. However, existing studies [7], [9], [11], [12] ignored this important issue. We will demonstrate in Section VI that a fast and precise prediction of the dynamic objects plays the key role for obstacle avoidance in complex dynamic environments. 

# V. FAST AND ADAPTIVE PLANNING

In this section, we will present our fast and adaptive planning which contains a trajectory optimization and an adaptive re-planning strategy. Our trajectory optimization does not require a front-end path search and takes into account the uncertainty of dynamic objects’ state estimation. Additionally, an adaptive re-planning is developed to address the case when a feasible solution is not found. The output is a dynamically feasible and safe trajectory. 

# A. Trajectory Definition

For a differentially flat system such as the UAV, we first define its motion as a piece-wise 3-dimension and 5-degree polynomials $p ( t )$ with $M$ pieces, and the lth piece can be expressed as: 

$$
p _ {l} (t) = \mathbf {c} _ {l} ^ {\mathrm {T}} \beta (t), \quad t \in [ 0, T _ {l} ], \tag {15}
$$

where $\mathbf { c } _ { l } \in \mathbb { R } ^ { 6 \times 3 }$ is the coefficient matrix of the piece and $\beta ( t ) = [ 1 , t , . . . , t ^ { 5 } ] ^ { \mathrm { T } }$ is natural basis vector. $T _ { l }$ is the duration of the piece. 

Then, we adopt MINCO (minimum control) [28] class to achieve the spatial-temporal decoupled optimization. The trajectory $p ( t )$ can only be parameterized by the time duration of each piece $\mathbf { T } = [ T _ { 1 } , . . . , T _ { M } ] ^ { \mathrm { T } }$ and the intermediate waypoints $\mathbf { q } = [ q _ { 1 } , . . . , q _ { M - 1 } ] ^ { \mathrm { T } }$ with a convenient space-time deformation $\mathcal { M }$ : 

$$
\mathbf {c} = \mathcal {M} (\mathbf {q}, \mathbf {T}), \tag {16}
$$

where $\mathbf { c } = [ \mathbf { c } _ { 1 } ^ { \mathrm { T } } , . . . , \mathbf { c } _ { M } ^ { \mathrm { T } } ]$ 

# B. Problem Formulation

For MINCO, a general optimization problem can be formulated as: 

$$
\min  _ {\mathbf {q}, \mathbf {T}} \mathcal {J} (\mathbf {q}, \mathbf {T}) + \sum \lambda_ {\star} \mathcal {I} _ {\star} (\mathbf {c} (\mathbf {q}, \mathbf {T}), \mathbf {T}), \tag {17}
$$

$$
\mathcal {J} = \int_ {0} ^ {T _ {t}} | | p ^ {(3)} (t) | | ^ {2} \mathrm {d} t + \rho T _ {t}, \quad T _ {t} = \sum_ {l = 1} ^ {M} T _ {l}, \tag {18}
$$

$$
\mathcal {I} _ {\star} = \sum_ {l = 1} ^ {M} \frac {T _ {l}}{\kappa_ {l}} \sum_ {\tau = 0} ^ {\kappa_ {l}} \mathcal {G} _ {\star} \left(\mathbf {c} _ {l}, T _ {l}, \frac {\tau}{\kappa_ {l}}\right), \tag {19}
$$

where $\mathcal { I }$ is the time-regularized control effort, which minimizes the jerk and the total duration $T _ { t }$ of the trajectory, and $\rho$ is the tunable weight value. $\mathcal { T }$ is the time integral penalty with weight $\lambda$ , and $\kappa$ means the sample numbers on a piece of trajectory, $\frac { \tau } { \kappa }$ indicates the specific timestamp. 

Then, we expect different types of cost function $\mathcal { G } _ { \star }$ to indicate the requirements of dynamic obstacle avoidance. The detailed penalty functions are designed as follows: 

1) Dynamical feasibility: The motion of the robot has to satisfy the dynamical feasibility. Here, we limit the range of velocity and acceleration by the cost function $\mathcal { G } _ { f }$ expressed as follows: 

$$
\mathcal {G} _ {v} = \max  \left\{\left(\left| \left| p _ {l} ^ {(1)} \left(t _ {\tau}\right) \right| \right| ^ {2} - v _ {\text {m a x}} ^ {2}\right), 0 \right\} ^ {3}, \tag {20}
$$

$$
\mathcal {G} _ {a} = \max  \left\{\left(\left\| p _ {l} ^ {(2)} \left(t _ {\tau}\right) \right\| ^ {2} - a _ {\text {m a x}} ^ {2}\right), 0 \right\} ^ {3}, \tag {21}
$$

$$
\mathcal {G} _ {f} = \mathcal {G} _ {v} + \mathcal {G} _ {a}, \tag {22}
$$

where $v _ { m a x }$ and $a _ { m a x }$ are the maximum allowed magnitudes of velocity and acceleration. $\begin{array} { r } { t _ { \tau } = T _ { l } \frac { \tau } { \kappa _ { l } } } \end{array}$ κl is a specific sample timestamp on the lth piece of the trajectory. 

2) Static obstacle avoidance: In Section III, we have obtained the static occupancy grid map, and the static obstacles can be modeled by the method in [2]. Then, for any point of $p ( t )$ , its distance to the closest obstacle can be calculated as 

a function $d _ { s } ( p ( t ) )$ . Then, the static obstacle collision cost $\mathcal { G } _ { s }$ can be formulated as: 

$$
\mathcal {G} _ {s} = \max  \left\{\left(\mathcal {D} _ {s} - d _ {s} \left(p _ {l} \left(t _ {\tau}\right)\right)\right), 0 \right\} ^ {3}, \tag {23}
$$

where $\mathcal { D } _ { s } = r _ { 0 } + \epsilon$ is the safety threshold between the robot and the obstacle surface, meaning a distance that a small constant $\epsilon$ greater than the radius of the robot $r _ { 0 }$ . 

3) Dynamic obstacle avoidance: Based on the tracking method of the moving objects proposed in III.C, the predicted trajectory $p _ { b } ( t )$ of a moving object with the estimated state position $\hat { \mathbf { o } } _ { k } ^ { i }$ and velocity $\hat { \dot { \bf o } } _ { k } ^ { i }$ at time $t _ { k }$ can be represented as: 

$$
p _ {b} ^ {i} (t) = \hat {\mathbf {o}} _ {k} ^ {i} + \hat {\dot {\mathbf {o}}} _ {k} ^ {i} (t - t _ {k}), \tag {24}
$$

By doing this, we can evaluate the safety of a trajectory at any time stamp. Therefore, for $I$ tracked moving objects, the dynamic obstacle collision cost $\mathcal { G } _ { d }$ can be designed as: 

$$
\mathcal {G} _ {d} = \sum_ {i = 1} ^ {I} \max  \left\{\left(\mathcal {D} _ {d} ^ {i} ^ {2} - \left| \left| p _ {l} \left(t _ {\tau}\right) - p _ {b} ^ {i} \left(t _ {\tau}\right) \right| \right| ^ {2}\right), 0 \right\} ^ {3}, \tag {25}
$$

where $\mathcal { D } _ { d } ^ { i } = r _ { 0 } + r ^ { i } + e ^ { i }$ is the safety clearance between the robot with radius $r _ { 0 }$ and the ith object with radius $r ^ { i }$ . The component $e ^ { i }$ represents the uncertainty of the estimated position at $t _ { \tau }$ , which can be defined by: 

$$
e ^ {i} = \sqrt {\sigma_ {\tau} ^ {i} (1 , 1) ^ {2} + \sigma_ {\tau} ^ {i} (2 , 2) ^ {2} + \sigma_ {\tau} ^ {i} (3 , 3) ^ {2}}, \tag {26}
$$

where $\sigma _ { \tau } ^ { i } = A _ { \tau } \sigma _ { k } ^ { i } A _ { \tau } ^ { \mathrm { T } }$ , means the transition of the covariance matrix from timestamp $t _ { k }$ to $t _ { \tau }$ of the object state. The difference between the formulation of $A _ { \tau }$ and $A _ { k }$ is $\Delta t$ in $A _ { k }$ and $\left( t _ { \tau } - t _ { k } \right)$ in $A _ { \tau }$ . The optimization for dynamic obstacles is described in Fig. 3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/7a207dc294c319d4872a3f4ffd9804c3a1afe307f5b9ea433ccd181e289732ee.jpg)



Fig. 3. The optimization of the trajectory to avoid a dynamic object. When the trajectory is not safe, the penalty will be added at each sample point (black dots), and the penalty incorporates the uncertainty of the prediction of dynamic objects (red dotted circle). After the optimization, the trajectory will be collision-free with dynamic objects. The optimization changes the position of intermediate waypoints $\mathbf { q }$ (yellow dots), as well as the time allocation of the trajectory pieces.


Considering the increasing uncertainty of $p _ { b } ^ { i }$ with the propagation of prediction time, $\mathcal { G } _ { d }$ is only valid while the prediction time $( t - t _ { k } )$ is within a given range. 

Above all, we have obtained the overall penalty in Eq. (18), and write it as $J ( \mathbf { q } , \mathbf { T } )$ for simplicity. To solve the optimization problem, we need the gradient of $J$ w.r.t q and the gradient 

of $J$ w.r.t T, which can be derived by the Gradient Propagation Law: 

$$
\frac {\partial J (\mathbf {q} , \mathbf {T})}{\partial \mathbf {q}} = \frac {\partial J}{\partial \mathbf {c}} \frac {\partial \mathbf {c}}{\partial \mathbf {q}}, \frac {\partial J (\mathbf {q} , \mathbf {T})}{\partial \mathbf {T}} = \frac {\partial J}{\partial \mathbf {T}} + \frac {\partial J}{\partial \mathbf {c}} \frac {\partial \mathbf {c}}{\partial \mathbf {T}}, \tag {27}
$$

where $\partial \mathbf { c } / \partial \mathbf { q }$ and $\partial \mathbf { c } / \partial \mathbf { T }$ can be derived from (8). Hitherto, this problem can be solved efficiently by unconstrained optimization algorithms such as L-BFGS. 

# C. Adaptive Re-planning Strategy

Our trajectory optimization can usually find a feasible solution when the environment is not complex. However, in the presence of dynamic cluttered environments, especially when the environment is small with many dynamic objects, trajectory optimization can usually fail. One common solution is to let the drone stay put to prevent wrong decisions. This decision, however, is dangerous in dynamic cluttered environments as dynamic objects can easily collide with the drone. To address this issue, we propose an adaptive replanning strategy to allow our drone to continue to carry out tasks without collisions even when a feasible solution is not found. 

Generally, our autonomous UAV has two mission states: navigating and hovering. Here, we present our adaptive planning strategy in the two states as follows: 

1) While navigating: When the UAV is navigating to a target position ${ \mathbf p } _ { f } \in \mathbb { R } ^ { 3 }$ , it is necessary to check the collision with static and dynamic obstacles within a certain period using the UAV trajectory $p ( t )$ , moving objects trajectory $p _ { b } ( t )$ and the occupancy grid map. If a collision risk is detected, the UAV will replan the trajectory based on the current state. However, if the dynamic obstacles are too dense, the feasible collisionfree trajectory to the target point $\mathbf { p } _ { f }$ may not exist. In this case, we need to calculate a temporary target position $\mathbf { p } _ { f } ^ { * }$ . First, for a moving object with a velocity ${ \bf v } _ { s }$ and a relative position vector $\mathbf { r } _ { s }$ to UAV, we generate a repulsion force vector $\mathbf { n } _ { s }$ where satisfies: 

$$
\mathbf {n} _ {s} = \frac {\mathbf {v} _ {s} \cdot \mathbf {r} _ {s}}{\left| \left| \mathbf {r} _ {s} \right| \right| ^ {2}} \mathbf {r} _ {s}, \tag {28}
$$

where $\mathbf { n } _ { s }$ indicates the component vector of ${ \bf v } _ { s }$ in the direction of $\mathbf { r } _ { s }$ . Then, we can calculate the total repulsion force vector ${ \bf n } _ { t o t a l } = \sum _ { s = 1 } ^ { S } { \bf n } _ { s }$ for the $S$ objects. Finally, $\mathbf { p } _ { 1 }$ can be determined by: 

$$
\mathbf {p} _ {f} ^ {*} = p \left(t _ {r}\right) + h \frac {\mathbf {n} _ {\text {t o t a l}}}{\left| \left| \mathbf {n} _ {\text {t o t a l}} \right| \right|}, \tag {29}
$$

where $h$ is the horizon of the intermediate target distance, and $t _ { r }$ is the time stamp while conducting the replanning. The description of this process is shown in Fig. 4. 

2) While hovering: If the UAV is hovering at $\mathbf { p } _ { 0 } ~ \in ~ \mathbb { R } ^ { 3 }$ and waiting for targets, while $S$ objects are moving toward the UAV that has a risk of collision in a short time $\delta$ , we expect the UAV to fly away from the objects by determining an intermediate target point $\mathbf { p } _ { f } ^ { * }$ to get a trajectory and replan to the original position after avoiding successfully. After the objects move away in $\delta$ , the robot will replan the trajectory back to the origin. The calculation of $\mathbf { p } _ { f } ^ { * }$ is the same with Eq. (29). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/40b1b52cea00b503ae11e68f75156aa3f6226350ecfbf3713da5e489d7f08085.jpg)



Fig. 4. The principle of the autonomous strategy. The method will plan a temporary target when the feasible collision-free trajectory to the target point $\mathbf { p } _ { f }$ does not exist. The repulsion force vector $\mathbf { n } _ { s }$ pushes the UAV to free space. A larger projection of $\mathbf { v } _ { s }$ in the direction of $\mathbf { r } _ { s }$ results in a more significant repulsion effect.


# VI. EXPERIMENTS AND EVALUATIONS

In this section, we test our system in both simulated and real-world dynamic cluttered environments. Comprehensive quantitative analyses are conducted to evaluate the advantages of our proposed system. 

# A. Implementation Details

For the experiments, we designed our experimental hardware platform UAV290, which is a $2 9 0 \mathrm { m m }$ wheelbase frame with the protection of the rotors, carrying an Intel NUC12WSHi7 running Ubuntu 20.04 as the onboard computer, and a Livox MID-360 Lidar with the FOV of $3 6 0 ^ { \circ }$ (horizontal) $\times 5 9 ^ { \circ }$ (vertical) and detection range of $4 0 \mathrm { m }$ within $10 \%$ reflectivity is equipped for onboard sensing, while publishing point cloud at $5 0 \mathrm { H z }$ . The controller of the UAV is a PixRacer-Pro running the PX4 flight stack. The overall system weighs $1 . 9 6 ~ \mathrm { k g }$ , with dimensions being $4 5 0 \times 4 5 0 \times 1 5 0 ~ \mathrm { m m }$ . The overview of our hardware platform is shown in Fig. 5. The simulation and evaluation of our algorithms are also conducted on Intel NUC12WSHi7. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/267b1066e465420c7167a5d1a035bd1b702ab901a9976bbd1b0f421933a03c55.jpg)



Fig. 5. Our UAV290 Hardware Platform.


# B. Evaluation of Dynamic Perception

Firstly, we quantitatively verify the accuracy and stability of our segmentation and state estimation for dynamic objects. Our work is compared with SOTA works and the results can be found in Table 1. The mean absolute error of our estimated position $e _ { p o s }$ achieves $0 . 1 1 \mathrm { ~ m ~ }$ and the mean absolute error of our estimated velocity $e _ { v e l }$ achieves $0 . 1 9 \mathrm { m } / \mathrm { s }$ . Multiple Object Tracking Accuracy (MOTA) $( \% )$ is defined in [29], while a higher value indicates better performance in detecting the dynamic objects and keeping the trackers. For our MOTA, it is composed of a false negative rate $f _ { n } = 4 . 3 \%$ (indicating nondetected dynamic objects), a false positives rate $f _ { p } = 5 . 2 \%$ (static objects misclassified as dynamic), and a mismatch rate $f _ { m } ~ = ~ 6 . 4 \%$ . The average time cost $t _ { p e r }$ of our algorithm achieves 12.77 ms, which is practical for real-time running on mobile terminals. The evaluation illustrates that our method improves tracking accuracy and robustness with less time cost in the clustered environment, and satisfies the requirements of real-time dynamic obstacle avoidance. The data collection for this evaluation is conducted in a motion capture room, with a running MID-360 Lidar and 3 people moving at about $1 ~ \mathrm { m / s }$ . 


TABLE I DYNAMIC PERCEPTION COMPARISON


<table><tr><td>Method</td><td>epos(m)</td><td>evel(m/s)</td><td>MOTA(%)</td><td>tper(ms)</td></tr><tr><td>Ours</td><td>0.17</td><td>0.29</td><td>84.10</td><td>12.77</td></tr><tr><td>[11]</td><td>0.24</td><td>0.35</td><td>82.90</td><td>29.52</td></tr><tr><td>[12]</td><td>0.33</td><td>0.37</td><td>76.40</td><td>40.33</td></tr><tr><td>[7]</td><td>0.34</td><td>0.41</td><td>70.20</td><td>40.52</td></tr></table>

To further demonstrate the effectiveness and efficiency of our proposed segmentation algorithm, we design two more scenarios. In the first scenario, we place the lidar in a room with four people. There are some obstacles surrounding the room and in the middle of the room to test the perception performance when an object is occluded by obstacles. All four persons have significantly different motions: one person standing still, one person walking back and forth, one person walking in a circular motion, and one person running. Please refer to the video for the real-time perception. Even though four people have different motions, their motions are all correctly detected and estimated. One snapshot of the video can be found in Fig. 6. It is seen in the figure that all dynamic objects have been segmented from the static local map. There is no false detection of dynamic objects. 

Finally, we hand-hold our drone with lidar and walk in a large-scale cluttered public zone. The zone is surrounded by walls, different static objects, and pedestrians. This is to test the perception performance of our algorithm in dynamic cluttered environments. As the zone and the number of objects are large, it is difficult to run existing methods in realtime as they need to design a Kalman filter for every object. Our method first segments the static and dynamic objects and then only design a Kalman filter for dynamic objects, which significantly reduces the computational load. As can be seen in our video, as the lidar moves in the large zone, all dynamic objects are segmented from static objects and their motions are also estimated in real time using our fast and adaptive 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/00436043dde7f9de816e54caf34f664f89ad4bc7332917c38206d6c1bf49a9e7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/b51d5685632443299078d770ff03c75afcc6d06ad688f89c29e5ffdabb7a1715.jpg)



Fig. 6. Dynamic perception in a small dynamic cluttered room. (a) is the third-person view image of the scenario. (b) is the data visualization in rviz.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/e4ff8faac760d0bf7686844de350585bbb2b3499bff46b02968abdd563c273db.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/e85c063b07cf4d8b1525d9cc5d8a6c680f2aef7e5af193ff637b910918e107db.jpg)



Fig. 7. Dynamic perception in a large-scale dynamic cluttered public zone. (a) is the first-person view image of the scenario. (b) is the data visualization in rviz.


perception method. One snapshot can be found in Fig. 7. It is seen that there are 10 dynamic objects near the lidar. No static walls or objects have been detected as dynamic objects, which shows the superior segmentation performance of our algorithm. 

# C. Evaluation of the Adaptive Perception with Covariance Adaptation

To show the advantages of our proposed adaptive perception in dynamic cluttered environments, we perform an ablation study. In the simulation, we compare the velocity estimation performance with and without covariance adaptation. We simulate three dynamic objects with different motions 1): an emerging object with a constant velocity of 5 m/s. 2): an object that changes the direction of motion rapidly, with an acceleration at $3 m / s ^ { 2 }$ from 0 s to 1.0 s and 1.2 s to $2 . 0 \ s$ $- 3 0 m / s ^ { 2 }$ from 1.0 s to 1.2 s. For this object, the acceleration also changes significantly. Therefore, the constant acceleration model also cannot reflect its real motion. 3): an object moving with a sinusoidal velocity, with a period of 1 s and amplitude of $6 . 2 8 ~ \mathrm { m } / \mathrm { s }$ . 

The result is shown in Fig. 8. As can be seen in Fig. 8, the filter with covariance adaptation can quickly estimate the changes in the velocities while the one without covariance adaptation takes a long time to estimate the velocities. The covariance adaptation method can obtain satisfactory results no matter if the velocity or the acceleration changes significantly. The mean absolute errors of the estimations are shown in 

Table II. We notice that the mean absolute error $e _ { v e l }$ and the time cost of converging to within $10 \%$ error $t _ { c o n }$ significantly reduce with our covariance adaptation, which demonstrates a higher accuracy and faster response. Especially, when the object is in non-uniform motion, the velocity cannot be predicted well without the covariance adaptation. 


TABLE II ABLATION STUDY OF THE COVARIANCE ADAPTATION


<table><tr><td>Scenario</td><td>Method</td><td>\( e_{vel}(m/s) \)</td><td>\( t_{con}(s) \)</td></tr><tr><td rowspan="2">Condition 1</td><td>Ours</td><td>0.29</td><td>0.10</td></tr><tr><td>w/o adaptation</td><td>0.99</td><td>0.40</td></tr><tr><td rowspan="2">Condition 2</td><td>Ours</td><td>0.08</td><td>0.08</td></tr><tr><td>w/o adaptation</td><td>0.56</td><td>/</td></tr><tr><td rowspan="2">Condition 3</td><td>Ours</td><td>0.36</td><td>0.14</td></tr><tr><td>w/o adaptation</td><td>2.39</td><td>/</td></tr></table>

This improvement in state estimation of dynamic objects will greatly improve the dynamic obstacle avoidance. Without such estimation, obstacle avoidance can easily fail in highly dynamic cluttered environments. We also design multiple simulation tests to show its effectiveness for dynamic obstacle avoidance. We let an object move towards a hovering UAV with a random rapid acceleration. The initial velocity of the object is $1 m / s$ , and the acceleration of the object ranges from $1 m / s ^ { 2 }$ to $5 m / s ^ { 2 }$ . In 50 tests, the UAV achieves a success rate of $94 \%$ with covariance adaptation, however, when the covariance adaptation is eliminated, the success rate is only $48 \%$ . An example of the comparison is shown in Fig. 9. Due to this reason, for all the following simulation tests or experiments, we all use the perception with the covariance adaptation unless specified. 

# D. Evaluation of Obstacle Avoidance in Simulation

In this section, we present the simulation results of the obstacle avoidance. We demonstrate UAV obstacle avoidance performance in three different environments: 1): A field with complex random static obstacles and dynamic objects. The field is $5 0 \mathrm { m } { } ^ { * } 5 0 \mathrm { m }$ , with 100 static boxes and 100 static circles randomly placed in it. We generate 100 moving obstacles with random velocities varying from $0 . 5 m / s$ to $3 m / s$ and random radius varying from $0 . 2 \mathrm { m }$ to $1 . 0 \mathrm { { m } }$ . The UAV should navigate to any target point safely in this environment. 2): A narrow corridor with dynamic objects moving in two opposite directions. The corridor is $4 0 \textrm { m }$ in length and $3 \textrm { m }$ in width, with 50 moving obstacles at velocities varying from $0 . 5 ~ \mathrm { m / s }$ to $3 \ \mathrm { m / s }$ . The UAV is required to fly through the corridor without collision. 3): A narrow corridor blocked by dynamic objects moving together. 5 moving objects in a row moving at the same velocity $( 0 . 6 ~ m / s )$ along the corridor. In this case, no feasible collision-free trajectory can be solved to reach the target point, and the UAV is expected to choose a temporary target point for planning. The map and the states of the objects are published at $5 0 \mathrm { H z }$ . To simulate the time cost of perception, we add the preassigned time delay $t _ { d e l a y }$ after the planner receives the objects’ state. $t _ { d e l a y }$ is set as 12.77 ms, which is the average time cost of our mapping algorithm shown in Table I. The visualization in Rviz of the results is 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/62d9278bb9e7637c481e1fa10661e601a0f73377dc81500aed0a832105678651.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/f7d9b8924bf32d62fb626ff43de087114909667178d5880a1d319e68584a3720.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/bd8706c798f1368dd22896553a4110c5730ff9114fde5228f4c863589ff80224.jpg)



Fig. 8. The comparison of the velocity estimation with covariance adaptation and without covariance adaptation.



With Adaptive Covariance :


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/ecb4998ec0fd49836561cd16ce757a375d88ed80ced59a56644f2391f7c3dc90.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/9f0cc2b5eec21e54925a0fcc80a150bc33fdd656707f787ecb687221c6879ee6.jpg)



Without Adaptive Covariance :


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/de9f834b59d713ae1b17a02533cfec67e0a239da8098dce68c91d726018f035c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/3edc9d1549838f09ca02f43e2a2ef3c916eee98c7bd1c84040e31740b9dd3bc2.jpg)



Fig. 9. With adaptive covariance updating, the state estimation Kalman filtering will approach the ground truth value faster, which has a significant improvement on obstacle avoidance.


shown in Fig. 10. Please refer to our video for the whole dynamic obstacle avoidance process. The performance of the simulation flight tests demonstrates the ability of our method to tackle various complex dynamic cluttered environments. 

Afterward, to verify the advantage of our obstacle avoidance method, we compare it with the method in [9], [11], and [7]. We performed 50 tests with each method in the three environments mentioned above and summarized the success rate $\eta ( \% )$ , average energy cost $E _ { A } ( m / s ^ { 3 } )$ , and average time cost $t _ { p l a n } ( m s )$ of algorithms. When a collision occurs, the test will be considered a failure. Energy cost is the jerk integral of the complete trajectory. The result can be found in Table III. 

From Table III we conclude that our method shows superiority in time cost and success rate of obstacle avoidance. Especially in environment 3, only our method can successfully tackle the problem in this situation. The trajectory energy cost of our method is slightly higher than the method in [9]. This is due to the trajectory in [9] being initialized by its front-end kinodynamic path searching. However, the polygon 


Environment 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/960cffd416468c027d014d24d834cef73070374478c91dc60886cbd68c06d14f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/b9ac72c03637648a5f2cbaf45bd38988e287703fad6de1c48351a1205a07eaeb.jpg)



Environment 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/20a88c33740dcd992631776c138cd092806ec7ecf120119bda9d1f7a85b2d983.jpg)



Environment 3


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/7cbce7f21ab578bcab76d93ecdb5486891a2c63f82f68662254d2e30ac6aec87.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/8e8f79f7fe2db7a0a1846082ae21d3175397f9de0e336b5396751f78928d1e43.jpg)



Optimal Trajectory



Flight Path



Fig. 10. Dynamic planning of UAV in 3 types of simulation environments.


generation in the front end will be very time-consuming when there is an excessive density of obstacles. That is why our method is significantly faster than all other methods. Moreover, the constraint of the complex polygons will also limit the feasibility of the trajectory, which might cause a failure of optimization. 


TABLE III DYNAMIC PLANNING BENCHMARK COMPARISON


<table><tr><td>Scenario</td><td>Method</td><td>EA(m/s3)</td><td>tplan(ms)</td><td>η(%)</td></tr><tr><td rowspan="4">Environment 1</td><td>Ours</td><td>1.44</td><td>2.48</td><td>94</td></tr><tr><td>[9]</td><td>1.23</td><td>9.59</td><td>78</td></tr><tr><td>[11]</td><td>2.85</td><td>5.79</td><td>70</td></tr><tr><td>[7]</td><td>2.14</td><td>7.21</td><td>74</td></tr><tr><td rowspan="4">Environment 2</td><td>Ours</td><td>1.48</td><td>3.12</td><td>88</td></tr><tr><td>[9]</td><td>1.31</td><td>13.10</td><td>64</td></tr><tr><td>[11]</td><td>2.52</td><td>6.59</td><td>58</td></tr><tr><td>[7]</td><td>2.33</td><td>7.68</td><td>52</td></tr><tr><td rowspan="4">Environment 3</td><td>Ours</td><td>2.35</td><td>2.80</td><td>90</td></tr><tr><td>[9]</td><td>/</td><td>/</td><td>/</td></tr><tr><td>[11]</td><td>/</td><td>/</td><td>/</td></tr><tr><td>[7]</td><td>/</td><td>/</td><td>/</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/f750585b03c6099eb9c36a8471e9f61ce9bfe01c41c98fbbb6f391d7c969b45d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/603d88697e3fe8e6a639773473fcf49d6ea9f7b11b8249e3b3af2748cc749f4f.jpg)



Fig. 11. The composed images of dodging a flying box. The left image is a success case running with covariance adaptation, the left is a fail case without covariance adaptation.


# E. Real-world Flight Experiments

Based on the simulation and quantitative studies, we finally validate our whole system in real-world experiments. Among all tests, the UAV uses the lidar inertial odometry algorithm Fast-Lio2 at $5 0 \mathrm { H z }$ [23] for localization. The run time of each module in real flight is summarized in Table IV. Overall, the entire system only takes about 20 ms in each iteration. 


TABLE IV THE RUN TIME OF EACH MODULE OF OUR PROPOSED SYSTEM


<table><tr><td>Modules</td><td>Time(ms)</td><td>Portion(%)</td></tr><tr><td>Onboard Localization</td><td>4.58</td><td>22.79</td></tr><tr><td>Fast and Adaptive Perception</td><td>12.77</td><td>63.53</td></tr><tr><td>Fast and Adaptive Planning</td><td>2.75</td><td>13.68</td></tr><tr><td>Total</td><td>20.10</td><td>100</td></tr></table>

We first performed the ablation experiments to validate the advantage of our covariance adaptation approach. In 10 tests for each of the two groups, people at a distance of about $5 \textrm { m }$ threw a box toward the hovering UAV. Dynamic obstacle avoidance with covariance adaptation succeeded 9 times, while the one without covariance adaptation succeeded only 2 times. We present a demo of comparison in Fig. 11. For this reason, all the following experiments are performed using the covariance adaptation. 

Afterward, we designed two types of scenarios for testing our system for dynamic cluttered environments. In the first scenario, the UAV is required to patrol a room from one corner to another while there are many “workers” moving boxes in the patrol route and pedestrians passing through the patrol route. As the UAV size is large, the room filled with so many people 

is a very cluttered environment with dynamic obstacles. Please refer to the video for the whole avoidance process. Moving “workers” and pedestrians are segmented from the static map and their motions are estimated using the adaptive estimation. The system outputs an optimized trajectory based on the predicted states of each dynamic object. The UAV, “workers” and pedestrians can work together without collisions. Some snapshots are given in Fig. 12. 

In the second scenario, the UAV is flying on a park sidewalk full of pedestrians and surrounded by common facilities and trees. As can be seen from the video, the UAV can successfully pass all of the pedestrians without collisions with people and the surrounding facilities. Some snapshots are shown in Fig. 13. All the experiments are repeated many times. Repeated experiments show similar patterns and are not shown. All these experimental tests verified our proposed system can handle highly dynamic and cluttered environments. 

# VII. CONCLUSION

In this paper, we considered the obstacle avoidance of UAVs in a complex dynamic and cluttered environment. We proposed FAPP to tackle the challenges in perception and planning brought by dynamic cluttered objects. The fast perception system can efficiently segment static and dynamic objects. To address the limitation of a constant velocity or acceleration model, we proposed an adaptive estimation that can quickly and accurately predict the motion of multiple dynamic objects. The proposed adaptive estimation also greatly facilitated the dynamic obstacle avoidance. Furthermore, our fast and adaptive planning can even address the case when trajectory optimization cannot find a feasible solution, which is common in dynamic cluttered environments. 

Our proposed system performs satisfactorily in dynamic cluttered environments. However, if the onboard localization fails while the UAV is performing aggressive maneuvers, it may experience failure occasionally. Future work would explore how to avoid failures even when the onboard localization fails. 

# ACKNOWLEDGEMENT

The authors gratefully thank Huibin Zhao, Qiyuan Qiao, Mingyang Li, Yuting Tao, Xiao Cao, Jingjan Lin, Yi Luo, Peiyu Chen, Weipeng Guan, and Fuling Lin for the experiment support. 

# REFERENCES



[1] B. Zhou, H. Xu, and S. Shen, “Racer: Rapid collaborative exploration with a decentralized multi-uav system,” IEEE Transactions on Robotics, vol. 39, no. 3, pp. 1816–1835, 2023. 





[2] X. Zhou, Z. Wang, H. Ye, C. Xu, and F. Gao, “Ego-planner: An esdffree gradient-based local planner for quadrotors,” IEEE Robotics and Automation Letters, vol. 6, no. 2, pp. 478–485, 2021. 





[3] A. Alcantara, J. Capit ´ an, R. Cunha, and A. Ollero, “Optimal trajectory ´ planning for cinematography with multiple unmanned aerial vehicles,” Robotics and Autonomous Systems, vol. 140, p. 103778, 2021. 





[4] C. Richter, A. Bry, and N. Roy, “Polynomial trajectory planning for aggressive quadrotor flight in dense indoor environments,” in Robotics Research: The 16th International Symposium ISRR, pp. 649–666, Springer, 2016. 



![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/f9b25bb17e2c9624612d3dc3e8ac4a1352ffd4190e399af912810e6932366e86.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/ccb9ee2ae5ea2e9c54d33d9d579baefb56f60e1a9bb8f677788acbc3f2d19386.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/c191066ca3bc5ff23013d64991190722e6da95ea4607c1b02887db2f471d953b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/cac0b9fd2b192dddbb2c874c6c7bd0150549d5c579ebb6e1480cf632a903d0a9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/4d03ac567035bc61d2a1ddb82e79c311dc63327cb508e651cc626a44f1467bd0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/1e6ce2064211f56914fa05cdabccdd4d45f10f58d627e3b426a9f90b08251677.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/c44f3aee0b2d68258a7433b70f6f6c45b2bbc2d4e4a943014888b0766c6ae64a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/71628221ec99f048d1ae615a474bdd6fddb718689e40bd87f67e7baf7166dacc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/c38a66e0d4160de87316b375cf6a0b7cff4b7c53626e9340440e4efbb730b2d4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/ddef46edc9b6f4a247dd60915b21e9d2f5faffe8a003670f34a733f64da75bdd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/7e3f6c55e2546f274eec7592dfa50d763460c303936e5c809be8844f21e337fd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/913cc91a78d63628c62461cf20bff0d5e09e507dea3e267509551d05e446966e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/e4485423ca63ef83d787fa83ba5edd98c368000d0145040645213b7a9e612134.jpg)



Dynamic points



Dynamic cluster



Velocity vector



Optimal trajectory



Fig. 12. The results of the indoor flight test. (a) - (f) is the third-person view snapshots of the indoor experiment with the corresponding data visualization in (g) - (l). 6 workers were carrying boxes, and the UAV could patrol the small room autonomously.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/8c356f20a936123d6c35b6897d4c1bd542edd34f63820399da73705a1cfe20dc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/69fa1cb9aebdb9a487755561d6b2974f134e7846ef4ece0906dc4ae2b795a958.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/b9a29774965e698b0c2bc8614dc8634a71e3508e0b6e3bccec07cbbb4ee48510.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/2cc5dbb822385c5d5ef7f1b3f01540ffc1ac6cd989048b1232b274e7d5e14b97.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/aa67062d269271e47018bc6e05085c3b650b072a044fe8c21168e3ba7b707635.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/5c0f1de550ebf8c918981c1bb63e1cd4baf74af0161d1db88daaa12dbba2cf27.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/1bd78fb7bc4001963ee7ac6ee4cf14d3b10a16fa4ea6ee5d10f8a044ab038074.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/a5c4d4cbcebe5f839061adf0fff0786a5e84c6d6139b57cfe27469fbccdf43b7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/62b3173d9621314b6d8aace0e629846f12d869a9b6e69c379e6da9d855e845e8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/303633871eabe583ea2117c1cf39a1e199ec8e2b8e6cf6cdfdfe1e715c0b2d5d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/4c71e31108a30e1febe5d92c9aed8a364f884d85728bb104bb2e8767ca52c44c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/e9ae7edb23139e78c38a002b202ceade68c4c2a46aa577940014fa4e605a0d75.jpg)



Fig. 13. The results of the outdoor flight test. (a) - (f) presents the bird’s-eye view snapshots of the outdoor experiment. (g) - (l) is the screenshots of data visualization in Rviz corresponding with (a) - (f). The UAV avoided the 6 walking persons while navigating on the park sidewalk.




[5] Y. Song, K. Shi, R. Penicka, and D. Scaramuzza, “Learning perceptionaware agile flight in cluttered environments,” in 2023 IEEE International Conference on Robotics and Automation (ICRA), pp. 1989–1995, 2023. 





[6] D. Falanga, K. Kleber, and D. Scaramuzza, “Dynamic obstacle avoidance for quadrotors with event cameras,” Science Robotics, vol. 5, no. 40, p. eaaz9712, 2020. 





[7] J. Lin, H. Zhu, and J. Alonso-Mora, “Robust vision-based obstacle avoidance for micro aerial vehicles in dynamic environments,” in 2020 IEEE International Conference on Robotics and Automation (ICRA), pp. 2682–2688, IEEE, 2020. 





[8] B. He, H. Li, S. Wu, D. Wang, Z. Zhang, Q. Dong, C. Xu, and F. Gao, “Fast-dynamic-vision: Detection and tracking dynamic objects with event and depth sensing,” in 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 3071–3078, IEEE, 2021. 





[9] M. Lu, H. Chen, and P. Lu, “Perception and avoidance of multiple small fast moving objects for quadrotors with only low-cost rgbd camera,” IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 11657–11664, 2022. 





[10] Z. Xu, D. Deng, Y. Dong, and K. Shimada, “Dpmpc-planner: A realtime uav trajectory planning framework for complex static environments with dynamic obstacles,” in 2022 International Conference on Robotics and Automation (ICRA), pp. 250–256, 2022. 





[11] H. Chen and P. Lu, “Real-time identification and avoidance of simultaneous static and dynamic obstacles on point cloud for uavs navigation,” Robotics and Autonomous Systems, vol. 154, p. 104124, 2022. 





[12] Y. Wang, J. Ji, Q. Wang, C. Xu, and F. Gao, “Autonomous flights in dynamic environments with onboard vision,” in 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 1966–1973, IEEE, 2021. 





[13] G. Chen, W. Dong, X. Sheng, X. Zhu, and H. Ding, “An active sense and avoid system for flying robots in dynamic environments,” IEEE/ASME Transactions on Mechatronics, vol. 26, no. 2, pp. 668–678, 2021. 





[14] T. Fan, B. Shen, H. Chen, W. Zhang, and J. Pan, “Dynamicfilter: an online dynamic objects removal framework for highly dynamic environ-





ments,” in 2022 International Conference on Robotics and Automation (ICRA), 2022. 





[15] H. Lim, S. Hwang, and H. Myung, “Erasor: Egocentric ratio of pseudo occupancy-based dynamic object removal for static 3d point cloud map building,” IEEE Robotics and Automation Letters, vol. 6, no. 2, pp. 2272–2279, 2021. 





[16] G. Kim and A. Kim, “Remove, then revert: Static point cloud map construction using multiresolution range images,” in 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 10758–10765, 2020. 





[17] T. Eppenberger, G. Cesari, M. Dymczyk, R. Siegwart, and R. Dube,´ “Leveraging stereo-camera data for real-time dynamic obstacle detection and tracking,” in 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 10528–10535, 2020. 





[18] X. Chen, B. Mersch, L. Nunes, R. Marcuzzi, I. Vizzo, J. Behley, and C. Stachniss, “Automatic labeling to generate training data for online lidar-based moving object segmentation,” IEEE Robotics and Automation Letters, vol. 7, no. 3, pp. 6107–6114, 2022. 





[19] B. Mersch, X. Chen, I. Vizzo, L. Nunes, J. Behley, and C. Stachniss, “Receding moving object segmentation in 3d lidar data using sparse 4d convolutions,” IEEE Robotics and Automation Letters, vol. 7, no. 3, pp. 7503–7510, 2022. 





[20] P. Fiorini and Z. Shiller, “Motion planning in dynamic environments using velocity obstacles,” The international journal of robotics research, vol. 17, no. 7, pp. 760–772, 1998. 





[21] N. Malone, H.-T. Chiang, K. Lesser, M. Oishi, and L. Tapia, “Hybrid dynamic moving obstacle avoidance using a stochastic reachable setbased potential field,” IEEE Transactions on Robotics, vol. 33, no. 5, pp. 1124–1138, 2017. 





[22] B. Zhou, F. Gao, L. Wang, C. Liu, and S. Shen, “Robust and efficient quadrotor trajectory generation for fast autonomous flight,” IEEE Robotics and Automation Letters, vol. 4, no. 4, pp. 3529–3536, 2019. 





[23] W. Xu, Y. Cai, D. He, J. Lin, and F. Zhang, “Fast-lio2: Fast direct 





lidar-inertial odometry,” IEEE Transactions on Robotics, vol. 38, no. 4, pp. 2053–2073, 2022. 





[24] Y. Cai, W. Xu, and F. Zhang, “ikd-tree: An incremental kd tree for robotic applications,” arXiv preprint arXiv:2102.10808, 2021. 





[25] M. Ester, H.-P. Kriegel, J. Sander, X. Xu, et al., “A density-based algorithm for discovering clusters in large spatial databases with noise.,” in kdd, vol. 96, pp. 226–231, 1996. 





[26] N. Wojke, A. Bewley, and D. Paulus, “Simple online and realtime tracking with a deep association metric,” in 2017 IEEE international conference on image processing (ICIP), pp. 3645–3649, IEEE, 2017. 





[27] P. Lu, E. van Kampen, C. de Visser, and Q. Chu, “Framework for state and unknown input estimation of linear time-varying systems,” Automatica, vol. 73, pp. 145–154, 2016. 





[28] Z. Wang, X. Zhou, C. Xu, and F. Gao, “Geometrically constrained trajectory optimization for multicopters,” IEEE Transactions on Robotics, vol. 38, no. 5, pp. 3259–3278, 2022. 





[29] K. Bernardin, A. Elbs, and R. Stiefelhagen, “Multiple object tracking performance metrics and evaluation in a smart room environment,” in Sixth IEEE International Workshop on Visual Surveillance, in conjunction with ECCV, vol. 90, Citeseer, 2006. 



![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/b41f9c27ae7d5f2776a3c92573099beea4d44efd85c02a91ef849c26e643f6b6.jpg)


Peng Lu obtained his BSc degree in automatic control and MSc degree in nonlinear flight control both from Northwestern Polytechnical University (NPU). He continued his journey on flight control at Delft University of Technology (TU Delft) where he received his PhD degree in 2016. After that, he shifted a bit from flight control and started to explore control for ground/construction robotics at ETH Zurich (ADRL lab) as a Postdoc researcher in 2016. He also had a short but nice journey at University of Zurich & ETH Zurich (RPG group) 

where he was working on vision-based control for UAVs as a Postdoc researcher. He was an assistant professor in autonomous UAVs and robotics at Hong Kong Polytechnic University prior to joining the University of Hong Kong in 2020. 

Prof. Lu has received several awards such as 3rd place in 2019 IROS autonomous drone racing competition and best graduate student paper finalist in AIAA GNC (top conference in aerospace). He serves as an associate editor for 2020 IROS (top conference in robotics) and session chair/co-chair for conferences like IROS and AIAA GNC for several times. He also gave a number of invited/keynote speeches at multiple conferences, universities and research institutes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/74a5c99c5c9866dd117858c2c63332c8bdefc571d96e97c8667b6debb708cc3e.jpg)


Minghao Lu received his Bachelor of Engineering in Automation in 2021 from Harbin Institute of Technology, China. 

He is currently working toward the Ph.D. degree in Mechanical Engineering at Adaptive Robotic Controls Lab (Arc-Lab) from the University of Hong Kong, China. His research interests include motion planning, robotic control, robotic vision, and aerial systems. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/a1ec1df21fecfc4b20a4e0214aebacab52bc844cdf500a638da2612fa77d824a.jpg)


Xiyu Fan received his Bachelor of Engineering in Automation in 2023 from Harbin Institute of Technology, China. 

He is currently working toward the Ph.D. degree in Mechanical Engineering at Adaptive Robotic Controls Lab (Arc-Lab) from the University of Hong Kong, China. His research interests include reinforcement learning, robotic control, and aerial systems. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/edf36acc-4cb8-4389-a986-560f4e770d8b/39823d527bd41bfcfb3b18ff366f6cf33fdb3f6b83e38528777b91e01dfb58d9.jpg)


Han Chen received his Bachelor of Engineering in 2016 from Beijing Institute of Technology, China, and his Master of Science from Beijing Institute of Technology in 2019. In 2023, he obtained his Doctor of Philosophy from the Department of Aeronautical and Aviation Engineering, The Hong Kong Polytechnic University. 

He is now a senior engineer at Huawei Technologies Co., Ltd, working on mapping engine. 