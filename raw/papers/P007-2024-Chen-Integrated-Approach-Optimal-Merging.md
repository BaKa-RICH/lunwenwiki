# An Integrated Approach to Optimal Merging Sequence Generation and Trajectory Planning of Connected Automated Vehicles for Freeway On-Ramp Merging Sections

Jieming Chen , Graduate Student Member, IEEE, Yue Zhou , Member, IEEE, and Edward Chung 

Abstract— Intensive interactions among vehicles at freeway on-ramp merging areas lead to congestion and accidents. The emergence of connected automated vehicles (CAVs) has shown great potential to improve this issue. In this paper, a mixed integer nonlinear programming (MINLP) model is proposed and solved for the task of a cooperative merging of two traffic streams at a freeway on-ramp merging section. The proposed model simultaneously optimizes multiple vehicles’ trajectories and their merging sequence to improve traffic efficiency and ensure safety. Unlike conventional treatments, which match one mainline facilitating vehicle with one merging vehicle, the proposed model determines the optimal number of facilitating vehicles and which mainline vehicles should serve as the facilitating vehicles to cooperatively minimize disruption from ramps. The safety and feasibility of the planned vehicle trajectories are guaranteed at any time. We propose an integrated solution algorithm that incorporates an iterative linear programming method into a novel search process based on a necessary condition for optimality that we identify and prove. The algorithm is highly efficient because it enjoys a significantly reduced search space. The proposed approach, consisting of the MINLP model and the solution algorithm, is evaluated under different traffic demands and mainline-ramp demand ratios and real vehicle arrival patterns from the NGSIM dataset. The performance of the proposed method outperforms benchmark CAV control algorithms, and the computational efficiency is promising for real-time automated merging tasks. 

Index Terms— Connected automated vehicles, on-ramp merging, optimal merging sequence, trajectory planning. 

# I. INTRODUCTION

FREEWAY on-ramp merging sections are common bot-tlenecks where two traffic streams must merge into tlenecks where two trafic streams must merge into one stream. Intensive interactions among vehicles in such 

Manuscript received 20 December 2022; revised 19 July 2023; accepted 7 September 2023. Date of publication 2 October 2023; date of current version 2 February 2024. This work was supported by the General Research Fund (Integrated Cooperative on-ramp Merging (InCoMe)) of the University Grants Committee of Hong Kong under Grant 15207320. The Associate Editor for this article was S. Ahn. (Corresponding author: Edward Chung.) 

Jieming Chen and Edward Chung are with the Department of Electrical Engineering, The Hong Kong Polytechnic University, Hong Kong, China (e-mail: jieming.chen@connect.polyu.hk; edward.cs.chung@polyu.edu.hk). 

Yue Zhou is with the Department of Electrical Engineering, The Hong Kong Polytechnic University, Hong Kong, China, and also with the C2SMART Center, Department of Urban and Civil Engineering, New York University, Brooklyn, NY 10012 USA (e-mail: zhouyue30@msn.com). 

Digital Object Identifier 10.1109/TITS.2023.3315650 

a section can result in traffic congestion, excessive fuel consumption, emissions, and accidents [1], [2], [3]. Hence, many control strategies have been proposed for managing traffic at freeway on-ramp merging sections, e.g., mainline variable speed limit and ramp metering. However, these classical flow-based control methods cannot directly influence microscopic driving behaviors which include longitudinal movements and gap selections. The advent of connected automated vehicles (CAVs) allows intelligent control of the microscopic driving behaviors of individual vehicles, and thus has initiated a new perspective to improve traffic safety and efficiency [4], [5], [6], [7], [8], [9]. 

Thanks to the significant development of perception and control technologies in the last decade, autonomous vehicles that operate based on information from on-board sensors, are getting into people’s lives. However, cooperative driving of CAVs based on V2X technology, i.e., information sharing among CAVs and between CAVs and traffic control devices, is still a developing capability. Cooperative driving involves two tasks: exploring combinations of individual actions and individual planning [10], [11], [12], [13]. In the context of freeway on-ramp merging, these two tasks correspond to merging sequence generation and trajectory planning. Merging sequence refers to the order by which mainline and on-ramp vehicles should follow to merge; it is also the order of the controlled vehicles right after the merging of these two streams of vehicles. Trajectory planning is concerned with generating trajectories following which the mainline vehicles and on-ramp vehicles, respectively, can create desired gaps and align with these gaps, both adhering to the generated merging sequence. 

The focus of this paper is to develop an integrated method that simultaneously optimizes the merging sequence and vehicle trajectories for the cooperative merging of an on-ramp and a mainline CAV streams of a freeway on-ramp merging section. 

# A. Literature Review

Existing works for on-ramp merging control of CAVs can be categorized into control without and with merging sequence decision, respectively. 

1) Trajectory Planning Without Merging Sequence Generation: This branch focuses on planning trajectories to merge 

safely and efficiently given that a mainline facilitating vehicle has been selected. One mainstream method is to convert merging problems to optimal control problems (OCPs), and then apply the Pontryagin Maximum Principle to solve OCPs. For example, Ntousakis et al. [14] formulated an OCP for a merging vehicle to minimize multi-order derivatives of speed. Zhou et al. [15] and [16] proposed decentralized optimal control problems for a facilitating vehicle and the related merging vehicle, respectively, to minimize control input. The advantage of this method is that the problem can be expressed as a linear quadratic controller clearly, and continuous-time optimal trajectories can be derived analytically. However, it is difficult to deal with complicated constraints. 

Another mainstream method is to describe trajectories in discrete-time form and then convert merging problems to numerical optimization problems. For example, in [17], two loosely coupled convex quadratic programs are formulated to obtain longitudinal and lateral motion trajectories over a finite discrete time horizon, respectively. Karimi et al. [18] formulated centralized quadratic problems for different triplets of vehicles composed of both conventional vehicles and CAV. 

There also exist works that adopt other methods. For example, Xu et al. [19] controlled a mainline facilitating vehicle with adaptive cruise control (ACC) and cooperative adaptive cruise control (CACC) to form enough space for a merging vehicle and assessed performance of both control methods. Milanes et al. [20] designed a fuzzy controller incorporating human procedural knowledge to track a linear reference distance function for a merging vehicle and a trailing mainline vehicle. 

2) Trajectory Planning With Merging Sequence Generation: Another branch of CAV merging strategies consists of the decision of merging sequence. Works in this branch can be further classified into hierarchical and integrated structures. The hierarchical structure refers to deciding a merging sequence first and then planning vehicles’ trajectories. Heuristic strategies are common ways to determine merging orders in the hierarchical structure. For example, the concept of virtual vehicles was proposed in [21], and with such a concept, all vehicles on different lanes were mapped into the same lane to obtain a driving sequence of vehicles. Similarly, the first-in-first-out (FIFO) principle was used to assign merging time instants to all vehicles [22]. Then, for each vehicle, an unconstrained fixed-time optimal control problem was formulated based on the given merging time instant and merging location to generate the associated trajectory. Letter et al. [23] calculated potential arrival time instants considering initial positions and speeds. Then, these potential arrival times are taken as parameters to plan their individual trajectories to reach the fixed merging point with a specified merging speed at these time instants. Herein, a linear programming model was formulated to maximize each vehicle’s travel speed over a finite number of time steps, with constraints imposed to ensure the fixed merging point, specified merging speed, and the merging time instant. 

Instead of using heuristic strategies to determine merging sequences as introduced above, some works tried to find optimal merging orders in the hierarchical structure. A bi-level 

optimization model was proposed in [24]. In the upper level, a mixed-integer linear programming (MILP) model was formulated to minimize travel delays and obtain each vehicle’s optimal merging time at the merging point. Then, given all the vehicles’ optimal merging times, trajectories were decided using a discrete-time trajectory planner or a heuristic continuous-time trajectory planner. The dynamic programming algorithm was utilized to find a so-called optimal passing order, given the estimated arrival time of each vehicle at the merging point, without planning trajectories [25], [26]. Chen et al. [27] put forward a hierarchical controller composed of tactical and operational layers. The tactical layer proposed a mixed integer programming model to establish the sequence and terminal time instants, which adopted the Helly car-following model and a proportional controller to describe vehicle acceleration. All sequences and different sampled terminal time instants were enumerated and fed to the model to find the best solution for the complicated tactical layer. Then, the operational layer controller utilized an OCP to generate associated trajectories. Tang et al. [28] adopted the Monte Carlo tree search method in the upper-level model to determine a merging sequence. Then trajectories were obtained by an OCP based on this sequence. Cooperative game theory was adopted to determine the merging sequence and then computed trajectories by an OCP [29]. 

The integrated structure takes care of merging sequence generation and trajectory planning simultaneously. Cao et al. [30] adopted the model predictive control (MPC) scheme to optimize the motions of a pair of mainline and on-ramp vehicles, with the nonlinear constraint that the relative distance between vehicles must be kept above an appropriate value. Therefore, the vehicle sequence is also determined when both trajectories are generated. However, this nonlinear constraint is hard to be applied to multiple vehicles. Similarly, Xie et al. [31] also specified absolute spacing between any two vehicles in a MILP model to maximize speed over a fixed number of time steps. Therefore, all possible vehicle sequences were considered, but for simplifying the problem, the time duration of merging cooperation was assumed to be known. Mu et al. [32] developed a complicated MINLP model to merge two platoons and developed a heuristic algorithm to solve the model. However, the heuristic algorithm only searches the solution near the sequence based on the first-in-first-out rule, which cannot guarantee optimality. 

3) Summary: As for methods focusing on trajectory planning only, optimal control can yield optimal continuous-time trajectories but is limited by complex constraints. In contrast, discrete-time trajectory optimization can solve various constraints more efficiently, but constraints can be enforced only at the discretization nodes and not in between the nodes. Hence, many sampling points must be needed to ensure the viability of the trajectory, which increases the computational burden. 

When it comes to methods that take care of both trajectory planning and merging sequence generation, there can be two methodological structures to do the job, namely hierarchical and integrated. The hierarchical structure usually first assigns each vehicle a time to reach a fixed merging point. Then, the trajectories of all the vehicles are planned based on these 

assigned merging times. The advantage of this structure is that the merging sequence generation and trajectory planning problems are explicitly separated, making each of them easier to solve. However, additional assumptions are needed, such as fixed merging points, and the estimated arrival times may result in infeasible solutions or low-quality trajectories which refers to time consuming, energy consuming, and jerky trajectories. The integrated structure takes care of trajectory planning and merging sequence generation simultaneously, usually by one model. In this structure, merging positions can be flexible rather than fixed. Moreover, the quality of planned trajectories can have an influence on the generation of merging sequence. Therefore, the integrated structure can avoid the drawbacks of the hierarchical structure. However, the integrated structure can result in a very complicated model that is difficult to solve. Because of this difficulty, few studies have adopted the integrated structure. 

Finally, we note that most of existing studies [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32] have applied a linear discrete-time motion model and thus can only guarantee safety at discrete time points. 

To fill in the above research gaps, this paper enriches the methodology of the integrated structure and meanwhile guarantees safety in the continuous-time form. 

# B. Summary of Highlights and Contributions

This paper contains three major technical contributions and three minor ones. The three major contributions are: 

1) A mixed integer nonlinear programming (MINLP) model is formulated to model the cooperative merging of on-ramp and mainline traffic streams. The proposed model jointly determines both the optimal merging sequence of these vehicles and their trajectories to minimize the disruption of on-ramp merging traffic to mainline traffic. 

2) An integrated solution algorithm is proposed to simultaneously obtain the optimal merging sequence and detailed trajectories. The vehicle sequence search process is designed based on the necessary optimality condition of the model that we identify and prove, so that the solution space for integer variables, i.e. merging sequences, is greatly refined, while ensuring optimality. During the search process, the relaxed nonlinear programming (NLP) model is solved efficiently by an iterative linear programming method. Thus, the proposed methods can satisfy real-time computation. 

3) The proposed approach, composed of the proposed model and algorithm, is an integrated approach so that the resulting merging sequence can guarantee feasible and high-quality trajectories. Moreover, the optimal traffic efficiency is obtained by the resulting optimal merging sequence, rather than heuristically assigning a facilitating vehicle to an on-ramp vehicle, as in many existing studies. 

The three minor contributions include: 

1) Trajectories are characterized by continuous-time functions so that artificial setting of numerous discrete points 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/caf2facfbe3a910b6f73632ff52d4c4627d38ac3c83f6ef124fe96ab8d324532.jpg)



Fig. 1. The on-ramp merging scenario.


is avoided, and the number of decision variables is reduced. The convex hull property of the Bernstein basis is incorporated to ensure that all constraints, such as car-following, merging safety and constraints on vehicle speeds and accelerations, are guaranteed at any time, rather than only at discrete time points. 

2) The merging time and locations are determined by the model instead of relying on external computational procedures. In other words, the merging time and locations are part of the outcome of the proposed model. 

3) The traffic efficiency, safety, and computational efficiency of the proposed approach are demonstrated under different traffic conditions and compared with three alternative methods, on the NGSIM dataset. 

# C. Organization of the Paper

In the remainder, Section II describes the modeling of cooperative merging of a mainline and an on-ramp traffic streams at a freeway on-ramp merging section as a MINLP problem; Section III develops a computationally efficient algorithm to solve the model; Section IV introduces the recursive feedback mechanism; Section V validates the proposed method by numerical experiments; Section VI concludes the paper. 

# II. MATHEMATICAL MODELING

# A. Preliminaries

We first introduce the merging scenario considered in this study, and then define two key notions that will be used in the formulation of the optimization problem, namely the merging sequence and the mathematical representation of trajectories. 

1) The Merging Scenario Considered in This Study: This study is oriented toward merging two streams of vehicles at a freeway on-ramp section. Fig.1 shows a typical freeway on-ramp merging section consisting of one mainline lane and one on-ramp lane connected with one acceleration lane. Initially, vehicles are assumed to be in a car-following mode. A roadside unit (RSU) is placed upstream of the intersection of the mainline and on-ramp lanes. RSU receives nearby CAVs’ information, executes the proposed model, and then sends acceleration/deceleration commands to CAVs. In addition, a trigger point (TP), enabled by, for example, a loop detector, is placed at a suitable location of the on-ramp. Every time an on-ramp vehicle arrives at the TP, RSU starts a new control cycle and regards nearby mainline and on-ramp vehicles as a batch of planned vehicles. It means that, instead of driving in a car-following mode, these planned vehicles follow the instructions of the proposed model. After completing merging tasks, these vehicles revert to the car-following mode again. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/bf59ba45218b09fb5ed1af9dc4edebdbae5f0ce1e2a6351f4d52bab2a19ba14e.jpg)



Fig. 2. Merging sequence description.


Fig. 1 shows two batches of planned vehicles. The formation of planned vehicles includes grouping on-ramp vehicles and mainline vehicles. In addition to the on-ramp vehicle that drives through the TP, its following on-ramp vehicles will be grouped if their time headway is less than a specified threshold. Then, the first and last on-ramp vehicles are mapped onto the mainline lane to determine the planned mainline vehicles in this control cycle. 

In this paper, we only consider the longitudinal motion of merging vehicles, in line with many previous studies [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31]. In addition, the model proposed in this paper is not limited to single-mainline merging scenarios because in generalized multi-mainline ramp merging scenarios, lane-changing and on-ramp merging maneuvers are usually expected to be performed on different segments of roads [33], [34], [35]. This means that we assume that the lane-changing behavior of the mainline vehicles has already taken place before the cooperative merge starts. Therefore, to focus on the merging behavior, we consider the scenario with one mainline lane and one on-ramp lane. 

As aforementioned, merging two streams of vehicles consists of two tasks: merging sequence scheduling and merging trajectory planning. Merging sequence scheduling determines the order of the controlled vehicles in the merged stream, i.e., after the merging is completed. Merging trajectory planning is responsible for generating trajectories for the mainline facilitating vehicles to create desired gaps and for the on-ramp vehicles to coordinate with these gaps adhering to the determined merging sequence. Furthermore, these two tasks are coupled with each other in the sense that the outcome of one of them can influence the outcome of the other. That is, the merging sequence influences the design of the trajectories, and the cost associated with these trajectories will in turn influence the determination of the merging sequence. 

2) Merging Sequence: The merging sequence refers to the order of the controlled vehicles right after the merging of the two streams of vehicles. It reflects the result of merge-in gap selections of on-ramp vehicles. In this paper, a merge-in gap refers to the gap between two mainline vehicles into which one or more on-ramp vehicles can merge. It ought to be noted that under our method, it is not necessary that each candidate merge-in gap will be selected. As shown in Fig. 2, let $L : =$ $\{ m , r \}$ denote the set of lanes, in which $m$ and $r$ refer to the mainline lane and on-ramp lane, respectively. Then, $I _ { m }$ and $I _ { r }$ represent a set of planned vehicles in the mainline lane and onramp lane, respectively, which means there are $\vert I _ { m } \vert$ planned mainline vehicles and $\left| I _ { r } \right|$ planned on-ramp vehicles in this control cycle. Besides, there may be a leading vehicle for these 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/8425b6a6ca17f510cdf1a0738f72ec8288d9472b5b539493072a81677a8ed97c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/5baa65b9a90fc5feb27e3fbbe1849bb9e527a352167460d4ab098503b2ab7fa7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/098344efc0c9904bce7f993cc8a6da8831dce0f79306692df0d6d14c45ef0634.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/5a713f13724e59139083d992d2a09b20d86ecf632c03a47ba44fb44527d3cd4f.jpg)



Fig. 3. The search tree of merging sequences: (a) the search space for the first on-ramp vehicle; (b) (c) (d) three possible search cases for the second on-ramp vehicle.


planned vehicles. Note that the leading vehicle can be either a mainline or on-ramp vehicle. It tracks designed trajectories from the previous control cycle, thereby not being involved in this control cycle. Then, let $I _ { m } ^ { + } : = \{ 1 , \ldots , | I _ { m } | + 1 \}$ denote the set of these merge-in gaps on the mainline lane. Both indexes of planned vehicles in each lane and merge-in gaps increase from one against the direction of traffic travel. 

For on-ramp vehicle $i$ , we define a binary vector $\gamma _ { i } : \ :$ $[ \gamma _ { i , 1 } , \dots , \gamma _ { i , k } , \dots , \gamma _ { i , | I _ { m } | + 1 } ] ^ { T }$ where each element $\gamma _ { i , k }$ represents whether on-ramp vehicle i, $i \in I _ { r }$ , chooses the merge-in gap k, $k ~ \in ~ I _ { m } ^ { + }$ , to merge. Thus, the existence of binary variables leads to the gap selection problem as an integer programming problem. 

The choice of merge-in gaps determines terminal positions of all vehicles. Specifically, if the $i ^ { t h }$ on-ramp vehicle merges into the $k ^ { t h }$ merge-in gap, then on-ramp vehicle i must keep a safe distance from both the $k - 1 ^ { t h }$ and $k ^ { t h }$ mainline vehicles at the terminal time. Thus, $\gamma _ { i }$ is closely coupled with vehicles’ trajectories. 

3) Mathematical Representation of Vehicle Trajectories: We consider a second-order model as the vehicles’ kinematic model: 

$$
\dot {x} _ {l, i} (t) = v _ {l, i} (t), \tag {1}
$$

$$
\dot {v} _ {l, i} (t) = a _ {l, i} (t), \tag {2}
$$

where l, $l \in L$ , refers to lanes; i , $i \in I _ { l }$ , refers to the vehicle index; $t$ refers to time; $a _ { l , i } ( t )$ is the acceleration; $v _ { l , i } ( t )$ is the velocity; $x _ { l , i } \left( t \right)$ is the position. The nonholonomic property of vehicles is omitted since we focus on the longitudinal motion. The coordinate system adopted in this paper is the Frenet coordinate system with the road center line as the reference line [48]. The longitudinal distance refers to the distance along the road center line. 

Polynomial functions up to the third order are adopted to prescribe the solution space of the model (1)-(2): 

$$
\left[ \begin{array}{l} x _ {l, i} (t) \\ v _ {l, i} (t) \\ a _ {l, i} (t) \end{array} \right] = \left[ \begin{array}{c c c c} t ^ {3} & t ^ {2} & t & 1 \\ 3 t ^ {2} & 2 t & 1 & 0 \\ 6 t & 2 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} \theta_ {l, i, 3} \\ \theta_ {l, i, 2} \\ \theta_ {l, i, 1} \\ \theta_ {l, i, 0} \end{array} \right], \tag {3}
$$

where $\mathbf { \theta } _ { \theta _ { l , i } } : = \left[ \theta _ { l , i , 3 } , \theta _ { l , i , 2 } , \theta _ { l , i , 1 } , \theta _ { l , i , 0 } \right] ^ { T }$ is the parameter vector of the polynomial curve of vehicle $i$ on lane l. The employment of polynomials allows a reduced search space. 

However, the polynomial basis has difficulty in handling some constraints, such as velocity constraints and minimum distance between the positions of two adjacent vehicles at any time along the entire position trajectories. In order to incorporate these constraints into the polynomial representations of the trajectories, we introduce the Bézier curves. 

A Bézier curve is defined by a set of control points. The control points include a start point, a terminal point, and shapedefined points. The first and last control points are always the endpoints of the curve. The order of a Bézier curve depends on the number of control points. A Bézier curve $P ( s )$ of order $n$ , obtained from $n + 1$ control points, is written as: 

$$
P (s) = \sum_ {j = 0} ^ {n} B _ {j} ^ {n} (s) P _ {j} \quad s \in [ 0, 1 ], \tag {4}
$$

where $B _ { j } ^ { n } \left( s \right)$ is the jth Bernstein polynomial of degree $n$ , which can be defined by: 

$$
B _ {j} ^ {n} (s) = \binom {n} {j} s ^ {j} (1 - s) ^ {n - j} = \frac {n !}{j ! (n - j) !} s ^ {j} (1 - s) ^ {n - j}. \tag {5}
$$

From (4), $P ( s )$ is a linear combination of $n$ Bernstein polynomial bases, and $P _ { j }$ is the coefficient of each $B _ { j } ^ { n } ( s )$ . $P _ { j }$ can regulate the magnitude of a basis. Hence, the shape of a curve $P ( s )$ can be manipulated by the control points. 

A Bernstein polynomial has a convex hull property, which means that a Bernstein polynomial is confined within the convex hull of its control points [36]. Therefore, we can enforce continuous trajectory functions to be within a specified feasible set by setting the control points. Then, polynomial basis (3) can be equivalently rewritten in terms of the Bernstein basis, and the control points of $x _ { l , i } ( t )$ , denoted by $\pmb { P } _ { l , i } ^ { x }$ , can be represented by $\pmb { \theta } _ { l , i }$ : 

$$
\left[ \begin{array}{l} P _ {l, i, 3} ^ {x} \\ P _ {l, i, 2} ^ {x} \\ P _ {l, i, 1} ^ {x} \\ P _ {l, i, 0} ^ {x} \end{array} \right] = \left[ \begin{array}{c c c c} t _ {f} ^ {3} & t _ {f} ^ {2} & t _ {f} & 1 \\ 0 & t _ {f} ^ {2} / 3 & 2 t _ {f} / 3 & 1 \\ 0 & 0 & t _ {f} / 3 & 1 \\ 0 & 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{l} \theta_ {l, i, 3} \\ \theta_ {l, i, 2} \\ \theta_ {l, i, 1} \\ \theta_ {l, i, 0} \end{array} \right], \tag {6}
$$

where $t _ { f }$ is terminal time of the trajectories. Similarly, the control points of $v _ { l , i } ( t )$ , denoted by $P _ { l , i } ^ { v }$ , are written as: 

$$
\left[ \begin{array}{l} P _ {l, i, 2} ^ {v} \\ P _ {l, i, 1} ^ {v} \\ P _ {l, i, 0} ^ {v} \end{array} \right] = \left[ \begin{array}{c c c c} 3 t _ {f} ^ {2} & 2 t _ {f} & 1 & 0 \\ 0 & t _ {f} & 1 & 0 \\ 0 & 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{l} \theta_ {l, i, 3} \\ \theta_ {l, i, 2} \\ \theta_ {l, i, 1} \\ \theta_ {l, i, 0} \end{array} \right], \tag {7}
$$

The detailed derivation of (6) and (7) is given in Appendix B. 

In our problem, $t _ { f }$ and the terminal states of vehicles are unknown, which causes (3, 6, 7) to be nonlinear equations and results in a nonlinear programming problem. 

# B. Model Formulation

A MINLP is formulated in this subsection to model the problem of integrated optimization of merging sequence generation and trajectory planning for cooperative on-ramp merging. The notation used in this paper is listed as follows. 

# Indices and Sets

$L$ set of lanes, $l\in L$ $l = \{m,r\}$ , where $m$ and $r$ refer to the mainline lane and on-ramp lane. $I_{m}$ set of planned mainline vehicles, $i$ (or $j)\in I_m$ $I_{r}$ set of planned on-ramp vehicles, $i$ (or $j)\in I_r$ $I_{m}^{+}$ set of merge-in gaps on the mainline lane, $k\in I_m^+$ 

# Input Parameters

$\tilde{v}$ desired terminal speed, e.g., the free-flow speed or initial speed of CAVs. 

$\tau$ minimum allowable time gap between vehicles. 

$s_0$ buffer distance. 

$l_{v}$ length of a vehicle. 

$l_{zone}$ length of the cooperation zone. 

$w_{m}$ weighting factor for the travel delay of mainline vehicles. 

$w_{r}$ weighting factor for the travel delay of on-ramp vehicles. 

$\overline{b}, \overline{a}$ maximum deceleration and acceleration. 

$\nu, \bar{\nu}$ minimum and maximum speeds. 

$x_{L,i}^{init}$ initial position of vehicle $i$ on lane $l$ . 

$v_{l,i}^{init}$ initial velocity of vehicle $i$ on lane $l$ . 

# Decision Variables

$t_f$ terminal time when merging cooperation is finished. continuous variable. 

$\pmb{\theta}_{l,i}$ vector of trajectory parameters of vehicle $i$ on lane $l$ . $\pmb{\theta}_{l,i} = \left[\theta_{l,i,3},\theta_{l,i,2},\theta_{l,i,1},\theta_{l,i,0}\right]^T$ . continuous variables. 

$\gamma_{i}$ vector indicating merge-in gap selection of on-ramp vehicle $i$ $i\in I_r.\gamma_i = [\gamma_{i,1},\dots ,\gamma_{i,l|m] + 1}]^T$ in which $\gamma_{i,k},i\in I_r,k\in I_m^+$ equals 1, if and only if the $k^{th}$ candidate merge-in gap is chosen by the $i^{th}$ on-ramp vehicle; 0, otherwise. binary variables. 

Our objective is to have the two streams of vehicles merge safely and meanwhile minimize their total delay, through planning the trajectories for all these vehicles. As introduced earlier, we are aiming at a joint optimization task that can yield the optimal merging sequence and trajectories simultaneously. Therefore, our decision variables include $\pmb { \theta } _ { l , i }$ , l ∈ L , $i \in I _ { l }$ ; $\gamma _ { i }$ , $i \in I _ { r }$ ; and $t _ { f }$ . The model is detailed as follows. 

$$
\begin{array}{l} \min  _ {\gamma_ {i}, \theta_ {l, i}, t _ {f}} w _ {m} \sum_ {i \in I _ {m}} \int_ {0} ^ {t _ {f}} \left(\tilde {v} - v _ {m, i} (t)\right) d t \\ + w _ {r} \sum_ {i \in I _ {r}} \int_ {0} ^ {t _ {f}} \left(\tilde {v} - v _ {r, i} (t)\right) d t \tag {8} \\ \end{array}
$$

subject to: $x _ { l , i } \left( t _ { f } \right) \geq x _ { l , i + 1 } \left( t _ { f } \right) + \tau \cdot v _ { l , i + 1 } \left( t _ { f } \right) + l _ { v } + s _ { 0 } ;$ 

$$
\forall l \in L, \quad i \in I _ {l} \backslash \{| I _ {l} | \} \tag {9}
$$

$$
x _ {\text {l e a d}} \left(t _ {f}\right) \geq x _ {m, 1} \left(t _ {f}\right) + \tau \cdot v _ {m, 1} \left(t _ {f}\right) + l _ {v} + s _ {0} \tag {10}
$$

$$
x _ {r, 1} \left(t _ {f}\right) \leq x _ {r, 1} (0) + l _ {\text {z o n e}} \tag {11}
$$

$$
\sum_ {k \in I _ {m} ^ {+}} \gamma_ {i, k} = 1; \quad \forall i \in I _ {r} \tag {12}
$$

$$
\gamma_ {i + 1, k} \leq \sum_ {n = 0} ^ {k} \gamma_ {i, n}; \quad \forall i \in I _ {r} \backslash \left\{\left| I _ {r} \right| \right\}, k \in I _ {m} ^ {+} \tag {13}
$$

$$
\begin{array}{l} x _ {r, i} \left(t _ {f}\right) \geq \boldsymbol {x} _ {m} ^ {T} \widetilde {\boldsymbol {\gamma}} _ {i} + \tau \cdot v _ {r, i} \left(t _ {f}\right) + l _ {v} + s _ {0}; \\ \forall i \in I _ {r} \tag {14} \\ \end{array}
$$

$$
\begin{array}{l} x _ {r, i} \left(t _ {f}\right) \leq \left[ \begin{array}{c} x _ {\text {l e a d}} \left(t _ {f}\right) \\ \boldsymbol {x} _ {m} \end{array} \right] ^ {T} \boldsymbol {\gamma} _ {i} - \tau \cdot v _ {r, i} \left(t _ {f}\right) \\ - l _ {v} - s _ {0}; \forall i \in I _ {r} \tag {15} \\ x _ {l, i} (t) - x _ {l, i + 1} (t) \geq l _ {v} + s _ {0}; \\ \end{array}
$$

$$
\forall t \in [ 0, t _ {f}), \quad l \in L, i \in I _ {l} \backslash \{| I _ {l} | \} \tag {16}
$$

$$
\bar {b} \leq a _ {l, i} (t) \leq \bar {a}; \quad \forall t \in [ 0, t _ {f} ], l \in L, i \in I _ {l} \tag {17}
$$

$$
\underline {{v}} \leq v _ {l, i} (t) \leq \bar {v}; \quad \forall t \in [ 0, t _ {f} ], l \in L, i \in I _ {l} \tag {18}
$$

$$
x _ {l, i} (0) - x _ {l, i} ^ {\text {i n i t}} = 0; \quad \forall l \in L, i \in I _ {l} \tag {19}
$$

$$
v _ {l, i} (0) - v _ {l, i} ^ {\text {i n i t}} = 0; \quad \forall l \in L, i \in I _ {l}. \tag {20}
$$

1) Cost Function: To improve traffic efficiency, the objective function (8) is to minimize the difference between all vehicles’ speeds and the desired speed, cumulated over the entire control horizon. Moreover, consecutive tiny speed drops at the merging point can incur traffic breakdown [37]. Therefore, the cost function helps avoid breakdown. 

2) Terminal Constraints: Constraint (9) ensures that terminal spacings between vehicles within the same lane must be greater than or equal to the distance corresponding to the minimum allowable time gap plus a vehicle length and buffer distance. 

Similarly, constraint (10) considers that the leading vehicle restricts the terminal position of the first mainline vehicle following behind it. In (10), $x _ { l e a d } ( t _ { f } )$ refers to the terminal position of the leading vehicle. Note that if the leading vehicle is planned in the last control cycle, its trajectory is known; otherwise, it can be predicted by rolling out the car-following model. 

Additionally, constraint (11) enforces that the merging positions of on-ramp vehicles must be within the range of the cooperation zone, $l _ { z o n e }$ , due to the limited acceleration lane. 

3) Constraints for Gap Selection: Obviously, each on-ramp vehicle can only merge into one merge-in gap, as constraint (12). Moreover, because overtaking is not allowed, constraint (13) states that an on-ramp vehicle can only choose a gap from the merge-in gap chosen by its preceding on-ramp vehicle and the following upstream merge-in gaps. Note that adjacent on-ramp vehicles can choose the same merge-in gap, i.e. it is permissible for a mainline vehicle to facilitate several on-ramp vehicles. 

Furthermore, when a merge-in gap is selected, the on-ramp vehicle and two mainline vehicles ahead and behind the selected gap are linked spatially. Correspondingly, constraints (14) and (15) impose that at the terminal time, if the $k ^ { t h }$ gap is chosen by the $i ^ { t h }$ on-ramp vehicle, both the $k - 1 ^ { t h }$ and $k ^ { t h }$ mainline vehicles need to spatially form a minimum distance from the $i ^ { t h }$ on-ramp vehicle, respectively. This minimum distance corresponds to the minimum allowable time gap plus a vehicle length and buffer distance. Constraint (14) is for the spatial relation between on-ramp vehicles and mainline vehicles behind merge-in gaps. In (14), the vector $\begin{array} { r l } { \pmb { x } _ { m } } & { { } : = } \end{array}$ $[ x _ { m , 1 } \left( t _ { f } \right) , \ldots , x _ { m , | I _ { m } | } ( t _ { f } ) ] ^ { \stackrel { \_ } { T } }$ contains terminal positions of all mainline vehicles; $\bar { \boldsymbol { \gamma } } _ { i } : = [ \gamma _ { i , 1 } , \ldots , \gamma _ { i , | I _ { m } | } ] ^ { T }$ contains all merge-in gap options except the last one, $\gamma _ { i , | I _ { m } | + 1 }$ . 

Likewise, constraint (15) is for the spatial relation between on-ramp vehicles and mainline vehicles ahead of mergein gaps. The physical implication of keeping at least one minimum allowable time gap is to smoothly switch to the 

car-following strategy (constant time-gap CACC or ACC) when the merging process is completed. 

4) Constraints of Collision Avoidance: During the cooperation, constraint (16) guarantees that collision will not happen between vehicles within the same lane. To ensure safety at any time, rather than only at discrete time nodes, the spacing between two trajectories, $x _ { l , i } \left( t \right) - x _ { l , i + 1 } ( t )$ , is represented by the Bézier basis. Thanks to its convex hull property, (16) can be concisely expressed as the control points of $x _ { l , i } \left( t \right) - x _ { l , i + 1 } \left( t \right)$ must be greater than or equal to the vehicle length plus the minimum spacing. Corresponding inequality equations are written as: 

$$
P _ {l, i, 1} ^ {x} - P _ {l, i + 1, 1} ^ {x} \geq l _ {v} + s _ {0}, \tag {21}
$$

$$
P _ {l, i, 2} ^ {x} - P _ {l, i + 1, 2} ^ {x} \geq l _ {v} + s _ {0}, \tag {22}
$$

where control points are expressed as (6). 

5) Constraints on Vehicle Speeds and Accelerations: Constraints (17) and (18) bound the acceleration and velocity of all vehicles at any time. Because the acceleration of a vehicle is linear in time, referring to (3), acceleration constraints only need to be imposed at the initial time and terminal time. Therefore, (17) can be equivalently re-written as: 

$$
\bar {b} \leq a _ {l, i} (0) \leq \bar {a}, \tag {23}
$$

$$
\bar {b} \leq a _ {l, i} (t _ {f}) \leq \bar {a}. \tag {24}
$$

To ensure velocity constraints at any time, control points of velocity functions are restricted to the lower and upper bounds of velocity, and (18) is rewritten as: 

$$
\underline {{v}} \leq P _ {l, i, 1} ^ {v} \leq \bar {v}, \tag {25}
$$

$$
\underline {{v}} \leq P _ {l, i, 2} ^ {v} \leq \bar {v}, \tag {26}
$$

where control points are expressed as (7). 

6) Constraints of Initial Conditions: The starting position and speed of each vehicle are specified in constraints (19) and (20). 

In sum, (8)-(20) represent the proposed mathematical problem formulation. Substantial nonlinearities exist in the cost function and the constraints. Furthermore, (14)-(15) introduce binary vectors. These render the optimization problem difficult to solve. Hence, we propose a solution algorithm to solve it efficiently. 

# III. AN INTEGRATED SOLUTION ALGORITHM

# A. Overview

In the above, we have formulated the task of merging sequence optimization and the task of vehicle trajectory optimization into one single mathematical model, i.e. the proposed MINLP, where $\pmb { \theta } _ { l , i }$ , l ∈ L , $i \in I _ { l }$ , and $t _ { f }$ are continuous decision variables defining trajectories, and γ i , $i \in I _ { r }$ , are binary decision variables defining merging sequence. 

When solving the proposed MINLP, the trajectory variables and the merging sequence variables must be solved jointly, in the sense that neither of them can be determined independently of the other or can be determined earlier than the other. Only if this can be achieved, can we say that the proposed 


TABLE I OPTIMAL SEQUENTIAL SEARCH PROCESS


<table><tr><td colspan="2">Algorithm 1. Integrated Solution Algorithm for Joint Optimization of Merging Sequence and Vehicle Trajectories</td></tr><tr><td colspan="2">Input: |Im| mainline CAVs and |Ir| on-ramp CAVs</td></tr><tr><td colspan="2">Output: Optimal merging sequence {γ1*, γ1*, ..., γI*rl}</td></tr><tr><td>1</td><td>Algorithm 2 returns the cost and the trajectories for the first on-ramp CAV and the |Im| mainline CAVs under different γ1, to obtain γ1*.</td></tr><tr><td>2</td><td>for i := 2 to |Ir| do</td></tr><tr><td>3</td><td>Algorithm 2 returns the cost and the trajectories for i (from the 1sttoith) on-ramp CAVs and the |Im| mainline CAVs under different γi, with γ1*, ..., γi-1as conditions, to obtain γi*.</td></tr><tr><td>4</td><td>end for</td></tr><tr><td>5</td><td>return {γ1*, γ2*, ..., γI*rl}</td></tr></table>

method is an integrated approach to optimal merging sequence generation and trajectory planning. 

In the following three paragraphs, we present an overview of the proposed algorithm, how we simultaneously solve the merging sequence optimization and trajectory optimization tasks in an integrated way, rather than a conventional two-stage approach that first deals with merging sequence optimization and then trajectory optimization. 

For a group of on-ramp vehicles, the proposed algorithm determines their optimal merge-in gaps one by one, starting from the first on-ramp vehicle (i.e. the most downstream one) and moving upstream. 

For a certain on-ramp vehicle, its optimal merge-in gap is determined from all the candidate merge-in gaps for this onramp vehicle. For each candidate merge-in gap, we optimize the trajectory parameters of all mainline vehicles, this on-ramp vehicle and all the on-ramp vehicles ahead of this on-ramp vehicle. The incurred cost is computed and recorded. Therefore, the optimal merge-in gap can be selected as the one that has incurred the lowest cost among all the candidate gaps. 

The above approach implies: 1) the results of trajectory optimization have influences on the selection of optimal merge-in gaps, and vice versa; 2) if and only if the optimal merge-in gap for the last on-ramp vehicle in this CAV group is determined, both the optimal merging sequence and corresponding trajectories of all involved vehicles in this CAV group are determined jointly and simultaneously. Neither of them can be determined independently of the other or can be determined earlier than the other. It is in such a way that the proposed solution algorithm integrates the task of merging sequence optimization and the task of trajectory optimization into one unified process. 

The algorithm is formally presented in TABLE I, where the embedded Algorithm 2 optimizes vehicle trajectories, which will be introduced in Section III-E. 

In Section III-B., we describe in detail by a simple case how the proposed algorithm determines the optimal merge-in gaps for a group of on-ramp vehicles one by one. In Section III-C., we explain the advantage of such a sequential determination of on-ramp vehicles’ optimal merge-in gaps – the size of search space can be reduced. In Section III-D., we prove that such a sequential way will indeed generate the same optimal results 

as one that considers all the on-ramp vehicles simultaneously, so have we verified by experiment in Section IV.H. Finally, in Section III-E., we present the iterative linear programming method, which is responsible for the trajectory generation, i.e. Algorithm 2 embedded in the integrated solution algorithm. 

# B. Determining Optimal Merge-in Gaps for On-Ramp Vehicles One by One

Mixed integer problems can be solved by the classic branchand-bound (B&B) method. However, the size of the B&B’s solution space in this problem is $2 ^ { ( | I _ { m } | + 1 ) | I _ { r } | }$ , where $\vert I _ { m } \vert$ and $\lvert I _ { r } \rvert$ are the number of mainline and on-ramp vehicles respectively. This implies that the size of the search space grows exponentially as the number of involved vehicles increases. To overcome this issue and exploit the characteristics of the merging scenario, the proposed process determines the optimal merge-in gap for each on-ramp vehicle one by one, starting from the first (i.e., the most downstream) on-ramp vehicle and moving upstream. 

Specifically, in the first step, all the combinations of $\gamma _ { 1 }$ , i.e., all possible merge-in gap selections for the first onramp vehicle, are enumerated, and the trajectories of the first on-ramp vehicle and all mainline vehicles are planned under each combination to determine $\gamma _ { 1 } ^ { * }$ . Then, the first and the second on-ramp vehicles and all the mainline vehicles are planned conditioning on $\gamma _ { 1 } ^ { * }$ to determine $\gamma _ { 2 } ^ { * }$ . Analogously, the first to the $i ^ { t h }$ on-ramp vehicles and all the mainline vehicles are planned conditioning on $\gamma _ { 1 } ^ { * } , \ldots , \gamma _ { i - 1 } ^ { * }$ to determine $\gamma _ { i } ^ { * }$ This process terminates until the best merge-in gap selection of the last on-ramp vehicle, i.e., $\gamma _ { | I _ { r } | } ^ { * }$ , is decided. 

Take the example of there being two mainline and two on-ramp vehicles in a control cycle. The corresponding searching process for this example is illustrated in Fig. 3. Obviously, there exist three merge-in gaps for merging vehicles because there are two mainline vehicles. Fig. 3 (a) depicts that all possible merge-in gaps of the first merging vehicle will be enumerated to find $\gamma _ { 1 } ^ { * }$ . Fig. 3 (b) shows that all the three possible gaps need to be searched again for the second merging vehicle if the first merging vehicle chooses the first gap, i.e., $\gamma _ { 1 } ^ { * } = [ 1 , 0 , 0 ] ^ { T }$ . Similarly, Fig. 3 (c) illustrates that the search space of the second merging vehicle narrowed to two options when the first merging vehicle chooses the second gap. Lastly, Fig. 3 (d) shows that the second on-ramp vehicle has only one merging order option, i.e., $[ 0 , 0 , 1 ] ^ { T }$ , if its leading on-ramp vehicle chooses the last merge-in gap. 

In Step 3 of Algorithm 1, when determining the merging sequence of the remaining vehicles, the merging sequence of the preceding vehicles has already been fixed, but their trajectories would be replanned to obtain a unified $t _ { f }$ and optimal trajectories for all vehicles. Moreover, under Algorithm 1, thanks to the sequential determination of optimal merge-in gaps for the on-ramp vehicles described above, the original MINLP is reduced to nonlinear program (NLP) to optimize vehicle trajectories, as in Step 1 and Step 3 of Algorithm 1. 

# C. Reduced Search Space

The proposed optimal sequential searching process can efficiently reduce the search space due to the following three 

reasons. First, the number of combinations of γ i , $i \in I _ { r }$ , is $| I _ { m } | + 1$ since (12) imposes that only one element in $[ \gamma _ { i , 1 } , \gamma _ { i , 2 } , \ldots , \gamma _ { i , | I _ { m } | + 1 } ] ^ { T }$ can be one. This greatly reduces the solution space from $2 ^ { | I _ { m } | + 1 }$ to $| I _ { m } | + 1$ for on-ramp vehicle i . Hence, for all $\left| I _ { r } \right|$ on-ramp vehicles, the search space is reduced to $( | I _ { m } | + 1 ) ^ { | I _ { r } | }$ , instead of $2 ^ { ( | I _ { m } | + 1 ) | I _ { r } | }$ . Second, (13) indicates that an on-ramp vehicle can only select the same mainline gap chosen by its preceding on-ramp vehicle or the following gaps. In other words, an on-ramp vehicle cannot choose a mainline gap downstream of the mainline gap chosen by its preceding on-ramp vehicle. Third, as presented in Algorithm 1, the merging sequence is sequentially solved from $\gamma _ { 1 }$ to $\gamma _ { \left| I _ { r } \right| }$ so that a tree-structured search space is constituted, and the tree’s depth is $\left| I _ { r } \right|$ . As an illustration, Fig. 3 shows a tree with depth two when there are two mainline and two on-ramp vehicles. 

# D. Optimality

Now we prove that the proposed optimal sequential searching process can indeed generate the optimal merging sequence. To this end, rather than work with the original objective function, (8), we instead work with an equivalent objective function, (27). 

$$
\left\{\boldsymbol {\gamma} _ {1} ^ {*}, \boldsymbol {\gamma} _ {2} ^ {*}, \dots , \boldsymbol {\gamma} _ {| I _ {r} |} ^ {*} \right\} = \underset {\gamma_ {1}, \dots , \gamma_ {| I _ {r} |}} {\operatorname {a r g m i n}} \sum_ {i \in I _ {m}} t _ {m, i} + \sum_ {j \in I _ {r}} t _ {r, j} \tag {27}
$$

where $t _ { m , i } , t _ { r , j }$ are the travel time of the $i ^ { t h }$ mainline vehicle and the $j ^ { t h }$ on-ramp vehicle, respectively. 

To see the equivalency between (8) and (27), first we note that (8) is actually to maximize the speeds of all the vehicles over the whole cooperation zone. This is because in (8), although the time to complete the cooperative merging maneuver, $t _ { f }$ , is not pre-determined, but before this time, all the vehicles will try to stay close to the maximum speed, v˜, and after this time, all the vehicles will traverse the remained part of the cooperation zone at the maximum speed, v˜. On the other hand, (27) minimizes the total travel time of all the vehicles over the whole cooperation zone, which is equivalent to maximizing the speeds of all the vehicles over the whole cooperation zone. 

Note that (27) does not explicitly involve the continuous decision variables, $t _ { f }$ and $\pmb { \theta } _ { l , i }$ , but only the binary variables $\gamma _ { i }$ , $i \in I _ { r }$ , which will greatly simplify the following analysis. This is justified because, per the proposed optimal sequential search algorithm, to determine $\gamma _ { i } ^ { * }$ , $i \in I _ { r }$ , for every enumerated $\gamma _ { i }$ , $i \in I _ { r }$ , $t _ { f }$ and $\pmb { \theta } _ { l , i }$ will be solved from a nonlinear program to be explained in Section III-B., so the associated trajectory cost can be computed; $\gamma _ { i } ^ { * }$ will then be determined after all the enumerations. 

Now we utilize the characteristics of single-lane merging problem to derive a necessary condition for the optimality of (27). In below, we claim this necessary condition and then prove it. 

Proposition 1: The merge-in gap selection of an on-ramp vehicle can be optimal only if the merge-in gap selections of all the preceding on-ramp vehicles are optimal. That is, $\gamma _ { 1 } ^ { * } , \ldots , \gamma _ { p - 1 } ^ { * }$ is a necessary condition for $\gamma _ { p } ^ { * }$ , $\forall p \in I _ { r }$ . 

Proof: It is straightforward that after merging, mainline and on-ramp vehicles form a platoon, which means that at this time, the leading vehicle of an on-ramp vehicle is either its initial preceding on-ramp vehicle or a mainline vehicle, and the same goes for the leading vehicle of a mainline vehicle. Therefore, the relation between the travel time of two consecutive vehicles after merging is given by (28) and (29). 

$$
t _ {r, j + 1} = t _ {r, j} + \min  \left\{\tau , \tau_ {0} \right\} o r t _ {m, i} + \min  \left\{\tau , \tau_ {0} \right\} \tag {28}
$$

$$
t _ {m, i} = t _ {m, i - 1} + \min  \left\{\tau , \tau_ {0} \right\} o r t _ {r, j} + \min  \tau , \tau_ {0} \tag {29}
$$

where $\tau$ is the minimum allowable time gap; $\tau _ { 0 }$ is initial time gap between these two vehicles. (28) and (29) indicate that the travel time of a vehicle is dependent on its leading vehicle. Moreover, (28) consists of two cases. In the first case, the $j ^ { t h }$ on-ramp vehicle is the leading vehicle of the $j + 1 ^ { t h }$ on-ramp vehicle, and therefore, the optimal $\mathfrak { t } _ { r , j } , \mathfrak { t } _ { r , j } ^ { * }$ , is the necessary condition for $t _ { r , j + 1 } ^ { * }$ . In the second case, the leading vehicle is the $i ^ { t h }$ r, j 1mainline vehicle. Likewise, $t _ { r , j + 1 } ^ { * }$ requires $\mathfrak { t } _ { m , i } ^ { * }$ . Then, $\mathfrak { t } _ { m , i } ^ { * }$ implies $\mathfrak { t } _ { r , j } ^ { * }$ because the $j ^ { t h }$ on-ramp vehicle must be downstream of the $i ^ { t h }$ mainline vehicle, as reflected by (29). Therefore, in both cases, $t _ { r , j } ^ { * }$ is a necessary condition for ∗ ∗ $t _ { r , j + 1 } ^ { * }$ . r, jSimilarly, a necessary condition for $t _ { m , i + 1 } ^ { * }$ is $t _ { m , i } ^ { * }$ r, j 1. Based on the necessary condition and the assumption that $\gamma _ { 1 } ^ { * } , \ldots , \gamma _ { p - 1 } ^ { * }$ corresponds to minimum $\begin{array} { r } { \sum _ { i = 1 } ^ { | I _ { m } | } t _ { m , i } + \sum _ { j = 1 } ^ { p - 1 } t _ { r , j } } \end{array}$ P m i =1 tm,i + Pp−1 j =1 tr, j , we deduce that $\mathrm { t h e } \gamma _ { 1 } ^ { * } , \ldots , \gamma _ { p - 1 } ^ { * }$ p is a necessary condition for $\gamma _ { p } ^ { * }$ . Therefore, Proposition 1 holds. □ 

The above necessary condition leads to the proposed sequential searching algorithm, which iteratively solves problem (30) for each on-ramp vehicle, from the most downstream on-ramp vehicle to the most upstream on-ramp vehicle, to determine the optimal merging sequence and the trajectories. 

$$
\begin{array}{l} \widetilde {\boldsymbol {\gamma}} _ {1} ^ {*}, \dots , \widetilde {\boldsymbol {\gamma}} _ {p} ^ {*} = \underset {\gamma_ {1}, \dots , \gamma_ {p}} {\operatorname {a r g m i n}} \sum_ {i = 1} ^ {| I _ {m} |} t _ {m, i} + \sum_ {j = 1} ^ {p} t _ {r, j} \\ \text {s u b j e c t} \gamma_ {1} = \widetilde {\boldsymbol {\gamma}} _ {1} ^ {*}, \dots , \gamma_ {p - 1} = \widetilde {\boldsymbol {\gamma}} _ {p - 1} ^ {*}; \forall p \in I _ {r} \tag {30} \\ \end{array}
$$

Problem (30) can be considered as to determine the optimal merge-in gap of the $p ^ { t h }$ on-ramp vehicle, $\tilde { \gamma } _ { p } ^ { * }$ , conditioning on fixed $\tilde { \gamma } _ { 1 } ^ { * } , \ldots \tilde { \gamma } _ { p - 1 } ^ { * }$ . We have added “∼” over $\gamma _ { i } ^ { * }$ ,, $i \in I _ { r }$ to be rigorous, i.e. to honor the subtle fact that although problem (30) is the consequence of a necessary optimality condition of problem (27), but they are two different problems. 

In Appendix A, we offer an alternative way to show Proposition 1. 

# E. An Iterative LP Method for Solving the NLP Trajectory Planning Model

Integer variables are searched by above sequential searching algorithm, but each subproblem in the search tree is still nonlinear w.r.t. the continuous variables $\pmb { \theta } _ { l , i }$ and $t _ { f }$ . It can be observed that the cost function (8) and constraints (9)-(20) are linear combinations of nonlinear (3, 6, 7). However, (3, 6, 7) can be treated as linear functions with respect to $\pmb { \theta } _ { l , i }$ if $t _ { f }$ is known. Based on this point, each node in the search space can be seen as a LP problem when a feasible $t _ { f }$ is given. Therefore, 


TABLE II INTERACTIVE LINEAR PROGRAMMING METHOD


<table><tr><td colspan="2">Algorithm 2. An Iterative LP Method for Trajectory Optimization</td></tr><tr><td colspan="2">Input: A node δ in the search tree</td></tr><tr><td colspan="2">Output: Optimal time tf*; trajectories θl,i; cost value J* for node δ</td></tr><tr><td>1</td><td>k←0</td></tr><tr><td>2</td><td>Given a feasible tf0, solve δ to obtain J0.</td></tr><tr><td>3</td><td>Repeat</td></tr><tr><td>4</td><td>Given tfk, solve δ to obtain the θl,i k and the cost value J(tfk)</td></tr><tr><td>5</td><td>Given tfk+ε, solve δ to obtain the cost value J(tfk+ε)</td></tr><tr><td>6</td><td>dk←-(J(tfk+ε)-J(tfk))/ε</td></tr><tr><td>7</td><td>Pick step size αk according to the Armijo rule.</td></tr><tr><td>8</td><td>tfk+1←tfk+αkd</td></tr><tr><td>9</td><td>Given tfk+1, solve δ to obtain Jk+1</td></tr><tr><td>10</td><td>k←k+1</td></tr><tr><td>11</td><td>until |Jk-Jk-1|&gt;ξ</td></tr><tr><td>12</td><td>return tf*←tfk, θl,i*←θl,i, J*←Jk</td></tr></table>

the gradient descent method is adopted to iteratively update $t _ { f }$ . Concretely, the LP subproblem associated to the $t _ { f } ^ { k }$ in kth iteration is first solved to obtain the optimal $\pmb { \theta } _ { l , i } ^ { k }$ , and then the resulting objective value can provide gradient direction for the subsequent tk+1f $\check { t } _ { f } ^ { k + 1 }$ update. The detailed procedure to solve each subproblem is summarized in Table II. We can see that the gradient of objective function is calculated numerically, and the step size is determined with the Armijo rule. 

# IV. RECURSIVE IMPLEMENTATION FOR FEEDBACK

In practical implementation, it is crucial to deal with various disturbances that may occur, such as variations in vehicle speed or unexpected events such as vehicles abruptly changing lanes from other main lanes. Therefore, a feedback loop is necessary to deal with these disturbances. 

To this end, the trajectories of CAV groups that have passed the trigger point (TP) are updated periodically. Specifically, within a predefined update interval, denoted as $t _ { u p }$ , the proposed approach replans trajectories based on the updated surrounding vehicles information, including their positions and speeds. This process continues until the cooperative merge task is successfully completed. 

# V. NUMERICAL EXPERIMENTS

To evaluate the proposed methodology, the computational experiments are performed on a workstation (16 cores of CPUs; 3.2GHz). The mathematical models and algorithms proposed in this study are implemented in Python (CasADi). 

# A. Experimental Settings

Experiments are simulated in SUMO1.14, a microscopic traffic simulation tool. The SUMO internal model, the Wiedemann 99 model, is applied to simulate the car-following behavior. The adjusted driving behavior and vehicles’ parameter values are listed in Table III. All other parameters assume default values. 

As shown in Fig. 4, the simulated freeway segment consists of one mainline lane and one on-ramp. The mainline is 4.1 kilometers long, which contains a 2-kilometer ‘warm-up’ segment. The cooperation zone, which includes the merging 


TABLE III PARAMETER SETTING


<table><tr><td>Parameter</td><td>Value</td><td>Unit</td><td>Source</td></tr><tr><td>vf</td><td>120</td><td>km/h</td><td>[42]</td></tr><tr><td>a</td><td>2.75</td><td>m/s2</td><td>[43]</td></tr><tr><td>b</td><td>2.75</td><td>m/s2</td><td>[43]</td></tr><tr><td>s0</td><td>1.5</td><td>m</td><td>[41]</td></tr><tr><td>lv</td><td>4.37</td><td>m</td><td>[41]</td></tr><tr><td>τ</td><td>1.5</td><td>s</td><td>[41]</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/3a585ae631b8ae2cb0746bc7fdcc168bae5e239b1d55ea41b65acd08f48f3f9e.jpg)



Fig. 4. Road setting.


and preparation sections, is 800 meters long. The so-called preparation section is from the on-ramp node up to the position in the mainline as a mapping of the trigger point in the onramp. The downstream segment is 1.5 kilometers, so that affected road sections are fully covered. 

To evaluate the effectiveness of the proposed method, we test different combinations of mainline/on-ramp demand ratio and the total demand. The three tested mainline/on-ramp demand ratios are 4/1, 3/1, and 2/1. The four tested total demand values (1932, 2082, 2147, 2190) are respectively $90 \%$ , $9 7 \%$ , $100 \%$ , and $102 \%$ of the theoretical capacity. Therefore, in total there are 12 scenarios to be tested. The experiment for each scenario runs for one hour in SUMO. 

The proposed method is compared with three baseline methods to evaluate its performance: 

VROCP: the virtual rotation optimal control problem, which combines [15] and [46]. First, the merging sequence is determined by a heuristic first-in-first-out way, and then the optimization model from [15] is applied to generate optimal vehicle trajectories. 

FTOCP: the fixed-time optimal control problem from [23]. First, a vehicle sequence is determined using the FIFO method, and then trajectories are planned over a fixed merge time. 

MCTS-DA: Monte Carlo Tree Search-based decomposition algorithm to find the optimal vehicle sequence from [25]. The time-optimal merge sequence is obtained by repeatedly solving a mixed integer programming model using the MCTS method. 

# B. Cooperative Merging in the Presence of a Metering Signal

Ramp metering signal control (one-car-per-green) can make on-ramp vehicles arrive uniformly at the event trigger point to avoid inputting large disturbances to the mainline. Both the proposed approach and the benchmark method, VROCP, are tested assuming the presence of such a ramp metering signal control. The results are in Table IV. The third and fourth columns present travel delays of the two methods, respectively. The last column shows the percentage of reduction of delay. 

Table IV shows that the proposed approach has similar travel delay to VROCP when the mainline/on-ramp demand split ratio is 4:1. On the other hand, the proposed approach has significant improvement when the split ratio is 3:1 and 2:1. 


TABLE IV TOTAL TRAVEL DELAY COMPARISON WITH RAMP METERING


<table><tr><td>Mainline/ On-Ramp Demand Ratio</td><td>Total Demand (veh/hour)</td><td>Proposed D1(s)</td><td>VROCP D2(s)</td><td>D.I.</td></tr><tr><td>4:1</td><td>1932</td><td>828.4</td><td>832.5</td><td>0.5%</td></tr><tr><td>4:1</td><td>2082</td><td>886.1</td><td>909.8</td><td>2.6%</td></tr><tr><td>4:1</td><td>2147</td><td>915.2</td><td>922.9</td><td>0.8%</td></tr><tr><td>4:1</td><td>2190</td><td>938.0</td><td>948.5</td><td>1.1%</td></tr><tr><td>3:1</td><td>1932</td><td>912.1</td><td>918.7</td><td>0.7%</td></tr><tr><td>3:1</td><td>2082</td><td>1115.3</td><td>1244.3</td><td>10.4%</td></tr><tr><td>3:1</td><td>2147</td><td>1182.8</td><td>1310.8</td><td>9.8%</td></tr><tr><td>3:1</td><td>2190</td><td>1226.3</td><td>1413.3</td><td>13.2%</td></tr><tr><td>2:1</td><td>1932</td><td>956.0</td><td>956.57</td><td>0%</td></tr><tr><td>2:1</td><td>2082</td><td>1182.8</td><td>2432.3</td><td>51.4%</td></tr><tr><td>2:1</td><td>2147</td><td>2981.8</td><td>4048.2</td><td>26.3%</td></tr><tr><td>2:1</td><td>2190</td><td>3362.4</td><td>4212.7</td><td>20.2%</td></tr></table>


Note:(1) $D _ { 1 }$ and $D _ { 2 }$ refer to total travel delay by the proposed approach and VROCP,respectively;(2) D.I.refers to delay improvement and is defined as $\begin{array} { r } { D _ { \bullet } I _ { \bullet } : = \frac { D _ { 2 } - D _ { 1 } } { D _ { 2 } } } \end{array}$ D2 


When the ratio is 4:1, on-ramp vehicles are sparsely distributed. There is little mutual influence between on-ramp vehicles, and adjacent on-ramp vehicles do not affect the choice of each other’s facilitating mainline vehicles. The proposed approach chooses the same merging sequence, i.e., FIFO as VROCP does. Therefore, both methods yield similar delays. 

When the on-ramp demand is high, with a ratio of 2:1, intense interactions occur. This means that the arrival of the following on-ramp vehicles coincides with the ongoing merging and deceleration process of the preceding on-ramp and mainline vehicles. As a result, more severe slowdowns and a significant increase in delay occurs. 

In this intensive interaction scenario, the delay improvement $( D . I . )$ becomes much more evident, due to the multi-vehicle cooperation advantage of the proposed model. More specifically, the proposed model considers cooperation between two streams of vehicles, rather than just one on-ramp vehicle merging into two mainline vehicles. For example, a facilitating mainline vehicle can create a large gap to accommodate multiple on-ramp merging vehicles as a group to minimize the overall delay. 

# C. Cooperative Merging Without a Metering Signal

Without metering control, on-ramp vehicles arrive at the on-ramp randomly, so they may form a big disturbance to the mainline traffic. In this case, we also compare the proposed approach with VROCP under the same traffic conditions. 

From Table V, we see that travel delay increases both as the inflow demand increases and as the number of on-ramp vehicles increases. Also, the proposed approach has at least an $11 \%$ improvement over the baseline under any condition. Moreover, when the split ratio is 2:1, VROCP would even lead to collisions because it only considers the leading mainline vehicle and ignores the leading on-ramp vehicle when planning trajectories. 

In addition to delay reduction, the proposed approach also reduces the variation of speed (VS). High VS is found to 


TABLE V TOTAL TRAVEL DELAY COMPARISON WITHOUT RAMP METERING


<table><tr><td>Mainline/ On-Ramp Demand Ratio</td><td>Total Demand (veh/hour)</td><td>Proposed D1(s)</td><td>VROCP D2(s)</td><td>D.I.</td></tr><tr><td>4:1</td><td>1932</td><td>1658.1</td><td>1958.1</td><td>15.3%</td></tr><tr><td>4:1</td><td>2082</td><td>1866.7</td><td>2203.1</td><td>15.3%</td></tr><tr><td>4:1</td><td>2147</td><td>1916.9</td><td>2242.6</td><td>14.5%</td></tr><tr><td>4:1</td><td>2190</td><td>2008.3</td><td>2366.3</td><td>15.1%</td></tr><tr><td>3:1</td><td>1932</td><td>2061.3</td><td>2355.4</td><td>12.5%</td></tr><tr><td>3:1</td><td>2082</td><td>2704.1</td><td>3065.1</td><td>11.8%</td></tr><tr><td>3:1</td><td>2147</td><td>2976.2</td><td>3484.7</td><td>14.6%</td></tr><tr><td>3:1</td><td>2190</td><td>3150.1</td><td>3590.7</td><td>12.3%</td></tr><tr><td>2:1</td><td>1932</td><td>1989.5</td><td>Failure</td><td>—</td></tr><tr><td>2:1</td><td>2082</td><td>3199.7</td><td>Failure</td><td>—</td></tr><tr><td>2:1</td><td>2147</td><td>4235.4</td><td>Failure</td><td>—</td></tr><tr><td>2:1</td><td>2190</td><td>4962.9</td><td>Failure</td><td>—</td></tr></table>


Note: (1) $D _ { 1 } , D _ { 2 }$ refer to total travel delay; (2 $\begin{array} { r } { { \stackrel { } { ) } } D _ { \bullet } I _ { \bullet } : = \frac { D _ { 2 } - D _ { 1 } } { D _ { 2 } } } \end{array}$ D2 


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/e75709cfd58d596b24d8e56aba96ba23ada2d1eda846826c5d28901627a607c0.jpg)



Fig. 5. Speed contour in the mainline: (a) with SUMO default control; (b) with the proposed approach.


be a precursor of collision accidents [44], [45]. To illustrate the improvement in VS achieved by the proposed approach, we compare the speed contour achieved by the proposed approach with the speed contour achieved by the SUMO default control. The evaluation time-space region is specified as [1800, 2500] $\sec \times [ 1 5 0 0 , 3 5 0 0 ] \mathrm { m } .$ . 

Fig. 5 (a) is the speed contour of the SUMO default control. The intersection of mainline and ramp is at $2 . 0 \mathrm { k m }$ , and we can observe that speed fluctuation starts from here and extends to the downstream, with significant velocity drops at 1900 and 2350 seconds. Fig. 5 (b) presents the speed contour plot of the proposed approach. We see that deceleration occurs at $1 . 5 \mathrm { k m }$ since the event trigger point is set there. Obviously, the proposed approach can mitigate speed variance. As a result, VS and travel delays are all reduced. 

In addition to traffic efficiency, we validate that the proposed approach guarantees CTH rules since safety is an essential consideration. Fig. 6 shows the time gap statistics for all CAVs at multiple locations on the mainline in a one-hour simulation period. Fig. 6 (a) illustrates time gap distributions under the SUMO default behavior, and we can observe that time gaps downstream of the $2 . 0 \ \mathrm { k m }$ location are much less than the desired time gap (1.5s) and even close to 0, which is risky and unreasonable. On the contrary, under the control of the proposed approach, time gaps can always be no less than the desired gap as shown in Fig. 6 (b). Fig. 6 (b) also 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/5686d2d1271b4d3f08a8dcc3bbaa27bd36a5151a71aa2b50a94fd0982199eeab.jpg)



Fig. 6. Time gap distribution in the mainline: (a) with SUMO default control; (b) with the proposed approach.


indicates that before vehicles drive through the trigger point (at $1 . 5 \ \mathrm { k m }$ location), the initial time gaps are concentrated around 2.2 seconds. Over the coordination zone, i.e., from $1 . 5 \ \mathrm { k m }$ to $2 ~ \mathrm { k m }$ , some of the time gaps increase to between 3 and 4 seconds, which corresponds to the slowing down of the facilitating mainline vehicles to generate gaps for the on-ramp traffic; downstream of the $2 . 0 \ \mathrm { k m }$ location, the gaps reduce to around 1.5 seconds because the on-ramp merging vehicles have merged into the mainline. 

# D. Analyses on Vehicles’ Trajectories

One advantage of the proposed model is the ability to allow multiple on-ramp vehicles to merge into the gap between two mainline vehicles rather than to allow only one onramp vehicle, which can be clearly demonstrated by plotting individual trajectories. 

As shown in Fig. 7 (a), the second and third on-ramp vehicles choose to merge in between the second and the third mainline vehicles when the initial positions of these two on-ramp vehicles are exactly between these two mainline vehicles, and there is not much difference in all vehicles’ velocities. The third mainline vehicle carries out a larger slowdown to generate a larger gap. However, as illustrated by Fig. 8 (a), the third on-ramp vehicle merges behind the third mainline vehicle when the initial speed of the third on-ramp vehicle is low. This is reasonable because when the initial speed of a merging vehicle is close to mainline vehicles’ speed, if a far upstream mainline vehicle is selected as a facilitating vehicle, the on-ramp merging vehicle will have to wage an extra deceleration and then acceleration in order to wait for the arrival of the mainline facilitating vehicle. Thus, nearby mainline vehicles should be chosen. Conversely, when the initial speed of a merging vehicle is low, choosing a nearby mainline vehicle to generate a gap would cause significant speed drop of facilitating and its following vehicles. Consequently, a relatively more upstream mainline vehicle should be selected, and the on-ramp vehicle could accelerate first to mitigate this negative effect. Reference [46]’s 


TABLE VI SAFETY AND DELAY COMPARISON WITH DIFFERENT COOPERATION RANGES


<table><tr><td rowspan="2">Cooperation Zone [m]</td><td colspan="2">Proposed</td><td colspan="2">VROCP</td></tr><tr><td>τ[s]</td><td>D[s]</td><td>τ[s]</td><td>D[s]</td></tr><tr><td>350</td><td>1.50</td><td>1186.95</td><td>1.66</td><td>1311.78</td></tr><tr><td>325</td><td>1.50</td><td>1292.37</td><td>1.47</td><td>1714.62</td></tr><tr><td>300</td><td>1.50</td><td>1998.20</td><td>Failure</td><td>Failure</td></tr></table>


Note: (1) T refers to mean time gap; (2) D refers to total travel delay. 


results drew similar conclusions: When the on-ramp vehicle’s speed is low, it would merge to the back of mainline platoon. When the on-ramp vehicle’s speed gets close to mainline vehicles’ speeds, the mainline vehicle close to the initial position of the merging vehicle is selected. Speed profiles, shown in Fig. 7 (b) and 8 (b), are parabolic or linear, because we describe the trajectory by cubic polynomial functions. Similarly, acceleration trajectories, shown in Fig. 7 (c) and 8 (c), are linear or constant. The upper and lower limits of the state variable velocity and the control input acceleration are always obeyed at any time instant. 

# E. The Effect of the Length of the Cooperation Zone

We are interested in the impact of different lengths of the cooperative zone on ramp merging. Thus, we test the safety and traffic efficiency of our proposed model and the baseline model under a 350-meter-long, 325-meter-long, and 300-meter-long zone (including the acceleration lane), respectively. Table VI summarizes the average time gap between merging and facilitating vehicles, and the total travel delay, resulting from the proposed approach and VROCP, under different lengths of the cooperation zone. 

From Table VI, we see that the baseline method, i.e., VROCP, achieves desired time gap (no less than 1.5 seconds) when the cooperation zone is sufficiently long $( 3 5 0 \mathrm { m } )$ . However, when the zone reduces to $3 2 5 \mathrm { m }$ , VROCP cannot guarantee the safe time gap anymore and significantly increases travel delay. Moreover, VROCP would lead to accidents when the zone further reduces to $3 0 0 \mathrm { m }$ . In contrast, the proposed approach still ensures the target time gap even when the zone is so short that the baseline fails. Inevitably, travel delay would increase as zone shortens. 

The reason why the proposed approach can ensure safety in the limited ramp length case is that we formulate the constant time headway rule for terminal spacing between vehicles as hard constraints, while the baseline method puts the terminal spacing between on-ramp vehicles and facilitating vehicles in the objective function, which leads to unsafe solution in restricted scenarios. Furthermore, when the cooperation zone is short, the cooperation pair chosen by FIFO cannot generate enough space for merging, but in contrast, the proposed approach can choose an upstream mainline vehicle to generate a feasible gap in advance albeit at the cost of on-ramp vehicles’ delay. 

# F. The Effect of Weighting Factors

The effect of weighting factors, i.e. $w _ { m }$ and $w _ { r }$ , on travel delay is investigated. Five combinations of $( w _ { m } , w _ { r } )$ are 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/e9a61935c6a1ab046dd0cba5482e7bff23311872eb4d11965ed2a3b17345ba25.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/152489a532e1e2e6c13dca2ccf246dd64a96a0a42445b560a940ce35d641b2c6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/1159440eed2bc80823f5d76c6dd92a11b061c0d4d420ae48e03e53ebcef4601f.jpg)



Fig. 7. Vehicle trajectories for the high on-ramp vehicle’s speed scenario: (a) positions; (b) speeds; (c) acceleration.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/58142775083be8456dffea812582f27df40cecc4e17abc357aa8a48e8d36d47c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/14f63d7661efc520aaf1c349a2f734bfe850769e239e45a5c26b40fafdb5cec9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/5d66166333ff477dfda3db24047c2888c22f5a66ea1b9a372713a43b3fc54752.jpg)



Fig. 8. Vehicle trajectories for the low on-ramp vehicle’s speed scenario: (a) positions; (b) speeds; (c) acceleration.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/7fb8b1e3aea89ba19bbf1e09ebf1acc3ecb11f536ceca80ece1ad97b47b099d4.jpg)



Fig. 9. Travel delay under different combinations of $( w _ { m } , w _ { r } )$ .


tested: (0.1, 0.9), (0.3, 0.7), (0.5, 0.5), (0.7, 0.3) and (0.9, 0.1). A total of 300 mainline and 150 on-ramp CAVs enter the simulation within 15 minutes. 

As shown in Fig. 9, increasing $w _ { m }$ can reduce the delay of mainline CAVs. Similarly, increasing $w _ { r }$ reduces the delay of on-ramp CAVs. In addition, when $w _ { m }$ is equal to $w _ { r }$ , the objective is to minimize the delay of all CAVs, and therefore the minimum total delay of all CAVs is obtained under the case. 

# G. Computational Efficiency

The computation time of different numbers of mainline vehicles and on-ramp vehicles is tested. The tested numbers of mainline vehicles are 1, 5, 10, 15, and 20, and the tested numbers of on-ramp vehicles are 1, 2, and 3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/ed3448f192d4d8796aaa22e2a76d250999ebf20d643242ef2a0b07ac5eda78b8.jpg)



Fig. 10. Computation time of various mainline and on-ramp CAVs number.


As a result, Fig. 10. shows that with 20 mainline vehicles and 1 on-ramp vehicle, the computation time is 0.63 seconds. With 20 mainline vehicles and 2 on-ramp vehicles, the computation time increases to 1.1 seconds. Similarly, with 20 mainline vehicles and 3 on-ramp vehicles, the computation time increases further to 1.8 seconds. 

We can see that the proposed method can handle a large number of mainline vehicles within 1 second, but the computation time increases quickly as the number of on-ramp vehicles increases. This result is consistent with the analysis of the search space of the vehicle sequences in Section III-B. That is, the search space is $( | I _ { m } | + 1 ) ^ { | I _ { r } | }$ . As the number of on-ramp vehicles increases, the size of the search space grows exponentially. This means that increasing the number of vehicles on the ramp will have a greater impact on the computation time. Nevertheless, in most practical ramp merge 


TABLE VII PERFORMANCE COMPARISON OF THE PROPOSED APPROACH AGAINST THREE ALTERNATIVE METHODS ON REAL DATASET


<table><tr><td></td><td>Proposed</td><td>MCTS-DA</td><td>VROCP</td><td>FTOCP</td></tr><tr><td>D(s)</td><td>469</td><td>469</td><td>562</td><td>666</td></tr><tr><td>Dm(s)</td><td>285</td><td>285</td><td>411</td><td>456</td></tr><tr><td>C(s)</td><td>13.9</td><td>441</td><td>5.9</td><td>3.9</td></tr></table>


Note: (1) D refers to total delay of all vehicles; (2) $D _ { m }$ refers to total delay of mainline vehicles;(3) C refers to total computation time. 


scenarios, the number of ramp vehicles is usually less than the number of mainline vehicles. 

# H. Real-World Data Validation

The proposed method is validated using real-world data from the Next Generation Simulation (NGSIM) Open Data, specifically the Interstate 80 (I-80) Freeway Dataset [47], which contains ramp merge scenarios. We extract both on-ramp vehicles and the rightmost mainline vehicles from the I-80 dataset, resulting in a total of 850 vehicles observed over a 45-minute period. These vehicles enter the simulation with the initial position and speed provided by the dataset and then are guided through the cooperative merging zone under the control of the following different methods: the proposed approach and the three alternative methods for comparison, namely, MCTS-DA, VROCP, and FTOCP. We compare the performance of the proposed approach with these alternative methods in terms of travel delay and total computation time. 

As shown in Table VII, the proposed approach outperforms the three alternatives. Specifically, the proposed approach achieves the same total travel delay as MCTS-DA, which can also obtain the time-optimal vehicle sequence by enumerating all vehicle sequences and repeatedly solving a MILP model to obtain the travel time of vehicles. However, the proposed approach requires way less computation time than MCTS-DA thanks to the reduced search space of the proposed method. The other two alternatives, VROCP and FTOCP, spend less total computation time, but their travel delays are larger because they do not allow for flexible merging sequence and merging time, respectively. In addition, the lower total delay of mainline vehicles shows that the better merging sequence mitigates the impact of on-ramp vehicles on mainline traffic. In the 45-minute traffic simulation, the accumulated total computation time differences between the proposed method and these two alternative methods are 8 seconds and 10 seconds respectively, but during this time, each method is triggered and solved for many times, and the single computation time difference is only at the magnitude of 0.1 seconds on average. 

# I. Impact of Human-Driven Vehicles on CAVs

We use a real lane-changing trajectory of a human-driven vehicle (HDV), followed by two mainline CAVs and an onramp CAV. Every 0.5 seconds, the model would re-plan these three CAVs based on the updated information of the humandriven vehicle. At each replanning step, the future speed of the human-driven vehicle is assumed to remain its current speed, a typical treatment in relevant studies. The below results show 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/c29fedeef9304ed98d0fc16c191d3f230dbf63fca092381ec24917ecedd349ae.jpg)



Fig. 11. Merging speed profile for the unexpected lane change.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/4ec97781d7ef869b9d37cd1c391a9c0fe4e6451b429dcd9f8a00ab2d80f03e60.jpg)



Fig. 12. Merging position profile for the unexpected lane change.


that the proposed approach successfully fulfilled the merging task under the influence of an uncontrolled, perturbing HDV. 

As depicted in Fig.11, the human driver initiates the lane change at a higher speed than the vehicles in the target lane and then gradually reduces the speed back to normal. 

The following mainline CAV first reduces speed slightly and then gradually accelerates to achieve the desired spacing with the leading human-driven vehicle. Similarly, the merging CAV also undergoes a noticeable deceleration to achieve sufficient merging distances (33m) to the leading and following mainline CAVs, respectively. Eventually, the speeds of all the CAVs reach the steady-state speed of the leading human-driven vehicle. 

# VI. CONCLUSION

In this paper, we modelled the task of cooperative merging of an on-ramp CAV stream and a mainline CAV stream at a freeway on-ramp merging section as a mixed integer nonlinear programming problem that guarantees safety and enjoys high-quality vehicle trajectories. The total travel delay is minimized by simultaneously optimizing the merging sequence and the continuous-time vehicle trajectories. Such a treatment can avoid generating a merging sequence that would result in infeasible or low-quality trajectories. Moreover, the merging positions and time are outcomes of the optimization model rather than heuristically pre-defined. In addition, trajectories are described in continuous-time form so that safety is guaranteed at any time. 

To efficiently solve the proposed MINLP model, on-ramp merging vehicles’ optimal merge-in gaps are determined one 

by one. This sequential search process was built based on a necessary condition of optimality of the proposed MINLP model which we identified and proved. Therefore, the sequential search process can generate the true optimal merging sequence, that is, the one that is obtained by considering all the on-ramp merging vehicles together. Thanks to the sequential feature, the search space is significantly reduced. Subproblems are NLP and are efficiently solved by the iterative LP method to generate planned trajectories. 

The traffic efficiency, safety and computational efficiency of the proposed approach are demonstrated under different traffic conditions and compared with three alternative methods on the NGSIM dataset. In addition, the impact of the length of the cooperative zone and the weighting factors on the traffic efficiency and safety is investigated. The computational efficiency is also evaluated. Furthermore, the proposed method is implemented in a feedback loop to complete the cooperative merging task under a real HDV trajectory. 

As a future endeavor, it is desirable to extend the current method to multiple-lane scenarios, where lane changing behaviors of mainline vehicles will be considered in the cooperative on-ramp merging. Second, the assumption of $100 \%$ CAVs can be relaxed to accommodate a mixed traffic condition by predicting human drivers’ trajectories. Third, the combination of microscopic trajectory generation methods and flow-based merging control methods appear to be promising in mitigating congestion and may deserve further examination. 

# APPENDIX A

# DIRECT DEDUCTION OF PROPOSITION 1

All on-ramp vehicles are split into two groups: $\{ 1 ^ { s t } , \ldots , k ^ { t h } \}$ on-ramp vehicles and $\left\{ k + 1 ^ { t h } , \ldots , \mathsf { | } I _ { r } | ^ { \bar { t } h } \right\}$ on-ramp vehicles. Correspondingly, the mainline vehicles can be two associated groups: $1 ^ { s t } , \ldots , n ^ { t h } \}$ mainline vehicles and $\big \{ n + 1 ^ { t h } , \dots , | I _ { m } | ^ { \bar { t } h } \big \}$ mainline vehicles. Note that the $n ^ { t h }$ mainline vehicle refers to the one in front of the $k ^ { t h }$ on-ramp vehicle, although the “n” is unknown. 

Minimizing the first group of on-ramp and mainline vehicles can be written as: 

$$
\min  _ {\gamma_ {1}, \dots , \gamma_ {| I r |}} \left(\sum_ {j = 1} ^ {k} t _ {r, j} + \sum_ {i = 1} ^ {n} t _ {m, i}\right) \tag {A.1}
$$

Then, it is straightforward that the decision variables $\gamma _ { k + 1 } , \ldots , \gamma _ { | I _ { r } | }$ do not affect (A.1). Hence, (A.1) can be express as (A.2). 

$$
\begin{array}{l} \min  _ {\gamma_ {1}, \dots , \gamma_ {k}} \left(\sum_ {j = 1} ^ {k} t _ {r, j} + \sum_ {i = 1} ^ {n} t _ {m, i}\right) \\ = t _ {r, 1} ^ {*} + \dots + t _ {r, k} ^ {*} + t _ {m, 1} ^ {*} + \dots + t _ {m, n} ^ {*} \tag {A.2} \\ \end{array}
$$

Similarly, minimizing another group of on-ramp and mainline vehicles can be written as (A.3) and can be extended as (A.6): 

$$
\begin{array}{l} \min  _ {\gamma_ {1}, \dots , \gamma_ {| I r |}} \left(\sum_ {j = k + 1} ^ {| I _ {r} |} t _ {r, j} + \sum_ {i = n + 1} ^ {| I _ {m} |} t _ {m, i}\right) \tag {A.3} \\ = \min  _ {\gamma_ {1}, \dots , \gamma_ {| I _ {r} |}} \left[ \sum_ {j = k + 1} ^ {| I _ {r} |} \left(\Delta t _ {r, j} + \min  _ {\gamma_ {1}, \dots , \gamma_ {k}} t _ {r, k}\right) + \sum_ {i = n + 1} ^ {| I _ {m} |} (\Delta \right. \\ \end{array}
$$

$$
\begin{array}{l} \left. \times t _ {m, i} + \min  _ {\gamma_ {1}, \dots , \gamma_ {k}} t _ {m, n}\right) \Bigg ] (A.4) \\ = \min  _ {\gamma_ {1}, \dots , \gamma_ {| I r |}} \left[ \sum_ {j = k + 1} ^ {| I _ {r} |} \left(\Delta t _ {r, j} + t _ {r, k} ^ {*}\right) + \sum_ {i = n + 1} ^ {| I _ {m} |} \left(\Delta t _ {m, i} + \right. \right. \\ \left. \times t _ {m, n} ^ {*}\right) \Bigg ] (A.5) \\ = \min  _ {\gamma_ {k + 1}, \dots , \gamma_ {| I _ {r} |}} \left[ \sum_ {j = k + 1} ^ {| I _ {r} |} \left(\Delta t _ {r, j} + t _ {r, k} ^ {*}\right) + \sum_ {i = n + 1} ^ {| I _ {m} |} \left(\Delta t _ {m, i} + \right. \right. \\ \left. \times t _ {m, n} ^ {*}\right) \Bigg ] (A.6) \\ = t _ {r, k + 1} ^ {*} + \dots + t _ {r, | I _ {r} |} ^ {*} + t _ {m, n + 1} ^ {*} + \dots + t _ {m, | I _ {m} |} ^ {*} (A.7) \\ \end{array}
$$

where $\Delta t _ { r , j }$ and $\Delta t _ { m , i }$ are the part of time delay of the $j ^ { t h }$ onramp vehicle and $i ^ { t h }$ mainline vehicle caused by the on-ramp vehicles after the $k ^ { t h }$ on-ramp vehicle, respectively. 

From (A.6), we can see that the optimal time of following vehicles, i.e., requires the o $t _ { r , k + 1 } ^ { * } + \ldots + t _ { r , | I _ { r } | } ^ { * }$ t ∗ and eding $t _ { m , n + 1 } ^ { * } + \ldots + t _ { m , | I _ { m } | } ^ { * }$ m,n+1 ∗ $t _ { r , k } ^ { * }$ $t _ { m , n } ^ { * }$ Therefore, Proposition 1 is obtained. 

# APPENDIX B DERIVATION OF EQUATION (6)

The polynomial position equation in (3) can be transformed as follows: 

$$
\begin{array}{l} x (t) = \theta_ {3} \cdot t ^ {3} + \theta_ {2} \cdot t ^ {2} + \theta_ {1} \cdot t + \theta_ {0} \\ = t _ {f} ^ {3} \theta_ {3} \left(\frac {t}{t _ {f}}\right) ^ {3} + t _ {f} ^ {2} \theta_ {2} \left(\frac {t}{t _ {f}}\right) ^ {2} + t _ {f} \theta_ {1} \frac {t}{t _ {f}} + \theta_ {0}, \frac {t}{t _ {f}} \in (0, 1 ] \tag {B.1} \\ \end{array}
$$

The related three order Bézier curve can be expanded as follows: 

$$
\begin{array}{l} P ^ {x} (s) \\ = \sum_ {j = 0} ^ {3} B _ {j} ^ {3} (s) P _ {j} ^ {x} \\ = B _ {0} ^ {3} (s) P _ {0} ^ {x} + B _ {1} ^ {3} (s) P _ {1} ^ {x} + B _ {2} ^ {3} (s) P _ {2} ^ {x} + B _ {3} ^ {3} (s) P _ {3} ^ {x} \\ = (1 - s) ^ {3} P _ {0} ^ {x} + 3 s (1 - s) ^ {2} P _ {1} ^ {x} + 3 s ^ {2} (1 - s) P _ {2} ^ {x} + s ^ {3} P _ {3} ^ {x} \\ = \left(P _ {3} ^ {x} - 3 P _ {2} ^ {x} + 3 P _ {1} ^ {x} - P _ {0} ^ {x}\right) s ^ {3} + \left(3 P _ {2} ^ {x} - 6 P _ {1} ^ {x} + 3 P _ {0} ^ {x}\right) s ^ {2} \\ + \left(3 P _ {1} ^ {x} - 3 P _ {0} ^ {x}\right) s + P _ {0} ^ {x}, s \in [ 0, 1 ] \tag {B.2} \\ \end{array}
$$

Then, a set of equations can be written to build the relationship between $\pmb \theta$ and $P ^ { x }$ . 

$$
\left\{ \begin{array}{l l} P _ {3} ^ {x} - 3 P _ {2} ^ {x} + 3 P _ {1} ^ {x} - P _ {0} ^ {x} = t _ {f} ^ {3} \theta_ {3} & \\ 3 P _ {2} ^ {x} - 6 P _ {1} ^ {x} + 3 P _ {0} ^ {x} = t _ {f} ^ {2} \theta_ {2} & \\ 3 P _ {1} ^ {x} - 3 P _ {0} ^ {x} = t _ {f} \theta_ {1} & \\ P _ {0} ^ {x} = \theta_ {0} & \end{array} \right. \tag {B.6}
$$

By solving (B.3)–(B.6), Equation (6) is derived. 

# A. Derivation of Equation (7)

Similarly, the polynomial velocity equation in (3) can be transformed as follows: 

$$
\begin{array}{l} v (t) = 3 \theta_ {3} \cdot t ^ {2} + 2 \theta_ {2} \cdot t + \theta_ {1} = 3 \theta_ {3} t _ {f} ^ {2} \left(\frac {t}{t _ {f}}\right) ^ {2} \\ + 2 \theta_ {2} t _ {f} \frac {t}{t _ {f}} + \theta_ {1}, \frac {t}{t _ {f}} \in (0, 1 ] \tag {B.7} \\ \end{array}
$$

The related two order Bézier curve can be expanded as follows: 

$$
\begin{array}{l} P ^ {v} (s) = \sum_ {j = 0} ^ {2} B _ {j} ^ {2} (s) P _ {j} ^ {v} = B _ {0} ^ {2} (s) P _ {0} ^ {v} + B _ {1} ^ {2} (s) P _ {1} ^ {v} + B _ {2} ^ {2} (s) P _ {2} ^ {v} \\ = \left(P _ {0} ^ {v} - 2 P _ {1} ^ {v} + P _ {2} ^ {v}\right) s ^ {2} + \left(2 P _ {1} ^ {v} - 2 P _ {0} ^ {v}\right) s + P _ {0} ^ {v} \\ \end{array}
$$

Then, a set of equations can be written as: 

$$
\left\{ \begin{array}{l} P _ {0} ^ {v} - 2 P _ {1} ^ {v} + P _ {2} ^ {v} = 3 \theta_ {3} t _ {f} ^ {2} \\ 2 P _ {1} ^ {v} - 2 P _ {0} ^ {v} = 2 \theta_ {2} t _ {f} \\ P _ {0} ^ {v} = \theta_ {1} \end{array} \right. \tag {B.10}
$$

By solving (B.8)–(B.10), Equation (7) is derived. 

# REFERENCES



[1] Y. Xiao, N. Coulombel, and A. D. Palma, “The valuation of travel time reliability: Does congestion matter?” Transp. Res. B, Methodol., vol. 97, pp. 113–141, Mar. 2017, doi: 10.1016/j.trb.2016.12.003. 





[2] Y. He, Z. Liu, X. Zhou, and B. Zhong, “Analysis of urban traffic accidents features and correlation with traffic congestion in large-scale construction district,” in Proc. Int. Conf. Smart Grid Electr. Autom. (ICSGEA), May 2017, pp. 641–644. 





[3] K. Zhang, S. Batterman, and F. Dion, “Vehicle emissions in congestion: Comparison of work zone, rush hour and free-flow conditions,” Atmos. Environ., vol. 45, no. 11, pp. 1929–1939, Apr. 2011, doi: 10.1016/j.atmosenv.2011.01.030. 





[4] J. Rios-Torres and A. A. Malikopoulos, “A survey on the coordination of connected and automated vehicles at intersections and merging at highway on-ramps,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 5, pp. 1066–1077, May 2017, doi: 10.1109/TITS.2016.2600504. 





[5] M. Wang, W. Daamen, S. P. Hoogendoorn, and B. van Arem, “Connected variable speed limits control and car-following control with vehicle-infrastructure communication to resolve stop-and-go waves,” J. Intell. Transp. Syst., vol. 20, no. 6, pp. 559–572, Nov. 2016, doi: 10.1080/15472450.2016.1157022. 





[6] A. Talebpour and H. S. Mahmassani, “Influence of connected and autonomous vehicles on traffic flow stability and throughput,” Transp. Res. C, Emerg. Technol., vol. 71, pp. 143–163, Oct. 2016, doi: 10.1016/j.trc.2016.07.007. 





[7] B. van Arem, C. J. G. van Driel, and R. Visser, “The impact of cooperative adaptive cruise control on traffic-flow characteristics,” IEEE Trans. Intell. Transp. Syst., vol. 7, no. 4, pp. 429–436, Dec. 2006, doi: 10.1109/TITS.2006.884615. 





[8] J. Rios-Torres and A. A. Malikopoulos, “Impact of partial penetrations of connected and automated vehicles on fuel consumption and traffic flow,” IEEE Trans. Intell. Vehicles, vol. 3, no. 4, pp. 453–462, Dec. 2018, doi: 10.1109/TIV.2018.2873899. 





[9] J. Sun and J. Sun, “Investigating the oscillation characteristics and mitigating its impact with low-penetration connected and automated vehicles,” in Proc. 21st Int. Conf. Intell. Transp. Syst. (ITSC), Nov. 2018, pp. 2339–2345. 





[10] Z. Wang, Y. Bian, S. E. Shladover, G. Wu, S. E. Li, and M. J. Barth, “A survey on cooperative longitudinal motion control of multiple connected and automated vehicles,” IEEE Intell. Transp. Syst. Mag., vol. 12, no. 1, pp. 4–24, Spring 2020, doi: 10.1109/MITS.2019.2953562. 





[11] L. Li, D. Wen, and D. Yao, “A survey of traffic control with vehicular communications,” IEEE Trans. Intell. Transp. Syst., vol. 15, no. 1, pp. 425–432, Feb. 2014, doi: 10.1109/TITS.2013.2277737. 





[12] B. Häfner, V. Bajpai, J. Ott, and G. A. Schmitt, “A survey on cooperative architectures and maneuvers for connected and automated vehicles,” IEEE Commun. Surveys Tuts., vol. 24, no. 1, pp. 380–403, 1st Quart., 2022, doi: 10.1109/COMST.2021.3138275. 





[13] C. Frese and J. Beyerer, “A comparison of motion planning algorithms for cooperative collision avoidance of multiple cognitive automobiles,” in Proc. IEEE Intell. Veh. Symp., Jun. 2011, pp. 1156–1162, doi: 10.1109/IVS.2011.5940489. 





[14] I. A. Ntousakis, I. K. Nikolos, and M. Papageorgiou, “Optimal vehicle trajectory planning in the context of cooperative merging on highways,” Transp. Res. C, Emerg. Technol., vol. 71, pp. 464–488, Oct. 2016, doi: 10.1016/j.trc.2016.08.007. 





[15] Y. Zhou, M. E. Cholette, A. Bhaskar, and E. Chung, “Optimal vehicle trajectory planning with control constraints and recursive implementation for automated on-ramp merging,” IEEE Trans. Intell. Transp. Syst., vol. 20, no. 9, pp. 3409–3420, Sep. 2019, doi: 10.1109/TITS.2018.2874234. 





[16] Y. Zhou, E. Chung, A. Bhaskar, and M. E. Cholette, “A stateconstrained optimal control based trajectory planning strategy for cooperative freeway mainline facilitating and on-ramp merging maneuvers under congested traffic,” Transp. Res. C, Emerg. Technol., vol. 109, pp. 321–342, Dec. 2019, doi: 10.1016/j.trc.2019.10.017. 





[17] J. Nilsson, M. Brännström, J. Fredriksson, and E. Coelingh, “Longitudinal and lateral control for automated yielding maneuvers,” IEEE Trans. Intell. Transp. Syst., vol. 17, no. 5, pp. 1404–1414, May 2016, doi: 10.1109/TITS.2015.2504718. 





[18] M. Karimi, C. Roncoli, C. Alecsandru, and M. Papageorgiou, “Cooperative merging control via trajectory optimization in mixed vehicular traffic,” Transp. Res. C, Emerg. Technol., vol. 116, Jul. 2020, Art. no. 102663, doi: 10.1016/j.trc.2020.102663. 





[19] Q. Xu and R. Sengupta, “Simulation, analysis, and comparison of ACC and CACC in highway merging control,” in Proc. IEEE IV Intell. Vehicles Symp., Jun. 2003, pp. 237–242. 





[20] V. Milanes, J. Godoy, J. Villagra, and J. Perez, “Automated onramp merging system for congested traffic situations,” IEEE Trans. Intell. Transp. Syst., vol. 12, no. 2, pp. 500–508, Jun. 2011, doi: 10.1109/TITS.2010.2096812. 





[21] A. Uno, T. Sakaguchi, and S. Tsugawa, “A merging control algorithm based on inter-vehicle communication,” in Proc. IEEE Intell. Transp. Syst., Oct. 1999, pp. 783–787. 





[22] J. Rios-Torres and A. A. Malikopoulos, “Automated and cooperative vehicle merging at highway on-ramps,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 4, pp. 780–789, Apr. 2017, doi: 10.1109/TITS.2016.2587582. 





[23] C. Letter and L. Elefteriadou, “Efficient control of fully automated connected vehicles at freeway merge segments,” Transp. Res. C, Emerg. Technol., vol. 80, pp. 190–205, Jul. 2017, doi: 10.1016/j.trc.2017.04.015. 





[24] F. Ye et al., “Bi-level optimal edge computing model for on-ramp merging in connected vehicle environment,” in Proc. IEEE Intell. Vehicles Symp. (IV), Jun. 2019, pp. 2005–2011. 





[25] S.-C. Lin, H. Hsu, Y.-T. Lin, C.-W. Lin, I. H.-R. Jiang, and C. Liu, “A dynamic programming approach to optimal lane merging of connected and autonomous vehicles,” in Proc. IEEE Intell. Vehicles Symp. (IV), Oct. 2020, pp. 349–356. 





[26] H. Pei, S. Feng, Y. Zhang, and D. Yao, “A cooperative driving strategy for merging at on-ramps based on dynamic programming,” IEEE Trans. Veh. Technol., vol. 68, no. 12, pp. 11646–11656, Dec. 2019, doi: 10.1109/TVT.2019.2947192. 





[27] N. Chen, B. van Arem, T. Alkim, and M. Wang, “A hierarchical model-based optimization control approach for cooperative merging by connected automated vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 22, no. 12, pp. 7712–7725, Dec. 2021, doi: 10.1109/TITS.2020.3007647. 





[28] Z. Tang, H. Zhu, X. Zhang, M. Iryo-Asano, and H. Nakamura, “A novel hierarchical cooperative merging control model of connected and automated vehicles featuring flexible merging positions in system optimization,” Transp. Res. C, Emerg. Technol., vol. 138, May 2022, Art. no. 103650, doi: 10.1016/j.trc.2022.103650. 





[29] R. Chen and Z. Yang, “A cooperative merging strategy for connected and automated vehicles based on game theory with transferable utility,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 10, pp. 19213–19223, Oct. 2022, doi: 10.1109/TITS.2022.3161535. 





[30] W. Cao, M. Mukai, T. Kawabe, H. Nishira, and N. Fujiki, “Cooperative vehicle path generation during merging using model predictive control with real-time optimization,” Control Eng. Pract., vol. 34, pp. 98–105, Jan. 2015, doi: 10.1016/j.conengprac.2014.10.005. 





[31] Y. Xie, H. Zhang, N. H. Gartner, and T. Arsava, “Collaborative merging strategy for freeway ramp operations in a connected and autonomous vehicles environment,” J. Intell. Transp. Syst., vol. 21, no. 2, pp. 136–147, Mar. 2017, doi: 10.1080/15472450.2016.1248288. 





[32] C. Mu, L. Du, and X. Zhao, “Event triggered rolling horizon based systematical trajectory planning for merging platoons at mainline-ramp intersection,” Transp. Res. C, Emerg. Technol., vol. 125, Apr. 2021, Art. no. 103006, doi: 10.1016/j.trc.2021.103006. 





[33] Z. Gao, Z. Wu, W. Hao, K. Long, Y.-J. Byon, and K. Long, “Optimal trajectory planning of connected and automated vehicles at on-ramp merging area,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 8, pp. 12675–12687, Aug. 2022, doi: 10.1109/TITS.2021.3116666. 





[34] S. Sharma, I. Papamichail, A. Nadi, H. Van Lint, L. Tavasszy, and M. Snelder, “A multi-class lane-changing advisory system for freeway merging sections using cooperative ITS,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 9, pp. 15121–15132, Sep. 2022, doi: 10.1109/TITS.2021.3137233. 





[35] X. Hu and J. Sun, “Trajectory optimization of connected and autonomous vehicles at a multilane freeway merging area,” Transp. Res. C, Emerg. Technol., vol. 101, pp. 111–125, Apr. 2019, doi: 10.1016/j.trc.2019.02.016. 





[36] V. Cichella, I. Kaminer, C. Walton, and N. Hovakimyan, “Optimal motion planning for differentially flat systems using Bernstein approximation,” IEEE Control Syst. Lett., vol. 2, no. 1, pp. 181–186, Jan. 2018, doi: 10.1109/LCSYS.2017.2778313. 





[37] L. Elefteriadou et al., “Proactive ramp management under the threat of freeway-flow breakdown,” in Proc. Int. Symp. Highway Capacity Quality Service, 2011, pp. 4–14. 





[38] M. Papageorgiou, “Some remarks on macroscopic traffic flow modelling,” Transp. Res. A, Policy Pract., vol. 32, no. 5, pp. 323–329, 1998, doi: 10.1016/S0965-8564(97)00048-7. 





[39] M. Papageorgiou, K.-S. Mountakis, I. Karafyllis, I. Papamichail, and Y. Wang, “Lane-free artificial-fluid concept for vehicular traffic,” Proc. IEEE, vol. 109, no. 2, pp. 114–121, Feb. 2021, doi: 10.1109/JPROC.2020.3042681. 





[40] D. Mellinger and V. Kumar, “Minimum snap trajectory generation and control for quadrotors,” in Proc. IEEE Int. Conf. Robot. Autom., May 2011, pp. 2520–2525, doi: 10.1109/ICRA.2011.5980409. 





[41] J. Zhu, I. Tasic, and X. Qu, “Flow-level coordination of connected and autonomous vehicles in multilane freeway ramp merging areas,” Multimodal Transp., vol. 1, no. 1, Mar. 2022, Art. no. 100005, doi: 10.1016/j.multra.2022.100005. 





[42] L. A. Elefteriadou, “The highway capacity manual 6th edition: A guide for multimodal mobility analysis,” ITE J., vol. 86, pp. 266–270, Apr. 2016. 





[43] A. Aashto, “Policy on geometric design of highways and streets,” Amer. Assoc. State Highway Transp. Officials, vol. 1, no. 990, p. 158, 2001. 





[44] C. Lee, B. Hellinga, and F. Saccomanno, “Real-time crash prediction model for application to crash prevention in freeway traffic,” Transp. Res. Rec., J. Transp. Res. Board, vol. 1840, no. 1, pp. 67–77, Jan. 2003, doi: 10.3141/1840-08. 





[45] C. Lee, B. Hellinga, and K. Ozbay, “Quantifying effects of ramp metering on freeway safety,” Accident Anal. Prevention, vol. 38, no. 2, pp. 279–288, Mar. 2006, doi: 10.1016/j.aap.2005.09.011. 





[46] T. Chen, M. Wang, S. Gong, Y. Zhou, and B. Ran, “Connected and automated vehicle distributed control for on-ramp merging scenario: A virtual rotation approach,” Transp. Res. C, Emerg. Technol., vol. 133, Dec. 2021, Art. no. 103451, doi: 10.1016/j.trc.2021.103451. 





[47] U.S. Department of Transportation Federal Highway Administration, emphNext Generation Simulation (NGSIM) Program I-80 Videos, Federal Highway Admin., Washington, DC, USA, 2016. 





[48] M. Werling, J. Ziegler, S. Kammel, and S. Thrun, “Optimal trajectory generation for dynamic street scenarios in a Frenét Frame,” in Proc. IEEE Int. Conf. Robot. Automat., Anchorage, AK, USA, May 2010, pp. 987–993, doi: 10.1109/ROBOT.2010.5509799. 



![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/f531c4e9cbf3440c560d3303c542a9b7549aca4831087e834c4ff62059f4e772.jpg)


Jieming Chen (Graduate Student Member, IEEE) received the B.Eng. degree in electrical engineering from Shanghai Maritime University, Shanghai, China, in 2017, and the M.S. degree in control engineering from the Technical University of Kaiserslautern, Kaiserslautern, Germany, in 2021. He is currently pursuing the Ph.D. degree in electrical engineering with The Hong Kong Polytechnic University, Hong Kong, China. His research interests include the operations and control of emerging intelligent vehicles. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/b9c807a8f74d0ee0aa9685d821b520948da1d563264682777a82f0d23fdc946f.jpg)


Yue Zhou (Member, IEEE) received the B.Eng. degree in transportation engineering from Tongji University, Shanghai, China, in 2003, the M.S. degree in civil engineering from the University of Nebraska–Lincoln, Lincoln, NE, USA, in 2007, and the Ph.D. degree in civil engineering from the Queensland University of Technology (QUT), Brisbane, Australia, in 2019. He is currently a Post-Doctoral Fellow with the Department of Electrical Engineering, The Hong Kong Polytechnic University, and an Affiliated Researcher with the 

Connected Cities for Smart Transportation (C2SMART) Center, Department of Urban and Civil Engineering, New York University. His research interests include connected automated vehicles, cooperative ITS, and traffic flow theory. He was a recipient of the ITE-ANZ SIDRA Solutions Postgraduate Award and the QUT Excellence Top-Up Scholarship. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/e9d6306b-3404-4098-b396-8a5e0c379452/2e1f8d4f31773efd3ed42dbee218375ae1c161580a5f69fcb8bfde6a99d03db4.jpg)


Edward Chung received the Bachelor of Civil Engineering (Hons.) and Ph.D. degrees from Monash University. He has many years of experience as an Engineer, an experienced Academician, and a Researcher working both nationally and internationally. From 1996 to 2009, he was a Senior Research Scientist with the Australian Road Research Board (1996–1999); a Manager of infrastructure analysis and modeling with the Victorian Department of Infrastructure, Australia (1999–2001); a Visiting Professor with the Centre for Collaborative 

Research, The University of Tokyo (2002–2004); and the Head of the ITS Group, LAVOC, EPFL, Switzerland (2005–2009). He is currently a Professor of intelligent transport systems (ITS) with the Department of Electrical Engineering, The Hong Kong Polytechnic University (PolyU). Before joining PolyU in 2017, he was a Professor with the Queensland University of Technology (QUT) and the Director of the Smart Transport Research Centre, QUT. 