# A traffic control strategy for freeway merging zones cooperating safety and efficiency in the intelligent connected environment of mixed vehicles

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/1959642536ac5cbf28bb505c6e8fb8791be762f6284bbf86c9feb3abc29944e0.jpg)


Lang Zhang , Heng Ding * , Zeyang Cheng , Xiaoyan Zheng , Weihua Zhang 

School of Automotive and Transportation Engineering, Hefei University of Technology, Hefei 230009, China 

# A R T I C L E I N F O

Keywords: 

Freeway 

Merging zone 

Mixed-vehicle traffic flow 

Cooperative control 

Model predictive control (MPC) 

# A B S T R A C T

The manner and intensity of vehicle interactions in a mixed-vehicle traffic flow differ from those in a typical traffic flow. This difference leads to greater potential conflicts and decreased efficiency in freeway merging zones, which involve a large amount of vehicle crossing behaviour. To avoid the deterioration of traffic status, cooperative control of safety and efficiency for mixedvehicle traffic flow using connected and automated vehicles (CAVs) in freeway merging zones is proposed. First, a multi-objective nonlinear mixed-integer program model for cooperative safety and efficiency is presented at the vehicle level to optimize CAV’s behavioural decisions using historical predicted data. Second, a Transformer neural network is adopted to forecast the traffic state under different control weights, accounting for the dynamic characteristics of the traffic system. An adaptive weighting model is constructed to choose the optimal solution from the Pareto frontier derived from the multi-objective problem. To ensure the feasibility of vehiclelevel decisions and to facilitate system-level optimization, CAVs are capable of sharing and coordinating their behaviour decisions through iterations. A typical scenario involving a two-lane freeway merging area is analysed, and the results show that the cooperative control strategy can effectively optimize the traffic state. Even at $2 0 \%$ CAV penetration rates, this strategy reduces total parking delays by $4 8 . 7 \%$ and time-integrated time-to-collision (TIT) by $7 2 . 2 \%$ . 

# 1. Introduction

As the bottleneck of the freeway system, the merging zone combines the mainline and on-ramp traffic flows. In this zone, vehicle merging behaviour tends to induce traffic shocks, increasing the probability and intensity of vehicle conflicts and consequently increasing the risk of collision and reducing freeway capacity ( Chen et al., 2021a; Ding et al., 2021). Especially in mixed-vehicle traffic flow scenarios, the interactions between cars and trucks affect the vehicle lane-changing probability, speed, and safety expectations (Yang et al., 2014; Kong et al., 2021; Ye and Zhang, 2009), not only leading to more ‘stop-and-go’ phenomena and nonessential traffic efficiency waste but also increasing the risk of vehicle collisions. Thus, simultaneously improving the traffic efficiency and safety of mixed-vehicle traffic flows in merging zones is an important issue that warrants attention. 

Traditional control strategies focus on managing traffic flow at the macro level, with ramp metering as one of the most established 

control methods. The methods in (Schmitt et al., 2017; Ma et al., 2021; Yu et al., 2024) were designed to reduce congestion on the mainline by restricting the entry of vehicles from on-ramp. However, as a macroscopic traffic control strategy, ramp metering cannot directly influence random, nonuniform microscopic driving behaviour, and eliminating the space–time gaps created during traffic merging is difficult (Chen et al., 2021c). Microscopic studies have shown (Laval et al., 2006; Chen et al., 2018) that lower merging velocities and bounded accelerations of human vehicles (HVs) result in a redundant gap that persists downstream during the merging process. 

As a new generation of microscopic technology, connected and automated vehicles (CAVs) can help directly control the acceler ation, deceleration and lane-changing manoeuvres of vehicles. By planning trajectories for CAVs, the space–time utilization of roads can be enhanced to improve freeway capacity ( Hu et al., 2024; Li et al., 2023; Wang et al., 2023a). Unlike traditional ramp metering, strategies involving vehicle trajectories aim to establish a safe gap for on-ramp vehicles to merge into the mainline in advance (Bushnell, 1970; Zhou et al., 2019). Current prevalent methods of trajectory planning can be categorized into distributed and centralized control strategies, where centralized control requires a greater degree of vehicle information sharing and cooperation than distributed control does. 

Distributed control typically focuses on preventing any unsmooth merging behaviour between a single merging vehicle and its surrounding vehicles. Liu et al. (2023) proposed a hierarchical control framework to optimize the sink position of CAVs, and address HV-induced interference in the case of three-vehicle coordination. Zhou et al. (2023) proposed a safety-enhanced eco-driving strategy based on a hierarchical and distributed framework that incorporates a driving risk field, shockwave theory, and a motion planning and control method. Karimi et al. (2020) developed a CAV control algorithm for various triplets, where CAVs collaborate with one another and establish the most favourable trajectory. Zhou et al. (2017) improved the conventional car-following model to enable CAVs to collaborate in ramp vehicle merging. The aim of these studies was to enhance the merging behaviour of a limited number of vehicles; although they guaranteed the process’s safety, they improved the system efficiency only slightly because of the distributed control limitations. 

Centralized control has garnered increased attention from academics, as it has greater potential at the system level. Tang et al. (2022) introduced a novel cooperative merge control model for hierarchical systems that considers flexible merge locations to ensure a safe and efficient merging process. Uno et al. (1999) innovatively mapped on-ramp vehicles to virtual lanes to create acceptable merge space. Chen et al. (2021b) developed an event-triggered rolling horizon-based systematic trajectory planning system that incorporates a real-time correction mechanism, enabling inter-vehicle merging behaviour to resist certain disturbances. Jing et al. (2019) built on previous research by using game theory to determine the optimal merging sequence. Merging two traffic flows by optimizing CAV trajectories can result in a substantial nonlinear optimization problem (Mu et al., 2021; Rios-Torres and Malikopoulos, 2017), as traffic safety constraints and objective functions tend to cause nonlinearity and nonconvexity. Centralized control exacerbates this problem, making it difficult to promptly reach an analytical solution. Despite the higher performance of such methods, this control is less realtime and less feasible. 

Considering the shortcomings of these two types mentioned above, a few scholars have developed a series of control algorithms to balance system performance and computational speed. For example, Tajalli et al. (2022) proposed a distributed control algorithm based on lane descent roadway scenarios, which can achieve centralized control. Chen et al. (2022) proposed a globally oriented approach for grouping vehicles and modelled discrete traffic flows via time windows. Li et al. (2018) designed lateral and longitudinal controllers for single and multiple vehicular strings, respectively, and ensured stability and consensus using the Routh-Hurwitz stability criterion and the Lyapunov technique. These methods combine the advantages of distributed and centralized control to improve real-time performance of control while avoiding local optimization; however, they still have some limitations in practical applications. 

First, the above studies are applicable only to fully CAV environments where information is fully known and vehicles are fully controllable. In the development of CAVs, there is a traffic flow with a mixture of CAVs and HVs and a simultaneous traffic flow with a mixture of trucks and cars (Zhang et al., 2022). The existing studies do not fully consider mixed-vehicle factors. Second, most existing trajectory control methods primarily aim to maximize throughput (Li et al., 2017; Xu et al., 2020), ensuring traffic safety only by setting collision avoidance constraints. These approaches are based on an ideal collision-free environment and ignore the importance of traffic safety in control, especially in mixed-vehicle scenarios with high collision risks. Although these strategies significantly improve the safety indices, they are not sufficiently interpretable in terms of traffic safety and do not consider practical application conditions. Third, in multi-objective planning problems, transforming a multi-objective planning problem into a single-objective planning problem based on the importance of different objectives is common (Zhang and Zuo, 2013; Windeatt and Ghaderi, 1998). However, the priorities of the objectives change under different traffic states, which is not considered in existing studies. Since the optimization methods for different tasks are different or even mutually exclusive, the control weights must be updated in real time to adapt to the dynamic characteristics of the traffic system. However, analysing the impact of an individual vehicle’s trajectory on the system state is difficult. Balancing system dynamic optimization with algorithm computational performance is a challenging problem. 

To solve the traffic efficiency and safety equilibrium problem of mixed-vehicle traffic flow in the merging zone, a CAV cooperative control strategy is proposed. First, a vehicle-level behavioural decision model is proposed to provide behavioural decisions for different types of CAVs. Second, a multi-objective planning program for traffic efficiency and safety is considered in the CAV behavioural decision model (BDM). By implementing this procedure, a Pareto frontier consisting of the optimal behavioural decisions of the CAV is obtained. Then, a Transformer network is used to fit the nonlinear relationship between individual controls and the system state. On this basis, an adaptive weighting model is developed, which can select the control weights with the highest overall performance at the Pareto front based on real-time traffic information. Finally, a negotiation relationship between vehicles is established, and system optimization with distributed control is achieved through iterative optimization. 

The main contributions of this paper are in four aspects: 

(1) A distributed CAV behavioural decision model is proposed for mixed-vehicle traffic flow. 

(2) Transformer is used to establish the relationship between individual CAV behaviours and the system state. 

(3) A dynamic balance approach is provided between traffic efficiency and safety in the merging zone through distributed control. 

(4) Several experiments are conducted to verify the feasibility and effectiveness of the strategy. 

The remainder of the paper is organized as follows. In Section 2, the control scenarios involved in this paper are described; in Section 3, a vehicle-level behaviour decision model is proposed; in Section 4, a Transformer-based weighting model for adaptive efficiency and safety is detailed; in Section 5, the framework and details of the cooperative control strategy are supplemented; in Section 6, a case analysis is provided; and in Section 7, the conclusions of this paper and future research are summarized. 

# 2. Control scenario and framework

# 2.1. Scenario and assumptions

As shown in Fig. 1, the control scenario consists of a two-lane mainline and a single-lane on-ramp. Considering the infrastructure deployment and vehicle communication range, the control area is defined within a circle with radius $R$ and centre point P. The length of the acceleration zone on ramp 3 within the cooperative control area is $L _ { s a . }$ , where $L _ { s a } \leq R$ . The length of the induction zone on mainline 1 and mainline 2 is $L _ { s a }$ , and the length of the merging zone is $L _ { m a }$ . Thus, the length of the entire control area is ${ { L } _ { c a } } = { { L } _ { s a } } + { { L } _ { m a } }$ . 

In this work, the mixed traffic flow consists of four types of vehicles: the CAV truck, the CAV car, the HV truck and the HV car. For the available location information and controllability, CAV trucks and CAV cars are the main system control objects. Before modelling in detail, the related assumptions are as follows: 

(1) CAV-to-CAV, CAV-to-HV and CAV-to-infrastructure communication is possible. Owing to advances in communication technology, the effects of communication delay are not considered in this paper (Sun et al., 2018). 

(2) CAVs are equipped with on-board computers capable of solving complex problems independently. 

(3) The physical performances of CAV cars and CAV trucks differ, but their driving behaviours do not. 

# 2.2. Control framework

The cooperative control strategy proposed in this paper is based on MPC. The control framework is illustrated in Fig. 2. The control strategy consists of two main components: the CAV behaviour decision model (BDM) and the adaptive weighting model (AWM). The predictive trajectory of HV and the historical behavioural programme of CAV are predictive models of MPC. The BDM provides a vehicle-level multi-objective nonlinear planning problem for computing traffic efficiency and safety metrics under different scenarios based on a predictive model. The obtained Pareto frontier includes a collection of CAV behaviour decisions. 

To find the scheme with the best overall performance on the Pareto frontier, the AWM is proposed in this paper. The basic idea of the AWM is to use the Transformer to predict the system state under different control weights. Then, the location on the Pareto frontier with the best system state is found. Note that the control weights discussed in AWM refer to the ordering of the optimal solution for the current traffic state in the Pareto frontier rather than the weights of the different objectives in the objective function. This is because the nature of the linear weighting method is to slice the objective space by a linear hyperplane, and the resulting solution cannot cover the entire non-convex region (Marler and Arora., 2004). Since the BDM is a nonlinear mixed integer programming model, the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/562f320904e598bf7ac4a2d7b638c7af24ceb9db1a42711e94503768d44adae5.jpg)



Fig. 1. Schematic diagram of the merging zone cooperative control scenario.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/260f509a4aec2d3fb9bd26c682e655bbbc200223fc196a69aacf57f4e5cd2615.jpg)



Fig. 2. Control framework.


generated Pareto frontier may contain non-convex regions, so we choose to select the optimal solution directly in the Pareto frontier. 

The consensus among vehicles is guided through several iterations of the system, and a more feasible solution is eventually ob tained. As the optimal weights of the controller are related only to real-time traffic information, the AWM is not involved in the iterative process of the system. The control schemes obtained are applied to the corresponding CAVs, and the optimization process is repeated online at each control moment. 

# 3. CAV behavioural decision model

Due to the continuity of the car-following behaviour, we update the speed variable more frequently. Vehicles update their trajectories every $\Delta t ( \Delta t = 0 . 1 )$ ) seconds and decide to change lanes every $\Delta t ^ { * }$ $\Delta t ^ { * } = 1 \dot { }$ ) seconds. We define T as the set of time steps and I as the set of all vehicles in the scene. The state variables $x _ { i } ^ { t }$ and $y _ { i } ^ { t }$ denote the longitudinal distance and lane position of vehicle $i \in I$ at time $t \in T _ { : }$ , respectively. Similarly, the variables $\nu _ { i } ^ { t }$ and $a _ { i } ^ { t }$ denote the speed and acceleration of vehicle $i \in I$ at time $t \in T _ { i }$ , respectively. A vehicle’s lane-changing manoeuvre depends on two binary decision variables, $\alpha _ { i } ^ { t }$ and $\beta _ { i } ^ { t }$ . If $\alpha _ { i } ^ { t }$ or $\beta _ { i } ^ { t }$ is 1, the CAV changes lanes to the left or right, respectively. Otherwise, if both are 0, the CAV stays in the current lane. Therefore, the state of each vehicle $i \in I$ at moment $t \in T$ can be defined as $s _ { i } ^ { t } = \{ x _ { i } ^ { t } , y _ { i } ^ { t } , \nu _ { i } ^ { t } , a _ { i } ^ { t } , \alpha _ { i } ^ { t } , \beta _ { i } ^ { t } \}$ . 

The BDM finds optimal behavioural decisions for CAVs by solving a multi-objective nonlinear planning problem. Since the predicted trajectory of the HV is an important component of the BDM input, we first predict the trajectory of the HV in the control area. 

# 3.1. Trajectory prediction of the HV

Four types of HV car-following behaviours are exhibited in mixed-driving environments: car-following cars (C–C), car-following trucks (C-T), truck-following cars (T-C), and truck-following trucks (T-T). Therefore, a modified IDM model (Liu et al., 2016) was used to predict the longitudinal driving behaviour of the HV as shown in Eq. (1): 

$$
\frac {d ^ {2} x _ {i} (t)}{d t ^ {2}} = a _ {i} \left[ 1 - \frac {v _ {i} (t)}{V _ {i}} \right] ^ {4} - \left(\frac {S _ {i} \left(v _ {i} (t) , \Delta v _ {i} (t)\right)}{\Delta x _ {i} (t) - l _ {i f}}\right) ^ {2} ] \tag {1}
$$

$$
S _ {i} \left(\nu_ {i} (t), \Delta \nu_ {i} (t)\right) = s _ {0} ^ {H V} + \varepsilon^ {H V} \nu_ {i} (t) - \frac {\nu_ {i} (t) \Delta \nu_ {i} (t)}{2 \sqrt {a _ {\max} ^ {H V} a _ {\min} ^ {H V}}}
$$

where $\Delta { \nu } _ { i } ( t )$ is the velocity difference between vehicle i and the lead vehicle at time $t ; l _ { i , f }$ is the length of the vehicle in front of i; $s _ { 0 } ^ { H V }$ is the desired headway; $\varepsilon ^ { H V }$ is the minimum headway; and $a _ { \mathrm { m a x } } ^ { H V }$ , $a _ { \operatorname* { m i n } } ^ { H V }$ are the maximum and minimum accelerations, respectively. There are four different values for $s _ { 0 } ^ { H V }$ , $\varepsilon ^ { H V }$ , $a _ { \mathrm { m a x } } ^ { H V }$ and $a _ { \operatorname* { m i n } } ^ { H V }$ depending on the combination of car-following. 

In terms of lateral motion, lane-changing behaviour is a binary problem, if treating it as an uncertain problem in the decisionmaking phase will lead to no feasible solution, it is necessary to simplify the lateral motion computational process. To reduce the computational complexity, this paper only predicts the mandatory lane-changing behaviour of ramp HVs and ignores the free lanechanging behaviour of mainline HVs in the decision-making phase. 

The probability of mandatory lane-changing behaviour is determined by Eq. (2): 

$$
p _ {d} = \alpha_ {1} / \left(1 + e ^ {\left(\left(x _ {b} - \alpha_ {2} \cdot x _ {l}\right) / \alpha_ {3}\right)}\right) \tag {2}
$$

where $p _ { d }$ is the lane change probability; $x _ { b }$ is the location where the lane change must be made; when $x _ { i } = x _ { b }$ , the lane change probability is 1; and $\alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 }$ are the lane change adjustment parameters. 

Parameter $\alpha _ { 1 }$ is computed as shown in Eq. (3): 

$$
\alpha_ {1} = 1 + \mathrm {e} ^ {(1 - \alpha_ {2}) \cdot x _ {\mathrm {b}} / \alpha_ {3}} \tag {3}
$$

The mandatory lane-changing behaviour must also fulfil the safety requirements outlined by Eqs. (4) and (5). 

$$
x _ {d - 1} - x _ {i} \geq \max  \left\{\nu_ {i} \varepsilon_ {i} ^ {H V}, s _ {0, i} ^ {H V} \right\} + l _ {i} \tag {4}
$$

$$
x _ {i} - x _ {d} \geq \max  \left\{\nu_ {d} \varepsilon_ {i} ^ {H V}, s _ {0, i} ^ {H V} \right\} + l _ {i} \tag {5}
$$

where $d$ and $d - 1$ are the rear and front vehicles in the target lane, respectively. 

When $p _ { d } > 0 . 5$ and the safety requirements Eqs. (4) and (5) are satisfied, the HV is assumed to change lanes, otherwise it is assumed not to change lanes. 

# 3.2. Objective function and constraints

The primary aim of the CAV cooperative control strategy is to enhance traffic efficiency and safety. Different objectives guided the design of the objective functions for this study. These functions are presented in Eqs. (6) and (7). 

$$
f _ {i} ^ {1} = \max  \left(\sum_ {t \in T} \left(x _ {i} ^ {t} - \gamma \left(\alpha_ {i} ^ {t} + \beta_ {i} ^ {t}\right) - \delta \mid a _ {i} ^ {t} \right]\right) \tag {6}
$$

$$
f _ {i} ^ {2} = \min  \left(\sum_ {t \in T} \left\{ \begin{array}{l l} \frac {\nu_ {i} ^ {t} - \nu_ {i - 1} ^ {t}}{x _ {i - 1} ^ {t} - l _ {i - 1} ^ {t} - x _ {i} ^ {t}} & \text {i f} v _ {i} ^ {t} > v _ {i - 1} ^ {t} \\ 0 & \text {e l s e} \end{array} \right.\right) \tag {7}
$$

where $\gamma$ and $\delta$ are the weighting coefficients. 

Eqs. (6) and (7) aim to enhance the trajectory-seeking capability of a controlled CAV by maximizing travel distance and minimizing collision risk. The first term in Eq. (6) aims to improve road capacity by maximizing the longitudinal travel distance of CAVs in the prediction time domain. Since the aim of this paper is to optimize the overall state of the merging zone, a penalty function is also added to Eq. (6) to prevent destructive speed changes and lane-changing behaviours in CAVs. The reciprocal time to collision (RTTC) is commonly employed to assess traffic safety (Balas and Balas, 2006) and displays a direct and consistent relationship with the prob ability of collision: an increase in the RTTC corresponds to a greater risk of collision. Therefore, considering traffic safety, Eq. (7) is set to minimize the sum of the RTTC in the prediction time domain. 

# (2) Constraint conditions

As the control relies on discrete time steps, in this paper, the state of the controlled vehicle is updated based on quadratic polynomial Eqs. (8)–(10) of motion. 

$$
x _ {i} ^ {t} = x _ {i} ^ {t - 1} + v _ {i} ^ {t} \Delta t + \frac {1}{2} a _ {i} ^ {t - 1} \Delta t ^ {2} \tag {8}
$$

$$
y _ {i} ^ {t} = y _ {i} ^ {t - 1} - \alpha_ {i} ^ {t - 1} + \beta_ {i} ^ {t - 1} \tag {9}
$$

$$
v _ {i} ^ {t} = v _ {i} ^ {t - 1} + a _ {i} ^ {t - 1} \Delta t \tag {10}
$$

In the control process, the acceleration and lane-changing manoeuvres of the CAV are the decision variables. Considering the practical conditions of the merging area and from a safety perspective, the following constraints are satisfied as much as possible. 

Eqs. (11) and (12) limit the speed and acceleration of the vehicle within a reasonable interval. 

$$
0 \leq v _ {i} ^ {t} \leq v _ {\max , i} \tag {11}
$$

$$
a _ {\min , i} \leq a _ {i} ^ {t} \leq a _ {\max , i} \tag {12}
$$

The lane-changing behaviour of a vehicle typically lasts 3–5 s (Thiemann et al., 2008). To be realistic, the lane changing frequency of CAVs is limited and the lane changing time constraint is shown in Eq. (13). This move also avoids the frequent lane-changing behaviour of CAVs and helps the system converge. 

$$
\sum_ {t ^ {*} = t - 4} ^ {t} \alpha_ {i} ^ {t ^ {*}} + \beta_ {i} ^ {t ^ {*}} \leq 1 \tag {13}
$$

To guarantee the safety and practicability of BDMs, CAVs must dynamically avoid collisions with predicted vehicle trajectories. The fundamental concept of vehicle safety constraints is to maintain a secure distance between every two vehicles in the same lane, with the surrounding vehicles’ state variables serving as inputs to the vehicle optimization problem. Notably, in both practical applications and simulation experiments, the CAV needs only to ensure that there is no risk of collision with vehicles within its communication range. This operation can significantly reduce computational stress. By setting Eqs. (14) and (15), a cooperative relationship is established between the vehicles. 

$$
x _ {j} ^ {t} - x _ {i} ^ {t} \geq l _ {j} ^ {t} + s _ {i} ^ {0} + v _ {i} ^ {t} \varepsilon_ {i} \tag {14}
$$

$$
x _ {i} ^ {t} - x _ {k} ^ {t} \geq l _ {k} ^ {t} + s _ {k} ^ {0} + v _ {k} ^ {t} \varepsilon_ {k} \tag {15}
$$

In addition to the risk of dynamic collisions with other vehicles during the travelling process, vehicles must also avoid stationary obstacles on the ground. Thus, the lane-changing process for vehicles on a ramp must be completed before the vehicles reach the end of the ramp. The maximum distance travelled by the ramp vehicle is limited by Eq. (16), and the ramp vehicle is motivated to change lanes. By predicting the trajectory, the ramp CAV is able to sense this physical bottleneck in advance. To maximize the travel distance, ramp vehicles need to actively change lanes earlier. 

$$
y _ {i} ^ {t} \leq y _ {\text {r a m p}} - 1 + M p _ {i} ^ {t}
$$

$$
P _ {i} ^ {t} = \left\{ \begin{array}{l l} 1 & \text {i f} x _ {i} ^ {t} \leq L _ {s a} + L _ {m a} \\ 0 & \text {e l s e} \end{array} \right. \tag {16}
$$

where $p _ { i } ^ { t }$ is an auxiliary variable and $y _ { r a m p }$ is the defined ramp lane value. 

Limitations are imposed on the change in lanes between mainline and ramp vehicles, with lane constraints established according to Eq. (17). 

$$
y _ {\min , i} ^ {t} <   y _ {i} ^ {t} <   y _ {\max , i} ^ {t}, \text {a n d} y _ {\min , i} ^ {t} = \left\{ \begin{array}{l l} 1 & y _ {i} ^ {t - 1} \leq 1 \\ 2 & y _ {i} ^ {t - 1} > 1 \end{array} , \quad y _ {\max , i} = \left\{ \begin{array}{l l} 2 & y _ {i} ^ {t - 1} \leq 1 \\ 3 & y _ {i} ^ {t - 1} > 1 \end{array} \right. \right. \tag {17}
$$

where $y _ { \mathrm { m a x } , i } ^ { t }$ and $y _ { \mathrm { m i n } , i } ^ { t }$ are the leftmost and rightmost lanes, respectively, that vehicle i can reach at time t. 

This paper focuses on the traffic system level, and does not model the vehicle lane-changing process in the main text. This is because considering the vehicle lane-changing process in a mixed-vehicle travelling environment would significantly increase the computational burden. Note that the vehicle lane changing process can actually be extended to BDM, and the effect results (see Appendix A for details) of lane-changing trajectories on the effectiveness of the control strategy is insignificant. 

# 3.3. Model solving algorithm

The NSGA-II algorithm (Deb et al., 2002) is widely used for solving multi-objective problems because of its excellent convergence performance, diversity maintenance capability, and fast operating speed. The main reason for choosing the NSGA-II algorithm to solve the BDM in this study is that this algorithm filters the solution directly through a nondominated relation that is not limited by the shape of the frontier and thus can cover the complete Pareto frontier. In addition, the NSGA-II algorithm incorporates a congestion ranking process. When both the population size and the number of iterations are high, the resulting set of solutions can be considered uniformly distributed on the Pareto frontier (Verma et al., 2021). This provides a solid foundation for the application of subsequent AWM methods. 

The process of solving the BDM via the NSGA-II algorithm includes the following six steps: 

Step 1: Initialise the population with the number of individuals $M _ { 0 }$ . In this paper, the population refers to the set of control schemes, and the individuals are independent control schemes. The population is a control scheme, and the individuals are represented by a matrix of control variables $N _ { c } \times N _ { x }$ , where $N _ { c }$ is the control time domain, and $N _ { x }$ is the number of decision variables. On this basis, the $f ^ { 1 } , f ^ { 2 }$ of each individual were calculated according to Eqs. (6)–(17). 

Step 2: Nondominated sorting of populations and calculation of individual crowding distances. 

Step 3: In each iteration, new populations are generated by selection, crossover, and mutation. 

Step 4: Combine parent and child populations for fast nondominated sorting and calculating crowding distances. 

Step 5: Select individuals to form new populations based on non-dominance relationships and crowding distances. 

Step 6: The iteration ends when the individuals in the population have no dominance relationship with each other (i.e., the al gorithm converges). The current population is the desired Pareto frontier. If the algorithm does not converge, return to Step 2 to continue the iterative process. 

# 4. Transformer-based adaptive efficiency and safety weighting model

Although solutions on the Pareto frontier do not dominate each other, there is still a scheme that offers the best overall performance in each traffic state. Through the use of the AWM, the control strategy can adjust the priority of the control objectives based on the state of the system, changes in the operating environment, and objective requirements. 

Since the solution on the Pareto frontier is not unique, and it is not possible to speculate on the state of the system based on different combinations of control schemes, it is necessary to determine the optimal weights before the control is implemented. However, the cooperative control strategy presented here utilizes a distributed control approach, which poses challenges in fitting the nonlinear relationship between the individual control weights and the system state. Neural networks are effective for overcoming this challenge because they can extract high-level, abstract features with only input–output data. In the field of traffic state prediction, neural networks are widely employed (Bai et al., 2023; Li and Abdel-Aty, 2022; Mohanty et al., 2020). In practical applications of cooperative 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/4f6d08948aacc182c8627adf83458dc5ac5b6b8339ca3fd5776049e2261c0f80.jpg)



Fig. 3. Structure of the AWM.


control techniques, the alteration in the traffic system state is linked to the control weights of all the controlled vehicles, which are often overlooked by conventional neural networks. The self-attention mechanism allows the model to attend to information provided by a range of vehicles. Therefore, in this study we employ the Transformer to project the traffic state. Additionally, the Transformer uses a multihead attention mechanism to enhance computational efficiency through parallel computation; its benefits have been established in numerous engineering applications (Zhang and Li, 2022). 

Since the Transformer is a predictive model and not a decision model, the optimal weights cannot be obtained directly. Note that the main role of the Transformer in this paper is to predict the road traffic state under different weights, thus to change the style of the control strategy, rather than directly instructing the behaviour of the CAV. Based on the prediction results, the optimal weights can be selected in the Pareto frontier. Since the AWM model focuses on the freeway system rather than individual vehicles, the average vehicle speed $\bar { \nu }$ and the standard deviation sd of the speed were chosen to evaluate the traffic efficiency and safety under different weights. To facilitate the calculations, the auxiliary variable $V _ { \mathrm { m a x } }$ was set to evaluate the speed indicator. As illustrated in Fig. 3, by utilizing the predicted outcomes (shaded area), the weight that leads to the current optimal integrated control performance of the vehicle can be obtained. The corresponding weight values are employed to locate the optimal point on the Pareto frontier identified by the BDM model. 

The input data comprise 10 features: the position $x _ { i } ^ { t }$ and lane $y _ { i } ^ { t }$ of vehicle $i$ at time t; the speed $\nu _ { i } ^ { t }$ and acceleration $a _ { i } ^ { t }$ of vehicle i at time t; the control weight λ of vehicle i at time t; CAV penetration $\mathbf { } p _ { i , t } ^ { c a \nu }$ and truck penetration $p _ { i , t } ^ { t r u c k }$ on the road sections within the communication range of vehicle i at time t; and the density $\rho _ { i , t } ,$ mean vehicle speed $\overline { { \nu } } _ { i , t }$ and standard deviation $s d _ { i , t }$ on the road sections within the communication range of vehicle i at time t. The output data comprise 3 features: the density $\rho _ { i , t + \Delta t } ,$ , mean vehicle speed $\overline { { \nu } } _ { i , t + \Delta t }$ and standard deviation $s d _ { i , t + \Delta t }$ on the road sections within the communication range of vehicle i at time $t + \Delta t .$ . 

The training and validation datasets are derived from the simulation experiments, where the training data are derived from the NGSIM dataset I-80 sections 4:00–4:15 and 5:00–5:15, and the validation data are derived from the I-80 sections 5:15–5:30. The initial speeds, entry times, and types of vehicles are consistent with real-world scenarios. A total of 86,060 training sets and 15,186 validation sets are extracted for the six different experimental setups. To ensure data diversity, a random function is used in the simulation to generate the control weight values. 

# 4.1. Adaptive weighting model

The NSGA-II algorithm is used to solve the multi-objective mixed-integer programming problem, and the feasible solutions obtained are uniformly distributed in the Pareto frontier. Depending on the size of the population $M _ { 0 }$ , the same number of nondominated solutions can be obtained. If the set of nondominated solutions is ordered according to the value of one of the objective functions, then the ordinal number of each solution in the set can be equated to the weights of the different objectives. Therefore, the value of the control weight $\begin{array} { r } { \lambda = \frac { \lambda _ { 0 } } { M _ { 0 } } \left( \lambda _ { 0 } = 1 , 2 , . . . , M _ { 0 } \right) } \end{array}$ is actually discrete and directly related to the value of $M _ { 0 }$ . Sort the set of nondominated solutions according to the value of $f ^ { 1 }$ , the final choice of control scheme in the solution set is ranked $\lambda M _ { 0 }$ . 

By inputting various values of λ into the pretrained Transformer, the current state of the road section under different control weights can be predicted. As shown in Eq. (18), λ, which minimizes the weighted product of sd and $V _ { \mathrm { m a x } } - \overline { { \nu } } ,$ , is chosen as the best control weight. The aim of this operation is to make the control strategy optimize the maximum ratio of traffic efficiency and safety. In addition, to ensure the adaptive capability of the control strategy in different states, this paper introduces Eq. (19) as a dynamic weighting function, which is able to dynamically influence the preference of the distributed control strategy according to the vehicle’s crash risk. Note that it is necessary to normalize the data involved before using Eqs. (18) and (19). 

$$
s d _ {\lambda} ^ {(1 - \omega (t t c))} \left(V _ {\max } - \bar {\nu} _ {\lambda}\right) ^ {\omega (t t c)} = \min  \left(s d ^ {(1 - \omega (t t c))} \left(V _ {\max } - \bar {\nu}\right) ^ {\omega (t t c)}\right) \tag {18}
$$

$$
\omega (t t c) = \frac {1}{1 + \frac {1}{e ^ {k (t t c - T t c _ {\text {t h r e s h o l d}})}}} \tag {19}
$$

where $V _ { \mathrm { m a x } }$ is an auxiliary variable; $k$ is a slope factor; $T T C _ { t h r e s h o l d }$ is the time-to-collision (TTC) threshold. $T T C _ { t h r e s h o l d }$ is set for cars to 3 s and for trucks to $5 s$ . 

# 4.2. Transformer neural network

As shown in Fig. 4, the Transformer employs an encoder-decoder structure and utilizes multihead self-attention in place of the standard loop layer in the encoder-decoder architecture. As a result, this is the first seq2seq model to rely on an attention mechanism. In this subsection, we discuss the fundamental components of the Transformer, specifically the self-attention and multihead attention mechanisms. 

The self-attention mechanism entails mapping the query, key, and value matrices to the output. Assuming the input is state, e represents the input vector sequence after positional encoding has been added. Obtaining the query matrix $Q = f _ { Q } ( e )$ , key matrix $K =$ $f _ { K } ( e )$ , and value matrix $V = f _ { V } ( e )$ involves applying a linear transformation to e. The correlation score among distinct vectors can be computed by executing a dot product on the vectors within the input sequence. The dot product attention is shown in Eq. (20): 

$$
\operatorname {A t t e n t i o n} (Q, K, V) = \operatorname {s o f t m a x} \left(\frac {Q K ^ {T}}{\sqrt {d _ {k}}}\right) V \tag {20}
$$

where $d _ { k }$ is the dimension of the embedding vector. 

Normalization is employed to decouple the sharpness of $Q K ^ { T }$ ’s distribution from its variance. Thus, the gradient of the Transformer remains stable throughout the training process. The SoftMax function transforms these values into a probability distribution ranging from 0 to 1, where the total sum equals 1. Dot product attention accurately learns temporal dependencies over long time spans by simultaneously computing attention between all embedding vectors. Furthermore, the self-attention mechanism can effectively capture temporal dependencies by calculating the query, key and value matrices. 

Multihead attention is a significant component of Transformers that helps combine multiple hypotheses when computing attention. To implement multihead attention, $h$ distinct linear transformations of the query, key, and value matrices are executed to obtain the corresponding matrices. Then, the query, key, and value matrices execute simultaneous attention tasks, and using the concatenation function, combine the information obtained from the $h$ heads to obtain the output. The formulas are displayed in Eqs. (21) and (22). 

$$
\operatorname {h e a d} _ {j} = \operatorname {A t t e n t i o n} \left(Q W _ {j} ^ {Q}, K W _ {j} ^ {K}, V W _ {j} ^ {V}\right) \tag {21}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/472cf8699df00980b3b08d8d4d2aab9baf72b50c44e6ad5872d2fcd4584287d2.jpg)



Fig. 4. Transformer neural network structure.


$$
\operatorname {M u l t i h e a d} (Q, K, V) = f _ {c} \left(\left[ \text {h e a d} _ {j} \right] _ {j = 1} ^ {h}\right) \tag {22}
$$

where $f _ { c }$ is the fully connected layer and $W _ { j } ^ { Q } , W _ { j } ^ { K } , W _ { j } ^ { V }$ are the linear transformation matrices. 

The data are input into the model and encoded through embedding and position coding layers, thereby obtaining feature vectors. These vectors are then fed into the encoder module in the N-layer. Similar to the encoder, the initial decoder layer in the decoder module receives inputs from the decoder’s embedding layer and the position coding layer. The remaining decoder layers receive their inputs from the previous decoder layers. However, in contrast to the encoder, the decoder layer incorporates a masked multihead attention layer, which rectifies the future bias problem through the use of a target mask. 

# 4.3. Model accuracy validation

Fig. 5 shows the convergence process of the loss function during the training of the Transformer. Since the AWM only focuses on the vehicle state in the local space, the model almost converges at approximately 30 iterations. 

In this study, we validated the performance of the Transformer by utilizing the following evaluation indicators: mean absolute error (MAE), mean square error (MSE), and root mean square error (RMSE) (Ding et al., 2022; Chen et al., 2023). To conduct our analysis, we used both the RNN and LSTM models as baselines and computed the evaluation indicators according to Eqs. (23)–(25). 

$$
M A E = \frac {1}{N} \sum_ {j = 1} ^ {N} \left| y _ {j} ^ {\text {r e a l}} - y _ {j} ^ {\text {p r e}} \right| \tag {23}
$$

$$
M S E = \frac {1}{N} \sum_ {j = 1} ^ {N} \left(y _ {j} ^ {\text {r e a l}} - y _ {j} ^ {\text {p r e}}\right) ^ {2} \tag {24}
$$

$$
R M S E = \sqrt {\frac {1}{N} \sum_ {j = 1} ^ {N} \left(y _ {j} ^ {\text {r e a l}} - y _ {j} ^ {\text {p r e}}\right) ^ {2}} \tag {25}
$$

where yj is the feature vector of the output data, including $\rho$ ,v,sd. The indicator values of the prediction accuracy are shown in Table 1. 

Table 1 shows that the time series model outperforms the other models, indicating that vehicle-to-vehicle interaction directly affects the system state. The Transformer achieves the highest accuracy among the models, which is attributed to its superior ability to capture long-range dependencies. 

# 5. Control process

The BDM shown in Eqs. (6)–(17) determines the micro driving behaviour of individual CAVs in a distributed manner, relying on the predicted trajectories of unconnected vehicles within the system. However, self-interested CAV-level optimization solutions negatively impact the level of the freeway system, and conflicts may arise between the control strategies of various CAVs, particularly in con gested traffic conditions. Thus, we cooperate among CAVs to obtain optimal system performance. This is achieved through the exchange of state information, which captures the current and predicted trajectories of vehicles within a specific range in the constraints of Eqs. (14) and (15). In addition, an iterative approach is utilized to drive the solution to an optimum (Mirheli et al., 2019; Typaldos 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/455b2afd58a11771114a0cea029232da664af826edeaecf2243cec5aa6eaefcc.jpg)



Fig. 5. Convergence process of the Transformer model.



Table 1 Model accuracy indicators.


<table><tr><td></td><td>MAE</td><td>MSE</td><td>RMSE</td></tr><tr><td>RNN</td><td>1.04</td><td>2.17</td><td>1.47</td></tr><tr><td>LSTM</td><td>1.02</td><td>2.01</td><td>1.42</td></tr><tr><td>Transformer</td><td>1.02</td><td>1.99</td><td>1.41</td></tr></table>

et al., 2023), inducing CAVs to reach a consensus. The iterative process is performed on a vehicle-by-vehicle basis, where the CAV adjusts its own behavioural decisions based on the predicted trajectories of the HVs and the current control schemes of other CAVs. A model for optimizing the system at a higher level is simultaneously introduced. In each iteration, the control centre receives all CAV decisions and evaluates the system performance according to Eqs. (26) and (27). Eqs. (26) and (27) aim to enhance the overall operational status of traffic flow (including total distance travelled and collision risk) by constructing a cooperative relationship between CAVs. The first term of $F _ { 1 }$ is the sum of the CAV lateral movement distances in the control time domain. To ensure consistency with the vehicle-level control objective $f ^ { 1 }$ , a penalty term is also set in $F _ { 1 } , F _ { 2 }$ is the sum of the collision risk indicators of all the vehicles in the control time domain. 

$$
F _ {1} = \max  (\sum_ {i \in I} \sum_ {t \in T} ((\boldsymbol {x} _ {i} ^ {t} - \gamma (\alpha_ {i} ^ {t} + \beta_ {i} ^ {t}) - \delta | a _ {i} ^ {t} |))) \tag {26}
$$

$$
F _ {2} = \min  \left(\sum_ {i \in I} \sum_ {t \in T} \left\{ \begin{array}{l l} \frac {\nu_ {i} ^ {t} - \nu_ {i - 1} ^ {t}}{x _ {i - 1} ^ {t} - l _ {i - 1} ^ {t} - x _ {i} ^ {t}} & \text {i f} \nu_ {i} ^ {t} > \nu_ {i - 1} ^ {t} \\ 0 & \text {e l s e} \end{array} \right.\right) \tag {27}
$$

In each iteration, the state $\boldsymbol { s } _ { i } ^ { t }$ of vehicle $i \in I$ in the control region at time $t \in T$ is updated. The control centre analyses the feasibility and convergence of the control scheme according to Eqs. (26) and (27) until the system converges or the maximum number of iterations is reached. The proposed distributed algorithm is based on MPC, where the model is iteratively updated online by rolling finite time domain optimization. The model has a time step Δt, a simulation time step number $k$ , a prediction time domain $N _ { p }$ , and a controller time step number $k _ { \mathrm { c } }$ . Through rolling optimization, the proposed control strategy ensures safe vehicle operation and eliminates HV-induced randomness to a certain extent. 

According to the control framework shown in Fig. 3, the process of the CAV cooperative control strategy is composed of six steps: 

Step 1: Information prediction. The system predicts the trajectories of HVs in the control area, and the predicted trajectory information is then shared among CAVs and between CAVs and the control centre. 

Step 2: Dynamic weighting. At time t, the state of the CAVs in the cooperative control area is initialized, and their information is input into a pretrained Transformer. Since the AWM is not involved in system iteration, this step is performed prior to the BDM. 

Step 3: CAV trajectory solving. The set of control schemes is solved by CAV for periods $k _ { \mathrm { c } } \Delta t$ to $( k _ { \mathrm { c } } + N _ { \mathrm { p } } ) \Delta t$ based on historical predicted trajectories. Subsequently, the optimal solution is selected according to the control weight obtained in Step 2. As the process relies only on historical data, this part of the computational task is performed independently by each CAV involved in the control. 


Table 2 Values of the main parameters.


<table><tr><td>Notation</td><td>Description</td><td>Value</td></tr><tr><td>l</td><td>Length of cars, trucks (m)</td><td>5,12</td></tr><tr><td>s0HV</td><td>Desired headway of C-C, C-T, T-T, T-C (m)</td><td>0.85,1.35,1.11,1.53</td></tr><tr><td>εHV</td><td>Safe headway time of C-C, C-T, T-T, T-C (s)</td><td>1.5,1.8,2,2.2</td></tr><tr><td>εCAV</td><td>Safe headway time of CAV car, CAV truck (s)</td><td>1.2</td></tr><tr><td>aHVmax</td><td>Maximum acceleration of C-C, C-T, T-T, T-C (m/s2)</td><td>1.01,1.03,0.78,0.74</td></tr><tr><td>aCAVmax</td><td>Maximum acceleration of CAV car, CAV truck (m/s2)</td><td>1.01,0.78</td></tr><tr><td>aHVmin</td><td>Minimum deceleration of C-C, C-T, T-T, T-C (m/s2)</td><td>-2.26, -2.12, -1.7, -1.61</td></tr><tr><td>aCAVmin</td><td>Minimum deceleration of CAV car, CAV truck (m/s2)</td><td>-2.26, -1.61</td></tr><tr><td>νHVmax</td><td>Maximum speed of C-C, C-T, T-T, T-C (m/s2)</td><td>27,19.2,20.6,17.6</td></tr><tr><td>νCAVmax</td><td>Maximum speed of CAV car, CAV truck (m/s)</td><td>27,20.6</td></tr><tr><td>k1</td><td>Spacing error weight</td><td>0.23</td></tr><tr><td>k2</td><td>Velocity error weight</td><td>0.07</td></tr><tr><td>γramp</td><td>Ramp lane value</td><td>3</td></tr><tr><td>ΔaHV,car</td><td>HV car lane-changing threshold</td><td>0.3</td></tr><tr><td>ΔaHV,truck</td><td>HV truck lane-changing threshold</td><td>0.5</td></tr><tr><td>ΔaCAV</td><td>CAV lane-changing threshold</td><td>0.3</td></tr><tr><td>p</td><td>Commutation parameter</td><td>1</td></tr><tr><td>Mo</td><td>Number of particles in the population in NSGA-II</td><td>100</td></tr><tr><td>Ho</td><td>Maximum number of iterations in NSGA-II</td><td>100</td></tr><tr><td>h</td><td>Number of heads in the multihead attention</td><td>10</td></tr><tr><td>N</td><td>Number of encoder and decoder layers</td><td>2</td></tr></table>

Step 4: Iterative optimization. The control centre evaluates the system control scheme based on Eqs. (24) and (25). The process terminates when it reaches the maximum number of iterations or when the system performance converges. At this point, the set of CAV trajectories that will most benefit global optimization is chosen. Otherwise, steps 2 and 3 are repeated, and all CAVs redesign their behavioural decision-making programmes based on the prediction results. 

Step 5: Control execution. The final solution is transmitted as a command to the CAV. Controls are implemented where it is determined that there is no risk of collision (Frejo and Camacho, 2012). 

Step 6: End. 

# 6. Case analysis

# 6.1. Parameter setting

The improved IDM (Liu et al., 2016) is adopted to model the following behaviour of HVs. The improved IDM considers the performance discrepancies among various car models and the interactions between HVs. CAVs use the classic ACC following model (Vollrath et al., 2011). The Mobile model (Kesting et al., 2007) can reflect the differences in vehicle following behaviour and lanechanging behaviour, and setting different lane changing thresholds and cooperative lane changing parameters can reflect the differences in a vehicle’s desire to change lanes. Therefore, the Mobile model is used to describe the free lane-changing behaviour of all types of vehicles (Peeta et al., 2005). In addition, on-ramp vehicles randomly make lane changes based on the mandatory lane change probability. 

For the prediction time domain $N _ { \mathfrak { p } }$ of the controller, $N _ { \mathrm { p } } = 5 0$ is taken as a combination of the control effect and the computational cost of the model in this study. To ensure driving safety, the control time domain $N _ { \mathrm { c } } = 1$ is usually taken as less than $N _ { \mathfrak { p } }$ (Ding et al., 2023). 

The values of other important parameters taken in the simulation are shown in Table 2. 

# 6.2. Feasibility validation

First, we test the feasibility of the proposed strategy to demonstrate how CAV trajectories affect the entire freeway system. The experiment uses real traffic flow data collected between 5:00 PM and 5:30 PM in 2005 from the I-80 segment of the NGISM dataset. The initial speeds, entry times, and types of vehicles are consistent with real-world scenarios. The experimental setup includes two mainline lanes and one ramp lane, with the specific parameters detailed in Table 3. The simulation lasts a total of 1800 s, with control applied to CAVs by the control centre starting at the 1000th second. 

Fig. 6 shows a comparison of the vehicle trajectories in each lane across scenarios without CAVs, scenarios with a small number of uncontrolled CAVs, and scenarios with a small number of controlled CAVs. In the diagrams, grey represents HV cars, red represents HV trucks, and blue represents CAVs. Since there are relatively few trucks, this experiment does not consider CAV trucks. 

Fig. 6(b) shows that, owing to the lower safe headway time and higher speed tracking capability of CAVs, the total parking delay in scenarios with a small number of uncontrolled CAVs decreased by $7 \%$ . However, the driving behaviour of CAVs in Fig. 6(b) did not significantly differ from that of HVs, and congestion issues in merged areas experienced only limited improvement. Influenced by the BDM-AWM algorithm, the driving behaviour of CAVs undergoes significant changes. First, controlled CAVs are more likely to preemptively switch to lane 1 relative to the uncontrolled scenario to gain long-term benefits. Second, controlled CAVs can utilize continuous lane changes to avoid collision risks by predicting the trajectories of vehicles in all lanes and can even successfully merge into the main lane traffic flow without meeting the safety requirements of mandatory lane changes. Compared with those in Fig. 6(a) and (b), the queuing phenomenon in Fig. 6(c) notably decreases, resulting in a $1 4 . 3 \%$ reduction in the overall vehicle parking delay relative to that in Fig. 6(a) and a $7 . 6 \%$ reduction compared with that in Fig. 6(b). In addition, relative to Fig. 6 (b), the time-integrated time-to-collision (TIT) in Fig. 6(c) decreases by $3 . 7 ~ \%$ . This phenomenon indicates that even in the absence of CAV cooperative behaviour, controlled CAVs still exhibit strong path optimization capabilities. 

To demonstrate the collaborative relationships among CAV trajectories under the influence of the BDM-AWM algorithm, we set 118 cars as CAVs, accounting for approximately $1 5 ~ \%$ of the total number of vehicles. The baseline method involves no control (NC). We extract and compare the vehicle trajectories within each lane of the simulation segment from 800 to 1200 s. Comparing Fig. 7 (a) and (b), it can be observed that the total parking delay and TIT in the BDM-AWM scenario decrease by $5 7 . 4 \%$ and $6 . 7 ~ \%$ compared with those in the NC scenario. This significant reduction greatly alleviates traffic congestion and virtually eliminates queuing phenomena. Furthermore, as indicated in the box, the CAV in lane 1 decelerates before accelerating in situations with large gaps ahead, creating a safe gap for the merging of lane 2 vehicles. This phenomenon demonstrates that the BDM-AWM not only optimizes the behavioural decisions of individual vehicles but also fosters cooperative relationships among CAVs, achieving system optimization effects. 


Table 3 Values of the experimental scenario.


<table><tr><td>Lane classification</td><td>Description</td><td>Value</td></tr><tr><td>Lsa</td><td>Length of the acceleration zone (m)</td><td>375</td></tr><tr><td>Lma</td><td>Length of the induction zone (m)</td><td>128</td></tr><tr><td>L</td><td>Length of the experimental roads (m)</td><td>600</td></tr></table>


Legend


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/65dba4ee215fd4cdd6f5bf5cce0d06de6edb52f2066d2d7b49202546de4380e1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/6357fd1648384be8b622e348e6836b9bdcb279a1e3e4904ad460a98356cc6dee.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/f46c57f1a1c134d2227133d4f8d792763cf4e8fd72da294811304f321d396736.jpg)



(a)Scenarios without CAVs


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/17a1a0d4edbb68af26070c3f4c9787b3f06c43f5bb19a463b398efcfcf1df26f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/7169166f6dafb27075619d88bf9218377f35e15ee7b610c7f567a9b7a7f6d584.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/a483d3fe4744737aa85702bb9975836c2a7cf4bef8c6bd1b64c150b7dfff1b78.jpg)



(b) Scenarios with a small number of uncontrolled CAVs


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/01fd003d72374f5a27e718e41b6609a8c2163f9b48c7ca110c493ce6c204579a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/52ed15340f0e77f4ac0be07d3bc6dfb336e13c16bec2dad3633f0fd7a7b4dfd2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/19735d9f4e4b7c8394d164daf8b5b0f84548efd0ed630119a05d38f2594a2a04.jpg)



(c) Scenarios with a small number of controlled CAVs



Fig. 6. Vehicle trajectories in each lane under different control scenarios.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/6aceadd59c4eaa9a5265192dc3d3c8681375957f744840eba0042e64776826ca.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/057cfe76de74487ca23abba8d67910d57f57aa3aa7de68f6d44ca514ceab1fbd.jpg)



(a)NC


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/684bbc96f036183173ab9f92c449545fc60ace345ebe4536c8506bac07011ccf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/fd3fde39a09d22d79b9cfd45a00ad70d43d91903b7b972854cafcfbedd8b27e4.jpg)



(b)BDM-AWM



Fig. 7. Vehicle trajectories in each lane under different control scenarios.


# 6.3. Result analysis

Next, we alter the relevant parameters and input flow rates of the experimental scenario to validate the practical performance of the BDM-AWM in more complex scenarios. The entire simulation lasts $3 0 \ \mathrm { m i n }$ , and the scenario parameters are shown in Table 4. 

To compare the results of the cooperative control strategy (BDM-AWM) proposed in this paper, three control scenarios, the NC, BDM alone and BDM-AWM, are analysed. To diminish the randomness of the experiment, a fixed control weight λ of 0.5 is chosen when using BDM alone. The vehicle trajectories in the three control scenarios with $2 0 \%$ , $6 0 \%$ , and $1 0 0 \%$ CAV-15 % truck penetration rates 


Table 4 Values of the experimental scenario.


<table><tr><td>Lane classification</td><td>Description</td><td>BDM</td></tr><tr><td>Lsa</td><td>Length of the acceleration zone (m)</td><td>300</td></tr><tr><td>Lma</td><td>Length of the merging zone (m)</td><td>300</td></tr><tr><td>L</td><td>Length of the experimental roads (m)</td><td>2000</td></tr></table>

are shown in Fig. 8. The colour of the trajectory points is correlated with the vehicle speed. 

Fig. 8(a), (d), and (g) illustrate that the vehicles in lane 1 do not slow under the nc strategy, and they maintain an almost uniform speed through the merging zone; this creates large, unnecessary gaps downstream of the trucks. Due to the lack of cooperative behaviour between vehicles, vehicles in lane 2 are forced to slow down and wait for an opportune moment to merge. The action thus decreases the gap available for on-ramp vehicles, causing a significant number of vehicles to slow, stop, or even queue. 

Fig. 8(b), (e), and (h) show that the space–time gaps in lane 1 decrease considerably because of the influence of the BDM strategy, resulting in a decrease in capacity. The vehicles in the mainline lanes cooperate with each other to create a safe acceptable gap for the ramp vehicles. Moreover, the free lane-changing behaviour of ramp vehicles increases. The BDM offers clear and appropriate opportunities for on-ramp vehicles to merge onto the mainline without stopping or even slowing down. Compared with that in the NC scenario, the mandatory lane-changing behaviour in the BDM scenario is reduced by $4 8 . 9 \%$ , $5 9 . 3 \%$ , and $5 2 . 6 \%$ at CAV penetration rates of $2 0 \%$ , $6 0 \%$ , and $1 0 0 \%$ , respectively. 

According to Fig. 8(c), (f), and (i), the deceleration of the mainline vehicles decreases and the free lane-changing behaviour of the ramp vehicles increases under the BDM-AWM compared with the BDM scenario. The BDM-AWM significantly improves the overall traffic flow. Compared with those in the BDM scenario, the mandatory lane-changing behaviour in the BDM-AWM scenario decreases by $9 . 7 ~ \%$ , $2 0 . 1 ~ \%$ , and $2 1 . 3 \%$ at CAV penetration rates of $2 0 \%$ , $6 0 ~ \%$ , and $1 0 0 \%$ , respectively. 

To explore the role played by trucks in the cooperative control strategy, the dwell time of trucks in the three lanes under different control conditions is recorded. The corresponding dwell times for trucks in different lanes given a typical scenario of $6 0 \%$ CAVs and 15 $\%$ trucks are shown in Table 5. 

Table 5 shows that in the NC scenario, trucks spend the most time in lanes 2 and 3 due to the lower desire to change lanes. Conversely, the trucks spend much less time on the on-ramp under the BDM and BDM-AWM strategies. Notably, the total dwell time of trucks is the lowest in the BDM-AWM scenario, with the dwell time ratio at the ramp amounting to only $2 3 . 2 \%$ , which is lower than the $2 6 \%$ in the BDM scenario. This shows that the cooperative control strategy introduced in this paper has the potential to establish a 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/6892e0812acb1dbc5ea9e9c5a38351e40b869eb1af2346b27e3a7e6d5d25bcd4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/19e9c1acd0cdf23c1a022a6ad11d269ca5dc1863e7f15e1ddcd17767b33c0c50.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/1872a9af35edebf9e829f88978ab351c2e8ddaf80daaac75649ba4dfc834049c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/3537741b1f40fded43492a89dc71a748ea75eb6b0a8d29bfeda5c3753ec55d1f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/d532f3900cc583a011b764fb31e4b63e64234c779f3331b8013becbdc4062125.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/6842807a72d69b5975084ce8297c5b072ca7d9535d994d466a9ce01f334f8260.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/619d491a4de7dabde17c5cb087d1ab052ec83af5ab238ee32737605489051ece.jpg)



(a) NC-20% CAV



(b) BDM-20% CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/866ea3d6ed71333bff925cf405254e666195785478cc26ebf2263eae9566682e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/83d1e70576826bba3bda82ecf0ae7d2dff4cca405f034dbc10abd6d005e2f255.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/9b632ebe35e8fb2534c56c4c4cfedf89a2eb4b27ae804db790723d9d9028c5b6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/b1ddecf01779d50f13e480bc1669e0080a7227c82ef62ebcb84138e49af852ef.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/d4cd2e142c7e535e0128edeb80266518ad970d3e72302291fb1f48b735723c10.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/e72f3aa4b7df40fe33776137f9d104c6ae55155062bf6bfac651999fb85cd743.jpg)



(c)BDM-AWM-20% CAV



(d) NC-60% CAV



Fig. 8. Vehicle trajectories in each lane under different control scenarios.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/c5d5f423e10681e707fb6174280d26f5d66594f52aa726cf151faa9f4ed15072.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/8465fba95808e4a6b8d9730cbb3114dd3c8bf39a22bc08490e0edfecae0cff8c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/d04e4320c0e241d45e17694e430dc7008c10b4f3f23b936ea9e6897ffb965ae0.jpg)



(e) BDM-60% CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/bd71e6d3c8f364e8c0d4f9429f441a7aa6347ca284607aac5bc810b24ba3dc12.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/9f0b8e8238ec91b43db0f1d3395d0b1a9d535c0eee63156c5388267f9022f5be.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/88c74cf7490f21963974d82ddcae11106c8f1374533703facb493f8de7d1ddda.jpg)



(f)BDM-AWM-60% CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/30c1a23896d6cb99c3454133c208e1dccff6668cf20e86421ea693e416a13536.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/fcfb4f676d2c481a987e6e0e345b06e9f1a450144de9e4465d9d44fa25e0ff1e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/e687da95d3082fb2d6686cb20409d2da654281ed986cf4132b46a30fdab9e46e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/8230df0f1112b06e5ba10e389b18aac12b2ace62808d936fb7d450a3eb9c0fe7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/0910ecfdb5c4f1f93ba7a3913dab958ce31c3a37226756419372fc8f5c86f9be.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/f4ef4182abec753866285a962430b3e91bc8b910e6e64f4c9e6f55b248c6d398.jpg)



(g) NC-100% CAV



(h) BDM-100% CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/9d1a376e1f748bffb3afc473e97482277f643cd5e44bed9cb4b23d01c16a105b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/41416fc517bf2e15ba9316326adb9b7706843ae91a855cbb0cfebb889327f5a2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/fa496f33dbb39bd0ca92d4f9692fff2ee4130c4c20120d351077158e437a84d8.jpg)



(i)BDM-AWM-100% CAV



Fig. 8. (continued).



Table 5 Total dwell time of trucks in different lanes (s).


<table><tr><td>Lane classification</td><td>NC</td><td>BDM</td><td>BDM-AWM</td></tr><tr><td>Lane 1</td><td>6726</td><td>8300</td><td>8211</td></tr><tr><td>Lane 2</td><td>7937</td><td>6584</td><td>6487</td></tr><tr><td>Ramp 3</td><td>5841</td><td>5243</td><td>4440</td></tr></table>

secure lane-changing environment for trucks and to suppress traffic shocks caused by truck lane-changing behaviour. 

For the two primary objectives of the control strategy, the effectiveness of control is examined in terms of traffic efficiency and traffic safety. 

# (1) Traffic efficiency

The total parking delay is selected as a traffic efficiency indicator, which illustrates how control strategies impact traffic efficiency in different scenarios. 

Fig. 9 displays the total parking delay results for 27 scenarios, with 3 CAV penetration rates and 3 truck penetration rates. It’s can be seen that the trucks act as ‘moving bottlenecks’ in the traffic flow, and the input flow to the merging zone is restricted. Only a small number of trucks can have a large impact on vehicle queuing phenomenon. Additionally, the BDM-AWM strategy is better at minimizing parking delays than the NC and BDM strategies are. The total stopping delay of the BDM-AWM strategy is lower in all con ditions. The statistics also show variations in the total parking delay under different truck penetration rate scenarios. 

# (2) Traffic safety

Considering the differences in vehicle performance, the TIT (Rahman and Abdel, 2018) is chosen as the traffic safety indicator because of its greater accuracy in reflecting the control strategy’s impact on traffic safety. As shown in Eq. (28), the TIT utilizes the integral of the crash time curve to display the safety level, and a higher TIT signifies a greater risk of collisions. 

$$
T I T = \sum_ {i = 1} ^ {N} \int_ {0} ^ {T} \left[ T T C _ {\text {t h r e s h o l d}} - T T C _ {i} (t) \right] d t, \quad 0 <   T T C _ {i} (t) \leq T T C _ {\text {t h r e s h o l d}} \tag {28}
$$

The TITs for different scenarios are shown in Fig. 10. 

As shown in Fig. 10, the TIT of the BDM-AWM scenario is consistently the lowest across all the scenarios. Compared with the NC scenario, the BDM-AWM scenario yields an average TIT reduction rate of $6 7 . 8 ~ \%$ , whereas the BDM scenario yields an average reduction rate of $5 9 . 7 \%$ . This evidence suggests that the AWM is effective in enhancing traffic safety. A comparison of the TITs across 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/a2783fa4a74e91fca373f7cbeb158357744513e451c136e8816e5048498270b6.jpg)



(a) $0 \%$ Truck


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/66c0945d286ed154c6575b7307610c88007e722b163b1420a4775dfcd87c5484.jpg)



(b) $5 \%$ Truck


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/e2bdd631f24ed472dad2a7ec184af811b8d47abf8a294b083f0472a48269dbcb.jpg)



(c) 15% Truck



Fig. 9. Total parking delay for different scenarios.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/02215f7259dcbc82b5c1593193b34105f472392a79261f103b852bf309f6deae.jpg)



(a) 0%Truck


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/b4c076b8c5d84b4e1715abe628362bd2cad3f049add9d1c3c921191d90486f37.jpg)



(b) 5%Truck


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/8fd39b85e81f4e5c400f629dcbd6bbe6bf3cf456dd150ddef4cc34be473d13cb.jpg)



(c) $1 5 \%$ Truck



Fig. 10. TIT for different control scenarios under different penetration rate conditions.



Table 6 TTTs, TDs and RTTCs for different scenarios.


<table><tr><td>CAV PR</td><td>Control method</td><td>Truck PR</td><td>TTT(s)</td><td>TD(s)</td><td>RTTC(1/s)</td></tr><tr><td rowspan="3">0 %</td><td rowspan="3">NC</td><td>0 %</td><td>123,498</td><td>63,232</td><td>143,742</td></tr><tr><td>5 %</td><td>125,304</td><td>63,475</td><td>90,098</td></tr><tr><td>15 %</td><td>121,801</td><td>56,942</td><td>75,840</td></tr><tr><td rowspan="9">20 %</td><td rowspan="3">NC</td><td>0 %</td><td>116,190</td><td>55,924</td><td>42,564</td></tr><tr><td>5 %</td><td>117,289</td><td>55,460</td><td>39,097</td></tr><tr><td>15 %</td><td>119,612</td><td>54,753</td><td>37,915</td></tr><tr><td rowspan="3">BDM</td><td>0 %</td><td>100,298</td><td>40,032</td><td>27,188</td></tr><tr><td>5 %</td><td>109,875</td><td>48,046</td><td>22,638</td></tr><tr><td>15 %</td><td>113,139</td><td>48,280</td><td>18,124</td></tr><tr><td rowspan="3">BDM-AWM</td><td>0 %</td><td>101,215</td><td>40,949</td><td>23,141</td></tr><tr><td>5 %</td><td>107,347</td><td>45,518</td><td>19,632</td></tr><tr><td>15 %</td><td>112,021</td><td>47,162</td><td>16,489</td></tr><tr><td rowspan="9">60 %</td><td rowspan="3">NC</td><td>0 %</td><td>75,769</td><td>15,503</td><td>36,182</td></tr><tr><td>5 %</td><td>103,236</td><td>41,407</td><td>27,846</td></tr><tr><td>15 %</td><td>115,753</td><td>50,894</td><td>24,486</td></tr><tr><td rowspan="3">BDM</td><td>0 %</td><td>71,271</td><td>11,005</td><td>19,131</td></tr><tr><td>5 %</td><td>99,239</td><td>37,410</td><td>16,991</td></tr><tr><td>15 %</td><td>111,658</td><td>46,799</td><td>13,307</td></tr><tr><td rowspan="3">BDM-AWM</td><td>0 %</td><td>70,848</td><td>10,582</td><td>16,912</td></tr><tr><td>5 %</td><td>95,463</td><td>33,634</td><td>15,190</td></tr><tr><td>15 %</td><td>109,918</td><td>45,059</td><td>11,545</td></tr><tr><td rowspan="9">100 %</td><td rowspan="3">NC</td><td>0 %</td><td>69,352</td><td>9,086</td><td>27,907</td></tr><tr><td>5 %</td><td>98,370</td><td>36,541</td><td>16,847</td></tr><tr><td>15 %</td><td>114,543</td><td>49,684</td><td>12,699</td></tr><tr><td rowspan="3">BDM</td><td>0 %</td><td>66,573</td><td>6,307</td><td>13,733</td></tr><tr><td>5 %</td><td>97,837</td><td>36,008</td><td>8,255</td></tr><tr><td>15 %</td><td>103,442</td><td>38,585</td><td>6,563</td></tr><tr><td rowspan="3">BDM-AWM</td><td>0 %</td><td>66,880</td><td>6,612</td><td>11,490</td></tr><tr><td>5 %</td><td>92,251</td><td>30,422</td><td>7,184</td></tr><tr><td>15 %</td><td>103,111</td><td>38,252</td><td>6,068</td></tr></table>

different truck penetration rate scenarios reveals that the risk of vehicle collisions is lower in scenarios with higher truck penetration rates. The main reason for this phenomenon is that the overall speed of the traffic flow is lower in the case of mixed trucks, reducing the risk of vehicle collisions. 

The total travel time (TTT), total delay (TD), and RTTC statistics for the experimental road are shown in Table 6. In the low CAV penetration scenario, the proportion of trucks has less impact on delays due to high congestion. In addition, TTT and TD are significantly higher in the high truck penetration scenario than in the low truck penetration scenario in most cases. The benefits of the BDM-AWM are evident across all scenarios. Compared with the NC scenario, the BDM-AWM featuring $1 0 0 \%$ CAV penetration significantly lowers the TTT by $2 9 . 2 \%$ , TD by $5 9 \%$ , and RTTC by $9 2 \%$ on average. This result proves that the BDM-AWM strategy can help release traffic congestion issues in merging zones. 

# 6.4. Sensitivity analysis

In optimization problems, the performance of the system is directly related to the number of iterations, and the set of feasible system solutions converges to the optimal system solution (Tajalli et al., 2022). The conditions under which the system converges may vary at different CAV penetration rates. In addition, the relationship between traffic states and control weights, HV stochastic features and control performance are also worth discussing. Therefore, the number of system iterations $k$ ,the optimal control weights λ and the human driving uncertainty were selected for sensitivity analysis. The corresponding results are shown below. 

# (1) Number of system iterations

Fig. 11 illustrates the correlation between the system’s target value $F _ { 1 } , F _ { 2 }$ and the number of iterations for varying CAV penetration rates at $t = 1 0 0 0 s$ . As shown, the system’s performance improves as the number of iterations increases. At the $2 0 \%$ CAV penetration 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/0248d90e5a5e749401d4b9b1436821ab10fc8f89916436e64c228eac2bc7273c.jpg)



(a) 0%Truck-20%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/511c256ee452a482856f8a22341f7b1e965732a31f4602a16ade253575dc4b96.jpg)



(b) 0%Truck-60%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/9848b3a6d531919daf7f9c3cd01993c2c715720e841990023b31bbaaf3003d78.jpg)



(c) 0%Truck-100%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/99f406911e6517c0058997aece9eb838863f2b018bef9ee388ff1968256dec5a.jpg)



(d) 5%Truck-20%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/7c119cf50b48cc7afaee3776f60ca514901e05565e78b21b3886f35fbe61f931.jpg)



(e) 5%Truck-60%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/842b39298af3504ed73f705cd76353fbddb5b56e50447791a07ae4e732d1e4ae.jpg)



(f) 5%Truck-100%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/e87e7b28ccfe8d2707f5ea505140b52e630e0b29f899c5abcf36e4024852ff50.jpg)



(g) 15%Truck-20%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/d9830fb6520043470444cb7822c6e6ad27cbcac5737fc620aebd2e3c8156b8f8.jpg)



(h) 15%Truck-60%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/89644f19e08d43a1bba2e628cd5e2b81f6bab1f89d2c48da8fcde4aa46f9db2a.jpg)



(i) 15%Truck-100%CAV



Fig. 11. Variation in the objective function during the iteration process under different conditions.


rate, the system nearly converges after the second iteration. When the CAV penetration rate reaches $6 0 \%$ , the system significantly changes during the initial three iterations. When the CAV penetration rate is increased to $1 0 0 \% , F _ { 1 } , F _ { 2 }$ still exhibit a significant change at the 5th iteration. As CAV penetration increases, the system requires a greater number of iterations. This increase is due to the increase in the CAV proportion, which provides a multitude of solutions for the system. Consequently, CAV negotiations transpire more frequently. Additionally, the inclusion of trucks did not significantly impact the system’s iteration requirements. To balance the computational cost and control effectiveness, in the experiments of this study, the maximum number of iterations, $k _ { \operatorname* { m a x } } = 2 , 3 , 5$ , is set for CAV penetrations of $2 0 \%$ , $6 0 ~ \%$ , and $1 0 0 ~ \%$ . 

# (2) Distribution of adaptive weights

We choose a typical $6 0 \%$ CAV-5 % truck environment to explore the distribution of optimal control weights under different traffic inputs. Fig. 12 displays the results, where 0 indicates exclusive consideration of traffic safety and 1 indicates exclusive consideration of traffic efficiency. Fig. 12 illustrates that prioritizing traffic efficiency is generally the preferable control strategy. The increase in road capacity provides a secure and pleasant driving environment for vehicles. However, in contrast to high-flow input situations, the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/7b4cc1876823f91a66093eeed0162caa7553a2b77bd4071b038c13d65e9859f4.jpg)



Fig. 12. Distribution of weights for different flow input conditions.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/f5677ac320f5b0efb4910092b4f9be691adeb0f1c361a8229375c386173635e5.jpg)



(a) Efficiency performance


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/4fd83d0ef0dacb580511ac3516f8017325ba9529bddefb0be1fb815115e3241d.jpg)



(b) Safety performance



Fig. 13. Performance variation of the BDM-AWM with different CAV and HVW penetration rates.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/c6cca936b421f2d1f35a1043f550942dce556726af54e502255f4e54325ace48.jpg)



(a) Efficiency performance


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/f2c753756879417a132c92d8892ac75c09bb29c502cda9e7e24389b4fb158b8a.jpg)



(b) Safety performance



Fig. 14. Performance variation of the BDM-AWM with different CAV and OVM penetration rates.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/65e517b31b6a61c49e3490261a192244a65479020e2a2e699131f12130058b43.jpg)



Fig. 15. Performance variation of the BDM-AWM with different CAV and OVM penetration rates.


importance of traffic efficiency is reduced to varying degrees in medium- and low-flow scenarios. This phenomenon indicates that optimizing traffic efficiency through control strategies has limited impacts when traffic flow is in a state of free flow. In this case, prioritizing traffic safety in the control strategy leads to better results. 

# (3) Stochastic feature of traffic

The robustness of the BDM-AWM can be verified by setting HVs without the vehicle awareness device (HVW) with different penetration rates. Unlike CAVs and HVs, HVWs cannot be controlled or participate in information interaction. Therefore, HVWs can be regarded as a type of interference in the behavioural decision of CAVs (Wang et al., 2023b). 

For HVW, CAV does not have direct access to its information. In the computation stage, to meet the needs of the BDM, we estimate the current speeds and positions of HVWs by linear interpolation (Ni and Wang, 2008) and assume that their speeds do not change in the prediction time domain. As for the lane-changing behaviour of HVWs, it is uniformly ignored. 

Fig. 13 shows the magnitude of changes in the efficiency performance (i.e., total stopping delay) and safety performance (i.e., TIT) of the BDM-AWM for different CAV and HVW penetration rates. The experimental data show that when the penetration rate of HVW is lower than $4 0 \%$ , the overall degradation of the control performance of the BDM-AWM is small, which indicates that the BDM-AWM is valid to resist interference. In addition, the robustness of the BDM-AWM improves with increasing CAV penetration. 

# (4) Car-following behaviour of HVs

In previous experiments, the improved IDM model was used for both the HV’s car-following model and the prediction model. To verify the effect of HV’s car-following behaviour on the performance of the control strategy, the OVM model is used to simulate the carfollowing behaviour of some HVs in the experiments (Bando et al., 1995), and the improved IDM model is still used to predict the HV’s 

trajectory in the BDM. 

Fig. 14 shows the magnitude of changes in the efficiency performance (i.e., total stopping delay) and safety performance (i.e., TIT) of the BDM-AWM for different CAV and OVM-HV penetration rates. The experimental data show that the performance of the BDM-AWM shows a negative correlation with the OVM-HV penetration rate. When the driving behavior of the HV differs from the predicted trajectory, the performance of the control strategy is affected to different degrees. The trend is most pronounced especially when the OVM-HV penetration reaches $6 0 ~ \%$ . Nevertheless, the maximum degree of control performance degradation of BDM-AWM is less than $1 5 \%$ and the average degree of degradation is less than $5 \%$ . In summary, the HV’s car-following model has a small impact on the effectiveness of the control strategy. 

Further, RTTCs were extracted for all individual vehicles in the $4 0 \%$ CAV- $0 \%$ OVM-HV and $4 0 \%$ CAV- $6 0 ~ \%$ OVM-HV scenarios, respectively. Fig. 15 illustrates the probability distribution of the values of RTTCs for the two scenarios. It can be seen that the RTTC values in both scenarios show a single-peak distribution, with the peaks all located around the point (0.05, 60), which proves the remarkable effectiveness of BDM-AWM in eliminating the collision risk. Compared to the $0 \%$ OVM-HV scenario, the slopes and peaks of the RTTC probability density curves are lower in the $6 0 ~ \%$ OVM-HV scenario, which suggests that the prediction model error degrades the performance of the BDM-AWM in terms of traffic safety. 

# 7. Conclusion

To alleviate congestion and improve traffic safety in the merging area of freeways, a CAV distributed control strategy for mixedvehicle traffic flow is proposed in this paper. This strategy, which is based on the MPC framework, determines the optimal behavioural decision set for CAVs by solving a multi-objective nonlinear mixed-integer programming problem at the vehicle level. To ensure the feasibility of vehicle-level decisions and enhance system-level optimization, CAVs share and coordinate their behavioural decisions, preventing the strategy from falling into a local optimum. Additionally, an adaptive weighting model is created based on a Transformer neural network, allowing the control strategy to adjust to the constantly changing traffic state. 

Four conclusions can be drawn from this study. First, regarding the congestion issue in freeway merging zones, the proposed BDM can effectively increase traffic efficiency and safety in merging zones. Second, as the CAV penetration rate increases, the probability of CAV negotiation and cooperation increases. The effectiveness of cooperative control strategies gradually improves, and traffic efficiency and safety indicators in the merging zone also improve. Third, the combined use of the BDM and AWM improves system performance to a greater degree than using only the BDM. This is particularly evident in traffic safety. Fourth, the cooperative control strategy proves to be more effective in the mixed-vehicle environment; this can be attributed to the fact that it eliminates the effects caused by the interactions of mixed vehicles. 

This study is based on the MPC framework, which addresses system perturbations and model uncertainties mainly through rolling optimization. However, the robustness of the system is not theoretically supported. Ensuring the ability of control strategies in more complex scenarios is one of the main future research directions. Second, the trajectory prediction of HVs in this study lacks full precision, which limits the solution space for vehicle behaviour decisions. It is worth investigating how to increase the accuracy of the control strategy in the future. 

# CRediT authorship contribution statement

Lang Zhang: Methodology, Software, Writing – original draft, Data curation. Heng Ding: Methodology, Supervision, Writing – review & editing, Funding acquisition. Zeyang Cheng: Investigation, Writing – review & editing, Data curation. Xiaoyan Zheng: Writing – review & editing, Data curation, Investigation. Weihua Zhang: Funding acquisition, Supervision. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Acknowledgements

This research was financially supported by the National Natural Science Foundation of China (Grant Nos. 52072108 and 52372326), the Science and Technology Plan Project of Anhui Housing and Urban Rural Construction, China (2022-YF145) and the Municipal Natural Science Foundation of Hefei, China (Grant No. 2022020). 

# Appendix A. Expansion of BDM on vehicle lateral motion

The modelling of the lateral motion of the vehicle can be achieved by setting successive y-variables and lateral velocity variables. To do this, the following modifications to the BDM are required. 

$$
f _ {i} ^ {1} = \max  \left(\sum_ {t \in T} \left(x _ {i} ^ {t} - \gamma \left(\alpha_ {i} ^ {t} + \beta_ {i} ^ {t}\right) - \kappa \left| a _ {\mathcal {Y}, i} ^ {t} \right| - \delta \left| a _ {x, i} ^ {t} \right|\right)\right) \tag {A1}
$$

$$
f _ {i} ^ {2} = \min  \left(\sum_ {t \in T} \left\{ \begin{array}{l l} \frac {\nu_ {x , i} ^ {t} - \nu_ {x j} ^ {t}}{x _ {j} ^ {t} - l _ {j} ^ {t} - x _ {i} ^ {t}} & \text {i f} \nu_ {x, i} ^ {t} > \nu_ {x, j} ^ {t} \\ 0 & \text {e l s e} \end{array} \right.\right) \tag {A2}
$$

where $x _ { i } ^ { t }$ is the longitudinal position of vehicle $i \in I$ at time $t \in T$ ; $a _ { x , i } ^ { t }$ and $a _ { y , i } ^ { t }$ are the longitudinal and lateral accelerations of vehicle $i \in I$ at time $t \in T$ , respectively; $\nu _ { x , i } ^ { t }$ is the longitudinal velocity of vehicle $i \in I$ at time $t \in T$ . 

$$
x _ {i} ^ {t} = x _ {i} ^ {t - 1} + v _ {x, i} ^ {t} \Delta t + \frac {1}{2} a _ {x, i} ^ {t - 1} \Delta t ^ {2} \tag {A3}
$$

$$
y _ {i} ^ {t} = y _ {i} ^ {t - 1} + v _ {y, i} ^ {t} \Delta t + \frac {1}{2} a _ {y, i} ^ {t - 1} \Delta t ^ {2} \tag {A4}
$$

where $\nu _ { y , i } ^ { t }$ is the lateral velocity of vehicle $i \in I$ at time $t \in T ; y _ { i } ^ { t }$ $y _ { i } ^ { t }$ is the lateral position of vehicle $i \in I$ at time $t \in T$ . 

$$
v _ {x, i} ^ {t} = v _ {x, i} ^ {t - 1} + a _ {x, i} ^ {t - 1} \Delta t \tag {A5}
$$

$$
v _ {y, i} ^ {t} = v _ {y, i} ^ {t - 1} + a _ {y, i} ^ {t - 1} \Delta t \tag {A6}
$$

$$
a _ {\min , i} ^ {x} \leq a _ {x, i} ^ {t} \leq a _ {\max , i} ^ {x} \tag {A7}
$$

$$
a _ {\min , i} ^ {y} \leq a _ {y, i} ^ {t} \leq a _ {\max , i} ^ {y} \tag {A8}
$$

where $a _ { \mathrm { m a x } , i } ^ { x }$ and $a _ { \mathrm { m i n } , i } ^ { x }$ are the maximum and minimum longitudinal acceleration of vehicle $i \in I _ { : }$ , respectively; $a _ { \mathrm { m i n } , i } ^ { y }$ and $a _ { \mathrm { m a x } , i } ^ { y }$ are the maximum and minimum lateral accelerations of vehicle $i \in I$ , respectively. 

$$
0 \leq v _ {x, i} ^ {t} \leq v _ {\max , i} \tag {A9}
$$

$$
- \nu_ {\min , i} ^ {y} \leq \nu_ {y, i} ^ {t} \leq \nu_ {\max , i} ^ {y} \tag {A10}
$$

$$
0 \leq v _ {x, i} ^ {t 2} + v _ {y, i} ^ {t 2} \leq v _ {\max , i} ^ {2} \tag {A11}
$$

where $\nu _ { \mathrm { m a x } , i } ^ { y }$ and $\nu _ { \mathrm { m i n } , i } ^ { x }$ are the maximum and minimum longitudinal velocities of vehicle $i \in I$ ; $\nu _ { \mathrm { m a x } , i }$ is the maximum velocity of the vehicle. 

$$
\sum_ {t ^ {*} = t - 4} ^ {t} \alpha_ {i} ^ {t ^ {*}} + \beta_ {i} ^ {t ^ {*}} \leq 1 \tag {A12}
$$

Eqs. (A13) and (A14) ensure that $\nu _ { y , i } ^ { t }$ and $a _ { y , i } ^ { t }$ are 0 for vehicle i when not changing lanes. 

$$
- M \sum_ {t ^ {*} = t - 4} ^ {t} \alpha_ {i} ^ {t ^ {*}} + \beta_ {i} ^ {t ^ {*}} \leq v _ {y, i} ^ {t} \leq M \sum_ {t ^ {*} = t - 4} ^ {t} \alpha_ {i} ^ {t ^ {*}} + \beta_ {i} ^ {t ^ {*}} \tag {A13}
$$

$$
- M \sum_ {t ^ {*} = t - 4} ^ {t} \alpha_ {i} ^ {t ^ {*}} + \beta_ {i} ^ {t ^ {*}} \leq \alpha_ {y, i} ^ {t} \leq M \sum_ {t ^ {*} = t - 4} ^ {t} \alpha_ {i} ^ {t ^ {*}} + \beta_ {i} ^ {t ^ {*}} \tag {A14}
$$

Eq. (A15) ensures that vehicle i changes into the centreline of the target lane within 4 s. 

$$
y _ {i} ^ {t} - \alpha_ {i} ^ {t} w + \beta_ {i} ^ {t} w - (1 - \alpha_ {i} ^ {t} - \beta_ {i} ^ {t}) M \leq y _ {i} ^ {t + 4} \leq y _ {i} ^ {t} - \alpha_ {i} ^ {t} w + \beta_ {i} ^ {t} w + (1 - \alpha_ {i} ^ {t} - \beta_ {i} ^ {t}) M \tag {A15}
$$

Eqs. (A16) and (A17) update the vehicle i based on the lane at time t and lane changing decision variables $\alpha$ and $\beta .$ . Eq. (A16) immediately updates the CAV lane $\boldsymbol { s } _ { i } ^ { t }$ after taking the decision to start the lane change. On the other hand, Eq. (A17) updates the CAV’s lane $o _ { i } ^ { t }$ with a lag of 4 s. The purpose of these two constraints is to avoid collisions between the CAV and vehicles in the current lane and the target lane. 

$$
s _ {i} ^ {t + 1} = s _ {i} ^ {t} + \alpha_ {i} ^ {t} - \beta_ {i} ^ {t} \tag {A16}
$$

$$
o _ {i} ^ {t + 1} = o _ {i} ^ {t} + \alpha_ {i} ^ {t - 4} - \beta_ {i} ^ {t - 4} \tag {A17}
$$

Eqs. (A18) and (A19) are collision avoidance constraints. 

$$
\left| \boldsymbol {x} _ {i} ^ {t} - \hat {\boldsymbol {x}} _ {j} ^ {t} \right| + \left| \boldsymbol {y} _ {i} ^ {t} - \hat {\boldsymbol {y}} _ {j} ^ {t} \right| + M \left| \boldsymbol {s} _ {i} ^ {t} - \hat {\boldsymbol {s}} _ {j} ^ {t} \right| \geq l _ {j} + s _ {0, j} \tag {A18}
$$

$$
\left| x _ {i} ^ {t} - \hat {x} _ {j} ^ {t} \right| + \left| y _ {i} ^ {t} - \hat {y} _ {j} ^ {t} \right| + M \left| o _ {i} ^ {t} - \hat {o} _ {j} ^ {t} \right| \geq l _ {j} + s _ {0, j} \tag {A19}
$$

where $s _ { 0 , j }$ is the desired headway of the front vehicle j. 

$$
s _ {i} ^ {t} \leq s _ {\text {r a m p}} - 1 + M p _ {i} ^ {t}
$$

$$
p _ {i} ^ {t} = \left\{ \begin{array}{l l} 1 & \text {i f} x _ {i} ^ {t} \leq L _ {s a} + L _ {m a} \\ 0 & \text {e l s e} \end{array} \right. \tag {A20}
$$

where $p _ { i } ^ { t }$ is an auxiliary variable and $s _ { r a m p }$ is the defined ramp lane value. 

Limitations are imposed on the change in lanes between mainline and ramp vehicles, with lane constraints established according to Eq. (A21). 

$$
s _ {\min , i} ^ {t} <   s _ {i} ^ {t} <   s _ {\max , i} ^ {t} \tag {A21}
$$

The experiments were conducted in a merging zone with a length of ${ 3 0 0 } \mathrm { m }$ and a width of $2 1 ~ \mathrm { \ m }$ . The bottom lane is the ramp. The experiment included a total of 20 vehicles in 30 s. The cooperative lane changing trajectories of the four CAVs are shown in Fig. A1. Under the influence of the BDM-AWM, the CAVs are able to change lanes cooperatively to achieve system optimization without collision risk. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/eb4923f18d6eff3a70a16d6744eaf50f2c286bd40d988ea38f6826eb31e5c6bf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/e60e82adee63f00753e2b4772c44992d686c32f77d5a43092720ed0502a2cdef.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/e1a4074b7761baeb8e3d0e7d0f86c2f6432e3d23c57f31f709690d0e32058cab.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/4b239cc94dd9eb2fde78c11247e9a835c075235d2a7b1d0af36d4e0b58454e87.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/f7f4c43c-21d4-48e0-ba15-c46aaf369a79/35a4c0ad55f97ecc6d3ca05fdedab6a513b92eb2098e3c89daa3d248750b18d7.jpg)



Fig. A1. CAV coordinated lane change trajectory


Table A1 shows the TTT and TIT for different control scenarios. From the table, it can be seen that the optimization effect of the BDM-AWM on efficiency is affected by the increase in constraints when the lane-changing trajectory is considered, but there is still a significant improvement relative to the NC scenario. In addition, the collision risk of the vehicle is slightly reduced without considering the lane-changing trajectories. 


Table A1 Transportation efficiency and safety indicators in different scenarios.


<table><tr><td>Control scenarios</td><td>TTT (s)</td><td>TIT (s)</td></tr><tr><td>BDM-AWM (Considering lane change trajectories)</td><td>264.4</td><td>2.17</td></tr><tr><td>BDM-AWM (Disregarding lane change trajectories)</td><td>266.1</td><td>2.09</td></tr><tr><td>NC (Disregarding lane change trajectories)</td><td>281.7</td><td>2.21</td></tr></table>

# Appendix B. Supplementary material

Supplementary data to this article can be found online at https://doi.org/10.1016/j.trc.2025.105298. 

# References



Bushnell, D., 1970. A merging control system for the urban freeway. IEEE Trans. Veh. Technol. 19 (1), 107–120. https://doi.org/10.1109/T-VT.1970.23438. 





Balas, V.E., Balas, M.M., 2006. Driver assisting by inverse time to collision. World Automation Congress 2006, 942–947. https://doi.org/10.1109/WAC.2006.376059. 





Bai, H., Guo, C., Ding, H., Wei, L., Sun, T., Chen, X., 2023. Modeling differential car-following behaviour under normal and rainy conditions: a memory-based deep learning method with an attention mechanism. Chin. Phys. B 32, 060507. https://doi.org/10.1088/1674-1056/acaa2f. 





Bando, M., Hasebe, K., Nakanishi, K., Nakayama, A., Shibata, A., Sugiyama, Y., 1995. Phenomenological study of dynamical model of traffic flow. J. Phys. I 5 (11), 1389–1399. https://doi.org/10.1051/jp1:1995206. 





Chen, N., Arem, B., Alkim, T., Wang, M., 2021a. A hierarchical model-based optimization control approach for cooperative merging by connected automated vehicles. IEEE Trans. Intell. Transport. Syst. 22 (12), 7712–7725. https://doi.org/10.1109/TITS.2020.3007647. 





Chen, M., Du, L., Zhao, X., 2021b. Event triggered rolling horizon based systematical trajectory planning for merging platoons at mainline-ramp intersection. Transp. Res. Part C Emerging Technol. 125, 103006. https://doi.org/10.1016/j.trc.2021.103006. 





Chen, T., Wang, M., Gong, S., Zhou, Y., Ran, B., 2021c. Connected and automated vehicle distributed control for on-ramp merging scenario: a virtual rotation approach. IEEE Trans. Intell. Transport. Syst 133, 103451. https://doi.org/10.1016/j.trc.2021.103451. 





Chen, D., Ahn, S., 2018. Capacity-drop at extended bottlenecks: merge, diverge, and weave. Transp. Res. B Methodol. 108, 1–20. https://doi.org/10.1016/j. trb.2017.12.006. 





Chen, C., Wu, B., Xuan, L., Chen, J., Qian, L., 2022. A discrete control method for the unsignalized intersection based on cooperative grouping. IEEE Trans. Veh. Technol. 71 (1), 123–136. https://doi.org/10.1109/TVT.2021.3128390. 





Chen, X., Zhang, W., Bai, H., Xu, C., Ding, H., Huang, W., 2023. Two-dimensional following lane-changing (2DF-LC): a framework for dynamic decision-making and rapid behavior Planning. IEEE Trans. Intell. Veh. https://doi.org/10.1109/TIV.2023.3324305. 





Ding, H., Di, Y., Zheng, X., Bai, H., Zhang, W.H., 2021. Automated cooperative control of multilane freeway merging areas in connected and autonomous vehicle environments. Transportmetr. B: Transport Dynam. 9 (1), 437–455. https://doi.org/10.1080/21680566.2021.1887774. 





Ding, H., Pan, H., Bai, H., Zheng, X., Chen, J., Zhang, W., 2022. Driving strategy of connected and autonomous vehicles based on multiple preceding vehicles state estimation in mixed vehicular traffic. Physica A 596, 127154. https://doi.org/10.1016/j.physa.2022.127154. 





Ding, H., Zhang, L., Chen, J., Zheng, X., Pan, H., Zhang, W., 2023. MPC-based dynamic speed control of CAVs in multiple sections upstream of the bottleneck area within a mixed vehicular environment. Physica A 613, 128542. https://doi.org/10.1016/j.physa.2023.128542. 





Deb, K., Pratap, A., Agarwal, S., Meyarivan, T., 2002. A fast and elitist multi-objective genetic algorithm: NSGA-II. IEEE Trans. Evol. Comput. 6 (1), 182–197. https:// doi.org/10.1109/4235.996017. 





Frejo, J.R.D., Camacho, E.F., 2012. Global versus local MPC algorithms in freeway traffic control with ramp metering and variable speed limits. IEEE Trans. Intell. Transport. Syst 13 (4), 1556–1565. https://doi.org/10.1109/TITS.2012.2195493. 





Hu, Y., Wang, Y., Guo, J., Zhang, L., Lu, Q., Liu, H., Li, Y., 2024. Eco-driving of connected autonomous vehicles in urban traffic networks of mixed autonomy with cutin and escape lane-changes of manually-driven vehicles. Transp. Res. Part C Emerging Technol. 169, 104889. https://doi.org/10.1016/j.trc.2024.104889. 





Jing, S., Hui, F., Zhao, X., Rios-Torres, J., Khattak, A.J., 2019. Cooperative game approach to optimal merging sequence and on-ramp merging control of connected and automated vehicles. IEEE Trans. Intell. Transport. Syst. 20 (11), 4234–4244. https://doi.org/10.1109/TITS.2019.2925871. 





Kong, D., Sun, L., Xu, Y., 2021. Modeling cars and trucks in the heterogeneous traffic based on car–truck combination effect using cellular automata. Physica A 562, 125329. https://doi.org/10.1016/j.physa.2020.125329. 





Karimi, M., Roncoli, C., Alecsandru, C., Papageorgiou, M., 2020. Cooperative merging control via trajectory optimization in mixed vehicular traffic. Transp. Res. Part C Emerging Technol. 116, 102663. https://doi.org/10.1016/j.trc.2020.102663. 





Kesting, A., Treiber, M., Helbing, D., 2007. General lane-changing model MOBIL for car-following models. Transp. Res. Rec. 1999 (1), 86–94. https://doi.org/ 10.3141/1999-10. 





Laval, J., Daganzo, C., 2006. Lane-changing in traffic streams. Transp. Res. B Methodol. 40 (3), 251–264. https://doi.org/10.1016/j.trb.2005.04.003. 





Li, P.T., Zhou, X., 2017. Recasting and optimizing intersection automation as a connected-and-automated-vehicle (CAV) scheduling problem: a sequential branch-andbound search approach in phase-time-traffic hypernetwork. Transp. Res. B Methodol. 105, 479–506. https://doi.org/10.1016/j.trb.2017.09.020. 





Li, Y., Tang, C., Li, K., He, X., Peeta, S., Wang, Y., 2018. Consensus-based cooperative control for multi-platoon under the connected vehicles environment. IEEE Trans. Intell. Transport. Syst 20, 2220–2229. https://doi.org/10.1109/TITS.2018.2865575. 





Li, P., Abdel-Aty, M., 2022. Real-time crash likelihood prediction using temporal attention–based deep learning and trajectory fusion. J. Transport. Eng., Part A Syst. 148 (7), 04022043. https://doi.org/10.1061/JTEPBS.0000697. 





Li, D., Zhu, F., Chen, T., Wong, Y., Zhu, C., Wu, J., 2023. COOR-PLT: a hierarchical control model for coordinating adaptive platoons of connected and autonomous vehicles at signal-free intersections based on deep reinforcement learning. Transp. Res. Part C Emerging Technol. 146, 103933. https://doi.org/10.1016/j. trc.2022.103933. 





Liu, H., Zhuang, W., Yin, G., Li, Z., Cao, D., 2023. Safety-critical and flexible cooperative on-ramp merging control of connected and automated vehicles in mixed traffic. IEEE Trans. Intell. Transp. Syst. 24 (3), 2920–2934. https://doi.org/10.1109/TITS.2022.3224592. 





Liu, L., Zhu, L., Yang, D., 2016. Modeling and simulation of the car-truck heterogeneous traffic flow based on a nonlinear car-following model. Appl. Math Comput. 273, 706–711. https://doi.org/10.1016/j.amc.2015.10.032. 





Ma, W., He, Z., Wang, L., Abdel-Aty, M., Yu, C., 2021. Active traffic management strategies for expressways based on crash risk prediction of moving vehicle groups. Accid. Anal. Prev. 163, 106421. https://doi.org/10.1016/j.aap.2021.106421. 





Marler, R., Arora, J., 2004. Survey of multi-objective optimization methods for engineering. Struct. Multidisc. Optim. 26, 369–395. https://doi.org/10.1007/s00158- 003-0368-6. 





Mohanty, S., Pozdnukhov, A., Cassidy, M., 2020. Region-wide congestion prediction and control using deep learning. Transp. Res. Part C Emerging Technol. 116, 102624. https://doi.org/10.1016/j.trc.2020.102624. 





Mu, C., Du, L., Zhao, X., 2021. Event triggered rolling horizon based systematical trajectory planning for merging platoons at mainline-ramp intersection. Transp. Res. Part C Emerging Technol. 125, 103006. https://doi.org/10.1016/j.trc.2021.103006. 





Mirheli, A., Tajalli, M., Hajibabai, L., Hajbabaie, A., 2019. A consensus-based distributed trajectory control in a signal-free intersection. Transp. Res. Part C Emerging Technol. 100, 161–176. https://doi.org/10.1016/j.trc.2019.01.004. 





Ni, D., Wang, H., 2008. Trajectory reconstruction for travel time estimation. J. Intell. Transp. Syst. 12 (3), 113–125. https://doi.org/10.1080/15472450802262307. 





Peeta, S., Zhang, P., Zhou, W., 2005. Behavior-based analysis of freeway car–truck interactions and related mitigation strategies. Transp. Res. B Methodol. 39 (5), 417–451. https://doi.org/10.1016/j.trb.2004.06.002. 





Rios-Torres, J., Malikopoulos, A.A., 2017. Automated and Cooperative Vehicle Merging at Mainline On-Ramps. IEEE Trans. Intell. Transport. Syst. 18 (4), 780–789. https://doi.org/10.1109/TITS.2016.2587582. 





Rahman, M., Abdel-aty, M., 2018. Longitudinal safety evaluation of connected vehicles’ platooning on expressways. Accid. Anal. Prev. 117, 381–391. https://doi.org/ 10.1016/j.aap.2017.12.012. 





Schmitt, M., Ramesh, C., Lygeros, J., 2017. Sufficient optimality conditions for distributed, non-predictive ramp metering in the monotonic cell transmission model. Transp. Res. B Methodol. 105, 401–422. https://doi.org/10.1016/j.trb.2017.10.001. 





Sun, Y., Ge, H., Cheng, R., 2018. An extended car-following model under V2V communication environment and its delayed-feedback control. Physica A 508, 349–358. https://doi.org/10.1016/j.physa.2018.05.102. 





Tang, Z., Zhu, H., Zhang, X., Iryo-Asano, M., Nakamura, H., 2022. A novel hierarchical cooperative merging control model of connected and automated vehicles featuring flexible merging positions in system optimization. Transp. Res. Part C Emerging Technol. 238, 103650. https://doi.org/10.1016/j.trc.2022.103650. 





Typaldos, P., Papageorgiou, M., 2023. Modified dynamic programming algorithms for GLOSA systems with stochastic signal switching times. Transp. Res. Part C Emerging Technol. 157, 104364. https://doi.org/10.1016/j.trc.2023.104364. 





Tajalli, M., Niroumand, R., Hajbabaie, A., 2022. Distributed cooperative trajectory and lane changing optimization of connected automated vehicles: freeway segments with lane drop. Transp. Res. Part C Emerging Technol. 143, 103761. https://doi.org/10.1016/j.trc.2022.103761. 





Thiemann, C., Treiber, M., Kesting, A., 2008. Estimating acceleration and lane-changing dynamics from next generation simulation trajectory data. Transport. Res. Record: J. Transport. Res. Board 2088, 90–101. https://doi.org/10.3141/2088-10. 





Uno, A., Sakaguchi, T., Tsugawa, S., 1999. A merging control algorithm based on inter-vehicle communication. In: Proceedings 199 IEEE/IEEJ/JSAI International Conference on Intelligent Transportation Systems, pp. 783–787. https://doi.org/10.1109/ITSC.1999.821160. 





Verma, S., Pant, M., Snasel, V., 2021. A comprehensive review on NSGA-II for multi-objective combinatorial optimization problems. IEEE Access 9, 57757–57791. https://doi.org/10.1109/ACCESS.2021.3070634. 





Vollrath, M., Schleicher, S., Gelau, C., 2011. The influence of cruise control and adaptive cruise control and driving behavior: a driving simulator study. Accid. Anal. Prev. 43 (3), 1134–1139. https://doi.org/10.1016/j.aap.2010.12.023. 





Wang, J., Lian, Y., Jiang, Y., Xu, Q., Li, K., Jones, C.N., 2023a. Distributed data-driven predictive control for cooperatively smoothing mixed traffic flow. Transp. Res. Part C Emerging Technol. 155, 104274. https://doi.org/10.1016/j.trc.2023.104274. 





Wang, Y., Lin, S., Wang, Y., Schutter, B., 2023b. Robustness analysis of platoon control for mixed types of vehicles. IEEE Trans. Intell. Transport. Syst. 24 (1), 331–340. https://doi.org/10.1109/TITS.2022.3213413. 





Windeatt, T., Ghaderi, R., 1998. Dynamic weighting factors for decision combining. Proceedings of International Conference on Data Fusion 123–130. 





Xu, H., Zhang, Y., Li, L., Li, W.X., 2020. Cooperative driving at unsignalized intersections using tree search. IEEE Trans. Intell. Transport. Syst. 21 (11), 4563–4571. https://doi.org/10.1109/TITS.2019.2940641. 





Yang, D., Jin, P., Pu, Y., Ran, B., 2014. Stability analysis of the mixed traffic flow of cars and trucks using heterogeneous optimal velocity car-following model. Physica A 395, 371–383. https://doi.org/10.1016/j.physa.2013.10.017. 





Ye, F., Zhang, Y., 2009. Vehicle type-specific headway analysis using freeway traffic data. Transport. Res. Record J. Transport. Res. Board 2124, 222–230. https://doi. org/10.3141/2124-22. 





Yu, H., Zhang, L., Zhang, M., Jin, F., Wang, Y., 2024. Coordinated Ramp Metering considering the Dynamics of Mixed-Autonomy Traffic. Sustainability 16, 10055. https://doi.org/10.3390/su162210055. 





Zhou, Q., Zhou, B., Hu, S., Roncoli, C., Wang, Y., Hu, J., Lu, G., 2023. A safety-enhanced eco-driving strategy for connected and autonomous vehicles: a hierarchical and distributed framework. Transp. Res. Part C Emerging Technol. 156, 104320. https://doi.org/10.1016/j.trc.2023.104320. 





Zhou, Y., Chung, E., Bhaskar, A., Cholette, M.E., 2019. A state-constrained optimal control based trajectory planning strategy for cooperative freeway mainline facilitating and on-ramp merging maneuvers under congested traffic. Transp. Res. Part C Emerging Technol. 109, 321–342. https://doi.org/10.1016/j. trc.2019.10.017. 





Zhou, M., Qu, X., Jin, S., 2017. On the impact of cooperative autonomous vehicles in improving freeway merging: a modified intelligent driver model-based approach. IEEE Trans. Intell. Transport. Syst. 18 (6), 1422–1428. https://doi.org/10.1109/TITS.2016.2606492. 





Zhang, P., Zhu, H., Zhou, Y., 2022. Modeling cooperative driving strategies of automated vehicles considering trucks’ behavior. Physica A 585, 126386. https://doi. org/10.1016/j.physa.2021.126386. 





Zhang, G., Zuo, H., 2013. Solution analysis of multi-objective programming problem. International Conference on Machine Learning and Cybernetics 2013, 1039–1044. https://doi.org/10.1109/ICMLC.2013.6890749. 





Zhang, K., Li, L., 2022. Explainable multimodal trajectory prediction using attention models. Transp. Res. Part C Emerging Technol. 143, 103829. https://doi.org/ 10.1016/j.trc.2022.103829. 

