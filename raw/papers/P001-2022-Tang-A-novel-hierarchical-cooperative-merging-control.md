# A novel hierarchical cooperative merging control model of connected and automated vehicles featuring flexible merging positions in system optimization

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/793b7f14f77b6e1c990f912acee2d200e2fa204b9678688c91accbfed36a3ddb.jpg)


Zhixian Tang, Hong Zhu*, Xin Zhang, Miho Iryo-Asano, Hideki Nakamura 

Department of Environmental Engineering and Architecture, Graduate School of Environmental Studies, Nagoya University, Nagoya 464-8603, Japan 

# ARTICLEINFO

Keywords: 

Connected and automated vehicle 

Merging bottleneck 

System optimal cooperative merging control 

Flexible merging positions 

Monte Carlo tree search 

# ABSTRACT

Merging sections on freeways are typical bottlenecks for traffic efficiency and safety. The connected and automated vehicles (CAV) technology has great capability in improving traffic performance of merging bottlenecks. Current approaches of system optimal cooperative merging control assume single fixed merging point (CMC-SMP) for on-ramp vehicles to reduce the complexity of their models. Non-fixed merging positions have the potential to further improve merging operations but may lead to the computational explosion. To solve this core contradiction, this study proposes a novel hierarchical system optimal cooperative merging control model considering flexible merging positions (CMC-FMP) to realize safe and efficient merging processes. The upper-level - the tactical planning model is formulated as a non-convex mixed integer quadratically constrained programming, aiming at minimal total travel time in the control zone. It optimizes not only the merging sequence but also vehicles' critical states in merging processes, such as the state of on-ramp vehicles when they merge. The lower-level - the motion planning model generates feasible trajectories and the next step actions for every vehicle. A Monte Carlo Tree Search-based decomposition algorithm (MCTS-DA) is further designed to improve the computational efficiency of the tactical planning model. Meanwhile, solutions of MCTS-DA are proved to have good optimality compared to the direct solving method. A batch-based scheme is developed to realize real-time control. The results reveal that the average delays of CMC-FMP are remarkably lower than those of CMC-SMP. Especially in low on-ramp ratio scenarios, the difference in improvement can reach $64\%$ . Furthermore, the sensitivity analysis indicates that large safe merging margins and short merging sections are disadvantageous for traffic efficiency for the merging flow controlled by CMC-FMP. 

# 1. Introduction

The merging section is the area where the on-ramp is connected with the mainline. In this section, the on-ramp vehicle accelerates and merges into the freeway mainline flow. However, the merging section is a typical bottleneck of traffic efficiency and safety. On the one hand, the information of surrounding vehicles that drivers can observe is limited. Therefore, in the merging section, the 

E-mail addresses: tang.zhixian@f.mbox.nagoya-u.ac.jp (Z. Tang), zhu.hong@a.mbox.nagoya-u.ac.jp (H. Zhu), zhang@genv.nagoya-u.ac.jp 

(X. Zhang), iryo@nagoya-u.jp (M. Iryo-Asano), nakamura@genv.nagoya-u.ac.jp (H. Nakamura). 

competitive nature of drivers makes them act to satisfy their own demands (Sun et al., 2014), which may do harm to the global traffic efficiency of the merging area. On the other hand, the unpredictable behavior of drivers may have negative impacts on traffic safety, especially at merging bottlenecks with high merging frequency (Qin et al., 2018) and when the speed difference between mainline and on-ramp is large (Kockelman et al., 2007; Li et al., 2013). Therefore, unorganized behaviors are the main reason for the majority of traffic problems at merging bottlenecks. 

With the development of wireless communication and autonomous driving, Connected Automated Vehicles (CAVs) technology renders new opportunities for traffic operation (Milanés et al., 2010; Li et al., 2014). CAVs at merging bottlenecks can exchange information with the control center through Vehicle-to-Infrastructure (V2I) communication (Wang et al., 2014). Only the vehicles within a certain control range are able to be coordinated. By using the shared vehicle information, the control center designs the trajectories for vehicles based on a certain algorithm. Therefore, CAVs can accomplish complicated merging tasks and the traffic operation at merging bottlenecks can be improved (Mahmassani, 2016). Different models of merging strategies have been proposed to facilitate smooth and efficient merging (Wang et al., 2013; Zhou et al., 2019). The state of art is the system optimal cooperative merging control (SO-CMC) which solves the trajectories and merging sequence based on optimization programming considering one or more performance indicators for all vehicles in the control zone (Letter and Elefteriadou, 2017; Mu et al., 2021). 

In the merging bottlenecks, the merging section serves as not only the acceleration lane but also the place where on-ramp vehicles complete merging. For human-driven vehicles (HDVs), on-ramp HDVs can complete merging at any proper position in the merging section. Several empirical studies proved that extending the merging section can remarkably improve the traffic performance in merging bottlenecks (Li and Zhang, 2000; Zhi et al., 2009; Wang et al., 2007). Because longer merging sections can provide more acceleration distance and merging positions for on-ramp HDVs. Similarly, a merging section with enough length and flexible merging positions for on-ramp CAVs in the SO-CMC will bring more possibilities to improve the traffic performance in the merging bottleneck. However, most of the current SO-CMC models have a common critical shortcoming: on-ramp vehicles are required to merge at single fixed merging point for achieving concise model structures (Letter and Elefteriadou, 2017; Mu et al., 2021). Some other studies simply applied non-fixed merging positions in the lower-level of trajectory planning models which only include 2 or 3 involved vehicles. Those choices of merging positions will not benefit global traffic optimization (Cao et al., 2013; Chen et al., 2021a). Obviously, such an unrealistic setting limits the solution space and results in the underutilization of the merging section. Eventually, it may lead to the inappropriate cooperating maneuver of on-ramp vehicles, which brings disadvantageous effects on traffic performance such as increasing delay of on-ramp vehicles and excessive interference on the mainline vehicles. 

Meanwhile, recent studies applying reinforcement learning (RL) achieved noticeable performance in lane-changing related topics. Wang et al. (2021) established an RL-based cooperative lane-changing model that generates discrete lane-changing decisions instead of controlling whole longitudinal trajectories. Their approach could remarkably promote traffic efficiency under either congestion or free-flow conditions compared to competitive strategies. Dong et al. (2020) proposed a multi-agent cooperative control framework through deep RL that outputs discrete lane-changing decisions for CAVs in a mixed flow environment. Their approaches enhanced communication and cooperation between CAVs using graphic convolutional network-based information fusion blocks assuming a limited sensing condition. Ren et al. (2020) proposed an RL-based cooperative lane-changing controller. The model could optimize the motion of merging vehicles by controlling their longitudinal trajectories. Results indicated that the controller has better mobility and safety performance than human drivers in merging at work zones. Hou and Graf (2021) constructed a decentralized multi-agent cooperative lane-changing controller at freeway weaving areas by applying an RL of proximal policy optimization. Multiple targets such as efficiency and emission have been considered by incorporating different weighted evaluation indexes into the reward function. This approach leads to outstanding improvement in those considered optimal targets compared to human drivers. The RL-based controllers could address non-fixed lane-changing positions with smaller computation resources than direct methods such as system optimization. In the above RL-based approaches, predefined function approximators (neural networks) were requested to learn good driving strategies through numerous training episodes. Model builders could hardly know whether the convergent results were locally optimal, globally optimal, or nonoptimal. In this regard, a SO-CMC model considering flexible merging positions is urgently demanded to provide benchmarks. Meanwhile, RL-based approaches may need millions of episodes and excessive training time before achieving an acceptable result because they may be trapped in searching for solutions in an unreasonable area. The SO-CMC model can also be incorporated into designing reward functions for achieving fast convergences. 

Therefore, this paper aims to establish a SO-CMC model considering flexible merging positions in system optimization (CMC-FMP for short) to achieve safe and efficient traffic operation at merging bottlenecks. Such an improvement will inevitably increase complexity of the models' variables, structure, and constraints, which may lead to a computational explosion that contradicts the requirement of online control. Therefore, a more effective model structure is necessary for accommodating new variables and complex constraints. A specific solving algorithm that can realize efficient execution and ensure the solutions' optimality is required as well. In addition, the study site focuses on the modeling for a merging bottleneck intersected by a single-lane freeway mainline and a single-lane on-ramp. It should also be noted that the study emphasizes the model's new structure and performance improvement brought about by flexible merging positions, which is interpreted through numerical studies assuming pure CAVs conditions. Considering the above issues, the main originality and contributions can be summarized as follows: 

- A novel hierarchical model is proposed to generate optimal merging strategies considering flexible merging positions for on-ramp vehicles, which includes an upper-level of tactical planning model to solve the optimal merging sequence and critical states; and a lower-level of motion planning model to determine the trajectories and next step actions. 

- A Monte Carlo Tree Search-based decomposition algorithm (MCTS-DA) is developed that solves the complicated tactical planning model with high computational efficiency and good optimality. 

- The performance of the proposed model is compared with the conventional cooperative merging control with single fixed merging point (CMC-SMP) by simulation, to interpret the significance of flexible merging positions. 

This paper is structured as follows: Section 2 reviews previous literature about SO-CMC and points out the research gap. Section 3 describes the basic problem and introduces models of CMC-FMP. Section 4 provides the detailed procedure of MCTS-DA. Furthermore, the performances of CMC-FMP and CMC-SMP are compared in Section 5. Their merits and shortcomings are pointed out through simulation experiments. The characteristics of the CMC-FMP are discussed through sensitivity analysis in the same section as well. Finally, Section 6 summarizes the conclusions, limitations, and future work. 

# 2. Literature review

Researchers have been developing the merging control for CAVs over the past decades. Some studies mainly focus on the method of providing safe gaps for the merging of on-ramp vehicles by adjusting the position and the length of the gap between mainline vehicles. For instance, Ran et al. (1999) developed a mainline gap consolidation scheme to accommodate on-ramp vehicles cooperatively, with mainline priority. Davis (2006) established a cooperative merging procedure based on a modified optimal velocity model to prevent the transition of mainline traffic from free flow to synchronous flow. Cao et al. (2013, 2015) proposed a model predictive control (MPC)-based cooperative merging algorithm that optimizes CAVs' merging trajectories in the merging section. Duret et al. (2020) proposed a hierarchical approach that controls automated truck platoons near merge points to create new equilibrium gaps for merging vehicles. The tactical-layer model generates decisions about optimized vehicle sequences, new gaps, and starting time of the gap creation process. The operational-layer model computes the optimal truck accelerations. Zhou et al. (2019) proposed an optimal control-based trajectory planning under congested traffic, with the objective of minimizing the merging influence of on-ramp vehicles on following mainline vehicles. The above methodologies only consider the merging of one on-ramp vehicle and a few relevant mainline vehicles near and in the merging region. They generate safe and smooth merging trajectories for only a few vehicles and attempt to relieve the negative impact of merging on mainline flow. However, the system optimal solutions are always expected, which is achieved by optimizing all vehicles in the system. Therefore, recently, several studies have been committed to filling this gap by SO-CMC. To minimize the engine effort and passenger's discomfort during merging, Ntousakis et al. (2016) built a nonlinear optimization model for trajectories of all CAVs and applied the MPC within an assumed control zone at the merging area. Some scholars optimized the motions of multiple CAVs to maximize the vehicles' speed (Letter and Elefteriadou, 2017; Xie et al., 2017). The trajectories are constrained by safe merging requirements such as acceptable space headway or minimum gaps at every time step. Karimi et al. (2020) extended the merging control to mixed traffic environments. They developed control algorithms to cooperate CAV trajectory for different types of merging triplets (the combination of CAVs and HDVs in different merging roles). The algorithms are realized through an improved MPC scheme considering the uncertainties of HDVs. While the studies above assume the merging section with only one-lane mainline roads, Hu and Sun (2019) focused on multilane freeway merging. They proposed a trajectory optimization model in which CAVs in the mainline are controlled to do cooperative lane changing before the merging region in order to create more acceptable space for on-ramp vehicles. 

Current SO-CMC methodologies can generate the optimal trajectories for multiple vehicles but have some simplifications for the convenience of the model establishment and solving. One of the most prominent research limitations is assuming a fixed merging point for on-ramp vehicles, which may limit the solution space and impact the model's performance. To the best of our knowledge, this limitation has not been solved well yet, which indicates the importance of this paper. 

However, considering flexible merging positions for on-ramp vehicles will remarkably increase models' complexity, leading to an excessively long computation time. The computational complexity of SO-CMC is mainly contributed by two tasks: solving the merging sequence, and motion planning. Among them, solving the merging sequence is the most time-consuming procedure (Mu et al., 2021), which may expand the computation time with factorial magnification as the number of involved vehicles increases. Solving the optimal merging sequence by a well-designed algorithm can maintain a good performance without computational explosion (Mu et al., 2021). For this reason, the algorithms of merging sequence in current SO-CMC are reviewed in detail. The existing approaches of merging sequences strategies in SO-CMC studies can be classified into two categories (Jing et al., 2019): the rule-based method which determines the sequence through explicit rules, and the optimal-based method which gives the sequence solved by optimization considering one or more performance indicators. 

The rule-based methods include virtual mapping, the first-in-first-out method, and others. They can quickly generate the merging sequence but cannot guarantee its optimality on traffic performance. According to Rios-Torres and Malikopoulos (2016), the virtual mapping method is to compare the path lengths of each vehicle to an assumed fixed merging point and the vehicle closer to the merging point will be assigned an earlier sequence. The first-in-first-out method has a similar principle to the virtual mapping method. The merging sequences will be established based on the expected time of each vehicle entering the defined control zone (Rios-Torres and Malikopoulos, 2016). The vehicle that will enter the control zone earlier will be assigned the prior sequence to depart. The first-in-first-out method was widely applied in several SO-CMC models (e.g., Letter and Elefteriadou, 2017; Hu and Sun, 2019). The rule-based algorithm proposed by Ding et al. (2020) assumed that the minimum safety headway in the merging zone for vehicles from different roads (on-ramp and mainline) is larger than vehicles on the same road. Therefore, their sequence algorithm is to cluster the arrival time of vehicles in the same lane as much as possible. However, the assumed vehicles' trajectories are simplified too much, which limits the usage of the model in complex situations such as the high degree of saturation. 

The optimal-based methods evaluate the future merging process exhaustively with all sequences, which is a very time-consuming process. Therefore, an optimal-based method is always accompanied by a simplified solution algorithm. Chen et al. (2021a) put 

forward a hierarchical model-based optimization control approach in which the merging sequence is solved by mixed integer quadratic programming problems. However, their suggested enumeration algorithm had difficulty in getting optimal solutions in an acceptable time. Sun et al. (2020) proposed a bi-level optimization program for determining the merging sequences and vehicles' trajectories. The computational complexity of the algorithm is simplified by using a multi-stage optimization, which means controls of some vehicles are relaxed at some stages and only trajectories of the other vehicles are optimized. However, this kind of decomposition scheme may influence optimality, but it is not discussed in their paper. Mu et al. (2021) developed an event-triggered rolling horizon based systematical trajectory planning by mixed integer nonlinear programs. A heuristic algorithm named multi-step increasingly approximating algorithm (MIA) is established for solving the program efficiently. But it only searches the solution near the sequence of first-in-first-out, which may have a poor performance in some situations such as when mainline and on-ramp flows are extremely high and unbalanced. 

In summary, the core contradiction of the SO-CMC is between computational complexity brought by improving model ability and the simplification required for quick solving. To achieve real-time CAV control and good traffic performance, a merging sequence algorithm with a short computation time and low optimization gap is always desired. 

# 3. Methodology

# 3.1. Problem description and model framework

# 3.1.1. Problem description and assumptions

This study focuses on optimizing the merging process at the freeway merging bottleneck. A merging bottleneck intersected by a single-lane freeway mainline and a single-lane on-ramp is assumed to be the study site, as illustrated in Fig. 1. Out of safety concerns, the speed limit of the on-ramp lane is lower than the mainline and merging section. Once on-ramp vehicles enter the merging section, they are allowed to accelerate, and are provided suitable opportunities to enter the mainline. The control center is located at the entrance of the merging section transmitting data with CAVs bi-directionally without communication delay and loss. The control center is in charge of the information collection and control of all the vehicles within the control zone. Vehicles strictly follow the trajectories planned by the control center. For simplification, all vehicles are assumed to be homogeneous in length and dynamic performance. Also, only longitudinal vehicle kinematics is considered. Therefore, the key problem of this study is to provide safe and smooth longitudinal trajectory planning for both on-ramp and mainline vehicles aiming at optimal global traffic efficiency of all vehicles in the control zone, while considering flexible merging position for on-ramp vehicles. 

# 3.1.2. Model framework

The proposed CMC-FMP is a hierarchical model including an upper-level of tactical planning model and a lower-level of motion planning model. The tactical planning model is to solve the optimal merging sequence and critical states for maximizing the efficiency of all vehicles within the control zone which is formulated as a non-convex mixed integer quadratically constrained programming (non-convex MIQCP). The solution of the tactical planning model serves as the input for motion planning. Then, the lower-level of the motion planning model concatenates all optimized critical states to generate trajectory plan for each vehicle following the optimized merging sequence. The optimal control model (Yu et al., 2018) and a modified Newell's car-following model provide solutions for motion planning under constraints of vehicle dynamics and safety requirements. 

The planned trajectory of each vehicle contains several points of vehicle states that are defined as vectors of time, speed, and 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/58d20ab04b46f24156fd274292be2e5c6794526e2e583d88e65e8b8e65e31ff5.jpg)



Fig. 1. Illustration of the merging bottleneck.



Table 1


Notations. 

<table><tr><td>Notation</td><td>Explanation</td></tr><tr><td colspan="2">1. Notations in the tactical planning model (section 3.3)</td></tr><tr><td colspan="2">1.1 General notations</td></tr><tr><td>Nm</td><td>The number of mainline vehicles in the control zone at to.</td></tr><tr><td>Nr</td><td>The number of on-ramp vehicles in the control zone at to.</td></tr><tr><td>k</td><td>The index of mainline vehicles, including a virtual mainline vehicle (Nm+1).</td></tr><tr><td></td><td>Also, the index of the gap before the mainline vehicle k.</td></tr><tr><td></td><td>k=1,2,...,Nm,Nm+1.</td></tr><tr><td>k'</td><td>The index of on-ramp vehicles, including a virtual on-ramp vehicle (Nm+Nf+2). K' = Nm+2, Nm+3, ..., Nm+Nf+1, Nm+Nf+2.</td></tr><tr><td>Ω</td><td>The set of mainline vehicles at to.</td></tr><tr><td>Ωd</td><td>The set of mainline vehicles which are downstream of the end of the merging section at to, Ωd⊆Ω.</td></tr><tr><td>Ωv</td><td>The set of mainline vehicles and the virtual mainline vehicle at to, Ωv = Ω ∪ {Nm+1}.</td></tr><tr><td>Ωam</td><td>The set of on-ramp vehicles which are approaching the merging section at to.</td></tr><tr><td>Ωim</td><td>The set of on-ramp vehicles that are in the merging section at to.</td></tr><tr><td>Ω'</td><td>The set of on-ramp vehicles at to, Ω' = Ωam + Ωim.</td></tr><tr><td>Ωv'</td><td>The set of on-ramp vehicles and the virtual on-ramp vehicle at to, Ωv' = Ω' ∪ {Nm+Nf+2}.</td></tr><tr><td colspan="2">1.2 Parameters</td></tr><tr><td>t0</td><td>Current time, 0 (s).</td></tr><tr><td>lms</td><td>The start position of the merging section (m).</td></tr><tr><td>lme</td><td>The end position of the merging section (m).</td></tr><tr><td>lss</td><td>The start position of the control zone (m).</td></tr><tr><td>lze</td><td>The end position of the control zone (m).</td></tr><tr><td>Δt</td><td>The step size for updating vehicle states (s).</td></tr><tr><td>τ</td><td>The time displacement in Newell's car-following model (s).</td></tr><tr><td>d</td><td>The space displacement in Newell's car-following model (m).</td></tr><tr><td>L</td><td>The vehicles' length (m).</td></tr><tr><td>β</td><td>Extra time headway for the safe merging (s).</td></tr><tr><td>(t0, y0', x0')</td><td>The current state of the on-ramp vehicle k'.</td></tr><tr><td>(t0, y0', x0')</td><td>The current state of the mainline vehicle k.</td></tr><tr><td>k'ms</td><td>The optimized tm's in the last step (s).</td></tr><tr><td>v'ms</td><td>The optimized vms in the last step (m/s).</td></tr><tr><td>νmax</td><td>The maximal speed limits of mainline and merging section (vmax) or on-ramp (vmax) (m/s).</td></tr><tr><td>νmin</td><td>The minimal speed limit (m/s).</td></tr><tr><td>a max</td><td>The upper bound of vehicles' acceleration (m/s2).</td></tr><tr><td>a min</td><td>The lower bound of vehicles' acceleration (m/s2).</td></tr><tr><td>n</td><td>The number of time segments of the feasible path.</td></tr><tr><td>M</td><td>A large positive number</td></tr><tr><td colspan="2">1.3 Variables for merging sequence (section 3.3.1)</td></tr><tr><td>g'k</td><td>The gap that is assigned to on-ramp vehicle k', g' = 1,2,...,Nm+1</td></tr><tr><td>δk,k</td><td>=1, if g' = k (i.e., k' merges into the gap k)</td></tr><tr><td></td><td>=0, o.w.</td></tr><tr><td>η'k</td><td>=0, if g''m+2 &gt; k (i.e., no on-ramp vehicle merges before the vehicle k)</td></tr><tr><td></td><td>=1, o.w.</td></tr><tr><td>ρk,k</td><td>=1, if k' is the last one in vehicles that merge into the gap k, if any (i.e., k' is the direct platoon leader of k)</td></tr><tr><td></td><td>=0, o.w.</td></tr><tr><td>ρk,k</td><td>=1, if k' is the first one in vehicles that merge into the gap k+1, if any (i.e., k' is the direct platoon follower of k)</td></tr><tr><td></td><td>=0, o.w.</td></tr><tr><td>σk,k</td><td>=1, if no on-ramp vehicle merges into the gap k (i.e., vehicle k has no direct platoon leader), and k' is the last one in vehicles that merge before the vehicle k (i.e., k' is the indirect platoon leader of k)</td></tr><tr><td></td><td>=0, o.w.</td></tr><tr><td>σk,k</td><td>=1, if no on-ramp vehicle merges into the gap k+1 (i.e., vehicle k has no direct platoon follower), and k' is the first one in vehicles that merge after the vehicle k (i.e., k' is the indirect platoon follower of k)</td></tr><tr><td></td><td>=0, o.w.</td></tr><tr><td colspan="2">1.4 Variables for critical states (section 3.3.2)</td></tr><tr><td>(tmsk', vmsk')</td><td>The time (s) and speed (m/s) when on-ramp vehicle k' arrives at lms.</td></tr><tr><td>(tmsk', vmsk', xmsk')</td><td>The time (s), speed (m/s) and position (m) when on-ramp vehicle k' merges into mainline.</td></tr><tr><td>(tsek', vtek')</td><td>The time (s) and speed (m/s) when on-ramp vehicle k' arrives at lse.</td></tr><tr><td>(tk', vk', xk')</td><td>The time (s), speed (m/s) and position (m) of mainline vehicle k when its platoon leader on-ramp vehicle merges.</td></tr><tr><td>(tk', vk', xk')</td><td>The time (s), speed (m/s) and position (m) of mainline vehicle k when its platoon follower on-ramp vehicle merges.</td></tr><tr><td>(tsek', vtek')</td><td>The time (s) and speed (m/s) when mainline vehicle k arrives at lte.</td></tr><tr><td>μ'k</td><td>=1, if t'k-1 &gt;tkms, (i.e., in a certain period, on-ramp vehicles k' and k' -1 will coexist in the merging section.)</td></tr><tr><td></td><td>=0, o.w.</td></tr><tr><td>λk</td><td>=1, if t'k &gt;tkse, (i.e., for mainline vehicle k, the cut-in time of its on-ramp follower is later than its leaving time from the control zone.)</td></tr><tr><td></td><td>=0, o.w.</td></tr><tr><td>vi</td><td>The speed at the end of time segment i.</td></tr><tr><td>(tkf, vkf, xkf)</td><td>The former state between (tk, vk, xk) and (tkz, vkz, lze).</td></tr><tr><td>(tkl, vkl, xkl)</td><td>The latter state between (tk, vk, xk) and (tkz, vkz, lze).</td></tr><tr><td colspan="2">2. Notations in the motion planning model (section 3.4)</td></tr><tr><td>S</td><td>The ordered set for merging sequence.</td></tr><tr><td>kms</td><td>The index of the vehicle order in the merging sequence.</td></tr><tr><td>a(t)</td><td>The variable of the optimal control model, the acceleration at time t.</td></tr><tr><td>v(t)</td><td>The variable of the optimal control model, the speed at time t.</td></tr><tr><td>x(t)</td><td>The variable of the optimal control model, the position at time t.</td></tr><tr><td>vkms</td><td>The next step speed of the kmsth vehicle in the merging sequence.</td></tr><tr><td>xkms</td><td>The next step position of the kmsth vehicle in the merging sequence.</td></tr><tr><td>vkpre</td><td>The next step speed of the preceding vehicle for the vehicle being solved.</td></tr><tr><td>xpre</td><td>The next step position of the preceding vehicle for the vehicle being solved.</td></tr><tr><td>aemergency</td><td>The emergency braking acceleration.</td></tr></table>

position, i.e., (time, speed, position). The flexibility of merging positions brings great complexities (e.g., quadratic constraint and nonconvex) to formulating the programming among multi-states of on-ramp and mainline vehicles. Directly solving the whole trajectory for all vehicles in one optimization is extremely time-consuming for this problem. However, only at some specific points of time or position, the vehicle states are significant to the model results and important for pinning trajectories, such as when 1) on-ramp vehicles are entering the merging section, 2) on-ramp vehicles are conducting merging, 3) the mainline platoon is being cut in by on-ramp vehicles, and 4) mainline and on-ramp vehicles leave the communication zone. The vehicle states in such movements are classified as critical states. The complete trajectory plan for a vehicle can be obtained by connecting all critical states. 

# 3.2. Notations

Please refer to Table 1 for the notations of the proposed CMC-FMP. 

# 3.3. Tactical planning model

The tactical planning model optimizes the merging sequence and critical states aiming at minimizing the total travel time. The total travel time is defined as the sum of the expected time for each vehicle to leave the control zone. It should be noted that the current time $t_0$ is always defined as zero for facilitating calculations. Therefore, the travel time for each vehicle equals the value of the time when it leaves the control zone (i.e., $t_{ze}^k$ for mainline vehicles and $t_{ze}^{k'}$ for on-ramp vehicles). The tactical planning model is formulated as a nonconvex MIQCP and the objective function is shown in Equation (1). 

$$
\min  \sum_ {k \in \Omega} t _ {z e} ^ {k} + \sum_ {k \in \Omega} t _ {z e} ^ {k ^ {\prime}} \tag {1}
$$

# s.t. Equations (2) to (37).

Furthermore, in section 3.3.1, the constraints for feasible merging sequences are established. In section 3.3.2, the constraints for safe and feasible critical states are introduced. 

# 3.3.1. Merging sequence

In this model, the merging sequence is determined by the assigned gap in the mainline platoon for each on-ramp vehicle as in Fig. 1. First of all, on-ramp vehicles can only choose the gaps that are upstream of the end of the merging section as in Equation (2). 

$$
\left| \Omega_ {d} \right| + 1 \leq g ^ {k ^ {\prime}} \leq N ^ {m} + 1, \forall k ^ {\prime} \in \Omega_ {v} ^ {\prime} \tag {2}
$$

Noteworthy that a stopping virtual mainline vehicle $k = N^m + 1$ is assumed to define the gap after the last mainline vehicle in the control zone. For facilitating the definition of the follower of mainline platoon, a stopping virtual on-ramp vehicle $k' = N^m + N^r + 2$ is assumed which will always be assigned to the last gap $N^m + 1$ as in Equation (3). 

$$
g ^ {N ^ {m} + N ^ {r} + 2} = N ^ {m} + 1 \tag {3}
$$

Since only a one-lane on-ramp is assumed for the study site, overtaking of on-ramp vehicles in the merging section is impossible. Therefore, this study further assumes that the gap assigned for each on-ramp vehicle should not precede the one chosen by its preceding vehicles as in Equation (4). 

$$
g ^ {k ^ {\prime}} \geq g ^ {k ^ {\prime} - 1}, \forall k ^ {\prime} \in \Omega_ {v} ^ {\prime}; k ^ {\prime} - 1 \in \Omega_ {v} ^ {\prime} \tag {4}
$$

It should be noted that Equation (4) is defined only for current on-ramp vehicles. Once an on-ramp vehicle finishes merging, it will be classified as a mainline vehicle in the next step. Then the following on-ramp vehicle is allowed to choose the gap ahead of it. Therefore, it is possible for the on-ramp vehicles to leave the merging section earlier than those on-ramp vehicles at front positions in 

terms of the final effect. 

Equations (5a) and (5b) define the equivalence between $\delta_{k,k}$ and $g^{k}$ . All on-ramp vehicles should and can only be assigned one gap. 

$$
k - M \left(1 - \delta_ {k, k}\right) \leq g ^ {k ^ {\prime}} \leq k + M \left(1 - \delta_ {k, k}\right), \forall k \in \Omega_ {v}; \forall k ^ {\prime} \in \Omega_ {v} ^ {*} \tag {5a}
$$

$$
\sum_ {k \in \Omega_ {v}} \delta_ {\vec {k}, k} = 1, \forall \vec {k} ^ {\prime} \in \Omega_ {v} ^ {\prime} \tag {5b}
$$

The merging process can be considered as consecutive mainline flow being separated as multiple platoons by several merging vehicles. For the convenience of determining critical states (which will be introduced in section 3.3.2), all mainline vehicles between two consecutive on-ramp vehicles (if any) in the merging sequence are defined as a separated mainline platoon. Fig. 2(a) shows the basic case of a separated mainline platoon. Then, for each separated mainline platoon, the next on-ramp vehicle assigned after the mainline platoon is named as the platoon follower and the first on-ramp vehicle ahead of the platoon is named as the platoon leader. It is noteworthy that only on-ramp vehicles can be platoon leaders/followers and all the mainline vehicles in a separated mainline platoon share the same platoon leader/follower. 

However, there may be some special cases as in Fig. 2(b). If no on-ramp vehicle merges into the gap $N^m + 1$ , the virtual on-ramp vehicle will be the platoon follower. Meanwhile, if no on-ramp vehicle merges into gap 1, there will be no platoon leader on-ramp vehicle for the first separated mainline platoon. A variable $\widehat{\eta}^k$ is defined to tell whether mainline vehicle $k$ has a platoon leader. If the first on-ramp vehicle $N^m + 2$ is assigned to the gap after mainline vehicle $k$ ( $\widehat{\eta}^k = 0$ ), mainline vehicle $k$ does not have a platoon leader. 

$$
k - M \widehat {\eta} ^ {k} <   g ^ {N ^ {m} + 2} \leq k + M \left(1 - \widehat {\eta} ^ {k}\right) \forall k \in \Omega \tag {6}
$$

Furthermore, only the first and last mainline vehicles in each separated mainline platoon will be directly influenced by on-ramp vehicles. For this sake, the platoon leader for the first mainline vehicle in a separated mainline platoon is called the direct platoon leader, and the platoon follower for the last mainline vehicle in a separated mainline platoon is called the direct platoon follower. For mainline vehicles in other positions of the separated mainline platoon, their platoon leaders/followers are called the indirect platoon leaders /followers. A series of variables $(\widehat{\rho}_{k,k},\widehat{\sigma}_{k,k},\overline{\rho}_{k,k},$ and $\overline{\sigma}_{k,k})$ are defined. $\widehat{\rho}_{k,k} = 1$ $(\overline{\rho}_{k,k} = 1)$ indicates that on-ramp vehicle $k^{\prime}$ is the direct platoon leader (follower) for mainline vehicle $k$ . On the contrary, $\widehat{\sigma}_{k,k} = 1$ $(\overline{\sigma}_{k,k} = 1)$ indicates that on-ramp vehicle $k^{\prime}$ is the indirect platoon leader (follower) of mainline vehicle $k$ . Noteworthy that there may be only one mainline vehicle in a separated mainline platoon. Then, it should interact with the merging behaviors of both the platoon follower and leader on-ramp vehicle simultaneously. In addition, if only one on-ramp vehicle is assigned to a gap, it will perform as both the platoon follower of its preceding platoon and the platoon leader of its following platoon. Equations (7a)-(7d) are constraint equations for $\widehat{\rho}_{k,k}$ ; Equations (8a)-(8d) are constraint equations for $\widehat{\sigma}_{k,k}$ ; Equations (9a)-(9d) are constraint equations for $\overline{\rho}_{k,k}$ ; and Equations (10a)-(10d) are constraint equations for $\overline{\sigma}_{k,k}$ . 

Equations for $\widehat{\rho}_{k,k}$ (Equations (7a)-(7d)) and $\widehat{\sigma}_{k,k}$ (Equations (8a)-(8d)) are interpreted as examples. As for $\widehat{\rho}_{k,k}$ , if the on-ramp vehicle $k'$ is the direct leader of the mainline vehicle $k$ (i.e. $\widehat{\rho}_{k,k} = 1$ ), firstly, the on-ramp vehicle $k'$ should select the gap $k$ (i.e., $g^{k'} = k$ ) (Equations (7a) and (7b)); Secondly, the on-ramp vehicle $k' + 1$ should be assigned to the gap after the mainline vehicle $k$ (Equation (7c)). Thirdly, at least one on-ramp vehicle is assigned to gap $k$ (Equation (7d)). Regarding $\widehat{\sigma}_{k,k}$ , firstly, if the on-ramp vehicle $k'$ is the indirect platoon leader of the mainline vehicle $k$ (i.e. $\widehat{\sigma}_{k,k} = 1$ ), the gap selected by on-ramp vehicle $k'$ should be 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/54a5e2411e3a3347e1812357198333cd25d7150f47f274a628f1b47c8174567c.jpg)



(a) Basic case


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/d0f453f4b5893cf53cad70e723c5ebbdcef48dd1ed7cbb2cbd97aceffb23e439.jpg)



(b) Special cases



Fig. 2. Definitions of the separated mainline platoon, follower, and leader.


no later than gap $k - 1$ (Equation (8a)), and the gap selected by on-ramp vehicle $k' + 1$ should be no earlier than gap $k + 1$ (Equation (8b)); Secondly, mainline vehicle $k$ must have an indirect or direct platoon leader (Equations (7d), (8c) and (8d)), except when mainline vehicle $k$ is in the first separated mainline platoon (Equation (8c)), as described in Fig. 2(b). 

$$
\widehat {\rho} _ {k ^ {\prime}, k} \leq 1 + \left(g ^ {k ^ {\prime}} - k\right) / M, \forall k \in \Omega ; \forall k ^ {\prime} \in \Omega_ {v} ^ {\prime} \tag {7a}
$$

$$
\widehat {\rho} _ {k ^ {\prime}, k} \leq 1 - \left(g ^ {k ^ {\prime}} - k\right) / M, \forall k \in \Omega ; \forall k ^ {\prime} \in \Omega_ {v} ^ {\prime} \tag {7b}
$$

$$
\widehat {\rho} _ {k ^ {\prime}, k} \leq 1 + \left(g ^ {k ^ {\prime} + 1} - k - 1\right) / M, \forall k \in \Omega ; \forall k ^ {\prime} \in \Omega_ {v} ^ {*} \tag {7c}
$$

$$
\sum_ {k ^ {\prime} \in \Omega_ {v} ^ {\prime}} \hat {\rho} _ {k ^ {\prime}, k} \geq \sum_ {k ^ {\prime} \in \Omega_ {v} ^ {\prime}} \delta_ {k ^ {\prime}, k} / M, \forall k \in \Omega \tag {7d}
$$

$$
\widehat {\sigma} _ {k ^ {\prime}, k} \leq 1 - \left(g ^ {k ^ {\prime}} - k + 1\right) / M, \forall k \in \Omega ; \forall k ^ {\prime} \in \Omega_ {v} ^ {\prime} \tag {8a}
$$

$$
\widehat {\sigma} _ {k ^ {\prime}, k} \leq 1 + \left(g ^ {k ^ {\prime} + 1} - k - 1\right) / M, \forall k \in \Omega ; \forall k ^ {\prime} \in \Omega_ {v} ^ {*} \tag {8b}
$$

$$
\sum_ {k ^ {\prime} \in \Omega_ {v} ^ {*}} \widehat {\sigma} _ {k ^ {\prime}, k} \geq \widehat {\eta} ^ {k} - M \sum_ {k ^ {\prime} \in \Omega_ {v} ^ {*}} \delta_ {k ^ {\prime}, k}, \forall k \in \Omega \tag {8c}
$$

$$
\sum_ {k ^ {\prime} \in \Omega_ {v} ^ {\prime}} \widehat {\sigma} _ {k ^ {\prime}, k} \leq 1 - \sum_ {k ^ {\prime} \in \Omega_ {v} ^ {\prime}} \delta_ {k ^ {\prime}, k} / M, \forall k \in \Omega \tag {8d}
$$

$$
\bar {\rho} _ {k ^ {\prime}, k} \leq 1 + \left(g ^ {k ^ {\prime}} - k - 1\right) / M, \forall k \in \Omega ; \forall k ^ {\prime} \in \Omega_ {v} ^ {\prime} \tag {9a}
$$

$$
\bar {\rho} _ {k ^ {\prime}, k} \leq 1 - \left(g ^ {k ^ {\prime}} - k - 1\right) / M, \forall k \in \Omega ; \forall k ^ {\prime} \in \Omega_ {v} ^ {\prime} \tag {9b}
$$

$$
\bar {\rho} _ {k ^ {\prime}, k} \leq 1 - \left(g ^ {k ^ {\prime} - 1} - k\right) / M, \forall k \in \Omega ; \forall k ^ {\prime} \in \Omega_ {v} ^ {\prime} \tag {9c}
$$

$$
\sum_ {k ^ {\prime} \in \Omega_ {v} ^ {*}} \bar {\rho} _ {k ^ {\prime}, k} \geq \sum_ {k ^ {\prime} \in \Omega_ {v} ^ {*}} \delta_ {k ^ {\prime}, k + 1} / M, \forall k \in \Omega \tag {9d}
$$

$$
\bar {\sigma} _ {k ^ {\prime}, k} \leq 1 + \left(g ^ {k ^ {\prime}} - k - 2\right) / M, \forall k \in \Omega ; \forall k ^ {\prime} \in \Omega_ {v} ^ {\prime} \tag {10a}
$$

$$
\bar {\sigma} _ {k ^ {\prime}, k} \leq 1 - \left(g ^ {k ^ {\prime} - 1} - k\right) / M, \forall k \in \Omega ; \forall k ^ {\prime} \in \Omega_ {v} ^ {\prime} \tag {10b}
$$

$$
\sum_ {k ^ {\prime} \in \Omega_ {v}} \bar {\sigma} _ {k ^ {\prime}, k} \geq 1 - M \sum_ {k ^ {\prime} \in \Omega_ {v}} \delta_ {k ^ {\prime}, k + 1}, \forall k \in \Omega \tag {10c}
$$

$$
\sum_ {k ^ {\prime} \in \Omega_ {v} ^ {*}} \bar {\sigma} _ {k ^ {\prime}, k} \leq 1 - \sum_ {k ^ {\prime} \in \Omega_ {v} ^ {*}} \delta_ {k ^ {\prime}, k + 1} / M, \forall k \in \Omega \tag {10d}
$$

# 3.3.2. Critical states

The vehicle states when the on-ramp vehicle enters the merging section $(t_{ms}^{k},\nu_{ms}^{k},l_{ms})$ (entering state), when it merges $(t_m^k,\nu_m^k,x_m^k)$ (merging state), and when it leaves the control zone $(t_{ze}^{k},\nu_{ze}^{k},l_{ze})$ (leaving state) are defined as the critical states for each on-ramp vehicle. Meanwhile, the vehicle states when the mainline vehicle leaves the control zone $(t_{ze}^{k},\nu_{ze}^{k},l_{ze})$ (leaving state), when its leader on-ramp vehicle merges $(\vec{t}^k,\hat{\nu}^k,\hat{x}^k)$ (cut-by-leader state), and when its on-ramp follower merges $(\vec{t}^k,\vec{\nu}^k,\vec{x}^k)$ (cut-by-follower state) are selected as the critical states for each mainline vehicle. In order to ensure the obtained critical states are safe and feasible, their solution space should be limited by car-following constraints, merging constraints, and feasible path constraints. 

# - Car-following constraints

The car-following constraints are established below to ensure vehicles' critical states can maintain a safe headway to their preceding vehicle. The Newell's car-following model (Newell et al., 2002) is applied to formulate the safe time and space headway between two continuous vehicles. Equations (11) and (13) are car-following constraints for critical states of on-ramp vehicles. Equation (14) is for mainline vehicles. Equations (15) and (16) are constraints between mainline vehicle and on-ramp vehicles at $l_{ze}$ . Fig. 3 

displays an example showing the positions where these car-following constraints are applied. 

For entering states, on-ramp vehicles are required to keep a safe time headway with their preceding vehicle as in Equation (11). 

$$
t _ {m s} ^ {k} \geq t _ {m s} ^ {k - 1} + \tau + (d + L) / v _ {m s} ^ {k}, \forall k ^ {\prime} \in \Omega_ {a m} ^ {\prime}; k ^ {\prime} - 1 \in \Omega^ {\prime} \tag {11}
$$

On-ramp vehicles that are in the merging section will still maintain an entering state. Its value will be assigned referring to the last-step solution as shown in Equation (12). 

$$
\left(t _ {m s} ^ {k ^ {\prime}}, v _ {m s} ^ {k ^ {\prime}}, l _ {m s}\right) = \left(\widetilde {t} _ {m s} ^ {k ^ {\prime}} - \Delta t, \widetilde {v} _ {m s} ^ {k ^ {\prime}}, l _ {m s}\right), \forall k ^ {\prime} \in \Omega_ {i m} ^ {\prime} \tag {12}
$$

For leaving states, Equation (13) explains the safe time headway between on-ramp vehicles and Equation (14) is the safe time headway constraint between mainline vehicles. Meanwhile, at the end of the control zone $(l_{ze})$ , on-ramp vehicles will have finished merging and mixed with mainline vehicles. Therefore, safe time headways between mainline vehicles and on-ramp vehicles are guaranteed through Equations (15) and (16). 

$$
t _ {z e} ^ {k} \geq t _ {z e} ^ {k - 1} + \tau + (d + L) / v _ {z e} ^ {k}, \forall k ^ {\prime} \in \Omega^ {\prime}; k ^ {\prime} - 1 \in \Omega^ {\prime} \tag {13}
$$

$$
t _ {z e} ^ {k} \geq t _ {z e} ^ {k - 1} + \tau + (d + L) / v _ {z e} ^ {k}, \forall k \in \Omega ; k - 1 \in \Omega \tag {14}
$$

$$
t _ {z e} ^ {k} \geq t _ {z e} ^ {k} + \tau + (d + L) / v _ {z e} ^ {k} - M \left(1 - \delta_ {k ^ {\prime}, k + 1}\right), \forall k ^ {\prime} \in \Omega^ {\prime}; \forall k \in \Omega \tag {15}
$$

$$
t _ {z e} ^ {k} \geq t _ {z e} ^ {k} + \tau + (d + L) / v _ {z e} ^ {k} - M \left(1 - \delta_ {k ^ {\prime}, k}\right), \forall k ^ {\prime} \in \Omega ; \forall k \in \Omega \tag {16}
$$

- Merging constraints 

Merging process is defined based on two assumptions. 

Assumption 1. The merging time of on-ramp vehicle $k^{\prime}$ should not be earlier than the one of its preceding on-ramp vehicle $k^{\prime} - 1$ as in Equation (17). 

$$
t _ {m} ^ {k ^ {\prime} - 1} \leq t _ {m} ^ {k ^ {\prime}}; \forall k ^ {\prime} \in \Omega_ {v} ^ {*}; k ^ {\prime} - 1 \in \Omega_ {v} ^ {*} \tag {17}
$$

Assumption 2. If two continuous on-ramp vehicles will be/are in the merging section at the same, and are assigned to merge into the same gap, they are required to merge at the same time, as in Equation (18). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/9e5441a6b072ae262ed22f06f38cd4847e34858ecc04b7558519b4f8e5033157.jpg)



Fig. 3. An example for car-following constraints and merging constraints.


$$
- M \left(1 - \mu^ {k ^ {\prime}}\right) - M \left(g ^ {k ^ {\prime}} - g ^ {k ^ {\prime} - 1}\right) \leq t _ {m} ^ {k ^ {\prime}} - t _ {m} ^ {k ^ {\prime} - 1} \leq M \left(1 - \mu^ {k ^ {\prime}}\right) + M \left(g ^ {k ^ {\prime}} - g ^ {k ^ {\prime} - 1}\right), \forall k ^ {\prime} \in \Omega^ {\prime}; k ^ {\prime} - 1 \in \Omega^ {\prime} \tag {18}
$$

Merging constraints ensure the safety and feasibility of the merging. Same as the majority of other CMC researches (e.g. Letter and Elefteriadou, 2017; Hu and Sun, 2019), this model does not consider the lateral motion of on-ramp vehicles during merging. Instead, it is assumed that once the merging is executed, the on-ramp vehicle will instantly shift from the merging section to the equivalent projection position on the mainline. This assumption also means that the on-ramp vehicle switches the car-following target from the preceding on-ramp vehicle to a mainline vehicle immediately. Meanwhile, the upcoming mainline vehicle shifts the car-following target from the preceding mainline vehicle to the on-ramp vehicle that cuts in. 

However, considering the complicated operations of on-ramp vehicles during the lane changing, the merging process needs more safety margin time than the car-following process (Ding et al., 2020). Therefore, $\beta$ is introduced as an extra time headway for the safe merging that is attached to the car-following headway as in Equations (19) and (20). These two Equations take effect only between on-ramp vehicles and mainline vehicles that are directly influenced by the merging (i.e., $\widehat{\rho}_{k,k} = 1$ or $\overline{\rho}_{k,k} = 1$ ). Fig. 3 displays the positions where these two merging constraints are applied. 

$$
x _ {m} ^ {k ^ {\prime}} - \widehat {x} ^ {k} \geq d + L + (\tau + \beta) \widehat {v} ^ {k} - M \left(1 - \widehat {\rho} _ {k ^ {\prime}, k}\right), \forall k \in \Omega ; k ^ {\prime} \in \Omega^ {*} \tag {19}
$$

$$
\bar {x} ^ {k} - x _ {m} ^ {k ^ {\prime}} \geq d + L + (\tau + \beta) \nu_ {m} ^ {k ^ {\prime}} - M (1 - \bar {\rho} _ {k ^ {\prime}, k}), \forall k \in \Omega ; k ^ {\prime} \in \Omega^ {\prime} \tag {20}
$$

Meanwhile, Equations (21) and (22) define the boundary of merging time and position. 

$$
t _ {m s} ^ {k ^ {\prime}} \leq t _ {m} ^ {k ^ {\prime}}, \forall k ^ {\prime} \in \Omega^ {*} \tag {21}
$$

$$
l _ {m e} \geq x _ {m} ^ {k ^ {\prime}} \geq l _ {m s}, \forall k ^ {\prime} \in \Omega^ {\prime} \tag {22}
$$

For merging states, the first thing is to confirm whether the on-ramp vehicles $k'$ and $k' - 1$ will coexist in the merging section by a variable $\mu^{k'}$ , as in Equation (23). 

$$
M \mu^ {k ^ {\prime}} \geq t _ {m} ^ {k ^ {\prime} - 1} - t _ {m s} ^ {k ^ {\prime}} > M \left(\mu^ {k ^ {\prime}} - 1\right), \forall k ^ {\prime} \in \Omega^ {\prime}; k ^ {\prime} - 1 \in \Omega^ {\prime} \tag {23}
$$

Then, Equation (24) ensures the safe distance headway for on-ramp vehicles $k'$ and $k' - 1$ when vehicle $k'$ merges. However, if $\mu^k = 0$ (i.e., vehicles $k'$ and $k' - 1$ will not coexist in the merging section), this constraint will be relaxed. If they are assigned to different gaps (i.e., $g^{k} > g^{k-1}$ ), they will be driven away from each other, therefore, this constraint will be relaxed as well. 

$$
x _ {m} ^ {k ^ {\prime} - 1} - x _ {m} ^ {k ^ {\prime}} \geq d + L + \tau v _ {m} ^ {k ^ {\prime}} - M \left(1 - \mu^ {k ^ {\prime}}\right) - M \left(g ^ {k ^ {\prime}} - g ^ {k ^ {\prime} - 1}\right), \forall k ^ {\prime} \in \Omega^ {\prime}; k ^ {\prime} - 1 \in \Omega^ {\prime} \tag {24}
$$

For cut-by-leader and cut-by-follower states, Equations (25) and (26) are established to find the merging time of the on-ramp leader, $\hat{t}^k$ , and follower, $\hat{t}^k$ , for mainline vehicle $k$ . In some special cases as in Fig. 2 (b), the first several mainline vehicles may not have a leader (i.e., $\sum_{k\in \Omega}\widehat{\rho}_{k,k} + \widehat{\sigma}_{k,k} = 0$ ). The $\hat{t}^k$ of those vehicles is 0. 

$$
\widehat {t} ^ {k} = \sum_ {\mathrm {k} ^ {\prime} \in \Omega} \widehat {\rho} _ {\mathrm {k} ^ {\prime}, \mathrm {k}} \cdot \mathbf {t} _ {\mathrm {m}} ^ {\mathrm {k} ^ {\prime}} + \sum_ {\mathrm {k} ^ {\prime} \in \Omega^ {\prime}} \widehat {\sigma} _ {\mathrm {k} ^ {\prime}, \mathrm {k}} \cdot \mathbf {t} _ {\mathrm {m}} ^ {\mathrm {k} ^ {\prime}}, \forall \mathrm {k} \in \Omega \tag {25}
$$

$$
\vec {t} ^ {k} = \sum_ {\vec {k} \in \Omega} \bar {\rho} _ {\vec {k} ^ {\prime}, k} \cdot t _ {m} ^ {k ^ {\prime}} + \sum_ {k ^ {\prime} \in \Omega} \bar {\sigma} _ {k ^ {\prime}, k} \cdot t _ {m} ^ {k ^ {\prime}}, \forall k \in \Omega \tag {26}
$$

When the leader and follower of the mainline vehicle merge, the safe space headway is only applied between those mainline vehicles in the same separated mainline platoon as in Equations (27) and (28). The relationship between the leader/follower and the first/last mainline vehicle in the platoon has been defined by Equations (19) and (20). 

$$
\widehat {x} ^ {k - 1} \geq \widehat {x} ^ {k} + d + L + \tau \widehat {\nu} ^ {k} - M \sum_ {k ^ {\prime} \in \Omega^ {\prime}} \delta_ {k ^ {\prime}, k}, \forall k \in \Omega ; k - 1 \in \Omega \tag {27}
$$

$$
\bar {x} ^ {k} \geq \bar {x} ^ {k + 1} + d + L + \tau v ^ {k + 1} - M \sum_ {k \in \Omega} \delta_ {k, k + 1}, \forall k \in \Omega ; k + 1 \in \Omega \tag {28}
$$

- Feasible path constraints 

The feasible path here is not the final trajectory. It is a reference path that is defined to guarantee the feasibility of vehicle dynamics between two adjacent states including critical states and the current states. The current states refer to vehicles states at time $t_0 = 0$ , i.e., $(t_0, \nu_0^k, x_0^k)$ for on-ramp vehicles and $(t_0, \nu_0^k, x_0^k)$ for mainline vehicles. Meanwhile, the feasible paths limit the solution space for the critical states so that the motion planning model can always get feasible trajectories with these regulated critical states as inputs. The feasible path is formulated by a discrete approximate quadrature approach as illustrated in Fig. 4. 

From the former state $(t_f, \nu_f, x_f)$ to the latter state $(t_l, \nu_l, x_l)$ , the time is discretized into $n$ segments evenly (in this study, $n = 3$ ), assuming constant acceleration in each segment. $\nu_i$ stands for the speed at the end of segments $i$ , starting from $\nu_0$ which equals the speed in the former state (Equation (29)), and ending with $\nu_n$ which equals the speed in the latter state (Equation (30)). The distance between $x_l$ and $x_f$ equals the area sum of all slices (Equation (31)). Meanwhile, vehicle dynamics consider the upper and lower bounds for speed and acceleration as in Equations (32) and (33). 

$$
v _ {0} = v _ {f} \tag {29}
$$

$$
v _ {n} = v _ {l} \tag {30}
$$

$$
x _ {l} - x _ {f} = \left(t _ {l} - t _ {f}\right) \left(v _ {0} + v _ {n} + 2 \sum_ {i = 1} ^ {n - 1} v _ {i}\right) / 2 n \tag {31}
$$

$$
v _ {\min } \leq v _ {i} \leq v _ {\max }, i = 0, 1, \dots , n \tag {32}
$$

$$
a _ {\min } \leq n \left(v _ {i + 1} - v _ {i}\right) / \left(t _ {l} - t _ {f}\right) \leq a _ {\max }, i = 0, 1, \dots , n - 1 \tag {33}
$$

Equations (29)-(33) are denoted as Equation (34). 

$$
d \left(t _ {f}, v _ {f}, x _ {f}, t _ {l}, v _ {l}, x _ {l}\right) \leq 0 \tag {34}
$$

For applying Equation (34), the former and the latter state in two adjacent states should be identified. Whereas, the time sequences of other states are fixed, except between $(\vec{t}^k,\vec{\nu}^k,\vec{x}^k)$ and $(t_{ze}^{k},\nu_{ze}^{k},l_{ze})$ . Therefore, a binary variable $\lambda_{k}$ is defined to compare $t_{ze}^{k}$ and $\vec{t}^k$ as in Equation (35). 

$$
M \left(1 - \lambda_ {k}\right) > t _ {z e} ^ {k} - \bar {t} ^ {k} \geq - M \lambda_ {k}, \forall k \in \Omega \tag {35}
$$

As in Equations (36a)-(36f), if $\vec{t}^k \leq t_{ze}^k$ (i.e., $\lambda_k = 0$ ), the former state $\left(t_f^k, \nu_f^k, x_f^k\right)$ will be $(\vec{t}^k, \vec{\nu}^k, \vec{x}^k)$ and the latter state $\left(t_l^k, \nu_l^k, x_l^k\right)$ will be $(t_{ze}^k, \nu_{ze}^k, l_{ze})$ , and vice versa. 

$$
t _ {f} ^ {k} = \left(1 - \lambda_ {k}\right) \tilde {t} ^ {k} + \lambda_ {k} t _ {z e} ^ {k} \tag {36a}
$$

$$
v _ {f} ^ {k} = (1 - \lambda_ {k}) \bar {v} ^ {k} + \lambda_ {k} v _ {z e} ^ {k} \tag {36b}
$$

$$
x _ {f} ^ {k} = \left(1 - \lambda_ {k}\right) \overline {{x}} ^ {k} + \lambda_ {k} l _ {z e} \tag {36c}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/ebaf7089b3d88c25e317e3f71529a628480a6b0984b0e88c4e71b9c06471a243.jpg)



Fig. 4. Discrete approximate quadrature approach for the feasible path.


$$
t _ {l} ^ {k} = \lambda_ {k} \bar {t} ^ {k} + (1 - \lambda_ {k}) t _ {z e} ^ {k} \tag {36d}
$$

$$
\nu_ {l} ^ {k} = \lambda_ {k} \bar {\nu} ^ {k} + (1 - \lambda_ {k}) \nu_ {z e} ^ {k} \tag {36e}
$$

$$
x _ {l} ^ {k} = \lambda_ {k} \bar {x} ^ {k} + (1 - \lambda_ {k}) l _ {z e} \tag {36f}
$$

Then, Equation (34) can be applied to each pair of adjacent states as in Equations (37a)-(37g). An example in Fig. 5 explains feasible paths and the corresponding constraint equations. 

$$
d \left(t _ {0}, v _ {0} ^ {k}, x _ {0} ^ {k}, \hat {t} ^ {k}, \hat {v} ^ {k}, \hat {x} ^ {k}\right) \leq 0, \forall k \in \Omega \tag {37a}
$$

$$
d \left(\widehat {t} ^ {k}, \widehat {v} ^ {k}, \widehat {x} ^ {k}, t _ {f} ^ {k}, v _ {f} ^ {k}, x _ {f} ^ {k}\right) \leq 0, \forall k \in \Omega \tag {37b}
$$

$$
d \left(t _ {f} ^ {k}, v _ {f} ^ {k}, x _ {f} ^ {k}, t _ {l} ^ {k}, v _ {l} ^ {k}, x _ {l} ^ {k}\right) \leq 0, \forall k \in \Omega \tag {37c}
$$

$$
d \left(t _ {0}, v _ {0} ^ {k}, x _ {0} ^ {k}, t _ {m s} ^ {k}, v _ {m s} ^ {k}, l _ {m s}\right) \leq 0, \forall k ^ {\prime} \in \Omega_ {a m} ^ {*} \tag {37d}
$$

$$
d \left(t _ {m s} ^ {k}, v _ {m s} ^ {k}, l _ {m s}, t _ {m} ^ {k}, v _ {m} ^ {k}, x _ {m} ^ {k}\right) \leq 0, \forall k ^ {*} \in \Omega_ {a m} ^ {*} \tag {37e}
$$

$$
d \left(t _ {0}, v _ {0} ^ {k}, x _ {0} ^ {k}, t _ {m} ^ {k}, v _ {m} ^ {k}, x _ {m} ^ {k}\right) \leq 0, \forall k ^ {\prime} \in \Omega_ {i m} ^ {\prime} \tag {37f}
$$

$$
d \left(t _ {m} ^ {k}, v _ {m} ^ {k}, x _ {m} ^ {k}, t _ {z e} ^ {k}, v _ {z e} ^ {k}, l _ {z e}\right) \leq 0, \forall k ^ {\prime} \in \Omega^ {\prime} \tag {37g}
$$

# 3.4. Motion planning model

In this section, the procedure to update the next step states is introduced. Given the optimized gaps assigned to each on-ramp vehicle, the optimized merging sequence is formulated as an ordered set $S$ and $k_{ms}$ is the index of the vehicle order in the merging sequence, i.e., $S(k_{ms}) = k \in \Omega$ or $k' \in \Omega'$ . The next step state of each vehicle will be updated sequentially following the merging sequence as shown in the flow chart in Fig. 6. In this procedure, two trajectory models are introduced: 1) the optimal control model, which aims to connect the given critical states and current states with trajectories that have minimum speed fluctuation, without considering the safe space requirement; 2) the modified Newell's car-following model, which provides dynamically feasible, efficient, and safe next step car following speed behind the preceding vehicle. However, it cannot guarantee that the vehicle will reach the critical states that are optimized by the tactical planning model. Therefore, the output of the optimal control model is given priority and will be considered first. However, in rare cases, the next step state from the optimal control model may violate the safe headway requirement. In these special cases, the modified Newell's car-following model will be activated. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/43ec8571a5cac55dd154c50acae35b93949975bc9e88d5e91f02a0972474d922.jpg)



Fig. 5. Typical example: feasible path constraints.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/7210fad0a93c4acb1c1e28a24547cd80efb7e1b18d38531f0bfdfb3a7ddb0c6b.jpg)



Fig. 6. The flow chart of the motion planning model.


# 3.4.1. Optimal control model

The optimal control model (Yu et al., 2018) is formulated in Equations (38)-(45). The upper-level tactical planning model provides the optimized critical states for each vehicle. The current state and critical states compose the state set for a vehicle. Each pair of two adjacent states (i.e., the start state $(t_{st},\nu_{st},x_{st})$ and the ending state $(t_{ed},\nu_{ed},x_{ed})$ ) from the state set serves as the input of the optimal control model. The optimal control model aims at connecting the state pair using trajectory with minimal speed fluctuation, which approximates fuel consumption minimization. This study applies the analytical solution method of Yu et al. (2018) to solve this model which is detailed in Appendix A. 

$$
\min  \int_ {t _ {s t}} ^ {t _ {e d}} | a (t) | d t \tag {38}
$$

s.t. 

$$
\left\{ \begin{array}{l} d x (t) / d t = v (t) \\ d v (t) / d t = a (t) \end{array} \right. \tag {39}
$$

$$
x \left(t _ {s t}\right) = x _ {s t} \tag {40}
$$

$$
x \left(t _ {e d}\right) = x _ {e d} \tag {41}
$$

$$
v \left(t _ {s t}\right) = v _ {s t} \tag {42}
$$

$$
v \left(t _ {e d}\right) = v _ {e d} \tag {43}
$$

$$
v _ {\text {m i n}} \leq v (t) \leq v _ {\text {m a x}} \tag {44}
$$

$$
a _ {\min } \leq a (t) \leq a _ {\max } \tag {45}
$$

Repeating such calculations, the whole trajectory for each vehicle can be obtained. The speed and position at $t_0 + \Delta t$ will be selected from the obtained trajectory, i.e., $\nu(t_0 + \Delta t)$ and $x(t_0 + \Delta t)$ . They will potentially be assigned to the next step state $\left( t_0 + \Delta t, \nu_{t_0 + \Delta t}^{k_{ms}}, x_{t_0 + \Delta t}^{k_{ms}} \right)$ . 

# 3.4.2. Safe spacing requirement

Except for the first vehicle in the merging sequence $(k_{ms} = 1)$ that does not have a preceding vehicle, the next step states of other vehicles should satisfy the safe spacing requirement with the preceding vehicle. The safe spacing requirement is a minimum space headway which is the sum of Newell's safe space headway and the safe braking distance as in Equation (46). Therefore, it is a strict requirement that can guarantee safety even when the preceding vehicle suddenly brakes. It should be noted that the extra time headway for merging, $(+\beta)$ , is an additional item which is only applied for vehicles from different roads. 

$$
x _ {t _ {0} + \Delta t} ^ {p r e} - x _ {t _ {0} + \Delta t} ^ {k _ {m s}} \geq d + L + (\tau (+ \beta)) v _ {t _ {0} + \Delta t} ^ {k _ {m s}} + \max  \left[ 0, \left(v _ {t _ {0} + \Delta t} ^ {k _ {m s}} ^ {2} - v _ {t _ {0} + \Delta t} ^ {p r e} ^ {2}\right) / (- 2 a _ {\min }) \right] \tag {46}
$$

Simply including Equation (46) in the optimal control model (section 3.4.1) will greatly increase the computation time for finding a solution. Therefore, Equation (46) is regarded as a checking criterion to justify whether the solution of optimal control in the motion planning model meets the basic safety requirements of car-following described in Equation (46). If it is satisfied, the solution of the optimal control model will be chosen and implemented. Once Equation (46) is not met, the modified Newell's car-following model in section 3.4.3 will be activated. In addition, it should be noted that in the majority of the cases the optimal control model dominates the motion planning model. The evidence from numerical studies proved that the frequency of application of the Modified Newell's car-following model was less than $5\%$ . 

It is noteworthy that Equation (46) defines the kinematic relationship between vehicles and reflects the model features under extreme conditions, such as emergency brakes. This study assumes a centralized system in which current states and future planning motions of all vehicles are mastered by the control center. Therefore, all maneuvers that happen on a downstream vehicle in an equilibrium platoon will be replicated completely and transmitted to upstream vehicles. For example, at time $t$ , multiple vehicles are cruising at the same speed with minimal time headway. Once the first vehicle plans to apply a deceleration $(-a_{\min})$ at $t + \Delta t$ . It can be derived through Equation (46) that the second vehicle will brake with the same deceleration $(-a_{\min})$ at $t + \Delta t$ as well. The same derivation is true for other upstream vehicles. This feature indicates that the model will neither amplify nor actively reduce traffic oscillation. For a more ideal safety performance, future work should consider adding a disturbance attenuation function to the motion planning model. In this study field, Chen et al. (2021b) has achieved a significant result by a rotation-based cooperative control strategy considering a distributed feedback and feedforward longitudinal controller in preparation. 

Remark 1. The preceding vehicle of the next step should be clarified for implementing the safe spacing requirement. For this purpose, the following procedure is provided. When $S(k_{ms}) = k' \in \Omega'$ : if $S(k_{ms} - 1) = k \in \Omega$ and $t_m^{k'} \leq \Delta t$ , the preceding vehicle is mainline vehicle $k$ ; otherwise, the preceding vehicle is on-ramp vehicle $k' - 1$ . Similarly, when $S(k_{ms}) = k \in \Omega$ : if $S(k_{ms} - 1) = k' \in \Omega'$ and $t_m^{k'} \leq \Delta t$ , the preceding vehicle is on-ramp vehicle $k'$ ; otherwise, the preceding vehicle is mainline vehicle $k - 1$ . 

# 3.4.3. Modified Newell's car-following model

In situations that the optimal control model does not meet Equation (46), the modified Newell's car-following model will provide an alternative solution based on the merging sequence given by the upper-level model of the tactical planning model. Given the planned state of the preceding vehicle at the next step, $(\nu_{t_0 + \Delta t}^{pre}$ and $x_{t_0 + \Delta t}^{pre})$ , and the current state of the subject vehicle $(\nu_{t_0}^{k_{ms}}, x_{t_0}^{k_{ms}})$ , the model aims at generating a next step state that can follow the preceding vehicle with minimum spacing as in Equation (47). The programming model is constrained by vehicle dynamic limitations (Equations (48) and (49)) and the safe spacing requirement (Equation (46)), assuming a constant acceleration, as Equation (50). 

$$
\min  \left(x _ {t _ {0} + \Delta t} ^ {\text {p r e}} - x _ {t _ {0} + \Delta t} ^ {k _ {m s}}\right) \tag {47}
$$

# s.t. Equation (46) and

$$
v _ {\min } \leq v _ {t _ {0} + \Delta t} ^ {k _ {m s}} \leq v _ {\max } \tag {48}
$$

$$
a _ {\text {e m e r g e n c y}} \leq \left(v _ {t _ {0} + \Delta t} ^ {k _ {m s}} - v _ {t _ {0}} ^ {k _ {m s}}\right) / \Delta t \leq a _ {\max } \tag {49}
$$

$$
x _ {t _ {0} + \Delta t} ^ {k _ {m s}} - x _ {t _ {0}} ^ {k _ {m s}} = \Delta t \left(v _ {t _ {0} + \Delta t} ^ {k _ {m s}} + v _ {t _ {0}} ^ {k _ {m s}}\right) / 2 \tag {50}
$$

$x_{t_0 + \Delta t}^{pre}, v_{t_0 + \Delta t}^{pre}, v_{t_0}^{k_{ms}}$ and $x_{t_0}^{k_{ms}}$ are input variables of this programming. $x_{t_0 + \Delta t}^{k_{ms}}$ can be represented by $v_{t_0 + \Delta t}^{k_{ms}}$ by Equation (50). Therefore, $v_{t_0 + \Delta t}^{k_{ms}}$ is the only variable to be solved. From the Equation (47), it can be known that $d(x_{t_0 + \Delta t}^{pre} - x_{t_0 + \Delta t}^{k_{ms}}) / d\nu_{t_0 + \Delta t}^{k_{ms}} = -\Delta t / 2 < 0$ . Therefore, the optimal solution of $v_{t_0 + \Delta t}^{k_{ms}}$ equals the maximal feasible value in its feasible area (i.e., Equations (46), (48), and (49)). By substituting Equation (50) into Equation (46), the safe spacing requirement can be transformed as Equation (51). 

$$
g \left(v _ {t _ {0} + \Delta t} ^ {k _ {m s}}\right) = 2 a _ {\min } \left(B ^ {*} - A ^ {*} v _ {t _ {0} + \Delta t} ^ {k _ {m s}}\right) + \max  \left(0, v _ {t _ {0} + \Delta t} ^ {k _ {m s}} ^ {2} - v _ {t _ {0} + \Delta t} ^ {p r e} ^ {2}\right) \leq 0 \tag {51}
$$

where $A^{*} = \tau (+\beta) + \Delta t / 2$ ( $A^{*} > 0$ ) and $B^{*} = x_{t_{0} + \Delta t}^{pre} - d - L - x_{t_{0}}^{k_{ms}} - v_{t_{0}}^{k_{ms}}\Delta t / 2$ ( $B^{*} > 0$ ). 

$g$ is continuous in both intervals of $\left[0,\nu_{t_0 + \Delta t}^{pre}\right)$ and $\left(\nu_{t_0 + \Delta t}^{pre}, + \infty\right)$ . For the only special point that $\nu_{t_0 + \Delta t}^{kms} = \nu_{t_0 + \Delta t}^{pre}$ , it can be proved that. 

$$
\lim  _ {v _ {t _ {0} + \Delta t} ^ {k m s} \rightarrow v _ {t _ {0} + \Delta t} ^ {p r e}} g = \lim  _ {v _ {t _ {0} + \Delta t} ^ {k m s} \rightarrow v _ {t _ {0} + \Delta t} ^ {p r e}} g = 2 a _ {\min } \left(B ^ {*} - v _ {t _ {0} + \Delta t} ^ {p r e} A ^ {*}\right) \tag {52}
$$

Therefore, $g$ is continuous in the whole interval of $[0, +\infty)$ . Meanwhile, according to its differential equation (Equation (53)). 

$$
\dot {g} = \left\{ \begin{array}{l l} - 2 a _ {\min } A ^ {*} + 2 v _ {t _ {0} + \Delta t} ^ {k _ {m s}} & \text {i f} v _ {t _ {0} + \Delta t} ^ {k _ {m s}} > v _ {t _ {0} + \Delta t} ^ {p r e}, \\ - 2 a _ {\min } A ^ {*}, & o. w. \end{array} \right. \tag {53}
$$

If $\nu_{t_0 + \Delta t}^{k_{ms}} > 0$ , then $\dot{g} > 0$ , which indicates that $g\left(\nu_{t_0 + \Delta t}^{k_{ms}}\right)$ increases monotonically with $\nu_{t_0 + \Delta t}^{k_{ms}}$ in the interval of $[0, +\infty)$ . Considering the continuity and monotonicity, it can be concluded that the maximal speed and minimal speed in $[0, +\infty)$ that satisfies Equation (46) are $g^{-1}(0)$ (i.e., $\nu_1^*$ as in Equation (54)) and 0 (i.e., $\nu_2^*$ as in Equation (55)) respectively. 

$$
v _ {1} ^ {*} = \left\{ \begin{array}{c} a _ {\min } A ^ {*} + \sqrt {- 2 a _ {\min } B ^ {*} + v _ {t _ {0} + \Delta t} ^ {p r e} {} ^ {2} + \left(a _ {\min } A ^ {*}\right) ^ {2}}, i f g \left(v _ {t _ {0} + \Delta t} ^ {p r e}\right) \leq 0 \\ B ^ {*} / A ^ {*}, o. w. \end{array} \right. \tag {54}
$$

$$
v _ {2} ^ {*} = 0 \tag {55}
$$

Regarding constraints of vehicle dynamic (i.e., Equations (48) and (49)). $\nu_{3}^{*}$ is the maximal feasible speed as in Equation (56) and $\nu_{4}^{*}$ is the minimal feasible speed as in Equation (57). 

$$
v _ {3} ^ {*} = \min  \left(v _ {\max }, v _ {t _ {0}} ^ {k _ {m s}} + a _ {\max } \Delta t\right) \tag {56}
$$

$$
v _ {4} ^ {*} = \max  \left(v _ {\min }, v _ {t _ {0}} ^ {k _ {m s}} + a _ {\text {e m e r g e n c y}} \Delta t\right) \tag {57}
$$

The solution $(\nu_{t_0 + \Delta t}^{*k_{ms}})$ of the modified Newell's car-following model can be divided into three situations: if $\nu_{1}^{*} > \nu_{3}^{*}$ , then $\nu_{t_0 + \Delta t}^{*k_{ms}} = \nu_{3}^{*}$ ; if $\nu_{4}^{*} \leq \nu_{1}^{*} \leq \nu_{3}^{*}$ , $\nu_{t_0 + \Delta t}^{*k_{ms}} = \nu_{1}^{*}$ ; if $\nu_{1}^{*} < \nu_{4}^{*}$ , $\nu_{t_0 + \Delta t}^{*k_{ms}} = \nu_{4}^{*}$ . " $\nu_{1}^{*} < \nu_{4}^{*}$ " denotes the situation that all feasible speed values within the vehicle's dynamic constraints cannot satisfy the safety space requirement (Equation (46)). However, such a risk case rarely happens owing to the effect of the tactical planning model. 

# 4. Monte Carlo tree search-based decomposition algorithm

Even when only solving the critical states instead of the whole trajectory in one optimization, there is still great difficulty in obtaining a solution within an acceptable time. The major complexity comes from the tactical planning model which is a non-convex MIQCP. Especially, the merging sequence has $C_{N^{m} + N^{r}}^{N^{m}}$ combinations. As the number of involved vehicles increases, the computation time may explode at a factorial rate. Monte Carlo tree search (MCTS) is a powerful method in solving sequential decision problems (Kocsis and Szepesvári, 2006). Ma et al. (2021) applied the MCTS to determine the optimal lane-changing strategy for CAVs at isolated signalized intersections, which greatly saved computation time and still maintained good solution optimality. Due to its outstanding performance, this study builds a vehicular sequential decomposition algorithm based on MCTS (MCTS-DA) for the non-convex MIQCP of the tactical planning model. The MCTS-DA decomposes the programing model into the following two-steps circulation. 

Circulation step 1: determine the next vehicle (section 4.1). 

Through MCTS, determine the next vehicle from vehicles that have not been assigned a sequence. In this step, the leaving state of the preceding vehicle (if any) is needed. 

Circulation step 2: solving critical states (section 4.2). 

Substitute the critical states of preceding vehicles into the tactical planning model and solve critical states for the subject vehicle. If no rest vehicles, the circulation terminates, otherwise turn into Circulation step 1 and start a new circulation. 

# 4.1. Determining the next vehicle

The search tree is illustrated in Fig. 7. Similar to merging sequence $S$ , the determined merging sequence is also defined as ordered set $S_{d}$ , and $k_{d}$ is the index of the vehicle order in $S_{d}$ . The last vehicle in $S_{d}$ is called the root node $(R)$ . The nodes after $R$ are called candidates $(C)$ which must be the first vehicle with no sequence assignment in each road (mainline, $M_{1} = \min(\Omega - S_{d})$ ; on-ramp, $O_{1} = \min(\Omega' - S_{d})$ ), $C \in \{M_{1}, O_{1}\}$ . The nodes after $C$ are the leaf nodes $(L)$ . For each $C$ , leaf vehicles can be the following vehicle after $C$ in the same lane or the first vehicle with no sequence assignment from the different road, i.e., if $C = M_{1}$ , then $M_{2} = M_{1} + 1$ and $L \in \{M_{2}, O_{1}\}$ ; and if $C = O_{1}$ , then $O_{2} = O_{1} + 1$ and $L \in \{M_{1}, O_{2}\}$ . 

The MCTS repeats the "playout" procedure which consists of four steps: selection, expansion, simulation, and backpropagation. 

Selection: Each candidate will be scored by Equations (58) and (59) (Kocsis and Szepesvári, 2006). Then, select the candidate with the highest score. 

$$
U _ {C} = Q _ {C} + p \sqrt {(\ln N) / N _ {C}} \tag {58}
$$

$$
Q _ {C} = \left\{ \begin{array}{c} 0, \text {i f} w = b \\ (w - b _ {C}) / (w - b), o. w. \end{array} \right. \tag {59}
$$

In Equation (58), $U_{C}$ is the value of Upper Confidence bounds applied to Trees (UCT) for candidate $C$ . The first term $Q_{C}$ is the exploitation value that is formulated as a normalized optimal value as in Equation (59); The second term $\sqrt{(\ln N) / N_C}$ is the exploration value, which gives chances to those candidates that have not been extensively searched, where $N$ is the total playout times and $N_{C}$ is the visit times of $C$ . $p$ is the parameter to adjust the preference of exploration and exploitation which is assigned as $\sqrt{2}$ , an experience value (e.g., Chen et al., 2021c). In Equation (59), $w$ is the worst optimal value, and $b$ is the best optimal value among all the candidates. $b_{C}$ is the best optimal value of candidate $C$ (Rei, 2018). 

Expansion: Upon one of the candidates being selected, further choose a random leaf node. 

Simulation: Starting from the selected leaf node, generate a merging sequence randomly for the rest of the vehicles. Similar to $S$ and $S_{d}$ , the random merging sequence is defined as an ordered set $S_{r}$ and $k_{r}$ is the index of the vehicle order in $S_{r}$ . Then substitute $S_{r}$ into 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/18c7f312bbf1c23eb4b53c8eb05a12bf3e62d10e210cd213e6058189de3e45bc.jpg)



Fig. 7. The flow of the Monte Carlo tree search for the merging sequence.


Algorithm 1 to derive the simulated total travel time for all vehicles in $S_r$ , i.e., $\sum_{k_r} t_{ze-SM}^{k_r}$ . 

Backpropagation: Update the score of candidates according to $\sum_{k_r}t_{ze - SM}^{kr}$ 

Algorithm 1: Simulation  
// Input  
Generate $S_r$ Input the optimized $t_{ze-MCTS}^L$ and $\nu_{ze-MCTS}^L$ // Simulation $(t_{ze-SM}^{k_r=1}, \nu_{ze-SM}^{k_r=1}) = (t_{ze-MCTS}^L, \nu_{ze-MCTS}^L)$ For $k_r = 2$ : length $(S_r)$ $t_{free}^{k_r} = \operatorname{argmin}_{d(t_0^{k_r}, t_0^{k_r}, t_{ze}^{k_r}, t_{ze}^{k_r}, t_{ze}^{k_r}) \leq 0} t_{ze}^{k_r}$ $\nu_{free}^{k_r} = \operatorname{argmax}_{d(t_0^{k_r}, t_0^{k_r}, t_{ze}^{k_r}, t_{ze}^{k_r}, t_{ze}^{k_r}) \leq 0} \nu_{ze}^{k_r}$ $\nu_{ideal}^{k_r} = \nu_{ze-SM}^{k_r-1}$ $t_{ideal}^{k_r} = t_{ze-SM}^{k_r-1} + \tau + \frac{d+L}{\nu_{ideal}^{k_r}}$ If $t_{free}^{k_r} > t_{ideal}^{k_r}$ $(t_{ze-SM}^{k_r}, \nu_{ze-SM}^{k_r}) = (t_{free}^{k_r}, \nu_{free}^{k_r})$ Else $(t_{ze-SM}^{k_r}, \nu_{ze-SM}^{k_r}) = (t_{ideal}^{k_r}, \nu_{ideal}^{k_r})$ Endif  
End for  
Return $\sum_{k_r} t_{ze-SM}^{k_r}$ 

Notes: $t_{ze-MCTS}^{L}$ and $\nu_{ze-MCTS}^{L}$ is the optimized leaving time and speed of leaf vehicle $L$ from the control zone, which is obtained through Algorithm 2; $t_{free}^{kr}$ and $\nu_{free}^{kr}$ is the leaving time and speed of vehicle $k_r$ from the control zone in free-flow conditions; $t_{ideal}^{kr}$ and $\nu_{ideal}^{kr}$ is the ideal leaving time and speed of vehicle $k_r$ from the control zone, which only considers constraints of Equations (13)-(16). 

After numerous playouts, the candidate with the highest exploitation value $(Q_{C})$ will be determined as the next vehicle in the merging sequence. The detailed algorithm for circulation step 1 is summarized in Algorithm 2. 

Algorithm 2: determining the next vehicle   
// Step 0: Input. Input the $(t_{ze}^{R},\nu_{ze}^{R})$ // Step 1: Initialization Initialize $N = 2$ $N_{max} = 500$ $b = M$ $w = 0$ For every C-L combination do $N_C = 1$ $b_{C} = M$ $U_{C} = 0$ Given $(t_{ze}^{R},\nu_{ze}^{R})$ , solve $(t_{ze - MCTS}^{C},\nu_{ze - MCTS}^{C},t_{ze - MCTS}^{L},\nu_{ze - MCTS}^{L})$ through the tactical planning model Drop infeasible combinations End for   
// Step 2: Selection $C = \mathrm{argmax}(U_C)$ $N = N + 1$ $N_C = N_C + 1$ // Step 3: Expansion   
// Step 4: Simulation Call Algorithm 1, return $t_{ze - MCTS}^{C} + \sum_{k_r}t_{ze - SM}^{k_r}$ // Step 5: Backpropagation If $b > t_{ze - MCTS}^{C} + \sum_{k_r}t_{ze - SM}^{k_r}$ $b = t_{ze - MCTS}^{C} + \sum_{k_r}t_{ze - SM}^{k_r}$ Elseif $w <   t_{ze - MCTS}^{C} + \sum_{k_r}t_{ze - SM}^{k_r}$ $w = t_{ze - MCTS}^{C} + \sum_{k_r}t_{ze - SM}^{k_r}$ Endif If $b_{C} > t_{ze - MCTS}^{C} + \sum_{k_r}t_{ze - SM}^{k_r}$ $b_{C} = t_{ze - MCTS}^{C} + \sum_{k_r}t_{ze - SM}^{k_r}$ Endif For every candidate node do Update $Q_{C}$ and $U_{C}$ through Equations (58) and (59) End for   
// Step 6: Termination If $N = N_{max}$ $C = \mathrm{argmax}(Q_C)$ Return $C$ and terminate Else Go to step 2 Endif 

# 4.2. Solving critical states

In the algorithm, the critical states of each vehicle will be solved after its merging sequence is determined. The basic procedure is to substitute the critical states of preceding vehicles and then output the critical states of the subject vehicle. However, it does not simply involve solving them one by one. If the vehicle to be solved is an on-ramp vehicle, its critical states can be fixed in the current circulation except in the rare case introduced in Remark 2. However, if it is a mainline vehicle, its cut-by-follower state can be solved only after the merging state of its on-ramp follower is understood. Therefore, all critical states of the mainline vehicles can be finalized only if critical states of its on-ramp follower are confirmed or no on-ramp vehicle is remaining in the $S_{r}$ . The following procedure is for the situation that the vehicle to be solved is a mainline vehicle, supposing the procedure starts from the first vehicle in a separated mainline platoon whose index is $k$ . 

Step 1: Substitute critical states of its preceding vehicles into the tactical planning model and solve the cut-by-leader state (if any) and leaving state. 

Step 2: Find the on-ramp vehicles from $S_r$ . If there are none, jump to Step 6. Otherwise, save these critical states temporally. 

Step 3: Substitute the temporal critical states into the next circulation and determine the next vehicle in the merging sequence. If it is a mainline vehicle, go back to Step 1. Otherwise, go to Step 4. 

Step 4: Substitute the temporal critical states of its preceding vehicles into the tactical planning model and solve the entering state (if any), merging state and, the leaving state for the on-ramp vehicle (supposing its number is $k$ ) and get $t_m^k$ . 

Step 5: Starting from vehicle $k$ until vehicle $k'$ , given $\vec{t}^k = t_m^k$ , re-optimize the critical states one by one through the tactical planning model. 

Step 6: Finalize the critical states of all vehicles in $S_{d}$ . 

Remark 2. In rare cases, when the subject vehicle is $k \in \Omega$ and its preceding vehicle is $k' \in \Omega'$ , the merging state of vehicle $k'$ may give no feasible space for the cut-by-leader state of vehicle $k$ . If this happens, there will be no feasible solution for vehicle $k$ . Then, critical states of vehicle $k'$ will be recalculated with additional lower bound constraints on the merging state considering the possible solution space of the cut-by-leader state of the vehicle $k$ . 

# 5. Numerical studies

# 5.1. Simulation framework

To evaluate the performance of the proposed model, a merging bottleneck intersected by a single-lane freeway mainline and a single-lane on-ramp is assumed to be the study site, as illustrated in Fig. 8. The control center is positioned at the start point of the merging section. Control radius is $300\mathrm{m}$ , covering $300\mathrm{m}$ mainline and $300\mathrm{m}$ on-ramp upstream of the communication center, $200\mathrm{m}$ merging section, and $100\mathrm{m}$ mainline downstream of the merging section. The whole mainline is $1100\mathrm{m}$ long ( $500\mathrm{m}$ outside and 600 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/adb7d3396f45e57d85f29d1d812a7debb50585a6cb01eb68e963c32b0923f84d.jpg)



Fig. 8. The layout of the simulation platform.


m inside the control zone). The whole on-ramp is $500\mathrm{m}$ (200 m outside and $300\mathrm{m}$ inside the control zone). The given lengths of the on-ramp and mainline ensure the queues in all scenarios will not extend to the outside of the system. Therefore, the performance evaluation covers all input vehicles. Furthermore, considering values suggested by Japanese manual (Japan Society of Traffic Engineers, 2018), the speed limit for the mainline and merging section $(\nu_{max}^{m})$ is $100\mathrm{km / h}$ (27.7 m/s); the speed limit for the on-ramp traffic $(\nu_{max}^{r})$ is $60\mathrm{km / h}$ (16.7 m/s). Vehicles in the control zone are fully controlled by the CMC-FMP. Parameters and calibration references for the testbed setup are given as in Table 2. Vehicles that are outside of the control zone are controlled by the Intelligent Driver Model (IDM) with an acceleration exponent of 4 (Treiber et al., 2000). The other parameters in the IDM are calibrated with the same values in Table 2. 

The logic of the simulation system is summarized in Fig. 9. The simulation environment was provided by Simulation of Urban MObility (SUMO) 1.7.0 (Lopez et al., 2018). In every time step, the information of vehicles in the control zone was obtained and relayed via the traffic control interface function (TraCI) from SUMO to MATLAB. The optimization model was coded in MATLAB, through which Gurobi 9.1 (Gurobi Optimization Inc, 2020) was called to solve the programming problem. Then, the control commands were generated and every individual vehicle executes the corresponding command. Finally, the new status (positions and speeds) of each vehicle for the next step will be updated and sent back to the SUMO through TraCI for visualization. 

# 5.2. Computational efficiency and real-time application

# 5.2.1. Computational efficiency

As in Fig. 10(a), the computation efficiency and solution optimality of MCTS-DA are compared with the direct method (the way to solve the CMC-FMP model directly without any decomposition algorithm). Programming problems in both MCTS-DA and direct method are solved by calling Gurobi 9.1 (Gurobi Optimization Inc. 2020) on a desktop with an Intel 5.30 GHz 10 core CPU and 64 GB memory. The exact same scenarios are generated randomly to be solved by each of them. The input size refers to the number of vehicles within the control zone in each scenario. For a fair comparison, the execution time of the direct method refers to the time when it returns the same objective value as the one from MCTS-DA. For accommodating their results into one plot, a logarithmic scale is applied. As the input size increases, both execution time of the MCTS-DA (blue line) and the direct method (orange line) increase. 

As in Fig. 10(a), when the input size is less than 5, both MCTS-DA and the direct method spend less than 1 s, which is because the vehicle number limits the combinations of merging sequences in this region. However, when the input size is lower than 6, the MCTS-DA spends more time on computation than the direct method. It is because the algorithms in MCTS-DA require some basic running time which is costly than the direct method under low input size. It is noticed that a remarkable increase from 0.17 s to 2.16 s is presented between the input size of 4 and 5. Because when the input size equals 5, all nodes of different roles in the search tree (Fig. 7) are probably filled. It means that the full algorithm in MCTS is activated. The blue line and the orange line cross between 6 and 7. For the direct method, the execution time after "input size = 7" increases explosively, which is from 4.43 s (7) to 34.93 s (8) then to 125.16 s (9). It is because, with the increase of input size, the combinations of merging sequences increase with factorial magnification. Furthermore, the direct method cannot get the result for scenarios with over 10 vehicles within an acceptable time. Therefore, the input size of Fig. 10(a) is scaled to 10. The increasing speed of execution time for the MCTS-DA is about 0.43 s per vehicle when the input size is higher than 4. Fig. 10(b) shows the execution time of MCTS-DA with large input size and the normal scale is applied. It can be observed that the execution time of MCTS-DA keeps a linearly increasing rate with the increase of input size. 

In MCTS-DA, the tactical planning model for numerous vehicles is decomposed into several two-vehicle scenarios to be solved sequentially, which drastically decreases computation complexity. To be specific, the computation time for the tactical planning model to solve the subproblem of a two-vehicle scenario is denoted as $T$ . If the input size is over 4, the MCTS-DA contains 7 or 8 such subproblems for each circulation, which are contributed by step 1 of Algorithm 2 (6 subproblems) and the process of solving critical states (1 or 2 subproblems in average). The overall computation time of MCTS-DA is around $7(N^{m} + N^{r})T$ or $8(N^{m} + N^{r})T$ , which explains the linearly increasing trend in Fig. 10(b). The linearly increasing trend of the computational time of MCTS-DA indicates that the 


Table 2 Parameters for the testbed setup and vehicle behaviour.


<table><tr><td>Parameters</td><td>Values</td></tr><tr><td>Δt</td><td>0.5 s*</td></tr><tr><td>n</td><td>3*</td></tr><tr><td>τ</td><td>1.5 s (Ding et al., 2020)</td></tr><tr><td>d</td><td>2.5 m (Ma et al. 2021)</td></tr><tr><td>L</td><td>5 m (Ma et al. 2021)</td></tr><tr><td>β</td><td>0.5 s (Ding et al., 2020)</td></tr><tr><td>lms</td><td>-200 m*</td></tr><tr><td>lme</td><td>0 m*</td></tr><tr><td>lzs</td><td>-500 m*</td></tr><tr><td>lze</td><td>100 m*</td></tr><tr><td>νmin</td><td>10 km/h (Zhou et al., 2019)</td></tr><tr><td>a max</td><td>2 m/s2 (Sun et al., 2020)</td></tr><tr><td>a min</td><td>-4 m/s2 (Sun et al., 2020)</td></tr><tr><td>aemergency</td><td>-6 m/s2 (Sun et al., 2020)</td></tr></table>


* Assumption. 


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/d18ef459396bd0cad174f8d56cbac45072890d030e347019466de88223a32e09.jpg)



Fig. 9. The logic of the simulation system.


computation time is in a controllable range. 

Then we let the direct method solve the above scenarios until the best solutions are achieved, without any time limitation. Treating these results of the total travel time as the optimal truth, the optimization gap is calculated as ((total travel time from MCTS-DA)-(optimal truth)/(optimal truth). Due to the extremely long calculation time of the direct method for scenarios with over 10 vehicles, the optimization gap is displayed only on input sizes within 10. As in Fig. 10(a), the optimization gap (black dashed line) is distributed under $10\%$ and most of these optimization gaps are located lower than $5\%$ , which indicates the MCTS-DA can generate comparable results to the optimal truth. This is because extensively searching the merging sequence through MCTS ensures its optimality. 

# 5.2.2. Real-time application: A batch-based scheme

A batch-based scheme is supposed for achieving real-time control as in Fig. 11. In this scheme, two trigger points are assumed, which are the $l_{tp}^{m}$ at the mainline and the $l_{tp}^{r}$ at the on-ramp respectively (both are upstream of the merging area). Once a vehicle without a trajectory plan from either the mainline or the on-ramp reaches the trigger points (as time $t_2$ in Fig. 11), the control center groups all vehicles without batch assignment between the trigger points and the upstream border of the control zone as a new batch of vehicles (green vehicles at time $t_2$ of Fig. 11). For vehicles in each newly identified batch, their merging sequence and critical states will be optimized by using the tactical planning model. The merging sequence and critical states will be fixed after the solution is obtained. Then, with the fixed merging sequence and critical states, the vehicle will apply the motion planning model in every time step (0.5 s) until they leave the control zone in a real-time manner (as time $t_3$ of Fig. 11). The fast solving (<0.01 s) of the motion planning model can be achieved by the analytical solutions indicated in sections 3.4.1 and 3.4.3. Therefore, the above-mentioned real-time control by the motion planning model is applicable. It is noteworthy that the solving of each batch should be compatible with the merging sequence and critical states of vehicles in the previous batch. Two requirements should be satisfied regarding the position of trigger points and calculation time of the tactical planning model for a batch. 

First, the distance between the on-ramp trigger point and merging section should be large enough to ensure that each on-ramp vehicle should receive its trajectory plan from MCTS-DA before it enters the merging section. Equation (60) considers the most extreme situation where the first on-ramp vehicle merges after the last mainline vehicle. 

$$
l _ {m s} - l _ {t p} ^ {r} \geq v _ {\max } ^ {r} s _ {\varphi} \left(n ^ {m} + 1\right) \tag {60}
$$

where $s_{\varphi}$ stands for the increasing slope of computational time with the number of vehicles; $n^{m}(n^{r})$ is the number of mainline (on-ramp) vehicles in a batch. 

Second, the calculation of the tactical planning model should be finished before the last vehicle in a batch (either from mainline or on-ramp) passes the trigger point as in Equation (61). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/1c79a728830b7353944dea81faf41856706e88e9cce6bc402f980894cb9deb3c.jpg)



(a) Input size $\sim 10$ and execution time in logarithmic scale


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/d612c4876502af43d6c523eb7f2a20da3c3c34db8ad366d3336ada7cb79f3e77.jpg)



(b) Input size $\sim 20$ and execution time in normal scale



Fig. 10. Execution time and optimization gaps of the MCTS-DA.


$$
s _ {\varphi} \left(n ^ {m} + n ^ {r}\right) \leq \min  \left(\left(l _ {t p} ^ {m} - l _ {z s}\right) / v _ {a v g} ^ {m}, \left(l _ {t p} ^ {r} - l _ {z s}\right) / v _ {a v g} ^ {r}\right) \tag {61}
$$

where $\nu_{avg}^{m}(\nu_{avg}^{r})$ is the average speed of the mainline (on-ramp) vehicles, $\nu_{min} \leq \nu_{avg}^{m} \leq \nu_{max}^{m}$ and $\nu_{min} \leq \nu_{avg}^{r} \leq \nu_{max}^{r}$ . 

To balance the length of batch identification areas on mainline and on-ramp, we let $\left(l_{tp}^{m} - l_{zs}\right) / \nu_{avg}^{m} = \left(l_{tp}^{r} - l_{zs}\right) / \nu_{avg}^{r}$ . Meanwhile, considering the equilibrium space headway of Newell's car-following model, $n^m$ and $n^r$ can be represented by Equation (62) and (63) respectively. 

$$
n ^ {m} = \left(l _ {t p} ^ {m} - l _ {z s}\right) / \left(d + L + \tau v _ {\text {a v g}} ^ {m}\right) \tag {62}
$$

$$
n ^ {r} = \left(l _ {t p} ^ {r} - l _ {z s}\right) / \left(d + L + \tau v _ {\text {a v g}} ^ {r}\right) \tag {63}
$$

Conditions of $l_{ip}^{r}$ and $s_{\varphi}$ can be further derived as in Equation (64) and (65). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/b7fec1f6ab2537f04601d149d56a24cfb334978e1ea98bd61e562f4345986fe5.jpg)


: Control center : Batch #1 

1: Batch #2 without trajectory plan 

: Trigger point : Batch #2 with trajectory plan : vehicles without batch assignment 

# $t_1$ : only batch 1 is controlled

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/7b6a6ed8ce398c37d2ede9c2e0e76598f1bafedd44518266aedf52ff6823859f.jpg)


# $t_2$ : batch 2 is identified

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/09528d87c5d9285cb847ba3a9f9f2722a15742e63e6d003c9e26124fdc6b1746.jpg)


# $t_3$ : trajectory plans for batch 2 are solved

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/afa6b11d38bd97dee0735ffd9e55bb26491ae850c2681bc8f43d396134679caf.jpg)



Fig. 11. Batch-based scheme.


$$
l _ {t p} ^ {r} \leq \left[ l _ {m s} + s _ {\varphi} v _ {m a x} ^ {r} \left(C ^ {*} l _ {z s} - 1\right) \right] / \left(s _ {\varphi} C ^ {*} v _ {m a x} ^ {r} + 1\right) \tag {64}
$$

where $C^* = \nu_{avg}^m / \left[ \nu_{avg}^r \left( d + L + \tau \nu_{avg}^m \right) \right]$ , which ranges from 0.014 to 0.204 with variations of $\nu_{avg}^m$ and $\nu_{avg}^r$ . 

$$
s _ {\varphi} \leq 1 / \left\{1 / \left[ (d + L) / v _ {a v g} ^ {m} + \tau \right] + 1 / \left[ (d + L) / v _ {a v g} ^ {r} + \tau \right] \right\} \tag {65}
$$

Considering the worst situation, i.e., $\nu_{avg}^{m} = \nu_{max}^{m} = 27.7m / s$ and $\nu_{avg}^{r} = \nu_{max}^{r} = 16.7m / s$ , it can be derived that $s_{\varphi} < 0.927$ . The $s_{\varphi}$ in Fig. 10 is 0.43 which is smaller than 0.927. Then, by substitutings $\varsigma_{\varphi} = 0.43$ into Equation (64) and considering the worst situation (i.e., $C^* = 0.204$ ), $I_{tp}^{r} < -380\mathrm{m}$ can be derived. Therefore, it can be concluded that the CMC-FMP using the MCTS-DA is feasible for applying the batch-based scheme if the trigger point at the on-ramp is set to $180\mathrm{m}$ upstream of the merging section (i.e., $120\mathrm{m}$ batch identification area). A larger batch identification area is preferred since it means a batch including more vehicles will be considered and optimized simultaneously. Using the batch-based scheme with limited batch identification area may discount the optimality. With the improvement of computational ability in the future, the batch identification area can be further enlarged. This paper aims to reveal the effect of considering flexible merging positions in system optimal control in a future scenario. For this sake, the batch-based scheme is 

not applied in the following simulation experiments. 

# 5.3. Comparison between CMC-FMP and CMC-SMP

The performance of the proposed CMC-FMP is examined through a case study. For a fair comparison, the CMC-SMP has the same model structure as CMC-FMP but applies different constraints in its tactical planning model for fixing the merging point. Similar to the majority of past studies (Mu et al., 2021), CMC-SMP requires that all on-ramp vehicles can only and must merge at the end of the merging section. For its detailed model formulation, please refer to Appendix B. 

In total, 12 demand scenarios were tested with different demand levels and demand splits. Four demand levels were given, i.e., 1200, 1400, 1600, and 1800 veh/h. For each demand level, three demand splits of on-ramp and mainline were defined, i.e., 20-80, 35-65, and 50-50. For each scenario, three parallel simulations were conducted with different random seeds of vehicle arrival time. Each simulation ran for 400 s including 100 s for warming up and 300 s for performance measurements. Given parameter values in Table 2, the capacity of the simulated merging bottleneck under pure mainline flow or pure on-ramp flow is 1800 veh/h. However, due to interactions between the on-ramp and mainline flow, the capacity under each demand split may vary slightly. Therefore, the capacity under each demand split varies. In principle, 1200 and 1400 veh/h are free-flow, 1600 veh/h is near-saturated and 1800 veh/h may be saturated or oversaturated. 

# 5.3.1. Average delay

Table 3 shows the average delay in various demand scenarios. The delay is calculated as the difference between the actual travel time and the free-flow travel for each vehicle. For each scenario, three delay values are separately measured from a) the total merging bottleneck including the mainline (1100 m: 500 m outside and 600 m inside the control zone) and the on-ramp (500 m: 200 m outside and 300 m inside the control zone); b) the mainline (1100 m: 500 m outside and 600 m inside the control zone); c) the on-ramp (500 m: 200 m outside and 300 m inside the control zone). For both CMC-FMP and CMC-SMP, with increasing demand levels, delays of the whole merging bottleneck, mainline and on-ramp increase under the different demand splits due to more frequent disturbances between the on-ramp and mainline vehicles. This trend accords with the common sense that heavy traffic volume leads to large delay. Only at the 1800 veh/h level, delays at 50-50 of CMC-FMP and all demand splits of CMC-SMP are larger than 10 s. It is because accumulation phenomena happened at on-ramps in these four scenarios. Especially, the highest delay is incurred at the 50-50 demand splits, which indicates that the high ratio of on-ramp demand is disadvantageous for traffic efficiency. 

A remarkable reduction in delay by the CMC-FMP can be observed compared to the results of CMC-SMP at all demand scenarios. The reduced delays of low demand levels (i.e., 1200 and 1400 veh/h) are less significant than high demand levels. But even so, changes in percentage of light traffic can reach $18 - 41\%$ . In this demand range, CMC-FMP and CMC-SMP have comparable performance in mainline vehicles. Improvements of CMC-FMP are mainly contributed by on-ramp vehicles; the reduction on their delay can even reach $74\%$ (20-80 with 1200 veh/h). Whereas, although the relative improvement is remarkable, the absolute difference in delay is less than 2 s under low demand levels. In fields of high-demand scenarios (i.e., 1600 and 1800 veh/h), the delay reduction on mainline vehicles becomes noticeable, which can reach $52\%$ with a maximal value difference of 5.23 s. Meanwhile, significant differences of delays between CMC-FMP and CMC-SMP can be observed from on-ramp vehicles, which can be up to $88\%$ with a maximal value difference of 17.54 s. For the performance of the whole merging bottleneck, the improvement percentages vary between $26\%$ and $64\%$ . The greatest 


Table 3 Results of average delay.


<table><tr><td colspan="14">Average delay of CMC-FMP (s)</td></tr><tr><td></td><td></td><td colspan="4">Total delay</td><td colspan="4">Mainline delay</td><td colspan="4">On-ramp delay</td></tr><tr><td>Level (veh/h)</td><td></td><td>1200</td><td>1400</td><td>1600</td><td>1800</td><td>1200</td><td>1400</td><td>1600</td><td>1800</td><td>1200</td><td>1400</td><td>1600</td><td>1800</td></tr><tr><td rowspan="3">Split</td><td>20-80</td><td>1.88</td><td>2.11</td><td>3.01</td><td>4.32</td><td>2.13</td><td>2.46</td><td>3.45</td><td>4.76</td><td>0.91</td><td>0.83</td><td>1.32</td><td>2.67</td></tr><tr><td>35-65</td><td>1.34</td><td>1.92</td><td>2.12</td><td>6.43</td><td>1.77</td><td>2.32</td><td>2.41</td><td>5.99</td><td>0.63</td><td>1.21</td><td>1.63</td><td>7.18</td></tr><tr><td>50-50</td><td>1.18</td><td>1.63</td><td>3.19</td><td>17.11</td><td>1.52</td><td>2.12</td><td>3.58</td><td>7.62</td><td>0.87</td><td>1.19</td><td>2.83</td><td>26.17</td></tr><tr><td colspan="14">Average delay of CMC-SMP (s)</td></tr><tr><td></td><td></td><td colspan="4">Total delay</td><td colspan="4">Mainline delay</td><td colspan="4">On-ramp delay</td></tr><tr><td>Level (veh/h)</td><td></td><td>1200</td><td>1400</td><td>1600</td><td>1800</td><td>1200</td><td>1400</td><td>1600</td><td>1800</td><td>1200</td><td>14 00</td><td>1600</td><td>1800</td></tr><tr><td rowspan="3">Split</td><td>20-80</td><td>2.47</td><td>2.81</td><td>5.76</td><td>12.13</td><td>2.20</td><td>2.78</td><td>4.32</td><td>9.99</td><td>3.47</td><td>2.92</td><td>11.23</td><td>20.21</td></tr><tr><td>35-65</td><td>1.96</td><td>2.87</td><td>5.30</td><td>11.76</td><td>1.95</td><td>2.32</td><td>4.03</td><td>9.74</td><td>1.97</td><td>3.80</td><td>7.50</td><td>15.18</td></tr><tr><td>50-50</td><td>1.44</td><td>2.76</td><td>5.36</td><td>23.08</td><td>1.69</td><td>2.57</td><td>4.38</td><td>10.10</td><td>1.20</td><td>2.93</td><td>6.29</td><td>35.27</td></tr><tr><td colspan="14">Change in Percentage (%): ((CMC-SMP)-(CMC-FMP)) / (CMC-SMP)</td></tr><tr><td></td><td></td><td colspan="4">Total delay</td><td colspan="4">Mainline delay</td><td colspan="4">On-ramp delay</td></tr><tr><td>Level (veh/h)</td><td></td><td>1200</td><td>1400</td><td>1600</td><td>1800</td><td>1200</td><td>1400</td><td>1600</td><td>1800</td><td>1200</td><td>1400</td><td>\( {1600} \)</td><td>1800</td></tr><tr><td rowspan="3">Split</td><td>20-80</td><td>24%</td><td>25%</td><td>48%</td><td>64%</td><td>3%</td><td>12%</td><td>20%</td><td>52%</td><td>74%</td><td>71%</td><td>88%</td><td>87%</td></tr><tr><td>35-65</td><td>31%</td><td>33%</td><td>60%</td><td>45%</td><td>9%</td><td>0%</td><td>40%</td><td>38%</td><td>68%</td><td>68%</td><td>78%</td><td>53%</td></tr><tr><td>50-50</td><td>18%</td><td>41%</td><td>41%</td><td>26%</td><td>10%</td><td>18%</td><td>18%</td><td>25%</td><td>28%</td><td>60%</td><td>55%</td><td>26%</td></tr></table>

reduction on delay values is the scenarios under 1800 veh/h with a 20-80 demand split. The above evidence reveals that the benefits of the consideration of specific individual merging positions in CMC are remarkable and meaningful because it will greatly improve the traffic efficiency of all vehicles. 

# 5.3.2. Mainline speed contours

Delay reduction of CMC-FMP at 1800 veh/h is especially significant. The scenarios under 1800 veh/h are further analyzed for exploring the different effects between CMC-FMP and CMC-SMP. Fig. 12 are the mainline speed contours of CMC-FMP and CMC-SMP for comparing propagations of mainline traffic in the merging area $(-200$ to $-0\mathrm{m})$ and the section upstream of the merging area $(-1100$ to $-200\mathrm{m})$ . 

At the demand split of 20-80, the mainline traffic of CMC-FMP is in free-flow conditions, which indicates that the mainline vehicles are scarcely influenced by on-ramp traffic in this scenario as shown in Fig. 12(a). Whereas for CMC-SMP, a large area of low speed (between 12 and $18\mathrm{m / s}$ ) can be found at the upstream of the merging section (between $-500\mathrm{m}$ and $-200\mathrm{m}$ ) at the same demand split as shown in Fig. 12(b), which indicates that the mainline flow is greatly influenced. 

As the demand ratio of on-ramp vehicles increases to $35\%$ only in a few areas of Fig. 12(c), the speed decreases to between 16 and $18~\mathrm{m / s}$ , which is distributed between $-400\mathrm{m}$ and $-200\mathrm{m}$ discontinuously and sporadically. This is because as the percentage of the on-ramp flow increases, the weight of the on-ramp efficiency began to increase. In some situations, mainline vehicles decelerated for 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/4893ee107dd978e4ba1d10738b987be2186bdc57d42d5db73a0423ed6d7adcc4.jpg)



(a) CMC-FMP: 1800-(20-80)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/f4d8faae81ab2b08db11f21f7f1f2d6c1103953bcff579171c15e694c9112c24.jpg)



(b) CMC-SMP: 1800-(20-80)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/f3213b725cb64dd2b8f3aae5675a9b8bfc43485c243558ca6840cdc851c7b99f.jpg)



(c) CMC-FMP: 1800-(35-65)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/85cb9c03ab9c7179c11594af536217f7c8a17ad046f8a20589fa6fbf34dd333f.jpg)



(d) CMC-SMP: 1800-(35-65)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/1956fd876cae139c14149245357ebf59a14a878f89bb243da7634396228ffb32.jpg)



(e) CMC-FMP: 1800-(50-50)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/c94c402373d553d9af90fa2c2fcc4f63c15e34760a2e8355fb80f6a7e45be304.jpg)



(f) CMC-SMP: 1800-(50-50)



Fig. 12. Mainline speed contour: CMC-FMP (left, (a) (c) (e)) VS. CMC-SMP (right, (b) (d) (f));


the convenience of the on-ramp merging. On the other hand, the distribution of low speed area in Fig. 12(d) is similar to the one in Fig. 12(b). However, the speed reduction of CMC-SMP at the demand split of 35-65 (Fig. 12(d)) is greater than the one at the demand split of 20-80. 

As the demand ratio of on-ramp vehicles further increases to 50-50, in the result of CMC-FMP (Fig. 12(e)), areas of low speed expand upstream of the merging section. These low-speed areas are still discontinuous and only concentrated in several areas, which means that the impact on mainline traffic is not serious and can dissipate in time. Compared to CMC-FMP, the low-speed areas in the result of CMC-SMP (Fig. 12(f)) are widely and continuously distributed. In addition, the speed reduction range of CMC-FMP at 50-50 (Fig. 12(e)) is greater than the CMC-FMP at 20-80 and 35-65. Even in some points, i.e., $(-290\mathrm{m}, 230\mathrm{s})$ , $(-230\mathrm{m}, 330\mathrm{s})$ , and $(-230\mathrm{m}, 370\mathrm{s})$ the speed decreases to lower than $8\mathrm{m/s}$ . Whereas, as in Fig. 12(f), the lowest speed of CMC-SMP is around $10\mathrm{m/s}$ . It indicates that, compared to CMC-FMP, the mainline speed reduction of CMC-SMP is smaller at the demand split of 50-50. The reason for this 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/cd4e7f42300834410470d9240ff67c047713e39f341f2e6742c196d86fd21c01.jpg)



(a) CMC-FMP: 1800-(20-80)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/90fab054f132de642b775d63916b4cef6e0bc3775033574559413fa966a9b2ef.jpg)



(b) CMC-SMP: 1800-(20-80)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/4aa7ee52e47e8b316575f8d77eff2cca77f27fe0ac3dc14d4a78d74f64fcb239.jpg)



(c) CMC-FMP: 1800-(35-65)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/946adf78cd8a231b680c7df6f1c9012ef46da4cb5a9fc57992a32edbf4925501.jpg)



(d) CMC-SMP: 1800-(35-65)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/b8be717338501b1197280d43817e2b96909792a7f4bf77f9296b3c1a43aa86da.jpg)



(e) CMC-FMP: 1800-(50-50)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/9a43fcc8467dc03b88ae1246803cc3530d1acade113772c9df0573a338dc041e.jpg)



(f) CMC-SMP: 1800-(50-50)



Fig. 13. Results of vehicle trajectories between 100 and $200\mathrm{s}$


finding will be further explained by trajectories in the following section. 

In summary, under the saturated demand level with various demand splits, the CMC with flexible merging positions can obtain better traffic strategies that can maintain the smoothness of mainline flow than the CMC with a fixed merging point. Therefore, regarding the influence on mainline speed, the benefit of the proposed CMC-FMP is noticeable. It should also be noted that the speed color of the section upstream of the control zone $(-1000\mathrm{m}$ to $-500\mathrm{m})$ is almost dark blue in all these six figures, which indicates that the proposed algorithms do not sacrifice upstream traffic for only ensuring the efficiency and smoothness of traffic in the merging area and control area. 

# 5.3.3. Trajectory maps

Fig. 13 displays trajectories of CMC-FMP and CMC-SMP under the demand level of 1800 veh/h. The trajectory maps are mainly for comparing the smoothness of merging processes of on-ramp vehicles. Therefore, those figures focus on a section of $600\mathrm{m}$ including $200\mathrm{m}$ merging area, $300\mathrm{m}$ upstream of the merging area, and $100\mathrm{m}$ downstream of the merging area. 

In Fig. 13(a) and (b), when the proportion of the on-ramp flow is 0.2, the trajectory smoothness of the on-ramp in CMC-FMP shows a great difference from the one in CMC-SMP. The majority of on-ramp vehicles in CMC-FMP could complete the merging without slowing down. Meanwhile, few mainline vehicles conducted slight speed adjustments to give acceptable gaps to approaching on-ramp vehicles. In contrast, the result of CMC-SMP shows that most on-ramp vehicles experienced significant speed reductions between $-250$ m and $-100$ m. Meanwhile, mainline vehicles that follow the on-ramp vehicles executed abrupt slow down to meet the requirement of safe merging. As the proportion of the on-ramp flow increases to 0.35, there are still more on-ramp vehicles that went through a long period of speed drop before merging in CMC-SMP (Fig. 13(d)) than those in CMC-FMP (Fig. 13(c)). However, this difference is less significant than at the demand split of 20-80. When it comes to the demand split of 50-50, the difference in trajectories of the two controls becomes negligible as in Fig. 13(e) and (f). 

The findings above are because the merging positions of on-ramp vehicles in CMC-SMP are fixed. Some on-ramp vehicles that are approaching the fixed merging point are not able to get a suitable merging opportunity from the limited solution space in time. Then, they have to slow down and wait until acceptable gaps are created. If an on-ramp vehicle still is not successful in merging after numerous mainline vehicles passing by, the on-ramp vehicle is likely to be in a state that is at a low speed and close to the merging point. The next coming mainline vehicle may adjust its speed largely to meet the strict merging constraint, which will do harm to the upstream mainline traffic. This is the reason why continuous and large areas of low speed can be observed in Fig. 12(b), (d), and (f). Unlike the CMC-SMP, on-ramp vehicles in CMC-FMP can merge into the mainline at any position within the merging section. Meanwhile, the surrounding mainline vehicles have more chances to create gaps for on-ramp vehicles to merge. Therefore, the CMC-FMP is more capable of generating strategies to make two traffic flows merge smoothly. However, such capability is not infinite. As the on-ramp traffic proportion rises, great speed reductions on both mainline and on-ramp may happen in some situations as can be 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/16c25258511f2e091776dc7a6f8fde14e5f28e507fa3645ec519f121cbb9fa76.jpg)



(a) 1800-(20-80)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/0d3932943c73dfefce6343263eb07a12ad3a4fea4fe4ca7df142aa88d43f5154.jpg)



(b) 1800-(35-65)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/c57aabaa30db06c4333feb10493836c894a8552ac78a2b11d0a2c518787ef6e3.jpg)



(c) 1800-(50-50)



Fig. 14. Time headway measured at $0\mathrm{m}$ , $-100\mathrm{m}$ , and $-200\mathrm{m}$ of mainline.


observed in Fig. 12(a), (c), and (e). In sum, the proposed model is more advantageous in the performance of cooperating the on-ramp trajectories with the mainline trajectories. 

Furthermore, it can be found that on-ramp vehicles' merging positions in CMC-FMP are distributed in the rear part of the merging section (between $-100\mathrm{m}$ and $0\mathrm{m}$ ) when the demand split is 20-80 as in Fig. 13(a). With the increase of the on-ramp traffic ratio, the number of vehicles that merge at the front part of the merging section (between $-200\mathrm{m}$ and $-100\mathrm{m}$ ) increases. Especially, at the demand split of 50-50, some on-ramp vehicles even enter into the mainline at the starting position of the merging section (e.g., $-200\mathrm{m}$ , 115 s in Fig. 13(e)). It means that merging speeds of these vehicles are only $60\mathrm{km/h}$ , which will seriously influence the mainline traffic. This is the main reason for the phenomenon that the mainline speed of CMC-FMP can decrease to "lower than $8\mathrm{m/s}$ " at the demand split of 50-50. 

# 5.3.4. Time headway distribution (traffic voids)

Fig. 14 displays cumulative probability curves of time headway measured at $0\mathrm{m}$ (blue lines), $-100\mathrm{m}$ (green lines), and $-200\mathrm{m}$ (red lines) of mainline under the demand level of 1800 veh/h, which is to compare models' performance in reducing traffic voids. 

It is clear that cumulative probability curves of time headway shifted rightward as the measuring position moves towards the upstream position $(0\mathrm{m}\rightarrow -100\mathrm{m}\rightarrow -200\mathrm{m})$ . It indicates the process that the mainline vehicles create new gaps for on-ramp vehicles in the upstream section, and the gaps are filled by on-ramp vehicles in the downstream section. Among scenarios of three demand splits, curves of CMC-FMP (solid lines) are all to the left of the curves of CMC-SMP (dashed lines) at the measuring position of $0\mathrm{m}$ , which indicates that the output flow of CMC-FMP has fewer voids than CMC-SMP. At the measuring positions of $-100\mathrm{m}$ and $-200\mathrm{m}$ , curves of CMC-FMP are all located to the left of CMC-SMP curves. It reveals that the platoon controlled by CMC-FMP during the merging process is more compact than CMC-SMP. Because the mainline vehicles controlled by CMC-SMP should always keep the created gap until the on-ramp vehicles enters at the fixed merging points. 

These findings further prove the merits of flexible merging positions in reducing traffic voids. Meanwhile, differences between curves of CMC-SMP and CMC-FMP are enlarged remarkably as the demand from on-ramp increases, which reveals that the advantages of CMC-FMP are more significant when merging activities are more frequent (higher on-ramp splits). 

# 5.4. Sensitivity analysis

The extra time headway for safe merging $\beta$ and the merging section length are two significant parameters that impact the performance of the proposed CMC-FMP. To further investigate models' characteristics, sensitivity studies are conducted on these two parameters with scenarios under the demand level of 1800 veh/h at three different demand splits. It should be noted that the output flow is measured at the end position of the control zone. 

# 5.4.1. Impacts of $\beta$

Keeping other parameters unchanged as in Table 2, $\beta$ is adjusted from 0.1 to $1.0\mathrm{s}$ , with an even interval of $0.1\mathrm{s}$ . Results are summarized in Fig. 15. In all three demand split scenarios, with the increase of $\beta$ , the output flow rate decreases, and the average delay increases. It is because larger $\beta$ denotes more strict safety requirements on the merging process. Then, every merging process needs mainline vehicles to adjust more to create safety margins with longer time or larger space. Also, merging opportunities for on-ramp 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/66a40ed4866d57f77d34d5b86319baa923ab1428fc09c4d2510c8761c6818bef.jpg)



Fig. 15. Impacts of the $\beta$ .


vehicles become fewer. Therefore, the large value of $\beta$ impacts the operational performance of the merging bottleneck, which further leads to the decrease of the output flow rate and the increase of average delay. 

Meanwhile, noticeable differences between the three scenarios can be observed. The increasing (decreasing) trend of the average delay (output flow rate) on $\beta$ is faster in scenarios with high on-ramp splits than it in scenarios with low on-ramp splits. It indicates that the impact of $\beta$ is more significant when the on-ramp vehicles' proportion is larger, which is because merging events happen more frequently in scenarios with higher on-ramp flow. 

# 5.4.2. Impacts of the merging section length

Keeping other parameters unchanged as in Table 2, the merging section length is extended from $100\mathrm{m}$ to $300\mathrm{m}$ with an even interval of $50\mathrm{m}$ by adjusting the position of $l_{ms}$ . Results are summarized in Fig. 16. In general, with the increase of the merging section length, the output flow rate increases, and the average delay decreases. This is because a longer merging section can provide more solution space for optimizing the performance of the merging bottleneck. Meanwhile, longer merging section means on-ramp vehicles may have more time to accelerate and merge into the mainline with higher speed so that mainline vehicles will be less affected. 

However, in the three scenarios, such a trend presents different types. For the 20-80 demand split, the output flow rate only increases in the section from $100\mathrm{m}$ to $150\mathrm{m}$ and then matches the input flow. The average delay decreases in this region and then changes less. For the 35-65 demand split, the output flow rate is lower than the 20-80 scenario at $100\mathrm{m}$ . It increases to the input value of 1800 veh/h until the merging section length is $250\mathrm{m}$ . The average delay decreases in the same region. More than this, the output flow rate of the 50-50 scenario is lower than the other two scenarios. Its output flow rate increases with the merging section length through all cases. Meanwhile, the average delay of the 50-50 scenario is two times more than the other two and keeps decreasing until $250\mathrm{m}$ . The above findings reveal that for improving the benefit of the CMC-FMP, extending the merging section is a possible measure. Whereas, a longer merging section is needed for merging bottlenecks with higher on-ramp traffic ratios. 

# 6. Conclusions and future work

The current cooperative merging models specify a fixed merging point for on-ramp vehicles, which is aimed at reducing the models' complexity. However, such a setting limits the solution space and influences the models' performance. This paper established a novel hierarchical model, i.e., CMC-FMP to achieve SO-CMC that features flexible merging positions for on-ramp vehicles. Unlike the traditional SO-CMC, this model does not get the whole trajectory of all vehicles in one optimization. Instead, its upper-level of tactical planning model mainly solves the optimal merging sequence and vehicles states at several critical time points or positions. Then, planned trajectories and next-step actions for all vehicles are determined through the lower-level of motion planning model based on the critical states optimized by the tactical planning model. A specific decomposition algorithm, MCTS-DA was proposed for solving the tactical model plan efficiently, whose solutions have small gaps (less than $10\%$ ) to the optimal truth values. Based on MCTS-DA, a batch-based scheme is further developed to realize real-time control. 

To evaluate the proposed CMC-FMP, case studies were conducted in different levels and splits of traffic demands and compared with the CMC-SMP which assumes a single fixed merging point at the end of the merging section. The simulation results proved that allowing on-ramp vehicles to merge at flexible positions (CMC-FMP) provides better chances for on-ramp vehicles to merge, which avoids excessive delay for on-ramp vehicles. Meanwhile, better than the CMC-SMP, the proposed CMC-FMP obtained smoother tra 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/7ee8716f3cab44aa8157481efeef3f972474685c3ba3fc0f34a3d394987ec0e7.jpg)



Fig. 16. Impacts of the merging section length.


jectories of on-ramp vehicles which also have less impact on the speed of mainline vehicles. Therefore, CMC-FMP greatly enhanced the performance of the cooperative merging model in improving the efficiency of merging bottlenecks compared to the CMC-SMP. Especially, under high traffic demand with a low demand ratio of on-ramp vehicles, the average delay of vehicles through the merging bottleneck could be greatly reduced by the CMC-FMP. The reduction range was even up to $64\%$ under 1800 veh/h (20-80). In addition, sensitivity analysis revealed that the increase of the $\beta$ and the decrease of the merging section length resulted in low output and high delay of the merging bottleneck. 

Despite the above contributions, this study is still limited and can be further improved from the following aspects. First, in terms of the model structure and formulation, the non-convex and non-linear nature of the tactical planning model led to difficulties in getting optimal solutions. Further improvement should consider the linearization of the model's constraint equations, which can bring great benefit to the computational efficiency. Second, only aiming at the minimal total delay, this paper only optimized the traffic efficiency at the merging bottleneck. Besides, passenger comfort and traffic emission are important evaluation indicators as well. They can be discussed by replacing the objective function. Furthermore, this model assumes a merging bottleneck intersected by a single-lane freeway mainline and a single-lane on-ramp, which is a critical limitation on its application. The future study should also consider the multilane freeway merging area by incorporating the optimized lane-changing control on the mainline (Hu and Sun, 2019). 

This paper emphasizes showing the new structural model and its performance improvement brought about by flexible merging positions. Therefore, only the application of the model to pure CAV flow conditions is discussed. However, the mixed flow traffic is an inevitable phase in CAVs' development and will introduce a more complex situation for merging since HDVs' motions are not fully controllable and are only partially detectable. Therefore, the behavior prediction and information completion of HDV are significant topics for CAV trajectory planning in mixed flow. Data-driven methods (e.g., He et al., 2015; Xie et al., 2019) are supposed to predict trajectories of detected HDVs. Model-based approaches (e.g., Wang et al., 2020) can be applied in vehicle information completion. However, a unified framework for CAV-based merging control under mixed-flow considering the nature of HDVs mentioned above is still an open issue in the literature. We will follow up on those topics in our future study. 

# CRediT authorship contribution statement

Zhixian Tang: Conceptualization, Methodology, Software, Writing - original draft, Writing - review & editing. Hong Zhu: Conceptualization, Methodology, Writing - original draft, Writing - review & editing. Xin Zhang: Writing - review & editing. Miho Iryo-Asano: Writing - review & editing. Hideki Nakamura: Conceptualization. 

# Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Appendix A. Analytic solution of the optimal control model

For solving convenience, the problem of Equations (38)-(45) is transformed as Equations (A1)-(A8) to eliminate the lower bound of the speed to zero. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/0d02a7d29b2374ce79c17bf7800577dec5310ce0be97169bd21024987ff2a25e.jpg)



Fig. 17. An example of piecewise trajectory by optimal control model.


$$
\min  \int_ {0} ^ {t _ {e d}} | a (t) | d t \tag {A1}
$$

s.t. 

$$
\left\{ \begin{array}{l} d x (t) / d t = v (t) \\ d v (t) / d t = a (t) \end{array} \right. \tag {A2}
$$

$$
x (0) = 0 \tag {A3}
$$

$$
x \left(r _ {e d}\right) = x _ {e d} \tag {A4}
$$

$$
v (0) = v _ {s t} \tag {A5}
$$

$$
v \left(t _ {e n d}\right) = v _ {e n d} \tag {A6}
$$

$$
0 \leq v (t) \leq v _ {\max } ^ {\prime} \tag {A7}
$$

$$
a _ {\min } \leq a (t) \leq a _ {\max } \tag {A8}
$$

where $t_{ed} = t_{ed} - t_{st}; x_{ed} = x_{ed} - x_{st} - \nu_{min} t_{ed}$ ; $\nu_{st} = \nu_{st} - \nu_{min}$ ; $\nu_{ed} = \nu_{ed} - \nu_{min}$ ; $\dot{\nu}_{max} = \nu_{max} - \nu_{min}$ . 

The optimal control model outputs piecewise trajectories that have 2 or 3 segments with 1 or 2 switching points between $t = 0$ and $t = t_{ed}$ . The acceleration in each segment is constant as $a_{max}$ , 0, or $a_{min}$ . Fig. 17 displays an example of a piecewise trajectory with three segments and two switching points. The first switching point is denoted as $t_{s1}$ and the second switching point in a three-segment trajectory is denoted as $t_{s2}$ . Given the start state $(0, \nu_{st}^{\prime}, 0)$ and the end state $(t_{ed}^{\prime}, \nu_{ed}^{\prime}, x_{ed}^{\prime})$ , the trajectory of the optimal control model can be obtained through solving Equations (A1)-(A8). By determining the duration of each segment, the shape of a trajectory can be fixed. Solutions can be divided into 9 scenarios as in Table 4. Please refer to Feng et al. (2018) and Yu et al. (2018) for detailed derivation. 

First, denote three threshold values $T_{1}$ , $T_{2}$ , and $T_{3}$ as Equations (A9), (A10), and (A11). 

$$
T _ {1} = \left(D ^ {*} - v _ {s t}\right) / a _ {\max } - \left(D ^ {*} - v _ {e d}\right) / a _ {\min } \tag {A9}
$$

$$
T _ {2} = \left\{ \begin{array}{c} x _ {e d} / v _ {s t} - \left(v _ {e d} ^ {\prime} - v _ {s t} ^ {\prime}\right) ^ {2} / \left(2 v _ {s t} a _ {\min }\right), i f v _ {s t} ^ {\prime} \geq v _ {e d} \\ x _ {e d} ^ {\prime} / v _ {e d} ^ {\prime} + \left(v _ {e d} ^ {\prime} - v _ {s t}\right) ^ {2} / \left(2 v _ {e d} a _ {\max }\right), o. w. \end{array} \right. \tag {A10}
$$

$$
T _ {3} = \left\{ \begin{array}{c} x _ {e d} / v _ {e d} + \left(v _ {e d} ^ {\prime} - v _ {s t} ^ {\prime}\right) ^ {2} / \left(2 v _ {e d} a _ {\min }\right), i f v _ {s t} ^ {\prime} \geq v _ {e d} ^ {\prime} \\ x _ {e d} / v _ {s t} - \left(v _ {e d} ^ {\prime} - v _ {s t} ^ {\prime}\right) ^ {2} / \left(2 v _ {e d} ^ {\prime} a _ {\max }\right), o. w. \end{array} \right. \tag {A11}
$$

where $D^{*} = \sqrt{\left(-2a_{max}a_{min}\pmb{x}_{ed} - a_{min}\nu_{st}^{2} + a_{max}\nu_{ed}^{2}\right) / (a_{max} - a_{min})}$ 

Case 1: $t_{ed} = T_1$ 

$$
t _ {s 1} = \left(v _ {e d} ^ {\prime} - v _ {s t} ^ {\prime} - a _ {\min } T _ {1}\right) / \left(a _ {\max } - a _ {\min }\right) \tag {A12}
$$

Case 2: $T_{1} < t_{ed} < T_{2}$ 

$t_{s1}$ is the smaller root of Equation (A13). 

$$
\frac {a _ {\min} - a _ {\max}}{2 a _ {\min}} a _ {\max} t ^ {2} + \left(\frac {v _ {e d} ^ {*} - v _ {s t} ^ {*}}{a _ {\min}} - t _ {e d} ^ {*}\right) a _ {\max} t + \left(x _ {e d} ^ {*} - \frac {\left(v _ {e d} ^ {*} - v _ {s t} ^ {*}\right) ^ {2}}{2 a _ {\min}} - t _ {e d} ^ {*} v _ {s t} ^ {*}\right) = 0 \tag {A13}
$$


Table 4



Nine cases of piecewise trajectories by optimal control model.


<table><tr><td>Case No.</td><td>Segment 1</td><td>Segment 2</td><td>Segment 3</td></tr><tr><td>Case 1</td><td>a max</td><td>a min</td><td>×</td></tr><tr><td>Case 2</td><td>a max</td><td>0</td><td>a min</td></tr><tr><td>Case 3</td><td>0</td><td>a min</td><td>×</td></tr><tr><td>Case 4</td><td>a max</td><td>0</td><td>×</td></tr><tr><td>Case 5</td><td>a min</td><td>0</td><td>a min</td></tr><tr><td>Case 6</td><td>a max</td><td>0</td><td>a max</td></tr><tr><td>Case 7</td><td>a min</td><td>0</td><td>×</td></tr><tr><td>Case 8</td><td>0</td><td>a max</td><td>×</td></tr><tr><td>Case 9</td><td>a min</td><td>0</td><td>a max</td></tr></table>

$$
t _ {s 2} = t _ {e d} ^ {*} + \left(v _ {s t} ^ {*} + a _ {\max } t _ {s 1} - v _ {e d} ^ {*}\right) / a _ {\min } \tag {A14}
$$

Case 3: $t_{ed} = T_2$ , $\nu_{st} \geq \nu_{ed}$ 

$$
t _ {s 1} = t _ {e d} ^ {\prime} + \left(v _ {s t} ^ {\prime} - v _ {e d} ^ {\prime}\right) / a _ {\min } \tag {A15}
$$

Case 4: $t_{ed} = T_2$ , $\nu_{st} < \nu_{ed}$ 

$$
t _ {s 1} = \left(v _ {e d} - v _ {s t}\right) / a _ {\max } \tag {A16}
$$

Case 5: $T_{2} < t_{ed} < T_{3}$ , $\nu_{st} \geq \nu_{ed}$ 

$$
v _ {s 1} = 0. 5 \left(- 2 a _ {\min } x _ {e d} ^ {2} - v _ {s t} ^ {2} + v _ {e d} ^ {2}\right) / \left(- a _ {\min } t _ {e d} ^ {2} - v _ {s t} ^ {2} + v _ {e d} ^ {2}\right) \tag {A17}
$$

$$
t _ {s 1} = \left(v _ {s 1} - v _ {s t} ^ {\prime}\right) / a _ {\text {m i n}} \tag {A18}
$$

$$
t _ {s 2} = t _ {e d} ^ {*} - \left(v _ {e d} ^ {*} - v _ {s 1}\right) / a _ {\text {m i n}} \tag {A19}
$$

Case 6: $T_{2} < t_{ed} < T_{3}$ , $\nu_{st} < \nu_{ed}$ 

$$
v _ {s 1} = 0. 5 \left(2 a _ {\max} x _ {e d} ^ {*} + v _ {s t} ^ {* 2} - v _ {e d} ^ {* 2}\right) / \left(a _ {\max} t _ {e d} ^ {*} + v _ {s t} ^ {*} - v _ {e d} ^ {*}\right) \tag {A20}
$$

$$
t _ {s 1} = \left(v _ {s 1} - v _ {s t} ^ {\prime}\right) / a _ {\max } \tag {A21}
$$

$$
t _ {s 2} = t _ {e d} ^ {*} - \left(v _ {e d} ^ {*} - v _ {s 1}\right) / a _ {\max } \tag {A222}
$$

Case 7: $t_{ed}^{\prime} = T_{3}$ $\nu_{st}\geq \nu_{ed}^{\prime}$ 

$$
t _ {s 1} = \left(v _ {e d} - v _ {s t} ^ {\prime}\right) / a _ {\text {m i n}} \tag {A23}
$$

Case 8: $t_{ed} = T_3$ , $\nu_{st} < \nu_{ed}$ 

$$
t _ {s 1} = t _ {e d} ^ {*} + \left(v _ {s t} ^ {*} - v _ {e d} ^ {*}\right) / a _ {\max } \tag {A24}
$$

Case 9: $t_{ed} > T_3$ 

$t_{s1}$ is the smaller root of Equation (A25). 

$$
\frac {a _ {\min} - a _ {\max}}{2 a _ {\max}} a _ {\min} t ^ {2} + \left(t _ {e d} ^ {\prime} + \frac {v _ {s t} ^ {\prime} - v _ {e d} ^ {\prime}}{a _ {\max}}\right) a _ {\min} t + \left(t _ {e d} ^ {\prime} v _ {s t} ^ {\prime} + \frac {\left(v _ {e d} ^ {\prime} - v _ {s t} ^ {\prime}\right) ^ {2}}{2 a _ {\max}} - x _ {e d} ^ {\prime}\right) = 0 \tag {A25}
$$

$$
t _ {s 2} = t _ {e d} ^ {\prime} + \left(a _ {\text {m i n}} t _ {s 1} - v _ {e d} ^ {\prime} + v _ {s t} ^ {\prime}\right) / a _ {\max } \tag {A26}
$$

# Appendix B. Tactical planning model for CMC-SMP

CMC-SMP features a single fixed merging point at the end of the merging section $(l_{me})$ . The tactical planning model is different from CMC-FMP. Since the merging point is fixed, cut-by-follower states and cut-by-leader states are not needed for mainline vehicles anymore. Instead, their roles are replaced by $\left(t_{me}^{k}, \nu_{me}^{k}, l_{me}\right)$ , i.e., the state when the mainline vehicle passes the fixed merging point. The modified formulation is presented below. 

$$
\min  \sum_ {k \in \Omega} t _ {z e} ^ {k} + \sum_ {k ^ {\prime} \in \vec {\Omega}} t _ {z e} ^ {k ^ {\prime}} \tag {B1}
$$

s.t. Equations (B2) to (B18). 

- Merging sequence 

$$
\left| \boldsymbol {\Omega} _ {d} \right| + 1 \leq g ^ {k ^ {\prime}} \leq N ^ {m} + 1, \forall k ^ {\prime} \in \Omega^ {\prime} \tag {B2}
$$

$$
g ^ {k ^ {\prime}} \geq g ^ {k ^ {\prime} - 1}, \forall k ^ {\prime} \in \Omega^ {\prime}; k ^ {\prime} - 1 \in \Omega^ {\prime} \tag {B3}
$$

$$
k - M \left(1 - \delta_ {k, k}\right) \leq g ^ {k ^ {\prime}} \leq k + M \left(1 - \delta_ {k, k}\right), \forall k \in \Omega_ {v}; \forall k ^ {\prime} \in \Omega^ {\prime} \tag {B4}
$$

$$
\sum_ {k \in \Omega_ {\nu}} \delta_ {k ^ {\prime}, k} = 1, \forall k ^ {\prime} \in \Omega^ {\prime} \tag {B5}
$$

- Car-following constraints 

$$
t _ {m s} ^ {k} \geq t _ {m s} ^ {k - 1} + \tau + (d + L) / v _ {m s} ^ {k}, \forall k ^ {\prime} \in \Omega_ {a m} ^ {\prime}; k ^ {\prime} - 1 \in \Omega^ {\prime} \tag {B6}
$$

$$
\left(t _ {m s} ^ {\vec {k}}, v _ {m s} ^ {\vec {k}}, l _ {m s}\right) = \left(\widetilde {t} _ {m s} ^ {\vec {k}} - \Delta t, \widetilde {v} _ {m s} ^ {\vec {k}}, l _ {m s}\right), \forall \vec {k} \in \Omega_ {i m} ^ {\prime} \tag {B7}
$$

$$
t _ {z e} ^ {k} \geq t _ {z e} ^ {k - 1} + \tau + (d + L) / v _ {z e} ^ {k}, \forall k ^ {\prime} \in \Omega^ {\prime}; \forall k ^ {\prime} - 1 \in \Omega^ {\prime} \tag {B8}
$$

$$
t _ {z e} ^ {k} \geq t _ {z e} ^ {k - 1} + \tau + (d + L) / v _ {z e} ^ {k}, \forall k \in \Omega ; \forall k - 1 \in \Omega \tag {B9}
$$

$$
t _ {z e} ^ {k} \geq t _ {z e} ^ {k} + \tau + (d + L) / v _ {z e} ^ {k} - M \left(1 - \delta_ {k, k + 1} ^ {\prime}\right), \forall k ^ {\prime} \in \Omega^ {\prime}; \forall k \in \Omega \tag {B10}
$$

$$
t _ {z e} ^ {k} \geq t _ {z e} ^ {k ^ {\prime}} + \tau + (d + L) / v _ {z e} ^ {k} - M \left(1 - \delta_ {k ^ {\prime}, k}\right), \forall k ^ {\prime} \in \Omega^ {\prime}; \forall k \in \Omega \tag {B11}
$$

- Merging constraints 

$$
t _ {m} ^ {k ^ {\prime}} \geq t _ {m} ^ {k ^ {\prime} - 1} + \tau + (d + L) / \nu_ {m} ^ {k ^ {\prime}}, \forall k ^ {\prime} \in \Omega^ {\prime}, k ^ {\prime} - 1 \in \Omega^ {\prime} \tag {B12}
$$

$$
t _ {m e} ^ {k} \geq t _ {m e} ^ {k - 1} + \tau + (d + L) / v _ {m e} ^ {k}, \forall k \in \Omega , k - 1 \in \Omega \tag {B13}
$$

$$
t _ {m} ^ {k ^ {\prime}} \geq t _ {m s} ^ {k ^ {\prime}}, \forall k ^ {\prime} \in \Omega^ {*} \tag {B14}
$$

$$
x _ {m} ^ {k ^ {\prime}} = l _ {m e}, \forall k ^ {\prime} \in \Omega^ {\prime} \tag {B15}
$$

$$
t _ {m e} ^ {k} - t _ {m} ^ {k} \geq \tau + \beta + (d + L) / v _ {m e} ^ {k} - M \left(1 - \delta_ {k, k}\right), \forall k \in \Omega , k ^ {\prime} \in \Omega^ {\prime} \tag {B16}
$$

$$
t _ {m} ^ {k ^ {\prime}} - t _ {m e} ^ {k} \geq \tau + \beta + (d + L) / v _ {m} ^ {k ^ {\prime}} - M \left(1 - \delta_ {k ^ {\prime}, k + 1}\right), \forall k \in \Omega , k ^ {\prime} \in \Omega^ {\prime} \tag {B17}
$$

Fig. 18 displays an example showing the positions where these car-following and merging constraints are applied in the tactical planning model of CMC-SMP. 

- Feasible path constraints 

$$
d \left(t _ {0}, v _ {0} ^ {k}, x _ {0} ^ {k}, t _ {m s} ^ {k}, v _ {m s} ^ {k}, l _ {m s}\right) \leq 0, \forall k ^ {\prime} \in \Omega_ {a m} ^ {*} \tag {B18a}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/eff29d8f-d45e-4246-9e1d-1ee6ed44328d/d8257325b3c29229b6f3d064b28dbadc31f6855d88878b2a89d23a486b7a72e8.jpg)



Fig. 18. An example for car-following constraints and merging constraints in CMC-SMP.


$$
d \left(t _ {m s} ^ {k}, v _ {m s} ^ {k ^ {\prime}}, l _ {m s}, t _ {m} ^ {k}, v _ {m} ^ {k ^ {\prime}}, x _ {m} ^ {k ^ {\prime}}\right) \leq 0, \forall k ^ {\prime} \in \Omega_ {a m} ^ {\prime} \tag {B18b}
$$

$$
d \left(t _ {0}, v _ {0} ^ {k}, x _ {0} ^ {k}, t _ {m} ^ {k}, v _ {m} ^ {k}, x _ {m} ^ {k}\right) \leq 0, \forall k ^ {\prime} \in \Omega_ {i m} ^ {\prime} \tag {B18c}
$$

$$
d \left(t _ {m} ^ {k}, v _ {m} ^ {k}, x _ {m} ^ {k}, t _ {z e} ^ {k}, v _ {z e} ^ {k}, l _ {z e}\right) \leq 0, \forall k ^ {\prime} \in \Omega^ {\prime} \tag {B18d}
$$

$$
d \left(t _ {0}, v _ {0} ^ {k}, x _ {0} ^ {k}, t _ {m e} ^ {k}, v _ {m e} ^ {k}, l _ {m e}\right) \leq 0, \forall k \in \Omega \tag {B18e}
$$

$$
d \left(t _ {m e} ^ {k}, v _ {m e} ^ {k}, l _ {m e}, t _ {z e} ^ {k}, v _ {z e} ^ {k}, l _ {z e}\right) \leq 0, \forall k \in \Omega \tag {B18f}
$$

# References



Cao, W., Mukai, M., Kawabe, T., Nishira, H., Fujiki, N., 2013. Mild merging path generation method with optimal merging point based on MPC. IFAC Proc. Vol. 46 (21), 756-761. https://doi.org/10.3182/20130904-4-JP-2042.00109. 





Cao, W., Mukai, M., Kawabe, T., Nishira, H., Fujiki, N., 2015. Cooperative vehicle path generation during merging using model predictive control with real-time optimization. Control Eng. Pract. 34, 98-105. https://doi.org/10.1016/j.conengprac.2014.10.005. 





Chen, N.a., van Arem, B., Alkim, T., Wang, M., 2021a. A hierarchical model-based optimization control approach for cooperative merging by connected automated vehicles. IEEE Trans. Intell. Transp. Syst. 22 (12), 7712-7725. https://doi.org/10.1109/TITS.2020.3007647. 





Chen, T., Wang, M., Gong, S., Zhou, Y., Ran, B., 2021b. Connected and automated vehicle distributed control for on-ramp merging scenario: a virtual rotation approach. Transp. Res. Part C: Emerg. Technol. 133, 103451. https://doi.org/10.1016/j.trc.2021.103451. 





Chen, X., Chen, X., Zheng, H., Xiao, F., 2021c. Efficient dispatching for on-demand ride services: Systematic optimization via Monte-Carlo tree search. Transp. Res. Part C: Emerg. Technol. 127, 103156. https://doi.org/10.1016/j.trc.2021.103156. 





Davis, L.C., 2006. Effect of cooperative merging on the synchronous flow phase of traffic. Physica A 361 (2), 606-618. https://doi.org/10.1016/j.physa.2005.06.046. 





Ding, J., Li, L., Peng, H., Zhang, Y., 2020. A rule-based cooperative merging strategy for connected and automated vehicles. IEEE Trans. Intell. Transp. Syst. 21 (8), 3436-3446. https://doi.org/10.1109/TITS.2019.2928969. 





Dong, J., Chen, S., Ha, P. Y. J., Li, Y., Labi, S., 2020. A DRL-based Multiagent Cooperative Control Framework for CAV Networks: a Graphic Convolution Q Network. arXiv preprint arXiv:2010.05437. 





Duret, A., Wang, M., Ladino, A., 2020. A hierarchical approach for splitting truck platoons near network discontinuities. Transp. Res. Part B: Methodol. 132, 285-302. https://doi.org/10.1016/j.trb.2019.04.006. 





Feng, Y., Yu, C., Liu, H.X., 2018. Spatiotemporal intersection control in a connected and automated vehicle environment. Transp. Res. Part C: Emerg. Technol. 89, 364-383. https://doi.org/10.1016/j.trc.2018.02.001. 





Gurobi Optimization, LLC, 2020. Gurobi optimizer reference manual. URL: https://www.gurobi.com. 





He, Z., Zheng, L., Guan, W., 2015. A simple nonparametric car-following model driven by field data. Transp. Res. Part B: Methodol. 80, 185-201. https://doi.org/10.1016/j.trb.2015.07.010. 





hou, Y., Graf, P., 2021. Decentralized cooperative lane changing at freeway weaving areas using multi-agent deep reinforcement learning. arXiv preprint arXiv: 2110.08124. 





Hu, X., Sun, J., 2019. Trajectory optimization of connected and autonomous vehicles at a multilane freeway merging area. Transp. Res. Part C: Emerg. Technol. 101, 111-125. https://doi.org/10.1016/j.trc.2019.02.016. 





Japan Society of Traffic Engineers, 2018. Planning and Design of at-grade Intersections - Basic Edition -; Guide for Planning, Design and Traffic Signal Control. Maruzen Co., Ltd. (in Japanese). 





Jing, S., Hui, F., Zhao, X., Rios-Torres, J., Khattak, A.J., 2019. Cooperative game approach to optimal merging sequence and on-ramp merging control of connected and automated vehicles. IEEE Trans. Intell. Transp. Syst. 20 (11), 4234-4244. https://doi.org/10.1109/TITS.2019.2925871. 





C: Emerg. Technol. 116, 102663. https://doi.org/10.1016/j.trc.2020.102663. 





Kockelman, K. M., Ma, J., 2007. Freeway speeds and speed variations preceding crashes, within and across lanes. In: Journal of the Transportation Research Forum, Vol. 46, No. 1424-2016-117787. doi: 10.22004/ag.econ.206875, pp. 43-61. 





Kocsis, L., Szepesvář, C., 2006. Bandit based monte-carlo planning. In: European conference on machine learning. Springer, Berlin, Heidelberg, pp. 282-293. doi: https://doi.org/10.1007/11871842_29. 





Letter, C., Elefteriadou, L., 2017. Efficient control of fully automated connected vehicles at freeway merge segments. Transp. Res. Part C: Emerg. Technol. 80, 190-205. https://doi.org/10.1016/j.trc.2017.04.015. 





Li, Z., Elefteriadou, L., Ranka, S., 2014. Signal control optimization for automated vehicles at isolated signalized intersections. Transp. Res. Part C: Emerg. Technol. 49, 1-18. https://doi.org/10.1016/j.trc.2014.10.001. 





Li, S., Zhang, Y., 2000. An application study of merging theory on designing acceleration lane for expressway. China J. Highway Transport 13 (2), 108-111/126. 





Li, Z., Wang, W., Chen, R., Liu, P., Xu, C., 2013. Evaluation of the impacts of speed variation on freeway traffic collisions in various traffic states. Traffic Inj. Prev. 14 (8), 861-866. https://doi.org/10.1080/15389588.2013.775433. 





Lopez, P.A., Behrisch, M., Bieker-Walz, L., Erdmann, J., Flotterod, Y.-P., Hilbrich, R., Lucken, L., Rummel, J., Wagner, P., Wiessner, E., 2018. Microscopic traffic simulation using SUMO. In: 2018 21st International Conference on Intelligent Transportation Systems (ITSC), pp. 2575-2582. https://doi.org/10.1109/ITSC.2018.8569938. 





Ma, C., Yu, C., Yang, X., 2021. Trajectory planning for connected and automated vehicles at isolated signalized intersections under mixed traffic environment. Transp. Res. Part C: Emerg. Technol. 130, 103309. https://doi.org/10.1016/j.trc.2021.103309. 





Mahmassani, H.S., 2016. 50th anniversary invited article—Autonomous vehicles and connected vehicle systems: Flow and operations considerations. Transp. Sci. 50 (4), 1140-1162. https://doi.org/10.1287/trsc.2016.0712. 





Milanés, V., Godoy, J., Villagrá, J., Pérez, J., 2010. Automated on-ramp merging system for congested traffic situations. IEEE Trans. Intell. Transp. Syst. 12 (2), 500-508. https://doi.org/10.1109/TITS.2010.2096812. 





Mu, C., Du, L., Zhao, X., 2021. Event triggered rolling horizon based systematical trajectory planning for merging platoons at mainline-ramp intersection. Transp. Res. Part C: Emerg. Technol. 125, 103006. https://doi.org/10.1016/j.trc.2021.103006. 





Ntousakis, I.A., Nikolos, I.K., Papageorgiou, M., 2016. Optimal vehicle trajectory planning in the context of cooperative merging on highways. Transp. Res. Part C: Emerg. Technol. 71, 464-488. https://doi.org/10.1016/j.trc.2016.08.007. 





Newell, G.F., 2002. A simplified car-following theory: a lower order model. Transp. Res. Part B: Methodol. 36 (3), 195-205. https://doi.org/10.1016/S0191-2615(00)00044-8. 





Qin, L., Persaud, B., Saleem, T., 2018. Safety evaluation of freeway acceleration lanes based on crashes and simulated conflicts. Can. J. Civ. Eng. 45 (1), 51-60. https://doi.org/10.1139/cjce-2016-0498. 





Ran, B., Leight, S., Chang, B., 1999. A microscopic simulation model for merging control on a dedicated-lane automated highway system. Transp. Res. Part C: Emerg. Technol. 7 (6), 369-388. https://doi.org/10.1016/S0968-090X(99)00028-5. 





Rei, R.J.R., 2018. Monte Carlo Tree Search for Combinatorial Optimization. (Doctoral dissertation, University of Porto, Porto, Portugal). Retrieved from https:// repositorio-aberto.up.pt/bitstream/10216/113507/2/275984.pdf. 





Res. Rec. 2674 (10), 363-374. https://doi.org/10.1177/0361198120935873. 





Rios-Torres, J., Malikopoulos, A.A., 2016. A survey on the coordination of connected and automated vehicles at intersections and merging at highway on-ramps. IEEE Trans. Intell. Transp. Syst. 18 (5), 1066-1077. https://doi.org/10.1109/TITS.2016.2600504. 





Sun, J., Ouyang, J., Yang, J., 2014. Modeling and analysis of merging behavior at expressway on-ramp bottlenecks. Transp. Res. Rec. 2421 (1), 74-81. https://doi.org/10.3141/2421-09. 





Sun, Z., Huang, T., Zhang, P., 2020. Cooperative decision-making for mixed traffic: A ramp merging example. Transp. Res. Part C: Emerg. Technol. 120, 102764. https://doi.org/10.1016/j.trc.2020.102764. 





Treiber, M., Hennecke, A., Helbing, D., 2000. Congested traffic states in empirical observations and microscopic simulations. Phys. Rev. E 62 (2), 1805-1824. 





Wang, G., Hu, J., Li, Z., Li, L., 2021. Harmonious lane changing via deep reinforcement learning. IEEE Trans. Intell. Transp. Syst. https://doi.org/10.1109/TITS.2020.3047129. 





Wang, M., Daamen, W., Hoogendoorn, S.P., van Arem, B., 2014. Rolling horizon control framework for driver assistance systems. Part I: Mathematical formulation and non-cooperative systems. Transp. Res. Part C: Emerg. Technol. 40, 271-289. https://doi.org/10.1016/j.trc.2013.11.024. 





Wang, Y., Wei, L., Chen, P., 2020. Trajectory reconstruction for freeway traffic mixed with human-driven vehicles and connected and automated vehicles. Transp. Res. Part C: Emerg. Technol. 111, 135-155. https://doi.org/10.1016/j.trc.2019.12.002. 





Wang, Y., E, W., Tang, W., Tian, D., Lu, G., Yu, G., 2013. Automated on-ramp merging control algorithm based on internet-connected vehicles. IET Intel. Transport Syst. 7 (4), 371-379. https://doi.org/10.1049/iet-its.2011.0228. 





Wang, X., Miyagi, T., Takagi, A., Ying, J., 2007. Analysis of the effects of acceleration lane length at merging sections by using micro-simulations. In: Proceedings of the Eastern Asia Society for Transportation Studies Vol. 6 (The 7th International Conference of Eastern Asia Society for Transportation Studies, 2007), 334-334. doi: https://doi.org/10.11175/eastpro.2007.0.334.0. 





Xie, D.F., Fang, Z.Z., Jia, B., He, Z., 2019. A data-driven lane-changing model based on deep learning. Transp. Res. Part C: Emerg. Technol. 106, 41-60. https://doi.org/10.1016/j.trc.2019.07.002. 





Xie, Y., Zhang, H., Gartner, N.H., Arsava, T., 2017. Collaborative merging strategy for freeway ramp operations in a connected and autonomous vehicles environment. J. Intell. Transp. Syst. 21 (2), 136-147. https://doi.org/10.1080/15472450.2016.1248288. 





Yu, C., Feng, Y., Liu, H.X., Ma, W., Yang, X., 2018. Integrated optimization of traffic signals and vehicle trajectories at isolated urban intersections. Transp. Res. Part B: Methodol. 112, 89-112. https://doi.org/10.1016/j.trb.2018.04.007. 





Zhi, Y.F., Zhang, J., Shi, Z.K., 2009. Research on design of expressway acceleration lane length and merging model of vehicle. China J. Highway Transp. 22 (2), 93-97. 





Zhou, Y., Chung, E., Bhaskar, A., Cholette, M.E., 2019. A state-constrained optimal control based trajectory planning strategy for cooperative freeway mainline facilitating and on-ramp merging maneuvers under congested traffic. Transp. Res. Part C: Emerg. Technol. 109, 321-342. https://doi.org/10.1016/j.trc.2019.10.017. 

