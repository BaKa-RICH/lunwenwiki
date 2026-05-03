RESEARCH 

# Hierarchical cooperative constrained control for multi-lane merging process under mixed traffic scenario

Xiaoyu Liu $\cdot$ Min Zhao $\cdot$ Liuping Wang · Dihua Sun 

Received: 7 September 2024 / Accepted: 20 March 2025 / Published online: 15 April 2025 $^ ©$ The Author(s), under exclusive licence to Springer Nature B.V. 2025 

Abstract The merging problems are widely recognized as one of the major reasons for the significant degeneration of traffic efficiency. All the vehicles’ interests involved in the merging process should be appropriately guaranteed. How to utilize all the multilane road spaces to merge with the premise of all vehicles’ interests remains open to discussion. Fortunately, using connected and autonomous vehicles (CAVs) is a powerful tool for creating control nodes to complete cooperative merging maneuvers and balance the interests of all vehicles. Hence, this paper proposes a hierarchical cooperative merging constrained control (HCMCC) algorithm-based decentralized framework under the mixed traffic scenario. The multi-lane merging problem is solved in the Tactical layer using a Mixed Integer Linear Programming (MILP) optimization model, which computes the programmed trajec-

X. Liu $\cdot$ M. Zhao $\cdot$ D. Sun Key Laboratory of Dependable Service Computing in Cyber-Physical Society of Ministry of Education, Chongqing University, Chongqing 400044, China e-mail: xyu524@163.com 

D. Sun e-mail: d3sun@163.com 

X. Liu $\cdot$ M. Zhao $\left( \boxtimes \right.$ ) D. Sun College of Automation, Chongqing University, Chongqing 400044, China e-mail: min992215@163.com 

L. Wang Royal Melbourne Institute of Technology (RMIT), School of Engineering, Melbourne, VIC 3000, Australia e-mail: liuping.wang@rmit.edu.au 

tories of the CAVs involved. The Laguerre-functionbased Continuous-time Model Predictive Control with the Prescribed-Time Observer (LCMPC-PTO) is built into the Operational layer to execute the computed trajectories. The entire system can be optimized to regenerate the trajectories when an emergency occurs due to unexpected behaviors from human-driven vehicles (HVs). Numerical studies in a realistic traffic simulation environment show that the congestion caused by the multi-lane merging problem is improved along with the reduction of the average travel time and the increment of the actual traffic flow. 

Keywords Mixed traffic scenario $\cdot$ CAV longitudinal trajectory optimization $\cdot$ Lane-change behavior Merging problem $\cdot$ Model predictive control 

# List of symbols

<table><tr><td>M</td><td>A sufficiently large number</td></tr><tr><td>Δt</td><td>The size of a time step</td></tr><tr><td>Φ</td><td>All vehicles within the Control Area</td></tr><tr><td>ΦA(t)</td><td>All CAVs within the Control Area at timet</td></tr><tr><td>ΦH(t)</td><td>All HVs within the Control Area at timet</td></tr><tr><td>Θt i</td><td>The future trajectories data of surround-ing vehicles of CAV i at timet</td></tr><tr><td>G t i</td><td>All the feasible lane-change spaces amongdata set Θt i</td></tr></table>

h The length of the data set construction stage in time steps 

$p ( i , t )$ The position of vehicle i at time t 

$v ( i , t )$ The velocity of vehicle i at time t 

$a ( i , t )$ The acceleration of vehicle i at time $t$ 

$\dot { a } ( i , t )$ The jerk of vehicle i at time t 

$a _ { i }$ The longitudinal acceleration profile of vehicle i 

$k _ { i } ( t )$ The lane occupation of vehicle $i$ at time t 

$k _ { i }$ The lateral lane-occupation sequence of vehicle i 

$l c _ { p }$ lcp The safety lane-change distance between CAV $i$ and its preceding vehicle 

$l c _ { f }$ The safety lane-change distance between CAV i and its following vehicle 

$t _ { 0 } ^ { i }$ The time of CAV i entering the Control Area 

$t _ { a r r i v a l } ^ { i }$ The time of CAV i leaving the Control Area 

$t _ { l e a v } ^ { i }$ The time of CAV i leaving the Merging Area 

$g _ { l } ( i , t )$ The lane-change space of CAV i in the adjacent lane on the left at time t 

gr (i, t ) The lane-change space of CAV i in the adjacent lane on the right at time t 

ωlp(i, t ) The preceding vehicle of CAV i in the adjacent lane on the left at time t 

ωl f (i, t ) The following vehicle of CAV i in the adjacent lane on the left at time t 

ωr p(i, t ) The preceding vehicle of CAV i in the adjacent lane on the right at time t 

ωr f (i, t ) The following vehicle of CAV i in the adjacent lane on the right at time t 

ω p(i, t ) The preceding vehicle of CAV i in the same lane at time t 

ω f (i, t ) The following vehicle of CAV i in the same lane at time t 

iA(t ) The preceding CAVs set of CAV i at time t 

iH (t ) The preceding HVs set of CAV i at time t 

iF (t ) The following vehicles set of CAV $i$ at time t 

$\Phi _ { W V } ^ { i } ( t )$ Vehicles that cannot complete merging $C _ { W V } ^ { m a x }$ The number of these vehicles that can b released to complete the merging 

$I _ { 0 } , I _ { 1 } , I _ { 2 }$ Unplanned CAVs in each lane within the Organizing Area 

it (n, j ) The number of vehicles in Lane $n$ , $j =$ $t , t + \Delta t , . . . t + h \times \Delta t$ 

κi ( j ) An auxiliary variable to indicate whether CAV i located at the assigned area, $j =$ $t , t + \Delta t , . . . t + h \times \Delta t$ 

$\theta _ { \omega } ( j )$ An auxiliary variable to indicate whether CAV $\omega$ located at the Merging Area, $\omega \in$ $I _ { 0 } \cup I _ { 1 } \cup I _ { 2 }$ $I _ { 0 } \cup I _ { 1 } \cup I _ { 2 } , j = t , t + \Delta t , \dotsc t + h \times \Delta t$ 

$\gamma ( j )$ An auxiliary variable to indicate whether the cooperative merging is completed, $j = t , t + \Delta t , . . . t + h \times \Delta t$ 

$\alpha ( j )$ An auxiliary variable to indicate the moment when spaces that vehicles in $\Phi _ { W V } ^ { i } ( t )$ need to complete merging are created, $j = t , t + \Delta t , . . . t + h \times \Delta t$ 

$\beta ( j )$ An auxiliary variable to indicate the moment when the cooperative merging is completed, $j = t , t + \Delta t , . . . t + h \times \Delta t$ 

$\chi ( j )$ An auxiliary variable to indicate whether the cut-in is completed, $\begin{array} { r l r } { \mathrm { ~  ~ \omega ~ } _ { j } } & { { } = } & { t , t + } \end{array}$ $\Delta t , \ldots t + h \times \Delta t$ 

( j ) An auxiliary variable to indicate the moment when the cut-in is completed, $j = t , t + \Delta t , . . . t + h \times \Delta t$ 

alower The maximum deceleration rates 

aupper The maximum acceleration rates 

j er klower The minimum jerk 

j er kupper The maximum jerk 

vupper The maximum velocity limit within the Control Area 

$t _ { h }$ The time headway 

$s _ { 0 }$ The minimum safety distance 

$l _ { 0 }$ The length of vehicle 

mi $m _ { i }$ The mass of vehicle 

$A _ { i }$ The vehicle cross-section area 

$\rho$ The air density 

$C _ { d , i }$ The drag coefficient 

$\tau _ { i }$ The inertial delay 

g The gravity acceleration 

$\mu _ { i }$ The coefficient of rolling resistance 

$\lambda$ The road slope 

$\upsilon ( i , t )$ The external disturbances 

$\iota _ { i }$ The first derivative upper bound of the external disturbances 

$u ( i , t )$ The control signal of the vehicle dynamic model 

$T$ The settling time of PTO 

$\boldsymbol { \kappa } _ { i , 1 } , \boldsymbol { \kappa } _ { i , 2 } , \boldsymbol { \kappa } _ { i , 3 }$ Parameters of PTO 

$e ( i , t )$ The state vector of the error system 

<table><tr><td>y(i,t)</td><td>The output of the error system</td></tr><tr><td>ζ(i,t)</td><td>The control signal of the extended error system</td></tr><tr><td>ζ(i,t)</td><td>The state vector of the extended error system</td></tr><tr><td>Ω(i,t)</td><td>The output of the extended error system</td></tr><tr><td>p</td><td>The Laguerre pole</td></tr><tr><td>N</td><td>The number of functions that the Laguerre network used</td></tr><tr><td>L(t)</td><td>The Laguerre function</td></tr><tr><td>η</td><td>A parameter vector</td></tr><tr><td>lpm</td><td>The length of the Pre-Merging Area</td></tr><tr><td>loa</td><td>The length of the Organizing Area</td></tr><tr><td>lpa</td><td>The length of the Preparing Area</td></tr><tr><td>lma</td><td>The length of the Merging Area</td></tr><tr><td>lvr</td><td>The length of the Velocity Regulating Area</td></tr><tr><td>tterminal</td><td>The time when CAV i meets the modified terminal condition</td></tr><tr><td>tradundant</td><td>The redundant time</td></tr></table>

# 1 Introduction

The merging problems are widely recognized as one of the major reasons for the significant degeneration of traffic efficiency. Intensive interactions among vehicles in such a section can result in traffic congestion and accidents [1,2]. Meanwhile, the merging area may be coupled with other traffic bottlenecks (e.g., traffic signals or tunnels) to create more complex traffic problems. However, with the development of communication, sensing, and control technologies, the introduction of connected and autonomous vehicles (CAVs) will have a positive effect on the overall safety performance of the traffic flow [3], which has the potential to alleviate congestion within the merging areas [4] and enhance merging efficiency and safety [5]. 

In recent years, considerable research has been devoted to merging algorithms for pure CAV traffic with objectives such as minimizing fuel consumption and travel time or improving traffic safety and efficiency [6–13]. However, these studies are developed for the case of a single main lane with a single merging lane, which does not consider lane-change behaviors for vehicles at the main lane. In the multi-lane merging scenario, vehicles at the main lane could adopt lane-change behaviors or keep their longitudinal movement. Algorithms that only allow vehicles to keep lon-

gitudinal movement in their original lane cannot fully utilize the capacity of the other lanes, thereby reducing merging efficiency. Recently, researchers have proposed cooperative merging algorithms for multi-lane merging scenarios to increase throughput and reduce fuel consumption, delays, or travel times [14–18]. It is believed that in the near future, the transportation system will inevitably experience a mixed traffic state where human-driven vehicles (HVs) and CAVs coexist. Thus, it is of great significance to investigate merging algorithms under the mixed traffic scenario. 

The major challenging issue related to the merging problem under the mixed traffic scenario is the lack of adequate modeling and control framework. Limited studies have investigated merging algorithms under the mixed traffic scenario. Wei et al. [19] developed a merging decision model that considers the interaction between the merging vehicle and the following vehicle at the main lane. Mu et al. [20] proposed an event-triggered rolling horizon-based systematical trajectory planning, which expects to safely and smoothly merge two platoons (pure or mixed CAV). It is noted that the hierarchical algorithm frameworks are widely employed by researchers for the merging problem under the mixed traffic scenario [21–24]. In particular, a hierarchical model for cooperative merging control is proposed by Hou et al. [25], which focuses on the multi-lane merging problem under the mixed traffic scenario that is more valuable than those research results about the single-lane merging problems [19– 24]. However, all the HVs in the model of Hou et al. [25] are assumed to be willing to perform cooperative merging maneuvers, which lack realism under the mixed traffic scenario. Moreover, one cannot guarantee that CAVs always exist at the main lane to perform the cooperative merging maneuvers, especially under low penetration rate conditions with the precondition of poor cooperative characteristics of HVs. Hence, there is a need to utilize not only the capacity of the inner lanes but also the CAVs at the inner lanes to complete the cooperative merging maneuvers and balance the interests of all vehicles. How to fully fulfill the advances of CAV technology for the multi-lane merging problem remains open to discussions under the mixed traffic scenario. 

In the frameworks of the existing hierarchical algorithm for the merging problem, conventional model predictive control is commonly used as the operational layer controller to ensure the completion of the coop-

erative merging maneuvers [9,10,25–28]. It is robust against model uncertainty and disturbance. For conventional model predictive control, the horizon window is determined by the prediction and control horizon. Precise control often requires a large prediction horizon and a control horizon. However, limited computational resources make using a vaguely large horizon window impossible. Therefore, Laguerre-functionbased Model Predictive Control (LMPC) has been proposed to overcome the above weakness. The LMPC had the characteristic that it could drastically reduce the number of optimization variables. These LMPC characteristics have advantages when using a large horizon with limited computational resources, and research on LMPC has begun in various fields [29–33]. It is feasible to integrate the LMPC into the hierarchical frameworks for the merging problem instead of conventional model predictive control, which advances real-world practice. 

Realizing the above research gaps, this paper proposes a hierarchical cooperative merging constrained control (HCMCC) model-based decentralized framework to complete the cooperative merging for the multilane merging problem under the mixed traffic scenario. The multi-lane merging problem is solved in the Tactical layer using a Mixed Integer Linear Programming (MILP) optimization model. The MILP model is used to ensure the high efficiency of problem-solving. Then, the programmed trajectories output from the Tactical layer are executed in the Operational layer. The nonlinear dynamic model subject to external disturbances is adapted in the Operational layer to fit the real-world practice. The Laguerre-function-based Continuous-time Model Predictive Control with the Prescribed-Time Observer (LCMPC-PTO) is built in the Operational layer, which not only addresses the influence of the external disturbances but fulfills the advance of the LMPC in the continuous-time under the precondition of limited computational resource. The entire framework possesses the capability of reprogramming trajectories to cope with the emergency raised by HVs who suffered from external disturbances. 

The main contributions of this paper include the following aspects. 

(1) CAVs at the inner lane are introduced into the proposed HCMCC model to complete the cooperative merging maneuvers if necessary. CAVs at the inner lane are permitted to either cut into the outer lane to complete the cooperative merging or provide 

assistance to create more spaces for the cooperative merging. Furthermore, a continuation cooperative utility model is integrated into the decentralized framework to relieve the traffic congestion of the merging area. The decentralized framework provides a new method to address the multi-lane merging problem under the mixed traffic scenario. 

(2) The heterogeneity of CAV and HV car-following behavior is taken into consideration in this paper. In the design, CAV’s car-following places emphasis on velocity consistency and achieves lower time headway with other CAVs in the constraints of the HCMCC model. This consequently releases the redundant road spaces for HVs. In comparison, the behavior of HV is captured by the IDM coupling with the conservative lane-change assumption, which occupies more road spaces than that of CAVs. Furthermore, the driving safety between CAV and HV is guaranteed through the constraints imposed in the HCMCC model. 

(3) The Prescribed-Time Observer (PTO) is integrated into the LCMPC to enhance the performance under the external disturbances. The LCMPC-PTO combines the characteristics of LMPC on limited computational resources for a large horizon with the estimation error convergence in the prescribed time. These techniques guarantee the algorithm application to real-time calculation. 

The remainder of this paper is organized as follows. Section 2 gives the problem description and the proposal of solutions. Section 3 formulates the Tactical Layer and the HCMCC model under the mixed traffic scenario. Section 4 builds the Operational Layer and the LCMPC-PTO. Section 5 designs the algorithm framework. Section 6 conducts numerical studies, degradation experiments, and sensitivity analyses. Finally, Sect. 7 delivers the conclusions. 

# 2 Problem description and overview of proposed solutions

# 2.1 Problem description

Figure 1 shows the details of a typical merging problem under the mixed traffic scenario. All vehicles are moving in the same direction. There is a Pre-Merging Area (the length is $l _ { p m . }$ ), a Merging Area (the length is $l _ { m a , \ l }$ ), and a Velocity Regulating Area (the length is $l _ { v r }$ ). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/ab069c1f3fdeb1ae9b35d15c327d3cba6df18412e3a855e03ebcc80ff38e122c.jpg)



Fig. 1 Typical merging problem under the mixed traffic scenario


The Cooperating Point is the point where the HCMCC model awakens. The Pre-Merging Area is divided into an Organizing Area (the length is $l _ { o a }$ ) and a Preparing Area (the length is $l _ { p a . }$ ) according to the position of the Cooperating Point. The Control Area includes all the areas mentioned above. An additional maximum velocity limit change is considered in this paper, which may be caused by traffic signals, variable velocity control, or tunnels. The maximum velocity limit changes at the end of the Control Area, for example, from $6 0 \mathrm { k m / h }$ dropping to $4 0 \mathrm { k m / h }$ . Following the velocity limit, CAVs and HVs coexist. 

# 2.2 Overview of proposed solutions

At time $t$ , let set $\Phi _ { A } ( t )$ denotes CAVs and set $\Phi _ { H } ( t )$ is HVs. Then set $\Phi = \{ \Phi ( t ) = \Phi _ { A } ( t ) \cup \Phi _ { H } ( t ) | t \geq 0 \}$ defines all vehicles within the Control Area. Each CAV within the Control Area collects states of other CAVs from V2X (including the programmed trajectories of other CAVs) and receives states of HVs from RSU (Road Side Unit). Hence, at time $t$ , the preceding CAVs set $\Phi _ { A } ^ { i } ( t )$ of CAV i, the preceding HVs set $\Phi _ { H } ^ { i } ( t )$ of CAV $i$ , and the following vehicles set (the following CAVs set $\Phi _ { F A } ^ { i } ( t )$ and the following HVs set $\Phi _ { F H } ^ { i } ( t ) ) \Phi _ { F } ^ { i } ( t ) = \dot { \Phi _ { F A } ^ { i } } ( t ) \cup \Phi _ { F H } ^ { i } ( t )$ are defined here, where $\Phi ( t ) = \Phi _ { A } ^ { i } ( t ) \cup \Phi _ { H } ^ { i } ( t ) \cup$ $\Phi _ { F } ^ { i } ( t ) \cup i$ . Together with the known car-following and lane-changing models, future trajectories of surrounding vehicles $( \Phi ( t ) \backslash \{ i \} )$ of CAV $i$ at time $t$ are built as a data set $\Theta _ { t } ^ { i }$ , which can be stored in the memory of CAV. Then, the Tactical Layer (Sect. 3) outputs the programmed trajectories using data set $\Theta _ { t } ^ { i }$ , and the Opera-

tional Layer (Sect. 4) executes them under time-varying traffic conditions. The dynamic model in the Operational layer is formulated based on the vehicle dynamic feature, and the proposed LCMPC-PTO is designed using the dynamic model to execute the programmed trajectories output by the Tactical layer (on the basis of the kinematic model). The relationship between these two models is shown in Fig. 2. 

# 3 Tactical layer

# 3.1 Definition of preconditions

Any CAV $i \in \Phi _ { A } ( t )$ can share the real-time state through vehicle-to-everything (V2X) without communication delay, including longitudinal position $p ( i , t )$ , longitudinal velocity $v ( i , t )$ , longitudinal acceleration $a ( i , t )$ and lane occupation $k _ { i } ( t ) ~ = ~ 0 , 1 , 2 , t ~ \in$ $[ t _ { 0 } ^ { i } , t _ { a r r i v a l } ^ { i } ] . t _ { 0 } ^ { i }$ and $t _ { a r r i v a l } ^ { i }$ are the time of CAV i entering and leaving the Control Area. 

The trajectories of CAVs can be decomposed into a lateral lane-occupation sequence $k _ { i }$ and a longitudinal acceleration profile $a _ { i } \ = \ \{ a ( i , t ) | t \ \in \ [ t _ { 0 } ^ { i } , t _ { a r r i v a l } ^ { i } ] \}$ . As shown in Fig. 3, CAV $i$ at time $t$ has two feasible lane-change spaces, $g _ { l } ( i , t ) ~ = ~ p ( \omega _ { l p } ( i , t ) , t ) ~ -$ $p ( \omega _ { l f } ( i , t ) , t )$ and $g _ { r } ( i , t ) = p ( \omega _ { r p } ( i , t ) , t ) - p ( \omega _ { r f }$ $( i , t ) , t ) . \omega _ { l p } ( i , t )$ and $\omega _ { l f } ( i , t )$ represents the preceding and following vehicle of CAV $i$ in the adjacent lane on the left at time t . $\omega _ { r p } ( i , t )$ and $\omega _ { r f } ( i , t )$ are vehicles of the same sense in the adjacent lane on the right. $\omega _ { p } ( i , t )$ and $\omega _ { f } ( i , t )$ are the preceding and following vehicles of CAV $i$ in the same lane. CAV i can perform lanechange behavior by taking feasible lane-change spaces 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/fb93097f7dbd6a198d1281ebb9f7fba457bdab8f277122bea774e23208c7dc6e.jpg)



Fig. 2 Block diagram of cascaded closed-loop solutions


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/9a435c24d8eb67dd36b752f81230f728f74c8d4cf454752041cef8d8fb4505fb.jpg)



Fig. 3 Definition of surrounding vehicles


at time t. Instant lane-changing behaviors are assumed for simplicity, the lane occupation $k _ { i } ( t )$ will change to the target lane number at time $t + \Delta t$ if any feasible lane-change spaces are taken at time t. $\Delta t$ is a constant time step size. Stay in the current lane is also permitted. The lateral lane-occupation sequence of CAV i can be defined as $k _ { i } = \{ k _ { i } ( t ) | t \in [ t _ { 0 } ^ { i } , t _ { a r r i v a l } ^ { i } ] \}$ . 

At time $t$ , once a new CAV $i$ arrives at the Cooperating Point and waits for the trajectory programming (which can be named as unplanned CAV), the HCMCC model awakens to organize all the CAVs within the Organizing Area (as shown in Fig. 2). CAV i collects states of other CAVs $( \Phi _ { A } ^ { i } ( t ) \cup \Phi _ { F A } ^ { i } ( t ) )$ from V2X (including the already programmed trajectories of other CAVs) and receives states of HVs from RSU. 

# 3.1.1 The conservative lane-change model for HVs

At the data set construction stage, the trajectories of surrounding $\mathrm { H V s } ( \Phi _ { H } ^ { i } ( t ) \cup \Phi _ { F H } ^ { i } ( t ) )$ are calculated with the aid of the IDM [34,35] car-following model and a conservative lane-change model (CLCM). Considering the uncontrollable feature of HVs and the driving purpose of vehicles within the Merging Area, we assume that the lane-change behaviors of HVs will be performed once the following conservative conditions (Eqs. (1) and (2)) are met. 

For $j \in \Phi _ { H } ^ { i } ( t ) \cup \Phi _ { F H } ^ { i } ( t )$ , the CLCM is as follows. 

$$
p (j, t) \leq p \left(\omega_ {l p} (j, t), t\right) - v (j, t) \times t _ {h} - s _ {0} - l _ {0}
$$

$$
- \frac {\left(\max \left(v (j , t) - v \left(\omega_ {l p} (j , t) , 0\right)\right) ^ {2} \right.}{2 \left| a _ {l o w e r} \right|} \tag {1}
$$

$$
\begin{array}{l} p (j, t) \geq p \left(\omega_ {l f} (j, t), t\right) + v \left(\omega_ {l f} (j, t), t\right) \times t _ {h} + s _ {0} \\ + l _ {0} + \frac {\left(\max \left(v \left(\omega_ {l f} (j , t) , t\right) - v (j , t) , 0\right)\right) ^ {2}}{2 \left| a _ {\text {l o w e r}} \right|} \tag {2} \\ \end{array}
$$

where $t _ { h }$ is the time headway, $a _ { l o w e r }$ is the maximum deceleration rates. $s _ { 0 }$ is the minimum safety distance. $l _ { 0 }$ is the length of vehicles. 

Besides, the lane-change behaviors of HVs from inner lanes to outer lanes are forbidden (e.g., from Lane 2 to Lane 1). This rule fits the actual driving habits of vehicles within the Merging Area since vehicles in outer lanes (Lane 1) suffer from the merging problem and usually have lower velocity than vehicles in inner lanes (Lane 2). The lane-change behaviors of HVs in Lane 0 are only permitted when entering the Merging Area. 

# 3.1.2 The feasible lane-change spaces for CAVs

At the data set construction stage, CAV i keeps driving on its current lane until the terminal condition is met. Meanwhile, other CAVs $( \Phi _ { A } ^ { i } ( t ) \cup \Phi _ { F A } ^ { i } ( t ) )$ move along with the already programmed trajectories, which serve in the proposed model’s safety constraints. All the trajectories are saved as data set $\Theta _ { t } ^ { i } = \{ \Theta _ { t } ^ { i } ( j ) | j =$ 

$t , t + \Delta t , \ldots t + h \times \Delta t \}$ and stored in the memory of CAV. This stage will end when CAV i meets the terminal condition and $h$ is the stage length in time steps. From data set $\Theta _ { t } ^ { i }$ , all the feasible lane-change spaces are recorded as $G _ { t } ^ { i } = \{ G _ { t } ( l , j ) = g _ { l } ( l , j ) \cup g _ { r } ( l , j ) | l \in$ $\Phi ( t ) , j = t , t + \Delta t , . . . t + h \times \Delta t \}$ $\Phi ( t )$ . The feasible lanechange spaces for CAVs are defined as follows. 

$$
p \left(\omega_ {l p} (i, j), j\right) - p (i, j) \geq l c _ {p}
$$

$$
p (i, j) - p \left(\omega_ {l f} (i, j), j\right) \geq l c _ {f} \tag {3}
$$

$$
p \left(\omega_ {r p} (i, j), j\right) - p (i, j) \geq l c _ {p}
$$

$$
p (i, j) - p \left(\omega_ {r f} (i, j), j\right) \geq l c _ {f} \tag {4}
$$

$l c _ { p }$ and $l c _ { f }$ are the safety lane-change distance between CAV i and its preceding (or the following) vehicles in the adjacent lane. In general, the safety lanechange distances should not be fixed but rather adjusted according to the vehicle’s velocity, and sometimes the velocity difference should be considered with the preceding (or the following) vehicles in the adjacent lane. However, to increase the feasibility of the HCMCC model, fixed values are taken at the data set construction stage, and detailed lane-change safety constraints are added in the exact modeling of longitudinal safety with lane-change behaviors (Sect. 3.2). 

# 3.1.3 Vehicle kinematics model

$$
p (i, j + \Delta t) = p (i, j) + (v (i, j + \Delta t) + v (i, j)) \times \frac {\Delta t}{2}
$$

$$
v (i, j + \Delta t) = v (i, j) + a (i, j) \times \Delta t
$$

$$
0 \leq v (i, j) \leq v _ {u p p e r} \tag {5}
$$

$$
a _ {l o w e r} \leq a (i, j) \leq a _ {u p p e r}
$$

$$
j e r k _ {l o w e r} \leq \dot {a} (i, j) \leq j e r k _ {u p p e r}
$$

where, $a _ { l o w e r }$ and $a _ { u p p e r }$ are the maximum deceleration and acceleration rates, jerklower and $j e r k _ { u p p e r }$ are the maximum and minimum jerk, respectively. vupper is the maximum velocity limit within the Control Area. 

# 3.2 The hierarchical cooperative merging constrained control model

# 3.2.1 Scenario description

As shown in Fig. 2, once an unplanned CAV arrives at the Cooperating Point, the HCMCC model is awakening to organize all the CAVs within the Organizing Area. Hence, there are several different combinations, 

as illustrated in Fig. 4, which are decided by the timevarying traffic conditions under the mixed traffic scenario. It is noted that all the combinations shown in Fig. 4 are just thumbnails, and the detail traffic conditions may be more complicated than the thumbnail (detail descriptions are as follows paragraph). 

Figure 4a–d shows that the unplanned CAV that arrives at the Cooperating Point is located at Lane 1, and the combinations are decided by whether there also exist unplanned CAVs in Lane 0 and Lane 2 within the Organizing Area. Figure 4e–h shows that the unplanned CAV that arrives at the Cooperating Point is located at Lane 0, and the combinations are decided by whether there also exist unplanned CAVs in Lane 1 and Lane 2 within the Organizing Area. The planned CAVs within the Organizing Area are omitted in these figures. From data set $\Theta _ { t } ^ { i }$ , one can obtain whether there exist vehicles that cannot complete merging and have to decelerate or even stop at the end of Lane 0 to wait for merging. Therefore, these vehicles can be defined as $\Phi _ { W V } ^ { i } ( t )$ . The number of these vehicles that can be released to complete the merging is chosen as $C _ { W V } = m i n ( C _ { W V } ^ { m a x }$ , lengt h(iW V (t))) where $C _ { W V } ^ { m a x }$ is chosen appropriately. 

Remark 1 Different from the existing model [25] for the multi-lane merging problem under the mixed traffic scenario, the HCMCC model in this paper is designed with additional consideration about the low penetration rate conditions of CAVs (as shown in Fig. 5). HVs in Lane 0 will decelerate or even stop at the end of Lane 0 because of the selfishness of HVs in Lane 1. Hence, the HCMCC model will create spaces by CAVs for these HVs to complete the merging. In other words, to balance the interests of all vehicles, it is necessary to sacrifice the interests of main lane vehicles appropriately. The CLCM used in this paper and $C _ { W V }$ defined above provide the applicability of the proposed model to the time-varying traffic conditions. 

# 3.2.2 The hierarchical cooperative merging constrained control model for CAVs in Lane 1 (HCMCC-L1)

In this subsection, the unplanned CAV i that arrives at the Cooperating Point is located at Lane 1. The objective is to check whether unplanned CAVs exist in Lanes 0 and 2, then create spaces for vehicles in $\Phi _ { W V } ^ { i } ( t )$ and minimize the travel time with the precondition 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/0b1230d4f336c075d60d97800644670dd68c91d699edb791c2e1f6be338b9d7a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/4a3fd775e02f5cc08ca5614fbb7855bed46851f254a0fbf2872b2164df352206.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/d41c76dd39289f6f013a58701172b3ea4af97a6b05e7565a1ae824ed305c2369.jpg)



(c）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/ee6d5477a43d8617f404f2b5c03c8134e6a2e79fe138ce3a64bc1fd242ca1213.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/6b8fed639d3676931ccb7e6b208c5124ceb407ca36f23b7c32756793bccb9b44.jpg)



（e)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/877a98892427fab8b74cea7e7953dd0ad1900dcf54a6d32d3f737c52bbcf1947.jpg)



(f)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/c012b414ac92446e17abb720ce7d1623534b3af342a958094e30044049fadef9.jpg)



(（g）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/2c8cccba03f7be4608f38fb1e995713c9cc704141e37c67ca0a6ffdab9c9e8e0.jpg)



Fig. 4 Illustration of combinations decided by the time-varying traffic conditions under the mixed traffic scenario



Fig. 5 Illustration of vehicles that cannot complete merging under the low penetration rate conditions


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/7f0952ba7ef3902863ca745ab523bd5b49ed06e141dbb1cb390e5601bfe5f817.jpg)


of driving safety. Hereinafter, the set of unplanned CAVs in Lanes 0, 1, and 2 within the Organizing Area is defined as $I _ { 0 } , \ I _ { 1 }$ , and $I _ { 2 }$ , respectively. The objective function (6) is to minimize the difference between the CAV’s velocity and the desired velocity cumulated over the entire control horizon. The other objective of (6) is to minimize the travel time and the merging time. The lateral lane-occupation sequence $k _ { \omega } , \omega ~ \in ~ \{ \sigma , i , \varpi ~ | \sigma ~ \in ~ I _ { 0 } , i ~ \in ~ I _ { 1 } , \varpi ~ \in ~ I _ { 2 } \}$ will synchronously update according to the merging time. In 

the following paragraphs, the mathematical equations for the constraints used in the optimization are introduced first, followed by discussions and interpretations of the constraints. The model is detailed as follows. 

# P1:

$$
\begin{array}{l} \min  _ {a (\omega , j), \omega \in \{\sigma , i, \varpi \}} \sum_ {j = t} ^ {t + h \times \Delta t} \left\{\kappa (j) \Delta t + (1 - \gamma (j)) \Delta t \right. \tag {6} \\ + \sum (v _ {u p p e r} - v (\omega , j)) \} \\ \end{array}
$$

s.t. 

$$
\begin{array}{l} \left\{ \begin{array}{l l} \kappa (j) = 1 p (i, j) \leq l _ {p m} + l _ {m a} \\ \kappa (j) = 0 p (i, j) > l _ {p m} + l _ {m a} \\ \kappa (j) = 1 p (\sigma , j) \leq l _ {p m} + l _ {m a} \\ \kappa (j) = 0 p (\sigma , j) > l _ {p m} + l _ {m a} \\ \kappa (j) = 1 p (\omega , j) \leq l _ {p m} + l _ {m a} \\ \kappa (j) = 0 p (\omega , j) > l _ {p m} + l _ {m a} \end{array} \right. \left\{ \begin{array}{l l} i f I _ {0} = \emptyset \& \\ \Phi_ {W V} ^ {i} (t) = \emptyset \\ i f I _ {0} \neq \emptyset \& \\ \Phi_ {W V} ^ {i} (t) = \emptyset \\ i f \Phi_ {W V} ^ {i} (t) \neq \emptyset \end{array} \right. \\ \omega = \omega_ {p} (i, j) \tag {7} \\ \end{array}
$$

$$
\left\{ \begin{array}{l} p (\sigma , j) \leq p (\omega , j) - s _ {0} - l _ {0} + (1 - \gamma (j)) \times M \omega \in \Phi_ {A} ^ {i} (t) \\ \hskip 2 8. 4 5 2 7 5 6 p t - \frac {(m a x (v (\sigma , j) - v (\omega , j) , 0) \times v _ {u p p e r})}{2 | a _ {l o w e r} |} \\ p (\sigma , j) \leq p (\omega , j) - s _ {0} - l _ {0} + (1 - \gamma (j)) \times M \omega \in \Phi_ {H} ^ {i} (t) \\ \hskip 2 8. 4 5 2 7 5 6 p t - \frac {(m a x (v (\sigma , j) \times v _ {u p p e r} - v ^ {2} (\omega , j) , 0))}{2 | a _ {l o w e r} |} \\ p (i, j) \leq p (\sigma , j) - s _ {0} - l _ {0} + (1 - \gamma (j)) \times M f o r a l l \\ \hskip 2 8. 4 5 2 7 5 6 p t - \frac {(m a x (v (i , j) - v (\sigma , j) , 0) \times v _ {u p p e r})}{2 | a _ {l o w e r} |} \end{array} \right.
$$

$$
\begin{array}{c} \omega = \omega_ {p} (i, j) \\ \hline \end{array} \tag {12}
$$

$$
\left\{ \begin{array}{l} p (\sigma , j) \leq p (\omega , j) - s _ {0} - l _ {0} + (1 - \beta (j)) \times M \omega \in \Phi_ {A} ^ {i} (t) - \frac {\left(\max  \left(v (\sigma , j) - v (\omega , j) , 0\right) \times v _ {u p p e r}\right)}{2 \left| a _ {l o w e r} \right|} \\ p (\sigma , j) \leq p (\omega , j) - s _ {0} - l _ {0} + (1 - \beta (j)) \times M \omega \in \Phi_ {H} ^ {i} (t) - \frac {\left(\max  \left(v (\sigma , j) \times v _ {u p p e r} - v ^ {2} (\omega , j) , 0\right)\right)}{2 \left| a _ {l o w e r} \right|} \end{array} \right. \tag {13}
$$

$$
\beta (j + \Delta t) = \gamma (j + \Delta t) - \gamma (j), \sum_ {j = t} ^ {t + h \times \Delta t} \beta (j) = 1, \omega = \omega_ {p} (\sigma , j)
$$

$$
\gamma (j) \leq 1 - \theta_ {\omega} (j), \omega \in \{i, \sigma \}, \gamma (t) = 0
$$

$$
\left\{ \begin{array}{l} \gamma (j) = 0 \quad i f I _ {0} = \varnothing \\ \sum_ {j = t} ^ {t + h \times \Delta t} \gamma (j) \geq 1 e l s e \end{array} \right. \tag {8}
$$

$$
p (\sigma , j) \leq l _ {p m} + l _ {m a} + \gamma (j) \times M \tag {14}
$$

$$
\left\{ \begin{array}{l} p (\varpi , j) \leq p (\omega , j) - s _ {0} - l _ {0} - \frac {\left(\max  (v (\varpi , j) - v (\omega , j) , 0) \times v _ {u p p e r}\right)}{2 \left| a _ {l o w e r} \right|} \omega \in \Phi_ {A} ^ {i} (t) \\ p (\varpi , j) \leq p (\omega , j) - s _ {0} - l _ {0} - \frac {\left(\max  (v (\varpi , j) \times v _ {u p p e r} - v ^ {2} (\omega , j) , 0)\right)}{2 \left| a _ {l o w e r} \right|} \omega \in \Phi_ {H} ^ {i} (t) \end{array} \right. \tag {15}
$$

$$
\varpi \in I _ {2}, \omega = \omega_ {p} (\varpi , j)
$$

$$
\begin{array}{l} \left\{ \begin{array}{l} \theta_ {\omega} (j) = 0 l _ {p m} \leq p (\omega , j) \leq l _ {p m} + l _ {m a} \\ \theta_ {\omega} (j) = 1 e l s e \end{array} \right. (9) \\ \omega \in \{i, \sigma \} (16) \\ \left\{ \begin{array}{c} p (i, j) \leq l _ {p m} + l _ {m a} - C _ {W V} \times \left(s _ {0} + l _ {0}\right) - \frac {v (i , j) \times v _ {u p p e r}}{2 \left| a _ {l o w e r} \right|} \\ \quad + (1 - \alpha (j)) \times M + \gamma (j) \times M \quad i f \Phi_ {W V} ^ {i} (t) \neq \emptyset \\ p (\sigma , j) \leq l _ {p m} + l _ {m a} - C _ {W V} \times \left(s _ {0} + l _ {0}\right) - \frac {v (\sigma , j) \times v _ {u p p e r}}{2 \left| a _ {l o w e r} \right|} \\ \quad + (1 - \alpha (j)) \times M + (1 - \gamma (j)) \times M \end{array} \right. (10) \\ \alpha (j + \Delta t) = \kappa (j + \Delta t) - \kappa (j), \sum_ {j = t} ^ {t + h \times \Delta t} \alpha (j) = 1 \\ \end{array}
$$

$$
\begin{array}{l} \left\{ \begin{array}{c c} p (\varepsilon , j) \leq p (\omega , j) - s _ {0} - l _ {0} + \gamma (j) \times M & \omega \in \Phi_ {A} ^ {i} (t) \\ - \frac {(m a x (v (\varepsilon , j) - v (\omega , j) , 0) \times v _ {u p p e r})}{2 | a _ {l o w e r} |} \\ p (\varepsilon , j) \leq p (\omega , j) - s _ {0} - l _ {0} + \gamma (j) \times M & \omega \in \Phi_ {H} ^ {i} (t) \\ - \frac {(m a x (v (\varepsilon , j) \times v _ {u p p e r} - v ^ {2} (\omega , j) , 0))}{2 | a _ {l o w e r} |} \end{array} \right. \\ \varepsilon \in \{i, \sigma \}, \omega = \omega_ {p} (\varepsilon , j) \tag {11} \\ \end{array}
$$

(I) Vehicle kinematics constraints: Based on the vehicle kinematics model (Eq. (5)). 

(II) Constraints for the travel time: In Eq. (7), $\kappa ( j )$ is an auxiliary variable, which takes the value either 1 or $0 . \kappa ( j ) = 0$ , if $\Phi _ { W V } ^ { i } ( t ) \neq \emptyset$ and the preceding vehicle of CAVs in Lane 1 $( i \in I _ { 1 } )$ has passed the Merging Area. This constraint indicates the moment 

when vehicles in $\Phi _ { W V } ^ { i } ( t )$ can be released to complete the merging. $\kappa ( j ) = 0$ , if $\Phi _ { W V } ^ { i } ( t ) = \theta$ and CAVs in Lane 0 $( \sigma \in I _ { 0 } )$ ) or Lane 1 $( i \in I _ { 1 } )$ has passed the Merging Area. This constraint indicates the travel time of CAVs. Because the travel time is the sum of $\kappa ( j )$ multiplied by the time step size $\Delta t$ , when $\kappa ( j ) = 1$ , it means that CAV is still within the Merging Area or the cooperative merging maneuver is not ended. 

Remark 2 It is noted that the merging point of CAVs is flexibly decided by the objective function Eq. (6). When the unplanned CAV that needs cooperative merging exists in Lane 0 $I _ { 0 } \ne \emptyset ,$ , the merging point of these CAVs $( \sigma \in I _ { 0 }$ ) is flexibly decided and located between the position of CAV in Lane 1 $( p ( i , j ) )$ and the end of Lane 0. In this way, CAVs in Lane 1 $( i \in I _ { 1 } )$ ) can ensure the merging point of CAV in Lane 0. It is unreliable to let the CAV in Lane 0 become the following vehicle of the CAV in Lane 1 after the merging if the original following vehicle of the CAV in Lane 1 is HV. The above phenomenon is quite possible considering the time-varying traffic conditions, especially under the low penetration rate conditions. In short, the auxiliary variable $\kappa ( j )$ can indicate the travel time of both CAVs in Lane 0 and Lane 1. 

(III) Constraints for completing cooperative merging: In Eq. (8) and (9), $\theta _ { \omega } ( j )$ and $\gamma ( j )$ are auxiliary variables. $\theta _ { \omega } ( j ) = 0$ if CAV $\omega \in \{ i , \sigma \}$ is located at the Merging Area. $\gamma ( j ) = 1$ if the cooperative merging is completed. 

(IV) Constraints about vehicles in $\Phi _ { W V } ^ { i } ( t )$ : In Eq. (10), $\alpha ( j )$ is an auxiliary variables. $\alpha ( j ) = 1$ stands for the moment when spaces that vehicles in $\Phi _ { W V } ^ { i } ( t )$ need to complete merging are created by CAVs. That is the moment when the original preceding vehicle of CAV i has passed the Merging Area. The moment is also constrained to later than the cooperative merging if $I _ { 0 } \neq \emptyset$ . 

Inspired by the method used in Mu et al. [20]. Hereafter, to avoid the convex constraints that complicate the MILP to the Mixed Integer Quadratic Programming, the convex terms like $\frac { v ^ { 2 } ( i , j ) } { 2 | a _ { l o w e r } | }$ 2 alower will be conservatively treated as v(i, j )×vupper $\begin{array} { r } { \frac { v ( i , j ) \times v _ { u p p e r } } { 2 | a _ { l o w e r } | } \geq \frac { v ^ { 2 } ( i , j ) } { 2 | a _ { l o w e r } | } } \end{array}$ 2|alower | 2 alo er . 

(V) Constraints for car-following: In this paper, collision avoidance is used for CAVs to achieve safety car-following. Considering the advance of CAVs, constraints for car-following are relaxed between CAVs but maintain conservatism when following a HV. The 

relaxed constraints (Eq. (11)) encourage CAVs to achieve the same velocity and maintain a smaller following distance so that redundant road spaces can be reserved for HVs. 

(VI) Constraints for completing safety merging: In Eqs. (12)-(14), $\beta ( j )$ is an auxiliary variables. $\beta ( j ) = 1$ if the cooperative merging is occurred. After the cooperative merging is completed, a local pure CAV platoon is formed. Cavs in Lane 0 $( \sigma \in I _ { 0 } ) ,$ ) become the new preceding vehicles of CAVs in Lane 1 $( i \in I _ { 1 } ) ,$ ) and the new following vehicles of the original preceding vehicle of CAVs in Lane 1. Equation (12) represents the constraints for completing safety merging. Moreover, CAVs in Lane 0 $\sigma \in I _ { 0 }$ ) should keep the safety car-following distance from its original preceding vehicle when the cooperative merging occurs (Eq. (13)). Equation (14) guarantees that the cooperative merging must be completed within the Merging Area. Otherwise, CAVs in Lane 0 $( \sigma \in I _ { 0 }$ ) have to decelerate and stop at the end of Lane 0. 

(VII) Constraints about vehicles in $I _ { 2 }$ : Eq. (15) is the constraint for car-following. Equation (16) is a conditional assistance constraint for CAVs in Lane 2 $\varpi \in$ $I _ { 2 }$ ) to create more spaces. If length $( \Phi _ { W V } ^ { i } ( t ) ) \geq C _ { W V } ^ { m a x }$ one can obtain that a certain number of vehicles are located at Lane 0 that fail to complete merging. Based on the CLCM, if CAVs in Lane 2 $( \varpi \in I _ { 2 } )$ ) maintain the same trajectory as CAVs in Lane 1 $( i \in I _ { 1 } ) ,$ , vehicles in $\Phi _ { W V } ^ { i } ( t )$ will have chances to continuously perform lane-change behaviors from Lane 1 to Lane 2 (as shown in Fig. 6). This will help to improve traffic efficiency under the condition of high traffic flow level but low PR. 

# 3.2.3 The hierarchical cooperative merging control model for CAVs in Lane 0 (HCMCC-L0)

In this subsection, the unplanned CAV $\sigma$ that arrives at the Cooperating Point is located at Lane 0. The objective is to check whether unplanned CAVs exist in Lanes 1 and 2, then create spaces for vehicles in $\Phi _ { W V } ^ { i } ( t )$ and minimize the travel time with the precondition of driving safety. The cost function is designed to improve traffic efficiency (same as P1). However, different from P1, the objective function (17) involves a new item to minimize the cut-in time of CAVs in Lane 2 if necessary (detailed descriptions are below). The lateral lane-occupation sequence $k _ { \omega } , \omega ~ \in ~ \{ \sigma , i , \varpi ~ | \sigma ~ \in ~ I _ { 0 } , i ~ \in ~ I _ { 1 } , \varpi ~ \in ~ I _ { 2 } \}$ will syn-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/b71216a42521665fbef5a883c0f6afc68cefe1fc32ce4610eb4a5f09025b6af9.jpg)



Fig. 6 Illustration of the conditional assistance constraint for CAV $\varpi \in I _ { 2 }$


chronously update according to the merging time and the cut-in time. The model is detailed as follows. 

P2: 

$$
\begin{array}{l} \min  _ {a (\omega , j), \omega \in \{\sigma , i, \varpi \}} \sum_ {j = t} ^ {t + h \times \Delta t} \\ \{\kappa (j) \Delta t + (1 - \gamma (j)) \Delta t + (1 - \chi (j)) \Delta t \\ + \sum (v _ {u p p e r} - v (\omega , j)) \} \\ \end{array}
$$

s.t. 

(17) 

$$
\begin{array}{l} \left\{ \begin{array}{l} \kappa (j) = 1 p (\sigma , j) \leq l _ {p m} + l _ {m a} \\ \kappa (j) = 0 p (\sigma , j) > l _ {p m} + l _ {m a} \\ \kappa (j) = 1 p (\omega , j) \leq l _ {p m} + l _ {m a} \\ \kappa (j) = 0 p (\omega , j) > l _ {p m} + l _ {m a} \end{array} \right\} i f \Phi_ {W V} ^ {i} (t) = \emptyset \\ \omega = \omega_ {p} (\sigma , j) \\ \end{array}
$$

(18) 

$$
\begin{array}{l} \left\{ \begin{array}{l} p (\sigma , j) \leq l _ {p m} + l _ {m a} - C _ {W V} \times (s _ {0} + l _ {0}) - \frac {v (\sigma , j) \times v _ {u p p e r}}{2 | a _ {l o w e r} |}   i f   \Phi_ {W V} ^ {i} (t) \neq \emptyset \\ \hskip 1 4. 2 2 6 3 7 8 p t + (1 - \alpha (j)) \times M + (1 - \gamma (j)) \times M \end{array} \right. \\ \alpha (j + \Delta t) = \kappa (j + \Delta t) - \kappa (j), \sum_ {j = t} ^ {t + h \times \Delta t} \alpha (j) = 1 \\ \end{array}
$$

$$
\begin{array}{l} \left\{ \begin{array}{r l} p (\sigma , j) \leq p (\omega , j) - s _ {0} - l _ {0} - \frac {(m a x (v (\sigma , j) - v (\omega , j) , 0) \times v _ {u p p e r})}{2 | a _ {l o w e r} |} & \\ + (1 - \gamma (j)) \times M + \chi (j) \times M & \omega \in \Phi_ {A} ^ {i} (t) \\ p (\sigma , j) \leq p (\omega , j) - s _ {0} - l _ {0} - \frac {(m a x (v (\sigma , j) \times v _ {u p p e r} - v ^ {2} (\omega , j) , 0))}{2 | a _ {l o w e r} |} & \\ + (1 - \gamma (j)) \times M + \chi (j) \times M & \omega \in \Phi_ {H} ^ {i} (t) \\ p (i, j) \leq p (\sigma , j) - s _ {0} - l _ {0} - \frac {(m a x (v (i , j) - v (\sigma , j) , 0) \times v _ {u p p e r})}{2 | a _ {l o w e r} |} & \\ + (1 - \gamma (j)) \times M + \chi (j) \times M & f o r a l l \end{array} \right. \\ \omega = \omega_ {p} (i, j) \\ \end{array}
$$

$$
\left\{ \begin{array}{r l r} p (\sigma , j) & \leq p (\omega , j) - s _ {0} - l _ {0} - \frac {\left(m a x \left(v (\sigma , j) - v (\omega , j) , 0\right) \times v _ {u p p e r}\right)}{2 \left| a _ {l o w e r} \right|} \\ & + (1 - \gamma (j)) \times M + (1 - \chi (j)) \times M & \omega \in \Phi_ {A} ^ {i} (t) \\ p (\sigma , j) \leq & p (\omega , j) - s _ {0} - l _ {0} - \frac {\left(m a x \left(v (\sigma , j) \times v _ {u p p e r} - v ^ {2} (\omega , j) , 0\right)\right)}{2 \left| a _ {l o w e r} \right|} \\ & + (1 - \gamma (j)) \times M + (1 - \chi (j)) \times M & \omega \in \Phi_ {H} ^ {i} (t) \\ p (\varpi , j) \leq & p (\sigma , j) - s _ {0} - l _ {0} - \frac {\left(m a x \left(v (\varpi , j) - v (\sigma , j) , 0\right) \times v _ {u p p e r}\right)}{2 \left| a _ {l o w e r} \right|} \\ & + (1 - \gamma (j)) \times M + (1 - \chi (j)) \times M & f o r a l l \\ & & \varpi \in I _ {2}, \omega = \omega_ {p} (\varpi , j) \end{array} \right. \tag {25}
$$

$$
\left\{ \begin{array}{c} p (\sigma , j) \leq p (\omega , j) - s _ {0} - l _ {0} + (1 - \beta (j)) \times M \\ - \frac {\left(\max  \left(v (\sigma , j) - v (\omega , j) , 0\right) \times v _ {u p p e r}\right)}{2 \left| a _ {l o w e r} \right|} \quad \omega \in \Phi_ {A} ^ {i} (t) \\ p (\sigma , j) \leq p (\omega , j) - s _ {0} - l _ {0} + (1 - \beta (j)) \times M \\ - \frac {\left(\max  \left(v (\sigma , j) \times v _ {u p p e r} - v ^ {2} (\omega , j) , 0\right)\right)}{2 \left| a _ {l o w e r} \right|} \quad \omega \in \Phi_ {H} ^ {i} (t) \end{array} \right. \tag {26}
$$

$$
\beta (j + \Delta t) = \gamma (j + \Delta t) - \gamma (j), \sum_ {j = t} ^ {t + h \times \Delta t} \beta (j) = 1, \omega = \omega_ {p} (\sigma , j)
$$

$$
p (\sigma , j) \leq l _ {p m} + l _ {m a} + \gamma (j) \times M \tag {27}
$$

$$
\left\{ \begin{array}{l} p (\varpi , j) \leq p (\omega , j) - s _ {0} - l _ {0} \quad \omega \in \Phi_ {A} ^ {i} (t) \\ - \frac {\left(\max \left(v (\varpi , j) - v (\omega , j) , 0\right) \times v _ {u p p e r}\right)}{2 \left| a _ {l o w e r} \right|} \\ p (\varpi , j) \leq p (\omega , j) - s _ {0} - l _ {0} \quad \omega \in \Phi_ {H} ^ {i} (t) \\ - \frac {\left(\max \left(v (\varpi , j) \times v _ {u p p e r} - v ^ {2} (\omega , j) , 0\right)\right)}{2 \left| a _ {l o w e r} \right|} \\ p (\varpi , j) \leq p (\omega , j) - s _ {0} - l _ {0} + \gamma (j) \times M \quad \omega \in \Phi_ {A} ^ {i} (t) \\ - \frac {\left(\max \left(v (\varpi , j) - v (\omega , j) , 0\right) \times v _ {u p p e r}\right)}{2 \left| a _ {l o w e r} \right|} \\ p (\varpi , j) \leq p (\omega , j) - s_{0}- l_{0}+\gamma(j)\times M \quad \omega \in \Phi_ {H} ^ {i} (t) \\ - \frac {\left(\max \left(v (\varpi , j) \times v _ {u p p e r} - v ^ {2} (\omega , j) , 0\right)\right)}{2 \left| a _ {l o w e r} \right|} \\ \end{array} \right\} \text {e l s e} \tag {28}
$$

$$
\left\{ \begin{array}{l} p (\varpi , j) \geq p (\omega , j) + s _ {0} + l _ {0} - (1 - \Lambda (j)) \times M \\ \hskip 2 8. 4 5 2 7 5 6 p t + \frac {(m a x (v (\omega , j) - v (\varpi , j) , 0) \times v _ {u p p e r})}{2 | a _ {l o w e r} |} \omega \in \Phi_ {A} ^ {i} (t) \\ p (\varpi , j) \geq p (\omega , j) + s _ {0} + l _ {0} - (1 - \Lambda (j)) \times M \\ \hskip 2 8. 4 5 2 7 5 6 p t + \frac {v ^ {2} (\omega , j)}{2 | a _ {l o w e r} |} \omega \in \Phi_ {H} ^ {i} (t) \end{array} \right.
$$

$$
\begin{array}{c} \Lambda (j + \Delta t) = \chi (j + \Delta t) - \chi (j), \sum_ {j = t} ^ {t + h \times \Delta t} \Lambda (j) = 1 \\ \varpi \in I _ {2}, \omega = \omega_ {r f} (\varpi , j) \end{array} \tag {29}
$$

$$
\left\{ \begin{array}{c} p (\varpi , j) \leq \max  \{p (\omega , j) \} \\ + \chi (j) \times M i f l e n g t h \left(\Phi_ {W V} ^ {i} (t)\right) \geq C _ {W V} ^ {\max } \\ \omega \in \{i, \sigma \} \end{array} \right. \tag {30}
$$

(I) Vehicle kinematics constraints and constraints for car-following: Vehicle kinematics constraints are identical to those used in Eq. (5). Similarly, the constraints for car-following remain unchanged as Eq. (11). 

(II) Constraints for the travel time: In Eq. (18), $\kappa ( j ) = 0$ , if $\Phi _ { W V } ^ { i } ( t ) \neq \emptyset$ and the preceding vehicle of CAVs in Lane 0 $( \sigma \in I _ { 0 } ) ,$ ) has passed the Merging Area. $\kappa ( j ) = 0$ , if $\Phi _ { W V } ^ { i } ( t ) = \emptyset$ and CAVs in Lane 0 $( \sigma \in I _ { 0 } )$ ) has passed the Merging Area. This constraint indicates the travel time of CAVs. 

(III) Constraints for completing cooperative merging: Considering the time-varying traffic conditions, one cannot guarantee that a pair of CAVs always exists 


Fig. 7 Illustration of the scenario that $I _ { 1 } = \emptyset$ and $I _ { 2 } \neq { \mathcal { O } }$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/cc222e231d8111c69918e02e0b3848680cef141741f1b8bc8eda051729a24252.jpg)



Fig. 8 Illustration of the non-cooperative merging


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/1e40385effd50cf7b405c751ddba480979575180bab3042ebb74bea4573784fc.jpg)


to perform the cooperative merging maneuvers, especially under low penetration rate conditions of CAVs (i.e., $I _ { 0 } \ne \emptyset$ , $I _ { 1 } = \varnothing$ , and $I _ { 2 } \ne \emptyset$ ). Hence, CAV in Lane 2 is necessary to cut into Lane 1 to complete the cooperative merging maneuvers (as shown in Fig. 7). The feasible lane-change spaces for cut-in are obtained from $G _ { t } ^ { i }$ . 

Equation (22) indicates whether the cut-in is necessary or not, that is $\chi ( j ) = 0$ , if the cut-in is unnecessary $I _ { 1 } \neq \emptyset$ ). $\chi ( j ) \leq 1$ , if the cut-in is needed. Also, the cooperative merging can only be completed when all the CAVs are within the Merging Area (Eqs. (19), (20) and (21)). Moreover, the cooperative merging is also constrained to a time later than the cut-in time if the cut-in is necessary. 

(IV) Constraints about vehicles in $\Phi _ { W V } ^ { i } ( t )$ : In Eqs. (23), the moment when spaces that vehicles in $\Phi _ { W V } ^ { i } ( t )$ need to complete merging are created is modified as the moment that CAV $\sigma$ has completed the cooperative merging and its preceding vehicle has passed the Merging Area. 

(V) Constraints for completing safety merging: Eqs. (24) and (25) indicate the safety merging constraints without and with the cut-in, respectively. The other constraints (Eqs. (26) and (27)) are the same as those in P1. 

(VI) Constraints about vehicles in $I _ { 2 } \colon \Lambda ( j ) = 1$ if the cut-in is occurred. Equation (28) ensures the safety distance for the car-following. Equation (29) restricts the safety lane-change behavior when performing the cut-in. The constraints in Eq. (29) are also classified according to the actual following vehicle in the adjacent lane on the right. Equation (30) is the conditional 

assistance constraint, but it is disabled when the cut-in is necessary. 

# 3.2.4 The simplified hierarchical merging control model for CAVs in Lane 0 (SHCMCC-L0)

In this subsection, the unplanned CAV $\sigma$ that arrives at the Cooperating Point is located at Lane 0. Different from the model defined in Sect. 3.2.3, a simplified model is defined for CAV $\sigma$ . As shown in Fig. 8, the unplanned CAV $\sigma$ complete merging without cooperative maneuvers $I _ { 1 } = \emptyset$ and $I _ { 2 } = \emptyset ,$ ). $g _ { l } ( \sigma , t )$ is a feasible lane-change space that satisfy Eq. (4) and the following safety lane-change constraint. The objective is to minimize travel time and cut-in time with the precondition of driving safety. The lateral lane-occupation sequence $k _ { \omega } , \omega ~ \in ~ \{ \sigma , i , \varpi ~ | \sigma \in I _ { 0 } , i \in I _ { 1 } , \varpi \in I _ { 2 } \}$ $\varpi \in I _ { 2 } \}$ will synchronously update according to the cut-in time. The mathematic constraints are introduced first and followed by interpretations. 

# P3:

$$
\begin{array}{l} \min  _ {a (\sigma , j)} \sum_ {j = t} ^ {t + h \times \Delta t} \\ \{\kappa (j) \Delta t + (1 - \chi (j)) \Delta t + \sum \left(v _ {\text {u p p e r}} - v (\sigma , j)\right) \} \\ \text {s . t .} \end{array} \tag {31}
$$

$$
\left\{ \begin{array}{l} \kappa (j) = 1 p (\sigma , j) \leq l _ {p m} + l _ {m a} \\ \kappa (j) = 0 p (\sigma , j) > l _ {p m} + l _ {m a} \end{array} \right. \tag {32}
$$

$$
\chi (j) \leq 1 - \theta_ {\sigma} (j), \chi (t) = 0, \sum_ {j = t} ^ {t + h \times \Delta t} \chi (j) \geq 1 \tag {33}
$$

$$
\left\{ \begin{array}{l} \theta_ {\sigma} (j) = 0 l _ {p m} \leq p (\sigma , j) \leq l _ {p m} + l _ {m a} \\ \theta_ {\sigma} (j) = 1 e l s e \end{array} \right. \tag {34}
$$

$$
\left\{ \begin{array}{l l} p (\sigma , j) \geq p (\omega , j) + s _ {0} + l _ {0} - (1 - \Lambda (j)) \times M \\ \hskip 2 8. 4 5 2 7 5 6 p t + \frac {(m a x (v (\omega , j) - v (\sigma , j) , 0) \times v _ {u p p e r})}{2 | a _ {l o w e r} |} & \omega \in \Phi_ {A} ^ {i} (t) \\ p (\sigma , j) \geq p (\omega , j) + s _ {0} + l _ {0} - (1 - \Lambda (j)) \times M \\ \hskip 2 8. 4 5 2 7 5 6 p t + \frac {v ^ {2} (\omega , j)}{2 | a _ {l o w e r} |} & \omega \in \Phi_ {H} ^ {i} (t) \end{array} \right.
$$

$$
\Lambda (j + \Delta t) = \chi (j + \Delta t) - \chi (j), \sum_ {j = t} ^ {t + h \times \Delta t} \Lambda (j) = 1
$$

$$
\sigma \in I _ {0}, \omega = \omega_ {l f} (\sigma , j) \tag {35}
$$

I) Vehicle kinematics constraints and constraints for car-following: Vehicle kinematics constraints are identical to those used in Eq. (5). Similarly, the constraints for car-following remain unchanged as Eq. (11). 

II) Constraints for the travel time: In Eq. (32), $\kappa ( j ) = 0$ , if CAV $\sigma$ has passed the Merging Area. This constraint indicates the travel time of CAVs. 

III) Constraints for safety lane-change behavior: Eqs. (33) and (34) ensure the cut-in can only be performed within the Merging Area. Equation (35) restricts the safety lane-change behavior when performing the cut-in. The feasible lane-change spaces for cut-in are obtained from $G _ { t } ^ { i }$ . 

# 4 Operational layer

# 4.1 Vehicle dynamic model

In order to grasp many important features of vehicle dynamics, such as inertia delay, the dynamics process of vehicle acceleration/deceleration, and so on, some scholars proposed the nonlinear third-order dynamic system. The model of CAV $i$ is expressed as follows: 

$$
\dot {p} (i, t) = v (i, t)
$$

$$
\dot {v} (i, t) = a (i, t)
$$

$$
\begin{array}{l} \dot {a} (i, t) = - \frac {a (i , t) + \frac {\rho A _ {i} C _ {d , i}}{2 m _ {i}} v ^ {2} (i , t) + g \sin \lambda + \mu_ {i} g \cos \lambda}{\tau_ {i}} \tag {36} \\ - \frac {\rho A _ {i} C _ {d , i}}{m _ {i}} v (i, t) a (i, t) - g \cos \lambda \\ + \mu_ {i} g \sin \lambda + \frac {c _ {i}}{m _ {i} \tau_ {i}} \\ \end{array}
$$

$m _ { i }$ is the mass, $A _ { i }$ is the vehicle cross-section area, $\rho$ and $C _ { d , i }$ denote the air density and drag coefficient, respectively, $\tau _ { i }$ is the inertial delay, $g$ represents the gravity acceleration, $\mu _ { i }$ is the coefficient of rolling resistance, $\lambda$ denotes the road slope. 

The linear feedback technique used in [36] is introduced to linearize the nonlinear third-order dynamic system (36). Due to such transformation, the actual input $c _ { i }$ of the dynamic system is arranged as 

$$
\begin{array}{l} c _ {i} = m _ {i} u (i, t) + m _ {i} v (i, t) + \tau_ {i} \rho A _ {i} C _ {d, i} v (i, t) a (i, t) \\ + \frac {1}{2} \rho A _ {i} C _ {d, i} v ^ {2} (i, t) \\ + \tau_ {i} m _ {i} g (\cos \lambda - \mu_ {i} \sin \lambda) \\ + m _ {i} g \sin \lambda + \mu_ {i} m _ {i} g \cos \lambda \tag {37} \\ \end{array}
$$

$u ( i , t )$ is the control signal to be derived later. $\upsilon ( i , t )$ is the external disturbances. Then the linear third-order dynamic system with the external disturbances is established as follows. 

$$
\dot {p} (i, t) = v (i, t)
$$

$$
\dot {v} (i, t) = a (i, t) \tag {38}
$$

$$
\dot {a} (i, t) = - \frac {1}{\varsigma_ {i}} a (i, t) + \frac {1}{\varsigma_ {i}} u (i, t) + \frac {1}{\varsigma_ {i}} v (i, t)
$$

Assumption 1 The first derivative of disturbance $\upsilon ( i , t )$ is bounded and satisfy $| \dot { \boldsymbol { \upsilon } } ( i , t ) | \leq \iota _ { i }$ , where $\iota _ { i }$ is the upper bound. 

Lemma 1 [37]: Define a time-varying scaling function as follows: 

$$
\vartheta (t) = \left\{ \begin{array}{l l} \frac {T ^ {\ell}}{(T - t) ^ {\ell}} & t \in [ 0, T) \\ 1 & t \in [ T, \infty) \end{array} \right. \tag {39}
$$

where $\ell > 2$ is any real number, T is the settling time. In addition 

$$
\dot {\vartheta} (t) = \left\{ \begin{array}{l l} \frac {\ell}{T} \vartheta^ {1 + \frac {1}{\ell}} (t) & t \in [ 0, T) \\ 0 & t \in [ T, \infty) \end{array} \right. \tag {40}
$$

Consider a system ${ \dot { x } } ( t ) = f ( t , x ( t ) ) , t \in \mathbb { R } _ { + }$ , $x ( 0 )$ $= x _ { 0 }$ . Let $V ( t , x ( t ) ) : U \times \mathbb { R } _ { + } \to \mathbb { R }$ be a continuously differentiable function and $U \in \mathbb { R } ^ { m }$ be a domain containing the origin. If there exists a real constant $b > 0$ such that 

$$
V (t, 0) = 0 \text {a n d} V (t, x (t)) > 0 \text {i n} U - \{0 \} \tag {41}
$$

$$
\dot {V} (t, x (t)) = - b V (t, x (t)) - 2 \frac {\dot {\vartheta} (t)}{\vartheta (t)} V (t, x (t)) i n U \tag {42}
$$

where $\dot { V } ( t , x ( t ) ) ~ = ~ ( \partial V ( t , x ( t ) ) / \partial x ( t ) ) f ( t , x ) $ , then the origin of system $\begin{array} { r c l } { \dot { x } ( t ) } & { = } & { f ( t , x ( t ) ) } \end{array}$ is prescribed-time stable with the prescribed time $T$ given 

in Eq. (39). If $U ~ = ~ \mathbb { R } ^ { m }$ , then the system $\dot { x } ( t ) \ =$ $f ( t , x ( t ) )$ is globally prescribed-time stable with the prescribed time $T$ . In addition, for $t ~ \in ~ [ 0 , T )$ , it holds that $V ( t , x ( t ) ) \leq \vartheta ^ { - 2 } ( t ) e ^ { - b t } V ( 0 , 0 )$ , and, for $t \in [ T , \infty )$ , it holds that $V ( t , x ( t ) ) \equiv 0$ . 

# 4.2 The prescribed-time observer

From the linear third-order dynamic system, we define $x ^ { T } ( i , t ) = \left[ p ^ { T } ( i , t ) ~ v ^ { T } ( i , t ) ~ a ^ { T } ( i , t ) \right] ^ { T }$ and $x ^ { \ast T } ( i , t ) =$ $\left[ p ^ { * T } ( i , t ) ~ \boldsymbol { v } ^ { * T } ( i , t ) ~ \boldsymbol { a } ^ { * T } ( i , t ) \right] ^ { T }$ , where $x ^ { * } ( i , t )$ is the desired state of CAV $i$ from the programmed trajectories at time t. The control signal $u ( i , t )$ is designed separately in Sect. 4.3. Then, the error system is established as follows. 

$$
\begin{array}{l} \dot {e} (i, t) = A _ {m} e (i, t) + B _ {m} u (i, t) \\ + B _ {m} \xi (i, t) + B _ {m} v (i, t) \tag {43} \\ \end{array}
$$

where $\begin{array} { r l r } { e ^ { T } ( i , t ) } & { { } = } & { x ^ { T } ( i , t ) ~ - ~ x ^ { * T } ( i , t ) ~ \div } \end{array}$ 

$$
\begin{array}{r l r} {[ e _ {p} ^ {T} (i, t) e _ {v} ^ {T} (i, t) e _ {a} ^ {T} (i, t) ] ^ {T}, A _ {m}} & = & {\left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \quad 1 \right],} \\ & & {\left[ \begin{array}{l l} 0 & - 1 / \tau_ {i} \end{array} \right]} \end{array}
$$

$B _ { m } = \left[ 0 0 1 / \tau _ { i } \right] ^ { T } , \xi ( i , t ) = - u ^ { * } ( i , t ) . u ^ { * } ( i , t )$ is the desired control signal. 

To deal with the effect of the external disturbances, a PTO is introduced as follows: 

$$
\begin{array}{l} \dot {\hat {e}} _ {a} (i, t) = - \frac {1}{\tau} \hat {e} _ {a} (i, t) \\ + \frac {1}{\tau} u (i, t) + \frac {1}{\tau} \xi (i, t) + \frac {1}{\tau} \hat {v} (i, t) \tag {44} \\ \end{array}
$$

$$
\begin{array}{l} \hat {v} (i, t) = (\kappa_ {i, 1} + \kappa_ {i, 2} \frac {\dot {\vartheta} (t)}{\vartheta (t)}) (e _ {a} (i, t) \\ - \hat {e} _ {a} (i, t)) + \kappa_ {i, 3} s i g n (e _ {a} (i, t) - \hat {e} _ {a} (i, t)) \\ + \int_ {0} ^ {t} \iota_ {i} \operatorname {s i g n} \left(e _ {a} (i, s) - \hat {e} _ {a} (i, s)\right) d s \tag {45} \\ \end{array}
$$

where $\hat { e } _ { a } ( i , t )$ and $\hat { \upsilon } ( i , t )$ are the estimate of $e _ { a } ( i , t )$ and $\upsilon ( i , t )$ , $\tilde { e } _ { a } ( i , t ) = e _ { a } ( i , t ) - \hat { e } _ { a } ( i , t )$ and $\tilde { \upsilon } ( i , t ) =$ $\upsilon ( i , t ) - \hat { \upsilon } ( i , t ) , \kappa _ { i , 1 } , \kappa _ { i , 2 } .$ , and $\kappa _ { i , 3 }$ are positive parameters, and $\kappa _ { i , 2 } > 1 . { s i g n } ( \bullet )$ is the sign function. 

Theorem 1 For the error system (43) with Assumption 1, under the PTO (Eq. (44)-(45)), the external disturbances $\upsilon ( i , t )$ can be estimated in the prescribed time $T$ with zero estimation error. 

Proof Taking the derivative of $\hat { e } _ { a } ( i , t )$ along with Eq. (44) yields 

$$
\begin{array}{l} \dot {\hat {e}} _ {a} (i, t) = \dot {e} _ {a} (i, t) - \dot {\hat {e}} _ {a} (i, t) \\ = - \frac {1}{\tau} \tilde {e} _ {a} (i, t) - \frac {1}{\tau} \left(\kappa_ {i, 1} + \kappa_ {i, 2} \frac {\dot {\vartheta} (t)}{\vartheta (t)}\right) \tilde {e} _ {a} (i, t) \\ - \frac {1}{\tau} \kappa_ {i, 3} \operatorname {s i g n} \left(\tilde {e} _ {a} (i, t)\right) + \hbar (i, t) \tag {46} \\ \end{array}
$$

$$
\begin{array}{l} \dot {\hbar} (i, t) = \frac {1}{\tau} \dot {\nu} (i, t) - \frac {1}{\tau} \iota_ {i} s i g n (\tilde {e} _ {a} (i, t)) \\ w h e r e \hbar (i, 0) = 0 \tag {47} \\ \end{array}
$$

The following Lyapunov function is considered $\begin{array} { r } { V _ { i } = \frac { 1 } { 2 } \tilde { e } _ { a } ^ { 2 } ( i , t ) } \end{array}$ . Taking the derivative of $V _ { i }$ along with Eq. (46)-(47), one can obtain that 

$$
\begin{array}{l} \dot {V} _ {i} = \tilde {e} _ {a} (i, t) \dot {\tilde {e}} _ {a} (i, t) \\ = - \frac {1}{\tau} \tilde {e} _ {a} ^ {2} (i, t) - \frac {1}{\tau} \left(\kappa_ {i, 1} + \kappa_ {i, 2} \frac {\dot {\vartheta} (t)}{\vartheta (t)}\right) \tilde {e} _ {a} ^ {2} (i, t) \\ - \frac {1}{\tau} \kappa_ {i, 3} \operatorname {s i g n} \left(\tilde {e} _ {a} (i, t)\right) \tilde {e} _ {a} (i, t) + \hbar (i, t) \tilde {e} _ {a} (i, t) \tag {48} \\ \end{array}
$$

Based on Eqs. (46)-(47), and Assumption 1, when $\tilde { e } _ { a } ( i , t )$ is positive, one can obtain that $\dot { \hbar } ( i , t ) ~ \leq ~ 0$ . Together with the initial condition that $\hbar ( i , 0 ) = 0$ in Eq. (47), it can be inferred that $\hbar ( i , t ) \leq 0$ . When $\tilde { e } _ { a } ( i , t )$ is negative, then $\dot { \hbar } ( i , t ) \geq 0$ based on Eq. (47). Together with the initial condition, then $\hbar ( i , t ) \ge 0$ . This concludes that $\hbar ( i , t ) \tilde { e } _ { a } ( i , t ) \leq 0$ for all $t \geq 0$ . Now, one can obtain that: 

$$
\begin{array}{l} \dot {V} _ {i} \leq - \left(\kappa_ {i, 1} + \kappa_ {i, 2} \frac {\dot {\vartheta} (t)}{\vartheta (t)}\right) \tilde {e} _ {a} ^ {2} (i, t) \\ = - \left(2 \kappa_ {i, 1} + 2 \frac {\dot {\vartheta} (t)}{\vartheta (t)}\right) V _ {i} \tag {49} \\ \end{array}
$$

Lemma 1 and Eq. (49), it can be derived that $\tilde { e } _ { a } ( i , t ) = 0$ and $\dot { \tilde { e } } _ { a } ( i , t ) = 0$ when $t \geq T$ . Considering that $\begin{array} { r } { \dot { \tilde { e } } _ { a } ( i , t ) = - \frac { 1 } { \tau } \tilde { e } _ { a } ( i , t ) + \frac { 1 } { \tau } \tilde { \upsilon } ( i , t ) } \end{array}$ , one can obtain that $\tilde { \upsilon } ( i , t ) = 0$ when $t \geq T$ . 

# 4.3 The Laguerre-function-based continuous-time model predictive control (LCMPC)

Letting $\varsigma ( i , t ) = u ( i , t ) + \xi ( i , t ) + \upsilon ( i , t )$ the error system (43) can be rewritten as 

$$
\dot {e} (i, t) = A _ {m} e (i, t) + B _ {m} \varsigma (i, t) \tag {50}
$$

Then, the output of the error system (43) is defined as $y ( i , t ) = C _ { m } e ( i , t )$ , where $C _ { m } = \left[ 1 0 0 \right]$ . The objective of LCMPC is to drive the output of the error system (43) to the desired output $r ( i , t )$ . That is the position error $\tilde { e } _ { p } ( i , t )$ converges to a finite set around $r ( i , t )$ . Hence, the desired output is set as $r ( i , t ) ~ = ~ 0$ for all $t \ \geq \ 0 . \ \delta ( i , t ) = y ( i , t ) - r ( i , t )$ . Therefore, the extended error system can be obtained. 

$$
\begin{array}{l} \overbrace {\left[ \begin{array}{l} \ddot {e} (i , t) \\ \dot {\delta} (i , t) \end{array} \right]} ^ {\dot {\zeta} (i, t)} = \overbrace {\left[ \begin{array}{l l} A _ {m} & 0 \\ C _ {m} & 0 \end{array} \right]} ^ {A _ {e}} \overbrace {\left[ \begin{array}{l} \dot {e} (i , t) \\ \delta (i, t) \end{array} \right]} ^ {\zeta (i, t)} + \overbrace {\left[ \begin{array}{l} B _ {m} \\ 0 \end{array} \right]} ^ {B _ {e}} \dot {\varsigma} (i, t) \tag {51} \\ \Omega (i, t) = \widetilde {\left[ \begin{array}{c} 0 \\ 1 \end{array} \right]} \left[ \begin{array}{c} \dot {e} (i, t) \\ \delta (i, t) \end{array} \right] \\ \end{array}
$$

From the extended error system (51), the state and output at the future time $\phi$ are described by the following equations: 

$$
\begin{array}{l} \zeta (i, t + \phi | t) = e ^ {A _ {e} \phi} \zeta (i, t) + \int_ {0} ^ {\phi} e ^ {A _ {e} (\phi - s)} B _ {e} \dot {\zeta} (s) d s \\ \Omega (i, t + \phi | t) = C _ {e} e ^ {A _ {e} \phi} \zeta (i, t) + C _ {e} \int_ {0} ^ {\phi} e ^ {A _ {e} (\phi - s)} B _ {e} \dot {\zeta} (s) d s \tag {52} \\ \end{array}
$$

The objective function for the extended error system (51) is chosen as: 

$$
\begin{array}{l} J = \int_ {0} ^ {T _ {p}} \left(\Omega^ {T} (i, t + s | t) \Omega (i, t + s | t) + \dot {\varsigma} ^ {T} (s) R \dot {\varsigma} (s)\right) d s \\ = \int_ {0} ^ {T _ {p}} \left(\zeta^ {T} (i, t + s | t) Q \zeta (i, t + s | t) + \dot {\zeta} ^ {T} (s) R \dot {\zeta} (s)\right) d s \tag {53} \\ \end{array}
$$

where $T _ { p }$ is the predictive horizon and $Q = C _ { e } ^ { T } C _ { e }$ . $R$ is the weight diagonal matrix. 

The idea for reducing the computational complexity by LCMPC is to describe the future control input as the sum of several orthonormal functions (satisfy Eq. (54)). The future control inputs were described as a linear combination of $N$ orthonormal functions. With this, the optimization variable was reduced to $N$ . 

$$
\left\{ \begin{array}{l} \int_ {0} ^ {\infty} l _ {m} ^ {2} (t) d t = 1 \quad m = j \\ \int_ {0} ^ {\infty} l _ {m} (t) l _ {j} (t) d t = 0 \quad m \neq j \end{array} \right. \tag {54}
$$

Next, the Continuous-time Laguerre Functions can be derived by the state-space form as below. Define the state vector $L ( t ) = \left[ l _ { 1 } ( t ) l _ { 2 } ( t ) \ldots l _ { j } ( t ) \right] ^ { T }$ . Assuming initial conditions of the state vector as $L ( 0 ) \ =$ $\sqrt { 2 p } \big [ 1 \ 1 \ . . . \ 1 \big ] ^ { T }$ , then the Laguerre functions satisfy 

the state-space equation: 

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {l} _ {1} (t) \\ \dot {l} _ {2} (t) \\ \vdots \\ \dot {l} _ {N} (t) \end{array} \right] = \left[ \begin{array}{c c c c} - p & 0 & \dots & 0 \\ - 2 p & - p & \dots & 0 \\ \vdots & \ddots & \ddots & \vdots \\ - 2 p & \dots & - 2 p & - p \end{array} \right] \left[ \begin{array}{c} l _ {1} (t) \\ l _ {2} (t) \\ \vdots \\ l _ {N} (t) \end{array} \right] \\ = A _ {p} \left[ \begin{array}{c} l _ {1} (t) \\ l _ {2} (t) \\ \vdots \\ l _ {N} (t) \end{array} \right] \tag {55} \\ \end{array}
$$

The solution of the differential equation (55) gives the set of the Continuous-time Laguerre Functions for $j ~ = ~ 1 , 2 , . . . N$ as $L ( t ) ~ = ~ e ^ { A _ { p } t } L ( 0 )$ . And the control signal $\varsigma ( i , t )$ at time $t$ is expressed as the orthonormal expansion $\dot { \varsigma } ( i , t ) = L ^ { T } ( t ) \eta$ , where $\eta =$ $\left[ c _ { 1 } c _ { 2 } \ldots c _ { N } \right] ^ { T }$ is the coefficient vector. Hence, Eq. (52) can be rewritten as: 

$$
\zeta (i, t + \phi | t) = e ^ {A _ {e} \phi} \zeta (i, t) + \bar {\lambda} ^ {T} (\phi) \eta \tag {56}
$$

$$
\Omega (i, t + \phi | t) = C _ {e} e ^ {A _ {e} \phi} \zeta (i, t) + C _ {e} \bar {\lambda} ^ {T} (\phi) \eta
$$

where $\begin{array} { r } { \bar { \lambda } ^ { T } ( \phi ) \ = \ \int _ { 0 } ^ { \phi } e ^ { A _ { e } ( \phi - s ) } B _ { e } L ^ { T } ( s ) d s } \end{array}$ . Combine Eqs. (52), (54) and (56) with Eq. (53). One can obtain that: 

$$
\begin{array}{l} \int_ {0} ^ {T _ {p}} \left(\zeta^ {T} (i, t + s | t) Q \zeta (i, t + s | t) + \dot {\zeta} ^ {T} (s) R \dot {\zeta} (s)\right) d s \\ = \int_ {0} ^ {T _ {p}} \zeta^ {T} (i, t + s | t) Q \zeta (i, t + s | t) d s + \eta^ {T} R \eta \\ = \eta^ {T} \left(\int_ {0} ^ {T _ {p}} \bar {\lambda} (s) Q \bar {\lambda} ^ {T} (s) d s\right) \eta + \left(2 \eta^ {T} \int_ {0} ^ {T _ {p}} \bar {\lambda} (s) Q e ^ {A _ {e} s} d s\right) \\ \end{array}
$$

$$
\zeta (i, t) + \zeta^ {T} (i, t) \left(\int_ {0} ^ {T _ {p}} e ^ {A _ {e} ^ {T} s} Q e ^ {A _ {e} s} d s\right) \zeta (i, t) + \eta^ {T} R \eta \tag {57}
$$

Then 

$$
\begin{array}{l} \frac {\partial J}{\partial \eta} = 2 \left(\int_ {0} ^ {T _ {p}} \bar {\lambda} (s) Q \bar {\lambda} ^ {T} (s) d s + R\right) \eta \tag {58} \\ + \left(2 \int_ {0} ^ {T _ {p}} \bar {\lambda} (s) Q e ^ {A _ {e} s} d s\right) \zeta (i, t) \\ \end{array}
$$

Let $\begin{array} { r } { \frac { \partial J } { \partial \eta } = 0 } \end{array}$ , the optimal $\eta$ that minimizes $J$ is 

$$
\eta = - \Theta^ {- 1} \Psi \zeta (i, t) \tag {59}
$$

For notational simplicity, we define $\begin{array} { r } { \Theta = \int _ { 0 } ^ { T _ { p } } \ d \chi ( s ) } \end{array}$ $Q \xi ^ { T } ( s ) d s + R$ and $\begin{array} { r } { \Psi = \int _ { 0 } ^ { N _ { p } } \bar { \lambda } ( s ) Q e ^ { A _ { e } s } d s } \end{array}$ , and the minimum of Eq. (53) is $\begin{array} { r } { J _ { \operatorname* { m i n } } = \zeta ^ { T } ( i , t ) ( \int _ { 0 } ^ { T _ { p } } e ^ { A _ { e } ^ { T } s } \mathcal { Q } e ^ { A _ { e } s } } \end{array}$ $d s - \Psi ^ { T } \Theta ^ { - 1 } \Psi ) \zeta ( i , t )$ . 

The matrices $\Theta$ and $\Psi$ are constant matrices defined above. They are computed off-line. In general, it is difficult to obtain the analytical solutions for the integral expressions. However, noting that these matrices are computed over a given prediction horizon $T _ { p }$ , the 

integral expressions can be evaluated off-line using a numerical approximation scheme. More specifically, letting $\phi = 0$ , -t, 2-t, . . ., we have the approximate relations as below: 

$$
\begin{array}{l} \Theta \approx \sum_ {j = 0} ^ {K} \bar {\lambda} (j \times \Delta t) Q \bar {\lambda} ^ {T} (j \times \Delta t) \Delta t + R \tag {60} \\ \Psi \approx \sum_ {j = 0} ^ {\kappa} \bar {\lambda} (j \times \Delta t) Q e ^ {A _ {e} j \times \Delta t} \Delta t \\ \end{array}
$$

where λ $\mathbf { \nabla } ^ { T } ( j \times \Delta t )$ and ¯λT (-t) are defined as follows. 

And $K$ in the closest integer of $T _ { p } / \Delta t$ . 

$$
\begin{array}{l} \bar {\lambda} ^ {T} (j \times \Delta t) = e ^ {A _ {e} \Delta t} \bar {\lambda} ^ {T} ((j - 1) \times \Delta t) \\ + \tilde {\lambda} ^ {T} (\Delta t) e ^ {(k - 1) A _ {p} ^ {T} \Delta t} \tag {61} \\ \end{array}
$$

$$
\begin{array}{l} A \bar {\kappa} ^ {T} (\Delta t) = - \left[ B _ {e} L ^ {T} (\Delta t) \right] - e ^ {A _ {e} \Delta t} B _ {e} L ^ {T} (0) ] \\ + \tilde {\lambda} ^ {T} (\Delta t) A _ {p} ^ {T} \tag {62} \\ \end{array}
$$

Combining Eqs. (50) and (59)-(62), the update law of the control signal $u ( i , t )$ is defined as follow: 

$$
\begin{array}{l} u (i, t) = u (i, t - \Delta t) + \dot {\zeta} (i, t - \Delta t) \times \Delta t - \xi (i, t) \\ - \hat {v} (i, t) \tag {63} \\ \end{array}
$$

In Eq. (63), item $\hat { \upsilon } ( i , t )$ is obtained from the PTO to compensate for the effect of the external disturbances $\upsilon ( i , t )$ . However, a residual error always exists between $\upsilon ( i , t )$ and $\hat { \upsilon } ( i , t )$ . This residual error is integrated into the error system. Fortunately, the objective function (Eq. (53)) of LCMPC-PTO proposed in this paper could ensure the minimization of $e _ { p } ( i , t )$ . The projection function is defined as Eq. (64) to avoid the violation of constraints about velocity, whose principle is to project the velocity to the interval $0 \le v ( i , t ) \le v _ { u p p e r }$ . Through LCMPC-PTO in this paper, the estimation error $\tilde { e } _ { a } ( i , t )$ and the state error $e ( i , t )$ will converge into a set around zero. 

$$
\left\{ \begin{array}{l l} p (i, t + \Delta t) = & p (i, t) + v (i, t) \Delta t \quad i f v (i, t) = 0 o r \\ a (i, t) = & 0 \quad v (i, t) = v _ {u p p e r} \\ p (i, t + \Delta t) = & p (i, t) + v (i, t) \Delta t \\ & + \frac {a (i , t) \Delta t}{2} \quad i f v (i, t + \Delta t) = 0 \\ a (i, t) = & (0 - v (i, t)) / \Delta t \\ p (i, t + \Delta t) = & p (i, t) + v (i, t) \Delta t \\ & + \frac {a (i , t) \Delta t}{2} \quad i f v (i, t + \Delta t) = v _ {u p p e r} \\ a (i, t) = & (v _ {u p p e r} - v (i, t)) / \Delta t \\ p (i, t + \Delta t) = & p (i, t) + v (i, t) \Delta t \\ & + \frac {a (i , t) \Delta t}{2} \quad e l s e \\ a (i, t) = & a (i, t - 1) \Delta t \\ & + \dot {a} (i, t - 1) \Delta t \end{array} \right. \tag {64}
$$

To sum up, the complete algorithm of LCMPC-PTO is summarized in Algorithm 1. 

# Algorithm 1 The complete algorithm of the LCMPC-PTO.

Require: The desired states $p ^ { * } ( i , j )$ , $v ^ { * } ( i , j )$ , $a ^ { * } ( i , j )$ , the desired control signal $u ^ { * } ( i , j )$ , the parameters of PTO $\kappa _ { i , 1 }$ , $\kappa _ { i , 2 } , \kappa _ { i , 3 } , \iota _ { i } , \ell , T .$ $\kappa _ { i , 2 }$ , the parameters of LCMPC $p$ , $N$ for all $t \leq j \leq t + h \times \Delta t .$ . The system matrixes $A _ { m }$ , $B _ { m }$ , $C _ { m }$ , Ae , $B _ { e }$ and $C _ { e }$ . The weight matrix $\boldsymbol { Q }$ and $R$ . 

Ensure: $u ( i , j )$ $u ( i , j ) , t \leq j \leq t + h \times \Delta t$ 

1: Initialize the variables as follows: $\varsigma ( i , t ) = 0$ , $\zeta ( i , t ) ~ =$ $\left[ 0 \mathrm { ~ } 0 \mathrm { ~ } 0 \right] ^ { T }$ , $\hat { e } _ { a } ( i , t ) = 0$ , $\hat { \upsilon } ( i , t ) = 0$ . Compute $A _ { p }$ using Eq. (55). Compute $\Theta$ and $\Psi$ using Eq. (60)-(62). $j = t$ 

2: while $j < t + h \times \Delta t$ do 

3: Compute $\hat { \upsilon } ( i , j )$ using Eq. (45). Update the error system using Eq. (43) and $u ( i , j )$ with the projection function (Eq. (64)), then one can obtain $\zeta ( i , j )$ . Obtain $\eta$ by $\eta ~ = ~ - \Theta ^ { - 1 } \Psi \zeta ( i , j )$ , then $\dot { \varsigma } ( i , j ) = L ^ { T } ( 0 ) \eta$ . Update the control signal $u ( i , j )$ using Eq. (63). 

4: end while 

# 5 The algorithm framework

5.1 The continuation cooperative utility (CCU) model 

As shown in Fig. 1, the Velocity Regulating Area provides an additional road space for vehicles that pass the Merging Area. The HCMCC model places the emphasis on the merging problem but not the difference in vehicle density between all lanes. In this subsection, the CCU model is proposed to balance the difference in vehicle density between all lanes within the Velocity Regulating Area, which relieves the traffic congestion of Lane 1 caused by the merging problem. 

For any CAV $i$ that arrives at the Velocity Regulating Area at time t, the data set $\Theta _ { t } ^ { i }$ is built with the same process as the HCMCC model. Then one can obtain the number of vehicles in Lane $n$ as $\Xi _ { t } ^ { i } ( n , j ) , j \ =$ $t , t + \Delta t , \ldots t + h \times \Delta t .$ $\begin{array} { r } { \bar { \Xi } _ { t } ^ { i } ( n ) = \sum _ { j = t } ^ { t + h \times \Delta \bar { t } } \Xi _ { t } ^ { i } ( n , j ) / h } \end{array}$ vehi-. CAV $i$ $n$ $\bar { \Xi } _ { t } ^ { i } ( n ) > \bar { \Xi } _ { t } ^ { i } ( m )$ , that is the average number of vehicles in current lane is higher than other lanes. The feasible lane-change spaces for cut-in are obtained from $G _ { t } ^ { i }$ . The lateral lane-occupation sequence $k _ { i }$ will synchronously update according to the lane-change behaviors. The CCU model is defined as follows. 

CCU: 

$$
\min  _ {a (i, j)} \sum_ {j = t} ^ {t + h \times \Delta t} \left\{\kappa (j) \Delta t + (1 - \chi (j)) \Delta t + \left(v _ {\text {u p p e r}} - v (i, j)\right) \right\}
$$

$$
\left\{ \begin{array}{l} \kappa (j) = 1 p (i, j) \leq l _ {p m} + l _ {m a} + l _ {v r} \\ \kappa (j) = 0 p (i, j) > l _ {p m} + l _ {m a} + l _ {v r} \end{array} \right. \tag {66}
$$

$$
\chi (j) \leq 1 - \theta_ {i} (j) \tag {67}
$$

$$
\begin{array}{l} \left\{ \begin{array}{l} \theta_ {i} (j) = 1 \bar {\Xi} _ {t} ^ {i} (n) \leq \bar {\Xi} _ {t} ^ {i} (m) \\ \theta_ {i} (j) = 0 e l s e \end{array} \right. \tag {68} \\ m \neq n \\ \end{array}
$$

$$
\begin{array}{l} \left\{ \begin{array}{l l} p (i, j) \geq p (\omega , j) + s _ {0} + l _ {0} - (1 - \eta (j)) \times M \\ \hskip 2 8. 4 5 2 7 5 6 p t + \frac {(m a x (v (\omega , j) - v (i , j) , 0) \times v _ {u p p e r})}{2 | a _ {l o w e r} |} & \omega \in \Phi_ {A} ^ {i} (t) \\ p (i, j) \geq p (\omega , j) + s _ {0} + l _ {0} - (1 - \eta (j)) \times M \\ \hskip 2 8. 4 5 2 7 5 6 p t + \frac {v ^ {2} (\omega , j)}{2 | a _ {l o w e r} |} & \omega \in \Phi_ {H} ^ {i} (t) \end{array} \right. \\ \eta (j + \Delta t) = \chi (j + \Delta t) - \chi (j), \sum_ {j = t} ^ {t + h \times \Delta t} \eta (j) = 1 \\ \omega = \omega_ {l f} (i, t) o r \omega_ {r f} (i, t) \tag {69} \\ \end{array}
$$

$$
v (i, j) \leq v _ {u p p e r} ^ {\prime} + \kappa (j) \times M \tag {70}
$$

I) Vehicle kinematics constraints and constraints for car-following: Vehicle kinematics constraints are identical to those used in Eq. (5). Similarly, the constraints for car-following remain unchanged as Eq. (11). 

II) Constraints for the travel time: In Eq. (66), $\kappa ( j ) = 0$ , if CAV i has passed the Control Area. This constraint indicates the travel time of CAVs. 

III) Constraints for safety lane-change behavior: Eqs. (67)-(70) show the constraints of the safety lanechange behavior. Equation (70) restricts the velocity constraint if an additional maximum velocity limit change $( v ^ { \prime } u p p e r \neq v _ { u p p e r } )$ exists at the end of the Control Area. 

# 5.2 Modifications of the terminal conditions for different models

As described in Sect. 3.1, at the data set construction stage, CAV i keeps driving on its current lane until the terminal condition is met. Whereas vehicles in Lane 0 must perform the cooperative merging or cut-in to continue moving. Also, considering vehicles in $\Phi _ { W V } ^ { i } ( t )$ , it is inappropriate to adopt the same terminal condition for both CAVs in Lane 0 and Lane 1. 

Moreover, the CCU model in Sect. 5.1 carries out the same process to build the data set $\Theta _ { t } ^ { i }$ , the terminal condition of this model is modified as CAV i 

has passed by the Control Area. The redundant time $( t _ { r e d u n d a n t } )$ is introduced to enhance the feasibility of all proposed models. In other words, the entire control horizon length is set as the closest integer of $( t _ { t e r m i n a l } + t _ { r e d u n d a n t } ) / \Delta t$ (that is $h = i n t ( ( t _ { t e r m i n a l } +$ $t _ { r e d u n d a n t } ) / \Delta t )$ ), where $t _ { t e r m i n a l }$ is the time when CAV i meets the modified terminal condition. 

To sum up, the terminal conditions for different models are defined as follows. 

i) The HCMCC-L0 model (Sect. 3.2.3) and the SHCMCC-L0 model (Sect. 3.2.4): CAV i has entered the Merging Area and stopped. 

ii) The HCMCC-L1 model (Sect. 3.2.2): CAV i has passed the Merging Area. 

iii) The CCU model (Sect. 5.1): CAV i has passed the Control Area. 

# 5.3 The trajectory programming process

The trajectory programming for CAVs within the Control Area (the overall architecture) is executed in a decentralized way, as shown in Fig. 9. The entire framework possesses the capability of reprogramming trajectories to cope with the emergency raised by HVs who suffered from external disturbances. 

# 6 Simulation results

# 6.1 Simulation setup

A simulation of the typical merging problem under the mixed traffic scenario in Fig. 1 is applied to explore the benefits of the proposed trajectory programming algorithm. The typical merging problem in this section has two main lanes (Lane 1 and Lane 2) and one merging lane (Lane 0) with the same direction for all lanes. The Control Area is located $3 0 0 m$ downstream from the starting boundary of vehicles, wherein $l _ { o a } = 1 0 0 m$ , $l _ { p a } = 1 0 0 m$ , $l _ { m a } = 1 0 0 m$ and $l _ { v r } ~ = ~ 1 0 0 m$ . The velocity limit is $v _ { u p p e r } = 6 0 k m / h$ and an additional maximum velocity limit change is considered, that is $v _ { ~ u p p e r } ^ { \prime } = 4 0 k m / h$ at the end of the Control Area. The external disturbance is $\upsilon ( i , t ) = 1 . 5 \times s i n ( t \times \Delta t )$ . The values of the model variables and parameters are listed in Table 1. 

In the simulation, the IDM car-following of the Simulation of Urban Mobility (SUMO) with default param-


Fig. 9 The trajectory programming process for CAVs within the Control Area


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/3ee76c769ddcf41a3b3c63a3027b51fec8f0f8e45a2af9f53988e09c40e1bfca.jpg)



Table 1 The values of variables and parameters


<table><tr><td>Notation</td><td>Value</td><td>Notation</td><td>Value</td><td>Notation</td><td>Value</td></tr><tr><td>Δt</td><td>0.1</td><td>λ</td><td>0</td><td>κi,3</td><td>0.01</td></tr><tr><td>th</td><td>1.5s</td><td>τi</td><td>0.5s</td><td>p</td><td>1</td></tr><tr><td>s0</td><td>2m</td><td>μi</td><td>0.02</td><td>N</td><td>8</td></tr><tr><td>l0</td><td>5m</td><td>lcp</td><td>5m</td><td>alower</td><td>-6m/s2</td></tr><tr><td>CmaxWV</td><td>3</td><td>lcf</td><td>6m</td><td>aupper</td><td>4m/s2</td></tr><tr><td>mi</td><td>1500kg</td><td>ιi</td><td>0.15</td><td>jerklower</td><td>-3m/s3</td></tr><tr><td>Ai</td><td>2.2m2</td><td>ℓ</td><td>0.1</td><td>jerkupper</td><td>3m/s3</td></tr><tr><td>ρ</td><td>0.2kg/m3</td><td>T</td><td>2s</td><td>tredundant</td><td>4</td></tr><tr><td>Cd,i</td><td>0.35</td><td>κi,1</td><td>2</td><td></td><td></td></tr><tr><td>g</td><td>9.8m/s2</td><td>κi,2</td><td>5</td><td></td><td></td></tr></table>

eters (Pablo et al. [38]) and the CLCM are used to capture the driving behaviors of HVs. Although the car-following model is defined to capture the driving behaviors of HVs, SUMO will add randomness when executing the velocity calculated by the IDM. So, it can simulate the scenario in which HVs are also subject to external disturbances. The fundamental IDM model is given in Eq. (71). The car-following and lane-change behavior of CAV are formulated as the related constraints in the proposed HCMCC model. 

$$
\begin{array}{l} a (i, t) = a _ {u p p e r} \left[ 1 - \left(\frac {v (i , t)}{v _ {u p p e r}}\right) ^ {4} - \left(\frac {S ^ {*} (i , t)}{p (\omega , t) - p (i , t)}\right) ^ {2} \right] \\ S ^ {*} (i, t) = s _ {0} + \max  \left(0, v (i, t) t _ {h} - \frac {v (i , t) [ v (\omega , t) - v (i , t) ]}{2 \sqrt {\left| a _ {u p p e r} a _ {l o w e r} \right|}}\right) \\ \omega = \omega_ {p} (i, t) \tag {71} \\ \end{array}
$$

Three levels of traffic flow (three flow distributions in each level) are tested in the simulation. Vehicles enter the Control Area in random lanes and at random velocities. The proposed algorithms are implemented in Python. The HCMCC models are solved using Gurobi 9.0. The simulation is conducted in SUMO using two random seeds considering stochastic vehicle arrivals. Each simulation run is $1 8 0 0 s$ with a warm-up period of $6 0 s$ . 

All the CAVs execute the programmed trajectories that output from the Tactical Layer and update the related state using the built-in function of SUMO to simulate the cooperative merging maneuver. Figure 10 shows an example of the above process involving two CAVs (labeled 2.72 and 1.133). CAV 2.72 will complete the cooperative merging at time 123s with the 

assistance of CAV 1.133 (the simulation snapshot is shown in Fig. 10a). The programmed trajectories of these two CAVs are presented in Fig. 10b–d. 

# 6.2 Benefits for CAVs

To better reflect the impact of the penetration rate (PR) on the HCMCC model and its effects, we analyzed the travel time (TT) of all vehicles (defined as $T T ( i ) =$ $t _ { l e a v } ^ { i } - t _ { 0 } ^ { i }$ , where $t _ { l e a v } ^ { i }$ is the time of vehicle i leaving the Merging Area) and the actual traffic flow (ATF) of the main lane and merging lane. 

Table 2 shows the average TT of all vehicles and the ATF at $2 8 0 0 v e h / h$ . As shown in Table 2, the HCMCC model can reduce the average TT of all vehicles in all the flow distributions. The ATF of all lanes has also been improved to some extent. However, the road spaces are relatively abundant at the current traffic level. That is also the reason why the benefits of ATF do not change significantly under high PR conditions. The HCMCC model focuses on reducing the average TT of all vehicles at this traffic flow level (about $1 6 . 3 2 \% \sim 4 2 . 8 6 \%$ ). 

Table 3 shows the average TT of all vehicles and the ATF at $3 2 0 0 v e h / h$ . At this traffic flow level, the conflict between the interests of the main lane vehicles and the interests of the merging vehicles is obvious. The HCMCC model appropriately sacrifices the interests of main lane vehicles to balance the interests of all vehicles. Otherwise, the ATF of the merging lane is significantly lower than the value in the flow distribution. The ATF of the main lane will return to the orig-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/5f20eff3cf1b7ad45879fe790face936c20ac59c5c377009b6f6244bed3a3c0a.jpg)



(a） Simulation snapshot at 123 $s$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/bcb0707dd6d6d8015c56bd5742c2bcaa0be4097b085942b60e2f849bfde4af97.jpg)



(b） The programmed position trajectory


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/f871b497a8ec7da8221e703373d00946ffc619186ee9bbe254b1c0252dd79386.jpg)



(c) The programmed velocity trajectory


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/7e861b287e7190b184bbbc99ec95acbc7c7d83964cde79ef14fb0aa12611ddf4.jpg)



(d) The programmed acceleration trajectory



Fig. 10 A simulation snapshot of SUMO and the corresponding programmed inputs/states



Table 2 The average TT of all vehicles and the ATF of all lanes at 2800veh/ h


<table><tr><td rowspan="2">Flow distribution (Main/Merging)</td><td rowspan="2">Name of index</td><td colspan="5">PR</td></tr><tr><td>0</td><td>0.2</td><td>0.4</td><td>0.6</td><td>0.8</td></tr><tr><td rowspan="3">80%/20%</td><td>Average TT (s)</td><td>34.09</td><td>22.81</td><td>21.93</td><td>20.39</td><td>19.48</td></tr><tr><td>ATF of the merging lane (veh/h)</td><td>523.15</td><td>543.83</td><td>545.89</td><td>541.76</td><td>547.96</td></tr><tr><td>ATF of the main lane (veh/h)</td><td>2156.19</td><td>2179.44</td><td>2189.78</td><td>2191.84</td><td>2191.84</td></tr><tr><td rowspan="3">75%/25%</td><td>Average TT (s)</td><td>31.7</td><td>22.13</td><td>22.27</td><td>20.24</td><td>19.4</td></tr><tr><td>ATF of the merging lane (veh/h)</td><td>653.42</td><td>682.37</td><td>682.37</td><td>682.37</td><td>682.37</td></tr><tr><td>ATF of the main lane (veh/h)</td><td>2026.42</td><td>2047.1</td><td>2053.3</td><td>2053.3</td><td>2053.3</td></tr><tr><td rowspan="3">65%/35%</td><td>Average TT (s)</td><td>30.46</td><td>25.49</td><td>20.87</td><td>19.79</td><td>19.54</td></tr><tr><td>ATF of the merging lane (veh/h)</td><td>907.75</td><td>947.59</td><td>957.38</td><td>957.38</td><td>957.38</td></tr><tr><td>ATF of the main lane (veh/h)</td><td>1770.02</td><td>1779.31</td><td>1778.29</td><td>1780.36</td><td>1782.42</td></tr></table>

inal level with the increase of PR conditions, and the ATF of the merging lane also continuously increase. The total ATF of all lanes is also improved with the increase of PR conditions $( 1 0 . 2 8 \% \sim 1 2 . 1 3 \%$ when PR is 0.8).The average TT of all vehicles is significantly improved (about $7 . 7 6 \% \sim \ 4 0 . 5 3 \% )$ , which is the same as those results shown in Table 2. 

Figure 11 shows the count of CAV that performed cut-in under two traffic flow levels. This could happen to CAVs if the traffic flow of the main lane is higher 

than the merging lane. However, the count under the high PR condition (e.g., 0.8) is lower than the medium PR condition because enough CAVs exist in Lane 1 to perform the cooperative merging. In addition, the count of CAV that performed cut-in under all PR conditions remains acceptable compared to the traffic flow level. 


Table 3 The average TT of all vehicles and the ATF of all lanes at 3200veh/ h


<table><tr><td rowspan="2">Flow distribution (Main/Merging)</td><td rowspan="2">Name of index</td><td colspan="5">PR</td></tr><tr><td>0</td><td>0.2</td><td>0.4</td><td>0.6</td><td>0.8</td></tr><tr><td rowspan="3">80%/20%</td><td>Average TT (s)</td><td>69.61</td><td>57.77</td><td>51.04</td><td>48.16</td><td>41.4</td></tr><tr><td>ATF of the merging lane (veh/h)</td><td>227.46</td><td>601.72</td><td>612.06</td><td>618.27</td><td>616.2</td></tr><tr><td>ATF of the main lane (veh/h)</td><td>2448.25</td><td>2148.42</td><td>2181.5</td><td>2266.28</td><td>2384.15</td></tr><tr><td rowspan="3">75%/25%</td><td>Average TT (s)</td><td>67.33</td><td>62.1</td><td>52.68</td><td>49.13</td><td>45.98</td></tr><tr><td>ATF of the merging lane (veh/h)</td><td>378.4</td><td>696.84</td><td>767.15</td><td>771.28</td><td>773.35</td></tr><tr><td>ATF of the main lane (veh/h)</td><td>2295.23</td><td>2049.17</td><td>2032.62</td><td>2117.04</td><td>2210.45</td></tr><tr><td rowspan="3">65%/35%</td><td>Average TT (s)</td><td>67.28</td><td>67.89</td><td>59.69</td><td>51.24</td><td>44.08</td></tr><tr><td>ATF of the merging lane (veh/h)</td><td>665.82</td><td>872.6</td><td>922.23</td><td>953.25</td><td>955.31</td></tr><tr><td>ATF of the main lane (veh/h)</td><td>2009.88</td><td>1873.41</td><td>1856.86</td><td>1927.17</td><td>1995.4</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/10809d01cd9bfbea6e47335c0cc8b0bc056061226175940a83ec35573c80f797.jpg)



(a) 3200 veh/h


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/6ea808039debc44d18b832a7128b13349d2726659ba6d748c228bee1d711b232.jpg)



(b) 3600 veh/h



Fig. 11 The count of CAV that performed cut-in under two traffic flow levels


# 6.3 Impacts on the merging vehicles

To better demonstrate the proposed model’s effectiveness, the average TT of all vehicles is divided into two categories according to the main lane and the merging lane, and the corresponding average TT of each lane is shown in the following figures. Considering the fact of serious imbalance interests that manifested under the condition of PR is 0, related simulation results of PR is 0 are omitted in the following figures. 

Figure 12 presents the average TT of each lane at 2800veh/ h. As described in the above subsection, the road spaces are relatively abundant at the current traffic level, and the ATF of all lanes has also been improved. In Fig 12, the average TT of the main lane and merging 

lane both decrease with the increase of PR. It is noted that the difference between the above two average TTs is obvious under low PR conditions, especially combined with the flow distribution of $6 5 \% / 3 5 \%$ (e.g., the difference is 11.73s when PR is 0.2). This phenomenon also demonstrates the imbalance of interests between the main lane and the merging lane. However, with the increase in PR, the HCMCC model prompts the average TT of each lane to become consistent (the difference decreases to $0 . 3 4 \sim 0 . 5 1 s$ when PR is 0.8). 

Figure 13a–c shows the average TT of each lane at $3 2 0 0 v e h / h$ . The average TT of the main lane and merging lane at $3 2 0 0 v e h / h$ is much higher than values at $2 8 0 0 v e h / h$ . This indicates that the traffic condition of the Control Area changes from uncongested 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/b661ccafbbc320723f254d9877c1212492fbd85d00c450aae9d12ac802c4597d.jpg)



(a) 80%/20%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/0bcb21826aee314a946f3c385fc2ad1a586fa8a90007bbdad19041c38191d381.jpg)



(b) 75%/25%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/86a8689cc6cddc1dde10b6d079721243c6a1d5d79d20239e8158822197132cb7.jpg)



(c) 65%/35%



Fig. 12 The average TT of each lane at 2800veh/ h


to congested condition. Under the same PR condition, increasing the ratio of the merging lane in flow distribution is not conducive to improving TT. It suggests maintaining a low ratio of the merging lane in flow distribution. Otherwise, the interests of the main lane must be sacrificed, resulting in a higher value in the average TT of each lane. For example, the average TT of the main lane first increases and then decreases as the PR increases when the flow distribution is $6 5 \% / 3 5 \%$ . A similar trend appears in the average TT of each lane at 3600veh/h under the flow distribution of $7 5 \% / 2 5 \%$ (Fig. 13d–f). The congested condition at $3 6 0 0 v e h / h$ is worse than $3 2 0 0 v e h / h$ , but the HCMCC model works more effectively to balance the interests of the main lane and merging lane. 

# 6.4 Degradation experiment

In this subsection, the degradation experiment aims to discuss the assistance of CAV in Lane 2. As described in Sect. 3.2, CAV in Lane 2 creates more spaces or even performs cut-in to complete the cooperative merging under the condition of high traffic flow level but low PR. Hence, the performance of the two strategies is discussed. 

Strategy 1: The HCMCC model with all the models enabled. 

Strategy 2: The HCMCC model without the assistance of CAV in Lane 2 (the cut-in and the conditional assistance of CAVs in Lane 2 are both disabled). 

Figure 14 shows the comparison results by the index of average TT and ATF under three different PR conditions at $3 2 0 0 v e h / h$ with the flow distribution of $7 5 \% / 2 5 \%$ . The average TT of the main lane and merg-

ing lane suffer an apparent degradation if the assistance of CAV in Lane 2 is omitted. Once the assistance of CAV in Lane 2 is enabled, the improvement of the average TT for both the main lane and the merging lane is more significant, especially under the low PR condition. The benefits in the percentage of the main lane and merging lane are $3 . 0 9 \sim 8 . 6 3 \%$ and $8 . 2 1 \sim 3 1 . 4 4 \%$ . The benefit is insignificant under high PR conditions because of the sufficient number of CAVs within the Control Area $5 . 1 4 \%$ and $8 . 2 1 \%$ ). Although the ATF of the main lane only obtained slight improvement, even a degradation under low PR conditions, the improvement of the ATF for the merging lane is enough to smooth out the degradation under low PR conditions. 

# 6.5 Sensitivity analysis

# 6.5.1 Comparison with SUMO

It is noted that few suitable benchmark studies in the literature have been found to be suitable for fair comparison because existing studies focus on longitudinal vehicle trajectory planning without considering lanechange behaviors or the assistance of CAV in Lane 2. Hence, the default car-following of SUMO and the modified default lane-change model of SUMO (the LC2013 model with the perception distance parameter setting and the cooperative lane-change behavior parameter setting [38]) are used as benchmark models of CAVs in this paper. It is worth noting that the cooperative lane-change behavior of the LC2013 model is permitted within the Merging Area, which means that it does not include a mechanism for early cooperative 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/cf1fe5ce11460375f4f5ad5b46a0c750927e29c6a947676e5c9d43f13f5febb0.jpg)



(a) 80%/20%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/5f9ce74f8a7b556e84e39b11d2261a1b5b518e1f25be677db225ac8c2bc6d0f7.jpg)



(b) 75%/25%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/63b0c73c67acf04ab47b327d601a90481c93278ca69d2119022394de28c55ce6.jpg)



(c) 65%/35%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/bf55277586ab9ea1b8369581ae2bbf424394b9f8943ea0a8afaec3e852ad919c.jpg)



(d) 80%/20%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/2fdf95d795da4fb9f7ef960bca27c5eb44da92d6583b1e1c09b6a7101bde062d.jpg)



(e) 75%/25%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/c1aacb570f631591844d9d3ed78a3f797b22b1469e9a874d6fa9c5cc6cfe77fe.jpg)



(f) 65%/35%



Fig. 13 The average TT of each lane at 3200veh/ h (a), (b) and (c). The average TT of each lane at 3600veh/ h (d), (e) and (f)


lane-change behavior with main lane vehicles before entering the Merging Area. 

Figures 15 and 16 illustrate the vehicle count within the Merging Area of the SUMO and HCMCC, respectively, under a traffic flow of $3 2 0 0 v e h / h$ and PR of 0.8. The lighter the color, the more vehicles are stuck and the worse the congestion. In Fig. 15, the merging vehicles may still be unable to complete merging under such a high PR condition, although the LC2013 model enables the cooperative lane-change behavior. There always exists a certain amount of vehicles in Lane 0. The road spaces of Lane 2 are wasted because the vehicle count in Lane 2 is always less than that of Lane 1. 

In contrast, almost all the vehicles in Lane 0 complete the merging, as shown in Fig. 16. This proves the superiority of the HCMCC model. Simultaneously, the traffic pressure is well distributed into Lane 1 and Lane 2, indicating that all the road spaces of the main lane are appropriately used. This improvement is also due to the more balanced traffic flow between all lanes when using the CCU model compared to the SUMO. 

# 6.5.2 Comparison with LCMPC

To demonstrate the effectiveness of the LCMPC-PTO in executing the programmed trajectories of CAVs that output from the Tactical Layer, the trajectory tracking performance of LCMPC-PTO and LCMPC are shown in Fig. 17. It can be seen from Fig. 17 that when executing the programmed trajectories in the presence of external disturbances, the LCMPC-PTO has better performance than LCMPC. All the tracking errors shown in Fig. 17b when using LCMPC fluctuate within a distinct range, while the tracking errors of LCMPC-PTO are fainter than LCMPC. This indicates that the LCMPC-PTO eliminates the influence of external disturbances and limits all the tracking errors within an acceptable range along the time axis. Figure 17c shows the distribution of the maximum position tracking error, in which the programmed trajectories of $3 2 0 0 v e h / h$ with the flow distribution of $7 5 \% / 2 5 \%$ and PR of 0.4 are selected as the test data. The LCMPC-PTO limits the maximum position tracking error to a small scale (the average is 0.042, and the median is 0.036), while 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/6cee8804a98423f3dc53a7783797021879b3c5d41d677bffae22b1e701b6a6c1.jpg)



(a) Average TT of merging lane


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/4c06258ee18c5b5a6c6532a5d56b963607581ede9d2d03f24b643b27e9969b59.jpg)



(c) ATF of merging lane


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/c5964e76c043560e0a8dd2c6e90d28ff53750d1a021f2a3e38351f146df93c7f.jpg)



(b) Average TT of main lane


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/613f0872d4ae74c6ac12e8b42a745f0f718c833dbdef23edf163af467f197d54.jpg)



(d) ATF of main lane



Fig. 14 The comparison results of two strategies


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/bf219fe2270d75565bd111ca3509a45f66b4f2f486179c4eb6045ecfc79f8e06.jpg)



(a) 80%/20%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/8baab93c43d7b57be00a1bd9532587a91b3a3826d89b06cb50b5973c04f0c61a.jpg)



(b） 75%/25%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/2311869c2d9d1f687c614a8e05c961e3923fd76264319029856a5dfc6b7c572f.jpg)



(c) 65%/35%



Fig. 15 Vehicle count within the merging area under a traffic flow of 3200veh/ h and PR of 0.8 (SUMO)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/66fd6e4ebf91382e43cecb3385a589f428b1442512463e81af24965bd85ceb54.jpg)



(a) 80%/20%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/e8c94addbc71656a7394bfa1612198f4832ea25aee6e7c17cc6e98164d2e2d27.jpg)



(b) 75%/25%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/aaa4812c65a67271de871a6c98470384aca1e33f80c190b47251a1e083933cc7.jpg)



(c) 65%/35%



Fig. 16 Vehicle count within the merging area under a traffic flow of 3200veh/ h and PR of 0.8 (HCMCC)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/14a5772aab9cf6040f4c7432bfbf65ce4671ea074ac098f07dc44c8d5cbb730f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/c1c989b8c44d87e360ecd3d37ad9b4a191da15d8ad8cef9dfb63c84a1e522d4b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/9fa2efe56a9215f836255e1eea029407381c2bbd7ccfa4328ecd0ad1c1eb9256.jpg)



（c）



Fig. 17 Example for the comparison of the trajectory tracking performance


the distribution of LCMPC is much larger (the average is 0.849, and the median is 0.847). 

# 6.5.3 Comparison with CORMC

To further demonstrate the superiority of the proposed HCMCC model, a comparison experiment with the CORMC model proposed by Hou et al. [25] is made. Considering the preconditions are different between this paper and Hou et al. [25], additional preconditions are added as follows: 

(1) All the HVs have access to receive guide suggestions through the on-board communication unit. 

(2) The car-following model of CAV is the default model of SUMO, while the car-following model of HV is still IDM. The parameters of the above two models used in HCMCC and CORMC are the same in the following comparison experiments. However, the lane-change model of HV is the CLCM. 

(3) The simulation setup remains unchanged, as in Sect. 6.1. All CAVs’ external disturbances have been removed in order to compare with the original work by Hou et al. [25]. 

Figure 18 presents the comparison results by the index of average TT and ATF under PR condition of 0.8 at $2 8 0 0 v e h / h$ with three different flow distributions. The fluctuation in the vehicle count within the Merging Area is shown in Figs. 19 and 20. Both models have achieved the desired outcomes and balanced the interests of all vehicles. However, in comparison, the HCMCC model combined with the CCU model in Sect. 5.1 provides more road space for the merging vehicles and maintains a more balanced effect between the merging and main lane. For instance, the absolute difference of average TT is $0 . 3 4 \sim 0 . 5 2 s$ which is less than $0 . 9 5 \sim 2 . 6 1 s$ of CORMC, and the fluctuation in the vehicle count within the Merging Area is smoother than that of CORMC. Because the CORMC model mainly focuses on the interest of the merging vehi-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/b5cc41ad13f4e8f3b4f1ff6837e4531e6e4fb37c16ef47d387b2b2ede5185fed.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/d79782a7df0ccecbc39a0b0d7f90bb34b590892f81a25e6000c56113cfeee71d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/22a90d0e1c7e01d8f7d4fc2c92968d7f951d21305dd071384884212bc9f51258.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/9a32b7520167224542c514c1106028f3ea9a7fd3b7d4fa7bac272565e1a8546e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/32f834b9984181bbf73312f4301f963252e7df3e177a04639263d964304407c7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/82364d26d1a559209ac9cb0830f8603263bb66e8254876fa96f9abeb08757dab.jpg)


(d) 80%/20% 


(e) 75%/25%



(f) 65%/35%



Fig. 18 Comparison of the average TT and the ATF between HCMCC and CORMC under a traffic flow of $2 8 0 0 v e h / h$ and PR of 0.8 with different flow distributions


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/9bfb4efad20a479ce4f95aeac89d4209bdea19774969f3b1536a98cdf8006f02.jpg)



(a) 80%/20%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/7e74f8f1a03e4699acc88dd7eb91f8279ac53b2f46fcb851ee6b85811b103585.jpg)



(b） 75%/25%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/5d4fd42d0a480b5c4fdb7d2acf3bffe71cc10b6ddac72c26198fd1df343bf5ae.jpg)



(c) 65%/35%



Fig. 19 Fluctuation in vehicle count within the merging area under a traffic flow of 2800veh/ h and PR of 0.8 with different flow distributions (HCMCC)


cles, which is determined by the built-in APS (Anticipatory Position Searching) model, the CORMC model will assign a pair of cooperative vehicles (located at the main lane) for each merging vehicle and provide a unique cooperative merging case. This characteris-

tic in the CORMC model results in the traffic flow of the main lane and the merging lane becoming similar (details are shown in the related simulation results of Hou et al. [25]). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/1643f08a561f1bb5e9b1ae8ea2b8b15fe6b371da4f15b6f0adb941fad90f5b10.jpg)



(a) 80%/20%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/2def85c1017f64d7861c0f0bf36127cadc22f8a5da412d183ce63af544eb9437.jpg)



(b) 75%/25%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/06b4d189-c216-488a-8787-44598534d580/199e1c3d1e6ef004cef7f9433475fcd1ec7d14196e3263f0662c423a71a2bdac.jpg)



(c) 65%/35%



Fig. 20 Fluctuation in vehicle count within the merging area under a traffic flow of 2800veh/h and PR of 0.8 with different flow distributions (CORMC)


# 7 Conclusion

This paper proposes a HCMCC model-based decentralized framework to complete the cooperative merging for the multi-lane merging problem under the mixed traffic scenario. The multi-lane merging problem is solved in the Tactical layer using a MILP optimization model. Then, the programmed trajectories output from the Tactical layer are executed in the Operational layer using LCMPC-PTO. The entire framework possesses the capability of reprogramming trajectories to cope with the emergency raised by HVs who suffered from external disturbances. 

Numerical studies validate the decentralized framework’s advantages. The average TT of all vehicles is improved with the increase of PR conditions at all traffic flow levels and achieves the maximum improvement at $2 8 0 0 v e h / h$ (about $1 6 . 3 2 \% \sim 4 2 . 8 6 \%$ . The total ATF of all lanes can achieve an increase of $1 0 . 2 8 \% \sim 1 2 . 1 3 \%$ at $3 2 0 0 v e h / h$ and PR of 0.8. Simulation results demonstrate the imbalance of interests between the main lane and the merging lane and show the performance of the HCMCC model in balancing the interests of all vehicles. The results also suggest maintaining a low ratio of the merging lane in flow distribution. 

Degradation experiments show the benefits (in terms of average TT) of the assistance of CAV in Lane 2. Once the assistance of CAV in Lane 2 is enabled, the benefits in the percentage of the main lane and merging lane are $8 . 2 1 \sim 3 1 . 4 4 \%$ and $5 . 7 6 \sim 1 5 . 4 5 \%$ . The sensitivity analysis shows that the HCMCC model-based decentralized framework can distribute the traffic pressure well into Lane 1 and Lane 2 and appropriately use all 

the road spaces of the main lane. The LCMPC-PTO eliminates the influence of external disturbances and limits all the tracking errors within an acceptable range along the time axis. 

Acknowledgements This work was jointly supported by the National Natural Science Foundation of China under Grant No.62273063, the Fundamental Research Funds for the Central Universities under Grant 2022CDJDX-003 and the Transportation Science and Technology Program of Chongqing under Grant CQJT-2024CZ6-1. 

Funding This work was jointly supported by the National Natural Science Foundation of China under Grant No.62273063, the Fundamental Research Funds for the Central Universities under Grant 2022CDJDX-003, the Transportation Science and Technology Program of Chongqing under Grant CQJT-CZKJ2024-06 and the Science and Technology Research Program of Chongqing Municipal Education Commission under Grant No. KJQN202303423. 

Data availibility Enquiries about data availability should be directed to the authors. 

# Declarations

Conflict of interest The authors declare that there are no Conflict of interest regarding the publication of this paper. 

# References



1. Xiao, Y., Coulombel, N., Palma, A.: The valuation of travel time reliability: does congestion matter? Transp. Res. Part B: Methodol. 97, 113–141 (2017) 





2. He, Y., Liu, Z., Zhou, X., Zhong, B.: Analysis of urban traffic accidents features and correlation with traffic congestion in large-scale construction district. In: 2017 International Conference on Smart Grid and Electrical Automation (ICS-GEA), pp. 641–644 (2017) 





3. Zhu, J., Tasic, I.: Safety analysis of freeway on-ramp merging with the presence of autonomous vehicles. Accid. Anal. Prev. 152, 105966 (2021) 





4. Liu, H., Kan, X.D., Shladover, S.E., Lu, X.-Y., Ferlis, R.E.: Modeling impacts of cooperative adaptive cruise control on mixed traffic flow in multi-lane freeway facilities. Transp. Res. Part C: Emerg. Technol. 95, 261–279 (2018) 





5. Zhou, M., Qu, X., Jin, S.: On the impact of cooperative autonomous vehicles in improving freeway merging: a modified intelligent driver model-based approach. IEEE Trans. Intell. Transp. Syst. 18(6), 1422–1428 (2017) 





6. Xue, Y., Zhang, X., Cui, Z., Yu, B., Gao, K.: A platoon-based cooperative optimal control for connected autonomous vehicles at highway on-ramps under heavy traffic. Transp. Res. Part C: Emerg. Technol. 150, 104083 (2023) 





7. Chen, J., Zhou, Y., Chung, E.: An integrated approach to optimal merging sequence generation and trajectory planning of connected automated vehicles for freeway on-ramp merging sections. IEEE Trans. Intell. Transp. Syst. 25(2), 1897–1912 (2024) 





8. Tang, Z., Zhu, H., Zhang, X., Iryo-Asano, M., Nakamura, H.: A novel hierarchical cooperative merging control model of connected and automated vehicles featuring flexible merging positions in system optimization. Transp. Res. Part C: Emerg. Technol. 138, 103650 (2022) 





9. Chen, N., Arem, B., Alkim, T., Wang, M.: A hierarchical model-based optimization control approach for cooperative merging by connected automated vehicles. IEEE Trans. Intell. Transp. Syst. 22(12), 7712–7725 (2021) 





10. Xue, Y., Ding, C., Yu, B., Wang, W.: A platoon-based hierarchical merging control for on-ramp vehicles under connected environment. IEEE Trans. Intell. Transp. Syst. 23(11), 21821–21832 (2022) 





11. Scholte, W.J., Zegelaar, P.W.A., Nijmeijer, H.: A control strategy for merging a single vehicle into a platoon at highway on-ramps. Transp. Res. Part C: Emerg. Technol. 136, 103511 (2022) 





12. Chen, T., Wang, M., Gong, S., Zhou, Y., Ran, B.: Connected and automated vehicle distributed control for on-ramp merging scenario: a virtual rotation approach. Transp. Res. Part C: Emerg. Technol. 133, 103451 (2021) 





13. Li, S., Zhou, Y., Ye, X., Jiang, J., Wang, M.: Sequencingenabled hierarchical cooperative cav on-ramp merging control with enhanced stability and feasibility. IEEE Trans. Intell. Veh. (2024). https://doi.org/10.1109/TIV. 2024.3409381 





14. Hu, X., Sun, J.: Trajectory optimization of connected and autonomous vehicles at a multilane freeway merging area. Transp. Res. Part C: Emerg. Technol. 101, 111–125 (2019) 





15. Karbalaieali, S., Osman, O.A., Ishak, S.: A dynamic adaptive algorithm for merging into platoons in connected automated environments. IEEE Trans. Intell. Transp. Syst. 21(10), 4111–4122 (2020) 





16. Liu, J., Zhao, W., Xu, C.: An efficient on-ramp merging strategy for connected and automated vehicles in multi-lane traffic. IEEE Trans. Intell. Transp. Syst. 23(6), 5056–5067 (2022) 





17. Chen, N., Arem, B., Wang, M.: Hierarchical optimal maneuver planning and trajectory control at on-ramps with multiple mainstream lanes. IEEE Trans. Intell. Transp. Syst. 23(10), 18889–18902 (2022) 





18. Gao, Z., Wu, Z., Hao, W., Long, K., Byon, Y.-J., Long, K.: Optimal trajectory planning of connected and automated vehicles at on-ramp merging area. IEEE Trans. Intell. Transp. Syst. 23(8), 12675–12687 (2022) 





19. Wei, C., He, Y., Tian, H., Lv, Y.: Game theoretic merging behavior control for autonomous vehicle at highway on-ramp. IEEE Trans. Intell. Transp. Syst. 23(11), 21127– 21136 (2022) 





20. Mu, C., Du, L., Zhao, X.: Event triggered rolling horizon based systematical trajectory planning for merging platoons at mainline-ramp intersection. Transp. Res. Part C: Emerg. Technol. 125, 103006 (2021) 





21. Jiang, Y., Man, Z., Wang, Y., Yao, Z.: Cooperative lanechanging for connected autonomous vehicles merging into dedicated lanes in mixed traffic flow. Expert Syst. Appl. 252, 124163 (2024) 





22. Sun, Z., Huang, T., Zhang, P.: Cooperative decision-making for mixed traffic: a ramp merging example. Transp. Res. Part C: Emerg. Technol. 120, 102764 (2020) 





23. Liu, H., Zhuang, W., Yin, G., Li, Z., Cao, D.: Safety-critical and flexible cooperative on-ramp merging control of connected and automated vehicles in mixed traffic. IEEE Trans. Intell. Transp. Syst. 24(3), 2920–2934 (2023) 





24. Shi, J., Li, K., Chen, C., Kong, W., Luo, Y.: Cooperative merging strategy in mixed traffic based on optimal final-state phase diagram with flexible highway merging points. IEEE Trans. Intell. Transp. Syst. 24(10), 11185–11197 (2023) 





25. Hou, K., Zheng, F., Liu, X., Guo, G.: Cooperative onramp merging control model for mixed traffic on multi-lane freeways. IEEE Trans. Intell. Transp. Syst. 24(10), 10774– 10790 (2023) 





26. Liu, K., Li, N., Tseng, H.E., Kolmanovsky, I., Girard, A.: Interaction-aware trajectory prediction and planning for autonomous vehicles in forced merge scenarios. IEEE Trans. Intell. Transp. Syst. 24(1), 474–488 (2023) 





27. Hang, P., Lv, C., Huang, C., Xing, Y., Hu, Z.: Cooperative decision making of connected automated vehicles at multi-lane merging zone: a coalitional game approach. IEEE Trans. Intell. Transp. Syst. 23(4), 3829–3841 (2022) 





28. Shi, Y., Wang, Z., Wang, C., Shao, Y.: Pseudospectral convex optimization for on-ramp merging control of connected vehicles. J. Franklin Inst. 360(15), 10972–10999 (2023) 





29. Wang, L.: Model predictive control system design and implementation using MATLAB, (2009) 





30. Jeong, D., Choi, S.B.: Tracking control based on model predictive control using laguerre functions with pole optimization. IEEE Trans. Intell. Transp. Syst. 23(11), 20652–20663 (2022) 





31. Saeed, J., Wang, L., Fernando, N.: Model predictive control of phase shift full-bridge dc-dc converter using laguerre functions. IEEE Trans. Control Syst. Technol. 30(2), 819– 826 (2022) 





32. Wang, L., Freeman, C.T., Rogers, E., Young, P.C.: Disturbance observer-based repetitive control system with nonminimal state-space realization and experimental evaluation. IEEE Trans. Control Syst. Technol. 31(2), 961–968 (2023) 





33. Wang, W., Yan, J., Wang, H., Ge, H., Zhu, Z., Yang, G.: Adaptive mpc trajectory tracking for auv based on laguerre function. Ocean Eng. 261, 111870 (2022) 





34. Treiber, M., Hennecke, A., Helbing, D.: Congested traffic states in empirical observations and microscopic simulations. Phys. Rev. E 62(2), 1805 (2000) 





35. Talebpour, A., Mahmassani, H.S.: Influence of connected and autonomous vehicles on traffic flow stability and throughput. Transp. Res. Part C: Emerg. Technol. 71, 143– 163 (2016) 





36. Guo, G., Yang, D., Zhang, R.: Distributed trajectory optimization and platooning of vehicles to guarantee smooth traffic flow. IEEE Trans. Intell. Veh. 8(1), 684–695 (2023) 





37. Wang, Y., Song, Y., Hill, D.J., Krstic, M.: Prescribed-time consensus and containment control of networked multiagent systems. IEEE Trans. Cybern. 49(4), 1138–1147 (2019) 





38. Lopez, P.A., Behrisch, M., Bieker-Walz, L., Erdmann, J., Flötteröd, Y.-P., Hilbrich, R., Lücken, L., Rummel, J., Wagner, P., Wiessner, E.: Microscopic traffic simulation using sumo. In: 2018 21st International Conference on Intelligent Transportation Systems (ITSC), pp. 2575–2582 (2018) 



Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law. 