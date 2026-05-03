# Integrated Longitudinal and Lateral Hierarchical Control of Cooperative Merging of Connected and Automated Vehicles at On-Ramps

Shoucai Jing , Fei Hui, Xiangmo Zhao , Jackeline Rios-Torres , Senior Member, IEEE, and Asad J. Khattak 

Abstract— Connected and automated vehicles (CAVs) can improve traffic safety and transportation network efficiency while also reducing environmental impacts. However, congestion and accidents can easily occur at merging roadways. Therefore, coordinating cooperative merging of CAVs is one of the most common traffic management problems. This paper addresses the problem of integrated longitudinal and lateral cooperative merging control with practical implications for CAVs approaching on-ramps. A hierarchical and decentralized cooperative coordination framework was developed to systematically control the merging of CAVs. The control system of each vehicle can be divided into an upper-level and lower-level. For upper-level control, an optimal control-based algorithm considering input constraints was presented to optimize fuel consumption and passenger comfort. A decision strategy was developed to optimize the start time of lateral trajectory planning. To achieve lowerlevel control, a Proportional-Integral (PI) controller was used for tracking the optimized longitudinal speed of the upper-level and a decentralized unified algorithm based on nonlinear model predictive control was proposed for tracking the upper-level optimal trajectory. To avoid lateral collision, the driving safety field based on vehicle size and motion state was selected as one of tracking the optimization objectives. Efficiency of the proposed framework and the algorithm was validated by CarSim/Simulink co-simulations of near-real-world vehicle scenarios. The proposed 

Manuscript received 18 November 2021; revised 13 July 2022; accepted 29 August 2022. Date of publication 21 September 2022; date of current version 5 December 2022. This work was supported in part by the National Key Research and Development Program of China under Grant 2021YFB2501202, in part by the National Natural Science Foundation of China under Grant 52202395, in part by the Key Research and Development Plan of Shaanxi Province under Grant 2021ZDLGY04-06, and in part by the Fundamental Research Funds for the Central Universities under Grant 300102241103. The work of Jackeline Rios-Torres was supported by the Laboratory Directed Research and Development Program of the Oak Ridge National Laboratory, managed by UT-Battelle, LLC, for the U.S. Department of Energy. The Associate Editor for this article was B. Fidan. (Corresponding authors: Fei Hui; Shoucai Jing.) 

Shoucai Jing is with the School of Information Engineering, Chang’an University, Xi’an 710064, China, and also with the Research and Development Center on Emergency Support Technologies for Transport, CCCC First Highway Consultants Company Ltd., Xi’an 710000, China (e-mail: scjing@chd.edu.cn). 

Fei Hui and Xiangmo Zhao are with the School of Information Engineering, Chang’an University, Xi’an 710064, China (e-mail: feihui@chd.edu.cn; xmzhao@chd.edu.cn). 

Jackeline Rios-Torres is with the Energy and Transportation Science Division, Oak Ridge National Laboratory, Oak Ridge, TN 37831 USA (e-mail: riostorresj $@$ ornl.gov). 

Asad J. Khattak is with the School of Information Engineering, Chang’an University, Xi’an 710064, China, and also with the Department of Civil and Environmental Engineering, The University of Tennessee Knoxvile, Knoxvile, TN 37996 USA (e-mail: akhattak@chd.edu.cn). 

Digital Object Identifier 10.1109/TITS.2022.3204033 

integrated merging control system can improve traffic efficiency and reduce fuel consumption compared to baseline with the potential for real-world application. Furthermore, the results demonstrate the potential applicability of cooperative control methods based on upper-level vehicle control. 

Index Terms— Connected and automated vehicles (CAVs), cooperative merging control, on-ramp merging, hierarchical decentralized framework, CarSim/Simulink. 

# I. INTRODUCTION

M ERGING roadways are a major source of conflictand congestion, and can lead to traffic accidents and andcongestinandcanleadtotraffcacidentsand huge economic losses [1], [2], [3], [4]. Moreover, congestion reduces traffic efficiency, causes passenger discomfort and results in excessive fuel consumption [5], [6], [7]. Typically, vehicles attempting to merge onto a main road initially slow down upon entering the on-ramp, wait for a safe distance between vehicles, gauge the mainstream vehicle speed, and then decide when and how much to accelerate before finally merging into the main traffic flow. Effective merging control methods can reduce congestion by eliminating the conflict between vehicles in time and space at merging roadways [8]. However, optimized merging control maneuvers are difficult to execute smoothly with manual driving due to diverse driving abilities, driver characteristics, and driving styles. 

Connected and automated vehicles (CAVs) can significantly reduce traffic congestion and improve vehicle safety through efficient vehicle coordination algorithms [9], [10], [11], [12], [13]. A number of approaches have been proposed to improve both safety and efficiency of CAVs at intersections and merging sections. Chen and Englund [14] surveyed key technologies and control maneuvers used in vehicle management for coordinating CAVs. Typically, a traffic manager communicates with each vehicle to optimize a specific performance criterion, such as efficiency, traffic flow or travel time. Several methods for cooperative control of vehicles have been reported in the literature [15], [16], [17], [18]. 

The majority of algorithms reduce traffic congestion and improve merging efficiency by controlling CAVs at on-ramps. An in-depth literature review of research on CAVs merging at on-ramps can be found in Rios-Torres and Malikopoulos [19]. Strategies for CAV coordination can be divided into centralized and decentralized approaches. 

In centralized approaches, a global traffic management controller decides on the action of each vehicle within the control 

zone. A merging strategy was developed by Athans [20], in which the cooperative merging problem was formulated as a linear regulator to control a string of vehicles. Ran et al. [21] proposed a microscopic automated merging maneuver to adjust gaps in the mainstream traffic flow, allowing vehicles to merge. The slot-based merging algorithm proposed by Marinescu et al. [22] divides the road into slots that are either free or occupied. Subsequently the traffic manager selects suitable slots on the main road for vehicles at on-ramps to merge into. This kind of approach requires high-precision vehicle positioning and intensive vehicle-to-infrastructure (V2I) communication. An optimal problem was formulated and solved to optimize travel time while avoiding collisions under the different constraints [23], [24], [25], [26], [27], [28]. The aforementioned methods mainly focus on merging maneuvers to achieve safe and highly efficient traffic. 

Recently, several methods have been proposed for the multi-objective optimization of cooperative merging problems.A parsimonious shooting heuristic algorithm and framework were proposed to optimize vehicle trajectories on a signalized highway segment and to analytically formulate the relationship between queue propagation and trajectory smoothing [12], [29], [30], [31]. Rios-Torres et al. [32], [33] derived an analytical solution for optimal coordination of CAVs inside the merging control zone. The square of the acceleration was selected as the objective function to reduce fuel consumption and improve traffic efficiency. Similarly, a trajectory planning method was developed to improve fuel efficiency and enhance passenger comfort by including jerk and its first derivative as part of the objective function [34]. An analytical solution based on optimal theory, linear-quadratic regulator approach, and model predictive control scheme was derived to manage possible disturbances in vehicle strings. In order to optimize lane changes and ensure that vehicles follow certain trajectories in multilane freeway merging systems, Hu and Sun [35] presented an online control algorithm and modeled the merging system as a time-discrete linear system. A grouping-based cooperative control strategy for CAVs merging was proposed to achieve a good tradeoff between computation time and merging performance [36]. In our previous work, a cooperative multi-player game-based optimization framework and algorithm were developed to achieve global optimization of merging sequences and vehicle longitudinal motion control [37]. Centralized approaches make full use of global information, and can be applied to high-level decision and control processes, but they require more computational efforts. 

In decentralized approaches, each vehicle is controlled independently according to information received from other vehicles. A number of approaches based on game theory have been presented for modeling lane-changing decisions of merging vehicles without considering the specific motion trajectory [38], [39]. Furthermore, the impact of lane-changing execution time during mandatory and discretionary lane-changing maneuvers was investigated under connected environment [40], [41]. The concept of virtual platooning was proposed by Lu et al. [42], [43] to map vehicles merging from the ramp onto the main road by creating a 

virtual platoon. Then, the controller simply adjusts the speed and acceleration of each vehicle to ensure that it arrives at the merging point at the appropriate time. In another study, a threelayer fuzzy logic controller was designed to control vehicle speed and ensure that a vehicle safely crosses the intersection [44]. From top to bottom, different layers played various roles related to decision-making, control and execution and this controller was later validated through field testing [45]. 

Another decentralized merging assistant based on a cooperative adaptive cruise control (CACC) system was designed to smooth traffic flow in mixed traffic situations [46], [47]. The CACC-equipped vehicle was found to reduce conflicts associated with merging traffic [48]. A decentralized optimal control framework was formulated for minimizing fuel consumption and feasible analytical solutions were derived under hard constraints [49], [50], [51], [52]. Similarly, the square of acceleration was used as the objective function in the optimization model. Zhou et al. [53], [54] derived an analytical solution to the optimal control problem with state and control constraints, which was implemented within a model predictive control framework. Wang et al. [55] developed a distributed consensus-based protocol with a feedback longitudinal controller for cooperative on-ramp merging, which was validated by agent-based simulations in the Unity3D environment. 

Compared to centralized control approaches, decentralized control is more suitable for implementing vehicle-level coordination, because each vehicle independently executes its own control law. However, one challenge is the potential for deadlocks in the solution due to limited local information. Thus, centralized and decentralized systems have their own advantages and disadvantages. 

Few hierarchical control frameworks were proposed to achieve efficient and safe merging of CAVs. The tactical layer is a centralized controller which uses a car-following model to generate the merging sequence [56]. The operational layer is a decentralized controller based on the model predictive control, which is used to optimize the desired CAV accelerations. A bi-level control strategy was proposed for maximizing traffic flow based on the first-order car-following model to determine the optimal merging order and equilibrium gaps for automated trucks [57]. The lower-level operational layer uses a third-order longitudinal dynamics model to compute the optimal truck accelerations. However, the existing hierarchical control framework does not integrate the control of traffic management and vehicle-level. 

To implement and validate cooperative merging control for CAVs, lateral control is essential. Several studies have focused on integrated longitudinal and lateral control for a single vehicle without considering the cooperation of vehicles [58], [59], [60]. In those cases, the problem was formulated as a trajectory planning and tracking problem considering only vehicle dynamics constraints. 

Therefore, a feasible coordination framework integrating the control of traffic management and vehicle-level to control the cooperative merging of CAVs remains a challenge. Furthermore, most strategies focus on longitudinal control of vehicles, with little to no emphasis on lateral control. To the best of the authors’ knowledge, an integrated cooperative longitudinal and 

lateral control method for merging CAVs at on-ramps has not been reported yet. Almost all of the aforementioned merging control methods have yet to be validated considering vehicle dynamics. 

The objective of this study was to develop a more practical merging coordination framework for CAVs (SAE Level 4 or 5). An integrated longitudinal and lateral cooperative control algorithm was developed and validated by near-real-world simulations. The main contributions of this paper are as follows: 

(1) A systematic and cooperative hierarchical coordination framework was proposed to integrate the control of traffic management and vehicle-level to control CAVs merging at on-ramps. 

(2) A decentralized unified lateral control algorithm was proposed to avoid lateral collision and track upper-level trajectories based on nonlinear model predictive control (NMPC). 

(3) Integration of a longitudinal optimal control algorithm and the proposed lateral control algorithm was validated by near-real-world vehicle simulation using CarSim/ Simulink. 

The remainder of this paper is organized as follows. In Section II, the hierarchical control framework for cooperative CAVs merging is introduced. Section III presents the upper-level longitudinal motion optimal planning. A decentralized unified control algorithm is proposed in Section IV to manage lateral merging. Section V presents results of CarSim/Simulink simulations. Finally, the results are discussed in Section VI and the main conclusions are outlined in Section VII. 

# II. MERGING PROBLEM FORMULATION AND HIERARCHICAL CONTROL FRAMEWORK

A hierarchical framework is developed to coordinate merging of CAVs, which consists of a traffic management level controller and vehicle level controller. Traffic management determines the merging sequence and merging state according to downstream traffic flow. Dynamic real-time planning and trajectory tracking of each vehicle rely on the merging sequence and merging state to ensure the state and time of arrival of the vehicle at the merging point. 

# A. Hierarchical Framework

In this paper, a merging roadway is defined as a single-lane main road and single-lane entry ramp, where all vehicles on the ramp need to merge onto the main road. It is assumed that the high-level centralized controller coordinates vehicles inside the control zone, as shown in Fig. 1. All vehicles can communicate with each other independently to gather information about the motion states of surrounding vehicles (V2V). A merging point is defined, where all vehicles are controlled to achieve the final merging state. The distance from the control zone entry to the merging point is $L$ . 

When a vehicle enters the control zone, the traffic management controller assigns the vehicle a unique identity i according to the FIFO (First-In-First-Out) merging sequence. The merging sequence inside the control zone is given by $Q _ { i } ( t ) \in \{ 1 , . . . , N \}$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/17ef1b90cb6ad0785bf593395b7751e1d2692de85ed8b4a785aeca4d3daca680.jpg)



Fig. 1. Hierarchical framework for merging control.


Definition 1: Once vehicle $i$ enters the control zone, it receives information set $I N _ { i } ( t )$ sent by traffic management level controller within a certain time period. 

$$
I N _ {i} (t) \triangleq \left\{Q _ {i} (t), p _ {i} \left(t _ {i} ^ {f}\right), v _ {i} \left(t _ {i} ^ {f}\right), a _ {i} \left(t _ {i} ^ {f}\right), t _ {i} ^ {f} \right\} \tag {1}
$$

where $p _ { i } \left( t _ { i } ^ { f } \right)$ $p _ { i } \left( t _ { i } ^ { f } \right) , \upsilon _ { i } \left( t _ { i } ^ { f } \right)$ and $a _ { i } \left( t _ { i } ^ { f } \right) .$ is the final state of the vehicle at the merging point, which is estimated by traffic management controller based on downstream information. Therefore, the following assumption is imposed: 

Assumption 1: Vehicles cruise after crossing the merging point. 

This implies that each vehicle will maintain a constant speed after crossing the merging point. The time $t _ { i } ^ { f }$ at which vehicle $i \in \mathcal { Q } ( t )$ arrives at the merging point is restricted by the imposed rear-end collision constraints. Under this assumption, the following condition is imposed to ensure safety constraints: 

$$
t _ {i} ^ {f} = \max  \left\{\min  \left\{t _ {i - 1} ^ {f} + \frac {S}{v _ {i - 1} \left(t _ {i - 1} ^ {f}\right)}, \frac {L}{v _ {\operatorname* {m i n}}} \right\}, \frac {L}{v _ {i} \left(t _ {i} ^ {0}\right)}, \frac {L}{v _ {\operatorname* {m a x}}} \right\} \tag {2}
$$

where $\upsilon _ { i - 1 } \left( t _ { i - 1 } ^ { f } \right)$ is the speed of the vehicle $i \mathrm { ~ - ~ } 1$ which arrives at the merging point at the time $t _ { i - 1 } ^ { f } ; t _ { i } ^ { 0 }$ is the time at which vehicle $i$ enters the control zone; $v _ { m i n }$ and $v _ { m a x }$ are the minimum and maximum speeds; and $S$ is the safe distance that should be maintained between preceding vehicle and following vehicle at the merging point. Considering those safety constraints, the appropriate time $t _ { i } ^ { f }$ has already been proved and calculated by Malikopoulos [49], [50] under the vehicle state constraints. The optimal final vehicle states have also been derived based on the optimal control. Here, the optimal control based method is used to establish a traffic management controller which sends the calculated optimal merging time and speed to the vehicle through V2I communication. This also ensures that the vehicle upper-level controller can use the optimal control to solve the optimal trajectory under vehicle state constraints. If each vehicle controls itself according to the current information set and maintains a safe distance at 

the merging point, the management control strategy can ensure longitudinal safety during merging operations. 

For vehicle level control, the trajectory of each vehicle is planned and tracked to ensure that the vehicle merges according to information set $I N _ { i } ( t )$ . Each vehicle is controlled independently and there is no negotiation between vehicles during the merging process. Both longitudinal and lateral dynamics of the vehicle must be considered to achieve a practical merging control model. However, decoupling longitudinal and lateral dynamics can reduce the complexity of the controller synthesis, which has been widely validated [58], [61]. Therefore, merging coordination can be decomposed into longitudinal control and lateral control. Two-level longitudinal control has been previously discussed and successfully implemented for CAVs under different scenarios [62]. 

For upper-level longitudinal control, the optimal motion trajectory from the current state to the final merging state within a specified merging time can be designed based on information set $I N _ { i } ( t )$ . The optimal speed profile is derived from the upper-level controller and used as input for the lowerlevel controller, which determines the throttle and braking required to obtain the desired speed. The lateral controller must decide on either the lane-keeping or merging process and is therefore extremely important for both main road and on-ramp vehicles inside the merging zone. 

Herein, a systematic and hierarchical coordination framework is provided for the integration of longitudinal and lateral cooperative merging control of CAVs at on-ramps and the proposed method is validated by near-real-world vehicle simulations. 

# III. VEHICLE UPPER-LEVEL CONTROL

# A. Longitudinal Upper-Level Controller

The upper-level longitudinal controller determines the optimal speed for each vehicle to reduce the fuel consumption and improve the passenger comfort. 

1) Longitudinal Control Vehicle Model: The kinematic bicycle model is the simplest vehicle dynamics model for capturing in-plane motion symmetry of the vehicle [61]. The upper-level controller is used to optimize the speed and acceleration of the vehicle as it reaches the merging point. Therefore, the bicycle model can be simplified as a moving point mass without considering the delays and noise in upper-level longitudinal control [34]. It is assumed that each vehicle is governed by a third order state equation: 

$$
\dot {x} _ {i} = v _ {i} (t)
$$

$$
\dot {v} _ {i} = a _ {i} (t)
$$

$$
\dot {a} _ {i} = u _ {i} (t) \tag {3}
$$

where $x _ { i } \in P _ { i }$ , $v _ { i } \in V _ { i }$ , $a _ { i } \in A _ { i }$ and $u _ { i } \in U _ { i }$ denote position, speed, acceleration /deceleration, and jerk (input), respectively. The set $P _ { i }$ , $V _ { i }$ , $A _ { i }$ and $U _ { i }$ is the complete bounded subset of $\mathbb { R }$ . To ensure that the vehicle state and input are within a reasonable range, the following constraints are defined: 

$$
\left. \begin{array}{l} A _ {i} = \left\{a _ {i} \mid a _ {\min } \leq a _ {i} (t) \leq a _ {\max } \right\} \\ V _ {i} = \left\{v _ {i} \mid v _ {\min } \leq v _ {i} (t) \leq v _ {\max } \right\} \\ U _ {i} = \left\{u _ {i} \mid u _ {\min } \leq u _ {i} (t) \leq u _ {\max } \right\} \end{array} \right\} \tag {4}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/3d2f537381c6641004e35bcbf29d114ce12b932ebfe2fb497a4420a3117019cd.jpg)



Fig. 2. Schematic illustration of longitudinal control.


where $a _ { m i n }$ and $a _ { m a x }$ are the minimum deceleration and maximum acceleration, respectively; $u _ { m i n }$ is the minimum control input; and $u _ { m a x }$ is the maximum control input. 

2) Longitudinal Control Problem Formulation: A joint cost function is defined to represent fuel consumption and comfort. The fuel consumption changes monotonically with respect to the acceleration [33]. Thus, it is necessary to minimize the acceleration in order to reduce the indirect fuel consumption. Moreover, minimizing jerk, which is the derivative of acceleration, improves passenger comfort [34]. The joint cost function can be expressed as 

$$
J _ {i} = \int_ {t _ {i} ^ {0}} ^ {t _ {i} ^ {f}} w _ {1} a _ {i} ^ {2} (t) + w _ {2} u _ {i} ^ {2} (t) d t \tag {5}
$$

where $w _ { 1 }$ and $w _ { 2 }$ are weighting factors, respectively. 

Upon entering the cooperative merging zone, each vehicle is assigned a merging time $t _ { i } ^ { f }$ and merging state $( x _ { i } ^ { f } , \upsilon _ { i } ^ { f } , a _ { i } ^ { f } )$ , which are together defined as information set $I N _ { i } ( t )$ . If each vehicle controls itself according to the information set, it will maintain a certain safe time headway at the merging point, as shown in Fig. 2. Thus, the longitudinal control problem is to guide the vehicle from its initial state to its merging state while minimizing the cost function from time $t _ { i } ^ { 0 }$ to time $t _ { i } ^ { f }$ . The decentralized problem for each vehicle i in upper-level controller is formulated as follows: 

$$
m i n \quad J _ {i}
$$

Subject to : (1), (2), (3) 

$$
x _ {i} (t _ {i} ^ {0}) = x _ {i} ^ {0}, v _ {i} (t _ {i} ^ {0}) = v _ {i} ^ {0}, a _ {i} (t _ {i} ^ {0}) = a _ {i} ^ {0},
$$

$$
\text {a n d g i v e n} t _ {i} ^ {0} \tag {6}
$$

The problem is formulated as an optimal control problem for finding the $u _ { i } ^ { * }$ that drives the vehicle state to the target state during time interval $[ t _ { i } ^ { 0 } , t _ { i } ^ { f } ]$ while minimizing the cost $J _ { i }$ under the state and input constraints. 

3) Solution Approach Based on Pontryagin’s Principle: The analytical solution of the optimal control problem considering the control constraints is derived based on Pontryagin’s maximum principle. The active state constraints problem is discussed in more detail in the literature [49], [50], [51], [52], [53], [54]. The Hamiltonian function for each vehicle i is defined as 

$$
H = \frac {1}{2} w _ {2} u _ {i} ^ {2} + \frac {1}{2} w _ {1} a _ {i} ^ {2} + \lambda_ {1} v _ {i} + \lambda_ {2} a _ {i} + \lambda_ {3} u _ {i} \tag {7}
$$

where $\lambda _ { 1 }$ and $\lambda _ { 2 }$ are co-state variables. According to Pontryagin’s maximum principle, if an optimal control input $u ^ { * } ( . )$ exists for the optimal problem, a costate function $\lambda ^ { * } ( . )$ 

necessarily exists and satisfies the following conditions: 

$$
\dot {x} _ {i} = H _ {\lambda_ {1}} = v _ {i} \tag {8}
$$

$$
\dot {v} _ {i} = H _ {\lambda_ {2}} = a _ {i} \tag {9}
$$

$$
\dot {a} _ {i} = H _ {\lambda_ {3}} = u _ {i} \tag {10}
$$

$$
\dot {\lambda} _ {1} = - H _ {x _ {i}} = 0 \tag {11}
$$

$$
\dot {\lambda} _ {2} = - H _ {v _ {i}} = - \lambda_ {1} \tag {12}
$$

$$
\dot {\lambda} _ {3} = - H _ {a _ {i}} = - w _ {1} a _ {i} - \lambda_ {2} \tag {13}
$$

$$
H _ {u} = w _ {2} u _ {i} + \lambda_ {3} = 0 \tag {14}
$$

Solving Eqs. (11)–(13), we obtain 

$$
\lambda_ {1} = C _ {1} \tag {15}
$$

$$
\lambda_ {2} = - C _ {1} t + C _ {2} \tag {16}
$$

$$
\dot {\lambda} _ {3} = - w _ {1} a _ {i} + C _ {1} t - C _ {2} \tag {17}
$$

where $C _ { 1 }$ and $C _ { 2 }$ are constants. As $u _ { m i n } \leq u _ { i } \leq u _ { m a x }$ , solving Eq. (13), for $- w _ { 2 } u _ { m a x } \le \lambda _ { 3 } \le - w _ { 2 } u _ { m i n }$ , we obtain 

$$
u _ {i} = - \frac {\lambda_ {3}}{w _ {2}} \tag {18}
$$

When $\lambda _ { 3 } > - w _ { 2 } u _ { m i n }$ , $H _ { u } > 0$ . Thus, Hamiltonian function H has a minimum value at u = umin. When λ3 < −w2umax, $u = u _ { m i n }$ $\lambda _ { 3 } < - w _ { 2 } u _ { m a x }$ $H _ { u } \ < 0$ . Thus, Hamiltonian function $H$ has a maximum value at $u = u _ { m a x }$ . 

When $- w _ { 2 } u _ { m a x } \ \leq \ \lambda _ { 3 } \ \leq \ - w _ { 2 } u _ { m i n }$ , after simultaneous derivation of both sides of Eq. (18) and combining Eq. (17), we obtain 

$$
w _ {2} \ddot {a} _ {i} = w _ {1} a _ {i} - C _ {1} t + C _ {2} \tag {19}
$$

Finally, solving the difference between Eqs. (8)–(10) and Eq. (19), gives 

$$
\begin{array}{l} x _ {i} (t) = C _ {3} \frac {w _ {2}}{w _ {1}} e ^ {\sqrt {\frac {w _ {1}}{w _ {2}}} t} + C _ {4} \frac {w _ {2}}{w _ {1}} e ^ {- \sqrt {\frac {w _ {1}}{w _ {2}}} t} + \frac {1}{6} \frac {C _ {1}}{w _ {1}} t ^ {3} \\ - \frac {1}{2} \frac {C _ {2}}{w _ {1}} t ^ {2} + C _ {5} t + C _ {6} \tag {20} \\ \end{array}
$$

$$
\begin{array}{l} v _ {i} (t) = C _ {3} \sqrt {\frac {w _ {2}}{w _ {1}}} e ^ {\sqrt {\frac {w _ {1}}{w _ {2}}} t} - C _ {4} \sqrt {\frac {w _ {2}}{w _ {1}}} e ^ {- \sqrt {\frac {w _ {1}}{w _ {2}}} t} \\ + \frac {1}{2} \frac {C _ {1}}{w _ {1}} t ^ {2} - \frac {C _ {1}}{w _ {1}} t + C _ {5} \tag {21} \\ \end{array}
$$

$$
a _ {i} (t) = C _ {3} e ^ {\sqrt {\frac {w _ {1}}{w _ {2}}} t} + C _ {4} e ^ {- \sqrt {\frac {w _ {1}}{w _ {2}}} t} + \frac {C _ {1}}{w _ {1}} t - \frac {C _ {2}}{w _ {1}} \tag {22}
$$

$$
u _ {i} (t) = C _ {3} \sqrt {\frac {w _ {1}}{w _ {2}}} e ^ {\sqrt {\frac {w _ {1}}{w _ {2}}} t} - C _ {4} \sqrt {\frac {w _ {1}}{w _ {2}}} e ^ {- \sqrt {\frac {w _ {1}}{w _ {2}}} t} + \frac {C _ {1}}{w _ {1}} \tag {23}
$$

Thus, the optimal control input is 

$$
u _ {i} ^ {*} (t) = \left\{ \begin{array}{l l} u _ {\max }, & \lambda_ {3} + w _ {2} u _ {\min } > 0 \\ C _ {3} \sqrt {\frac {w _ {1}}{w _ {2}}} e ^ {\sqrt {\frac {w _ {1}}{w _ {2}}} t} & \\ - C _ {4} \sqrt {\frac {w _ {1}}{w _ {2}}} e ^ {- \sqrt {\frac {w _ {1}}{w _ {2}}} t} + \frac {C _ {1}}{w _ {1}}, & \text {O t h e r s} \\ u _ {\min }, & \lambda_ {3} + w _ {2} u _ {\max } <   0 \end{array} \right. \tag {24}
$$

The optimal speed is 

$$
v _ {i} ^ {*} (t) = \left\{ \begin{array}{l l} v _ {i} ^ {t _ {a}} + u _ {\max } * t, & u _ {i} ^ {*} (t) = u _ {\max } \text {a n d} t > t _ {a} \\ C _ {3} \sqrt {\frac {w _ {2}}{w _ {1}}} e ^ {\sqrt {w _ {1}}} \sqrt {w _ {2}} t \\ - C _ {4} \sqrt {\frac {w _ {2}}{w _ {1}}} e ^ {- \sqrt {w _ {1}} t} \\ + \frac {1}{2} \frac {C _ {1}}{w _ {1}} t ^ {2} - \frac {C _ {1}}{w _ {1}} t + C _ {5}, & \text {o t h e r s} \\ v _ {i} ^ {t _ {a}} + u _ {\min } * t, & u _ {i} ^ {*} (t) = u _ {\min } \text {a n d} t > t _ {a} \end{array} \right. \tag {25}
$$

where $C _ { 3 }$ , $C _ { 4 }$ , $C _ { 5 }$ and $C _ { 6 }$ are constants computed using the initial and terminal merging states of each vehicle $i$ , $t _ { a }$ is the activation time of control constraint, and $\upsilon _ { i } ^ { ( t _ { a } ) }$ is the vehicle speed at $t _ { a }$ . The initial state values of each vehicle are collected at each time point. When the control constraint is not activated, six conditions can be formulated as six equations which are solved using Runge-Kutta methods to obtain the numerical solution of $C _ { 1 } - C _ { 6 }$ . 

When the control constraint is activated, it is set that $\lambda _ { 3 } \ + \ w _ { 2 } u _ { m } a x \ = \ 0$ or $\lambda _ { 3 } ~ + ~ w _ { 2 } u _ { m } i n ~ = ~ 0$ . Then, seven equations can be solved to obtain $C _ { 1 } { - } C _ { 6 }$ and $t _ { a }$ . After solving the equations, we obtain the optimal trajectory, speed and acceleration profile. The optimal speed is used as the reference speed input for the lower-level controller. 

B. Lateral Vehicle Trajectory Planning for On-Ramp Merging 

The lateral trajectory is a constant trajectory for vehicles on the main road and is only used to keep the vehicle in the lane. For merging vehicles, the longitudinal controller adjusts the speed while the lateral trajectory determines the vehicle’s direction of merging. The smooth and differentiable sigmoid function can be used to plan the trajectory of any two path points. Based on longitudinal optimal control state $x _ { i } ( t )$ , we use the sigmoid function to generate a lateral reference trajectory, expressed as 

$$
y _ {i} (t) = \frac {a}{1 + e ^ {(- (x _ {i} (t) - b) / c)}} + d \tag {26}
$$

where $a$ is the longitudinal proportional gain, which represents the maximum lateral deviation of the vehicle; $b$ and $c$ are the horizontal offset and steepness of the lateral trajectory from the center of the current lane to the center of the target lane, respectively; $d$ is the lateral offset. Different combinations of parameters will produce different shapes of trajectories. To ensure that the ramp vehicles merge onto the main road with continuous trajectory, different parameter combinations were tried according to the length and width of the ramp. The following set of parameters were chosen: $a = 4$ , $b = 1$ , $c = 2 0$ , and $d = - 4$ . 

The lateral trajectory must be chosen when lateral trajectory planning begins. The starting time of the lateral trajectory $t _ { i y s t a r t } ^ { 0 }$ will determine whether a lateral collision occurs, as shown in Fig. 3. A reasonable start time can effectively prevent lateral collision. Therefore, a decision-making strategy for selecting the start time was developed herein, presented as Algorithm 1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/6d80bf30461c68993d1e09f5700d8dc7e43b40cc12c4cc32ff9891e7b15e0153.jpg)



Fig. 3. Illustration of the impact of different start times on lateral trajectory planning.


# Algorithm 1 Decision Strategy for Selecting Start Time of Lateral Trajectory Planning

Initialization: $t _ { i y s t a r t } ^ { 0 } = t _ { i } ^ { f } - ( t _ { i + 1 } ^ { f } - t _ { i } ^ { f } )$ ; The initial value is set as the time when two vehicles maintain the setting safe time. 

Input: Longitudinal and lateral trajectory of vehicle i and following vehicle $i + 1$ in time period $[ t _ { i } ^ { 0 } t _ { i } ^ { f } ]$ : 

$$
\boldsymbol {x} _ {i + 1} (t), \boldsymbol {y} _ {i + 1} (t), \boldsymbol {x} _ {i} (t), \boldsymbol {y} _ {i} (t)
$$

Output: Lateral trajectory planning start time $t _ { i y s t a r t } ^ { 0 }$ while (1) do 

for $( t = t _ { i v s t a r t } ^ { 0 } ; t < t _ { i } ^ { f } )$ 

if $( x _ { i } ( t ) - x _ { i + 1 } ( t ) \leq \varepsilon )$ ; Determine whether there is an intersection between the longitudinal trajectories of the two vehicles; where $\varepsilon$ is the longitudinal minimum safe distance. then 

if $( y _ { i } ( t ) - y _ { i + 1 } ( t ) \leq d / 2 )$ where $d$ denotes the width of the lane, determine whether the lateral trajectories of two vehicles are in the same lane. 

# then

return $t _ { i y s t a r t } ^ { 0 } \gets t$ ; If two vehicles are in the same lane, the iteration stops and returns time t as the start time $t _ { i y s t a r t } ^ { 0 }$ . 

# end

return $t _ { i y s t a r t } ^ { 0 } \gets t$ ; If two vehicles are in the $t$ as the start time $t _ { i y s t a r t } ^ { 0 }$ . 

# end

$$
t \leftarrow t + 0. 1;
$$

if $( t _ { i } ^ { f } - t _ { i y s t a r t } ^ { 0 } ) \geq \tau$ where $\tau$ is the maximum required time value to complete the lane change. then 

return $t _ { i y s t a r t } ^ { 0 }$ ; If the time difference exceeds the value of $\tau$ , the current value is returned. 

# end

$t _ { i y s t a r t } ^ { 0 } = t _ { i y s t a r t } ^ { 0 } - 0 . 1$ ; Update the start time, and gradually reduce it. 

# end

If there is no intersection point between two vehicles in the longitudinal and lateral trajectories, t 0i ys t ar t $t _ { i y s t a r t } ^ { 0 }$ is appropriate and lateral collision is avoided. However, to ensure enough time to execute the lateral trajectory and avoid sudden changes in the lateral trajectory, an earlier start time is better as it represents a longer lateral trajectory. Algorithm 1 searches for the appropriate start time along the direction of decreasing value and judges whether the longitudinal and lateral trajectories of 

the two vehicles are within the safe threshold range. If they are not within the safe range, the algorithm stops, returns to the current time as the starting time and ends. 

It is important to note that the particle model used in the decision-making stage does not consider vehicle size and motion state. Lateral collision avoidance considering vehicle size and state is addressed in the tracking process. In the next section, the lower-level controller is presented, and a decentralized unified control method based on the driving safety field is proposed for trajectory tracking and real-time collision avoidance. 

# IV. VEHICLE LOWER-LEVEL CONTROL

# A. Lower-Level Longitudinal Control

The optimized speed profile obtained from the upper-level longitudinal controller is used as the target speed and input into the vehicle lower-level control. The lower-level controller involves non-linear pedals, throttle and tire force. The CarSim software has an integrated PID controller for the brake and throttle, which generates speed adjustments based on the error between the upper-level and lower-level, as follows: 

$$
u _ {\text {l o w e r - l e v e l}} (t) = K _ {p} e (t) + K _ {i} \int_ {0} ^ {t} e (t) d t + K _ {d} \frac {d e (t)}{d t}
$$

$$
\text {A n d} e (t) = v _ {\text {u p p e r - l e v e l}} ^ {*} (t) - v _ {\text {l o w e r - l e v e l}} (t) \tag {27}
$$

where optima $\upsilon _ { u p p e r - l e \upsilon e l } ^ { * } ( t )$ and and a $\upsilon _ { l o w e r - l e \upsilon e l } ( t )$ are the upper-levelthe vehicle, respectively; $K _ { p }$ , $K _ { i }$ , and $K _ { d }$ are the proportional, integral and derivative control parameters, respectively. The following set of parameters was chosen based on a manual tuning process during the simulation: $K _ { p } = 0 . 3$ , $K _ { i } = 0 . 1 5$ , and $K _ { d } = 0$ . Therefore, PI controller is used in the simulation. Some learning techniques, such as genetic algorithm or deep learning may be used in the future research to obtain more suitable weight values. 

1) Lower-Level Lateral Control: Targets of lateral control for merging vehicles and main road vehicles are selected to control the merging process and ensure lane-keeping. Although the decision-making method is designed to select a suitable start time of lateral trajectory planning in the upperlevel, lateral collisions can still occur during the merging process due to vehicle size and state. Therefore, lateral control is transformed into a unified control to integrate both vehicle tracking and collision avoidance. 

2) Vehicle Model: This section describes the vehicle models used for lateral control. Assuming a low sideslip rate and constant longitudinal speed at a constant sampling time, the bicycle model can be simplified as a single-track vehicle model [63], as shown in Fig. 4. Dynamics and relative motion of vehicle i can be described as 

$$
\dot {Y} _ {i} = \dot {x} _ {i} \sin \varphi_ {i} + \dot {y} _ {i} \cos \varphi_ {i} \tag {28a}
$$

$$
\dot {X} _ {i} = \dot {x} _ {i} \cos \varphi_ {i} - \dot {y} _ {i} \sin \varphi_ {i} \tag {28b}
$$

$$
m \ddot {y} _ {i} = - m \dot {x} _ {i} \dot {\varphi} _ {i} + 2 \left[ C _ {c f} \left(\delta_ {i} - \frac {\dot {y} _ {i} + l _ {r} \dot {\varphi} _ {i}}{\dot {x} _ {i}}\right) + C _ {c r} \frac {l _ {f} \dot {\varphi} _ {i} - \dot {y} _ {i}}{\dot {x} _ {i}} \right] \tag {28c}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/c3522477652b0ac0393919036ee50b1f76c4c8da401c39b5437816eada61ec99.jpg)



Fig. 4. Schematic illustration of vehicle dynamics model.



TABLE I SINGLE-TRACK VEHICLE MODEL PARAMETERS


<table><tr><td>Symbol</td><td>Description</td></tr><tr><td>m</td><td>Vehicle mass</td></tr><tr><td>Iz</td><td>Yaw moment of inertia about the axis</td></tr><tr><td>lf, lr</td><td>Distance from the CoG to the front/rear wheels</td></tr><tr><td>Clf, Clr</td><td>Linearized cornering stiffness of the front/rear wheels</td></tr><tr><td>Ccf, Ccr</td><td>Tire lateral stiffness of the front/rear wheels</td></tr><tr><td>sf, sr</td><td>Tire slip angles of the front/rear wheels</td></tr><tr><td>Xi, Yi</td><td>Global X/Y axis coordinate</td></tr><tr><td>xi, yi</td><td>Longitudinal/lateral speed at CoG in vehicle reference frame</td></tr><tr><td>φi</td><td>Yaw angle</td></tr><tr><td>φi</td><td>Yaw rate</td></tr><tr><td>δi</td><td>Angle of front wheel</td></tr></table>

$$
m \ddot {x} _ {i} = m \dot {y} _ {i} \dot {\varphi} _ {i} + 2 \left[ C _ {l f} s _ {f} + C _ {c f} \left(\delta_ {i} - \frac {\dot {y} _ {i} + l _ {r} \dot {\varphi} _ {i}}{\dot {x} _ {i}}\right) \delta_ {i} + C _ {l r} s _ {r} \right] \tag {28d}
$$

$$
\dot {\varphi} = \ddot {\varphi} \tag {28e}
$$

$$
I _ {z} \ddot {\varphi} _ {i} = 2 \left[ C _ {c f} \left(\delta_ {i} - \frac {\dot {y} _ {i} + l _ {r} \dot {\varphi} _ {i}}{\dot {x} _ {i}}\right) - l _ {f} C _ {c r} \frac {l _ {f} \dot {\varphi} _ {i} - \dot {y} _ {i}}{\dot {x} _ {i}} \right] \tag {28f}
$$

Model parameters are listed in Table I. For simplicity, the vehicle model is transformed into a discrete state-space equation. The state space vector $x _ { i }$ includes global X-axis coordinate $X _ { i }$ , global Y-axis coordinate $Y _ { i }$ , longitudinal speed $\dot { x } _ { i }$ , lateral speed $\dot { y } _ { i }$ , yaw angle $\varphi _ { i }$ , and yaw rate $\dot { \varphi } _ { i }$ . The front wheel $\delta _ { i }$ is the control input. The nonlinear vehicle model described in equations (28a)–(28f) can be converted into the following compact form: 

$$
\dot {\boldsymbol {x}} _ {i} (t) = f \left(\boldsymbol {x} _ {i} (t), \boldsymbol {u} _ {i} (t)\right) \tag {29}
$$

where $f ( \cdot , \cdot )$ is the state transition equation; $\begin{array} { r l } { x _ { i } ( t ) } & { { } = } \end{array}$ $[ Y _ { i } , X _ { i } , \dot { y } _ { i } , \dot { x } _ { i } , \varphi _ { i } , \dot { \varphi } _ { i } ] ^ { T } \ \in \ X _ { i }$ and ${ \pmb u } _ { i } ( t ) = \delta _ { i } \in { \pmb U } _ { i }$ are the state and input of vehicle i, respectively. Subsets $X _ { i }$ and $U _ { i }$ are totally bounded subsets of $\mathbb { R }$ . 

3) Collision Avoidance Based on Driving Safety Field Theory: This section focuses on vehicle safety description based on driving safety field theory. Although the safety headway is considered at the management level $I N _ { i } ( t )$ , realtime collision avoidance is required to ensure lateral safety. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/5eec5c875761d1a9730700ead6f03edeb11f09140c46fff4b4933778812d4efb.jpg)



Fig. 5. Cooperative merging vehicles and field strengths of corresponding safety fields ( $R _ { 1 } = R _ { i } = 1$ , $m _ { 1 } = m _ { i } = 1 7 2 3 \mathrm { ~ k g } .$ , $k _ { 1 } = 0 . 5$ , $k _ { 2 } = k _ { 4 } = 1$ , $k _ { 3 } = 4 5$ , $\gamma = 0 . 0 6 .$ ).


The driving safety field concept and model were proposed by Wang et al. [64], [65], which provide a mathematical method for virtual mass calculations and for comprehensively describing driving risk. 

The driving safety index integrates the safety potential energy $\left( S E ( t ) \right)$ and its rate of change $( \dot { S E } ( t ) )$ to describe the driving risk of a vehicle. The safety potential energy represents the spatial variability of driving risk and its rate of change expresses temporal variability. Strength of the kinetic field $E _ { \upsilon , i 1 } ( t )$ of vehicle 1 can be expressed as 

$$
\boldsymbol {E} _ {V, i 1} (t) = \frac {k _ {1} R _ {i} m _ {i} k _ {3}}{\left(k _ {3} - \left| \boldsymbol {v} _ {i} (t) \right| \cos \alpha_ {i} (t)\right) \cdot \left| \boldsymbol {r} _ {i 1} (t) \right| ^ {k _ {2}}} \tag {30}
$$

where $m _ { i }$ is the virtual mass of vehicle i ; $R _ { i }$ is the influencing factor associated with the road condition at the location of vehicle i; $r _ { i 1 }$ is the distance vector between vehicle 1 and vehicle i; $\alpha _ { i }$ is the angle between the direction of ${ \boldsymbol { v } } _ { i }$ and $r _ { i 1 }$ ; $k _ { 1 }$ and $k _ { 2 }$ are undetermined constants; and $k _ { 3 }$ is the speed of the wave. Field strengths of cooperative merging vehicles and their driving safety fields are shown in Fig. 5. 

Only vehicle-vehicle impact is considered here, while the road condition and other factors are ignored. Thus, the driving safety index of vehicle 1 at time t can be simplified as 

$$
\left\{ \begin{array}{l} S E _ {V, i 1} (t) = \frac {k _ {1} R _ {i} R _ {1} m _ {i} m _ {1} k _ {3}}{\left(k _ {2} - 1\right) \left| \boldsymbol {r} _ {2 1} (t) \right| ^ {k _ {2} - 1}} \\ \cdot \left[ \frac {\left(k _ {3} - \left| \boldsymbol {v} _ {i} (t) \right| \cos \alpha_ {i}\right) ^ {1 - k _ {2}}}{k _ {3} - \left| \boldsymbol {v} _ {i} (t) \right| ^ {\frac {1}{k _ {2}}}} \right] ^ {\frac {1}{1}} \\ H _ {i} (t) = \min  \left\{\left(\frac {L _ {w}}{2 D _ {i} (t)}\right) ^ {k _ {4}}, 1 \right\} \\ S E _ {1} (t) = \sum_ {i = 2} ^ {N} \left(H _ {i} \cdot S E _ {V, i 1} (t)\right) \\ S \dot {E} _ {i 1} (t) = M _ {1} R _ {1} E _ {V, i 1} \cdot (\boldsymbol {v} _ {i} (t) - \boldsymbol {v} _ {1} (t)) \\ S \dot {E} _ {1} (t) = \sum_ {i = 2} ^ {N} \left(H _ {i} \cdot S \dot {E} _ {i 1} (t)\right) \\ D S I _ {1} (t) = \gamma \cdot S E _ {1} (t) + (1 - \gamma) \cdot S \dot {E} _ {1} (t) \end{array} \right. \tag {31}
$$

where $D S I _ { 1 } ( t )$ is the driving safety index of vehicle 1; $H _ { i } ( t )$ is the weighting factor of vehicle i ; $D _ { i } ( t )$ is the distance 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/4488aefb814f0c1be727c6a4fc4aff6358ec357cc7b3ac26c5fd982edbb7d40a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/9fb6a41a4e360d47f5c3552451d006380da02feb8d77ad96f0a79336063c2704.jpg)



Fig. 6. Interactive 3D simulation scenarios in CarSim and Simulink simulation.


between the center of mass vehicle i and the center line of the right lane; $L _ { W }$ is the lane width; and $k _ { 4 }$ is an undetermined constant. γ is the weight. The following set of parameters was selected based on field tests [65]: $R _ { 1 } = R _ { i } = 1$ , $m _ { 1 } = m _ { i } =$ $1 7 2 3 k g$ , $L _ { W } = 4 m$ , $k _ { 1 } { = } 0 . 5$ , $k _ { 2 } = k _ { 4 } = 1$ , $k _ { 3 } ~ = ~ 4 5$ , and $\gamma = 0 . 0 6$ . 

4) Decentralized Nonlinear Model Predictive Control: In this section, the proposed decentralized trajectory tracking method for lateral control in cooperative merging is introduced. Trajectory tracking is formulated as a unified control problem based on NMPC with multi-constraints derived from vehicle dynamics and kinematics. 

# (1) Prediction of state and output variables

An important step in the design of a nonlinear model predictive control for trajectory tracking is predicting the future state of the vehicle at each time step, which determines the control inputs within a specified prediction horizon. To obtain a discrete state-space equation, the system dynamics expressed by Eq. (29) are discretized with fixed sampling time $T$ , as follows: 

$$
\dot {\boldsymbol {x}} _ {i} (k + 1) = f \left(\boldsymbol {x} _ {i} (k), \boldsymbol {u} _ {i} (k)\right) \tag {32}
$$

$$
\boldsymbol {u} _ {i} (k) = \boldsymbol {u} _ {i} (k - 1) + \Delta \boldsymbol {u} _ {i} (k) \tag {33}
$$

where $\begin{array} { l l l l } { x _ { i } ( k ) } & { = } & { [ Y _ { i } ( k ) , X _ { i } ( k ) , \dot { y } _ { i } ( k ) , \dot { x } _ { i } ( k ) , \varphi _ { i } ( k ) , \dot { \varphi } _ { i } ( k ) ] ^ { T } } \end{array}$ ${ \pmb u } _ { i } ( k ) = \delta _ { i } ( k )$ ; $\Delta { { u } _ { i } } ( k )$ denotes the optimal input at time $k$ and $k$ is the current sampling time. 

Assuming that the prediction horizon is $N _ { p }$ and the control horizon is $N _ { c }$ , the future state variables $x _ { i } ( k )$ can be predicted for $N _ { p }$ steps ahead, as follows: 

$$
\boldsymbol {x} _ {i} (k + 1), \dots , \boldsymbol {x} _ {i} (k + m), \dots , \boldsymbol {x} _ {i} (k + N _ {p}) \tag {34}
$$

where $x _ { i } ( k + m )$ is the predicted state variable at $k + m$ . Let $U _ { i } ( k )$ denote the input computed at time $k$ , that is 

$$
\boldsymbol {U} _ {i} (k) = \left[ \Delta \boldsymbol {u} _ {i} (k), \dots , \Delta \boldsymbol {u} _ {i} (k + m), \dots , \Delta \boldsymbol {u} _ {i} (k + N _ {c} - 1) \right] ^ {T} \tag {35}
$$

Using the current state variable and input, state variables of the vehicle can be iteratively calculated as follows: 

$$
\boldsymbol {x} _ {i} (k + 1) = \boldsymbol {x} _ {i} (k) + f \left(\boldsymbol {x} _ {i} (k), \boldsymbol {u} _ {i} (k)\right) * T \tag {36}
$$

$$
\begin{array}{l} \boldsymbol {x} _ {i} (k + N _ {c}) = \boldsymbol {x} _ {i} (k + N _ {c} - 1) \\ + f \left(\boldsymbol {x} _ {i} (k + N _ {c} - 1), \boldsymbol {u} _ {i} (k + N _ {c} - 1)\right) * T \tag {37} \\ \end{array}
$$

$$
\begin{array}{l} \boldsymbol {x} _ {i} (k + N _ {p}) = \boldsymbol {x} _ {i} (k + N _ {p} - 1) \\ + f \left(\boldsymbol {x} _ {i} (k + N _ {p} - 1), \boldsymbol {u} _ {i} (k + N _ {c} - 1)\right) * T \tag {38} \\ \end{array}
$$

When the controller action is beyond the control horizon, the last controller action ${ \pmb u } _ { i } ( k + N _ { c } - 1 )$ is used as the control action to predict the state variables. 

# (2) Cost function

To bring the vehicle state as close as possible to the reference trajectory while avoiding collision, a cost function is formulated to represent both tracking capability and safety. The driving safety field incorporates both the spatial and the temporal driving risk of the vehicle. Therefore, it must be minimized to improve safety within the control horizon. The finite horizon cost function of vehicle i can be expressed as 

$$
\begin{array}{l} J _ {i} (k) = \sum_ {t = 1} ^ {t + N _ {p} - 1} \| Y _ {i} (k + t | t) - Y _ {r} (k + t) \| _ {Q _ {i}} ^ {2} \\ + \sum_ {t = 0} ^ {t + N _ {c}} \| \Delta \boldsymbol {u} _ {i} (t + k | t) \| _ {R _ {i}} ^ {2} \\ + \sum_ {t = 0} ^ {t + N _ {c}} \| D S I _ {i} (t + k \mid t) \| _ {S _ {i}} ^ {2} \tag {39} \\ \end{array}
$$

where $Q _ { i }$ , Ri , and $S _ { i }$ are weighting factors; $Y _ { r } ( k )$ is the set-point of the reference trajectory for vehicle tracking; and $D S I _ { i } ( t + k | t )$ is the driving safety index of vehicle i at time $k$ . 

# (3) Constraint analysis for NMPC

According to the kinematics and dynamics of the vehicle model, the following dynamic integrity constraints can be defined to ensure that the vehicle state and control input are within a reasonable range. 

$$
\delta_ {\min } (k) \leq u _ {i} (k) \leq \delta_ {\max } (k)
$$

$$
\Delta \delta_ {\min } (k) \leq \Delta u _ {\delta i} (k) \leq \Delta \delta_ {\max } (k) \tag {40}
$$

where $\Delta \delta ( k )$ is the rate of change of the steering wheel angle. These two constraints together guarantee the passenger’s comfort and avoid lateral skidding. 

# (4) Decentralized nonlinear model predictive control

The goal of vehicle $i$ is to track its own reference trajectory and avoid collision inside the control zone. The rolling cooperative lateral control problem for merging at step $k$ can be expressed as 

$$
\begin{array}{c c} \text {m i n} & J _ {i} (k) \end{array}
$$

$$
\text {S u b j e c t} (3 0) (3 1) (3 9), \boldsymbol {x} _ {i} (1) = \boldsymbol {x} _ {i} ^ {0} \tag {41}
$$

To calculate cost function $J _ { i } ( k )$ and solve the control problem, motion information about surrounding vehicles is required, thus making it a coupled problem. Since the traffic management level controller decides on the merging consequence, there is no negotiation between vehicles during the control process at each step. Therefore, a decentralized NMPC (DNMPC) is developed to solve the coupled problem. 

At each sampling time $k$ , the proposed decentralized control scheme is implemented as follows: 

# Algorithm 2 Decentralized Lateral Control of Vehicle Merging Based on Model Predictive Control

Input: Current state of each vehicle: $x _ { i } ( k )$ , $i = 1 , 2 , 3 , \dotsc , N$ . 

Output: Optimal control input for each vehicle: ${ \pmb u } _ { i } ( k )$ , $i = 1 , 2 , 3 , \dotsc , N$ . 

# do

Step 1 At step $k$ , the current state $x _ { i } ( k )$ of each vehicle $i = 1 , 2 , 3 , \dotsc , N$ , is measured and the vehicle state within $N _ { p }$ horizon is predicted using Eqs. (35) - (37). 

Step 2 Each vehicle sends its current state $x _ { i } ( k )$ to the surrounding vehicles. 

Step 3 Each vehicle receives information about the state of the surrounding vehicles and solves the local receding-horizon control problem to obtain $U _ { i } ^ { * } ( k )$ . The first element of optimal control sequence $u _ { i } ( k ) = u _ { i } ( k - 1 ) + \Delta u _ { i } ^ { * } ( k )$ is used as the input for each vehicle lateral controller. 

Step 4 Roll the control horizon to update $t = ( k + 1 ) * T$ and return to Step (1). 

# while;

The interior point method (the “fmincon” function using “active-set” algorithm in the MATLAB) is used to solve the nonlinear optimal problem. The computation time suggests that the method can efficiently solve non-linear equations in real-time. The simulation is presented in the next section. 


TABLE II CARSIM VEHICLE MODEL PARAMETERS


<table><tr><td>Symbol</td><td>Value (units)</td></tr><tr><td>m</td><td>1723( kg)</td></tr><tr><td>l f, l r</td><td>1.23( m), 1.46( m)</td></tr><tr><td>I z</td><td>4192( kg·m2)</td></tr><tr><td>s f, s r</td><td>0.2(deg), 0.2(deg)</td></tr><tr><td>C c f, C c r</td><td>66900( N/rad), 62700( N/rad)</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/b3dc1a55fdc0b9e0c1f6dfb676a2451b2a262537dfb047f53e831867ff8fe5e8.jpg)



(a) Speed profiles


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/474f8fe3eb6436734c228735b81216bda116189661a74ea766ea8ab08b5e3e3c.jpg)



(b) Longitudinal acceleration profiles



Fig. 7. Results of longitudinal upper-level control simulated in Matlab.


# V. SIMULATION EXPERIMENTS

To verify the proposed cooperative hierarchical framework and integrated longitudinal and lateral decentralized control method, two typical vehicle merging cases were simulated in CarSim/Matlab/Simulink on a Lenovo computer (RAM: 4GB, processor: Intel Core i7-3700, Operating frequency: $3 . 4 0 \mathrm { G H z }$ ). CarSim is a simulation software specially designed for vehicle dynamics, which makes the experiment close to real life scenarios. 

The upper-level longitudinal controller was used to optimize the speed profile, which was set as the target speed and input into the lower-level control. The selection of weight values for cost function of upper-level longitudinal controller is discussed in Jing et al. [37]. Here, it is assumed that $w _ { 1 } = w _ { 2 } = 1$ . 

The DNMPC was built in Matlab/Simulink and used to control vehicles in CarSim using a closed-loop merging maneuver. The vehicle execution delay was also considered, represented in Simulink by the transfer delay function $1 / z$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/6b014b62636bc9843b68db65c1df22acf2ee31483cd4461c6e57ff71f313db11.jpg)



(a) Position trajectory


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/0a7cf219c38207696168ce343f363593eb63022c5bba893553ded2e1b8a17b2f.jpg)



(b） Speed profiles


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/959de79ae1acc95b4f3b8ba7a48038cc66930f12653083e613628d0c9adddedb.jpg)



(c)Longitudinal acceleration profiles


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/42cb13f510758753a933545ea1af8d65abab7eab8bf9b1946f523a562f053f62.jpg)



(d) Yaw angle profiles


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/8e148d01194ac7108b0b72ee1030f57350642f28a491babd01b142c375cf5f13.jpg)



(e) Lateral acceleration profiles



Fig. 8. CarSim/Simulink co-simulation results for case study 1.



TABLE III DECENTRALIZED NONLINEAR MODEL PREDICTIVE CONTROLLER PARAMETERS


<table><tr><td>Symbol</td><td>Value (units)</td></tr><tr><td>Np, Nc</td><td>20,2</td></tr><tr><td>Q1, R1, S1</td><td>200, 100, 0</td></tr><tr><td>Q2, R2, S2</td><td>1000, 100, 0.001</td></tr><tr><td>Q3, R3, S3</td><td>200, 100, 0.001</td></tr><tr><td>(δmin, δmax)</td><td>[-10, 10]</td></tr><tr><td>(Δδmin, Δδmax)</td><td>[-0.85, 0.85]</td></tr></table>

The high-fidelity “E-class, Sedan” vehicle model was selected in CarSim and the relevant parameters are listed in Table II. Sample time $T$ was 0.02s. Parameters of the DNMPC are presented in Table III. 

# A. Merging Case Study 1: Coordination of Three Vehicles With Different Driving States

In this case, three vehicles move along two merging roads with a random entry time. The interactive 3D environment of CarSim/Simulink and simulation scenarios are shown in Fig. 6. Length of the cooperative control zone $\mathrm { L } = 1 5 0 \mathrm { m }$ and longitudinal safe distance $S = 2 5 \mathrm { ~ m ~ }$ . The maximum speed limit is $1 2 0 ~ \mathrm { k m / h }$ and longitudinal acceleration ranges from $- 2 ~ \mathrm { m } / \mathrm { s } ^ { 2 }$ to $2 ~ \mathrm { m } / \mathrm { s } ^ { 2 }$ . Vehicle 1 and vehicle 3 move along the main road and vehicle 2 moves on the secondary road. 

Vehicle 1, designated as the leading vehicle of the platoon, enters the control zone at 0.5 s and at a speed of $9 0 ~ \mathrm { k m / h }$ . Vehicle 2 enters the control zone at 0.5 s on the secondary road at a speed of $6 0 ~ \mathrm { k m / h }$ and vehicle 3 enters the control zone at 2 s on the main road at a speed of $7 2 ~ \mathrm { k m / h }$ . Results of the longitudinal upper-level control simulated in Matlab are 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/d811dcc8a2e7a50bec920bbaac60a01ebfca5244f4601101f9294031e171235c.jpg)



Fig. 9. Decentralized nonlinear model predictive controller (DNMPC) tracking error of the merging vehicle.


shown in Fig. 7. Position, speed, acceleration and yaw angle profiles generated in CarSim/Simulink are shown in Fig. 8. 

Vehicle trajectories do not intersect in time and space, as shown in Fig. 8(a), which indicates that merging is performed safely. Comparing Fig. 7(a) and Fig. 7(b), it is evident that the speed profiles are similar at different control levels, thereby illustrating the ability of the lower-level PI controller to track longitudinal speed. Speed profiles of each vehicle are smooth, indicating that there is no stop-and-go driving. 

The DNMPC tracking error of the merging vehicle at the on-ramp is illustrated in Fig. 9. As the merging vehicle approaches the main road vehicle, the influence of the safety field increases. The tracking error fluctuates slightly 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/382edbb561ab0d8f1cb4791c4abdf47932aa4a58995eeb3a57c2ba565f966ba1.jpg)



Fig. 10. Computation time for each control cycle.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/44c157af71364926790e8f05f7149e4055b05dd9f5d9408445f66966e40a3563.jpg)



Fig. 11. Cumulative fuel consumption of vehicles.


$( 2 s \mathrm { ~  ~ { ~  ~ } ~ } t \mathrm { ~  ~ { ~ \textc ~ } ~ } 6 s $ ), but eventually approaches 0, suggesting stable and reliable tracking. Moreover, yaw and lateral profiles are smooth, further demonstrating good performance of the proposed DNMPC. 

The proposed DNMPC requires solving nonlinear optimization problems, which can be time consuming. To verify computational efficiency of the DNMPC, computation time was calculated for each control cycle of each vehicle, as shown in Fig. 10. For each vehicle, the computation time is less than 0.02 s in a control cycle, suggesting that the proposed system can be implemented in real-time. 

Fuel consumption (in kg) of vehicles was also calculated over the same time period in CarSim. Here, a baseline value was used to estimate fuel consumption benefits of the proposed method. In the baseline scenario, vehicles on the main road accelerate to $9 0 \ \mathrm { k m / h }$ and vehicles on the ramp slow down to wait for vehicles on main road to cross before accelerating at $2 ~ \mathrm { m } / \mathrm { s } ^ { 2 }$ and merging onto the main road. Fuel consumption results are shown in Fig. 11 Compared to baseline, the proposed method reduces overall fuel consumption by $2 1 . 9 \%$ . 

# B. Merging Case Study 2: Coordination of Six Vehicles in Different Driving States

The CarSim version used here can support up to six vehicles in one combined simulation. In this case, six vehicles move 


TABLE IV INITIAL VEHICLE PARAMETERS


<table><tr><td>ID</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Headway (s)</td><td>0</td><td>0</td><td>0.8</td><td>0.9</td><td>1.3</td><td>1.2</td></tr><tr><td>Speed (km/h)</td><td>72</td><td>50</td><td>70</td><td>45</td><td>63</td><td>72</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/d92e1c4f86671edb1f7a75ba22f4fd86311509900d19fb4f3eb8cba7cb98cc50.jpg)



(a) Speed profiles


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/3342eba58b1260dfe787a9e865e3d8b750bfd3f4026d527f21bc55616333ceb2.jpg)



(b) Longitudinal acceleration profiles



Fig. 12. Longitudinal upper-level control simulated in Matlab.


along two merging roads with a random entry time. Length of the cooperative control zone $\mathrm { L } = 1 2 0 \mathrm { ~ m ~ }$ and longitudinal safe distance $S = 2 0 \mathrm { ~ m ~ }$ . Again, the maximum speed limit is $1 2 0 \ \mathrm { k m / h }$ and the longitudinal acceleration ranges from $- 2 \ m / \mathrm { s } ^ { 2 }$ to $2 \ m / \mathrm { s } ^ { 2 }$ . Vehicles 1, 3, 5 and 6 travel on the main road, while vehicles 2 and 4 merge from the ramp onto the main road. 

Initial headway times between vehicles are presented in Table IV. Results of the longitudinal upper-level control simulation in Matlab are presented in Fig. 12. The CarSim/Simulink results are shown in Fig. 13. Lateral acceleration profiles exhibit a few oscillations when the vehicles start moving due to the selected vehicle startup mode in CarSim. Upon entering the control zone, lateral acceleration profiles are smooth. The time required to solve the nonlinear optimization problems of each vehicle in each control horizon is shown in Fig. 15. The results indicate that the proposed DNMPC can safely and efficiently control cooperative merging of each vehicle in the lateral direction. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/8d91d6fa7d725fb498e0abeadb7a94fa65ee5bb957e09ef8261044ea5f9e0620.jpg)



(a) Position trajectory


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/013e34a70b1d0d7b89280b72abe011792f4104361f23663a4efdeb54284be1d1.jpg)



(b) Speed profiles


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/a563089200fa076b3b58cc15ecaafb8b3b416f68583ff19e263c8150ce7c55b6.jpg)



(c)Longitudinal acceleration profiles


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/84ec07b11caf24174227f4b28239ff4fddc0c6eb9dec9266daaf47b711a48496.jpg)



(d) Yaw angle profiles


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/3008dda24577dc8b56888bf08b4162c723d6d2d5c315c195e37296115333baae.jpg)



(e) Lateral acceleration profiles



Fig. 13. CarSim/Simulink co-simulation results for case study 2.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/391c440fa9004689116465487d30938c42d30b510c45722f84ec247f4a41af22.jpg)



Fig. 14. Decentralized nonlinear model predictive controller (DNMPC) tracking error of two merging vehicles.


In this case study, for the baseline scenario, vehicles on the main road accelerate to $7 2 ~ \mathrm { k m / h }$ , and the other conditions are the same as those used in case study 1. The fuel consumption is shown in Fig. 16. Compared to the baseline, the proposed method reduces overall fuel consumption by $3 . 9 \%$ . 

Based on the two case studies, improved fuel consumption is related to the vehicle state when entering and exiting the control zone. The results also verify that smooth speeds can reduce the fuel consumption. 

The CarSim/Simulink results demonstrate that the proposed decentralized framework and integrated control method for cooperative merging vehicles are safe, effective and may also benefit the environment. It is important to note that 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/223284b4848d5b5724856a24dce391ef0e8422d1b5f8d0f966242469299d715b.jpg)



Fig. 15. Computation time for each control cycle.


the proposed method is not restricted to particular ranges of speeds, merging zone lengths, and vehicle headways. Different parameters should not affect the conclusions of this paper. In fact, the optimal control based upper-level coordination using the acceleration as the cost function has already been successfully tested under various traffic conditions [49], [50], [51], [52], [53], [54], [66]. Here, the optimal control based upper-level approach was further verified by near-real-world vehicle simulations. 

# VI. DISCUSSION

Systematic simulation experiments were carried out to verify integrated execution of the upper and lower vehicle coordination algorithms for cooperative merging of CAVs 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/59fcc1cea484822de4628f40a58c7a595604569a8131d5a6a661104ee0b810e3.jpg)



Fig. 16. Cumulative fuel consumption of vehicles.


at on-ramps. Acceleration outputs of CarSim represent the actual acceleration of the vehicle. Comparing the longitudinal acceleration profiles of the upper and lower levels, as shown in Fig. 7(b), Fig. 12(b), Fig. 8(c) and Fig. 13(c), it can be found that the acceleration profiles are clearly different. 

If the acceleration obtained by the upper-level controller is not used as tracking input for the lower-level controller, the vehicle acceleration is, controlled by the lower-level controller instead. Due to the limitations of the CarSim software, acceleration and speed were not simultaneously used as inputs of the lower-level. Similarly, single inputs were previously used for the upper-level speed in real vehicle experiments [62]. The vehicle chassis is nonlinear and complex. Thus, developing an efficient controller for multi-input tracking remains a challenge. 

Acceleration and jerk can be used to represent passenger comfort within a certain range [34]. By comparing longitudinal acceleration profiles of two layers, it can be further concluded that the upper-level controller cannot predict the level of passenger comfort which is decided by the lower-level controller. Therefore, in order to improve passenger comfort, the lower-level controller must be able to track the optimal acceleration of the upper-level controller. Since the lower-level controller is involved in mechanical and nonlinear control, it remains uncertain whether it can track the acceleration and jerk derived from upper-level controller and will require further verification. 

# VII. CONCLUSION

In this paper, the problem of longitudinal and lateral integration of merging control was addressed and the practical implication for CAVs merging at on-ramps was verified. First, a systematic and hierarchical cooperative coordination framework was developed to control CAVs merging. Then, an optimal control based vehicle upper-level longitudinal control algorithm was presented for optimizing fuel consumption and passenger comfort under hard control constraints. The S-function was used to generate a lateral reference trajectory. Subsequently, a decentralized lateral coordination algorithm for vehicle lower-level control was proposed to avoid lateral collision and to track upper-level trajectory. Finally, the proposed decentralized framework and integrated control method 

were validated by simulating near real-world vehicle scenarios in CarSim/Simulink. Compared to baseline, the proposed integrated merging control system can effectively improve traffic efficiency and reduce fuel consumption, which shows potential for practical applications. Simulation results further verified the ability of the optimal upper-level controller to improve fuel consumption by optimizing speed. Furthermore, the validated method provides additional support for other upper-level cooperative control methods using the simple vehicle model. 

This paper focused on the control method and validation for SAE Level 4 or 5 automation. This framework does not consider the influence of uncertainties such as unreliable communication and information interference. Further studies are needed to improve the ability of the algorithm to deal with uncertainty such as communication delay and disturbance [67], [68] Future research should investigate the impact of cooperative CAVs control at on-ramps on traffic flow to better understand the variety of traffic flow within merging sections. CAVs will certainly coexist with manually driven vehicles for a long time to come. A few studies have focused on merging coordination [69], [70] and lane changing [71], [72] in mixed traffic. More research is needed on cooperative merging control at on-ramps under mixed traffic conditions and assessments of merging efficiency under different penetration rates. 

# REFERENCES



[1] L. C. Davis, “Effect of cooperative merging on the synchronous flow phase of traffic,” Phys. A, Stat. Mech. Appl., vol. 361, no. 2, pp. 606–618 Mar. 2006. 





[2] R. Liu, “Merge: The current practice in the UK and towards establishing general principles,” in Proc. Social Behav. Sci., vol. 16, pp. 184–195, Jan. 2011. 





[3] F. Marczak, W. Daamen, and C. Buisson, “Merging behaviour: Empirical comparison between two sites and new theory development,” Transp. Res. C, Emerg. Technol., vol. 36, pp. 530–546, Nov. 2013. 





[4] J. Sun, J. Ouyang, and J. Yang, “Modeling and analysis of merging behavior at expressway on-ramp bottlenecks,” Transp. Res. Rec., J. Transp. Res. Board, vol. 2421, no. 1, pp. 74–81, Jan. 2014. 





[5] Y. Chung and W. W. Recker, “Spatiotemporal analysis of traffic congestion caused by rubbernecking at freeway accidents,” IEEE Trans. Intell. Transp. Syst., vol. 14, no. 3, pp. 1416–1422, Sep. 2013. 





[6] G. R. Iordanidou, C. Roncoli, and I. P. M. Papamichail, “Feedback-based mainstream traffic flow control for multiple bottlenecks on motorways,” IEEE Trans. Intell. Transp. Syst., vol. 16, no. 2, pp. 610–621, Feb. 2015. 





[7] X. Li, J. Cui, S. An, and M. Parsafard, “Stop-and-go traffic analysis: Theoretical properties, environmental impacts and oscillation mitigation,” Transp. Res. B, Methodol., vol. 70, pp. 319–339, Dec. 2014. 





[8] H. Li, J. Zhang, Z. Zhang, and Z. Huang, “Active lane management for intelligent connected vehicles in weaving areas of urban expressway,” J. Intell. Connected Vehicles, vol. 4, no. 2, pp. 52–67, Sep. 2021. 





[9] M. Wang, W. Daamen, S. P. Hoogendoorn, and B. Van Arem, “Rolling horizon control framework for driver assistance systems. Part II: Cooperative sensing and cooperative control,” Transp. Res. C, Emerg. Technol., vol. 40, pp. 290–311, Mar. 2014. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S0968090X13002611 





[10] Y. Guo, C. Xiong, J. Ma, and X. Li, “Joint optimization of vehicle trajectories and intersection controllers with connected automated vehicles: Combined dynamic programming and shooting heuristic approach,” Transp. Res. C, Emerg. Technol., vol. 98, pp. 54–72, Jan. 2019. 





[11] X. Zhao, S. Jing, F. Hui, R. Liu, and A. J. Khattak, “DSRC-based rear-end collision warning system—An error-component safety distance model and field test,” Transp. Res. C, Emerg. Technol., vol. 107, pp. 92–104, Oct. 2019. 





[12] Z. Xu et al., “Trajectory optimization for a connected automated traffic stream: Comparison between an exact model and fast heuristics,” IEEE Trans. Intell. Transp. Syst., vol. 22, no. 5, pp. 2969–2978, May 2021. 





[13] S. Jing, X. Zhao, F. Hui, A. J. Khattak, and L. Yang, “Cooperative CAVs optimal trajectory planning for collision avoidance and merging in the weaving section,” Transportmetrica B, Transp. Dyn., vol. 9, no. 1, pp. 219–236, Jan. 2021. 





[14] L. Chen and C. Englund, “Cooperative intersection management: A survey,” IEEE Trans. Intell. Transp. Syst., vol. 17, no. 2, pp. 570–586, Feb. 2016. 





[15] C. Katrakazas, M. Quddus, W.-H. Chen, and L. Deka, “Real-time motion planning methods for autonomous on-road driving: State-of-the-art and future research directions,” Transp. Res. C, Emerg. Technol., vol. 60, pp. 416–442, Nov. 2015. 





[16] D. Bevly et al., “Lane change and merge maneuvers for connected and automated vehicles: A survey,” IEEE Trans. Intell. Vehicles, vol. 1, no. 1, pp. 105–120, Mar. 2016. 





[17] B. Paden, M. Cáp, S. Z. Yong, D. Yershov, and E. Frazzoli, “A survey of ˇ motion planning and control techniques for self-driving urban vehicles,” IEEE Trans. Intell. Vehicles, vol. 1, no. 1, pp. 33–55, Jun. 2016. 





[18] Z. Wang, Y. Bian, S. E. Shladover, G. Wu, S. E. Li, and M. J. Barth, “A survey on cooperative longitudinal motion control of multiple connected and automated vehicles,” IEEE Intell. Transp. Syst. Mag., vol. 12, no. 1, pp. 4–24, Dec. 2020. 





[19] J. Rios-Torres and A. A. Malikopoulos, “A survey on the coordination of connected and automated vehicles at intersections and merging at highway on-ramps,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 5, pp. 1066–1077, May 2017. 





[20] M. Athans, “A unified approach to the vehicle-merging problem,” Transp. Res., vol. 3, no. 1, pp. 123–133, Apr. 1969. 





[21] B. Ran, S. Leight, and B. Chang, “A microscopic simulation model for merging control on a dedicated-lane automated highway system,” Transp. Res. C, Emerg. Technol., vol. 7, no. 6, pp. 369–388, 1999. 





[22] D. Marinescu, J. Curn, M. Bouroche, and V. Cahill, “On-ramp trafficˇ merging using cooperative intelligent vehicles: A slot-based approach,” in Proc. 15th Int. IEEE Conf. Intell. Transp. Syst. (ITSC), Sep. 2012, pp. 900–906. 





[23] L. Li and F. Y. Wang, “Cooperative driving at blind crossings using intervehicle communication,” IEEE Trans. Veh. Technol., vol. 55, no. 6, pp. 1712–1724, Nov. 2006. 





[24] J. Lee and B. Park, “Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment,” IEEE Trans. Intell. Transp. Syst., vol. 13, no. 3, pp. 81–90, Mar. 2012. 





[25] J. Lee, B. Park, K. Malakorn, and J. So, “Sustainability assessments of cooperative vehicle intersection control at an urban corridor,” Transp. Res. C, Emerg. Technol., vol. 32, pp. 193–206, Jul. 2013. 





[26] Q. Jin, G. Wu, K. Boriboonsomsin, and M. Barth, “Multi-agent intersection management for connected vehicles using an optimal scheduling approach,” in Proc. Int. Conf. Connected Vehicles Expo (ICCVE), Dec. 2012, pp. 185–190. 





[27] F. Zhu and S. V. Ukkusuri, “A linear programming formulation for autonomous intersection control within a dynamic traffic assignment and connected vehicle environment,” Transp. Res. C, Emerg. Technol., vol. 55, pp. 363–378, Jun. 2015. 





[28] Y. Xie, H. Zhang, N. H. Gartner, and T. Arsava, “Collaborative merging strategy for freeway ramp operations in a connected and autonomous vehicles environment,” J. Intell. Transp. Syst., Technol., Planning, Oper., vol. 21, no. 2, pp. 136–147, 2017. 





[29] F. Zhou, X. Li, and J. Ma, “Parsimonious shooting heuristic for trajectory design of connected automated traffic. Part I: Theoretical analysis with generalized time geography,” Transp. Res. B, Methodol., vol. 95, pp. 394–420, Jan. 2017. 





[30] J. Ma, X. Li, F. Zhou, J. Hu, and B. B. Park, “Parsimonious shooting heuristic for trajectory design of connected automated traffic. Part II: Computational issues and optimization,” Transp. Res. B, Methodol., vol. 95, pp. 421–441, Jan. 2017. 





[31] X. Li, A. Ghiasi, and Z. Xu, “A piecewise trajectory optimization model for connected automated vehicles: Exact optimization algorithm and queue propagation analysis,” Transp. Res. B, Methodol., vol. 118, pp. 429–456, Dec. 2018. 





[32] J. Rios-Torres, A. Malikopoulos, and P. Pisu, “Online optimal control of connected vehicles for efficient traffic flow at merging roads,” in Proc. IEEE 18th Int. Conf. Intell. Transp. Syst., Sep. 2015, pp. 2432–2437. 





[33] J. Rios-Torres and A. A. Malikopoulos, “Automated and cooperative vehicle merging at highway on-ramps,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 4, pp. 780–789, Apr. 2017. 





[34] I. A. Ntousakis, I. K. Nikolos, and M. Papageorgiou, “Optimal vehicle trajectory planning in the context of cooperative merging on highways,” Transp. Res. C, Emerg. Technol., vol. 71, pp. 464–488, Oct. 2016. 





[35] X. Hu and J. Sun, “Trajectory optimization of connected and autonomous vehicles at a multilane freeway merging area,” Transp. Res. C, Emerg. Technol., vol. 101, pp. 111–125, Apr. 2019. 





[36] H. Xu, S. Feng, Y. Zhang, and L. Li, “A grouping-based cooperative driving strategy for CAVs merging problems,” IEEE Trans. Veh. Technol., vol. 68, no. 6, pp. 6125–6136, Jun. 2019. 





[37] S. Jing, F. Hui, X. Zhao, J. Rios-Torres, and A. J. Khattak, “Cooperative game approach to optimal merging sequence and on-ramp merging control of connected and automated vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 20, no. 11, pp. 4234–4244, Nov. 2019. 





[38] M. Wang, S. P. Hoogendoorn, W. Daamen, B. Van Arem, and R. Happee, “Game theoretic approach for predictive lane-changing and car-following control,” Transp. Res. C, Emerg. Technol., vol. 58, pp. 73–92, Sep. 2015. 





[39] Y. Ali, Z. Zheng, M. M. Haque, and M. Wang, “A game theorybased approach for modelling mandatory lane-changing behaviour in a connected environment,” Transp. Res. C, Emerg. Technol., vol. 106, pp. 220–242, Sep. 2019. 





[40] Y. Ali, Z. Zheng, and M. M. Haque, “Modelling lane-changing execution behaviour in a connected environment: A grouped random parameters with heterogeneity-in-means approach,” Commun. Transp. Res., vol. 1, Dec. 2021, Art. no. 100009. 





[41] K. L. Lim, J. Whitehead, D. Jia, and Z. Zheng, “State of data platforms for connected vehicles and infrastructures,” Commun. Transp. Res., vol. 1, Dec. 2021, Art. no. 100013. 





[42] X.-Y. Lu and J. K. Hedrick, “Longitudinal control algorithm for automated vehicle merging,” Int. J. Control, vol. 76, no. 2, pp. 193–202, 2003. 





[43] X.-Y. Lu, H.-S. Tan, S. E. Shladover, and J. K. Hedrick, “Automated vehicle merging maneuver implementation for AHS,” Vehicle Syst. Dyn., vol. 41, no. 2, pp. 85–107, 2004. 





[44] V. Milanés, J. Pérez, E. Onieva, and C. González, “Controller for urban intersections based on wireless communications and fuzzy logic,” IEEE Trans. Intell. Transp. Syst., vol. 11, no. 1, pp. 243–248, Mar. 2010. 





[45] V. Milanés, J. Godoy, J. Villagrá, and J. Pérez, “Automated on-ramp merging system for congested traffic situations,” IEEE Trans. Intell. Transp. Syst., vol. 12, no. 2, pp. 500–508, Jun. 2011. 





[46] R. Pueboobpaphan, F. Liu, and B. van Arem, “The impacts of a communication based merging assistant on traffic flows of manual and equipped vehicles at an on-ramp using traffic flow simulation,” in Proc. 13th Int. IEEE Conf. Intell. Transp. Syst., Sep. 2010, pp. 1468–1473. 





[47] S. M. Weaver, S. A. Balk, and B. H. Philips, “Merging into strings of cooperative-adaptive cruise-control vehicles,” J. Intell. Transp. Syst., Technol., Planning, Oper., vol. 25, no. 4, pp. 401–411, Jul. 2021. 





[48] H. Liu, X. D. Kan, S. E. Shladover, X.-Y. Lu, and R. E. Ferlis, “Impact of cooperative adaptive cruise control on multilane freeway merge capacity,” J. Intell. Transp. Syst., Technol., Planning, Oper., vol. 22, no. 3, pp. 263–275, May 2018. 





[49] A. A. Malikopoulos, C. G. Cassandras, and Y. Zhang, “Decentralized optimal control for connected and automated vehicles at an intersection,” in Proc. 55th Conf. Dec. Control, Dec. 2016, pp. 1–17. 





[50] A. A. Malikopoulos, C. G. Cassandras, and Y. Zhang, “A decentralized energy-optimal control framework for connected automated vehicles at signal-free intersections,” Automatica, vol. 93, pp. 244–256, Jul. 2018. [Online]. Available: https://www.sciencedirect. com/science/article/pii/S0005109818301511 





[51] A. A. Malikopoulos, S. Hong, B. B. Park, J. Lee, and S. Ryu, “Optimal control for speed harmonization of automated vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 20, no. 7, pp. 2405–2417, Jul. 2019. 





[52] A. A. Malikopoulos, L. Beaver, and I. V. Chremos, “Optimal time trajectory and coordination for connected and automated vehicles,” Automatica, vol. 125, Mar. 2021, Art. no. 109469. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S0005109820306671 





[53] Y. Zhou, M. E. Cholette, A. Bhaskar, and E. Chung, “Optimal vehicle trajectory planning with control constraints and recursive implementation for automated on-ramp merging,” IEEE Trans. Intell. Transp. Syst., vol. 20, no. 9, pp. 3409–3420, Sep. 2019. 





[54] Y. Zhou, E. Chung, A. Bhaska, and M. E. Cholette, “A state-constrained optimal control based trajectory planning strategy for cooperative freeway mainline facilitating and on-ramp merging maneuvers under congested traffic,” Transp. Res. C, Emerg. Technol., vol. 109, pp. 321–342, Dec. 2019. 





[55] Z. Wang et al., “Cooperative ramp merging system: Agent-based modeling and simulation using game engine,” SAE Int. J. Connected Automated Vehicles, vol. 2, no. 2, pp. 1–16, May 2019. 





[56] N. Chen, B. Van Arem, T. Alkim, and M. Wang, “A hierarchical model-based optimization control approach for cooperative merging by connected automated vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 22, no. 12, pp. 7712–7725, Dec. 2021. 





[57] A. Duret, M. Wang, and A. Ladino, “A hierarchical approach for splitting truck platoons near network discontinuities,” Transp. Res. B, Methodol., vol. 132, pp. 285–302, Feb. 2020. 





[58] R. Rajamani, H.-S. Tan, B. K. Law, and W.-B. Zhang, “Demonstration of integrated longitudinal and lateral control for the operation of automated vehicles in platoons,” IEEE Trans. Control Syst. Technol., vol. 8, no. 4, pp. 695–708, Jul. 2000. 





[59] J. Ji, A. Khajepour, W. W. Melek, and Y. Huang, “Path planning and tracking for vehicle collision avoidance based on model predictive control with multiconstraints,” IEEE Trans. Ultrason. Eng., vol. 66, no. 2, pp. 952–964, Feb. 2017. 





[60] S. Zhu and B. Aksun-Guvenc, “Trajectory planning of autonomous vehicles based on parameterized control optimization in dynamic onroad environments,” J. Intell. Robot. Syst., Theory Appl., vol. 100, nos. 3–4, pp. 1055–1067, Dec. 2020. 





[61] P. Liu, Ü. Özguner, and Y. Zhang, “Distributed MPC for cooperative highway driving and energy-economy validation via microscopic simulations,” Transp. Res. C, Emerg. Technol., vol. 77, pp. 80–95, Apr. 2017. 





[62] J. Ma, J. Hu, E. Leslie, F. Zhou, P. Huang, and J. Bared, “An ecodrive experiment on rolling terrains for fuel consumption optimization with connected automated vehicles,” Transp. Res. C, Emerg. Technol., vol. 100, pp. 125–141, Mar. 2019. 





[63] J. Gong, Y. Jiang, and W. Xu, Model Predictive Control for Self-Driving Vehicles. Beijing, China: Beijing Institute of Technology Press, 2014. 





[64] J. Wang, J. Wu, and Y. Li, “The driving safety field based on driver–vehicle–road interactions,” IEEE Trans. Intell. Transp. Syst., vol. 16, no. 4, pp. 2203–2214, Aug. 2015. 





[65] J. Wang, J. Wu, X. Zheng, D. Ni, and K. Li, “Driving safety field theory modeling and its application in pre-collision warning system,” Transp. Res. C, Emerg. Technol., vol. 72, pp. 306–324, Nov. 2016. 





[66] B. Chalaki, L. E. Beaver, and A. A. Malikopoulos, “Experimental validation of a real-time optimal controller for coordination of CAVs in a multi-lane roundabout,” in Proc. IEEE Intell. Vehicles Symp. (IV), Oct. 2020, pp. 775–780. 





[67] C. Mu, L. Du, and X. Zhao, “Event triggered rolling horizon based systematical trajectory planning for merging platoons at mainline-ramp intersection,” Transp. Res. C, Emerg. Technol., vol. 125, Apr. 2021, Art. no. 103006. 





[68] Y. Fang, H. Min, X. Wu, W. Wang, X. Zhao, and G. Mao, “On-ramp merging strategies of connected and automated vehicles considering communication delay,” IEEE Trans. Intell. Transp. Syst., early access, Jan. 11, 2022, doi: 10.1109/TITS.2022.3140219. 





[69] J. Rios-Torres and A. A. Malikopoulos, “Impact of partial penetrations of connected and automated vehicles on fuel consumption and traffic flow,” IEEE Trans. Intell. Veh., vol. 3, no. 4, pp. 453–462, Dec. 2018. 





[70] Z. Zhao, Z. Wang, G. Wu, F. Ye, and M. J. Barth, “The state-of-theart of coordinated ramp control with mixed traffic conditions,” in Proc. IEEE Intell. Transp. Syst. Conf. (ITSC), Oct. 2019, pp. 1741–1748. 





[71] Y. Ali, M. C. Bliemer, Z. Zheng, and M. M. Haque, “Cooperate or not? Exploring drivers’ interactions and response times to a lane-changing request in a connected environment,” Transp. Res. C, Emerg. Technol., vol. 120, Nov. 2020, Art. no. 102816. 





[72] X. Jiang, P. J. Jin, and Y. Wang, “A dynamic merge assistance method based on the concept of instantaneous virtual trajectory for vehicleto-infrastructure connected vehicles,” J. Intell. Transp. Syst., Technol., Planning, Oper., vol. 25, no. 3, pp. 293–312, May 2021. 



![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/36f2af64500dbb57d927b9e0ecd87a9a6d8dc38fadc3f4767dee46ec05a3b745.jpg)


Shoucai Jing received the B.S. degree in automation and the Ph.D. degree in traffic information engineering and control from Chang’an University, Xi’an, China, in 2014 and 2020, respectively. He is currently a Post-Doctoral Researcher with the School of Information Engineering, Chang’an University. He has been involved in connected and automated vehicle control systems. His research interests include cooperative control theory, game theory, and vehicle active safety. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/05231015ecaff50a82ae16fdbb44245b4e297dff0c92867bf5b8a2a12748d47c.jpg)


Fei Hui received the Ph.D. degree from the Department of Computer System Architecture, Xi’an Institute of Microelectronics Technology, Xi’an, China, in 2009. He is currently a Professor with the School of Information Engineering, Chang’an University, Xi’an. He has been involved in the China “863” Project (as the Technical Director), Information Technology Major Project of Transportation Ministry (as the Technical Director), and the National Natural Science Foundation. His current research interests include connected vehicles, vehicular networks, and image processing. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/3b01321d6f0dce65d22d9a0bbf287a7c77019ce34a87709cb754d27c595c6cc9.jpg)


Xiangmo Zhao received the Ph.D. degree from Chang’an University, Xi’an, China. He is currently a Professor with the School of Information Engineering, Chang’an University. He is also the Vice President of the Joint Laboratory for Connected Vehicles, Ministry of Education, and China Mobile and Shaanxi Road Traffic Intelligent Detection and Equipment Engineering Technology Research Centre, and is a Leader of the national key subjects-traffic information engineering and control at Chang’an University. He is also the Director of 

the Information Professional Committee and member of Advisory Expert Group, China Transportation Association, a member of the National Motor Vehicle Operation Safety Testing Equipment Standardization Committee and leading group of the National Traffic Computer Application Network, the Vice Chairperson of the Institute of Highway Association on Computer Professional Committee, and the Deputy Director of the Institute of Computer in Shaanxi Province. His currently research interests include connected vehicles, automated vehicles, intelligent transportation systems, and computer science. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/d4ae6fb3807e9a6568ea6c2fd167dd5c60c06dca37568cfdcb768b278456626a.jpg)


Jackeline Rios-Torres (Senior Member, IEEE) received the B.S. degree in electronic engineering from the Universidad del Valle, Colombia, in 2008, and the Ph.D. degree in automotive engineering from Clemson University in 2015. She is currently a Eugene P. Wigner Fellow with the Energy and Transportation Science Division, Oak Ridge National Laboratory. Her research is focused on connected and automated vehicles, intelligent transportation systems, and modeling and energy management control of HEVs/PHEVs. She is a GATE Fellow at the 

Center for Research and Education in Sustainable Vehicle Systems, CU-ICAR. She was a recipient of the Southern Automotive Women Forum Scholarship and the Smith Fellowship at CU-ICAR. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/1e43c793-5b03-4a45-87c3-267598646ad9/12ac64a3da3d76515107b438e39aab61ec6b8ec685d081dfabead6024944e3c7.jpg)


Asad J. Khattak received the M.S. and Ph.D. degrees in civil engineering from Northwestern University. 

He is currently a Beaman Distinguished Professor at the Department of Civil and Environmental Engineering (CEE), The University of Tennessee, Knoxville, and serves as the Coordinator for the Transportation Group, CEE, the Associate Director for the Collaborative Sciences Center for Road Safety, a National University Transportation Center consortium led by University of North Carolina at 

Chapel Hill, and the Co-Director of the Initiative for Sustainable Mobility. He is affiliated with the UT Center for Transportation Research as well as the Bredesen Center, which integrates university resources with Oak Ridge National Laboratory to promote advanced research. He works on a broad range of research and educational projects sponsored by state and federal agencies. He has authored/coauthored 193 articles and reports (127 scholarly journal articles and 66 technical reports to research sponsors). He has given 192 presentations at international conferences and invited talks. 

Dr. Khattak is a Special Adviser to the Journal of Transportation Safety and Security and an Advisory Board Member of analytic methods in accident research. He is the Editor-in-Chief of Science Citation Indexed Journal of Intelligent Transportation Systems, with a two-year impact factor of 1.769 in 2016. He is an Associate Editor of SCI-indexed International Journal of Sustainable Transportation, with a two-year impact factor of 1.973 in 2016. 