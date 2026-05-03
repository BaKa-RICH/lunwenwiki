# Safety-Critical and Flexible Cooperative On-Ramp Merging Control of Connected and Automated Vehicles in Mixed Traffic

Haoji Liu , Weichao Zhuang , Member, IEEE, Guodong $\mathrm { Y i n } ^ { \mathbb { \oplus } }$ , Senior Member, IEEE, Zhaojian $\operatorname { L i } ^ { \oplus }$ , Senior Member, IEEE, and Dongpu Cao , Senior Member, IEEE 

Abstract— Cooperative on-ramp merging control for connected and automated vehicles (CAVs) can effectively improve traffic throughput and vehicle fuel efficiency at highway on-ramp merging bottlenecks. However, in the mixed traffic scenario where CAVs and human-driven vehicles (HDVs) coexist, the uncertain maneuvers of human drivers pose a major challenge to merging control in terms of safety and flexibility. To this end, this paper proposes a hierarchical cooperative on-ramp merging control strategy for CAVs to optimize flexible trajectories with safety guarantees in mixed traffic. First, the on-ramp merging control problem for CAVs is considered in the case of a threevehicle coordination, resulting in an optimal control problem (OCP) coordinating on-ramp and main-lane CAVs for efficient operation while satisfying multiple safety-critical constraints. Second, a two-level hierarchical control architecture is developed to solve the OCP with mixed state-control constraints. The upper-level planner solves an unconstrained OCP with Pontryagin’s Minimum Principle to calculate an expected merging position, which is embedded in the variable time headway of safe merging constraints in the lower-level controller. Then, the controller converts the nonlinear OCP with safety-critical constraints to a quadratic programing (QP) problem by exploiting Control Barrier Functions (CBFs) and Control Lyapunov Functions (CLFs). By solving the QP efficiently, the time and energy efficient trajectory for each CAV is obtained. In addition, a receding horizon control framework is employed, which enables CAVs to determine flexible merging opportunity and tackle the disturbances caused by HDVs. Finally, comprehensive simulation results show that the proposed cooperative on-ramp merging strategy has potential in enabling merging flexibility, improving traffic efficiency and energy economy in real time. 

Index Terms— Connected and automated vehicle (CAV), on-ramp merging, cooperative control, mixed traffic, control barrier function (CBF). 

Manuscript received 16 September 2021; revised 18 August 2022; accepted 1 November 2022. Date of current version 1 March 2023. This work was supported in part by the National Natural Science Foundation of China (NSFC) under Grant 52172383, Grant 52025121, Grant 51975118, and Grant 51805081; in part by the Key Research and Development Program of Jiangsu Province under Grant BE2019004; and in part by the Achievements Transformation Project of Jiangsu Province under Grant BA2020068 and Grant BA2018023. The Associate Editor for this article was B. Ayalew. (Corresponding authors: Guodong Yin; Weichao Zhuang.) 

Haoji Liu, Weichao Zhuang, and Guodong Yin are with the School of Mechanical Engineering, Southeast University, Nanjing, Jiangsu 211189, China (e-mail: hjl@seu.edu.cn; wezhuang@seu.edu.cn; ygd@seu.edu.cn). 

Zhaojian Li is with the Department of Mechanical Engineering, Michigan State University, Michigan, MI 48823 USA (e-mail: lizhaoj1@egr.msu.edu). 

Dongpu Cao is with the School of Vehicle and Mobility, Tsinghua University, Beijing 100084, China (e-mail: dpcao2016@163.com). 

Digital Object Identifier 10.1109/TITS.2022.3224592 

# I. INTRODUCTION

R ECENT advances in artificial intelligence and vehicularcommunication technique promote the development of communication technique promote the development of connected and automated vehicles (CAVs) [1], [2], [3]. As an advanced CAV application, cooperative driving has attracted increasing research interests, which uses vehicle-to-everything (V2X) communications to coordinate CAVs and infrastructures for driving safety and efficiency improvement [4], [5]. 

One of the cooperative driving applicable scenarios is the traffic conflict zone (e.g., highway on-ramp merging zones) [6], [7]. The on-ramp merging is a stressful task for human drivers due to the involved risk and the close interaction with other drivers. Therefore, incorrect merging maneuver may happen, causing traffic perturbations, inefficient traffic flow and even crashes. As such, the cooperative on-ramp merging is one of the promising directions to improve traffic safety and efficiency at highway on-ramps [8]. Specifically, aiming at its core task, i.e., resolving possible trajectory conflicts between vehicles on the ramp and those on the adjacent main lane, the main idea of cooperative on-ramp merging control is adjusting longitudinal speeds of both on-ramp and mainlane CAVs to achieve safe and efficient on-ramp merging [9], [10], [11], [12]. In general, the cooperative merging problem is formulated as an optimal control problem (OCP), which aims to minimize the energy consumption and merging duration while keeping safe inter-vehicle distances [12]. 

The cooperative on-ramp merging control can be generally categorized into two types, i.e., centralized control and decentralized control [12], [13]. In centralized approach, a roadside central controller collects CAV states in a merging control zone through V2X communication, and optimizes CAV trajectories and merging sequence globally. Rios-Torres et al. [14] formulated the CAV trajectory optimization problem as an unconstrained OCP by assigning the merging timing and position of each vehicle in the merging zone. The analytical optimal solution is then derived through Hamiltonian analysis. According to the analytical optimal control rule, Ding et al. [15] proposed a rule-based algorithm to determine the merging sequence for better traffic efficiency. In addition, Jing et al. [16] used the cooperative game theory to solve the cooperative merging problem globally, which optimizes merging sequence and trajectory simultaneously. 

Although the centralized control provides the global optimal solution, it may suffer great computational burden with increased number of CAVs involved, especially during heavy traffic. Once the central controller fails, the whole traffic may tie up. As an alternative solution, the decentralized approach has been widely studied in academia and industry due to its flexibility, scalability, and fault tolerance performance compared to the centralized system [17]. Ntousakis et al. [18] formulated a finite-horizon unconstrained OCP for the onramp merging, which is solved by time-variant linear-quadratic regulator (LQR) approach. Fukuyama [19] solved the on-ramp merging problem with game theory, and derived the optimal trajectories for each vehicle with zero-suppressed binary decision diagram. Another study presented by Xiao et al. [20], designed a decentralized on-ramp optimal control framework considering merging safety constraints, which is solved by using Pontryagin’s Minimum Principle (PMP). 

The aforementioned studies all assume the vehicles on road are connected and automated. However, due to the cost and accessibility consideration, the market penetration rate of CAV is expected to evolve gradually. The human-driven vehicles (HDVs) are expected to still drive on road for a long time and thus form a mixed traffic with CAVs [21]. Rios-Torres et al. [22] developed a microscopic on-ramp merging framework for the mixed traffic scenario, where the HDV is modeled by the Gipps car-following model. The CAV trajectory is planned by the same optimal control method as [14], which regulates the CAV arrive at the merging point (the end of an on-ramp) with prespecified timing. Similarly, Sun et al. [23] also specified merging position and timing for on-ramp CAVs and used deterministic traffic flow models to describe HDV trajectories. However, as pointed out in [24], the maneuver of human drivers is hard to predict, hence the HDV is usually regarded as a disturbance for CAV control with uncertain merging time. Karimi et al. [25] employed a model predictive control (MPC) scheme to alleviate the effects caused by HDVs. At each time step, longitudinal trajectories of CAVs are optimized to ensure merging safety. 

The mixed traffic studies mentioned above all use the prespecified-position merging (PPM) policy, which is common in full-CAV studies [12]. As all vehicles are controllable, following the pre-planned trajectories could achieve global optimization. However, in the mixed traffic scenario, the PPM policy may have limited optimality since the uncertain movements of HDVs require flexible merging choices for CAVs to actively seize the transient optimal opportunity instead of passively waiting for a fixed merging position. Thus, some studies presented the flexible-merging position (FPM) policy, which enables on-ramp CAVs to merge into the main road at a flexible position once proper gap and relative speed between vehicles is generated. The driving scenarios for FPM and PPM are depicted in Fig. 1. Liao et al. [26] introduced a decentralized agent-based game strategy to flexibly decide merging sequence and trajectory in mixed traffic, but energy efficiency was not considered. Zhou et al. [27], [28] developed a free-terminal optimal control method considering speed and control limits to plan flexible merging positions for CAVs. A recursive optimization framework is 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/c477d362816d782b3aaaf5c9f4eecc4d6c14c65047ab64c09802015733ee02c3.jpg)



Fig. 1. Comparison of FPM and PPM policy.


used to tackle the uncertain behaviors of HDVs. Due to computational burden consideration, safe distance constraints were not evolved. However, the inter-vehicle safety-critical constraints are of great significance to avoid vehicle collisions in mixed traffic, especially when the main-lane traffic is dense. Therefore, although the literatures mentioned above provide a meaningful exploration, there still remains a research gap between flexible merging position planning and safetycritical control of cooperative on-ramp merging in mixed traffic. 

To overcome the aforementioned limitations, this paper proposes a hierarchical on-ramp merging control strategy for CAVs in mixed traffic, which is composed of upper-level and lower-level controllers. In particular, the upper level decides the flexible expected merging position for CAVs by using PMP, while the lower-level controller optimizes CAV trajectories using an indirect optimal control method, which combines Control Barrier Function (CBF) and Control Lyapunov Function (CLF). The CBF-CLF based method can effectively solve the OCP with multiple state constraints and objectives [29], [30], which has been used in cooperative merging control in full-CAV traffic by Xiao et al. [31], [32]. In this paper, the flexible non-state time-varying variable, i.e., expected merging position, is integrated into the CBF, which is called Flexible Control Barrier Function (FCBF). In addition, a receding horizon control framework is adopted to update the traction forces repeatedly to tackle the uncertainties of HDVs. 

The main contributions of this paper are threefold. First, the flexible merging position is enabled by the proposed hierarchical merging control strategy, wherein the FCBF connects the upper and lower levels through time-varying expected merging positions and variable time headways. Second, the optimal merging control problem with mixed state-control constraints is efficiently solved with two optimization problems, i.e., an unconstrained OCP in upper-level and safety-critical trajectory optimization problems in the lower-level. The two levels are both computationally efficient and can be implemented in real time. Specifically, the unconstrained OCP in the upper-level is solved analytically by PMP, while the lower-level problem is formulated in the quadratic programming (QP) form by using CBF-CLF based method, which could be solved efficiently as well. Third, a receding horizon control framework is employed to repeatedly update expected merging positions and traction forces for tackling the disturbances from HDVs and maintaining merging flexibility and safety. 

The remainder of this paper is organized as follows. In Section II, we formulate the cooperative on-ramp merging problem in mixed traffic. The control objectives and constraints for CAVs are defined. In Section III, a two-level hierarchical control architecture is presented, where the upper-level 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/378dff1e11fb3609fcf39654e0eebee084eb12f3fefc484d1a2163bebc7a1029.jpg)



Fig. 2. The mixed traffic on-ramp merging scenario.


merging regulator is developed by formulating an unconstrained free-terminal optimal control, and the lower-level controller is designed by using CBF-CLF method. Section IV presents several simulations with detailed discussions. Finally, conclusions are drawn in Section V. 

# II. PROBLEM FORMULATION AND CONTROL FRAMEWORK

This section will firstly introduce the problem of cooperative on-ramp merging control for CAVs in mixed traffic. The optimal control problems of both on-ramp and main-lane CAVs are formulated with involved driving safety concerns. A two-level hierarchical control architecture is proposed to optimize the expected merging position and trajectories of CAVs simultaneously. 

# A. Problem Statement

We define a generic on-ramp merging scenario with two lanes as shown in Fig. 2, including a single-lane main road and an on-ramp connected with an acceleration lane. The merging of on-ramp vehicles is only allowed within the acceleration lane. 

Since on-ramp merging is basically a process of an on-ramp vehicle merging into the gap of two adjacent main-lane vehicles, this paper solves the cooperative on-ramp merging problem in mixed traffic by cooperating three vehicles, which compose the three-vehicle coordination group (TCG). Specifically, the main-lane predecessor of a TCG, called leading vehicle, can be either a CAV or HDV, whose trajectory is treated as disturbance for its main-lane follower and subsequent on-ramp vehicle because it directly reflected the influence caused by the downstream HDVs [33]. The main-lane follower is a CAV, called assisted vehicle, whose responsibility is yielding to the merging vehicle for generating a suitable merging gap. The on-ramp merging vehicle is also a CAV, intends to merge into the main road between two main-lane vehicles by adjusting its longitudinal speed. Thus, this paper will focus on cooperatively regulating the merging and assisted CAVs under the disturbances of downstream traffic (or the leading vehicle) to realize traffic throughout and energy efficiency improvement. 

To achieve such purpose, the local coordinator is utilized to share traffic information with CAVs, assign the leading vehicle and assisted vehicle to form a TCG, and recursively plan expected merging positions for CAVs in the TCG. The TCG is grouped when the on-ramp merging CAV enters the coordination zone. A trigger position (TP) is defined for determining whether a merging CAV enters the coordination zone, as shown in Fig. 2. Note that, the rule of selecting the leading vehicle and assisted vehicle is beyond 


TABLE I NOTATION OF MAJOR VARIABLES


<table><tr><td>Variables</td><td>Description</td></tr><tr><td>t</td><td>Time instant</td></tr><tr><td>t0</td><td>Time when the TCG is formed, also the initial time of cooperative merging control process</td></tr><tr><td>tm</td><td>Time when the merging process is accomplished</td></tr><tr><td>k</td><td>Recursive step number, k = 0,1,2,...</td></tr><tr><td>tc</td><td>Initial time of each recursive step, tc = t0 + kΔt</td></tr><tr><td>pl(t),pm(t),ps(t)</td><td>Position of the leading vehicle, merging vehicle, assisted vehicle at time t</td></tr><tr><td>vl(t),vm(t),vs(t)</td><td>Speed of the leading vehicle, merging vehicle, assisted vehicle at time t</td></tr><tr><td>al(t),am(t),as(t)</td><td>Acceleration of the leading vehicle, merging vehicle, assisted vehicle at time t</td></tr><tr><td>um(t),us(t)</td><td>Traction force (also control input of system (1)) of the merging vehicle, assisted vehicle at time t</td></tr><tr><td>Fr,m(t),Fr,s(t)</td><td>Resistance force of the merging vehicle, assisted vehicle at time t</td></tr><tr><td>zl-m(t),zm-s(t),zl-s(t)</td><td>Distance between vehicles at time t (leading vehicle-merging vehicle, merging vehicle-assisted vehicle, leading vehicle-assisted vehicle, respectively)</td></tr><tr><td>Δzl-m(t),Δzm-s(t)</td><td>Deviation of the actual inter-vehicle distance from the required minimum safe distance (leading vehicle -merging vehicle, merging vehicle-assisted vehicle, respectively), see Equation (11)</td></tr><tr><td>Δvl-m(t),Δvl-s(t)</td><td>Deviation of vehicle speeds (leading vehicle -merging vehicle, leading vehicle - assisted vehicle, respectively), see Equation (12)</td></tr><tr><td>Imexp| (t), Imexp| (t)</td><td>Expected merging position of merging vehicle and assisted vehicle at time t</td></tr></table>

the scope of this paper and will be studied in our future work. This paper mainly focuses on flexible merging position planning and decentralized ramp merging control as elaborated later. 

Definition 1. Vehicle Role Notation: The leading vehicle, merging vehicle and assisted vehicle in a TCG are denoted by l , m, and $s$ respectively. A general symbol $\varsigma$ ( $\varsigma = m$ or $s$ represents merging CAV or assisted CAV) is defined to avoid repeated statements of the common parts for different CAVs. 

To facilitate the development of the following contents, we give the notation of major variables in Table I. 

# B. Vehicle Dynamics and Constraints

1) Nonlinear Vehicle Dynamics: Since we only consider longitudinal movements of vehicles out of the same purpose to dissolve merging trajectory conflicts as [14], nonlinear longitudinal vehicle dynamics [34] for CAVs is modelled. 

$$
\underbrace {\left[ \begin{array}{l} \dot {p} _ {\varsigma} (t) \\ \dot {v} _ {\varsigma} (t) \end{array} \right]} _ {x _ {\varsigma} (t)} = \underbrace {\left[ \begin{array}{c} v _ {\varsigma} (t) \\ - \frac {1}{M} F _ {r , \varsigma} \left(v _ {\varsigma} (t)\right) \end{array} \right]} _ {f (x _ {\varsigma} (t))} + \underbrace {\left[ \begin{array}{l} 0 \\ \frac {1}{M} \end{array} \right]} _ {g (x _ {\varsigma} (t))} u _ {\varsigma} (t) \tag {1}
$$

where $\pmb { x } _ { \varsigma } ( t ) \ = \ \big ( p _ { \varsigma } ( t ) , \upsilon _ { \varsigma } ( t ) \big )$ denotes the state vector of vehicle $\varsigma ( \varsigma = m$ or s), the position $p _ { \varsigma } ( t )$ is defined by $p$ -axis as shown in Fig. 2, whose origin is the TP and the positive direction towards the downstream. The resistance force $F _ { r , \varsigma } ( t )$ is expressed below, where sgn (·) is the signum function. 

$$
F _ {r, \varsigma} (t) = \alpha_ {0} \operatorname {s g n} \left(v _ {\varsigma} (t)\right) + \alpha_ {1} v _ {\varsigma} (t) + \alpha_ {2} v _ {\varsigma} ^ {2} (t) \tag {2}
$$

2) Dynamic Limitations: Traction force limitation: For each CAV $\varsigma$ , the traction force is limited by its driving and braking capacity 

$$
- c _ {d} M g \leq u _ {\varsigma} (t) \leq c _ {a} M g \tag {3}
$$

Speed Limitation: The speed for each CAV $\varsigma$ is bounded by minimum and maximum speed limits 

$$
v _ {\min } \leq v _ {\varsigma} (t) \leq v _ {\max } \tag {4}
$$

3) Safe Constraints: Two safety-related constraints are imposed, i.e., safe car-following and safe merging constraints, to achieve safe control. The former prevents the possible rear-end collision travelling on the same lane, while the latter is designed to avoid the lateral collision when the merging vehicle is changing lane. 

Safe car-following distance constraint: In a TCG, the main-lane assisted vehicle s should always keep safe car-following distance from the leading vehicle l. Adopting the time headway policy [35], we have 

$$
z _ {l - s} (t) = p _ {l} (t) - p _ {s} (t) \geq \varphi_ {c f} v _ {s} (t) + l _ {c f} \tag {5}
$$

where $\varphi _ { c f }$ is the constant time headway for safe car-following, $l _ { c f }$ is the standstill distance. 

Safe merging distance constraint: When an on-ramp vehicle merges at time $t ^ { m }$ , its distance from the leading vehicle $z _ { l - m } ( t ^ { m } )$ should satisfy 

$$
z _ {l - m} \left(t ^ {m}\right) = p _ {l} \left(t ^ {m}\right) - p _ {m} \left(t ^ {m}\right) \geq \varphi_ {m e r} v _ {m} \left(t ^ {m}\right) + l _ {m e r} \tag {6}
$$

where $\varphi _ { m e r }$ is the constant time headway for safe merging, $l _ { m e r }$ is the standstill distance for merging. The assisted vehicle also keeps safe distance from the merging vehicle at time 

$$
z _ {m - s} \left(t ^ {m}\right) = p _ {m} \left(t ^ {m}\right) - p _ {s} \left(t ^ {m}\right) \geq \varphi_ {m e r} v _ {s} \left(t ^ {m}\right) + l _ {m e r} \tag {7}
$$

Mandatory merging position constraint: Although we seek to realize flexible-position merging similar to the discretionary lane-change, the on-ramp merging vehicle must merge into the main road before it reaches the end of the acceleration lane, 

$$
0 \leq p _ {m} \left(t ^ {m}\right) \leq L \tag {8}
$$

# C. Cooperative Optimal Control Problem

To achieve safety-critical and flexible cooperative on-ramp merging control, we formulate the optimal control problem for the whole merging control process, whose goal is to minimize overall energy consumption and travel efficiency of two CAVs in a TCG under driving safety concerns. 

Problem I: Optimal ramp merging control 

$$
\min  _ {u _ {m}, u _ {s}} Q _ {1} = \int_ {t ^ {0}} ^ {t ^ {m}} [ E (u _ {m} (t)) + E (u _ {s} (t)) + \omega ] d t \tag {9}
$$

subject to constraints (3)-(8), governed by nonlinear vehicle dynamics (1)-(2). 

In the objective function $Q _ { 1 }$ , $E ( \cdot )$ , a function related to system control input $u _ { m } ( t )$ and $u _ { s } ( t )$ , represents the energy consumption of CAVs [36]. $\omega$ is the penalty coefficient for travel time, the bigger the value, the shorter the overall travel time. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/20e076db19d3276d03ad89b4f63811e298c5663fdb5ddea160d59ce8750304c7.jpg)



Fig. 3. Hierarchical receding horizon merging control architecture for CAVs.


Problem I is addressed by optimizing control and state variables. The merging position $p _ { \varsigma } ( t ^ { m } )$ and merging time $t ^ { m }$ are also variables to be optimized simultaneously, which enable the FPM policy. However, Problem I is rather challenging to directly solve since it’s governed by nonlinear vehicle systems with several constraints. This paper aims to propose an efficient optimal control strategy to achieve safety-critical and flexible cooperative merging in mixed traffic. 

# D. Control Framework

The formulated constrained optimal control problem (Problem I) could be solved analytically [14] or numerically [37]. However, the mixed state-control constraints increase computational complexity, making Problem I hard to solve in real time for some cases. Therefore, this paper proposes a two-level hierarchical control architecture shown in Fig. 3 to solve the constrained optimal control problem efficiently. 

1) Hierarchical Receding Horizon Control Architecture: The whole constrained OCP is firstly resolved into two suboptimization problems, i.e., an unconstrained OCP and a trajectory optimization problem with state and control constraints. The unconstrained OCP is solved in upper-level by using PMP to derive a candidate merging position, then the smallest one of the candidate and the mandatory merging position $L$ will be selected as the expected merging position, which is the input of the lower-level controller. The lower-level trajectory controller converts the safety-critical OCP with state and control constraints to a QP problem by using CBF-CLF based method. The merging time and energy efficiency oriented optimal speed profiles for both merging and assisted CAVs are calculated. 

In addition, a receding horizon control framework is proposed to handle the disturbance from the uncertainties of 

the leading vehicle. The traction force for both merging and assisted CAVs are updated in each control period recursively. The receding time interval $\tau _ { k }$ is derived by partitioning the continuous time equally according to sampling time $\Delta t$ , i.e., 

$$
\tau_ {k} := \left[ t ^ {0} + k \Delta t, t ^ {0} + (k + 1) \Delta t\right) \subset \left[ t ^ {0}, t ^ {m} \right], \quad k = 0, 1, 2, \dots \tag {10}
$$

During each time interval $\tau _ { k }$ (also recursive step $k$ ), the upper-level planner addresses the unconstrained OCP with consideration of mandatory merging position $L$ to derive an expected merging position $L _ { \varsigma } ^ { e x \bar { p } } | ( t ^ { \bar { 0 } } + k \Delta t )$ , depending on the states of the leading vehicle and CAVs. Then, based on $L _ { \varsigma } ^ { e x p } | ( t ^ { 0 } + k \Delta t )$ and vehicle states, the lower-level controller will calculate the traction force $u _ { \varsigma } | ( t ^ { 0 } + k \Delta t )$ by solving the QP problem. The movements of all CAVs, $\pmb { x } _ { \varsigma } ( t ^ { 0 } + ( k + 1 ) \Delta t )$ , are calculated by executing the derived traction forces. 

2) Merging Requirements: The abovementioned procedures are repeated until suitable state conditions (called merging requirements) are met, which include the inter-vehicle gaps and relative speeds. The former is required by safe merging distance constraint (6)-(7). The latter is considered because close relative speeds can ensure the stability of required inter-vehicle gaps, thereby providing a stable initial condition for other subsequent operations. Deviation between the actual inter-vehicle distance and required minimum distance of (6)-(7) is 

$$
\Delta z _ {l - m} \left(t ^ {m}\right) = p _ {l} \left(t ^ {m}\right) - p _ {m} \left(t ^ {m}\right) - \varphi_ {\text {m e r}} v _ {m} \left(t ^ {m}\right) - l _ {m e r} \tag {11a}
$$

$$
\Delta z _ {m - s} \left(t ^ {m}\right) = p _ {m} \left(t ^ {m}\right) - p _ {s} \left(t ^ {m}\right) - \varphi_ {\text {m e r}} v _ {s} \left(t ^ {m}\right) - l _ {\text {m e r}} \tag {11b}
$$

Deviation between the actual speed of CAV $\varsigma$ and that of leading vehicle $l$ is 

$$
\Delta v _ {l - m} \left(t ^ {m}\right) = v _ {l} \left(t ^ {m}\right) - v _ {m} \left(t ^ {m}\right) \tag {12a}
$$

$$
\Delta v _ {l - s} \left(t ^ {m}\right) = v _ {l} \left(t ^ {m}\right) - v _ {s} \left(t ^ {m}\right) \tag {12b}
$$

The merging CAV executes merging maneuver once the following merging requirements are met. 

$$
\Delta z _ {l - m} \left(t ^ {m}\right) \in [ - \Delta z _ {\max }, \Delta z _ {\max } ] \tag {13a}
$$

$$
\Delta z _ {m - s} \left(t ^ {m}\right) \in \left[ - \Delta z _ {\max }, \Delta z _ {\max } \right] \tag {13b}
$$

$$
\Delta v _ {l - m} \left(t ^ {m}\right) \in \left[ - \Delta v _ {\max }, \Delta v _ {\max } \right] \tag {13c}
$$

$$
\Delta v _ {l - s} \left(t ^ {m}\right) \in [ - \Delta v _ {\max }, \Delta v _ {\max } ] \tag {13d}
$$

where $\Delta z _ { \mathrm { m a x } }$ is the maximum allowable distance deviation, $\Delta v _ { \mathrm { m a x } }$ is the maximum allowable speed deviation. 

# III. COOPERATIVE MERGING CONTROL STRATEGY DESIGN

This section will introduce the two-level cooperative control strategy for CAVs to achieve efficient on-ramp merging. The upper level calculates an expected merging position, which is a reference for the lower level. The lower level optimizes the speed profiles of CAVs considering safety-critical constraints. 

# A. Upper-Level Merging Position Planning

As discussed in Section II, suitable inter-vehicle distances are required for safe merging. Since the assisted vehicle is regulated to reserve the sufficient gap, the upper-level planner will calculate the expected merging position by optimizing the trajectory of the assisted vehicle. That is, the upper level will solve an optimal control problem, whose objective is optimizing the control effort (acceleration) of the assisted vehicle for minimum energy consumption and maximum travel efficiency while meeting the safe merging requirements. 

1) Free-Terminal Optimal Control Problem: To enable efficient computation, the nonlinear dynamics (1) is simplified to a second-order linear form. 

$$
\dot {\boldsymbol {x}} _ {s} (t) = \left[ \begin{array}{l} \dot {p} _ {s} (t) \\ \dot {v} _ {s} (t) \end{array} \right] = \left[ \begin{array}{l} v _ {s} (t) \\ a _ {s} (t) \end{array} \right] \tag {14}
$$

where $a _ { s } ( t )$ is the acceleration of the assisted CAV, which is also the control variable of system (14). In addition, the safety-related state constraints are also ignored for computation burden consideration. Therefore, the expected merging position is calculated by solving the Problem II, as follows. 

Problem II. Expected merging position planning 

$$
\min  Q _ {2} \left(a _ {s} (t)\right) = \int_ {t ^ {0}} ^ {t ^ {m}} \left[ \frac {1}{2} \left(a _ {s} (t)\right) ^ {2} + \delta \right] d t \tag {15a}
$$

$$
\mathrm {s . t} p _ {l} \left(t ^ {m}\right) - p _ {s} \left(t ^ {m}\right) = 2 \varphi_ {m e r} v _ {s} \left(t ^ {m}\right) + 2 l _ {m e r} \tag {15b}
$$

$$
v _ {s} \left(t ^ {m}\right) = v _ {l} \left(t ^ {m}\right) \tag {15c}
$$

where $\delta$ is the penalty coefficient for travel time. The first term in Eq.(15a) is to minimize the control efforts as it indirectly reflects the energy consumption [36], while the second one is to improve the travel efficiency. Constraints (15b)-(15c) are terminal conditions derived from the merging requirements (13), where the terminal deviations are set to zero to close inter-vehicle distances and relative speeds as [14]– [23], [27], [28] do. In constraint (15b), $p _ { l } ( t ^ { m } ) \mathrm { ~ - ~ }$ $\begin{array} { r l r } { p _ { s } ( t ^ { m } ) } & { = } & { ( p _ { l } ( t ^ { m } ) \ - \ p _ { m } ( t ^ { m } ) ) \ + \ ( p _ { m } ( t ^ { m } ) \ - \ p _ { s } ( t ^ { m } ) ) = } \end{array}$ $\varphi _ { m e r } \upsilon _ { m } ( t ^ { m } ) + l _ { m e r } + \varphi _ { m e r } \upsilon _ { s } ( t ^ { m } ) + l _ { m e r }$ , since we want to achieve close relative speeds at terminal time $t ^ { m }$ , i.e., $\upsilon _ { m } ( t ^ { m } ) = \upsilon _ { s } ( t ^ { m } )$ , then we have (15b). 

Problem II is a free-terminal optimal control problem, where the terminal time $t ^ { m }$ and position $p _ { s } ( t ^ { m } )$ are variables to be optimized. Note that, the solution of Problem II is only used as a reference in the lower-level controller but not the actual merging time. Thus, we will use $t ^ { f }$ instead of $t ^ { m }$ in the upper level to distinguish the difference. 

2) PMP-Based Analytical Solution: Since Problem II is an unconstrained OCP with free terminal time, the PMP is used to calculate the optimal solution analytically [38]. The Hamiltonian of Problem II, which introduces Lagrangian multipliers $\mu _ { 1 } ( t ) , \mu _ { 2 } ( t )$ to combine objective function and system dynamics, is 

$$
H = \frac {1}{2} a _ {s} (t) ^ {2} + \frac {1}{2} \delta - \mu_ {1} (t) v _ {s} (t) - \mu_ {2} (t) a _ {s} (t) \tag {16}
$$

The Euler-Lagrange equations are 

$$
\dot {\mu} _ {1} (t) = \frac {\partial H}{\partial x _ {s}} = 0 \tag {17a}
$$

$$
\dot {\mu} _ {2} (t) = \frac {\partial H}{\partial v _ {s}} = - \mu_ {1} (t) \tag {17b}
$$

$$
\frac {\partial H}{\partial a _ {s}} = a _ {s} (t) - \mu_ {2} (t) = 0 \tag {17c}
$$

Recall that Problem II is solved recursively, the initial boundary conditions are current conditions $x _ { s } ( t ^ { c } )$ and $\upsilon _ { s } ( t ^ { c } )$ at $t ^ { c } = \dot { t } ^ { 0 } + k \Delta t ( k = 0 , 1 , 2 , . . . )$ , and the terminal boundary conditions W at terminal time $t ^ { f }$ are 

$$
\begin{array}{l} \mathrm {W} = \left[ \begin{array}{c} w _ {1} (t ^ {f}) \\ w _ {2} (t ^ {f}) \end{array} \right] \\ = \left[ \begin{array}{c} x _ {s} \left(t ^ {f}\right) - x _ {l} \left(t ^ {f}\right) + 2 l _ {\text {m e r}} + 2 \varphi_ {\text {m e r}} v _ {s} \left(t ^ {f}\right) \\ v _ {s} \left(t ^ {f}\right) - v _ {l} \left(t ^ {f}\right) \end{array} \right] \tag {18} \\ \end{array}
$$

yields transversality conditions 

$$
\mu_ {1} \left(t ^ {f}\right) = - \beta_ {1} \frac {\partial w _ {1}}{\partial x} \left(t ^ {f}\right) - \beta_ {2} \frac {\partial w _ {2}}{\partial x} \left(t ^ {f}\right) = - \beta_ {1} (1 9 a)
$$

$$
\mu_ {2} \left(t ^ {f}\right) = - \beta_ {1} \frac {\partial w _ {1}}{\partial v} \left(t ^ {f}\right) - \beta_ {2} \frac {\partial w _ {2}}{\partial v} \left(t ^ {f}\right) = - \beta_ {2} (1 9 b)
$$

$$
H \left(t ^ {f}\right) + \beta_ {1} \frac {\partial w _ {1}}{\partial t ^ {f}} \left(t ^ {f}\right) + \beta_ {2} \frac {\partial w _ {2}}{\partial t ^ {f}} \left(t ^ {f}\right) = 0 \tag {19c}
$$

where $\beta _ { 1 } , \beta _ { 2 }$ are constants of transversality condition. Substitute (16)-(18) into (19) gives 

$$
\begin{array}{l} \frac {1}{2} a _ {s} \left(t ^ {f}\right) ^ {2} + \frac {1}{2} \delta - \mu_ {2} \left(t ^ {f}\right) a _ {s} \left(t ^ {f}\right) \\ - \left(2 \varphi_ {\operatorname {m e r}} \mu_ {1} \left(t ^ {f}\right) - \mu_ {2} \left(t ^ {f}\right)\right) \dot {v} _ {l} \left(t ^ {f}\right) = 0 \tag {20} \\ \end{array}
$$

Solving the two-point boundary value problem consisting of (16)-(20) derives the optimal acceleration, speed and position. 

$$
a _ {s} (t) = \mu_ {2} (t) = - c _ {1} t + c _ {2} \tag {21a}
$$

$$
v _ {s} (t) = - \frac {1}{2} c _ {1} t ^ {2} + c _ {2} t + c _ {3} \tag {21b}
$$

$$
x _ {s} (t) = - \frac {1}{6} c _ {1} t ^ {3} + \frac {1}{2} c _ {2} t ^ {2} + c _ {3} t + c _ {4} \tag {21c}
$$

where the parameters $c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 }$ are variables to be solved. 

3) Expected Merging Position: Combining Equation (21) and boundary conditions (18), the parameters $c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 }$ and expected merging time $t _ { f }$ are calculated by solving the following algebraic equations (22) 

$$
v _ {s} \left(t ^ {c}\right) = - \frac {1}{2} c _ {1} \cdot \left(t ^ {c}\right) ^ {2} + c _ {2} t ^ {c} + c _ {3} \tag {22a}
$$

$$
x _ {s} \left(t ^ {c}\right) = - \frac {1}{6} c _ {1} \cdot \left(t ^ {c}\right) ^ {3} + \frac {1}{2} c _ {2} \cdot \left(t ^ {c}\right) ^ {2} + c _ {3} t ^ {c} + c _ {4} \tag {22b}
$$

$$
v _ {s} \left(t ^ {f}\right) = - \frac {1}{2} c _ {1} \cdot \left(t ^ {f}\right) ^ {2} + c _ {2} t ^ {f} + c _ {3} = v _ {l} \left(t ^ {f}\right) \tag {22c}
$$

$$
\begin{array}{l} x _ {s} \left(t ^ {f}\right) = - \frac {1}{6} c _ {1} \left(t ^ {f}\right) ^ {3} + \frac {1}{2} c _ {2} \left(t ^ {f}\right) ^ {2} + c _ {3} t ^ {f} + c _ {4} \\ = x _ {l} \left(t ^ {f}\right) - 2 l _ {m e r} - 2 \varphi_ {m e r} v _ {l} \left(t ^ {f}\right) \tag {22d} \\ \end{array}
$$

$$
\begin{array}{l} \frac {1}{2} \left(- c _ {1} t ^ {f} + c _ {2}\right) ^ {2} + \frac {1}{2} \delta - \left(- c _ {1} t ^ {f} + c _ {2}\right) ^ {2} \\ - \left(2 \varphi_ {m e r} c _ {1} + c _ {1} t ^ {f} - c _ {2}\right) \dot {v} _ {l} \left(t ^ {f}\right) = 0 \quad (2 2 \mathrm {e}) \\ \end{array}
$$

Then we have candidate flexible merging position for CAVs 

$$
L _ {s} ^ {c} = x _ {l} \left(t ^ {0}\right) + \int_ {t ^ {0}} ^ {t ^ {f}} \left(v _ {s} \left(t ^ {0}\right) + \int_ {0} ^ {t} (- c _ {1} \tau + c _ {2}) d \tau\right) d t \tag {23a}
$$

$$
L _ {m} ^ {c} = L _ {s} ^ {c} + l _ {\text {m e r}} + \varphi_ {\text {m e r}} v _ {l} \left(t ^ {f}\right) \tag {23b}
$$

Recall that the merging position of the on-ramp vehicle cannot exceed the end of the acceleration lane, hence the candidate needs comparing with the mandatory merging position to determine the expected one at current time $t ^ { c }$ , i.e., 

$$
L _ {m} ^ {\exp} \mid (t ^ {c}) = \min  \left\{L _ {m} ^ {c}, L \right\} \tag {24a}
$$

$$
L _ {s} ^ {e x p} \mid (t ^ {c}) = L _ {m} ^ {e x p} \mid (t ^ {c}) - l _ {m e r} - \varphi_ {m e r} v _ {l} (t ^ {f}) \tag {24b}
$$

# B. Lower-Level Safe Optimal Control

The aim of the lower-level controller is to derive the decentralized optimal control solutions for CAVs to achieve merging at the expected merging position calculated in the upper-level efficiently while considering the safety constraints (as shown in Problem I). 

1) Decentralized Optimal Control Problem: The merging and assisted CAVs will calculate their own optimal trajectories in a decentralized manner, i.e., the Problem I is reformulated as follows. 

Problem III. Optimal control for the merging CAV 

$$
\min  _ {u _ {m}} Q _ {3} = \int_ {t ^ {0}} ^ {t ^ {m}} [ E (u _ {m} (t)) + \omega ] d t \tag {25}
$$

subject to (3)-(4), (6), (8), governed by (1)-(2). 

Problem IV. Optimal control for the assisted CAV 

$$
\min  _ {u _ {s}} Q _ {4} = \int_ {t ^ {0}} ^ {t ^ {m}} [ E (u _ {s} (t)) + \omega ] d t \tag {26}
$$

subject to (3)-(5), (7), governed by (1)-(2). 

Since the common optimal control methods, e.g., PMP, have difficulties in addressing the multi-constraint nonlinear OCP due to the computational complexity, this paper uses an indirect optimal control method to derive the optimal solution, which combines CBFs and CLFs. The core idea of CBF-CLF based method is converting the state constraints $\mathbf { \boldsymbol { x } } _ { \varsigma } ( t )$ to control constraints $u _ { \varsigma } ( t )$ . As a result, the nonlinear time-invariant control system and multiple safety-related constraints are both considered. In addition, the original OCP can be transformed into a QP problem, which enables efficient computation. The details about CBF-CLF-based method and controller design will be given later. 

2) Safety-Critical and Flexible Merging Constraint: To enable safety-critical and flexible optimal ramp merging control in the lower level, we transform the constant time headway $\varphi _ { m e r }$ of safe merging distance constraints (6) and (7) into linear continuous functions $\Phi _ { l - m } ( p _ { m } ( t ) )$ and $\Phi _ { m - s } ( p _ { s } ( t ) )$ for merging CAV and assisted CAV, respectively. 

Definition 2. Time Headway Function: The linear time continuous time headway function $\Phi _ { m - s } ( p _ { s } ( t ) )$ (or $\Phi _ { l - m } ( p _ { m } ( t ) ) )$ 

is a class $\mathcal { \kappa }$ function satisfying $\Phi _ { m - s } ( p _ { s } ( t ^ { m } ) ) = \varphi _ { m e r }$ (or $\Phi _ { l - m } ( p _ { m } ( t ^ { m } ) ) = \varphi _ { m e r } )$ . 

The defined time headway function reflects a process of gradually expanding inter-vehicle distances and meeting the merging requirement at $t ^ { m }$ along with CAVs traveling from initial position $p _ { \varsigma } ( t ^ { 0 } )$ to merging position $p _ { \varsigma } \left( t ^ { m } \right)$ . The function is correlated with initial position $p _ { \varsigma } ( t ^ { 0 } )$ , current position $p _ { \varsigma } ( t ^ { c } )$ and merging position $p _ { \varsigma } ( t ^ { m } )$ . The function value is set to linearly increase from an initial value to a constant value $\varphi _ { m e r }$ , which is the required safe value. 

Theorem 1. The linear continuous function $\Phi _ { m - s } ( p _ { s } ( t ) )$ for the safe merging distance between the merging CAV $m$ and assisted CAV $s$ is 

$$
\begin{array}{l} \Phi_ {m - s} \left(p _ {s} (t)\right) = k _ {1} \left(p _ {s} (t) - p _ {s} \left(t ^ {0}\right)\right) + b _ {1}, t \in \left[ t ^ {0}, t ^ {m} \right] \\ k _ {1} = \frac {\varphi_ {m e r} v _ {s} (t ^ {0}) + p _ {s} (t ^ {0}) + l _ {m e r}}{v _ {s} (t ^ {0}) (p _ {s} (t ^ {m}) - p _ {s} (t ^ {0}))} \\ b _ {1} = - \frac {p _ {s} \left(t ^ {0}\right) + l _ {m e r}}{v _ {s} \left(t ^ {0}\right)} \tag {27} \\ \end{array}
$$

Proof: see Appendix A. 

Theorem 2. The linear continuous function $\Phi _ { l - m } ( p _ { m } ( t ) )$ for the safe merging distance between the leading vehicle $l$ and merging CAV $m$ is 

$$
\begin{array}{l} \Phi_ {l - m} (p _ {m} (t)) = k _ {2} \left(p _ {m} (t) - p _ {m} (t ^ {0})\right) + b _ {2}, t \in \left[ t ^ {0}, t ^ {m} \right] \\ k _ {2} = \frac {v _ {m} (t ^ {0}) \varphi_ {m e r} - p _ {l} (t ^ {0}) + l _ {m e r}}{v _ {m} (t ^ {0}) p _ {m} (t ^ {m})} \\ b _ {2} = \frac {p _ {l} \left(t ^ {0}\right) - l _ {m e r}}{v _ {m} \left(t ^ {0}\right)} \tag {28} \\ \end{array}
$$

Proof: see Appendix B. 

The above two theorems give linear time headway functions in general form. Simplified ones are given in Corollary 1. 

Corollary 1. Let $l _ { m } ~ = ~ 0$ due to its limited effect on inter-vehicle distance when CAV speeds are high. Set the time headway for safe merging to zero at initial cooperation time $t ^ { 0 }$ . It makes sense because the merging vehicle and leading vehicle are on different roads initially, plus the safe merging distance constraint is supposed to be gradually intervene in CAV control to avoid sudden control switch at $t ^ { 0 }$ . Thus, $\Phi _ { l - m } ( p _ { m } ( t ^ { 0 } ) ) = \Phi _ { m - s } ( p _ { s } ( t ^ { 0 } ) ) = 0$ , which derives 

$$
\Phi_ {m - s} \left(p _ {s} (t)\right) = \frac {\varphi_ {\text {m e r}}}{p _ {s} \left(t ^ {m}\right) - p _ {s} \left(t ^ {0}\right)} \left(p _ {s} (t) - p _ {s} \left(t ^ {0}\right)\right) \tag {29a}
$$

$$
\Phi_ {l - m} \left(p _ {m} (t)\right) = \frac {\varphi_ {m e r} p _ {m} (t)}{p _ {m} \left(t ^ {m}\right)}, t \in \left[ t ^ {0}, t ^ {m} \right] \tag {29b}
$$

Corollary 2. To enable the FPM policy, we replace the $p _ { s } ( t ^ { m } )$ and $p _ { m } ( t ^ { m } )$ in (29a)-(29b) by the expected merging position $L _ { s } ^ { e x p }$ and $L _ { m } ^ { e x p }$ , which are derived from the upperlevel planner. Based on Corollary 1, we have 

$$
\begin{array}{l} \Phi_ {m - s} \left(p _ {s} (t), L _ {s} ^ {\exp}\right) = \frac {\varphi_ {m e r}}{L _ {s} ^ {\exp} - p _ {s} \left(t ^ {0}\right)} \left(p _ {s} (t) - p _ {s} \left(t ^ {0}\right)\right) (30a) \\ \Phi_ {l - m} \left(p _ {m} (t), L _ {m} ^ {\exp}\right) = \frac {\varphi_ {m e r} p _ {m} (t)}{L _ {m} ^ {\exp}}, t \in \left[ t ^ {0}, t ^ {m} \right] (30b) \\ \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/2eae744cc37b5909154be7658a4fe1fe785e1a82ad5408a95874cd5587d0ed59.jpg)



Fig. 4. Recursive updating principle for time headway value of the merging CAV $m$ . The upper half shows the relationship between variable time headway and vehicle position, while the lower half shows the relationship between vehicle position and time. Line segment OA, OB, OC, and OD (OE), whose terminal point A, B, C, and D (E) are dependent on flexible expected merging position (24a) at corresponding time $t ^ { 0 } + k \Delta t ( k = 0 , 1 , 2 . . . )$ , are defined by Corollary 2. The time headway value of point A’, B’, C’, D’, and $\mathrm { E } '$ are determined by (30b).


Remark 1: Corollary 2 embeds the flexible expected merging position into safe merging distance constraints via time-varying continuous time headway functions (30). 

Now we choose the merging CAV m as an example to explain how to recursively update the time headway value based on the proposed receding horizon control framework. The updating principle is depicted in Fig. 4. At initial cooperation time $t ^ { 0 }$ , $\Phi _ { l - m } = 0$ as we set. In the next recursive step, the upper-level planner plans an expected merging position $L _ { m } ^ { e x p } \bar { | ( t ^ { 0 } + \Delta t ) }$ at initial time $t ^ { 0 } + \Delta t$ , which determines terminal point B and hence slope of line segment OB as defined in Definition 2 and Corollary 2. The time headway value of point $\mathbf { B } ^ { \ast }$ is determined by (30b) dependent on the current position $p _ { m } ( t ^ { 0 } { + } \Delta t )$ . Then in the next several recursive steps, the time headway value is determined in the same way until states of CAV m satisfy merging requirements (13a) and (13c) at merging time $t ^ { m }$ . The updating principle of assisted CAV’s time headway is basically the same and we omit the explanation. 

Based on variable time headway (30b), the safety-critical and flexible distance constraints are written as (31). 

$$
\begin{array}{l} z _ {l - m} (t) \geq \Phi_ {l - m} \left(p _ {m} (t), L _ {m} ^ {e x p}\right) v _ {m} (t) + l _ {\text {m e r}} \\ = \frac {\varphi_ {\text {m e r}} p _ {m} (t)}{L _ {m} ^ {\exp}} v _ {m} (t) + l _ {m e r} \tag {31a} \\ \end{array}
$$

$$
\begin{array}{l} z _ {m - s} (t) \geq \Phi_ {m - s} \left(p _ {s} (t), L _ {s} ^ {e x p}\right) v _ {s} (t) + l _ {\text {m e r}} \\ = \frac {\varphi_ {\text {m e r}} \left(p _ {s} (t) - p _ {s} \left(t ^ {0}\right)\right)}{L _ {s} ^ {\exp} - p _ {s} \left(t ^ {0}\right)} v _ {s} (t) + l _ {\text {m e r}} \tag {31b} \\ \end{array}
$$

There are two prominent advantages of the revised safe merging constraints. On one hand, the revised constraints yield the benefit of achieving FPM policy and safety guarantee simultaneously. The other advantage of such a design is 

providing safe merging constraints with access to CBFs. Since the original constraints (6)-(7) are time discontinuous and only imposed at the merging time $t ^ { m }$ , they cannot be transformed to continuous CBF form. However, the revised time headway makes it feasible to formulate a CBF. Details of safety-critical and flexible merging CBFs will be given later. 

3) CBF-CLF-Based Method: CLFs are designed to stabilize system states to specified optimization objectives. 

Theorem 3. Control Lyapunov function (CLF) [30]: For a continuously differentiable function $V ( \pmb { x } ) : \mathbb { R } ^ { n }  \mathbb { R }$ , if there exist positive constants $\xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } > 0$ such that 

$$
\zeta_ {1} \| \boldsymbol {x} \| ^ {2} \leq V (\boldsymbol {x}) \leq \zeta_ {2} \| \boldsymbol {x} \| ^ {2} \tag {32a}
$$

$$
L _ {f} V (\boldsymbol {x}) + L _ {g} V (\boldsymbol {x}) u + \xi_ {3} V (\boldsymbol {x}) \leq \delta \tag {32b}
$$

for $\forall x \in \mathbb { R } ^ { n }$ , then $V ( { \pmb x } )$ is an exponentially stabilizing CLF. The $\delta > 0$ is a slack variable to make (32b) a soft constraint. 

CBFs aim to confine system states within a safe set bounded by multiple safety constraints. Consider a set $\mathcal { D }$ defined by (33) for a continuously differentiable function $d ( \pmb { x } ) : \mathbb { R } ^ { n }  \mathbb { R }$ 

$$
\mathcal {D} = \left\{\boldsymbol {x} \in \mathbb {R} ^ {n}: d (\boldsymbol {x}) \geq 0 \right\} \tag {33a}
$$

$$
\partial \mathcal {D} = \left\{\boldsymbol {x} \in \mathbb {R} ^ {n}: d (\boldsymbol {x}) = 0 \right\} \tag {33b}
$$

$$
\operatorname {I n t} (\mathcal {D}) = \left\{\boldsymbol {x} \in \mathbb {R} ^ {n}: d (\boldsymbol {x}) > 0 \right\} \tag {33c}
$$

Theorem 4. Control barrier function $\left( C B F \right) [ 3 0 ] .$ : A function $B ( d ( \pmb { x } ) ) : \mathcal { D }  \mathbb { R }$ is a control barrier function for an affine control system ${ \dot { x } } \ = \ f ( x ) + g ( x ) u$ if there exist class $\mathcal { \kappa }$ function $\rho _ { 1 } , \rho _ { 2 }$ and constant $\gamma > 0$ such that 

$$
\frac {1}{\rho_ {1} (d (\boldsymbol {x}))} \leq B (d (\boldsymbol {x})) \leq \frac {1}{\rho_ {2} (d (\boldsymbol {x}))} \tag {34a}
$$

$$
\frac {\partial B (d (\boldsymbol {x}))}{\partial t} + L _ {f} B (d (\boldsymbol {x})) + L _ {g} B (d (\boldsymbol {x})) u - \frac {\gamma}{B (d (\boldsymbol {x}))} \leq 0 \tag {34b}
$$

where $L _ { f }$ and $L _ { g }$ denote the Lie derivatives of $B ( d ( x ) )$ for system (1) along $f ( x )$ and $g ( x )$ , respectively. According to (34a), we take $\rho _ { 1 } ( d ( x ) ) ~ = ~ \rho _ { 2 } ( d ( x ) ) ~ = ~ d ( x ) ~ = ~$ $1 / B ( d ( x ) )$ , such that all control values satisfying (34b) render $\mathcal { D }$ safe, i.e., control invariant. Besides, we choose $\gamma = 1$ for all CBFs. 

With the aim of introducing flexible merging position into CBFs, we revise normal CBFs and define as below. 

Definition 3. Flexible Control Barrier Function (FCBF): For a CBF applied in a receding horizon framework, if there exists $d ( \boldsymbol { x } ( t ) , \mathcal { L } ( k ) )$ affected by state variable $x ( t )$ and recursively updated non-state variables $\begin{array} { l l } { { \mathcal { L } } ( k ) } & { : = } \end{array}$ $\{ L _ { 1 } ( k ) , L _ { 2 } ( k ) \ldots , L _ { n } ( k ) \} \in \mathbb { R } ^ { n }$ $\{ L _ { 1 } ( k )$ , where $k = 0$ , 1, 2, …is the recursive step number, such a CBF $B ( d ( { \pmb x } ( t ) , { \mathcal { L } } ( k ) ) )$ is called FCBF. 

Remark 2: FCBFs can be formulated based on timecontinuous safety-critical and flexible merging distance constraints (31), and hence bridge the gap between merging flexibility and safety. 

4) CBF/FCBF Design for Constraints: Speed Limitations: Let $d _ { 1 , \varsigma } ( \pmb { x } ( t ) ) = \upsilon _ { m a x } - \upsilon _ { \varsigma } ( t )$ for maximum speed limitation (4) of CAV. Since $d _ { 1 , \varsigma }$ satisfies (33), then according to (34b) 

we have the CBF control law (35). Similarly, let $d _ { 2 , \varsigma } ( \boldsymbol { x } ( t ) ) =$ $\upsilon _ { \varsigma } ( t ) - \upsilon _ { m i n }$ for minimum speed limitation (4). 

$$
\begin{array}{l} \underbrace {- F _ {r , \varsigma} \left(v _ {\varsigma} (t)\right)} _ {L _ {f} B _ {1, \varsigma}} + \underbrace {\frac {1}{M \left(v _ {\max } - v _ {\varsigma} (t)\right) ^ {2}}} _ {L _ {g} B _ {1, \varsigma}} u _ {\varsigma} (t) \\ - \left(v _ {\max } - v _ {\zeta} (t)\right) \leq 0 \tag {35} \\ \end{array}
$$

Safe car-following distance constraint (5): Let $d _ { 3 } ( { \pmb x } ( t ) ) =$ $z _ { l - s } ( t ) - \varphi _ { c f } \upsilon _ { s } ( t ) - l _ { c f }$ , we have the CBF control law 

$$
\begin{array}{l} \frac {v _ {l} (t) - v _ {s} (t)}{\underbrace {\left(z _ {l - s} (t) - \varphi_ {c f} v _ {s} (t) - l _ {c f}\right) ^ {2}} _ {\frac {\partial B _ {3} \left(d _ {3}\right)}{\partial t}}} \\ - \underbrace {\frac {\varphi_ {c f} F _ {r , s} (v _ {s} (t))}{M (z _ {l - s} (t) - \varphi_ {c f} v _ {s} (t) - l _ {c f}) ^ {2}}} _ {L _ {f} B _ {3}} \\ + \underbrace {\frac {\varphi_ {c f}}{M \left(z _ {l - s} (t) - \varphi_ {c f} v _ {s} (t) - l _ {c f}\right) ^ {2}}} _ {L _ {g} B _ {3} (d _ {3})} u _ {s} (t) \\ \leq \underbrace {z _ {l - s} (t) - \varphi_ {c f} v _ {s} (t) - l _ {c f}} _ {\frac {\gamma}{B _ {3} (d _ {3})}} \tag {36} \\ \end{array}
$$

Consider the situation where a CAV needs to decelerate with the minimum traction force i.e., $- c _ { d } M g$ , to keep a safe distance with its preceding vehicle. To avoid the conflict between safe distance constraints and the traction force constraint (3), we revise $d _ { 3 }$ with a minimum braking distance term [31], [39]. 

$$
d _ {3} ^ {\prime} (\boldsymbol {x}) = z _ {l - s} (t) - \varphi_ {c f} v _ {s} (t) - l _ {c f} - \frac {\left(v _ {s} (t) - v _ {l} (t)\right) ^ {2}}{2 c _ {d} g} \tag {37}
$$

Safety-critical and flexible merging distance constraints (31): In each recursive step, with consideration of avoiding traction force constraint conflicts, we have 

$$
\begin{array}{l} d _ {4, s} \left(\boldsymbol {x}, L _ {s} ^ {\exp}\right) = z _ {m - s} (t) - l _ {\text {m e r}} - \frac {\left(v _ {s} (t) - v _ {m} (t)\right) ^ {2}}{2 c _ {d} g} \\ - \Phi_ {m - s} \left(p _ {s} (t) + \frac {v _ {s} ^ {2} (t) - v _ {m} ^ {2} (t)}{2 c _ {d} g}, L _ {s} ^ {\exp}\right) v _ {s} (t) \tag {38} \\ \end{array}
$$

$$
\begin{array}{l} d _ {4, m} \left(\boldsymbol {x}, L _ {m} ^ {\exp}\right) = z _ {l - m} (t) - l _ {m e r} - \frac {\left(v _ {m} (t) - v _ {l} (t)\right) ^ {2}}{2 c _ {d} g} \\ - \Phi_ {l - m} \left(p _ {m} (t) + \frac {v _ {m} ^ {2} (t) - v _ {l} ^ {2} (t)}{2 c _ {d} g}, L _ {m} ^ {\exp}\right) v _ {m} (t) \tag {39} \\ \end{array}
$$

The reciprocals of (37)-(39) are the corresponding CBFs / FCBFs. Due to the limited space, CBF / FCBF control laws of (37)-(39) are not presented. 

5) CLF Design for Travel Efficiency Optimization: In Problem III and IV, the objective of minimizing travel time does not involve state variables, so it cannot be directly transformed into the CLF form. However, CAVs can achieve this objective indirectly by approaching the desired speed $v _ { d }$ as soon as possible. Define output $y _ { \varsigma } ( \pmb { x } ) : = \upsilon _ { \varsigma } - \upsilon _ { d }$ , choose Lyapunov 

function $V ( y _ { \varsigma } ( \pmb { x } ) ) = y _ { \varsigma } ^ { 2 } ( \pmb { x } )$ satisfying (32a) with $\xi _ { 1 } = \xi _ { 2 } = 1$ , and then we have the CLF control law 

$$
\begin{array}{l} \underbrace {- \frac {2 \left(v _ {\varsigma} (t) - v _ {d}\right)}{M} F _ {r , \varsigma} \left(v _ {\varsigma} (t)\right)} _ {L _ {f} V \left(y _ {\varsigma} (\boldsymbol {x})\right)} + \underbrace {\frac {2 \left(v _ {\varsigma} (t) - v _ {d}\right)}{M}} _ {L _ {g} V \left(y _ {\varsigma} (\boldsymbol {x})\right)} u _ {\varsigma} (t) \\ + \xi_ {3} \left(v _ {\varsigma} (t) - v _ {d}\right) ^ {2} \leq \delta_ {\varsigma} (t), \forall t \in \left[ t ^ {0}, t ^ {m} \right] \tag {40} \\ \end{array}
$$

6) CBF-CLF-Based Quadratic Programming Problem: 

Based on designed FCBFs, CBFs, and CLFs, we transform the OCP (Problem III and Problem IV) which optimizes state and control variables at the same time, to an optimization problem which only concerns system control variables. Recall the objective to minimize energy consumption and travel efficiency, the objective function is given as 

$$
\boldsymbol {q} ^ {*} = \underset {u _ {\varsigma} (t), \delta_ {\varsigma} (t)} {\operatorname {a r g m i n}} \left(\frac {u _ {\varsigma} (t) - F _ {r , \varsigma} \left(v _ {\varsigma} (t)\right)}{M}\right) ^ {2} + \omega_ {q} \delta_ {\varsigma} ^ {2} (t) \tag {41}
$$

where $\omega _ { q }$ is the penalty for travel efficiency slack variable $\delta _ { \varsigma }$ 

Reformulate the problem of each CAV into a discrete quadratic programmer (QP) in a unified form as 

$$
\begin{array}{l} \underset {\boldsymbol {q} (t)} {\operatorname {a r g m i n}} Q (\boldsymbol {q} (t)) = \frac {1}{2} \boldsymbol {q} (t) ^ {T} \boldsymbol {H} \boldsymbol {q} (t) + J ^ {T} \boldsymbol {q} (t) \\ \boldsymbol {q} (t) = \left[ \begin{array}{c} u _ {\varsigma} (t) \\ \delta_ {\varsigma} (t) \end{array} \right], \boldsymbol {H} = \left[ \begin{array}{c c} \frac {2}{M ^ {2}} & 0 \\ 0 & 2 \omega_ {q} \end{array} \right], \\ \boldsymbol {J} = \left[ - \frac {2 F _ {r , \varsigma} \left(v _ {\varsigma} (t)\right)}{M ^ {2}} 0 \right] \tag {42} \\ \end{array}
$$

subject to 

(a) Traction force constraint (3) 

(b) CBF/FCBF control constraints (34a) generated from: 

$d _ { 1 , m } , d _ { 2 , m } , d _ { 4 , m }$ , for merging CAV $( \varsigma = m$ ), 

$d _ { 1 , s } , d _ { 2 , s } , d _ { 3 } ^ { \prime } , d _ { 4 , s }$ for assisted CAV $\zeta = s \mathrm { i }$ 

(c) CLF control constraint (40) 

Remark 3: The formulated quadratic programmer is able to realize safety and optimization simultaneously, which means both the upper-level planner and lower-level controller play a role in improving traffic performance. 

In each receding horizon, the cooperative control strategy plans the expected merging position by solving Problem II in the upper level and control optimal trajectories of each CAV by solving QPs of Problem III and Problem IV. The receding procedures are repeated until the merging requirements are met. 

# IV. SIMULATION RESULTS AND DISCUSSION

Two on-ramp merging simulation studies are conducted in this section. Section IV-A presents a single-TCG scenario simulation, where the merging and assisted vehicles are controlled by the proposed flexible cooperative on-ramp merging control strategy. The results of the proposed strategy are compared with two cooperative merging control strategies, which use the PPM policy. The second simulation, presented in Section IV-B, focuses on the merging performance evaluation in multiple vehicles driving scenario. In Case B-1, we simulate in a multi-HDV traffic, while in Case B-2, we consider the 

scenario where only the leading vehicle is the HDV. Note that in existing relevant studies, none of them has compared PPM policy with FPM policy. 

To compare the energy consumption between different control strategies, the fuel consumption model (43) is used [40], including fuel consumption rate $f _ { c r u , \varsigma } \left( t \right)$ driving with constant speed and additional fuel consumption rate $f _ { a c c , \varsigma } ( t )$ caused by acceleration. 

$$
\operatorname {F u e l} _ {\varsigma} = \int_ {t ^ {0}} ^ {t ^ {m}} \left(f _ {c r u, \varsigma} (t) + f _ {a c c, \varsigma} (t)\right) d t \tag {43a}
$$

$$
f _ {c r u, \varsigma} (t) = \vartheta_ {0} + \vartheta_ {1} v _ {\varsigma} (t) + \vartheta_ {2} v _ {\varsigma} ^ {2} (t) + \vartheta_ {3} v _ {\varsigma} ^ {3} (t) \tag {43b}
$$

$$
f _ {\mathrm {a c c}, \varsigma} (t) = a _ {\varsigma} (t) \left(\sigma_ {0} + \sigma_ {1} v _ {\varsigma} (t) + v _ {\varsigma} ^ {2} (t)\right) \tag {43c}
$$

where the fuel consumption coefficients $\vartheta _ { 0 } , \vartheta _ { 1 } , \vartheta _ { 2 }$ and $\vartheta _ { 3 }$ are 0.1569 mL/s, $0 . 0 2 4 5 \mathrm { m L / m }$ , $- 7 . 4 1 5 \times 1 0 ^ { - 4 } \mathrm { \ m L \cdot s / m ^ { 2 } }$ and $5 . 9 7 5 \times 1 0 ^ { - 5 } \mathrm { ~ m L } \cdot \mathrm { s } ^ { 2 } / \mathrm { m } ^ { 3 }$ . The fuel consumption coefficients $\sigma _ { 0 } , \sigma _ { 1 }$ and $\sigma _ { 2 }$ are $7 . 2 2 4 \times 1 0 ^ { - 2 } \mathrm { m L \cdot s / m }$ , $9 . 6 8 1 \times 1 0 ^ { - 2 } \mathrm { m L }$ · $\mathrm { s } ^ { 2 } / \mathrm { m } ^ { 2 }$ and $1 . 0 7 5 \times 1 0 ^ { - 3 } \mathrm { m L } \cdot \mathrm { s } ^ { 3 } / \mathrm { m } ^ { 3 }$ . When $a _ { \varsigma } ( t ) < 0$ , the fuel consumption is assumed to be 0. 

The length of the acceleration lane is $4 0 0 \mathrm { ~ m ~ }$ . The trigger position is located at the entrance of acceleration lane, i.e., the parameter $L$ equals to $4 0 0 \mathrm { ~ m ~ }$ . The main parameters for the vehicle and controller are listed in Table II and Table III. 

# A. Case A: Single TCG

In this case, only one TCG exists. The initial states of vehicles are listed in Table IV. 

The leading vehicle is driven by human driver, and we use the sinusoidal function (44) to simulate its trajectory. 

$$
v _ {l} (t) = 2 0 \times \left(1 - \frac {1}{6} \sin \frac {\pi}{2 0} t\right) \tag {44a}
$$

$$
p _ {l} (t) = 5 8 + 2 0 \times \left(1 + \frac {1 0}{3 \pi} \cos \frac {\pi}{2 0} t\right) - \frac {2 0 0}{3 \pi} \tag {44b}
$$

We compare the proposed flexible cooperative on-ramp merging control strategy (named FPM-FCBF) with two cooperative strategies using the PPM policy. One uses PMP to solve an unconstrained OCP [22], named PPM-OC. The other employs the fixed merging position strategy and the CBF-CLF based control method similar to FPM-FCBF, called PPM-CBF. The difference between PPM-CBF and FPM-FCBF lies in the reference merging position, since the time headway of the former one relies on flexible merging position (29) while that of the latter relies on fixed merging position (30). The fixed merging position of PPM strategies is defined at the end of acceleration lane, i.e., $p _ { m } ( t ^ { m } ) = 4 0 0 ~ \mathrm { m }$ . 

1) Simulation Results of PPM-OC: As discussed in Section I, most existing papers transform the on-ramp merging control problem into an unconstrained OCP and prespecifies fixed merging position and merging timing. We adopt a strategy like [22], in which PMP is used to solve the OCP, and the merging time $t ^ { m }$ for each CAV is specified recursively according to the predicted merging time $t _ { p r e } ^ { m }$ of its preceding vehicle, i.e., each CAV keeps a certain merging time gap with its preceding vehicle at the fixed merging position. $t _ { p r e } ^ { m }$ is updated recursively by assuming the speed of the preceding 


TABLE II VEHICLE PARAMETER SETTINGS


<table><tr><td>Parameters</td><td>Description</td><td>Value</td></tr><tr><td>α0</td><td>Resistance coefficient</td><td>0.1 kg·m/s2</td></tr><tr><td>α1</td><td>Resistance coefficient</td><td>5 kg/s</td></tr><tr><td>α2</td><td>Resistance coefficient</td><td>0.25 kg/m</td></tr><tr><td>M</td><td>Mass</td><td>1665 kg</td></tr><tr><td>g</td><td>Gravity coefficient</td><td>9.8 m/s2</td></tr><tr><td>ca</td><td>Acceleration coefficient</td><td>0.3</td></tr><tr><td>cd</td><td>Deceleration coefficient</td><td>0.5</td></tr><tr><td>vmin</td><td>Minimum speed</td><td>10 m/s</td></tr><tr><td>vmax</td><td>Maximum speed</td><td>30 m/s</td></tr><tr><td>vd</td><td>Desired speed</td><td>30 m/s</td></tr><tr><td>φcf</td><td>Constant car-following time headway</td><td>1.8 s [35]</td></tr><tr><td>φmer</td><td>Constant merging time headway</td><td>1.8 s [35]</td></tr></table>


TABLE III CONTROL PARAMETERS


<table><tr><td>Parameter</td><td>Symbol</td><td>Value</td></tr><tr><td>Exponential convergence rate</td><td>ξ3</td><td>10</td></tr><tr><td>Travel efficiency penalty</td><td>ωq</td><td>1</td></tr><tr><td>Receding horizon sampling time</td><td>Δt</td><td>0.1 s</td></tr><tr><td>Maximum allowable inter-vehicle distance deviation</td><td>Δzmax</td><td>3 m</td></tr><tr><td>Maximum allowable relative speed deviation</td><td>Δvmax</td><td>1 m/s</td></tr></table>


TABLE IV INITIAL CONDITIONS


<table><tr><td>Vehicle role</td><td>Denotation</td><td>Initial position (m)</td><td>Initial speed (m/s)</td></tr><tr><td>Leading vehicle</td><td>HDV</td><td>pl(0) = 58</td><td>vl(0) = 20</td></tr><tr><td>Merging vehicle</td><td>CAV1</td><td>pm(0) = 0</td><td>vm(0) = 10</td></tr><tr><td>Assisted vehicle</td><td>CAV2</td><td>ps(0) = -15</td><td>vs(0) = 20</td></tr></table>

vehicle is constant in each planning horizon. The merging time gap is set to 1.8s, then $t ^ { m } = t _ { p r e } ^ { m } + 1 . 8$ . 

Fig. 5 shows the simulation results. As observed, the merging vehicle (CAV1) arrives at the fixed merging position within the prespecified moment, and inter-vehicle distances of the three vehicles are sufficient. However, when the merging CAV gets close to the merging position at around 21s, huge acceleration occurs, which exceeds the control capability. The possible reason for the results is the uncertainty of the leading HDV making the assisted vehicle (CAV2) hard to reach the fixed merging position exactly at the prespecified merging time, unless adopting aggressive operations. Therefore, we need to give more flexibility to CAVs to choose more flexible merging opportunities, i.e., using the FPM policy. 

In addition, due to computational complexity considerations, constraints are always ignored. Nevertheless, it may put CAVs into danger. As shown in Fig. 5(a), since CAV2 surpasses CAV1 for a period, it is doubted that CAV2 may collide with HDV in the same lane if the initial distance is small, i.e., violating the system safety requirements [20]. On the contrary, the proposed strategy based on CBF-CLF based 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/f4da8d00d05da9555a26e28d1a5ba95bc78ebcded15366ad8736224090cc9477.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/e95145969454a4f322792f4f6c16e5a63a518d4a0c94fac6daeb9d9a7d9ee818.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/d7a6ebf89ac598c4f1fa27cb86c901f824b2d764561a49bf2433a6d30f35e54f.jpg)



(c)



Fig. 5. Simulation results of PMP-OC: (a)Position, (b)Speed, (c) Acceleration.


control method can always ensure safety and be applied in real time. 

2) Comparison Between PPM-CBF and FPM-FCBF: Compared to the PPM-OC strategy, PPM-CBF and FPM-FCBF both consider the safety-critical constraints and vehicle dynamics. As a result, the safety-guaranteed solutions are derived to control the CAVs safely. The main difference between PPM-CBF and FPM-FCBF is fixed or flexible merging position, i.e., the safe merging time headway $\Phi _ { m - s }$ and $\Phi _ { l - m }$ are different for the two strategies. 

Figs. 6 and 7 show the simulation results of FPM-FCBF and PPM-CBF. In general, both strategies yield similar cooperative merging control process. The control constraint and reference inter-vehicle merging distance are depicted in Figs. 6 and 7(d)-(e). As observed, the initial inter-vehicle distances and relative speeds are adjusted to meet the merging requirement (13). 

In Fig. 6, at the beginning, the merging CAV1 has a low initial speed and its distance to the leading HDV is large, thus CAV1 accelerate with its maximum traction force to shorten the relative speed and distance gaps as soon as possible. During the acceleration stage, the distance between CAV1 and HDV increases firstly and then decreases after the speed of CAV1 exceeds that of HDV. When the actual inter-vehicle distance approaches the required distance, CAV2 begins to decelerate to maintain a suitable merging distance and relative speed until the merging requirements are all satisfied. 

For the assisted CAV2, it keeps suitable distances with the leading and merging vehicles. At the beginning, CAV2 decelerates to expand the distance between CAV2 and CAV1 because the initial distance is small. The CAV1-CAV2 distance converges to the required distance boundary before 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/edf9267f7fad7e45aa188ebe3eb5229006d92587db7d8091aa2c34a5e7659c79.jpg)



(a) Position


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/735a9f437441ca2c466278b637ad820c3d2742c19d016fdc4ca1a2a1c5bfbc4e.jpg)



(b) Speed


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/cc5995781e00d9e25314eac6578896f10c9660fd75a25ca67d03ccf55ea21197.jpg)



(c) Acceleration


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/9ae23da51d8511e407f864b7bbb9908472d1d1daddc00268f6af43eedbc6de1e.jpg)



(d) Traction Force


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/ca405f5f568c87658036ebcdf4ed2e27f6bef41f2df9dd06d9b50c942e5df741.jpg)



(e) Inter-Vehicle Distance



Fig. 6. Simulation results of FPM-FCBF for one TCG scenario.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/b40525eec83ec56d7ce921833764a346e84b928fb67ccc3de0b14f96d6c6c4e2.jpg)



(a)Position


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/720af1e8bba50a0a06251ac1070c49066f784e83bbdaa42237a2a9644a36a2ce.jpg)



(b) Speed


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/2d48d5521ce706f414e9f08d339b4f11ee49e34896282a1b9901afa8db6ed79c.jpg)



(c) Acceleration


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/bda0792736224f02603368c7b0c950ce3902ab225f212593a973e3f02cd466b6.jpg)



(d) Traction Force


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/a4148d792935fd4616e28eb390d18d8833682f119c9329a99c06dbf4df43685f.jpg)



(e) Inter-Vehicle Distance



Fig. 7. Simulation results of PPM-CBF for one TCG scenario.


4s. Since then, CAV2 adjusts its speed to follow the reference inter-vehicle merging distance. Finally, CAV1 executes the merging maneuver when all merging requirements are met. 

Fig. 8 shows the expected merging position (28) calculated by the upper-level planner and its corresponding time headway defined in Eq. (30). Since the expected merging position is affected by the states of CAV2, the reduced CAV2 speed and increasing HDV-CAV2 distance cause an increase in the expected merging position. Similarly, the acceleration of CAV2 leads to decrease of expected position. In addition, the time headway between HDV and CAV1 $( \Phi _ { m - s } )$ , and CAV1 and CAV2 $( \Phi _ { l - m } )$ , both keep increasing during the whole process, and approach to the constant value 1.8, which is defined in safe merging condition Eqs. (11) and (12). $\Phi _ { m - s }$ is higher than $\Phi _ { l - m }$ during the first 8 seconds because the higher initial speed of CAV2 makes the travel distance of CAV2 account for a larger proportion of its expected merging distance. Note that, although time headways do not strictly reach 1.8 at the merging time, the merging requirement (13) can still ensure CAVs merge in a safe condition, as shown in Fig. 6 (b), (e). 

However, compared to FPM-FCBF, because of the fixed merging position is relatively lagging than the expected one, PPM-CBF always makes CAVs execute redundant operations and lose earlier merging opportunities as depicted in Fig. 7. At the first 7 seconds, the reference merging distance increase slower, which makes the travel efficiency objective (40) of CAVs dominate over a period of time, and further results in redundant acceleration and excessive peak speed of CAVs (see Fig. 7(b)-(c)) compared to the FPM-FCBF strategy. Fig. 7(e) shows that before 12s, the inter-vehicle distances have converged to the reference merging distance, and the speeds of three vehicle are nearly the same. It is obvious that the merging CAV1 could merge into the main lane at this moment (around 12s). However, PPM-CBF enforces CAV1 to 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/94f48fdfb894efe121f58bc74b42eb3cc97f4ded8254eb2e6f74632164a5ccf6.jpg)



(a) Expected merging position


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/edb40ccc6020705b80019f730fa42ec51b6f537ab31226fd8fa0ff81998d1cb5.jpg)



(b) Time headway



Fig. 8. Expected merging position (24) and corresponding time headway (30) of safe merging constraint (6)-(7) in the FPM-FCBF strategy.


merge at the end of the acceleration lane. As a result, PPM-CBF may miss the early merging opportunities and execute redundant operation. As CAVs keep approaching the fixed merging position, the merging time headway keeps growing, thus, each CAV has to decelerate to keep a speed gap between its preceding vehicle to satisfy the reference inter-vehicle merging distance as shown in Fig. 7(b) and (e). Such a speed gap is unfavorable because after merging successfully, CAVs still need to accelerate to keep a stable distance with the leading vehicle, which will incur excessive energy consumption. Besides, the big speed reduction of CAV2 may worsen the upstream traffic efficiency. 

Fig. 9 illustrates the merging control duration, merging position, and fuel consumption of the two strategies. The speed color bars of CAVs present that the FPM-FCBF yields a short but efficient merging process. As a result, the FPM-FCBF strategy compresses $4 9 . 2 8 \%$ merging duration, and shortens $4 9 . 9 8 \%$ and $4 5 . 9 0 \%$ merging travel distance of CAV2 and CAV1, respectively. In terms of economic performance, the fuel consumptions of CAV1 and CAV2 are saved by $2 2 . 6 7 \%$ and $4 9 . 4 9 \%$ , respectively, and the corresponding total consumption is saved by $3 2 . 3 3 \%$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/24a33643cb40a9d19927284c9ccf88328c3810f17493afdc6314a43f6364d68b.jpg)



Fig. 9. Comparison of FPM-FCBF and PPM-CBF for a single-TCG scenario.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/744e083c8238d257db636e33fe6a9602cca6a5fa0ab0a8d725acd4e624b490ba.jpg)



Fig. 10. The speed profile of the leading HDV in Case B.


All simulations are carried out on a desktop computer with an Intel CORETM i7-9700K CPU @ 3.60GHz. The software MATLAB (R2021b) is implemented, in which the “vpasolve” function is used to solve Eqs. (22) and the “quadprog” function for solving QP problems (42). Computation time for each recursive step is less than 0.06s, which is within the sampling time 0.1s. 

In summary, the proposed FPM-FCBF strategy could be implemented in real time, and outperforms other two strategies in improving travel efficiency and fuel economy. 

# B. Case B: Multiple Merging Vehicles

In Case B, two sub-case studies are conducted. In Case B-1, a multi-HDV mixed traffic scenario is simulated. In Case B-2, only the leading vehicle is HDV, and the remaining 26 mainlane followers and 3 on-ramp merging vehicles are CAVs. 

In both cases, the speed profile of the leading vehicle is presented in Fig. 10, which depicts that a vehicle slows down when entering the on-ramp merging area and accelerates to its maximum speed after driving through the on-ramp. 

1) Case B-1: Multiple HDVs: In this case, we want to evaluate the effectiveness of the proposed cooperative on-ramp merging control strategy (FPM-FCBF) in a multi-HDV mixed traffic, including 3 on-ramp merging CAVs, 3 corresponding following main-lane CAVs, and 14 main-lane HDVs. We set initial speeds of vehicles (except the leading HDV) as random values, i.e., $2 0 { \pm } 2 \ \mathrm { m / s }$ for the main-lane vehicles and $1 0 { \pm } 2$ $\mathrm { m } / \mathrm { s }$ for the on-ramp merging vehicles. All the vehicles are imposed to follow the first-in-first-out (FIFO) policy [41], i.e., each vehicle leaves the merging coordination zone in the same order it enters. 

FPM-FCBF is applied to control the merging CAVs and their corresponding following main-lane CAVs, i.e., 3 TCGs in the mixed traffic. Note that, once a TCG complete merging 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/1159469c22e7c117f143b3975c8a7edb614fc31f00a74cd65f74bc02412116ea.jpg)



(a) Speed


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/984de4e9925a727d4a7dd98dc6414a05b85f1cb2a1c8bdd0f2ed19bfe584ed9a.jpg)



(b) Position



Fig. 11. Simulation results of NC when multiple HDVs exist.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/c21942b76dc2195389ea1a32fad9ce6b68a0780a90fe4bed6092103ffb8fc1f5.jpg)



(a) Speed


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/7438a43e009fb4be025b8a16140e6a0ecaaf6f914d0a345e0327f9bb9824b74c.jpg)



(b) Position



Fig. 12. Simulation results of FPM-FCBF when 3 TCGs exists in a multi-HDV traffic.


control, the CAVs of this TCG switch to the car-following mode based on the CBF-CLF based control method. For comparison, a non- cooperative strategy (NC) is simulated. Except the leading vehicle, all vehicles are modeled as the commonly used Intelligent Driver Model (IDM) [42]. 

Simulation results are shown in Figs. 11 and 12, including acceleration, speed, and position profiles. As observed in Fig. 11, the speed reductions occur when an on-ramp vehicle mergesinto the main road. The existing bottleneck may cause serious traffic issues, such as jam and crashes. On the contrary, although FPM-FCBF prefers violent actions to shorten the speed or inter-vehicle distances quickly, the traffic shock wave caused by the leading vehicle is alleviated by the cooperative control of on-ramp and main-lane CAVs. As a result, the traffic speed and efficiency in this bottleneck are improved a lot, as shown in the orange and red part of Fig. 12(b). 

2) Case B-2: One Leading HDV: In addition, we also compare FPM-FCBF and PPM-CBF in a multi-CAV scenario, in which only leading vehicle is HDV, and other vehicles are CAVs. Since CAVs are controllable, the initial speeds of main-lane CAVs and on-ramp CAVs are $2 0 \mathrm { m / s }$ and $1 5 \mathrm { m / s }$ , respectively. 

Recall that in FPM-FCBF, when arriving at the TP, each merging CAV will ask the coordinator to organize a TCG by selecting a main-lane CAV as the assisted CAV. The ungrouped main-lane CAVs will execute the car-following operation based on the CBF-CLF based method. Once the on-ramp vehicle completes merging, the CAVs of TCGs will also be driven in car-following mode. 

Figs. 13 and 14 depict the simulation results of Case B-2, including the acceleration, speed and position profiles. As can be seen, all on-ramp CAVs (red lines) merge into the main road safely. In addition, the speed wave introduced by the leading HDV is gradually reduced with the controlling of followed CAVs. Fig. 13(b) also shows that all vehicles travel smoothly, and the speed reduction caused by the leading vehicle spreading to the upstream is mitigated smoothly. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/cb385787a256f34ac082a7a328fa16972e5c91e4064cabd71d42cb2d5678f918.jpg)



(a) Speed


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/bc3a0ec5b78ff031fee3e965c44bc2744e2fe4373d59ecbbf743ee7ebbfdd884.jpg)



(b) Position



Fig. 13. Simulation results of FPM-FCBF in a multi-CAV scenario.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/eeccdf41ae5fad37003ed1ae86bd2741435938c974e642b191b870ad5a94a573.jpg)



(a) Speed


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/430382664eb9225954688e8acacaf741a36948c9b79b034827304e0dbebccf0f.jpg)



(b) Position



Fig. 14. Simulation results of PPM-CBF in a multi-CAV scenario.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/fa58e51a26d29785b3f0aace7cf38407d9774d1c33443a85b4612dc08a9c1248.jpg)



Fig. 15. Average fuel consumption comparison of FPM-FCBF and PPM-CBF in a multi-CAV scenario.


By comparing the results of FPM-FCBF and PPM-CBF, the traffic shock wave of PPM-CBF is worse than FPM-FCBF. The speed variation of PPM-CBF is also bigger than that of FPM-FCBF. Specifically, in Fig. 14(b), a great speed variation occurs before merging, e.g., the 2nd or 3rd merging vehicle. This is mainly because the controller requires the merging vehicle keeping a close speed with its preceding one for the traffic efficiency concern (the orange part before $4 0 0 \mathrm { m }$ in Fig. 14(b). However, the safe merging constraint gets stricter while merging, the speed reduction takes place (the deep blue part before $4 0 0 \mathrm { m }$ in Fig. 14(b). Although the speed reduction is mitigated gradually with the help of other CAVs, hence the speed wave is limited in a certain range, which is better than the full-CAV scenario, PPM-CBF may bring traffic problems due to bigger and wider speed and acceleration variations. 

In addition, we also compare the average fuel consumption of FPM-FCBF and PPM-CBF, as shown in Fig. 15. FPM-FCBF achieves more than $10 \%$ fuel consumption reduction within $1 0 0 0 \mathrm { m }$ travel range, compared to PPM-CBF. 

# V. CONCLUSION

In this paper, a safety-critical and flexible cooperative control strategy is developed to improve travel efficiency and fuel economy of CAVs at highway on-ramp merging area in mixed traffic. The cooperative on-ramp merging control is decomposed into two levels. The upper level plans the flexible expected merging position by solving a free terminal OCP 

using PMP, while the lower level optimizes the safety-critical trajectories by solving a CBF-CLF based QP problem. The FCBF is a bridge connecting the two levels through the time-varying expected merging position and variant time headway. In addition, the whole cooperative control procedures are recursively updated to tackle the disturbance incurred by the uncertainty of HDVs. 

The proposed cooperative on-ramp merging control strategy (FPM-FCBF) is verified in numerous simulations. First, a single-TCG scenario simulation is conducted. By comparing to two PPM strategies, i.e., PPM-OC and PPM-CBF, the FPM-FCBF reduce vehicle travel time and fuel economy while meeting the safety constraints. Second, the multiple merging vehicle scenario is simulated. Results reveal that FPM-FCBF is beneficial for tracking speeds of the preceding vehicles and mitigating speed reduction, thus has potential in improving traffic efficiency in mixed traffic compared to noncooperative situation. Moreover, the full-CAV scenario indicates that FPM-FCBF outperforms PPM-CBF in attenuating traffic shock waves and reducing fuel consumption. 

Several prospects of future study have been planned. First, the influence of CAV penetration and traffic density will be considered. Second, although we have illustrated the effectiveness of our proposed merging control strategy, a comprehensive work including the merging sequence optimization based on our proposed control strategy is worth studying to further explore the optimization potential. Third, it could be interesting to take inter-vehicle interactions, e.g., nudge maneuvers, into account to make merging (lane change) more flexible. Fourth, a data-driven trajectory prediction model for HDVs will be studied in our future research. 

# APPENDIX

# A. Proof of Theorem 1

For moment $t ^ { 0 }$ , the merging vehicle arrives at TP and its position is $p _ { m } ( t ^ { 0 } ) = 0$ . The distance between the merging and assisted CAV at $t ^ { 0 }$ 

$$
\begin{array}{l} z _ {m - s} \left(t ^ {0}\right) = p _ {m} \left(t ^ {0}\right) - p _ {s} \left(t ^ {0}\right) = 0 - p _ {s} \left(t ^ {0}\right) \\ = \Phi_ {m - s} \left(p _ {s} \left(t ^ {0}\right)\right) v _ {s} \left(t ^ {0}\right) + l _ {m e r} \tag {A.1} \\ \end{array}
$$

yields 

$$
\Phi_ {m - s} \left(p _ {s} \left(t ^ {0}\right)\right) = - \frac {p _ {s} \left(t ^ {0}\right) + l _ {m e r}}{v _ {s} \left(t ^ {0}\right)} \tag {A.2}
$$

At the time instant $t ^ { m }$ , the distance of them is supposed to be at least $z _ { m - s } ( t ^ { m } ) = l _ { m e r } + \varphi _ { m e r } \upsilon _ { s } ( t ^ { m } )$ , i.e., 

$$
\Phi_ {m - s} \left(p _ {s} \left(t ^ {m}\right)\right) = \varphi_ {m e r} \tag {A.3}
$$

According to (A.2) and (A.3), we have 

$$
\begin{array}{l} \Phi_ {m - s} \left(p _ {s} (t)\right) = \frac {\varphi_ {m e r} - \left(- \frac {p _ {s} \left(t ^ {0}\right) + l _ {m e r}}{v _ {s} \left(t ^ {0}\right)}\right)}{p _ {s} \left(t ^ {m}\right) - p _ {s} \left(t ^ {0}\right)} \left(p _ {s} (t) - p _ {s} \left(t ^ {0}\right)\right) \\ - \frac {p _ {s} \left(t ^ {0}\right) + l _ {m e r}}{v _ {s} \left(t ^ {0}\right)}, t \in \left[ t ^ {0}, t ^ {m} \right] \tag {A.4} \\ \end{array}
$$

which derives (27), and the proof is complete. - 

# B. Proof of Theorem 2

The distance between the leading vehicle and merging CAV at $t ^ { 0 }$ 

$$
\begin{array}{l} z _ {l - m} \left(t ^ {0}\right) = p _ {l} \left(t ^ {0}\right) - p _ {m} \left(t ^ {0}\right) = p _ {l} \left(t ^ {0}\right) - 0 \\ = \Phi_ {l - m} \left(p _ {m} \left(t ^ {0}\right)\right) v _ {m} \left(t ^ {0}\right) + l _ {m e r} \tag {B.1} \\ \end{array}
$$

yields 

$$
\Phi_ {l - m} \left(p _ {m} \left(t ^ {0}\right)\right) = \frac {p _ {l} \left(t ^ {0}\right) - l _ {m e r}}{v _ {m} \left(t ^ {0}\right)} \tag {B.2}
$$

At the time instant $t ^ { m }$ , 

$$
\Phi_ {l - m} \left(p _ {m} \left(t ^ {m}\right)\right) = \varphi_ {m e r} \tag {B.3}
$$

Then we have (28) according to (B.2)-(B.3), and the proof is complete. 

# REFERENCES



[1] S. Feng, X. Yan, H. Sun, Y. Feng, and H. X. Liu, “Intelligent driving intelligence test for autonomous vehicles with naturalistic and adversarial environment,” Nature Commun., vol. 12, no. 1, pp. 1–14, Feb. 2021. 





[2] X. Di and R. Shi, “A survey on autonomous vehicle control in the era of mixed-autonomy: From physics-based to AI-guided driving policy learning,” Transp. Res. C, Emerg. Technol., vol. 125, Apr. 2021, Art. no. 103008. 





[3] N. Lu, N. Cheng, N. Zhang, X. Shen, and J. W. Mark, “Connected vehicles: Solutions and challenges,” IEEE Internet Things J., vol. 1, no. 4, pp. 289–299, Aug. 2014. 





[4] J. Ma, X. Li, F. Zhou, J. Hu, and B. B. Park, “Parsimonious shooting heuristic for trajectory design of connected automated traffic Part II: Computational issues and optimization,” Transp. Res. B, Methodol., vol. 95, pp. 421–441, Jan. 2017. 





[5] W. Zhuang, L. Xu, and G. Yin, “Robust cooperative control of multiple autonomous vehicles for platoon formation considering parameter uncertainties,” Automot. Innov., vol. 3, no. 1, pp. 88–100, 2020. 





[6] K. Xu, C. G. Cassandras, and W. Xiao, “Decentralized time and energyoptimal control of connected and automated vehicles in a roundabout,” in Proc. IEEE Int. Intell. Transp. Syst. Conf. (ITSC), Indianapolis, IN, USA, Sep. 2021, pp. 681–686. 





[7] C. Sun, J. Guanetti, F. Borrelli, and S. J. Moura, “Optimal ecodriving control of connected and autonomous vehicles through signalized intersections,” IEEE Internet Things J., vol. 7, no. 5, pp. 3759–3773, May 2020. 





[8] J. Zhu and I. Tasic, “Safety analysis of freeway on-ramp merging with the presence of autonomous vehicles,” Accident Anal. Prevention, vol. 152, Mar. 2021, Art. no. 105966. 





[9] Z. Wang, Y. Bian, S. E. Shladover, G. Wu, S. E. Li, and M. J. Barth, “A survey on cooperative longitudinal motion control of multiple connected and automated vehicles,” IEEE Intell. Transp. Syst. Mag., vol. 12, no. 1, pp. 4–24, Spring 2020. 





[10] A. A. Malikopoulos, L. Beaver, and I. V. Chremos, “Optimal time trajectory and coordination for connected and automated vehicles,” Automatica, vol. 125, Mar. 2021, Art. no. 109469. 





[11] Y. Xue, C. Ding, B. Yu, and W. Wang, “A platoon-based hierarchical merging control for on-ramp vehicles under connected environment,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 11, pp. 21821–21832, Nov. 2022, doi: 10.1109/TITS.2022.3175967. 





[12] J. Rios-Torres and A. A. Malikopoulos, “A survey on the coordination of connected and automated vehicles at intersections and merging at highway on-ramps,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 5, pp. 1066–1077, May 2017. 





[13] N. Chen, B. Van Arem, T. Alkim, and M. Wang, “A Hierarchical model-based optimization control approach for cooperative merging by connected automated vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 22, no. 12, pp. 7712–7725, Dec. 2021. 





[14] J. Rios-Torres and A. A. Malikopoulos, “Automated and cooperative vehicle merging at highway on-ramps,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 4, pp. 780–789, Apr. 2017. 





[15] J. Ding, L. Li, H. Peng, and Y. Zhang, “A rule-based cooperative merging strategy for connected and automated vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 21, no. 8, pp. 3436–3446, Aug. 2020. 





[16] S. Jing, F. Hui, X. Zhao, J. Rios-Torres, and A. J. Khattak, “Cooperative game approach to optimal merging sequence and on-ramp merging control of connected and automated vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 20, no. 11, pp. 4234–4244, Nov. 2019. 





[17] H. Xu, S. Feng, Y. Zhang, and L. Li, “A grouping-based cooperative driving strategy for CAVs merging problems,” IEEE Trans. Veh. Technol., vol. 68, no. 6, pp. 6125–6136, Jun. 2019. 





[18] I. A. Ntousakis, I. K. Nikolos, and M. Papageorgiou, “Optimal vehicle trajectory planning in the context of cooperative merging on highways,” Transp. Res. C, Emerg. Technol., vol. 71, pp. 464–488, Oct. 2016. 





[19] S. Fukuyama, “Dynamic game-based approach for optimizing merging vehicle trajectories using time-expanded decision diagram,” Transp. Res. C, Emerg. Technol., vol. 120, Nov. 2020, Art. no. 102766. 





[20] W. Xiao and C. G. Cassandras, “Decentralized optimal merging control for connected and automated vehicles with safety constraint guarantees,” Automatica, vol. 123, Jan. 2021, Art. no. 109333. 





[21] J. I. Ge, S. S. Avedisov, C. R. He, W. B. Qin, M. Sadeghpour, and G. Orosz, “Experimental validation of connected automated vehicle design among human-driven vehicles,” Transp. Res. C, Emerg. Technol., vol. 91, pp. 335–352, Jun. 2018. 





[22] J. Rios-Torres and A. A. Malikopoulos, “Impact of partial penetrations of connected and automated vehicles on fuel consumption and traffic flow,” IEEE Trans. Intell. Veh., vol. 3, no. 4, pp. 453–462, Dec. 2018. 





[23] Z. Sun, T. Huang, and P. Zhang, “Cooperative decision-making for mixed traffic: A ramp merging example,” Transp. Res. C, Emerg. Technol., vol. 120, Nov. 2020, Art. no. 102764. 





[24] Z. Zhao, Z. Wang, G. Wu, F. Ye, and M. J. Barth, “The state-of-the-art of coordinated ramp control with mixed traffic conditions,” in Proc. IEEE Intell. Transp. Syst. Conf. (ITSC), Auckland, New Zealand, Oct. 2019, pp. 1741–1748. 





[25] M. Karimi, C. Roncoli, C. Alecsandru, and M. Papageorgiou, “Cooperative merging control via trajectory optimization in mixed vehicular traffic,” Transp. Res. C, Emerg. Technol., vol. 116, Jul. 2020, Art. no. 102663. 





[26] X. Liao et al., “Game theory-based ramp merging for mixed traffic with unity-sumo co-simulation,” IEEE Trans. Syst., Man, Cybern. Syst., vol. 52, no. 9, pp. 5746–5757, Sep. 2022, doi: 10.1109/TSMC.2021.3131431. 





[27] Y. Zhou, M. E. Cholette, A. Bhaskar, and E. Chung, “Optimal vehicle trajectory planning with control constraints and recursive implementation for automated on-ramp merging,” IEEE Trans. Intell. Transp. Syst., vol. 20, no. 9, pp. 3409–3420, Sep. 2019. 





[28] Y. Zhou, E. Chung, A. Bhaskar, and M. E. Cholette, “A state-constrained optimal control based trajectory planning strategy for cooperative freeway mainline facilitating and on-ramp merging maneuvers under congested traffic,” Transp. Res. C, Emerg. Technol., vol. 109, pp. 321–342, Dec. 2019. 





[29] A. D. Ames, X. Xu, J. W. Grizzle, and P. Tabuada, “Control barrier function based quadratic programs for safety critical systems,” IEEE Trans. Autom. Control, vol. 62, no. 8, pp. 3861–3876, Aug. 2017. 





[30] A. D. Ames, S. Coogan, M. Egerstedt, G. Notomista, K. Sreenath, and P. Tabuada, “Control barrier functions: Theory and applications,” in Proc. 18th Eur. Control Conf. (ECC), Jun. 2019, pp. 3420–3431. 





[31] W. Xiao, C. Belta, and C. G. Cassandras, “Decentralized merging control in traffic networks: A control barrier function approach,” in Proc. 10th ACM/IEEE Int. Conf. Cyber-Phys. Syst., Apr. 2019, pp. 270–279. 





[32] W. Xiao, C. G. Cassandras, and C. A. Belta, “Bridging the gap between optimal trajectory planning and safety-critical control with applications to autonomous vehicles,” Automatica, vol. 129, Jul. 2021, Art. no. 109592. 





[33] M. A. S. Kamal, J.-I. Imura, T. Hayakawa, A. Ohata, and K. Aihara, “Smart driving of a vehicle using model predictive control for improving traffic flow,” IEEE Trans. Intell. Transp. Syst., vol. 15, no. 2, pp. 878–888, Apr. 2014. 





[34] Hassan K. Khalil, Nonlinear Systems, 2rd ed. Upper Saddle River, NJ, USA: Prentice-Hall, 2002. 





[35] K. Vogel, “A comparison of headway and time to collision as safety indicators,” Accident Anal. Prevention, vol. 35, no. 3, pp. 427–433, May 2003. 





[36] W. Zhuang et al., “A survey of powertrain configuration studies on hybrid electric vehicles,” Appl. Energy, vol. 262, Mar. 2020, Art. no. 114553. 





[37] H. Dong, W. Zhuang, B. Chen, G. Yin, and Y. Wang, “Enhanced ecoapproach control of connected electric vehicles at signalized intersection with queue discharge prediction,” IEEE Trans. Veh. Technol., vol. 70, no. 6, pp. 5457–5469, Jun. 2021. 





[38] D. S. Naidu, Optimal Control Systems. Boca Raton, FL, USA: CRC Press, 2002. 





[39] A. D. Ames, J. W. Grizzle, and P. Tabuada, “Control barrier function based quadratic programs with application to adaptive cruise control,” in Proc. 53rd IEEE Conf. Decis. Control, Dec. 2014, pp. 6271–6278. 





[40] M. A. S. Kamal, M. Mukai, J. Murata, and T. Kawabe, “Model predictive control of vehicles on urban roads for improved fuel economy,” IEEE Trans. Control Syst. Technol., vol. 21, no. 3, pp. 831–841, Apr. 2013. 





[41] K. Dresner and P. Stone, “A multiagent approach to autonomous intersection management,” J. Artif. Intell. Res., vol. 31, pp. 591–656, Mar. 2008. 





[42] A. Kesting, M. Treiber, and D. Helbing, “Enhanced intelligent driver model to access the impact of driving strategies on traffic capacity,” Phil. Trans. Roy. Soc. A, Math., Phys. Eng. Sci., vol. 368, no. 1928, pp. 4585–4605, Oct. 2010. 



![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/0b582962688a8cf09a0d73e9e51bff7d23712cbfb7d79581a852966f826d61b7.jpg)


Haoji Liu received the M.S. degree in mechanical engineering from Southeast University, Nanjing, China, in 2022. His research interests include connected and automated vehicles, safe optimal control, and intelligent transportation systems. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/04494caef3f44a54cc71373766262f9b9d481220fdb71af8daaa74b387c316f2.jpg)


Weichao Zhuang (Member, IEEE) received the B.Eng. and Ph.D. degrees in mechanical engineering from the Nanjing University of Science and Technology, Nanjing, China, in 2012 and 2017, respectively. From January 2014 to December 2015, he was a Visiting Student at the Department of Mechanical Engineering, University of Michigan, Ann Arbor, MI, USA. He is currently an Associate Professor with the School of Mechanical Engineering, Southeast University, Nanjing. His current research interests include connected and automated vehicles, 

optimal control, clean energy vehicles, and multi-agent control. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/93309dbe7d2290baf25c68e439f0c6b0c8d553a1ee57a0aa929b434b8cb09111.jpg)


Guodong Yin (Senior Member, IEEE) received the Ph.D. degree in mechanical engineering from Southeast University, Nanjing, China, in 2007. From August 2011 to August 2012, he was a Visiting Scholar at the Department of Mechanical and Aerospace Engineering, The Ohio State University, Columbus, OH, USA. He is currently a Professor with the School of Mechanical Engineering, Southeast University. His research interests include connected and automated vehicles, vehicle dynamics and control, and advanced vehicle control. He was a 

recipient of the National Science Fund for Distinguished Young Scholars. He is an Associate Editor of IEEE TRANSACTIONS ON INTELLIGENT VEHICLES. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/fb3ed95be8747884695398b119697580da21571c293260900d792bb3e534230e.jpg)


Zhaojian Li (Senior Member, IEEE) received the B.Eng. degree from the Nanjing University of Aeronautics and Astronautics in 2010 and the M.S. and Ph.D. degrees in aerospace engineering (flight dynamics and control) from the University of Michigan, Ann Arbor, in 2013 and 2015, respectively. He worked as an Algorithm Engineer at General Motors from January 2016 to July 2017. Since August 2017, he has been an Assistant Professor with the Department of Mechanical Engineering, Michigan State University. His research interests 

include learning-based control, nonlinear and complex systems, robotics, and automated vehicles. He was a recipient of the NSF CAREER Award. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-27/56ca9920-79fb-459f-8451-02193f6a94eb/f0d0e7525bcbecd3044741ceac32efacd548d16751976169ba170d233b352ec3.jpg)


Dongpu Cao (Senior Member, IEEE) received the Ph.D. degree from Concordia University, Canada, in 2008. He is a Professor with Tsinghua University. He has contributed more than 200 papers and three books. His current research interests include driver cognition, automated driving, and cognitive autonomous driving. He is an IEEE VTS Distinguished Lecturer. He received the SAE Arch T. Colwell Merit Award in 2012, the IEEE VTS 2020 Best Vehicular Electronics Paper Award, and six Best Paper Awards from international conferences. He has 

served as the Deputy Editor-in-Chief for IET Intelligent Transport Systems journal and an Associate Editor for IEEE TRANSACTIONS ON VEHIC-ULAR TECHNOLOGY, IEEE TRANSACTIONS ON INTELLIGENT TRANS-PORTATION SYSTEMS, IEEE/ASME TRANSACTIONS ON MECHATRONICS, IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS, IEEE/CAA JOUR-NAL OF AUTOMATICA SINICA, IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, and Journal of Dynamic Systems, Measurement and Control (ASME). 