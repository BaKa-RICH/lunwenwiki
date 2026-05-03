# Cooperative control of CAVs in the merging area of multi-lane mainline and dual-lane ramps on freeways

Yi Wang1, Jian Xiang 2, *, Junliang Pan2, Jie Wang2, Tao Chen2 and Hao Wang2,3 

1School of Hydraulic and Ocean Engineering, Changsha University of Science & Technology, Changsha 410114, Hunan, China; 

2School of Transportation, Changsha University of Science & Technology, Changsha 410114, Hunan, China; 

3Hunan Communications Research Institute Co., Ltd., Changsha 410114, Hunan, China. 

∗Corresponding author. E-mail: dr_xiang2022@163.com 

# Abstract

This study introduces a multi-area cooperative merging control strategy to enhance the safety and efficiency of connected and autonomous vehicles (CAVs) at freeway merging areas with multiple mainline lanes and a dual-lane ramp. The strategy integrates lane changing in advance tactics for upstream mainline vehicles and speed regulation for ramp vehicles into a structured control framework. This framework comprises distinct areas for proactive mainline lane changing in advance, ramp speed regulation and cooperative merging. For the mainline lane-changing area, we propose a strategy that relies on maintaining a minimum safety distance and optimizing speed benefits, thereby enhancing merging opportunities for ramp vehicles and balancing downstream traffic flows. In the ramp speed regulation area, a vehicular speed control model is established, utilizing a ‘FIFO rule’ based on the vehicles’ arrival times at the acceleration lane start, coupled with a virtual platoon concept to synchronize and optimize platoon speeds for efficient travel on ramps. In the cooperative merging area, vehicle trajectories on the mainline and ramp are optimized in a rolling horizon manner, facilitating seamless integration of ramp vehicles into the mainline. Simulation results indicate that our proposed cooperative control method significantly surpasses uncontrolled and trajectory-only optimization approaches in control efficiency across varying traffic demands. This method demonstrates notable advancements in average speed, delay reduction and fewer stops, with minimized fluctuations and increased control stability. Additionally, the cooperative control approach demonstrates superior adaptability across different numbers of ramp lanes, with scenarios involving dual-lane ramps exhibiting a more pronounced advantage. 

Keywords: intelligent network environment; ramp merging area; multi-area cooperative merging control; lane-changing strategy; vehicle trajectory optimization 

# 1. Introduction

Freeway merging areas are commonly recognized as bottleneck sections where the frequent joining of ramp vehicles into the mainline can cause stop-and-go traffic or even complete interruptions in flow. These areas frequently experience congestion and accidents, posing significant traffic safety risks [1]. Traditionally, traffic control in these areas has utilized variable speed limit control [2, 3] and ramp metering [4, 5] from a macroscopic perspective to enhance merging efficiency. Typically, these controls are applied to simpler configurations, such as single or double mainline lanes with a single ramp lane [6]. However, with increasing vehicle ownership and freeway expansion, merging areas now often feature multiple lanes on both the mainline and the ramp, rendering traditional macroscopic traffic control methods inadequate for these complex scenarios. In recent years, advancements in wireless communication, artificial intelligence, 5G technology and cloud computing have paved the way for the development of CAVs [7]. The integration of big data analytics with vehicle-to-vehicle (V2V), vehicle-to-infrastructure (V2I) and vehicle-to-cloud (V2C) communications supports dynamic interaction and real-time information optimization. This technological synergy enables real-

time, vehicle-level control in freeway merging areas and facilitates the microscopic optimization of vehicle trajectories, thereby enhancing the safety and efficiency of vehicle flow [6, 8]. 

The development of CAV technologies, integrating advanced capabilities such as wireless communication, 5G and artificial intelligence, has significantly enhanced safety and traffic efficiency on freeways [9], and it can significantly reduce energy consumption [10]. Research indicates that CAV technologies can increase the capacity of road segments by $20 \%$ to $5 0 \%$ , particularly on freeways [11]. Merging areas, critical bottlenecks on freeways, are often compromised by frequent merging and lane-changing manoeuvres from ramp vehicles and unsafe or inefficient yielding by mainline vehicles [7]. The intrinsic real-time communication capabilities of CAV technology facilitate the execution of optimal control commands, enabling precise vehicle-level control. Studies have shown that optimal control algorithms for individual vehicles significantly improve performance [12]. Despite the clear benefits of CAV technology in managing freeway merging, much of the existing research has been limited to scenarios involving singlelane ramps merging into one or two mainline lanes [12, 13]. There is a notable gap in effective control methods for more complex merging scenarios, such as those involving multi-lane ramps and 

multi-lane mainlines. This paper addresses the merging control challenges in such complex scenarios, focusing on merging areas with multiple mainline lanes and dual-lane ramps. 

In the context of freeway merging areas with multi-lane mainlines and multi-lane ramps, cooperative merging control for CAVs emerges as a critical research area in vehicle-road cooperation. However, existing research exhibits several limitations: (1) The cooperative control between mainline multi-lane and ramp vehicles is insufficient. The strategy of having vehicles in the outermost lane of the mainline change lanes inward in advance to create gaps for ramp vehicles still needs optimization. Therefore, current methods that consider only single-lane mainline control are not suitable for merging areas on multi-lane freeways. (2) Current research almost never considers multi-lane ramps. In practice, dual-lane ramps have seen numerous real-world engineering applications. However, the merging control and vehicle trajectory optimization for multi-lane ramps—especially the trajectory optimization for CAV platoons—remain under-researched. (3) Fixed merging points in merging control. Most studies adhere to a predetermined merging point, typically at the end of the acceleration lane [14]. However, the entire acceleration lane offers multiple potential merging points. An optimal control approach should enable merging at various points along this lane to enhance flexibility and efficiency. (4) Assumptions on ramp vehicle speed limits and lane changing. Many studies assume uniform speed limits for both ramp and mainline vehicles. When assessing lane-changing manoeuvres, the focus is usually on spatial gaps with adjacent vehicles in the target lane. However, considering speed benefits is crucial to ensure vehicles do not significantly reduce their speed post lane change, which would impact overall traffic flow. Addressing these gaps is essential for advancing the effectiveness of CAV technologies in complex multi-lane merging scenarios. 

To address the aforementioned gaps, this paper focuses on a merging scenario with a multi-lane mainline and a dual-lane ramp. We propose a cooperative control method for CAVs that integrates a pre-lane-changing strategy on the mainline and optimizes ramp vehicle trajectories using a virtual platoon concept. The merging control problem is formulated as a time-discrete nonlinear programming problem, ensuring safety through constraint conditions and achieving optimal merging efficiency. The main contributions of this paper are as follows: 

1) For the merging scenario of multi-lane mainlines and ramps, the merging area is divided into multiple control areas, and a multi-areas cooperative merging control framework is constructed, encompassing the mainline, ramp and merging area. 

2) On the upstream section of the mainline in the merging area, a lane-changing strategy that considers both driving safety and efficiency is proposed. This strategy is based on the minimum safe following distance and speed benefits, facilitating vehicles that comply with lane-changing rules to move to the center or innermost lanes in advance. This creates as many merging gaps as possible on the outermost lane and promotes balanced lane occupancy rates downstream in the merging area. 

3) On the upstream entrance ramp of the merging area, the passage order of CAVs for the two lanes of the ramp is determined based on the ‘FIFO rule’ and the concept of virtual platoons. Through cyclical rolling trajectory optimization, it is ensured that all CAVs in the queue avoid collisions within a cycle and reach the beginning of the merging area at the maximum speed, thus enhancing the traffic efficiency on the ramp. 

4) In the cooperative merging area, a CAV trajectory optimization model is established for the vehicles on the mainline and the ramp acceleration lane, based on cyclical rolling optimization. This model guides the CAVs on the ramp to merge into the mainline at the end of the cycle, achieving coordinated merging. 

The remainder of this paper is structured as follows. Section 2 briefly reviews the literature. Section 3 details the proposed control method: Section 3.1 introduces the research scenario and assumptions, Section 3.2 constructs the multi-area cooperative merging control framework, Section 3.3 explains the upstream mainline CAV lane-changing strategy considering velocity benefits, Section 3.4 develops a speed optimization method for CAVs on the dual-lane ramp using a virtual platoon, and Section 3.5 presents a cyclical rolling optimization method for CAV trajectories. Section 4 covers the simulation platform and experiments, with Section 4.1 setting the simulation scene and parameters and Section 4.2 analysing the simulation results. Finally, Section 5 concludes the paper and offers suggestions for future research. 

# 2. Literature review

Cooperative merging control in complex freeway merging areas has become a popular area of research in recent years. Li et al. [15] modelled the merging time intervals but did not address effective merging control. Currently, there are several methods available to tackle the merging control problem. In addition to ramp metering and variable speed limit controls that do not require CAV technology, there are primarily two major categories: rule-based merging controls [16–24] and optimization-based merging controls [25– 34]. Additionally, a few studies have discussed other merging sequence and trajectory coordination optimization control methods [35–38]. 

# (1) Rule-based merging control methods

Rule-based merging control methods coordinate vehicle movements on the mainline and ramp through predefined rules. These rules guide vehicles to cooperatively merge, aiming to achieve stable traffic flow in the merging area. The control model focuses on the interaction between ramp vehicles and potentially conflicting mainline vehicles, orchestrating coordinated control to enhance traffic efficiency. Commonly used rule-based methods include the FIFO rule [16, 17] and the ‘Local Gap Optimization’ concept [18 23]. 

Under the FIFO rule, vehicles merge based on their order of arrival or distance from the merging area. This approach promotes smooth traffic flow and prevents the stop-and-go phenomenon, which often leads to congestion. Rios-Torres and Malikopoulos [16] proposed an optimization framework based on the FIFO rule to optimize the cooperative merging sequence of CAVs in freeway merging areas. Similarly, Ding et al. [17] applied this rule to develop a CAV cooperative merging strategy, designing a rule-based algorithm that uses assigned arrival times to determine the merging order. While these methods benefit from reduced computational complexity, their simplicity may result in suboptimal travel time efficiency as they do not account for the dynamic characteristics of traffic flow. 

Another rule-based approach is founded on the concept of ‘local gap optimization’, where mainline vehicles provide gaps for ramp merging vehicles through speed adjustment or lane changing in advance [18], resulting in a locally optimal solution. In studies focusing on providing merging gaps through upstream speed 

adjustments on the mainline, Zhang et al. [19] utilized V2I technology to identify the minimum safe gap on the outer lane of the mainline that meets merging criteria or to adjust the speed of mainline vehicles in the outer lane to create this gap. This strategy guides ramp vehicles to merge smoothly into the mainline, significantly reducing traffic delays and conflicts in the merging area. Zhou et al. [20] developed a new cooperative intelligent driver model based on the traditional intelligent driver model, which controls the mainline vehicles in the merging area to actively accelerate or decelerate upstream to provide larger gaps for merging vehicles. Yang et al. [21] proposed a multi-lane centralized cooperative control strategy based on cooperative game theory for multi-lane mainline merging scenarios. The strategy achieves safe cooperative merging of vehicles based on merging rules and utilizes the Pontryagin principle to derive the analytical solutions for the optimal longitudinal control of all vehicles. Some studies create gaps by having upstream mainline vehicles change lanes in advance, such as the rule-based lanechanging strategy proposed by Shi et al. [22] for freeways with two main lanes and a single ramp lane, which allows some vehicles in the outer main lane to change lanes in advance to provide gaps for ramp merging vehicles. These methods only consider individual vehicle merging gaps and do not address multi-vehicle or flow-level merging rules. A limited number of studies coordinate gaps for multiple vehicles merging from ramps through platooning. For instance, Xu et al. [23] proposed a platoon-based CAV cooperative merging strategy, where vehicles in the same lane with headways below a predetermined threshold are treated as a platoon. This strategy provides gaps for merging vehicles while maintaining a constant merging sequence within the platoon, achieving a good balance between computational complexity and traffic flow control efficiency. Zhu et al. [24] introduced a flowlevel CAV cooperative merging strategy for multi-lane freeways, actively creating gaps by adjusting mainline vehicle speeds and forming platoons when a sufficient number of ramp vehicles accumulate, thus coordinating the merging of mainline and ramp vehicles. 

In rule-based merging control methods, solutions are easily obtainable with low computational overhead, enabling quick determination of merging sequences and high control efficiency. However, these methods typically produce locally optimal solutions without guaranteeing global optimality in merging sequences, making it difficult to achieve system-wide optimal control in continuous traffic flows. 

# (2) Optimization-based merging control methods

Optimization-based approaches transform complex merging control issues into optimization problems. They aim for a globally optimal solution by constructing models with explicit objective functions and constraints, optimizing the trajectories of all merging vehicles to achieve an optimal merging control solution. These control methods are categorized into centralized and distributed control strategies [25]. 

In centralized control methods, a central controller is responsible for decision-making for all vehicles involved in the merging process within the system. For example, Jing et al. [26] proposed a cooperative optimization framework and algorithm based on multi-vehicle game theory. Within this framework, the central controller collects information from vehicles entering the merging area and globally optimizes coordination by treating each vehicle as an agent, thus minimizing the global cost of travel time, fuel consumption and passenger comfort. Jiang et al. [27] 

introduced a centralized cooperative merging control method for CAVs, established a centralized ramp merging cooperative control model and transformed it into a nonlinear optimization problem through discretization, which was solved using the NOMAD algorithm. Wang et al. [28] researched centralized CAV cooperative merging control methods, translating the optimization of merging sequences involving special CAVs into a search for the optimal sequence set based on game theory. They determined the optimal merging sequence using a cooperative game payoff matrix and applied Pontryagin’s maximum principle to solve for the longitudinal optimal trajectory of merging vehicles at minimal strategy cost. Meng et al. [29] developed an optimizationbased centralized ramp merging cooperative control method capable of enhancing fuel economy and driving safety in ramp traffic. 

In distributed control methods, every vehicle in the system determines its own control strategy based on information received from other vehicles on the mainline and ramp. Uno et al. [30] were the pioneers in proposing the concept of cooperative merging with virtual vehicles for ramps, a distributed control method that maps virtual vehicles onto the mainline before the physical merging, enabling a safer and smoother merging operation. Building on the virtual vehicle concept, Chen et al. [31] proposed a CAV distributed cooperative merging control strategy based on virtual rotation. This strategy employs distributed feedback and feedforward longitudinal controllers, transforming the ramp vehicle merging challenge into a virtual vehicle car-following problem, reducing the complexity and dimensionality of cooperative CAV merging control. Continuing with the virtual vehicle-following control strategy, Chen et al. [32] expanded capacity analysis by considering the stochastic traffic arrival patterns of both mainline and ramp CAVs. Beyond the virtual vehicle concept, other distributed methods for CAV merging control exist, such as the method proposed by Wang et al. [33]. Road-side units (RSUs), through wireless communication technologies, receive information on the speed and position of vehicles on the mainline and ramp to predict the time of vehicles’ arrival at the merging point and determine the merging order. Subsequently, a control algorithm establishes each vehicle’s acceleration, enabling vehicles to adjust their speed and position in advance for smooth and orderly merging. Zhou et al. [34] developed a vehicle trajectory planning method for ramp CAV coordination that articulates the planning tasks of ramp and mainline vehicles as two correlated distributed optimal control problems. 

Optimization-based merging control methods enable control over each individual vehicle, achieving the system’s optimal solution. However, these methods generally require the extraction and computation of the speed and acceleration of all vehicles within the control area, resulting in complex and time-consuming calculations, yet they yield the optimal merging sequence. 

# (3) Other approaches for merging sequence optimization and vehicle trajectory control

Currently, there are also various other methods employed for the synergistic optimization of merging sequences and vehicle trajectories. For instance, Wang et al. [35] proposed a CAV cooperative merging control method for scenarios involving three mainline lanes and a single ramp lane on freeways. This approach commences by optimizing the vehicle lane-changing conditions, introducing a rule-based strategy that facilitates lane changing in advance by upstream mainline vehicles to create gaps for ramp vehicles. Subsequently, a time-discrete vehicle trajectory optimiza-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/2535f029cfc106bd20f18330c54c1fdf3f68c35e6236fc4c86e3941f33065a88.jpg)



Fig. 1. Collaborative merging scenario on a multi-lane mainline with dual-lane ramp on a freeway.


tion model is presented, which iteratively refines the driving trajectories of vehicles within the merging area in a cyclical manner. Chen et al. [36] formulated and solved a mixed integer nonlinear programming model for the cooperative merging of mainline and ramp traffic flows in freeway ramp merging areas. The model is capable of simultaneously optimizing the trajectories and merging sequences of multiple vehicles, thereby enhancing traffic efficiency and ensuring safety. Irshayyid et al. [37] provided a comprehensive review of research on merging sequence optimization and vehicle trajectory control in ramp merging areas using reinforcement learning. Various methodologies have been proposed, employing reinforcement learning techniques to facilitate the safe and effective integration of CAVs into freeway mainline traffic from ramps. For example, Li et al. [38] designed an interactive merging strategy based on multi-agent deep reinforcement learning, enabling CAVs on the ramp to consider the dynamic reactions of mainline vehicles, thus coordinating between mainline and ramp traffic to improve the overall safety, efficiency and comfort of the system. 

In summary, although numerous control strategies and solution algorithms have been developed for freeway merging control, most existing studies focus on scenarios involving single-lane or dual-lane mainlines and single-lane ramps. There is a lack of research on optimizing merging sequences and vehicle trajectories in scenarios where both the mainline and ramp have multiple lanes. This paper addresses this research gap by proposing a cooperative merging control method for freeway merging areas with multi-lane mainlines and dual-lane ramps. The method first optimizes lane changes for upstream mainline vehicles based on speed gain to provide ramp vehicles with as many merging gaps as possible. Meanwhile, upstream ramp vehicles optimize their speed based on the concept of virtual queues. Notably, the optimization of mainline lane changes and ramp speed adjustments are conducted independently. Subsequently, a rolling optimization of vehicle trajectories is implemented for all vehicles within the cooperative merging area. The effectiveness of the proposed method is verified through simulations in the SUMO software. 

# 3. Methodology

# 3.1. Scenario description and assumptions

The merging scenario for a multi-lane mainline and dual-lane ramp on an intelligent connected freeway is depicted in Fig. 1, with the ramp’s lanes merging with the mainline via a parallel acceleration lane. The freeway establishes a communication network through RSUs, which acquire real-time data on all vehicles’ speeds, accelerations and positions within the system and issue control commands to the vehicles. This paper delineates the merging area and its surrounding upstream and downstream sections, as well as the ramp, into six areas: Area $\mathrm { L } _ { 1 }$ is the upstream free-driving area of the mainline, where vehicles proceed under normal conditions; Area $\mathrm { L } _ { 2 }$ is the upstream lane-changing area of the mainline, where vehicles begin to receive control instructions from RSUs and conduct lane changing in advance if lanechanging rules are met; Area $\mathrm { L } _ { 3 }$ is the collaborative merging area, where mainline vehicles are prohibited from changing lanes, and RSUs control the merging vehicles’ trajectories based on an optimization model, allowing ramp vehicles to merge into the mainline after completing trajectory optimization on the acceleration lane; Area $\mathrm { L } _ { 4 }$ is the downstream free-driving area of the mainline, where vehicles exit the merge control and proceed freely; Area $\mathrm { L } _ { 5 }$ is the upstream free-driving area of the ramp; and Area $\mathrm { L } _ { 6 }$ is the upstream speed adjustment area of the ramp, facilitating ramp vehicles to safely and efficiently enter the acceleration lane at high speeds. 

In simplifying the vehicle cooperative control optimization process, this study is predicated on the following assumptions [12] for subsequent discussions: 

1) All vehicles are CAVs capable of V2V and V2I communications. They can acquire operational data from surrounding vehicles and receive control commands from RSUs, complying fully with these instructions. 

2) Communication delays are not considered, allowing for realtime exchange of information between vehicles and between vehicles and infrastructure. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/a8340d852b86e221258e5564d97d83f66681936cb3ba9420861fa1611ec7744c.jpg)



Fig. 2. Multi-area cooperative merging control framework.


3) Lateral trajectory planning and control for vehicle lane changing are not considered. It is assumed that within the mainline area L and ramp area L , vehicles can change lanes only once and cannot perform cross-lane changes. 

# 3.2. Multi-areas collaborative control framework

We have established a multi-area collaborative merging control framework that considers proactive lane changing for upstream mainline vehicles based on velocity benefits, speed optimization for ramp vehicles using virtual platooning and cooperative trajectory optimization in the merging area, as illustrated in Fig. 2. When mainline vehicles enter area $\mathrm { L } _ { 2 }$ or ramp vehicles enter area L , the system detects all vehicle state information within these areas, triggering the multi-area collaborative control strategy. Here is a step-by-step breakdown of how this process works. 

In the upstream mainline area of the merge area, the system triggers a proactive lane-changing strategy within area $\mathrm { L } _ { 2 }$ upon detecting incoming ramp vehicles. This approach begins from the innermost lane and progresses outwards, examining vehicles in each lane to determine if they meet predefined thresholds for minimum safe separation and velocity enhancement relevant to lane changing. If these conditions are met, vehicles systematically move towards the adjacent inner lane, creating suitable merging gaps for ramp vehicles. Vehicles in the outermost lane that do not change lanes in advance will, upon exiting area L , participate in subsequent collaborative trajectory optimization with vehicles from the ramp acceleration lane. Conversely, in the absence 

of ramp vehicles, the system refrains from initiating lane changing in advance and subsequent trajectory optimization strategy, allowing vehicles to maintain their course within their respective lanes. 

In the upstream ramp area of the merge area, a velocity control strategy is triggered when vehicles are detected in Area L . This strategy begins by predicting the arrival times of vehicles at the start of the acceleration lane. Based on these times, the FIFO rule is applied to determine the merging order, which is then used to form a virtual platoon. Continuous velocity adjustments are made as vehicles approach the merging area’s acceleration lane, culminating in cooperative trajectory optimization with mainline vehicles to facilitate the merge. In the absence of mainline vehicles, ramp vehicles can complete the merging process directly without velocity adjustments or subsequent trajectory optimization. 

# 3.3. Consider velocity-benefit-orientated lane changing in advance strategy for mainline CAVs

On multi-lane mainline freeways, when the traffic flow is high on the center lanes, it is difficult for vehicles in the outermost lane to find suitable gaps for lane changing to the center lane, resulting in dense flow and potential congestion in the merging area downstream on the outermost lane. However, if the traffic flow is low on the innermost or center lanes, and there are sufficient gaps for lane changing, the system can control some vehicles on the center lane to change lanes towards the inner direction, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/4d16258ca4407207adb391f1740b42fbc87f43d57e0b6c8290ba678899ccbb64.jpg)



Fig. 3. Mainline vehicle lane-changing flowchart.


providing more opportunities for the outermost lane vehicles to lane change in advance into the inner center lane, thus creating more gaps for ramp acceleration lane vehicles to merge safely into the mainline in area L . 

In area L , vehicles must satisfy safety gap requirements before initiating a lane change, and upon completion of a lane change, a vehicle should attain a definite speed advantage. Lane changes are executed only when both the minimum safety gap and speed constraints are met concurrently; otherwise, vehicles continue in their current lane. Ensuring balanced utilization of lane capacities and even occupancy rates downstream of the merging area, this paper employs the methodology outlined in Refs. [12, 35] to develop a lane-changing strategy founded on minimum safe following distance and speed benefits. 

Vehicles satisfying lane-changing criteria execute lane changes towards the adjacent inner lane, adhering to a protocol that initiates with vehicles in the center lane n changing towards the innermost lane, then progressively expanding outwards until vehicles in the outermost lane identify a suitable gap and successfully change lane to center lane 1. The lane-changing sequence proceeds as follows: from center lane n to the innermost lane, from center lane n–1 to center lane n and so on, until from the outermost lane to center lane 1. The lane-changing procedure under this strategy is illustrated in Fig. 3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/11c7210eb5af9926f2168999e71312c2fde38c0b85a2cfdea251fc55ac0f1132.jpg)



Fig. 4. Schematic diagram of mainline vehicle positions.


As illustrated in Fig. 4, this paper uses the example of a vehicle in a mainline center lane changing to the adjacent inner lane to discuss the minimum safety gap and speed benefit associated with lane changing (the decision-making process for vehicles in the outermost lane changing to center lane 1 is analogous). In this scenario, vehicle B represents the lane-changing vehicle in the center lane, while vehicles E and D represent the leading and following vehicles, respectively, in the adjacent inner lane. 

# (1) Minimum lane-changing safety gap

According to Fig. 4, at any given moment t, to prevent collisions, vehicle B will not attempt to follow vehicle E at a time interval less than the minimum safety headway. Additionally, to prevent scenarios where vehicle B’s speed becomes critically low (approaching zero), resulting in an insufficient following distance under the control of the minimum safety headway, it is imperative to define a minimum safety distance to ensure the safety of the lane change [12]. 

Thus, the minimum safe following distance between vehicle B and vehicle E is denoted by $\mathrm { H _ { B } }$ , and the value is taken as the following distance of vehicle B under the control of the minimum safety headway, or taken as the maximum of the minimum safety distances specified in Ref. [13], as shown in Eq. (1). Similarly, vehicle B must also consider the minimum safe following distance with the trailing vehicle D, denoted by $\mathrm { H _ { D } }$ , as shown in Eq. (2): 

$$
H _ {B} = \max  \left(v _ {B} t _ {0}, s _ {0}\right) \tag {1}
$$

$$
H _ {D} = \max  \left(v _ {D} t _ {0}, s _ {0}\right) \tag {2}
$$

where $\boldsymbol { v } _ { \mathrm { B } }$ and $v _ { \mathrm { D } }$ denote the velocities of vehicles B and D at time t, respectively; t0 represents the minimum safety headway; and s0 signifies the minimum safety distance. 

When vehicle B intends to change lanes to the adjacent inner lane at time t, the positional relationship between vehicle B and vehicles D and E must satisfy the following constraints: 

$$
S _ {E} (t) - S _ {B} (t) \geq H _ {B} + L \tag {3}
$$

$$
S _ {B} (t) - S _ {D} (t) \geq H _ {D} + L \tag {4}
$$

where S (t), $S _ { \mathrm { E } } ( { \sf t } )$ and $S _ { \mathrm { D } } ( \mathrm { t } )$ respectively represent the distances of vehicles B, E and D from the starting point of the area $\mathrm { L } _ { 2 }$ at time t; L denotes the length of the vehicle itself. 

# (2) Speed gain

At any time t, it is necessary to consider whether vehicle B can achieve a speed increase or maintain its original lane speed after changing lanes. If the speed of the leading vehicle E is less than that of yehicle B.then after changing lanes,yehicle B willbe subjected to a reduced speed due to the limiting of vehicle E, thereby not obtaining a speed benefit. If the speed of the following vehicle D is significantly low, it indicates that the traffic flow in the target 

lane is unstable with large speed fluctuations, making it unwise for vehicle B to change lanes at this time. 

Therefore, vehicle B can meet the speed constraint condition for lane changing only when the average speed of vehicles D and E at time t is greater than the speed of vehicle B, and the speed of vehicle E is greater than that of vehicle B [35]: 

$$
v _ {B} <   \frac {v _ {D} + v _ {E}}{2} \tag {5}
$$

$$
v _ {B} <   v _ {E} \tag {6}
$$

where $\boldsymbol { \mathrm { { } \mathrm { { } } v _ { E } } }$ denotes the speed of the vehicle E at time t. 

# 3.4. Virtual platoon-based speed optimization for CAVs on ramps

Under dual-lane ramp conditions, vehicles in different lanes must compete to enter the acceleration lane. When traffic flow is high, vehicles may have to stop at the beginning of the merging area to wait for their turn to merge into the cooperative merging area, resulting in significant travel delays. Therefore, for the scenario of dual-lane ramp merging, this paper proposes a vehicle speed control model for the ramp area preceding the start of the merging area. Initially, the model predicts the arrival times of vehicles on different ramp lanes at the start point of the merge area. Based on these predicted times, vehicles are sequentially organized into a virtual platoon following the FIFO rule. Subsequently, speed regulation is applied to each vehicle within this virtual platoon to ensure conflict-free arrival at the start point and a smooth entry into the cooperative merge area. The speed control for ramp vehicles is executed in a rolling fashion as delineated in Section 3.5. 

# (1) Virtual platoon on a dual-lane ramp

When vehicles enter the speed control area L on the ramp, RSUs extract data on their speed, acceleration and position. Utilizing the state information of the vehicles and the current time, the system predicts their arrival times at the beginning of the merge area. Thereafter, the order of entry into the acceleration lane is determined following the FIFO rule. After the entry sequence is determined, vehicles from the two distinct lanes in the ramp area $\mathrm { L } _ { 6 }$ are mapped onto a single lane to form a virtual platoon. For any vehicle within this configuration, its leader may be located in the same lane or in a different lane. When in the same lane, the leading vehicle is identified as the actual leader of the following vehicle. Conversely, when the vehicles are in different lanes, the leading vehicle is designated as the virtual leader of the vehicle behind it. Fig. 1 depicts a virtual platoon on the ramp, consisting of five vehicles, where vehicle 1 on ramp lane A is the virtual leader of vehicle 2 on ramp lane B, and vehicle 3 on ramp lane A is the actual leader of vehicle 4 on ramp lane A. 

Ensuring the efficiency of the merging area traffic, ramp vehicles must accelerate to a certain merging speed to achieve efficient merging. However, they cannot accelerate indefinitely; therefore the predicted maximum speed of the vehicles should consider the impact of speed limits. The process of predicting the speed of ramp vehicles, taking into account the impact of ramp speed limits, is as follows: 

In the computational process, the ramp speed limit and the initial speed of vehicles are known factors. Therefore, assuming the vehicle accelerates at its maximum acceleration, one can calculate the possible minimum acceleration time $\mathrm { { t } _ { m i n } }$ required for a vehicle to reach the starting point of the acceleration lane (the beginning of the merge area), as expressed in Eq. (7): 

$$
t _ {\min } = \frac {v _ {\mathrm {r} - \max } - v _ {0}}{a _ {\max }} \tag {7}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/9bf2c3d1887d6f8034077ef15d658b2f8ba4a5c5a53d3a1801b11d7f0e61af8d.jpg)



Fig. 5. Time-variation of speed for a ramp vehicle transitioning from uniform acceleration to constant speed travel.


where $v _ { 0 }$ denotes the initial velocity of the vehicle, $\mathrm { m } / \mathrm { s }$ . 

Similarly, the minimum acceleration distance $S _ { \mathrm { m i n } }$ required for a vehicle to reach the starting point of the acceleration lane can be calculated. The formula is as follows: 

$$
S _ {\min } = \frac {v _ {\mathrm {r} - \max } ^ {2} - v _ {0} ^ {2}}{2 a _ {\max }} \tag {8}
$$

The distance S from the vehicle’s current position at time t to the beginning of the acceleration lane is known; hence: 

1) If $S _ { \mathrm { m i n } } \leq S _ { \mathrm { L } }$ , then the ramp vehicle can accelerate to the maximum permitted speed of the ramp before entering the acceleration lane, which can be divided into two phases: uniform acceleration and constant speed. Initially, the vehicle undergoes uniform acceleration, with the travel time for this process denoted as t1 , as shown in Eq. (9); subsequently, the vehicle travels at a constant speed, with the travel time for this phase denoted as $\ t _ { 2 } ^ { 1 }$ , as shown in Eq. (10). Consequently, one can calculate the moment $\mathrm { t _ { d } ^ { 1 } }$ at which the vehicle reaches the start of the acceleration lane, as shown in Eq. (11): 

$$
t _ {1} ^ {1} = t _ {\min } \tag {9}
$$

$$
t _ {2} ^ {1} = \frac {S _ {\mathrm {L}} - S _ {\min }}{\nu_ {\mathrm {r} \text {- m a x}}} \tag {10}
$$

$$
t _ {\mathrm {d}} ^ {1} = t _ {0} + t _ {1} ^ {1} + t _ {2} ^ {1} \tag {11}
$$

In this scenario, the time-varying process of the ramp vehicle’s speed is illustrated in Fig. 5. 

2) If $S _ { \mathrm { m i n } } > S _ { \mathrm { L } }$ , then the ramp vehicle cannot accelerate to the maximum speed permitted by the ramp upon entering the acceleration lane. Consequently, the vehicle continues to travel with uniform acceleration, and the travel time is denoted as $\mathrm { t } _ { 1 } ^ { 2 }$ , as shown in Eq. (12). Thus, the moment $\mathrm { t } _ { \mathrm { d } } ^ { 2 }$ at which the vehicle reaches the start of the acceleration lane can be calculated, as shown in Eq. (13): 

$$
t _ {1} ^ {2} = \frac {\sqrt {v _ {0} ^ {2} + 2 a _ {\max} S _ {\mathrm {L}}} - v _ {0}}{a _ {\max}} \tag {12}
$$

$$
t _ {\mathrm {d}} ^ {2} = t _ {0} + t _ {1} ^ {2} \tag {13}
$$

In this scenario, the time-varying process of the ramp vehicle’s speed is illustrated in Fig. 6. 

It is noteworthy that due to differences in initial speeds, there may be instances where the predicted arrival time at the start of the acceleration lane for a following vehicle in the same lane is earlier than that of the leading vehicle, resulting in the following 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/6ec4602a57b48dd7793f294f8efde548ac9c14822be8ff5bdbfdc4858248ed1b.jpg)



Fig. 6. Time-variation of speed for a ramp vehicle undergoing continuous uniform acceleration.


vehicle entering before the leading vehicle. Consequently, this paper assumes that in the same lane, the entry into the cooperative merging area strictly adheres to the FIFO rule. 

# (2) Speed control of ramp vehicles

After determining the order in which vehicles from a dual-lane ramp enter the cooperative merging area and form a virtual platoon, it is still necessary to control the speed of each vehicle in the virtual platoon. The aim is to ensure conflict-free arrival at the beginning of the merging area for vehicles from different lanes while maximizing vehicular traffic efficiency. The speed control model presented in this paper is similar to the vehicle trajectory optimization model described in Section 3.5, wherein the driving speed of each vehicle in the virtual platoon is adjusted periodically. However, the difference lies in the fact that since the conflict point for vehicles on the dual-lane ramp is fixed at the start of the merging area, the speed control should be based on the virtual platoon method, treating vehicles from the two lanes as ‘single-lane’ vehicles and strictly constraining the vehicular spacing within the platoon at each moment during the period. The speed control method is as follows: 

# 1) Control objective

The speed control model aims to maximize the driving speed of the virtual platoon within each period, ensuring that vehicles from different lanes avoid collisions at the start of the merging area, thereby increasing traffic efficiency. This is formulated in Eq. (14): 

$$
Z = \max  \left(\sum_ {q = 1} ^ {Q} \sum_ {m = 1} ^ {M} v _ {q, m}\right) \tag {14}
$$

where $v _ { q , m }$ represents the speed of the vehicle $q$ in the virtual platoon at time m, unit: m/s; Q is the total number of vehicles in the virtual platoon for each period, unit: veh; q is the vehicle index within the virtual platoon; M is the duration of the speed control period, unit: s; and m is any given moment within the speed control period, unit: s. 

# 2) Constraint conditions

Ensuring driving safety and comfort, the following constraints are adhered to during speed control: 

Maximum speed constraint: The vehicle’s driving speed at each time step must not exceed the ramp’s speed limit. 

$$
0 \leq v _ {q, m} \leq v _ {\mathrm {r} - \max } \quad \forall q, m \tag {15}
$$

Maximum and minimum acceleration constraints: Due to the constraints of vehicle dynamic performance, the acceleration of 

the vehicle at each time step is subject to maximum and minimum value constraints. 

$$
a _ {\min } \leq a _ {q, m} \leq a _ {\max } \quad \forall q, m \tag {16}
$$

where $\boldsymbol { a } _ { q , m }$ denotes the acceleration of the q vehicle in the virtual platoon at time m, unit: $\mathrm { m } / \mathrm { s } ^ { 2 }$ . 

Acceleration change constraint: Ensuring comfort, the difference in acceleration between adjacent time steps for a vehicle cannot exceed a certain value. 

$$
\left| a _ {q, m + 1} - a _ {q, m} \right| \leq A _ {\max } \quad \forall q: m = 1, \dots , M - 1 \tag {17}
$$

Minimum safety distance constraint: Ensuring driving safety, the headway distance between two adjacent vehicles in the virtual platoon must not fall below a predetermined threshold at any time step within the period. 

$$
S _ {q + 1, m} - S _ {q, m} \geq D _ {\min } \quad \forall m; q = 1, \dots , Q - 1 \tag {18}
$$

where $\boldsymbol { \mathrm { S } } _ { q , m }$ represents the distance of the q vehicle in the virtual platoon from the start of the ramp speed control area at time m, unit: m. 

Vehicle dynamics equation constraint: The vehicle dynamics equation describes the relationship between acceleration, speed and distance. It is the basis for speed control, and thus the speed control model is subject to this constraint. 

$$
S _ {q, m + 1} - S _ {q, m} = v _ {q, m} \Delta m \quad \forall q; m = 1, \dots , M - 1 \tag {19}
$$

$$
v _ {q, m + 1} - v _ {q, m} = a _ {q, m} \Delta m \quad \forall q; m = 1, \dots , M - 1 \tag {20}
$$

where -m represents the time step for speed control decision making, unit: s. 

# 3.5. Vehicle trajectory optimization

After exiting area L2, vehicles on the mainline are prohibited from changing lanes in area L . Consequently, the merging problem in the merging area is transformed into a coordination issue between the outermost lane of the mainline and the acceleration lane vehicles. In merge control based on optimization methods, current research primarily conducts iterative optimization within the simulation interval, discretizing time and implementing rolling trajectory optimization for all vehicles within the control area per cycle [7, 12, 13, 35]. 

Inspired by the optimization control strategy in Refs. [13, 35], this paper proposes a time-discretized vehicle trajectory optimization model. An appropriate cycle length is selected, and at the beginning of each cycle, data on the speed, acceleration and position of all vehicles in the region that have not undergone trajectory optimization are collected. The trajectories of merging vehicles are then uniformly planned. By the end of each cycle, vehicles on the acceleration lane will have accelerated to a speed similar to that of the mainline vehicles, creating a gap in the outermost lane of the mainline. The trajectory optimization is completed, allowing vehicles on the acceleration lane to smoothly merge into the mainline. Vehicles can merge at any point along the acceleration lane, with the merging position being the trajectory position at the end of the cycle. The trajectory optimization for these vehicles is conducted on the acceleration lane itself, with speed constraints identical to those of the mainline vehicles, rather than the ramp speed limits. 

The objective function and constraints of the vehicle trajectory optimization model are defined by Eqs. (21) to (28): Eq. (21) represents the objective function, which, after discretizing time, maximizes the speed of merging vehicles within a cycle, using the speed at each time step as the decision variable. Eqs. (22) 

and (23) impose constraints on vehicle speed and acceleration to ensure driving safety. Eq. (24) limits changes in vehicle acceleration between consecutive time steps to ensure ride comfort. Eq. (25) maintains driving safety by keeping the headway distance between two adjacent vehicles in the same lane above a certain threshold. Eq. (26) ensures smooth merging of ramp vehicles into the mainline by maintaining the headway distance between any two vehicles in different lanes above a certain threshold at the end of the cycle. Eqs. (27) and (28) are vehicle dynamics equations related to displacement, speed and acceleration. The detailed formulation of these equations is as follows: 

$$
Z = \max  \left(\sum_ {l = 1} ^ {2} \sum_ {n = 1} ^ {N _ {l}} \sum_ {t = 1} ^ {T} v _ {l, n, t}\right) \tag {21}
$$

$$
0 \leq v _ {l, n, t} \leq v _ {\mathrm {m} - \max } \quad \forall l, n, t \tag {22}
$$

$$
a _ {\min } \leq a _ {l, n, t} \leq a _ {\max } \quad \forall l, n, t \tag {23}
$$

$$
\left| a _ {l, n, t + 1} - a _ {l, n, t} \right| \leq j _ {\max } \quad \forall l, n; t = 1, \dots , T - 1 \tag {24}
$$

$$
\left| S _ {l, n + 1, t} - S _ {l, n, t} \right| \geq D _ {\min } \quad \forall l, t; n = 1, \dots , N _ {l} - 1 \tag {25}
$$

$$
\left| S _ {1, i, T} - S _ {2, j, T} \right| \geq D _ {\min } \quad \forall i = 1, \dots , N _ {1}; j = 1, \dots , N _ {2} \tag {26}
$$

$$
S _ {l, n, t + 1} - S _ {l, n, t} = v _ {l, n, t} \Delta t \quad \forall l, n; t = 1, \dots , T - 1 \tag {27}
$$

$$
v _ {l, n, t + 1} - v _ {l, n, t} = a _ {l, n, t} \Delta t \quad \forall l, n; t = 1, \dots , T - 1 \tag {28}
$$

where l denotes the lane number, 1 represents the outermost lane of the mainline and 2 represents the acceleration lane. n represents the index of merging vehicles in lane l within each cycle area L . N denotes the total number of merging vehicles in lane l within each cycle area L3. t represents any moment within the cycle. T denotes the duration of the cycle. $v _ { \mathrm { l } , n , \mathrm { t } }$ represents the velocity of the $n$ -th vehicle in lane l at time t. $\mathcal { V } _ { \mathrm { m \_ m a x } }$ denotes the speed limit of the mainline road. $a _ { \mathrm { l , } n , \mathrm { t } }$ represents the acceleration of the n-th vehicle in lane l at time t. $a _ { \mathrm { m a x } }$ represents the maximum acceleration. $a _ { \mathrm { m i n } }$ represents the minimum deceleration. $\dot { J } _ { \mathrm { { m a x } } }$ denotes the maximum change in acceleration between consecutive time steps. $S _ { \mathrm { l , } n , \mathrm { t } }$ represents the distance of the n-th vehicle in lane l from the region’s starting point at time t. $\mathrm { D } _ { \mathrm { m i n } }$ denotes the critical car-following headway distance. i represents the index of merging vehicles in the outermost lane of the mainline within each cycle area L . j represents the index of merging vehicles in the acceleration lane within each cycle area L . $\mathrm { N } _ { 1 }$ denotes the total number of merging vehicles in the outermost lane of the mainline within each cycle area L3. $\mathrm { N } _ { 2 }$ denotes the total number of merging vehicles in the acceleration lane within each cycle area L3. -t represents the decision time step. 

In summary, the cycle duration T must not be too short, as this would prevent ramp vehicles from accelerating to speeds comparable to mainline vehicles by the end of the cycle. Conversely, it must not be too long, as this would cause ramp vehicles to reach the end of the acceleration lane before the cycle concludes. Therefore, ensuring successful trajectory optimization, the maximum value of T must be calculated under the most extreme conditions. Assuming area L3 has just started its m-th cycle optimization (at time mT seconds), at time $m T { \pm } 1$ , a ramp vehicle enters the starting point of the acceleration lane with a speed equal to the ramp speed limit. The vehicle can only optimize its trajectory during the $( m { + } 1 )$ -th cycle (corresponding to time $( m { + } 1 ) T$ seconds) and then switch to the outermost mainline lane at time $( m + 2 ) T$ . It is essential to ensure that the maximum distance travelled by the ramp 

vehicle within 2T 1 seconds does not exceed the length of the acceleration lane. The maximum distance scenario involves the ramp vehicle first accelerating to the mainline speed limit with maximum acceleration and then maintaining that speed. Hence, the cycle duration T must satisfy the constraint given by Eq. (29): 

$$
\frac {v _ {\mathrm {m} _ {-} \max } ^ {2} - v _ {\mathrm {r} _ {-} \max } ^ {2}}{2 a _ {\max }} + \left(2 T - 1 - \frac {v _ {\mathrm {m} _ {-} \max } - v _ {\mathrm {r} _ {-} \max }}{a _ {\max }}\right) v _ {\mathrm {m} _ {-} \max } \leq H _ {3} (2 9)
$$

where $\boldsymbol { \mathrm { { U } _ { \mathrm { { r } _ { \mathrm { { m a x } } } } } } }$ denotes the speed limit of the ramp and $H _ { 3 }$ denotes the length of the acceleration lane. 

# 4. Simulation analysis

# 4.1. Simulation scenario and parameter settings

To validate the effectiveness of the cooperative merging control method, we conducted a simulation using SUMO software on a freeway merging area with three mainline lanes and a double-lane ramp. SUMO, an open-source, multimodal traffic simulation tool, allows for real-time traffic control via its Traffic Control Interface, co-simulated with Python. 

In the simulated merging scenario, the mainline road is ${ 1 0 0 0 } \mathrm { m }$ , the ramp is $4 0 0 ~ \mathrm { m }$ and the lane width is $3 . 7 5 \mathrm { ~ m ~ }$ . The simulation runs for 3,600 s with a time step of 1 s. The simulation process is illustrated in Fig. 7, and the simulation experiment parameters are set similarly to those used in Refs. [7, 13, 35], as shown in Table 1. 

In this study, simulation experiments are conducted based on 16 sets of traffic demand scenarios for the ramp and the mainline. Each set of experiments is simulated three times using different random seeds, and the average values are taken. The traffic flow for the mainline is set to 800 veh/h/ln, 1,200 veh/h/ln, 1,600 veh/h/ln and 2,000 veh/h/ln for each lane, while the traffic flow for the ramp is set to 400 veh/h/ln, 500 veh/h/ln, 600 veh/h/ln and 700 veh/h/ln for each lane. 

# 4.2. Simulation results analysis

# 4.2.1. Comparative analysis of simulation results for different control strategies on dual-lane ramp

Tables 2 to 4 present simulation results for average vehicle speed, average delay and total stop counts (vehicles with speeds less than $1 \mathrm { m / s }$ considered stopped [22]) under three control strategies—no control, trajectory optimization control and cooperative control— in a dual-lane ramp scenario across varying traffic demand levels. Content included in the parentheses indicate the percentage change of each metric relative to the no-control scenario. 

The experimental results from Tables 2 to 4 indicate the following: 

1) In a dual-lane ramp scenario, under various traffic demand levels, the performance indicators using trajectory optimization control consistently surpass those of the nocontrol approach. Furthermore, cooperative control outperforms trajectory optimization control, demonstrating that implementing lane-changing strategies to alleviate traffic pressure on the outer lane significantly enhances vehicle merging efficiency. 

2) When both the mainline and ramp experience low traffic demand (with mainline flows of 800 veh/h/ln or 1,200 veh/h/ln, and ramp flows of 400 veh/h/ln or 500 veh/h/ln, across four groups), compared to the no-control approach, vehicles using only trajectory optimization show an average speed increase of $6 . 9 \%$ and an average delay reduction of $3 0 . 9 \%$ . Cooperative control results in an average speed increase of $9 . 6 \%$ and an average delay reduction of $4 4 . 9 \%$ , with mi-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/d915f27108c047345e5bb68a8b4eb88785e18ef41ea891212169e6134b717ef5.jpg)



Fig. 7. Simulation process flowchart.


nor differences in average speeds between the three control strategies. 

3) In scenarios where one of either the mainline or ramp has high traffic demand while the other is low (mainline flows exceeding 1,200 veh/h/ln with low ramp flows, or ramp flows exceeding 500veh/h/ln with low mainline flows, across eight groups), vehicles under trajectory optimization control achieve an average speed increase of $1 3 . 5 \%$ and an average delay reduction of $4 7 . 8 \%$ . Cooperative control leads to an average speed increase of $1 6 . 6 \%$ and an average delay reduction of $5 5 . 4 \%$ , showing significant differences from the nocontrol scenario and highlighting the advantages of cooperative control. 

4) When both the mainline and ramp are under high traffic demand (mainline flows not less than 1,600 veh/h/ln, and ramp flows not less than 600 veh/h/ln, across four groups), trajectory optimization control results in an average speed increase of $4 1 . 6 \%$ and an average delay reduction of $6 2 . 0 \%$ . Cooperative control boosts average speeds by $4 9 . 1 \%$ and reduces delays by $7 0 . 2 \%$ , and the cooperative control approach significantly enhances the traffic efficiency in merging areas. 

The experimental results in Table 4 show that without control, vehicle stopping phenomenons occurred across 11 groups at varying traffic demand levels, mainly at medium and high levels. In contrast, trajectory optimization control only resulted in 


Table 1. Simulation experiment parameters.


<table><tr><td>Parameter</td><td>Unit</td><td>Value</td><td>Description</td></tr><tr><td>t0</td><td>s</td><td>1.2</td><td>Minimum safe headway</td></tr><tr><td>s0</td><td>m</td><td>2.0</td><td>Minimum safe distance</td></tr><tr><td>L</td><td>m</td><td>5.0</td><td>Length of vehicle</td></tr><tr><td>H1</td><td>m</td><td>200.0</td><td>Length of area L1</td></tr><tr><td>H2</td><td>m</td><td>300.0</td><td>Length of area L2</td></tr><tr><td>H3</td><td>m</td><td>300.0</td><td>Length of area L3</td></tr><tr><td>H4</td><td>m</td><td>200.0</td><td>Length of area L4</td></tr><tr><td>H5</td><td>m</td><td>300.0</td><td>Length of ramp speed control area</td></tr><tr><td>vm_max</td><td>m/s</td><td>25.0</td><td>Mainline road speed limit</td></tr><tr><td>vr_max</td><td>m/s</td><td>16.7</td><td>Ramp speed limit</td></tr><tr><td>a_max</td><td>m/s²</td><td>5.0</td><td>Maximum acceleration</td></tr><tr><td>a_min</td><td>m/s²</td><td>-5.0</td><td>Minimum deceleration</td></tr><tr><td>A_max</td><td>m/s²</td><td>3.0</td><td>Maximum acceleration change per adjacent time step</td></tr><tr><td>D_min</td><td>m</td><td>8.0</td><td>Critical following headway</td></tr><tr><td>T</td><td>s</td><td>6.0</td><td>Merging vehicle trajectory optimization model cycle duration</td></tr><tr><td>M</td><td>s</td><td>8.0</td><td>Ramp vehicle speed control model cycle duration</td></tr><tr><td>Δt</td><td>s</td><td>1.0</td><td>Following driving decision time step</td></tr><tr><td>Δk</td><td>s</td><td>1.0</td><td>Trajectory optimization decision time step</td></tr><tr><td>Δm</td><td>s</td><td>1.0</td><td>Speed control decision time step</td></tr></table>


Table 2. Comparison of average vehicle speeds $\mathrm { ( k m / h ) }$ ) under different traffic demand levels.


<table><tr><td rowspan="2">Ramp flow/(veh/h/ln)</td><td rowspan="2">Control strategy</td><td colspan="4">Mainline flow/(veh/h/ln)</td></tr><tr><td>800</td><td>1,200</td><td>1,600</td><td>2,000</td></tr><tr><td rowspan="3">400</td><td>No control</td><td>75.42</td><td>71.86</td><td>68.37</td><td>64.73</td></tr><tr><td>Only trajectory optimization control</td><td>79.10 (+4.9%)</td><td>77.64 (+8.0%)</td><td>76.21 (+11.5%)</td><td>75.29 (+16.3%)</td></tr><tr><td>Cooperative control</td><td>80.74 (+7.1%)</td><td>79.15 (+10.1%)</td><td>77.92 (+14.0%)</td><td>76.86 (+18.7%)</td></tr><tr><td rowspan="3">500</td><td>No control</td><td>73.20</td><td>70.98</td><td>66.64</td><td>63.85</td></tr><tr><td>Only trajectory optimization control</td><td>78.14 (+6.7%)</td><td>76.72 (+8.1%)</td><td>75.47 (+13.2%)</td><td>74.96 (+17.4%)</td></tr><tr><td>Cooperative control</td><td>80.36 (+9.8%)</td><td>79.03 (+11.3%)</td><td>77.80 (+16.7%)</td><td>76.64 (+20.0%)</td></tr><tr><td rowspan="3">600</td><td>No control</td><td>70.51</td><td>69.18</td><td>63.16</td><td>53.20</td></tr><tr><td>Only trajectory optimization control</td><td>77.72 (+10.2%)</td><td>76.53 (+10.6%)</td><td>74.45 (+17.9%)</td><td>72.38 (+36.0%)</td></tr><tr><td>Cooperative control</td><td>79.65 (+13.0%)</td><td>78.68 (+13.7%)</td><td>77.54 (+22.8%)</td><td>76.31 (+43.4%)</td></tr><tr><td rowspan="3">700</td><td>No control</td><td>67.76</td><td>65.45</td><td>50.48</td><td>42.33</td></tr><tr><td>Only trajectory optimization control</td><td>77.04 (+13.6%)</td><td>75.40 (+15.2%)</td><td>72.71 (+44.0%)</td><td>71.25 (+68.3%)</td></tr><tr><td>Cooperative control</td><td>79.30 (+17.0%)</td><td>78.22 (+19.5%)</td><td>76.81 (+52.2%)</td><td>75.29 (+77.9%)</td></tr></table>


Table 3. Comparison of average vehicle delay (s/veh) under different traffic demand levels.


<table><tr><td rowspan="2">Ramp flow/(veh/h/ln)</td><td rowspan="2">Control strategy</td><td colspan="4">Mainline flow/(veh/h/ln)</td></tr><tr><td>800</td><td>1,200</td><td>1,600</td><td>2,000</td></tr><tr><td rowspan="3">400</td><td>No control</td><td>1.79</td><td>2.48</td><td>3.32</td><td>4.25</td></tr><tr><td>Only trajectory optimization control</td><td>1.40 (-21.8%)</td><td>1.65 (-33.5%)</td><td>1.83 (-44.9%)</td><td>1.96 (-53.9%)</td></tr><tr><td>Cooperative control</td><td>1.13 (-36.9%)</td><td>1.36 (-45.2%)</td><td>1.69 (-49.1%)</td><td>1.80 (-57.6%)</td></tr><tr><td rowspan="3">500</td><td>No control</td><td>2.24</td><td>2.70</td><td>3.69</td><td>4.42</td></tr><tr><td>Only trajectory optimization control</td><td>1.49 (-33.5%)</td><td>1.76 (-34.8%)</td><td>1.95 (-47.2%)</td><td>2.02 (-54.3%)</td></tr><tr><td>Cooperative control</td><td>1.16 (-48.2%)</td><td>1.37 (-49.3%)</td><td>1.71 (-53.6%)</td><td>1.82 (-58.8%)</td></tr><tr><td rowspan="3">600</td><td>No control</td><td>2.73</td><td>3.06</td><td>4.45</td><td>6.13</td></tr><tr><td>Only trajectory optimization control</td><td>1.61 (-41.0%)</td><td>1.79 (-41.5%)</td><td>2.13 (-52.1%)</td><td>2.47 (-59.7%)</td></tr><tr><td>Cooperative control</td><td>1.36 (-50.2%)</td><td>1.42 (-53.6%)</td><td>1.80 (-59.6%)</td><td>1.88 (-69.3%)</td></tr><tr><td rowspan="3">700</td><td>No control</td><td>3.35</td><td>3.84</td><td>6.76</td><td>9.43</td></tr><tr><td>Only trajectory optimization control</td><td>1.68 (-49.8%)</td><td>1.92 (-50.0%)</td><td>2.38 (-64.8%)</td><td>2.70 (-71.4%)</td></tr><tr><td>Cooperative control</td><td>1.4 (-58.2%)</td><td>1.45 (-62.2%)</td><td>1.85 (-72.6%)</td><td>1.94 (-79.4%)</td></tr></table>


Table 4. Comparison of total stop counts under different traffic demand levels.


<table><tr><td rowspan="2">Ramp flow/(veh/h/ln)</td><td rowspan="2">Control strategy</td><td colspan="4">Mainline flow/(veh/h/ln)</td></tr><tr><td>800</td><td>1,200</td><td>1,600</td><td>2,000</td></tr><tr><td rowspan="2">400</td><td>No control</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Only trajectory optimization control</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="4">500</td><td>Cooperative control</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>No control</td><td>0</td><td>4</td><td>10</td><td>17</td></tr><tr><td>Only trajectory optimization control</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Cooperative control</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="3">600</td><td>No control</td><td>6</td><td>9</td><td>20</td><td>32</td></tr><tr><td>Only trajectory optimization control</td><td>0</td><td>0</td><td>0</td><td>2</td></tr><tr><td>Cooperative control</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="3">700</td><td>No control</td><td>16</td><td>25</td><td>38</td><td>84</td></tr><tr><td>Only trajectory optimization control</td><td>0</td><td>0</td><td>2</td><td>5</td></tr><tr><td>Cooperative control</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

stopping phenomenons at high demand levels for both the mainline and ramp. The cooperative control approach, however, eliminated stopping entirely, further demonstrating the effectiveness of combining lane-changing strategies with trajectory optimization models across various levels of traffic demand. Moreover, compared to controlled scenarios, the number of stopping phenomenons significantly increases under the same levels of traffic 

demand with no control. This increase indicates that when traffic flow is high, greater conflicts arise as vehicles from two lanes on the ramp merge into the acceleration lane, leading to vehicle queuing. Additionally, as the traffic flows on the mainline and ramp increase, even the trajectory optimization control method experiences a small number of stopping phenomena. However, after implementing the speed control model described in this paper, vehicles in the ramp’s speed control area are proactively planned with trajectories that allow them to reach the start of the acceleration lane without conflicts, smoothly entering into the cooperative merging area. By integrating lane-changing strategies and trajectory optimization models, the occurrence of vehicle stopping and queuing is consistently avoided, demonstrating that the cooperative control method described in this paper offers superior control efficiency. 

The smoothed comparison results of the average vehicle speed, average delay, and total stop counts under three different control strategies across varying levels of traffic demand are illustrated in Figs. 8, 9 and 10. From Figs. 8 to 10, the following is evident. 

When both the mainline and ramp traffic flows are low, the curves representing average vehicle speed, average delay, and total stop counts under the three control strategies are very close to each other. As the traffic flows on the mainline and ramp increase, the curve representing average vehicle speed under the no-control scenario significantly declines, while the curves for average delay and total stop counts sharply rise. Conversely, the vehicles under trajectory optimization control and cooperative con-

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/0f5f0a30180cc0bbb7677e0af5484835dd5c0b840d2f0aac92296c9a79dba398.jpg)



Fig. 8. Comparison of average vehicle speeds under three control strategies for different traffic demands.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/2000604b3e2823506eb260219ae2ba01d2820524bbaece69e29f0208447d1d7b.jpg)



Fig. 9. Comparison of average vehicle delays under three control strategies for different traffic demands.


trol exhibit minimal fluctuations in all three curves, consistently maintaining superior values. The difference between these controlled strategies and the no-control strategy becomes increasingly pronounced, highlighting the advantages of a cooperative control approach that combines lane-changing strategies, speed optimization strategies and trajectory optimization models 

# 4.2.2. Comparison of cooperative control method effects in single-lane and dual-lane ramp scenarios

The case analyses of different control strategies under dual-lane ramp scenarios have validated the effectiveness of the cooperative optimization model. To verify the effects of the cooperative control method under varying numbers of ramp lanes, this section compares the control effects in single-lane and dual-lane ramp scenarios under different mainline and ramp traffic demand levels. The experimental parameters are set according to Section 4.1. Under different ramp lane counts and traffic demand levels, the simulation results are presented in Tables 5 to 7 (with content included in the parentheses indicating the percentage 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/a33fa1cbb11075aa32539c25100b042456f0736527b4f267a97377bfa381c065.jpg)



Fig. 10. Comparison of total stop counts under three control strategies for different traffic demands.


increase/decrease in average speed/average delay compared to single-lane ramps). 

The experimental results from Tables 5 to 7 indicate the following: 

1) Under the cooperative control method proposed in this study, whether on single-lane or dual-lane ramps, the method maintains high efficiency across different traffic demand levels, with no significant differences in vehicle speed, delay or stop counts. This demonstrates that the control method can be applied to different scenarios and is universally applicable. 

2) As shown in Table 5, under the cooperative control method, the average vehicle speed decreases gradually with increasing mainline and ramp traffic flows. Although the difference in vehicle speeds between single-lane and dual-lane ramps is not large, vehicles on dual-lane ramps still maintain a speed advantage, and can achieve a maximum increase of $2 . 2 0 \%$ in average speed compared to single-lane ramps. 

3) According to Table 6, under the cooperative control method, although the average vehicle speed decreases with increasing traffic flows on both the mainline and ramps, the difference in delays between the two is minimal. Vehicles on dual-lane ramps experience less delay compared to those on single-lane ramps. 

4) As per Table 7, regardless of being on single-lane or duallane ramps, the number of vehicle stops is zero, indicating no occurrences of vehicle stopping. This shows that the cooperative control method is effective in different scenarios and adapts well to varying traffic demands. The control method significantly enhances the traffic efficiency in merging areas. 

Based on the results from Tables 5 to 7, it is evident that whether on single-lane or dual-lane ramps, as traffic demand increases, the efficiency of the merging areas gradually decreases. However, the cooperative control method proposed in this study maintains good control efficiency. Furthermore, the merging scenarios on dual-lane ramps have a distinct advantage, as they can prevent ramp vehicles from stopping and waiting, thereby enhancing traffic safety. 


Table 5. Comparison of average vehicle speeds $\mathrm { ( m / s ) }$ under different traffic demand levels.


<table><tr><td rowspan="2">Ramp flow/(veh/h/ln)</td><td rowspan="2">Ramp</td><td colspan="4">Mainline flow/(veh/h/ln)</td></tr><tr><td>800</td><td>1,200</td><td>1,600</td><td>2,000</td></tr><tr><td rowspan="2">400</td><td>Single-lane ramp</td><td>80.10</td><td>77.72</td><td>76.24</td><td>75.76</td></tr><tr><td>Dual-lane ramp</td><td>80.74 (+0.80%)</td><td>79.15 (+1.84%)</td><td>77.92 (+2.20%)</td><td>76.86 (+1.45%)</td></tr><tr><td rowspan="2">500</td><td>Single-lane ramp</td><td>79.07</td><td>77.68</td><td>76.18</td><td>75.59</td></tr><tr><td>Dual-lane ramp</td><td>80.36 (+1.63%)</td><td>79.03 (+1.74%)</td><td>77.80 (+2.13%)</td><td>76.64 (+1.39%)</td></tr><tr><td rowspan="2">600</td><td>Single-lane ramp</td><td>78.90</td><td>77.60</td><td>75.94</td><td>75.43</td></tr><tr><td>Dual-lane ramp</td><td>79.65 (+0.95%)</td><td>78.68 (+1.39%)</td><td>77.54 (+2.11%)</td><td>76.31 (+1.17%)</td></tr><tr><td rowspan="2">700</td><td>Single-lane ramp</td><td>78.26</td><td>77.30</td><td>75.68</td><td>75.19</td></tr><tr><td>Dual-lane ramp</td><td>79.30 (+1.33%)</td><td>78.22 (+1.19%)</td><td>76.81 (+1.49%)</td><td>75.29 (+0.13%)</td></tr></table>


Table 6. Comparison of average vehicle delays (s/veh) under different traffic demand levels.


<table><tr><td rowspan="2">Ramp flow/(veh/h/ln)</td><td rowspan="2">Ramp</td><td colspan="4">Mainline flow/(veh/h/ln)</td></tr><tr><td>800</td><td>1,200</td><td>1,600</td><td>2,000</td></tr><tr><td rowspan="2">400</td><td>Single-lane ramp</td><td>1.10</td><td>1.44</td><td>1.76</td><td>1.87</td></tr><tr><td>Dual-lane ramp</td><td>1.13 (2.73%)</td><td>1.36 (-5.56%)</td><td>1.69 (-3.98%)</td><td>1.80 (-3.74%)</td></tr><tr><td rowspan="2">500</td><td>Single-lane ramp</td><td>1.27</td><td>1.48</td><td>1.77</td><td>1.91</td></tr><tr><td>Dual-lane ramp</td><td>1.16 (-8.66%)</td><td>1.37 (-7.43%)</td><td>1.71 (-3.39%)</td><td>1.82 (-4.71%)</td></tr><tr><td rowspan="2">600</td><td>Single-lane ramp</td><td>1.31</td><td>1.52</td><td>1.84</td><td>1.93</td></tr><tr><td>Dual-lane ramp</td><td>1.36 (-3.82%)</td><td>1.42 (-6.58%)</td><td>1.80 (-2.17%)</td><td>1.88 (-2.59%)</td></tr><tr><td rowspan="2">700</td><td>Single-lane ramp</td><td>1.45</td><td>1.59</td><td>1.88</td><td>1.95</td></tr><tr><td>Dual-lane ramp</td><td>1.4 (-3.45%)</td><td>1.45 (-8.81%)</td><td>1.85 (-1.60%)</td><td>1.94 (-0.51%)</td></tr></table>


Table 7. Comparison of total stop counts under different traffic demand levels.


<table><tr><td rowspan="2">Ramp flow/(veh/h/ln)</td><td rowspan="2">Ramp</td><td colspan="4">Mainline flow/(veh/h/ln)</td></tr><tr><td>800</td><td>1,200</td><td>1,600</td><td>2,000</td></tr><tr><td rowspan="2">400</td><td>Single-lane ramp</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Dual-lane ramp</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="2">500</td><td>Single-lane ramp</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Dual-lane ramp</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="2">600</td><td>Single-lane ramp</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Dual-lane ramp</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="2">700</td><td>Single-lane ramp</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Dual-lane ramp</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

# 4.2.3. Sensitivity analysis

The cooperative control method proposed in this paper is adaptable to different ramp scenarios and levels of traffic demand, capable of enhancing vehicle speed in merging areas, reducing average travel delays and minimizing the total stop counts. For the merging scenarios on dual-lane ramps, this section conducts a sensitivity analysis of the optimization model parameters. The critical following headway is a crucial parameter in the vehicle trajectory optimization model. Based on the principle of controlling variables, the impact of the critical following headway on average vehicle speed and delay is analysed through simulations, with other parameter values remaining consistent with those listed in Table 1. 

Different studies on merging optimization define varying lengths for critical following headways, with Ref. [7] setting it at 6 m and Ref. [12] at $1 0 \mathrm { m }$ . Considering a vehicle length L of 5 m, this paper sets critical following headways at $8 \textrm { m }$ , 10 m and 12 m. In dual-lane ramp merging scenarios, these critical following headways are analysed under various traffic demand levels to assess 

their impact on average vehicle speed and delay. The simulation results are presented in Figs. 10 and 11. 

From Figs. 11 and 12, the following observations can be made: 

1) Under varying traffic demand levels on the mainline and ramps, as the critical following headway increases, the average vehicle speed gradually decreases and the average delay increases. This phenomenon demonstrates that the larger the traffic flows, the greater the impact of the critical following headway on vehicle speed and delay. This suggests that in high-flow traffic conditions, managing and optimizing headway settings is crucial for maintaining traffic efficient and minimizing delays. 

2) At lower levels of mainline traffic demand, the differences in average vehicle speed and delay across the three critical following headways are relatively minor and not distinctly apparent. However, as the mainline traffic demand increases, the differences in average vehicle speed and delay across these critical following headways become more pronounced, especially with higher ramp traffic demands. The maximum difference observed is 1.45 km/h for average speed and 0.18 s for average delay. 

3) Combining the insights from Figs. 11 and 12, at lower critical following headways, vehicles tend to have higher average speeds and lower average delays. These differences become more significant as the level of mainline traffic demand increases. 

# 5. Conclusions

1) A cooperative merging control method for CAVs has been proposed for multi-lane mainline and dual-lane ramp scenarios in intelligent connected freeway merging areas. The merging area and its upstream and downstream sections are divided into six areas, where some mainline vehicles are 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/652f5584915f58ab9a33558dc2865c53ba538b0d72791df420fa5602974e775d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/af694cf6b1344cff4cafbaf1e64e5ecd29b2413e5e34530d82ae8e11fa96aeba.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/6aed91c6de9b08ccedd265f2b8951489909fe0eeacfbbcfb746be94d54f442ff.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/479f96a13b14b6b0fdc806b3735f0b5a65ffddf820b5f0309324dbe93da40179.jpg)



Fig. 11. Comparison of average vehicle speeds at different critical following headways: (a) ramp flow is 800 veh/h/ln; (b) ramp flow is 1,000 veh/h/ln; (c) ramp flow is 1,200 veh/h/ln; (d) ramp flow is 1,400 veh/h/ln.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/a34ef2526b9b0306b0937c71dada276dbbe65705b5f78457cb571cf2fbdc8298.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/c35a1a0348dd9a6a2fc6961d703ec86ce23506474cf2cf7480e8187d82c6541f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/b6858bdbac01b465b0646ca66d1e80db30e4be4fbc882274e6c88eb848e00edb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/62375f39-d339-46a1-b51d-22adda60d98f/a4278332a21a641635d7ff1adb5ece13240e738566380a2675227521d00485f5.jpg)



Fig. 12. Comparison of average vehicle delays at different critical following headways: (a) ramp flow is 800 veh/h/ln; (b) ramp flow is 1,000 veh/h/ln; (c) ramp flow is 1,200 veh/h/ln; (d) ramp flow is 1,400 veh/h/ln.


guided to change lanes in advance and adjust their speeds ahead of time, and the merging vehicles’ trajectories are optimized in specific areas. This approach enhances vehicular safety and traffic efficiency in the merging area. 

2) Simulation experiments validate the advantages of the proposed vehicle cooperative control method over uncontrolled natural merging and trajectory optimization only within the merging area. Under various traffic demand levels on the mainline and ramps, the method effectively increases average vehicle speed, reduces average delay and eliminates the occurrence of stops. Moreover, the higher the traffic demand level, the more pronounced the advantages of the cooperative control method. The efficiency of the control method under different ramp lane configurations was compared, verifying its adaptability to various application scenarios. An analysis of the sensitivity of different parameters in the optimization model further demonstrates the adaptability and effectiveness of the method in various scenarios. 

3) This paper optimizes the cooperative merging control method for complex merging areas involving multi-lane mainlines and dual-lane ramps, providing unique insights into the cooperative merging control of ramp merging areas. However, to simplify the study, several limitations remain. For instance, all vehicles are assumed to be CAVs, whereas, for the foreseeable future, traffic will consist of a mix of CAVs and human-driven vehicles. Therefore, the merging control of mixed traffic flows, particularly the merging control of platoons comprising both CAVs and human-driven vehicles, will be a key focus of future research. Additionally, the lanechanging strategy in this paper does not consider the lateral trajectory optimization and tracking during the lanechanging process, as lane changes are not instantaneous. Hence, our future work will involve optimizing the lateral lane-changing trajectories. 

# Informed consent statement

Informed consent has been obtained from all authors and funders involved in the study, and each author has agreed to and decided on the publication of this paper. 

# Acknowledgements

This research was funded by the Natural Science Foundation of Hunan Province (Grant No. 2023JJ30039), the National National Natural Science Foundation of China (Grant No. 52372296), the Postgraduate Scientific Research Innovation Project of Hunan Province (Grant No. CX20220862) and the ChangSha Science and Technology Major Special Project (Grant No. kh2301004). The authors are responsible for the content. 

# Author contributions

The authors confirm contribution to the paper as follows: Yi Wang, Junliang Pan and Jie Wang—conceptualization, methodology, investigation, writing-original draft preparation, sofware, validation; Jian Xiang—methodology, writing-review and editing, formal analysis, supervision, revisions, project administration, funding acquisition; Tao Chen and Hao Wang—Validation, Review. All authors have reviewed and agreed to the published version of the manuscript. 

# Conflict of interest statement

None declared. 

# Data availibility

All datasets used and generated in the current study, as well as all developed software codes, are available from the corresponding author upon reasonable request. 

# References



1. Zheng L, Hou QZ, Guo YY et al. Conflict extremum modeling and traffic accident prediction for expressway merging areas. J Highw Transp Res Dev 2022;39:132–40. 





2. Abdel-Aty M, Dilmore J, Dhindsa A. Evaluation of variable speed limits for real-time freeway safety improvement. Accid Anal Prev 2006;38:335–45. 





3. Li ZB, Jin MJ, Liu P et al. Evaluation of impact variable speed limits on improving traffic efficiency on freeways. J Jilin Univ Eng Technol Ed 2013;43:1204–9. 





4. Sun X, Horowitz R. A localized switching ramp-metering controller with a queue length regulator for congested freeways. In: Proceedings of the2005, American Control Conference, 2005, Portland, OR, USA, 2005;2141–6. 





5. Wu J, McDonald M, Chatterjee K. A detailed evaluation of ramp metering impacts on driver behaviour. Transp Res Part F Traffic Psychol Behav 2007;10:61–75. 





6. Yang S, Du M, Chen Q. Impact of connected and autonomous vehicles on traffic efficiency and safety of an on-ramp. Simul Model Pract Theory 2021;113:102374. 





7. Hu X, Sun J. Trajectory optimization of connected and autonomous vehicles at a multilane freeway merging area. Transp Res Part C Emerg Technol 2019;101:111–25. 





8. Lozano Domínguez JM, Mateo Sanguino TJ. Review on V2X, I2X, and P2X communications and their applications: A comprehensive analysis over time. Sensors 2019;19:2756. 





9 Jing X, Pei X, Yan S et al. Safety benefit of cooperative control for heterogeneous traffic on-ramp merging. Transp Saf Environ 2022;4:tdac031. 





10. Shang WL, Zhang M, Wu G et al. Estimation of traffic energy consumption based on macro-micro modelling with sparse data from Connected and Automated Vehicles. Appl Energy 2023;351:121916. 





11. Ni D, Li J, Andrews S et al. A methodology to estimate capacity impact due to connected vehicle technology. Int J Veh Technol 2012;2012:502432. 





12. Letter C, Elefteriadou L. Efficient control of fully automated connected vehicles at freeway merge segments. Transp Res Part C Emerg Technol 2017;80:190–205. 





13. Xie Y, Zhang H, Gartner NH et al. Collaborative merging strategy for freeway ramp operations in a connected and autonomous vehicles environment. J Intell Transp Syst 2017;21:136–47. 





14. Liu C, Zhuang WC, Yin GD et al. Cooperative merging control of multiple connected and automated vehicles on freeway ramp. J Southeast Univ Nat Sci Ed 2020;50:965–72. 





15. Li Y, Zhu J, Haque MM et al. Hazard-based duration modelling of merging time interval on freeway on-ramps. Transp Saf Environ 2023;5:tdac040. 





16. Rios-Torres J, Malikopoulos AA. Automated and cooperative vehicle merging at highway on-ramps. IEEE Trans Intell Transp Syst 2017;18:780–9. 





17. Ding J, Li L, Peng H et al. A rule-based cooperative merging strategy for connected and automated vehicles. IEEE Trans Intell Transp Syst 2020;21:3436–46. 





18. Ran B, Leight S, Chang B. A microscopic simulation model for merging control on a dedicated-lane automated highway system. Transp Res Part C Emerg Technol 1999;7:369–88. 





19. Zhang CB, Li JS, Huang CM et al. The method of vehicle merging guidance at freeway on-ramp based on cooperative vehicle infrastructure system. J Wuhan Univ Technol Transp Sci Eng 2017;41:537–42. 





20. Zhou M, Qu X, Jin S. On the impact of cooperative autonomous vehicles in improving freeway merging: A modified intelligent driver model-based approach. IEEE Trans Intell Transp Syst 2017;18:1422–8. 





21. Yang L, Zhan J, Shang WL et al. Multi-lane coordinated control strategy of connected and automated vehicles for on-ramp merging area based on cooperative game. IEEE Trans Intell Transp Syst 2023;24:13448–61. 





22. Shi Y, Yu H, Guo Y et al. A collaborative merging strategy with lane changing in multilane freeway on-ramp area with V2X network. Future Internet 2021;13:123. 





23. Xu H, Feng S, Zhang Y et al. A grouping-based cooperative driving strategy for CAVs merging problems. IEEE Trans Veh Technol 2019;68:6125–36. 





24. Zhu J, Tasic I, Qu X. Flow-level coordination of connected and autonomous vehicles in multilane freeway ramp merging areas. Multimodal Transp 2022;1:100005. 





25. Zhao Z, Wang Z, Wu G et al. The state-of-the-art of coordinated ramp control with mixed traffic conditions. In: IEEE Intelligent Transportation Systems Conference, Auckland, New Zealand, 2019;1741–8. 





26. Jing S, Hui F, Zhao X et al. Integrated longitudinal and lateral hierarchical control of cooperative merging of connected and automated vehicles at on-ramps. IEEE Trans Intell Transp Syst 2022;23:24248–62. 





27. Jiang HB, Hu ZN, Liu QC et al. Centralized coordinated ramp merging control for intelligent and connected vehicles. J Hunan Univ Nat Sci 2021;48:159–70. 





28. Wang QL, Zhao XM, Xu ZG et al. Centralized ramp confluence cooperative control method with special connected and automated vehicle priority. J Traffic Transp Eng 2022;22:263–72. 





29. Meng T, Xu B, Qin X et al. Cooperative ramp merging control for connected and automated vehicles. In: SAE Technical Paper Series 2020-01-5020;2020. https://doi.org/10.4271/2020-01-5020. 





30. Uno A, Sakaguchi T, Tsugawa S. A merging control algorithm based on inter-vehicle communication. In: Proceedings 199 IEEE/IEEJ/JSAI International Conference on Intelligent Transportation Systems, Tokyo, Japan, 1999,:783–7. 





31. Chen T, Wang M, Gong S et al. Connected and automated vehicle distributed control for on-ramp merging scenario: A virtual rotation approach. Transp Res Part C Emerg Technol 2021;133:103451. 





32. Chen T, Gong S, Wang M et al. Stochastic capacity analysis for a distributed connected automated vehicle virtual car-following control strategy. Transp Res Part C Emerg Technol 2023;152:104176. 





33. Wang Z, Wu G, Barth M. Distributed consensus-based cooperative highway on-ramp merging using V2X communications. In: SAE Technical Paper Series 2018-01-1177;2018. https://doi.org/10.4 271/2018-01-1177. 





34. Zhou Y, Cholette ME, Bhaskar A et al. Optimal vehicle trajectory planning with control constraints and recursive implementation for automated on-ramp merging. IEEE Trans Intell Transp Syst 2019;20:3409–20. 





35. Wang ZW, Pan JL, Chen T et al. Cooperative merging control of connected and automated vehicles in merging area for one-way three-lane freeway. J Traffic Transp Eng 2023;23: 270–82. 





36. Chen J, Zhou Y, Chung E. An integrated approach to optimal merging sequence generation and trajectory planning of connected automated vehicles for freeway on-ramp merging sections. IEEE Trans Intell Transp Syst 2024;25:1897–912. 





37. Irshayyid A, Chen J, Xiong G. A review on reinforcement learning-based highway autonomous vehicle control. Green Energy Intell Transp 2024;3:100156. 





38. Li L, Zhao W, Wang C et al. Nash double Q-based multi-agent deep reinforcement learning for interactive merging strategy in mixed traffic. Expert Syst Appl 2024;237:121458. 

