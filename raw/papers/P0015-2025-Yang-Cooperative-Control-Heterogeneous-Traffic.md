# Cooperative control strategy for heterogeneous traffic flow in multi-lane on-ramp areas with connected and automated technology

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/75a49a4a35e8eb887808aa68d3102e06250f091d69816aed93067146187e24e6.jpg)


Wenzhang Yang a,b,c , Changyin Dong d,e , Ziqian Zhang a,b,c , Hui Zhang a,b,c , ， Hao Wang a,b,c,* 

a Jiangsu Key Laboratory of Urban ITS, Southeast University, Nanjing 211189, China 

b Jiangsu Province Collaborative Innovation Center of Modern Urban Traffic Technologies, Nanjing 211189, China 

c School of Transportation, Southeast University, Nanjing 211189, China 

d School of Aeronautics, Northwestern Polytechnical University, Xi’an 710072, China 

e National Key Laboratory of Aircraft Configuration Design, Xi’an 710072, China 

# A R T I C L E I N F O

Keywords: 

On-ramp 

Cooperative control 

Connected and automated technology 

Heterogeneous traffic flow 

# A B S T R A C T

With the rapid advancement of connected and automated technology, the study of traffic flow in on-ramp areas has become increasingly important in transportation research. This paper presents a cooperative control strategy for connected and automated vehicles (CAVs) in on-ramp areas under heterogeneous traffic flow conditions. It consists of two primary components: merging control and lane-changing control. The former focuses on coordinating CAVs traveling in the outer lane of the mainline with those entering from the ramp, with the goal of optimizing platoon dynamics before reaching the merging boundary to mitigate potential conflicts. The latter allows CAVs to make informed decisions about lane changes on the mainline, thereby promoting balanced traffic flow. To evaluate the strategy’s efficacy, a simulation framework is developed with calibrated parameters reflecting real-world conditions. Results demonstrate that the pro posed cooperative control strategy significantly improves traffic performance in on-ramp areas. Several safety-related indicators show average reduction rates exceeding $9 0 ~ \%$ for typical simu lation scenarios. Additionally, delays and cumulative discomfort index values can be reduced by up to $4 0 \%$ . Even with lower CAV penetration rates, significant improvements are achieved under this strategy. Furthermore, simulations reveal that the cooperative control approach mitigates the capacity drop phenomenon, enhancing overall merge-zone efficiency. These findings provide valuable insights for CAV control strategies in heterogeneous traffic flow environments, advancing the development of intelligent transportation systems. 

# 1. Introduction

The on-ramp area serves a critical function within the road network by facilitating the entry of vehicles onto the mainline of the highway. This specific zone is particularly susceptible to various traffic conflicts, notably those arising from merging challenges be tween vehicles on the outer lane of the mainline and those entering from the ramp. These conflicts significantly contribute to increased 

# Nomenclature

a acceleration of the subject vehicle 

aemer emergency braking deceleration of vehicles 

amax $a _ { \mathrm { m a x } }$ maximum acceleration of vehicles 

$a _ { \mathrm { m i n } }$ maximum deceleration of vehicles 

$\alpha$ minimum reduction coefficients for speed 

$\beta$ minimum reduction coefficients for deceleration 

C cumulative dissatisfaction of the driver 

$C ^ { * }$ threshold value of accumulate dissatisfaction 

CD cumulative discomfort of the subject vehicle 

CPMR conflict-potential mergence ratio 

$D$ discomfort endured by passengers of the subject vehicle 

$d$ lane-changing decision of the subject CAV 

d average delay 

Δt time step 

e headway error of the subject vehicle 

$G$ matrix including all feasible gap selection schemes 

$\boldsymbol { G } ^ { l }$ l-th gap selection scheme in G 

gi selected gap for vehicle “i” 

$\widetilde { g } _ { 1 , i }$ anticipated gap for vehicle “i” 

$\widetilde { g } _ { 2 , i }$ set of feasible gaps for ramp vehicle “i” in collaboration with Outside Lane CAVs 

$\widetilde { g } _ { 3 , i }$ set of feasible gaps for CAV “i” under active deceleration control 

γ a composite parameter 

$\overline { { K } }$ overall density 

$k _ { 1 }$ parameter in PATH ACC model 

$k _ { 2 }$ parameter in PATH ACC model 

$k _ { \mathrm { d } }$ parameter in PATH CACC model 

$k _ { \mathrm { I L } }$ density of vehicles in the Inside Lane 

$k _ { \mathrm { O L } }$ density of vehicles in the and Outside Lane 

$k _ { \mathrm { p } }$ parameter in PATH CACC model 

$K _ { \mathrm { P } }$ regulator parameter of the additional proportional term 

$K _ { \mathrm { R } }$ a regulator parameter 

$k _ { u }$ threshold value for enhancing uniformity 

$L$ vehicle length 

$L _ { 0 }$ length of the on-ramp area prior to the merging point 

$L _ { 1 }$ length of the acceleration lane 

$L _ { 2 }$ position difference threshold for lane-changing 

$\lambda$ flow rate 

$n$ discrete time index 

$N _ { \mathrm { E } }$ number of vehicles to exit the on-ramp area in a round 

$N _ { \mathrm { O L } }$ count of vehicles on the Outside Lane prior to the merging boundary 

$N _ { \mathrm { R } }$ counts of vehicles on the ramp prior to the merging boundary 

$N _ { \mathrm { R E } }$ number of ramp vehicles to exit the on-ramp area 

$N _ { \mathrm { ~ I L ~ } }$ quantities of vehicles on the Inside Lane 

$N _ { \mathrm { { { O L } } } }$ quantities of vehicles on the Outside Lane 

$N _ { \mathrm { ~ R ~ } } ^ { \ast }$ quantities of vehicles on the ramp 

$o _ { \mathrm { o u t } } ( n )$ lane-averaged mainstream occupancy 

$\widehat { \boldsymbol { o } }$ a set (desired) value for the occupancy 

$p$ probability of lane-changing selection 

$P$ probability 

pAV proportion AVs 

pCAV proportion of CAVs 

$p _ { \mathrm { H D V } }$ proportion of HDVs 

$q _ { r }$ the real (measured) ramp inflow 

$r ( n )$ on-ramp inflow 

rmin $r _ { \mathrm { m i n } }$ a minimum admissible ramp inflow 

rmax $r _ { \mathrm { m a x } }$ ramp’s flow capacity 

s spacing of the subject vehicle and the preceding vehicle 

$S_0$ minimum safety distance $S_1$ minimum distance required for a lane change $s_{\mathrm{brak}}$ braking spacing of the subject vehicle $s_{\mathrm{min}}$ critical spacing of the subject vehicle $t$ current time $t'$ estimated time for the subject vehicle to reach the merging boundary $T$ a certain duration $T'$ estimated arrival time of the subject vehicle $T''$ time of the subject vehicle to exit the on-ramp area $\tau$ reaction time of the driver  
TET time exposed TTC  
TETMP TET of merging process  
Time total duration that the subject vehicle spends within the on-ramp area $\tau_{\mathrm{lb}}$ lower bound of $\tau$ $\tau_{\mathrm{ub}}$ upper bound of $\tau$ $T_{\mathrm{RM}}$ cycle of ramp metering  
TTC time-to-collision  
TTC* TTC threshold value  
TTC1* TTC threshold value used to determine the need for emergency braking  
TTC2* TTC threshold value used to determine whether a lane change is permissible $t_x$ desired gap headway of vehicles $t_{x,\mathrm{lb}}$ lower bound of $t_x$ $t_{x,\mathrm{ub}}$ upper bound of $t_x$ $u$ uniformity of traffic flow $u_v$ uniformity in terms of speed $u_k$ uniformity in terms of density $\nu$ speed of the subject vehicle $\overline{\nu}$ overall average speed $\nu^*$ speed difference threshold for lane-changing $\nu_{\mathrm{f}}$ free flow speed $\overline{\nu}_{\mathrm{IL}}$ average speed of vehicles in the Inside Lane $\nu_{k,i}^*$ anticipated merging speed at which vehicle "k" when it is located behind vehicle "i" $\nu_{\mathrm{max}}$ maximum speed of vehicles $\overline{\nu}_{\mathrm{OL}}$ average speed of vehicles in the Outside Lane $x$ position of the subject vehicle $X$ number of vehicles arriving at a duration $T$ ZCAV set of all CAVs 

accident rates and decreased traffic efficiency (Jing et al., 2019; Rios-Torres and Malikopoulos, 2017). Research indicates that the accident rate per kilometer in on-ramp areas exceeds 3 times the average accident rate per kilometer across highways overall (McCartt et al., 2004). Particularly during peak hours, achieving safe and efficient merging presents significant challenges (Xue et al., 2023). 

In the context of on-ramp areas, early research primarily focused on analyzing how vehicle merging processes influence traffic flow. For instance, Sarvi et al. (2010) conducted field observations at eight interchange merging zones on Tokyo’s expressways, examining traffic volume, lane-changing behavior, and geometric characteristics. Their study revealed key patterns in queue discharge flow and driving behavior under congested conditions. Jia et al. (2005) employed a cellular automaton model to investigate the effects of acceleration lane length and traffic regulations. They found that prohibiting mainline vehicles from changing lanes into the acceleration lane could enhance the overall capacity of the ramp system—a finding that has since served as the theoretical foundation for current on-ramp management strategies. Additionally, researchers have observed that when congestion forms upstream of a bottleneck in highway on-ramp areas, the downstream maximum flow rate tends to fall significantly below the bottleneck’s nominal capacity. This phenomenon, termed “capacity drop,” has been extensively documented (Chen and Ahn, 2018; Leclercq et al., 2011). Wang et al. (2023) further contributed to this understanding by developing a detailed simulation method for highway on-ramp merging areas, along with modeling techniques to capture the capacity drop effect. Regarding traffic management strategies, ramp metering remains the most widely adopted approach. Among the various methods, the ALINEA algorithm—based on feedback control theory—has proven particularly effective (Papageorgiou et al., 1991). Building upon this, Wang et al. (2014) proposed the PI-ALINEA control algorithm to address the time-delay effects of ramp metering on traffic flow. 

The advancement of connected and automated technology presents innovative approaches to vehicle control strategies in on-ramp areas. In a connected and automated transportation environment, the roadway accommodates not only traditional human-driven vehicles (HDVs) but also connected human-driven vehicles (CVs), automated vehicles (AVs), and connected and automated vehi cles(CAVs)(Chenetal.202: Chenetal2025:Lietal2024b:Yaoetal2024: Yuetal,2023:Nagalurubravetietal.:Lin et al., 2023). Research indicates that integrating these vehicles with vehicle-to-everything (V2X) technology can significantly enhance 

traffic conditions in on-ramp areas (Luo et al., 2022; Yang et al., 2025; Zhu and Tasic, 2021). 

The cooperative control of CAVs, in particular, holds the potential to fundamentally address existing traffic issues (Li et al., 2024a; Xue et al., 2023; Yang et al., 2023a). By utilizing effective cooperative control strategies, it is possible to enhance both safety and traffic efficiency in on-ramp systems without compromising the right of way for ramp vehicles. Presently, research in this field primarily explores two main directions. The first direction focuses on optimizing the merging process, which involves coordinating control between vehicles on the ramp and those in the adjacent mainline lane. The objective here is to minimize merging conflicts for a safer merging process (Fang et al., 2022; Liu et al., 2023; Mu et al., 2021; Sun et al., 2020; Yang et al., 2023b). The second direction targets optimizing lane selection for CAVs where multiple lanes are available on the mainline. This approach aims to enable CAVs to choose the most appropriate lanes, thereby improving overall traffic efficiency (Luo et al., 2022; Hou et al., 2023; Han et al., 2023). 

Building on these approaches, recent studies have predominantly relied on simulation to evaluate cooperative control strategies for CAVs in on-ramp areas. For instance, Rios-Torres and Malikopoulos (2017) developed an optimization framework with closed-form analytical solutions for real-time CAV coordination in merging zones, demonstrating significant reductions in fuel consumption and travel time through simulations. Sun et al. (2020) proposed a bi-level dynamic programming approach for mixed traffic conditions, with simulation results indicating an $1 8 ~ \%$ increase in roadway capacity at high CAV penetration rates. Further improvements of $1 0 \mathrm { - } 1 5 \%$ were achieved through cooperative control strategies. Mu et al. (2021) advanced this line of research by introducing an eventtriggered rolling horizon system that divides the merging zone into pre-merging, virtual merging, and post-merging sub-areas, employing mixed-integer nonlinear programming and heuristic algorithms to optimize CAV platoon trajectories. Yang et al. (2023b) introduced a novel bi-level gap selection cooperative control method specifically designed for mixed traffic flows in on-ramp areas, which significantly enhanced merging safety without compromising traffic efficiency. 

A parallel research stream has emerged around virtual platoon theory, which reconceptualizes merging conflicts between ramp and mainline traffic flows within a unified virtual platoon framework. Chen et al. (2021) pioneered this approach by formulating merging coordination as a virtual car-following problem, creating a multi-predecessor following model with unidirectional multi-leader communication topology. Yang et al. (2023a) subsequently refined this concept through a virtual platoon − based speed control model that simultaneously improved fuel efficiency and passenger comfort during merging maneuvers. Meanwhile, reinforcement learning has gained traction as an alternative methodological approach. Li et al. (2023) demonstrated the effectiveness of reinforcement learning in training CAV behavior selection for merging scenarios, while He et al. (2023) developed a more sophisticated constrained adversarial reinforcement learning framework that employs a constrained actor-critic algorithm to optimize merging decisions in stochastic mixed traffic environments. 

The field has witnessed additional noteworthy contributions that have broadened both theoretical understanding and practical applications. Karimi et al. (2020) provided a systematic taxonomy of six distinct merging scenarios in CAV-HDV mixed traffic, developing customized control strategies for each case. Fang et al. (2022) conducted rigorous mathematical simulations to quantify the effects of communication delays on CAV merging performance. In a significant practical advancement, Liao et al. (2022) implemented a real-time digital twin system for CAV cooperative merging, with field tests in Riverside, California confirming substantial safety and 


Table 1 Summary of related studies on cooperative control of CAVs in the on-ramp area.


<table><tr><td rowspan="2">Reference</td><td colspan="2">Environment</td><td colspan="2">Module</td><td colspan="2">Method</td><td colspan="2">Cooperative</td><td colspan="2">Strengths</td></tr><tr><td>Pure CAVs</td><td>Hetero-geneous</td><td>Merging only</td><td>And lane-changing</td><td>Peri-odic</td><td>Real-time</td><td>Ord-ered</td><td>Bala-nced</td><td>Saf-ety</td><td>Effic-ency</td></tr><tr><td>Liu et al. (2023)</td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td></tr><tr><td>Jing et al. (2019)</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td></tr><tr><td>Rios-Torres and Malikopoulos (2017)</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td></tr><tr><td>Li et al. (2024a)</td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td>✓</td></tr><tr><td>Roncoli et al. (2017)</td><td></td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>✓</td></tr><tr><td>Karimi et al. (2020)</td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>Yang et al. (2023a)</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td></tr><tr><td>Sun et al. (2020)</td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td>✓</td></tr><tr><td>Fang et al. (2022)</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>Xiong et al. (2022)</td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td></tr><tr><td>Ramezani and Ye (2019)</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td></tr><tr><td>Xue et al. (2023)</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td></tr><tr><td>Shi et al. (2023)</td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td></tr><tr><td>Yang et al. (2023b)</td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>Luo et al. (2022)</td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td></tr><tr><td>Ding et al. (2021)</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>✓</td></tr><tr><td>Mu et al. (2021)</td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td>✓</td></tr><tr><td>Han et al. (2023)</td><td></td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td></tr><tr><td>Li et al. (2023)</td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td></tr><tr><td>Hou et al. (2023)</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td>✓</td><td>✓</td><td></td><td>✓</td></tr><tr><td>Chen et al. (2021)</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>Liao et al. (2022)</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>He et al. (2023)</td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td></td></tr><tr><td>This study</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr></table>

sustainability improvements under realistic communication constraints. Concurrently, multiple research teams have targeted specific performance metrics: Xiong et al. (2022) and Shi et al. (2023) focused on fuel efficiency and throughput optimization in mixed traffic, while Li et al. (2024a) introduced a dynamic cooperative merging assistance strategy specifically designed to enhance traffic flow efficiency. For heavy traffic conditions, Xue et al. (2023) developed a novel platoon-based optimal control approach that demonstrated particular effectiveness in high-density scenarios. 

It is important to note that these control strategies primarily target the merging process of ramp vehicles, with research scenarios limited to the ramp and an adjacent mainline lane. In contrast, Ding et al. (2021) proposed a control strategy for the multi-lane onramp area, effectively incorporating the merging process of ramp vehicles and lane-changing behavior of mainline vehicles. Hou et al. (2023) developed a hierarchical model for cooperative control of on-ramps under heterogeneous traffic conditions, which creates appropriate merging opportunities for ramp vehicles by adjusting the behavior of mainline vehicles. Roncoli et al. (2017) proposed a feedback control strategy for lane allocation at bottleneck locations. This strategy maximizes throughput by optimally allocating lanes to vehicles upstream of the bottleneck. Ramezani and Ye (2019) focused on alleviating highway congestion by controlling the lateral flow of autonomous vehicles, including a proactive lane density distribution optimization strategy and a reactive lane-change advisory system. Additionally, Han et al. (2023) introduced a trajectory optimization method for CAVs, encompassing both lane-changing and merging optimization. Liu et al. (2022) addressed multi-lane merging by integrating lane flow imbalance modeling with reinforcement learning for lane selection, overcoming limitations of single-lane merging studies. Yang et al. (2025) advanced this approach with a dual-module framework combining proximal policy optimization algorithm for merge control and lane-changing decisions, demonstrating notable improvements in efficiency. 

Table 1 summarizes the characteristics of current research on the cooperative control of CAVs in the on-ramp area. Several limitations persist in the existing literature: (1) Some approaches are designed exclusively for pure CAV environments, rendering them ineffective for heterogeneous traffic flows that include HDVs; (2) Most studies focus solely on merging control, with only a few exploring the integration of both merging and lane-changing controls; (3) In terms of cooperative control, the main objectives often focus on either making the platoon more ordered or balancing the traffic flow, with very few studies addressing both aspects simultaneously; (4) Regarding the strengths of control strategies, the primary goals are typically safety or traffic efficiency, yet considering both is crucial. (5) Numerous strategies depend on trajectory prediction methods, particularly for HDVs, which introduces reliability concerns, especially for non-real-time control applications. These gaps collectively highlight the need for a more robust and adaptable control framework. 

In response to these challenges, this paper proposes a novel cooperative control strategy for CAVs in on-ramp areas, with the dual objectives of mitigating traffic conflicts and improving overall traffic efficiency. The proposed strategy operates in real time without relying on trajectory prediction, thereby enhancing robustness in dynamic traffic conditions. Furthermore, it is specifically designed for heterogeneous traffic flows, ensuring compatibility with mixed CAV-HDV environments. The strategy also integrates both merging and lane-changing control, simultaneously optimizing platoon ordering and traffic flow balance to provide a comprehensive conflictresolution solution in on-ramp scenarios. To validate the approach, a high-fidelity simulation framework was developed, with key parameters calibrated using real-world traffic data. The results demonstrate the strategy’s effectiveness and offer practical insights for the implementation of cooperative control in connected and automated environments, contributing to the broader development of intelligent transportation systems. 

The paper is organized as follows. Section 2 outlines the operational environment of on-ramp areas under connected and automated vehicle technologies. Section 3 introduces the proposed cooperative control strategy. Section 4 describes the simulation modeling framework, including parameter calibration and evaluation indicators. Section 5 presents a thorough analysis of the simulation results. Finally, Section 6 provides the conclusions. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/eb0cf8e478f40d3df4ce54586c6a3bef055481b673633d8a3ff34ad22edba7d5.jpg)



Fig. 1. A typical on-ramp area with connected and automated technology.


# 2. Research scenario

Currently, there is a global surge in enthusiasm surrounding the research and development of intelligent vehicle technology. This development primarily revolves around two key technological pathways: automated technology, which focuses on achieving autonomous vehicle control to replace human drivers, and connected technology, which emphasizes seamless coordination between vehicles, infrastructures, and other elements. The convergence of these two technologies has given rise to CAVs. Consequently, it’s foreseeable that, prior to the full-scale adoption of CAV technology, we may witness the coexistence of four vehicle types on roads: HDVs, CVs, AVs, and CAVs. HDVs represent the majority of vehicles currently on the roads, controlled by human drivers. CVs, also under human control, are equipped with onboard information terminals that enable wireless communication and data exchange with other vehicles and infrastructures, ensuring real-time awareness of their speed and position. AVs operate autonomously for most of the time, boasting advanced driving capabilities surpassing those of HDVs, yet without communication capabilities with external platforms. As for CAVs, they represent the pinnacle, integrating all technologies of CVs and AVs, and demonstrating superior driving capabilities. 

The on-ramp area plays a crucial role in the highway network, serving as a pivotal point for vehicle transitions. As illustrated in Fig. 1, ramp vehicles begin to actively seek opportunities to merge into the mainline once they surpass the merging boundary. It’s crucial to understand that this merging process differs from regular lane changes, as it must be completed before reaching the end of the acceleration lane. Consequently, there are frequent traffic conflicts arising from these merging maneuvers, which are the most conspicuous feature of the on-ramp area (Rios-Torres and Malikopoulos, 2017; Zhu and Tasic, 2021). Moreover, since the mainline typically consists of multiple lanes, traffic conflicts resulting from merging can extend to adjacent lanes due to the lane-changing behavior of mainline vehicles. 

In a connected and automated environment, centralized control strategies offer significant benefits in managing vehicles within the on-ramp areas. By centrally regulating and organizing vehicles, conflicts between them can be more easily resolved, leading to smoother traffic flow (Xue et al., 2023; Yang et al., 2023b). Implementing centralized control requires establishing a roadside control center and deploying high-precision wide-range vehicle detectors in the on-ramp area. The control center is responsible for devising control strategies using available data and communicating control commands to nearby CAVs. Simultaneously, the vehicle detectors continuously monitor the position and speed of all vehicles within a specified section of the road, transmitting this data to the control center in real-time. Consequently, real-time monitoring of HDVs in the on-ramp area becomes feasible, blurring the distinction between CVs and conventional HDVs. Therefore, when modelling heterogeneous traffic flow in on-ramp areas with connected and automated technology, this study focuses on three vehicle types—HDVs, AVs, and CAVs. Additionally, as illustrated in Fig. 1, the modelling designates the mainline lane further from the ramp as the Inside Lane, while the one closer to the ramp is labeled the Outside Lane. 

# 3. Cooperative control strategy for CAVs

In the on-ramp area, the control center employs high-precision wide-range vehicle detectors to continuously monitor real-time information of all vehicles. Control decisions are made based on this information, following a pre-established strategy, and corre sponding instructions are transmitted to CAVs within the designated range. This pre-established strategy represents a cooperative control approach for CAVs, with the objective of enhancing traffic conditions. 

The cooperative control strategy proposed in this study for CAVs comprises two primary components. Firstly, the merging control aspect is examined, which involves coordinating vehicles on the mainline Outside Lane with those on the ramp. This coordination is achieved through the modulation of their right-of-way allocation, facilitating an organized merging process between vehicles on these respective lanes. The objective is to optimize platoon dynamics before reaching the merging boundary, thereby reducing potential conflicts. Secondly, the lane-changing control component is addressed, which focuses on enabling CAVs to make informed decisions regarding lane changes on the mainline. This entails managing traffic density and vehicle speed across the two mainline lanes to ensure a balanced flow of traffic. 

# 3.1. Merging control

The main traffic challenge observed in the on-ramp area is the merging interaction between vehicles on the mainline Outside Lane and those entering from the ramp. Encouraging a structured arrangement of vehicle platoon in both lanes before they reach the merging boundary has the potential to decrease conflict instances and improve the overall safety of the on-ramp system. This objective is central to merging control (Yang et al., 2023b). In the merging control section, the process of forming vehicle platoon can be understood as the selection of gaps by ramp vehicles. Each ramp vehicle can be seen as fitting into the gap between two vehicles on the Outside Lane. Once the gap for each ramp vehicle is identified, the composition of the resulting platoon, can be established. Through the development of optimal gap selection scheme, the formation of the most orderly vehicle platoon can be achieved, ultimately maximizing safety outcomes. 

# 3.1.1. Gap selection schemes of ramp vehicles

In this study, the merging control is executed at each simulation step, leading to the real-time formulation of gap selection schemes for ramp vehicles. At any specific simulation step, the anticipated gap for each ramp vehicle can be initially established by considering the speed and position of vehicles. This process can be formally represented by the following model: 

$$
\widetilde {g} _ {1, i} = \min  k, \forall k = 0, 1 \dots , N _ {\mathrm {O L}}
$$

$$
s. t. k \geq g _ {i - 1}, \forall k = 0, 1 \dots , N _ {\mathrm {O L}} \tag {1}
$$

$$
t _ {\mathrm {O L}, k + 1} ^ {\prime} (t) > t _ {\mathrm {R}, i} ^ {\prime} (t), \forall k = 0, 1 \dots , N _ {\mathrm {O L}} - 1
$$

$$
t _ {\mathrm {R}, i} ^ {\prime} (t) = t + \left(L _ {0} - x _ {\mathrm {R}, i} (t)\right) / v _ {\mathrm {R}, i} (t) \tag {2}
$$

$$
t _ {\mathrm {O L}, k} ^ {\prime} (t) = t + \left(L _ {0} - x _ {\mathrm {O L}, k} (t)\right) / v _ {\mathrm {O L}, k} (t) \tag {3}
$$

In the equation above, the subscript “OL” denotes the pertinent parameters of the Outside Lane, while the subscript “R” represents the relevant parameters of the ramp. $N _ { \mathrm { O L } }$ and $N _ { \mathrm { R } }$ denote the respective counts of vehicles on the Outside Lane and ramp prior to the merging boundary. v denotes the speed of the subject vehicle. $x$ represents the position of the subject vehicle. t is the current time. $g _ { i }$ signifies the selected gap for vehicle “i”. Meanwhile, $\widetilde { g } _ { 1 , i }$ represents the anticipated gap for vehicle “i”, where $\widetilde { g } _ { 1 , i } = k ^ { \prime \prime }$ indicates that vehicle “i” will merge into the gap between the vehicles “k” and $\boldsymbol { ^ { * } k } + \boldsymbol { 1 } ^ { \prime \prime }$ on the Outside Lane. $t '$ signifies the estimated time for the vehicle to reach the merging boundary. $L _ { 0 }$ is the length of the on-ramp area prior to the merging boundary. 

The coordination of CAVs is a crucial factor in determining the selection of gaps for ramp vehicles. CAVs have the ability to affect the feasible gap for vehicle merging by actively decelerating. For example, when considering a ramp vehicle “i” and an Outside Lane vehicle $\mathit { \Omega } ^ { \ast } k ^ { \prime \prime }$ , if $\widetilde { g } _ { 1 , i } = k ^ { \prime \prime }$ , it means that vehicle “k” will reach the merging boundary before vehicle “i”. However, if vehicle “k” is a CAV, it has the potential to arrive after vehicle “i” by using appropriate active deceleration, thus impacting the anticipated gap value for vehicle “i”. The effectiveness of the deceleration can be evaluated by calculating the merging speed of the vehicles. Assuming that when vehicle $^ { * } k$ ” reaches the merging boundary, the relationship between it and vehicle “i” in the adjacent lane meets the lanechanging condition, namely: 

$$
x _ {i} ^ {\prime} (t) - L _ {0} \geq L + S _ {1} \tag {4}
$$

$$
T T C _ {i, k} (t) \geq T T C _ {2} ^ {*} \text {o r} T T C _ {i, k} (t) \leq 0 \tag {5}
$$

where $\boldsymbol { x } _ { i } ^ { \prime }$ denotes the position of vehicle “i” when vehicle “k” reach the merging boundary. L is the vehicle length. $s _ { 1 }$ is the minimum distance required for a lane change. $T T C _ { 2 } ^ { * }$ represents the threshold value used to determine whether a lane change is permissible. TTC stands for time-to-collision, which is defined as “the time required for two vehicles to collide if they continue at their present speeds and on the same path” (Hayward, 1972). For any given vehicle, the TTC between it and the preceding vehicle is computed using the following formula: 

$$
T T C _ {i - 1, i} (t) = \frac {\mathbf {x} _ {i - 1} (t) - \mathbf {x} _ {i} (t) - L}{\nu_ {i} (t) - \nu_ {i - 1} (t)} \tag {6}
$$

where $T T C _ { i - 1 }$ , i represent the TTC value of the subject vehicle with its preceding vehicle. If vehicle “k” approaches the merging boundary after undergoing consistent deceleration, we can determine two critical speeds by applying Eqs. (4) and (5), which then enable us to calculate the speed at which vehicle $^ { * } k$ ” reaches the merging boundary: 

$$
x _ {i} (t) + v _ {i} (t) \frac {2 \left(L _ {0} - x _ {k} (t)\right)}{v _ {k , i} ^ {\prime} (t) + v _ {k} (t)} - L _ {0} = L + S _ {1} \tag {7}
$$

$$
\Rightarrow v _ {k, i} ^ {\prime \prime} (t) = \frac {2 v _ {i} (t) \left(L _ {0} - x _ {k} (t)\right)}{S _ {1} + L + L _ {0} - x _ {i} (t)} - v _ {k} (t) \tag {8}
$$

$$
\begin{array}{l} \left[ x _ {i} (t) + v _ {i} (t) \frac {2 \left(L _ {0} - x _ {k} (t)\right)}{v _ {k , i} ^ {\prime \prime} (t) + v _ {k} (t)} - L _ {0} - L \right] / \left(v _ {k, i} ^ {\prime \prime} (t) - v _ {i} (t)\right) = T T C _ {2} ^ {*} (9) \\ \Rightarrow \nu_ {k, i} ^ {\prime \prime} (t) = \frac {- B + \sqrt {B ^ {2} - 4 A C}}{2 A} \\ A = T T C _ {2} ^ {*} (10) \\ \end{array}
$$

$$
B = T T C _ {2} ^ {*} \nu_ {k} (t) - T T C _ {2} ^ {*} \nu_ {i} (t) - x _ {i} (t) + L + L _ {0}
$$

$$
C = - \left(\boldsymbol {x} _ {i} (t) - L _ {0} - L\right) \nu_ {k} (t) - 2 \nu_ {i} (t) \left(L _ {0} - \boldsymbol {x} _ {k} (t)\right) - T T C _ {2} ^ {*} \nu_ {i} (t) \nu_ {k} (t)
$$

$$
v _ {k, i} ^ {\prime} (t) = \left\{ \begin{array}{c} v _ {k, i} ^ {\prime \prime} (t), \text {i f} v _ {k, i} ^ {\prime \prime} (t) <   v _ {i} (t) \\ v _ {k, i} ^ {\prime \prime \prime} (t), \text {e l s e} \end{array} \right. \tag {11}
$$

where $\nu _ { k , i } ^ { \prime }$ denotes the anticipated speed at which vehicle $\scriptstyle { \mathcal { k } }$ ” will reach the merging boundary when it is located behind vehicle “i”. Thus, it can be inferred that the acceleration of vehicle “k” at any specific time is: 

$$
a _ {k, i} (t) = \frac {\nu_ {k , i} ^ {2} (t) - \nu_ {k} ^ {2} (t)}{2 \left(L _ {0} - x _ {k} (t)\right)} \tag {12}
$$

where a represents the acceleration of the subject vehicle. In this way, the rationality for the active deceleration of the Outside Lane CAVs can be judged. The process facilitates an expansion in the number of feasible gaps for ramp vehicle “i”, which occurs as follows: 

$$
\widetilde {g} _ {2, i} = \{k \}, \forall k = 0, 1 \dots , N _ {\mathrm {O L}} - 1
$$

$$
\begin{array}{l} s. t. k + 1 \in Z _ {\text {C A V}}, \forall k = 0, 1 \dots , N _ {\mathrm {O L}} - 1 \\ k <   \widetilde {g} _ {1, i}, \forall k = 0, 1 \dots , N _ {\mathrm {O L}} - 1 \tag {13} \\ \end{array}
$$

$$
\mathcal {v} _ {k + 1, i} ^ {\prime} (t) > \alpha v _ {k + 1} (t), \forall k = 0, 1 \dots , N _ {\mathrm {O L}} - 1
$$

$$
a _ {k + 1, i} (t) > \beta a _ {\min }, \forall k = 0, 1 \dots , N _ {\mathrm {O L}} - 1
$$

where $\widetilde { g } _ { 2 , i }$ denotes the set of feasible gaps for ramp vehicle “i” in collaboration with Outside Lane CAVs. ZCAV represents the set of all CAVs. $\alpha$ and $\beta$ are the minimum reduction coefficients for speed and deceleration, respectively, with values between 0 and 1. $a _ { \mathrm { m i n } }$ represents the maximum deceleration of vehicles under normal conditions. 

Meanwhile, if the ramp vehicle “i” is a CAV, it possesses the capability to expand its feasible gaps by actively decelerating and positioning itself behind the corresponding vehicle on the Outside Lane, as shown in the following equation: 

$$
\begin{array}{l} \widetilde {g} _ {3, i} = \{k \}, \forall k = 0, 1 \dots , N _ {\mathrm {O L}} \\ s. t. k > \widetilde {g} _ {1, i}, \forall k = 0, 1 \dots , N _ {\mathrm {O L}} \\ k \geq g _ {i - 1}, \forall k = 0, 1 \dots , N _ {\mathrm {O L}} \tag {14} \\ \end{array}
$$

$$
\mathcal {V} _ {i, k} ^ {\prime} (t) > \alpha \nu_ {i} (t), \forall k = 1 \dots , N _ {\mathrm {O L}}
$$

$$
a _ {i, k} (t) > \beta a _ {\min }, \forall k = 1 \dots , N _ {\mathrm {O L}}
$$

where $\widetilde { g } _ { 3 , i }$ represents the set of feasible gaps for CAV “i” under active deceleration control. Consequently, for any ramp vehicle, the set encompassing all feasible gaps can be mathematically expressed as follows: 

$$
\widetilde {g} _ {i} = \left\{ \begin{array}{c} \widetilde {g} _ {1, i} \cup \widetilde {g} _ {2, i} \cup \widetilde {g} _ {3, i}, \text {i f} i \in Z _ {\mathrm {C A V}} \\ \widetilde {g} _ {1, i} \cup \widetilde {g} _ {2, i}, \text {e l s e} \end{array} \right. \tag {15}
$$

By systematically calculating the feasible gap sets for each vehicle in sequence, a comprehensive matrix encompassing all feasible gap selection schemes for ramp vehicles can be derived, as illustrated in the subsequent representation: 

$$
G = \left[ \begin{array}{l} G (1) \\ G (2) \\ G (3) \\ \dots \dots \\ G \left(N _ {G}\right) \end{array} \right] = \left[ \begin{array}{c} \widetilde {g} _ {1} (1), \widetilde {g} _ {2} (1), \widetilde {g} _ {3} (1) \dots , \widetilde {g} _ {N _ {R}} (1); \\ \dots \dots \\ \widetilde {g} _ {1} (1), \widetilde {g} _ {2} (1), \widetilde {g} _ {3} (1) \dots , \widetilde {g} _ {N _ {R}} \left(n _ {N _ {R}}\right); \\ \dots \dots \\ \widetilde {g} _ {1} \left(n _ {1}\right), \widetilde {g} _ {2} \left(n _ {2}\right), \widetilde {g} _ {3} \left(n _ {3}\right) \dots , \widetilde {g} _ {N _ {R}} \left(n _ {N _ {R}}\right) \end{array} \right] \tag {16}
$$

where $G$ is the matrix including $N _ { G }$ feasible gap selection schemes. $G ( l )$ means the l-th gap selection scheme in G. $\widetilde { g } _ { i } ( l )$ means the l-th selected gap of vehicle “i”. $n _ { i }$ means the number of elements in $\widetilde { g } _ { i }$ . Since $\widetilde { g } _ { i }$ is related to the selected gap of vehicle ${ } ^ { \iint } i \mathbf { - } \mathbf { 1 } ^ { \prime \prime }$ , so the value of $n _ { i }$ is not fixed. 


(a)



OL4 Ramp4 OL3 Ramp3 Ramp2 OL2 Ramp1 OL1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/5fec5e31cc6d1f527624a7f2df0e18731752f6d66f42456006da5989a3e31a18.jpg)



Ramp4 Ramp3 OL4OL3Ramp2 Ramp1 OL2OL1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/432b0b6ee23945ba7892e804e6939b84a7710365561c8f6e324caa3ce02d5b79.jpg)


OL4OL3 Ramp4 Ramp3 Ramp2 Ramp1 OL2OL1 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/b6864d3e628d3f664eb24db8ac5344b9b995781ae113dfeb31e13542de9c41b4.jpg)



—ReliableVB Unreliable VB



Fig. 2. The diagram of virtual platoons employing various gap selection schemes. (The “OL” in the figure represents Outside Lane.).


# 3.1.2. Optimal scheme

In order to achieve effective cooperative control and minimize conflicts during merging, it is crucial to determine the most optimal gap selection scheme from various feasible options. For instance, when arranging all vehicles on the Outside Lane and ramp prior to the merging boundary in Fig. 1 into a virtual platoon using different gap selection schemes, there are multiple arrangements possible. Fig. 2 depicts three of these arrangements. According to Yang et al. (2023b), the connection mode between any two adjacent vehicles in a virtual platoon can be referred to as a vehicle bond (VB). In this study, VBs are categorized into two types: reliable VBs and unreliable VBs. A reliable VB signifies that the subject vehicle can perceive real-time information from the preceding vehicle in the virtual platoon, enabling it to make informed judgments. Reliable VB occurs in two situations: when the preceding vehicle and the subject vehicle are on the same lane, or when the subject vehicle is a CAV. On the other hand, an unreliable VB represents a connection that lacks reliability and is the primary factor leading to potential conflicts during merging. Fig. 3 provides a clear illustration of all the scenarios corresponding to reliable VBs and unreliable VBs. 

Therefore, in order to establish an ideal virtual platoon, this study proposes a two-layered approach for selecting the optimal scheme. The first layer focuses on minimizing the number of unreliable VBs, while the second layer considers the degree of vehicle sequence changes. The optimal scheme selection function can be defined as follows: 

$$
G ^ {\prime} = G \left(\min  f _ {1} (G (l))\right), l = 1 \dots , N _ {G} \tag {17}
$$

$$
G ^ {\prime \prime} = G ^ {\prime} \left(\operatorname {m i n f} _ {2} \left(G ^ {\prime} (l)\right)\right), l = 1 \dots , N _ {G ^ {\prime}} \tag {18}
$$

$$
f _ {2} \left(G ^ {\prime} (l)\right) = \sum_ {i = 1} ^ {N _ {\mathrm {O L}} + N _ {\mathrm {R}}} \left| S _ {i} - S _ {i} ^ {\prime} \right| \tag {19}
$$

where $f _ { 1 } ( G ( l ) )$ represents the function to calculate the number of unreliable VBs in the virtual platoon determined by $G ( l ) , N _ { G }$ is the number of gap selection schemes in G’. G’’ is the optimal gap selection scheme. S represents the sequence of the subject vehicle based on its current position relative to all other vehicles involved in the gap selection process. On the other hand, S’ represents the sequence of the subject vehicle within the virtual platoon which is determined by $G ^ { \prime } ( l )$ . 

Based on Eqs. 17–19, the optimal gap selection scheme can be derived. Subsequently, cooperative control instructions will be assigned to all CAVs within the specified range. During the simulation, when a CAV is assigned a virtual preceding vehicle from a different lane, Eqs. 7–12 are utilized to update its acceleration. In all other scenarios, the CAV will follow the preceding vehicle in its respective lane. 

# 3.2. Lane-changing control

The cooperative lane-changing control strategy for CAVs aims to optimize traffic flow on the two mainline lanes, namely the Inside Lane and the Outside Lane. The primary objective is to ensure a balanced distribution of vehicles between the lanes. Unequal distribution in terms of vehicle volume or average speed can indicate substantial differences in traffic flow characteristics between the lanes, leading to low utilization of one lane. Such imbalance will negatively impact overall traffic efficiency. To quantify the uniformity of traffic flow, this study proposes the following model: 

$$
u (t) = u _ {v} (t) \cdot u _ {K} (t) \tag {20}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/132ee18cabc8e291446a9cf7974d686177e56defa4fe83ad4967ed8b4eaa014b.jpg)



Fig. 3. The relationship between VB types and vehicle types.


$$
u _ {\nu} (t) = 1 - \frac {\sqrt {\left[ (\bar {\nu} _ {\mathrm {I L}} (t) - \bar {\nu} (t)) ^ {2} + (\bar {\nu} _ {\mathrm {O L}} (t) - \bar {\nu} (t)) ^ {2} \right] / 2}}{\bar {\nu} (t)} \tag {21}
$$

$$
u _ {K} (t) = 1 - \frac {\sqrt {\left[ \left(K _ {\mathrm {I L}} (t) - \bar {K} (t)\right) ^ {2} + \left(K _ {\mathrm {O L}} (t) - \bar {K} (t)\right) ^ {2} \right] / 2}}{\bar {K} (t)} \tag {22}
$$

where $u$ represents the uniformity of traffic flow. A higher value of $u$ indicates a more balanced distribution of traffic flow. $u _ { \nu }$ and $u _ { k }$ are measures of uniformity in terms of speed and density, respectively. $\overline { { \nu } } _ { \mathrm { { I L } } }$ and $\overline { { \nu } } _ { \mathrm { O L } }$ indicate the average speed of vehicles in the Inside Lane and Outside Lane, respectively. v denotes the overall average speed. $K _ { \mathrm { I L } }$ and $K _ { \mathrm { O L } }$ designate the density of vehicles in the Inside Lane and Outside Lane, respectively. $\overline { { K } }$ is the overall density. Eqs. 23–28 outline the calculation methods for the aforementioned parameters. It is pertinent to note that when determining parameters pertaining to the Outside Lane, it is essential to include ramp vehicles in the calculation. This is due to the fact that ramp vehicles will ultimately merge into the Outside Lane. 

$$
\bar {\nu} (t) = \left(\bar {\nu} _ {\mathrm {I L}} (t) + \bar {\nu} _ {\mathrm {O L}} (t)\right) / 2 \tag {23}
$$

$$
\bar {v} _ {\mathrm {I L}} (t) = \sum_ {i = 1} ^ {N _ {\mathrm {I L}} ^ {\prime}} \left[ v _ {i} (t) \right] / N _ {\mathrm {I L}} ^ {\prime} \tag {24}
$$

$$
\bar {\nu} _ {\mathrm {O L}} (t) = \sum_ {i = 1} ^ {N _ {\mathrm {O L}} ^ {\prime} + N _ {\mathrm {R}} ^ {\prime}} \left[ \nu_ {\mathrm {i}} (t) \right] / \left(N _ {\mathrm {O L}} ^ {\prime} + N _ {\mathrm {R}} ^ {\prime}\right) \tag {25}
$$

$$
\bar {K} (t) = \left(K _ {\mathrm {I L}} (t) + K _ {\mathrm {O L}} (t)\right) / 2 \tag {26}
$$

$$
K _ {\mathrm {I L}} (t) = N _ {\mathrm {I L}} ^ {\prime} / \left(L _ {0} + L _ {1}\right) \tag {27}
$$

$$
K _ {\mathrm {O L}} (t) = \left(N _ {\mathrm {O L}} ^ {\prime} + N _ {\mathrm {R}} ^ {\prime}\right) / \left(L _ {0} + L _ {1}\right) \tag {28}
$$

where $N _ { \mathrm { I L } } , N _ { \mathrm { O L } } ^ { \prime }$ and $N _ { \mathrm { ~ R ~ } } ^ { \prime }$ symbolize the respective quantities of vehicles on the Inside Lane, Outside Lane, and ramp. 

The primary goal of cooperative lane-changing control for CAVs is to achieve a well-balanced traffic flow on multiple lanes. As mentioned previously, a higher value of “u” indicates a higher level of equilibrium between the traffic flow on the two lanes. Hence, during the simulation, a CAV’s decision to change lanes depends on the magnitude of the increase in the $u$ value, as outlined below: 

$$
d _ {i} = \left\{ \begin{array}{c} 1, \text {i f} u _ {i} ^ {\prime} (t) \geq k _ {u} \cdot u (t) \\ 0, \text {e l s e} \end{array} \right. \tag {29}
$$

where $d$ represents the lane-changing decision of the subject CAV. If $d$ is equal to 1, it indicates that the subject vehicle intends to change lanes. Conversely, if $d$ is equal to 0, the CAV will refrain from seeking lane-changing opportunities. $\boldsymbol { u ^ { \prime } } _ { i }$ signifies the uniformity 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/d7f0c1a805a579d8649df517deaa7a0e9cd79d103ff56cbf3658f79a2fa637df.jpg)



Fig. 4. Simulation model architecture.


of traffic flow after CAV “i” changes its lane. $k _ { u }$ denotes the threshold value for enhancing uniformity, which must be greater than 1. It is crucial to emphasize that once a CAV decides to change lanes, its actual execution of the lane change should still be subjected to verification based on lane-changing conditions. 

# 4. Simulation modelling framework

# 4.1. Simulation modelling method

In traffic mathematical modelling and simulation, the conventional method of car-following simulation is widely used (Ni, 2016). This method primarily concentrates on monitoring the movements of a constrained number of vehicles, varying from a few to several dozen. However, it falls short for prolonged continuous traffic simulation and encounters difficulties in accurately representing more complex vehicle behaviors. The CA model addresses these challenges. In cellular automata models, a lane is typically divided into multiple cells. Each cell corresponds to a one-dimensional array, collectively forming a fixed-size two-dimensional array that represents the lane (Simon and Gutowitz, 1998; Tadaki and Kikuchi, 1995). In traffic simulations, vehicles transition between these cells, and their data is distributed mathematically across different arrays. When a vehicle enters or leaves the road, its information is exchanged between corresponding arrays as well. Nonetheless, in this model, vehicle data is stored within these fixed-interval cells, retaining crucial approximate information while neglecting certain specifics. As a result, attaining precise control of vehicles becomes arduous. 

Drawing on the principles of cellular automata models, this research divides vehicles into three primary categories within the mathematical simulation model: approaching vehicles, in-area vehicles, and departed vehicles, as depicted in Fig. 4. Moreover, the first two categories are further divided into three sub-categories based on different lanes: Inside Lane, Outside Lane, and ramp. Each sub-category is represented by a two-dimensional array designed to hold vehicle data. Every vehicle is associated with a onedimensional array containing essential data such as vehicle ID, estimated arrival time, vehicle type, speed, position, and acceleration. Certain data remain constant, reflecting the inherent traits of the vehicle, while others are dynamic, updated as the simulation progresses through various vehicle behavior models and control strategies. The integration of these one-dimensional arrays constructs the corresponding two-dimensional arrays. Lane-changing, entrance, and exit actions are carried out by adding or removing specific one-dimensional arrays within the two-dimensional arrays. Consequently, the size of any two-dimensional array remains flexible. This methodology facilitates the real-time monitoring and storage of vehicle data, while also streamlining vehicle control within the same vicinity. Unlike conventional microscopic car-following simulations, this modelling approach avoids excessive storage of redundant information and enhances various functionalities. Moreover, its simulation accuracy surpasses that of cellular automata models. 

In the simulation modelling framework, simulations adhere to the process illustrated in Fig. 5. First, all approaching vehicles are simultaneously generated according to specific rules. Then, as the main process progresses with each time step, continuous updates are made for variables such as acceleration, speed, position, and located lane for in-area vehicles. Additionally, entrances and exits of vehicles are constantly determined. Finally, upon completion of the simulation, all required data, including evaluation indicators, are generated as output. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/7aef06e27a58040704f03de489c88ecc5336a966142817a97a0590f763a9eba7.jpg)



Fig. 5. Simulation process.


# 4.2. Modelling the behaviors and dynamics of vehicles

This section presents several models for generating or updating fundamental vehicle information within the simulation. This en compasses the generation of traffic flow, the updating of vehicle acceleration, speed, and position, as well as the modelling of carfollowing and lane-changing behaviors. 

# 4.2.1. Traffic flow generation

Throughout the process of generating traffic flow, there are two key points. First, the arrival of vehicles should be randomized while carefully managing flow rates and proportions of various vehicle types for accurate simulation. Second, since vehicles enter the simulation environment at the starting section, it’s important to set constraints for vehicles entering the on-ramp area. As a result, the following methods are established for generating initial vehicle data. 

The first and most important task is to set the estimated arrival time of vehicles. Researches have shown that the pattern of vehicle arrivals on a specific section of a continuous road follows a Poisson distribution (Rengaraju and Rao, 1995): 

$$
P (X = k) = \frac {(\lambda T) ^ {k}}{k !} \mathrm {e} ^ {- \lambda T}, k = 0, 1, 2, 3 \dots \tag {30}
$$

where $P$ is the probability. T is a certain duration. X is the number of vehicles arriving at the duration. λ is the flow rate. Therefore, the probability of no vehicles arriving during a given duration can be expressed as follows: 

$$
P (X = 0) = \mathrm {e} ^ {- \lambda T} \tag {31}
$$

In essence, $P ( X = 0 )$ ) represents the likelihood that a vehicle’s headway exceeds or equals T. Thus, it verifies that vehicle headways follow a negative exponential distribution: 

$$
P (h \geq T) = \mathrm {e} ^ {- \lambda T} \tag {32}
$$

$$
\Rightarrow T = - \frac {\ln (P (h \geq T))}{\lambda} \tag {33}
$$

The probability value of $P ( h \geq T )$ lies within the range of [0, 1), aligning with the characteristic of uniformly distributed random numbers. This can be expressed as follows: 

$$
Y = P (h \geq T) \tag {34}
$$

$$
f _ {5} (Y) = \left\{ \begin{array}{c} 1, 0 \leq Y <   1 \\ 0, \text {e l s e} \end{array} \right. \tag {35}
$$

where $f _ { 5 } ( Y )$ represents the probability density function of the parameter Y. Therefore, the estimated arrival time of vehicles can be determined as follows: 

$$
T _ {1} ^ {\prime} (1) = 0 \tag {36}
$$

$$
T _ {i + 1} ^ {\prime} = T _ {i} ^ {\prime} - \ln (Y) / \lambda , i = 1, 2, 3, \dots \tag {37}
$$

where T’ represents the estimated arrival time of the subject vehicle. 

Regarding the initial data for other parameters: Firstly, assigning a unique ID to each vehicle is essential for subsequent vehicle search and identification. Vehicle types need to be allocated based on the varying proportions of HDVs, AVs, and CAVs. The initial lane of the subject vehicle corresponds to the lane in which it was generated. Car-following characteristic parameters of vehicles are randomly generated within predefined ranges. Any remaining parameters can be initially set to zero. 

After generating the initial data, it’s also essential to establish the rule for vehicles entering the on-ramp area. The decision for a vehicle to access this zone depends on the position and speed of the last in-area vehicle in its lane. Using “j” to represent the vehicle ready to enter the on-ramp area and ${ \mathfrak { s } } _ { j - 1 } \prime \prime$ to indicate the last in-area vehicle in its lane, the critical spacing for any vehicle ”j“ can be calculated as follows: 

$$
s _ {\min  j} (t) = f _ {4} \left(v _ {j - 1} (t)\right) \tag {38}
$$

where $s _ { \mathrm { m i n } }$ represents the critical spacing of the subject vehicle. $f _ { 4 }$ is the speed-spacing relationship function of the subject vehicle, which is determined by its car-following characteristics. Since vehicle “j” begins at position 0 upon entering the on-ramp area, the position of vehicle ${ \mathrm { } ^ { \mathrm { 4 } } } j { \mathrm { - } } 1 ^ { \prime \prime }$ corresponds to the spacing between vehicle ”j“ and vehicle $" j  – 1 \prime$ . As a result, for any given vehicle “j”, establish its entrance restriction according to Rule 1, where Time_Now denotes the current simulation time, and Deci signifies the 

vehicle entrance decision. If Deci equals 0, restrict vehicle “j” from entering; if Deci equals 1, allow vehicle “j” to enter. 


Rule 1: Vehicle entrance restriction


<table><tr><td>if Time_Now &gt; T&#x27;j</td></tr><tr><td>if smin,j(t) &gt; xj-1(t)</td></tr><tr><td>Deci = 0</td></tr><tr><td>else</td></tr><tr><td>Deci = 1</td></tr><tr><td>vj(t) = vj-1(t)</td></tr><tr><td>end if</td></tr><tr><td>end if</td></tr><tr><td>return Deci, vj(t) (if Deci = 1)</td></tr></table>

# 4.2.2. Update of vehicle acceleration, speed, and position

In traffic simulation, accurately updating a vehicle’s speed and position during each simulation step hinges on first determining the longitudinal acceleration of the vehicle. In this study, the initial values for the vehicles’ longitudinal acceleration were sourced either from the car-following model or the vehicle’s cooperative control strategy, depending on the particular scenario. However, additional processing is necessary on these initial values to derive the final vehicle acceleration. 

When the vehicle is running under normal conditions in simulation, it’s essential to limit its acceleration and speed within pre defined ranges. Keeping this in consideration, the initial acceleration is handled as follows: 

$$
a _ {i} (t) = \min  \left\{a _ {\max }, a _ {i} (t), \frac {\nu_ {\max } - \nu_ {i} (t)}{\Delta t} \right\} \tag {39}
$$

$$
a _ {i} (t) = \max  \left\{a _ {\min }, a _ {i} (t), \frac {- v _ {i} (t)}{\Delta t} \right\} \tag {40}
$$

where Δt denotes the time step. $a _ { \mathrm { m a x } }$ represents the maximum acceleration of vehicles. $\nu _ { \mathrm { m a x } }$ represents the maximum speed of vehicles. Eqs. (39) and (40) serve to maintain the vehicles’ speeds within the range of [0, $\nu _ { \mathrm { m a x } } ]$ throughout the simulation, and ensuring that acceleration under normal conditions remains within the bounds of $[ \boldsymbol { a } _ { \mathrm { m i n } } , \boldsymbol { a } _ { \mathrm { m a x } } ]$ . 

In addition, to prevent collisions within the simulation, vehicles must engage their brakes in hazardous scenarios. This study categorizes the braking behavior of vehicles into four distinct steps: 

(1) Firstly, when there is a potential risk of collision between vehicles, they will decelerate to prevent accidents. This study utilizes the concept of TTC to assess this collision risk. Therefore, the first step of vehicles’ braking behavior is as follows: 

$$
a _ {i} (t) = \left\{ \begin{array}{c c} a _ {\min }, & \text {i f} 0 <   T T C _ {i - 1, i} (t) <   T T C ^ {*} \\ & a _ {i} (t), \text {e l s e} \end{array} \right. \tag {41}
$$

where $T T C ^ { * }$ is the TTC threshold value, it is used to delimit whether the current scene is safe. 

(2) When the risk of vehicles colliding is high, emergency braking kicks in. In these scenarios, the vehicle’s braking becomes more forceful compared to regular conditions. As a result, the vehicle exhibits the following secondary braking behavior: 

$$
a _ {i} (t) = \left\{ \begin{array}{c} a _ {\text {e m e r}}, \text {i f} 0 <   T T C _ {i - 1, i} (t) <   T T C _ {1} ^ {*} \\ a _ {i} (t), \text {e l s e} \end{array} \right. \tag {42}
$$

where $T T C _ { 1 } { } ^ { * }$ represents the threshold value used to determine the need for emergency braking, and is set to a value lower than $T T C ^ { * }$ $a _ { \mathrm { e m e r } }$ is the emergency braking deceleration, with its value significantly smaller than $a _ { \mathrm { m i n } }$ . 

(3) Both CAVs and AVs possess the ability to accurately detect the acceleration, speed, and position of the preceding vehicle. Therefore, when the preceding vehicle decelerates, they are equipped to initiate emergency braking in extreme circumstances. Sub sequently, the third braking behavior of vehicles unfolds as follows: 

$$
a _ {i} (t) = \left\{ \begin{array}{c} a _ {\text {e m e r}, \text {i f}} v _ {i - 1} (t) <   v _ {i} (t) \& a _ {i - 1} (t) <   0 \& s _ {i} (t) <   s _ {\text {b r a k}, i} (t) \\ a _ {i} (t), \text {e l s e} \end{array} \right. \tag {43}
$$

$$
s _ {\text {b r a k}, i} (t) = L + S _ {0} - v _ {i - 1} ^ {2} (t) / \left(2 * a _ {i - 1} (t)\right) + v _ {i} ^ {2} (t) / \left(2 * a _ {\text {e m e r}}\right) \tag {44}
$$

where s means the spacing of the subject vehicle and the preceding vehicle, $\begin{array} { r } { s _ { i } ( t ) = x _ { i - 1 } ( t ) - x _ { i } ( t ) . } \end{array}$ . $s _ { \mathrm { b r a k } }$ represents the braking spacing of the subject vehicle. $S _ { 0 }$ is the minimum safety distance. Eqs. (43) and (44) ensure that when emergency braking is completed, the vehicle stops behind the preceding vehicle and maintains a minimum safety distance from it. However, this braking behavior only applies to CAVs and AVs. 

(4) When the distance between vehicles falls below the minimum safety threshold, the subject vehicle must also initiate emergency braking. As a result, we have outlined the following final step for vehicle braking behavior: 

$$
a _ {i} (t) = \left\{ \begin{array}{c} a _ {\text {e m e r}}, \text {i f} s _ {i} (t) <   L + S _ {0} \\ a _ {i} (t), \text {e l s e} \end{array} \right. \tag {45}
$$

In conclusion, we’ve outlined six steps for processing vehicle acceleration, as detailed in Eqs. (39), 40, 41, 42, 43, and 45. Throughout each simulation step, the initial acceleration values for vehicles are applied sequentially using the aforementioned formulas to determine vehicles’ final acceleration at that step. Subsequently, we adjust a vehicle’s current speed based on its acceleration, and then update its position using both the current speed and the speed from the previous step. This process unfolds in the following formulas: 

$$
\nu_ {i} (t) = \nu_ {i} (t - 1) + a _ {i} (t - 1) \Delta t \tag {46}
$$

$$
x _ {i} (t) = x _ {i} (t - 1) + \frac {\nu_ {i} (t - 1) + \nu_ {i} (t)}{2} \Delta t \tag {47}
$$

where t-1denotes the previous time step. 

# 4.2.3. Car-following models

In traffic simulation, modelling car-following behavior is crucial. Yet, much of the previous research has been criticized for oversimplification, assuming that all vehicles of the same type behave identically. This simplification is apparent in the uniform selection and parameter settings of car-following models. However, in reality, there are notable variations in car-following behaviors among vehicles on actual roads. Relying solely on a single model undermines the simulation’s credibility. Hence, this study introduces greater randomness into modelling car-following behaviors. Instead of a one-size-fits-all approach, multiple car-following models are employed for vehicles of the same type. Furthermore, key parameters in the models fluctuate within predetermined ranges, reflecting the diversity observed in real-world driving. This approach allows the simulation to better capture the nuances of car-following behaviors, enhancing its overall credibility. 

Specifically, this study integrates a range of commonly employed car-following models into the simulation framework. For HDVs, the Intelligent Driver Model (IDM) (Treiber et al., 2000), Longitudinal Control Model (LCM) (Ni, 2016), and Gipps model (Gipps, 1981) are utilized equally. The car-following behaviors of AVs are modeled using IDM and the PATH adaptive cruise control (ACC) model (Milan´es and Shladover, 2014). Additionally, the PATH cooperative adaptive cruise control (CACC) model (Milan´es and Shladover, 2014) is integrated to model car-following behaviors of CAVs, alongside the IDM and the PATH ACC model. Key parameters include the desired gap headway between vehicles and driver’s reaction time, with values stochastically assigned within predetermined ranges that vary according to vehicle type. 

4.2.3.1. IDM. The IDM, introduced by Treiber et al. (2000), stands as one of the foremost car-following models extensively employed in research. Its applicability extends beyond merely elucidating the car-following dynamics of HDVs to encompass AVs and CAVs as well. The IDM posits that the acceleration of the subject vehicle is influenced by a composite effect of the driving force aimed at attaining maximum speed and the drag force exerted by the preceding vehicle. Typical formulations of this model are outlined as follows: 

$$
a _ {i} (t) = a _ {\max } \left[ 1 - \left(\frac {v _ {i} (t)}{v _ {\mathrm {f}}}\right) ^ {4} - \left(\frac {s _ {i} ^ {*} (t)}{s _ {i} (t) - L}\right) ^ {2} \right] \tag {48}
$$

$$
s _ {i} ^ {*} (t) = S _ {0} + t _ {x} \nu_ {i} (t) + \frac {\left(\nu_ {i} (t) - \nu_ {i - 1} (t)\right) \nu_ {i} (t)}{2 \sqrt {- a _ {\operatorname* {m a x}} a _ {\operatorname* {m i n}}}} \tag {49}
$$

where $\nu _ { \mathrm { f } }$ denotes the free flow speed. $t _ { x }$ represents the desired gap headway of vehicles. Within simulation, the values of $t _ { x }$ are randomly assigned from a predetermined range, as expressed in the following equation: 

$$
f _ {3} \left(t _ {x}\right) = \left\{ \begin{array}{c} \frac {1}{t _ {x , \mathrm {u b}} - t _ {x , \mathrm {l b}}}, t _ {x, \mathrm {l b}} \leq t _ {x} \leq t _ {x, \mathrm {u b}} \\ 0, \text {e l s e} \end{array} \right. \tag {50}
$$

where $f _ { 3 }$ is the probability density function of $t _ { x }$ . $t _ { x , \mathrm { l b } }$ and $t _ { x , \mathrm { u b } }$ are the lower and upper bounds of $t _ { x } ,$ respectively. The values of $t _ { x , }$ lb and 


Table 2 Parameter setting for the upper and lower bounds of $t _ { x }$ in simulation.


<table><tr><td colspan="2">Vehicle type</td><td colspan="2">Parameter setting</td></tr><tr><td>Subject vehicle</td><td>Preceding vehicle</td><td>Lower bound</td><td>Upper bound</td></tr><tr><td>HDV</td><td>HDV, AV, CAV</td><td>tH, lb</td><td>tH, ub</td></tr><tr><td>AV</td><td>HDV, AV, CAV</td><td>tA, lb</td><td>tA, ub</td></tr><tr><td>CAV</td><td>HDV, AV</td><td>tA, lb</td><td>tA, ub</td></tr><tr><td>CAV</td><td>CAV</td><td>tC, lb</td><td>tC, ub</td></tr></table>

$t _ { x , }$ , ub exhibit variation based on vehicle type, as shown in Table 2. 

4.2.3.2. LCM. Ni (2016) introduced the LCM car-following model, designed to depict the behavior of HDVs following other vehicles. The LCM model posits that vehicle acceleration decisions are influenced by three primary factors: (1) the attraction stemming from traffic efficiency; (2) the impediment posed by the vehicle’s current speed; and (3) the hindrance created by the preceding vehicle. The mathematical expression of this model is as follows: 

$$
a _ {i} (t + \tau) = a _ {\max } \left(1 - \frac {\nu_ {i} (t)}{\nu_ {\mathrm {f}}} - \mathrm {e} ^ {1 - \frac {s _ {i} (t)}{s _ {i} ^ {* *} (t)}}\right) \tag {51}
$$

$$
s _ {i} ^ {* *} (t) = \gamma v _ {i} ^ {2} (t) + \tau v _ {i} (t) + L + S _ {0} \tag {52}
$$

where $\gamma$ is a composite parameter. τ denotes the reaction time of the driver. In the simulation, the values of $\tau$ are chosen from a predetermined range, as depicted in the subsequent equation: 

$$
f _ {6} (\tau) = \left\{ \begin{array}{c} \frac {1}{\tau_ {\mathrm {u b}} - \tau_ {\mathrm {l b}}}, \tau_ {\mathrm {l b}} \leq \tau \leq \tau_ {\mathrm {u b}} \\ 0, \text {e l s e} \end{array} \right. \tag {53}
$$

where $f _ { 6 }$ is the probability density function of τ. $\tau _ { \mathrm { l b } }$ and $\tau _ { \mathrm { u b } }$ are the lower and upper bounds of τ, respectively. 

4.2.3.3. Gipps model. Gipps (1981) presented a safety-distance model based on the driving safety principle. According to this principle, the driver of a vehicle must maintain a sufficient distance from the preceding vehicle at all times, ensuring that the former can safely come to a stop if the latter abruptly halts, thereby averting collisions. Additionally, Gipps model incorporates considerations of the free flow state of vehicles. The structure of the model is depicted below: 

$$
v _ {i} (t + \tau) = \min  \left\{ \begin{array}{c} v _ {i} (t) + 2. 5 a _ {\max } \tau \left(1 - \frac {v _ {i} (t)}{v _ {\mathrm {f}}}\right) \sqrt {0 . 0 2 5 + \frac {v _ {i} (t)}{v _ {\mathrm {f}}}} (\text {f r e e f l o w}) \\ a _ {\min } \tau + \sqrt {a _ {\min } ^ {2} \tau^ {2} + a _ {\min } \left[ v _ {i} (t) \tau + \frac {v _ {i - 1} ^ {2} (t)}{a _ {\min }} + 2 \left(L + S _ {0}\right) - 2 s _ {i} (t) \right]} (\text {f o l l o w i n g}) \end{array} \right. \tag {54}
$$

In the simulation, determine the acceleration of the vehicle at any given moment using the following equation: 

$$
a _ {i} (t) = \frac {\nu_ {i} (t + \tau) - \nu_ {i} (t)}{\tau} \tag {55}
$$

4.2.3.4. PATH ACC model. Research conducted by the California PATH Program has developed and validated a car-following model utilizing experimental data (Milan´es and Shladover, 2014). This model aptly reflects the dynamics of car-following observed in ve hicles equipped with ACC. Consequently, the model proves suitable for characterizing the car-following behavior of AVs and specific CAVs. The mathematical formulation of this model is outlined below: 

$$
a _ {i} (t) = k _ {1} \left(s _ {i} (t) - t _ {x} v _ {i} (t) - L - S _ {0}\right) - k _ {2} \left(v _ {i} (t) - v _ {i - 1} (t)\right) \tag {56}
$$

where $k _ { 1 }$ and $k _ { 2 }$ are the gains on positioning and speed errors respectively. 

4.2.3.5. PATH CACC model. When one CAV follows another, it is equipped with CACC. In this scenario, the car-following behavior of the CAV can be characterized using the PATH CACC model, which is formulated as follows (Milan´es and Shladover, 2014): 

$$
v _ {i} (t + \Delta t) = v _ {i} (t) + k _ {\mathrm {p}} e _ {i} (t) + k _ {\mathrm {d}} \dot {e} _ {i} (t) \tag {57}
$$

$$
e _ {i} (t) = s _ {i} (t) - L - S _ {0} - t _ {x} \nu_ {i} (t) \tag {58}
$$

where $e$ is the headway error of the subject vehicle. $k _ { \mathrm { p } }$ and $k _ { \mathrm { d } }$ are the gains attempted to adjust headway error with respect to the preceding vehicle. In the simulation, the formula for calculating the vehicle’s acceleration can be derived by simplifying Eqs. (57) and (58), as demonstrated below: 

$$
a _ {i} (t) = \frac {k _ {\mathrm {p}} \left(s _ {i} (t) - t _ {x} v _ {i} (t) - L - S _ {0}\right) - k _ {\mathrm {d}} \left(v _ {i} (t) - v _ {i - 1} (t)\right)}{\Delta t + k _ {\mathrm {d}} t _ {x}} \tag {59}
$$

# 4.2.4. Lane-changing behaviors

The modelling of lane-changing behaviors involves two main elements: lane-changing decision-making and lane-changing 

condition assessment. The section concerning lane-changing decision-making concentrates on identifying when vehicles opt to change lanes. Subsequently, after the decision to change lanes is made, a vehicle undergoes a lane-changing condition assessment to confirm that it meets the necessary criteria before proceeding with the maneuver. In simulation environments, a lane change is authorized solely when the vehicle adheres to the pre-established lane-changing conditions. Once these conditions are met, the vehicle promptly carries out the lane-changing action within the designated simulation time step. 

4.2.4.1. Lane-changing decision-making. In the on-ramp area, two distinct patterns of lane-changing behaviors can be observed. The first pattern involves vehicles merging from the ramp into the mainline traffic, while the second pattern entails vehicles changing lanes within the mainline itself. In the former case, vehicles from the ramp typically strive to seamlessly integrate into the flow of mainline traffic as they approach the merging boundary, thus reducing the need for lane-changing decision-making. Therefore, regulations concerning lane-changing decision-making are specifically designed to manage the latter type of behavior, where vehicles switch between the two mainline lanes. 

When vehicles travel along the mainline within the on-ramp area, their tendency to change lanes often arises from dissatisfaction with the low speed. This phenomenon, characterized by drivers’ dissatisfaction with speed, can be theoretically expounded upon using the model proposed by Chen and Wang (2019), as follows: 

$$
c _ {i} (t) = \left(\nu_ {\max } - \nu_ {i} (t)\right) / \nu_ {\max } \Delta t \tag {60}
$$

$$
C _ {i} (t) = \sum_ {k = 1} ^ {t} c _ {i} (k) \tag {61}
$$

where $C$ is the cumulative dissatisfaction of the driver. Rule 2 demonstrates the probability of vehicles selecting lane changes. Here, “i-$1 ^ { \prime \prime }$ refers to the preceding vehicle on the current lane, and ”k“ denotes the preceding vehicle on the target lane. $p$ is the probability of lane-changing selection. $C ^ { * }$ is the threshold value of accumulate dissatisfaction. $\nu ^ { * }$ represents the speed difference threshold for lanechanging. $L _ { 2 }$ signifies the position difference threshold for lane-changing. Specifically, when drivers’ cumulative dissatisfaction with their current lane exceeds $C ^ { * }$ , they opt to switch lanes if it allows their vehicle to attain a higher speed. This results in two scenarios for lane changes: (1) when the preceding vehicle on the target lane is moving faster than the one on the current lane, and (2) when there is significant distance between the preceding vehicle on the target lane and the current one. 


Rule 2: Probability of lane-changing selection for vehicles


<table><tr><td>if C_i(t) &gt; C*</td></tr><tr><td>if v_k(t) - v_{i-1}(t) ≤ 0</td></tr><tr><td>p = 0</td></tr><tr><td>elif 0 &lt; v_k(t) - v_{i-1}(t) &lt; v*</td></tr><tr><td>p = (v_k(t) - v_{i-1}(t)) / v*</td></tr><tr><td>else</td></tr><tr><td>p = 1</td></tr><tr><td>end</td></tr><tr><td>if x_k(t) - x_{i-1}(t) &gt; L_2</td></tr><tr><td>p = 1</td></tr><tr><td>end</td></tr><tr><td>end</td></tr><tr><td>return p</td></tr></table>

While the lane-changing decision-making model was initially developed through an analysis of HDV behaviors, its applicability extends to AVs and CAVs under certain conditions. In instances where AVs and CAVs operate without cooperative control systems, lanechanging preferences are primarily influenced by the operators’ preferences, allowing for the utilization of the same decision-making model. However, in the case of CAVs equipped with cooperative control systems, lane-changing decisions are dictated by the particular cooperative control strategy implemented. 

4.2.4.2. Lane-changing conditions. Vehicles prioritize safety considerations during lane changes, necessitating the specification of lanechanging conditions within the simulation framework. Should these conditions not be satisfied during simulation, vehicles abstain from executing lane changes. The present study outlines the mathematical model governing these lane-changing conditions as follows: 

$$
x _ {k} (t) - x _ {i} (t) \geq L + S _ {1} \tag {62}
$$

$$
x _ {i} (t) - x _ {k + 1} (t) \geq L + S _ {1} \tag {63}
$$

$$
T T C _ {k, i} (t) \geq T T C _ {2} ^ {*} \text {o r} T T C _ {k, i} (t) \leq 0 \tag {64}
$$

$$
T T C _ {i, k + 1} (t) \geq T T C _ {2} ^ {*} \text {o r} T T C _ {i, k + 1} (t) \leq 0 \tag {65}
$$

where $k$ and $k + 1$ denote the preceding and rear vehicles in the target lane, respectively. Furthermore, the simulation incorporates the 

following regulations about lane-changing: (1) After completing a lane change, vehicles are restricted from making consecutive lane changes within a 10-second interval. (2) Within ${ 2 0 } \mathrm { m }$ of the on-ramp entrance, vehicles are prohibited from changing lanes to avoid disrupting vehicles entering from the on-ramp. (3) As vehicles on the Outside Lane surpass the merging boundary, they adhere to the first-in-first-out principle, akin to ramp vehicles on the acceleration lane. Upon meeting lane-changing criteria, a ramp vehicle is permitted to merge into the mainline promptly. 

# 4.3. Model calibration

# 4.3.1. Data source

In this study, the exiD dataset is utilized as the source data for model calibration. The exiD dataset is a real-world trajectory dataset that captures highly interactive highway scenarios in Germany (Moers et al., 2022). It records continuous vehicle trajectories on highway on-ramps and off-ramps, spanning over 16 h of measurement data. Similar to the well-known highD dataset (Krajewski et al., 2018), the exiD dataset was recorded using drones equipped with cameras, ensuring no vehicle occlusion and minimal disruption to traffic flow, which contributes to the high accuracy of the data. 

The data collection area used in this study is depicted in Fig. 6 and includes both an on-ramp and an off-ramp section. The on-ramp area consists of two mainline lanes, one ramp lane, and an acceleration lane, which closely aligns with the schematic of the on-ramp area shown in Fig. 1. The dataset provides comprehensive trajectory information for all vehicles within the collection area, including their positions, headings, lateral and longitudinal speeds, and accelerations at each time step. Additionally, it contains lane-specific details such as lane ID, distance to the lane, and the IDs of surrounding vehicles. All subsequent model calibrations are based on this dataset. 

# 4.3.2. Verification of the distribution of vehicle arrival time intervals

In Section 4.2.1, we discussed studies suggesting that the pattern of vehicle arrivals on a specific segment of a continuous road follows a Poisson distribution (Rengaraju and Rao, 1995). As a result, the time intervals between vehicle arrivals can be modeled by a negative exponential distribution. Building on this, we implemented a vehicle entrance restriction to simulate traffic flow generation in the model. In this section, we will validate the vehicle arrival pattern in the simulation by comparing the results from the exiD dataset with those generated by the simulation. 

Fig. 7 presents the comparison results. We differentiate between the arrival time interval distributions for vehicles on the mainline and those on the ramp. The exiD data group results are derived from extracting vehicle trajectories from the exiD dataset, while the simulation results correspond to the arrival time intervals for vehicles entering the on-ramp area in the simulation. The fitted curve represents the ideal negative exponential distribution, as shown in Eq. (66), where the parameter λ corresponds to the average flow rate in the exiD dataset. 

$$
P (h = T) = \lambda \mathrm {e} ^ {- \lambda T} \tag {66}
$$

The results indicate that the vehicle arrival time intervals on the mainline closely follow a negative exponential distribution. However, the arrival time intervals for ramp vehicles show slight deviations from the ideal negative exponential distribution, although the overall trend remains consistent. This discrepancy arises because the negative exponential distribution assumes random arrivals, while ramp vehicles, which often pass through toll stations, may follow a different arrival pattern that is not entirely random. Nonetheless, the distribution of ramp vehicle arrivals still largely adheres to the characteristics of a negative exponential distribution. 

The negative exponential distribution is advantageous in simulations due to its simplicity and the fact that it involves only one parameter—flow rate (λ), whereas other distributions require more parameters. In traffic simulations, the vehicle generation process generally requires only the flow rate to be specified, making more complex distributions unsuitable for modeling ramp vehicles. Therefore, we continue to use the negative exponential distribution for simulating the arrival time intervals of ramp vehicles in the simulation. 

# 4.3.3. Parameter calibration for lane-changing decision-making model

In Section 4.2.4.1, we introduced a lane-changing decision-making model to simulate vehicle lane-change behavior. In this section, we calibrate the key parameter, $C ^ { * }$ , in the model using exiD dataset. 

During the data processing, we extracted all lane-change records of vehicles between the two mainline lanes in the on-ramp area, as shown in Fig. 6. This resulted in a total of 1,115 lane-change records. Next, we calculated the cumulative dissatisfaction of these vehicles prior to executing the lane change. The distribution characteristics of the cumulative dissatisfaction were then analyzed, as 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/3b3d140c7935f9ca3e4ed8ab12451014887e89359858edbd56f94fc20f14adf6.jpg)



Fig. 6. The data collection area for the exiD dataset used in this study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/d93c4002ca26e985ba4b6dd3c6e5eb4b3270c4c24452095bb64c15b2bde0f6e3.jpg)



(a) Mainline


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/ac599b5d3dd8e572c00b4bbe7f20672b26427511df74fa70e07bf452484f4b96.jpg)



(b)Ramp



Fig. 7. Comparison of the vehicle arrival time distribution between the exiD data and simulation results.


depicted by the scatter plot in Fig. 8. 

Based on the distribution of cumulative dissatisfaction, we observed a long-tail pattern before the lane change. Therefore, $C ^ { * }$ should not be set as a fixed value. Therefore, this study uses a probability distribution to determine the driver’s cumulative dissatisfaction threshold. After comparing different distribution forms, we selected the truncated normal distribution to best fit the data. In a truncated normal distribution, the probability density of a value $y$ can be determined by the following function: 

$$
f (y) = \frac {\frac {1}{\sigma} \phi \left(\frac {y - \mu}{\sigma}\right)}{\Phi \left(\frac {b - \mu}{\sigma}\right) - \Phi \left(\frac {a - \mu}{\sigma}\right)} \tag {67}
$$

where $( a , b )$ are the bounds, $\mu$ Is the mean value, and $\sigma$ is the standard deviation. After fitting the exiD data, we determined the following parameter values: $\pmb { a } = 0 . 4 4 s$ , $b = 8 . 3 4 s ,$ , $\mu = 0 . 4 3 s$ , $\sigma = 2 . 3 0 s$ . 

# 4.3.4. Parameter calibration for lane-changing conditions

In Section 4.2.4.2, we introduced the lane-changing conditions for vehicles. In this section, we calibrate the parameters $T T C _ { 2 } ^ { * }$ and $S _ { 1 }$ using the exiD dataset. To do this, we extracted all lane-changing records from the dataset, including those from both on-ramp and off-ramp areas, as shown in Fig. 6. A total of 4,149 lane-changing records were extracted and classified into two categories: lane changes occurring during on-ramp merging and all other lane changes. Specifically, 1,408 records correspond to on-ramp merging, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/8f2762f8c9ca052844809fc3930ed4be477539e536383770232f8387893f5398.jpg)



(a) Distribution frequency


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/c03144d2f5c77eb303f2438190bc1fb411a232fe74d010868b9724002d62e688.jpg)



(b)Cumulative frequency



Fig. 8. Distribution of cumulative dissatisfaction in the exiD dataset.


while 2,741 records represent other types of lane changes. 

After processing the data, we calculated the TTC and distance values for the subject vehicle relative to the preceding and rear vehicles in the target lane at the time of the lane change, as depicted in Fig. 9. In this figure, the x-axis represents the minimum threshold value, while the y-axis indicates the probability that data points fall below this threshold. 

Ideally, the minimum value of the data would be selected as the threshold. However, to account for potential data errors and the possibility that a small number of vehicles may exhibit unsafe lane-changing behaviors that are not representative of the general model, this study employs an inflection point analysis to determine the threshold. In economics, an inflection point is defined as the point where the marginal gain (or loss) from increasing variable X results in a significant change in variable Y, often accompanied by a sharp shift in the slope of the graph. For example, in Fig. 9(a), the line remains relatively flat when the TTC is below 3 s, but the slope becomes steeper once TTC exceeds 3 s. Therefore, we identified $T T C = 3$ s as the inflection point and set $T T C _ { 2 } ^ { * }$ to 3 s. Similarly, from Fig. 9(b), we determined that $5 \mathrm { m }$ is the value for $S _ { 1 }$ . 

For all lane-changing data, only $0 . 1 8 1 ~ \%$ of instances have a TTC below the $T T C _ { 2 } { ^ * }$ threshold of $3 \ : s _ { \mathrm { { \scriptsize ~ { \scriptsize ~ { \delta \pi } ~ } } } }$ , indicating that the threshold setting is reasonable. Similarly, only $0 . 1 9 3 \%$ of instances exhibit a distance below the $s _ { 1 }$ value of $5 \mathrm { m }$ . Lane changes during on-ramp merging tend to be more aggressive, with a higher proportion of instances showing very low TTC values and distances. However, even in these more aggressive cases, only $0 . 3 2 \%$ of instances have a TTC below the 3-second threshold, and only $0 . 4 6 2 \%$ have a distance below $5 \mathrm { m }$ . This suggests that the threshold settings are indeed appropriate. 

# 4.4. Evaluation indicators

In the simulation modelling framework utilized in this study, vehicle evaluation indicators have been systematically categorized into three primary groups: safety-related, efficiency-related, and comfort-related metrics. Some indicators are dynamically updated in real-time, based on the vehicles’ speed and position data, while others are calculated once vehicles have traversed the on-ramp area. These evaluation indicators are reliable instruments for assessing the effectiveness of control strategies. 

# 4.4.1. Safety-related indicators

4.4.1.1. Time exposed TTC (TET). The TET concept is derived from the TTC (Minderhoud and Bovy, 2001). TET quantifies the period during which a vehicle remains in an unsafe condition. Its expression is as follows: 

$$
T E T _ {i - 1, i} (t) = \delta (t) \times \Delta t, \delta (t) = \left\{ \begin{array}{l l} 1, & \text {i f} 0 <   T T C _ {i - 1, i} (t) <   T T C ^ {*} \\ & 0, \text {e l s e} \end{array} \right. \tag {68}
$$

The TET metric is employed for assessing the longitudinal safety performance of a vehicle when navigating on the road following its preceding vehicle within the same lane. During simulation, the cumulative TET value for each vehicle traversing the on-ramp area is derived by monitoring TET values across the entire process, as demonstrated by the subsequent equation: 

$$
T E T _ {i} = \sum_ {t = 1} ^ {\text {T i m e}} T E T _ {i - 1, i} (t) \tag {69}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/e79479627f44a7f2c30ff98f075c214e27f54cb800f44cb624fa530c1c452947.jpg)



(a) TTC


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/52bc9b36bdd19f7139a339f4215ffd4a11a05b8f835bc171292f49336e2bbbd8.jpg)



(b) Distance



Fig. 9. The TTC and distance values for the subject vehicle relative to the adjacent vehicles in the target lane at the time of the lane change, based on the exiD dataset.


where Time means the total duration that the subject vehicle spends within the on-ramp area. At the conclusion of each simulation round, the mean TET for all vehicles exiting the on-ramp area is computed, as depicted in the equation below: 

$$
\overline {{T E T}} = \frac {1}{N _ {\mathrm {E}}} \sum_ {i = 1} ^ {N _ {\mathrm {E}}} T E T _ {i} \tag {70}
$$

where $N _ { \mathrm { E } }$ is the number of vehicles to exit the on-ramp area. 

4.4.1.2. TET of merging process (TETMP). The TETMP, originating from the TET concept, functions as an evaluation metric utilized to gauge the safety of the merging procedure (Yang et al., 2023b). Considering the numerous conflicts inherent in the merging process, TETMP emerges as a critical indicator within the on-ramp area. More precisely, it quantifies the collision risk endured by a ramp vehicle until the merging conditions are satisfied. This risk encompasses factors originating from both virtual preceding and rear vehicles on the Outside Lane of the mainline. For a merging vehicle “i” on the acceleration lane, with its corresponding virtual preceding and rear vehicles on the mainline Outside Lane labeled as “k” and $\ddot { \kappa } + 1 { \mathit { \Omega } } ^ { \prime \prime }$ respectively, the TETMP value can be calculated using the following equation: 

$$
T E T M P _ {i} = \sum_ {t = 1} ^ {\text {T i m e}} \max  \left(T E T _ {k, i} (t), T E T _ {i, k + 1} (t)\right) \tag {71}
$$

$$
\overline {{T E T M P}} = \frac {1}{N _ {\mathrm {R E}}} \sum_ {i = 1} ^ {N _ {\mathrm {R E}}} T E T M P _ {i} \tag {72}
$$

where $N _ { \mathrm { R E } }$ is the number of ramp vehicles to exit the on-ramp area. 

4.4.1.3. Conflict-potential mergence ratio (CPMR). Ramp vehicles typically aim to smoothly integrate into the flow of mainline traffic upon reaching the merging boundary, ideally achieving a seamless transition. However, this ideal scenario is not always attainable. In this study, when a ramp vehicle is able to merge directly into the mainline upon crossing the merging boundary, it is categorized as a conflict-free mergence. Otherwise, it is classified as a conflict-potential mergence. The CPMR quantifies the proportion of vehicles involved in conflict-potential mergences relative to all vehicles exiting the on-ramp area. This metric offers insights into the severity of merging conflicts within the on-ramp area. 

# 4.4.2. Efficiency-related indicator

Delay stands out as the predominant evaluation indicator concerning efficiency. It quantifies the variance between the actual and optimal travel durations for vehicles. The following equation is employed to ascertain the average delay experienced by vehicles upon exiting the on-ramp area in each simulation round: 

$$
\bar {d} = \frac {1}{N _ {\mathrm {E}}} \sum_ {i = 1} ^ {N _ {\mathrm {E}}} \left(\frac {L _ {0} + L _ {1}}{v _ {\max }} - \left(T _ {i} ^ {\prime \prime} - T _ {i} ^ {\prime}\right)\right) \tag {73}
$$

where T“ is the time of the subject vehicle to exit the on-ramp area. $L _ { 1 }$ is the length of the acceleration lane. 

# 4.4.3. Comfort-related indicator

Passenger discomfort experienced during vehicle rides often correlates with the occurrence of frequent and excessive deceleration. Within the realm of international standard, specifically addressed in the “Mechanical Vibration and Shock” section, human comfort concerning acceleration is systematically classified into five distinct levels, as outlined in Table 3 (ISO 2631–1, 1997). Utilizing this standard, the cumulative discomfort endured by passengers in a simulation round can be quantified employing the following formula. 

$$
C D _ {i} = \sum_ {t = 1} ^ {\text {T i m e}} \left(D _ {i} (t) \times \Delta t\right) \tag {74}
$$


Table 3 Comfort assessment level according to ISO 2631–1(1997).


<table><tr><td>Absolute value of acceleration</td><td>Comfort level</td></tr><tr><td>&lt; 0.315 m/s2</td><td>Not uncomfortable</td></tr><tr><td>0.315 ~ 0.63 m/s2</td><td>A little uncomfortable</td></tr><tr><td>0.5 ~ 1 m/s2</td><td>Fairly uncomfortable</td></tr><tr><td>0.8 ~ 1.6 m/s2</td><td>Uncomfortable</td></tr><tr><td>1.25 ~ 2.5 m/s2</td><td>Very uncomfortable</td></tr><tr><td>&gt; 2 m/s2</td><td>Extremely uncomfortable</td></tr></table>

$$
D _ {i} (t) = \left\{ \begin{array}{c} 0. 1, \text {i f} - 1. 2 5 \mathrm {m} / \mathrm {s} ^ {2} <   a _ {i} (t) \leq - 0. 8 \mathrm {m} / \mathrm {s} ^ {2} \\ 0. 2, \text {i f} - 1. 6 \mathrm {m} / \mathrm {s} ^ {2} <   a _ {i} (t) \leq - 1. 2 5 \mathrm {m} / \mathrm {s} ^ {2} \\ 0. 4, \text {i f} - 2 \mathrm {m} / \mathrm {s} ^ {2} <   a _ {i} (t) \leq - 1. 6 \mathrm {m} / \mathrm {s} ^ {2} \\ 0. 8, \text {i f} - 2. 5 \mathrm {m} / \mathrm {s} ^ {2} <   a _ {i} (t) \leq - 2 \mathrm {m} / \mathrm {s} ^ {2} \\ 1. 6, \text {i f} a _ {i} (t) \leq - 2. 5 \mathrm {m} / \mathrm {s} ^ {2} \\ 0, \text {e l s e} \end{array} \right. \tag {75}
$$

where $D$ represent the discomfort endured by passengers of the subject vehicle. CD is the cumulative discomfort of the subject vehicle in a simulation round. Given that passenger discomfort primarily arises from instances of significant deceleration, the quantification process primarily focuses on assessing values corresponding to such occurrences, rather than accumulating data pertaining to minor deceleration and acceleration events. After each simulation round, the average CD for all vehicles leaving the on-ramp area is calculated using the following equation: 

$$
\overline {{C D}} = \frac {1}{N _ {\mathrm {E}}} \sum_ {i = 1} ^ {N _ {\mathrm {E}}} C D _ {i} \tag {76}
$$

# 5. Simulation results

# 5.1. Simulation objectives and settings

After introducing the simulation modelling framework and cooperative control strategy for CAVs, this section will present the simulation results conducted within the proposed modelling framework. The simulation in this study aims to achieve two primary objectives: firstly, to examine the performance advantages of AVs and CAVs over HDVs in transportation systems without cooperative control. The simulation results pertaining to this objective are detailed in Section 5.2. Within this section, vehicles adhere to designated car-following and lane-changing models in the simulation, operating without any intervention from a central control center or vehicle detectors. 

The second objective is to assess the extent to which the proposed cooperative control strategy enhances traffic conditions across various traffic environments and CAV penetration rates. This analysis, as elaborated in Sections 5.3-5.7, involves comparing the performance metrics derived from simulations with and without cooperative control implementation. 

All parameter values utilized in the simulation are outlined in Table 4. Additionally, it is important to note that the maximum speed of vehicles on the ramp is set to $6 0 ~ \%$ of the mainline speed limit $( \nu _ { \mathrm { m a x } } )$ . The numerical simulations are executed within a Python environment, using a computer equipped with an “Intel(R) Core(TM) i5-10400F CPU $\ @ \ : 2 . 9 0 \ : \mathrm { G H z ^ { \prime \prime } }$ . Throughout a single simulation round employing a step size of 0.1 s and spanning $_ { 0 . 5 \mathrm { ~ h ~ } }$ , the average simulation time is approximately 15 s under uncongested conditions and around 39 s under congested scenarios, demonstrating a notably efficient simulation process. 

# 5.2. The performance advantages of AVs and CAVs over HDVs

This section presents four sets of simulations designed to analyze the performance advantages of AVs and CAVs in comparison to HDVs. These simulations utilize the mathematical modelling framework introduced earlier. The purpose of the four simulation sets is to compare the traffic conditions in different scenarios by considering various vehicle types and varying total flow rates. 

In Set 1, the traffic flow consists of AVs and HDVs, with a total flow rate of 3500 veh/h. Inside Lane and Outside Lane each have a flow rate of 1500 veh/h, and the ramp has a flow rate of 500 veh/h. This scenario aims to simulate traffic congestion. Set 2 also includes AVs and HDVs, but with a lower total flow rate of 2500 veh/h. Inside Lane and Outside Lane each have a flow rate of 1000 


Table 4 Parameter values in the simulation.


<table><tr><td>Parameter</td><td>Value</td><td>Unit</td><td>Parameter</td><td>Value</td><td>Unit</td></tr><tr><td>Δt</td><td>0.1</td><td>s</td><td>L0</td><td>200</td><td>m</td></tr><tr><td>tH, lb</td><td>1.2</td><td>s</td><td>L1</td><td>200</td><td>m</td></tr><tr><td>tH, ub</td><td>2.0</td><td>s</td><td>L2</td><td>40</td><td>m</td></tr><tr><td>tA, lb</td><td>0.9</td><td>s</td><td>a max</td><td>3</td><td>m/s2</td></tr><tr><td>tA, ub</td><td>1.3</td><td>s</td><td>a min</td><td>-3</td><td>m/s2</td></tr><tr><td>tC, lb</td><td>0.5</td><td>s</td><td>a emer</td><td>-8</td><td>m/s2</td></tr><tr><td>tC, ub</td><td>0.7</td><td>s</td><td>kp</td><td>0.45</td><td>s-1</td></tr><tr><td>νf</td><td>30</td><td>m/s</td><td>kd</td><td>0.25</td><td>-</td></tr><tr><td>νmax</td><td>25</td><td>m/s</td><td>k1</td><td>0.23</td><td>s-1</td></tr><tr><td>γ</td><td>-0.02</td><td>s2/m</td><td>k2</td><td>0.07</td><td>s-2</td></tr><tr><td>τlb</td><td>0.8</td><td>s</td><td>γ*</td><td>3</td><td>m/s</td></tr><tr><td>τub</td><td>1.4</td><td>s</td><td>TTC*</td><td>2</td><td>s</td></tr><tr><td>L</td><td>5</td><td>m</td><td>TTC1*</td><td>1</td><td>s</td></tr><tr><td>S0</td><td>2</td><td>m</td><td>α</td><td>0.7</td><td>-</td></tr><tr><td>S1</td><td>5</td><td>m</td><td>β</td><td>0.3</td><td>-</td></tr><tr><td>ku</td><td>1.15</td><td>-</td><td></td><td></td><td></td></tr></table>

veh/h, and the ramp has a flow rate of 500 veh/h. The flow rate settings for Set 3 and Set 4 are identical to those of Set 1 and Set 2, respectively, but their traffic flow is composed of CAVs and HDVs. 

For each of the four sets, 10 subset simulations were conducted based on the penetration rate of AVs or CAVs, spanning from 0.1 to 1. Each subset underwent 100 simulation rounds. Each round lasted for 1800 s, with a simulation step size of 0.1 s. At the end of the simulation, the average values of all evaluation indicators across all sets were output, as depicted in Fig. 10. The color depth of each square in the figure signifies the normalized ratio value of each indicator, ranging from 0 to 1. The numbers superscripted on each square indicate the actual average value of each indicator. 

Firstly, by analyzing the simulation results from each set, it becomes apparent that the integration of AVs or CAVs significantly improves traffic conditions on on-ramp systems. For instance, within Set 1, a comparison of evaluation indicators between AV penetration rates of 0.1 and 1 demonstrates several noteworthy improvements. At a penetration rate of 1, compared to 0.1, the reduction in TET exceeds $9 5 \%$ , indicating a significant enhancement in longitudinal vehicle safety. Moreover, both TETMP and CPMR values exhibit marked decreases, indicating improved merging safety for ramp vehicles. CD value shows a reduction exceeding $6 0 \%$ , highlighting an increase in ride comfort. Furthermore, the reduction in delay exceeds $9 8 ~ \%$ , signifying an enhancement in vehicle traffic efficiency. 

By analyzing simulation outcomes across varied flow rates, it becomes evident that flow rates exert a discernible influence on the on-ramp system. For instance, within Set 1, when the penetration rate of AVs stands at 0.1, vehicles experience a mean delay of 217 s. Conversely, in Set 2, this delay reduces significantly to 16.1 s. This stark contrast highlights the presence of severe congestion in Set 1, where traffic inflow exceeds the on-ramp system’s capacity. Comparing assorted evaluation metrics between the two result sets reveals that the enhancements in traffic efficiency coincide with improved driving safety and passenger comfort. Moreover, it’s important to note that irrespective of congestion scenarios (Set 1 and 3) or uncongested scenarios (Set 2 and 4), both AVs and CAVs contribute positively to ameliorating on-ramp system traffic conditions. 

Finally, upon comparing the outcomes between AV-HDV and CAV-HDV heterogeneous traffic flows, it becomes evident that CAVs offer advantages in enhancing traffic conditions over AVs, particularly at higher penetration rates. For instance, in Set 1, when AVs comprise $9 0 ~ \%$ of the traffic, vehicles experience an average delay of 8.28 s and a TET of 0.47 s. Conversely, in Set 3, when CAVs constitute $9 0 \%$ of the traffic, vehicle delay reduces significantly to only 1.87 s, accompanied by a minimal TET of 0.11 s. Notably, these 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/04e090d2e4ff9f2573d2cd92d33aa23ec7a768d83081f743537ce6e5d462df6a.jpg)



(a) Set 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/0389977a0d377e581d9089051ee7d08ee46a74631d02b6f946cd18c1cc710ec3.jpg)



(b)Set 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/36aaa5e591898cfb09f9e73c24082d48cfefc81e2a0d4e02dd6dd77f06e9bdbc.jpg)



(c) Set3


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/d86582cf82ed6467f9f8f77ad45411009da3ad4ceaa99f4ed30ca509cd41bd71.jpg)



(d)Set 4



Fig. 10. The values and ratios of all evaluation indicators across various sets.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/247bea66a8d9619dd11ccfa3e1c3ef9e1d12cbcfc120f5e3120d7761c41793fb.jpg)



(a)TET


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/8b16848e3f27a2f3c501cd129c7225d9bd9193e7ef11e817dda253d5897d22c0.jpg)



(b)TETMP


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/f59a1295a9ac3e1a4a1e1fab0f5a238e8bb2acc8e26dda3e17b5242d7b1d14bd.jpg)



(c) CPMR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/1fa83fb162e957b5b412e5011dbca95b8e2299fb4ac49a9d5433047073a81dc3.jpg)



(d) Delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/06d5e072852b7bf4395bf1b49047b94d517e077908740eedce019d164acd8efe.jpg)



(e)CD



Fig. 11. The average values of diverse evaluation indicators at a total flow rate of 3500 vehicles per hour.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/ff54f1452eb3c341a4b8b1a7309efb9035bb864859083d360205327ae7ec7ac0.jpg)



(a)TET


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/e2972eb06a852238ebdba03586d2dd0900d57e0f9545accc8258395d866c5b5e.jpg)



(b)TETMP


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/80c310c85ffff48aa8d50cf1517a84592fe454c975e72c28190b20163bd4d911.jpg)



(c) CPMR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/ae06c7ee8c8a34b7c598fe2ecdd32564ace1b3dcea2a78562d8e82b731ee0672.jpg)



(d) Delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/4b929ca868796b8cced4b10f909b5e93042cf7b098afb7537ad6a515e0613361.jpg)



(e)CD



Fig. 12. The average values of diverse evaluation indicators at a total flow rate of 2500 vehicles per hour.


metrics represent less than $2 5 ~ \%$ of the corresponding values observed in the AV-dominated scenario. 

# 5.3. The effectiveness of cooperative control strategy

# 5.3.1. The typical simulation results

In this section, to assess the impact of cooperative control strategy for CAVs on the traffic conditions of the on-ramp system, the simulations are divided into two distinct groups: the cooperative control group and the non-cooperative control group. In the cooperative control group, the CAVs located in the on-ramp area are equipped with the cooperative control strategy as described in Section 3. On the other hand, the car-following and lane-changing behavior of CAVs in the non-cooperative control group is governed by the conventional model within the simulation framework. 

For each group, a comprehensive set of 10 subset simulations was executed, wherein the penetration rate of CAVs was system atically adjusted from 0.1 to 1. The proportion setting of vehicle types within the simulation framework is outlined below: 

$$
p _ {\mathrm {A V}} = \left(1 - p _ {\mathrm {C A V}}\right) \cdot p _ {\mathrm {C A V}} \tag {77}
$$

$$
p _ {\mathrm {H D V}} = 1 - p _ {\mathrm {A V}} - p _ {\mathrm {C A V}} \tag {78}
$$

where pHDV, pAV, and $p _ { \mathrm { { C A V } } }$ are the proportion of HDVs, AVs and CAVs, respectively. 

Each subset underwent 100 simulation rounds. Within each round, identical approaching vehicle data was inputted across both experimental groups, ensuring fairness in result assessment. Each simulation round had a duration of 1800 s, with a simulation step size set at 0.1 s. Figs. 11 and 12 depict the values of each evaluation indicator within the simulation results, alongside the decline rate observed during cooperative control. Fig. 11 corresponds to simulations conducted with a total flow rate of 3500 vehicles per hour, while Fig. 12 illustrates results obtained with a total flow rate of 2500 vehicles per hour. The flow rate settings for each lane align precisely with those outlined in Section 5.2. 

The figures illustrate a clear impact of the cooperative control strategy on enhancing the traffic conditions within the on-ramp system. Specifically, regarding the longitudinal safety of vehicles, depicted in Fig. 11 (a) and 12 (a), it is evident that at lower penetration rates of CAVs, the average TET value is notably high. Notably, irrespective of the penetration rate, the cooperative control group consistently exhibits lower average TET values compared to the non-cooperative control group. Furthermore, within the penetration rate range of 0.4 to 0.5, the TET value remains high, indicating relatively unsafe traffic conditions. However, the implementation of the cooperative control strategy yields a reduction in TET ranging from $3 0 \%$ to $6 0 \%$ . Moreover, at penetration rates surpassing 0.7, the cooperative control strategy achieves a decline rate in TET exceeding $8 0 \%$ , thereby significantly enhancing the safety performance of traffic conditions. 

In terms of safety during the merging process for ramp vehicles, the data presented in Fig. 11 (b)&(c) and 12 (b)&(c) demonstrate that at high levels of CAV integration, ramp vehicles operating without cooperative control mechanisms still encounter significant merging risks. For instance, when the CAV penetration rate is 0.8 and the flow rates are 3500 and 2500 vehicles per hour, the CPMR for the non-cooperative control group stands at 0.61 and 0.44, respectively. Conversely, in the cooperative control group, these 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/db9ea054babdcb59365236cb09b33879ce2152c695b1484cdc1a60caca471d16.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/9a7d1a7cc0fe17a2610344c7f0a50d190feea7ac28801009734384085c7090e1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/141007ab94de8d356951f5a4eede48daf4acddf5ac00b92a9636ed3325f5a788.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/4a03fa57799a0ac2e0cdf01415d1a598acde7fdf890d6af97181f54e0d9148b3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/a1b1577b1db312f89f7765ca1a1c673080c037df4169de7d4341f795ef43d2e1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/d682bfaa9b4a4425f4c968f660dd22ec16b352bd66ea0a01d1fb27459691c757.jpg)



Fig. 13. The average values of diverse evaluation indicators across different vehicle types, with a total flow rate of 3500 vehicles per hour.


corresponding indicator values decrease to 0.15 and 0.09, respectively. This underscores the substantial risk reduction achieved through the implementation of cooperative control strategies. In scenarios featuring exclusively CAV traffic, the risk associated with vehicle merging can be virtually eliminated through the use of cooperative control strategies. 

When considering traffic efficiency, Fig. 11 (d) and 12 (d) demonstrate that the flow rate and penetration rate of CAVs have a significant impact on vehicle traffic. Fig. 11 (d) shows that with a CAV penetration rate of 0.3–0.6, the cooperative control strategy reduces delays by $1 5 \% { - } 5 0 \%$ , indicating its effectiveness in improving traffic efficiency during mild congestion. However, when traffic is not congested, vehicle travel delays are already minimal, limiting the potential improvement of cooperative control strategies. 

In terms of ride comfort, Fig. 11 (e) and 12 (e) illustrate that the cooperative control strategy also reduces the average value of CD. As the penetration rate increases, the cooperative control strategy can achieve a maximum decrease in CD of approximately $5 0 \%$ . This substantial reduction clearly indicates a significant enhancement in ride comfort. 

# 5.3.2. Comparison of indicators for different vehicle types

This section examines the influence of cooperative control strategies on various vehicle types. To achieve this, the simulation outcomes presented in Section 5.3.1 are segregated based on vehicle types, as illustrated in Figs. 13 and 14. These figures depict the evaluation indicator values of different vehicle types under cooperative control (solid lines), along with the rate of decline in their indicator values (dashed lines). 

It is evident that while the proposed cooperative control strategy only governs the behaviors of CAVs, there is a noticeable descent in the evaluation indicator values of AVs and HDVs. This descent is apparent as the majority of decline rate values in the figures are greater than zero. This implies that the enhancement of traffic conditions facilitated by CAVs extends system-wide, transcending the confines of CAVs alone. 

Moreover, scrutiny of Fig. 13 (b), (c), and 14 (b), (c) reveals that, under the cooperative control strategy, the safety enhancement of CAVs is particularly pronounced. This underscores the superiority of CAVs over other vehicle types, within the context of connected and automated technologies. 

# 5.3.3. Control effect analysis

The cooperative control strategy outlined in this research encompasses two primary components: merging control and lanechanging control. In order to evaluate the distinct effects of these components on the transportation system, two supplementary simulation groups have been established: the only merging control group and the only lane-changing control group. Each of these groups exclusively employs either merging control or lane-changing control, while conventional models within the simulation framework are used for other behaviors of CAVs. 

Consistent with previous description, the simulations also varied the penetration rate of CAVs and considered different flow rates. The reported results represent the average of 100 simulation rounds, as depicted in Figs. 15 and 16. 

Analysis of the simulation results indicates that both components contribute to an improvement in overall traffic conditions to some extent. Optimal traffic conditions are observed when both components are employed simultaneously. Furthermore, while the lanechanging control demonstrates effectiveness, Fig. 15 (b), (c), and 16 (b), (c) illustrate that the primary enhancement in vehicle 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/74cb8996c1778140ce4579e9f9dd5eec9de5501f2a3beb586129ba8e67fe7eb3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/af6c15e37c41129a3bfc810fced3429e674a9a657d1ed18d6fe31f1f9c07e84c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/c8befc7be09aa9a2bd3d6261d1526e587a2094eec26dbef3c7d6a56dafc0e8af.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/bc31fe050d4fb0dd2fb17cf98f7d25cbd94be00688dfac47c260f680fa81ab5e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/b95ce967baf9711f81e148974509e425dcfcd24e45d516d93f3f4b545f9adca0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/06f9a82a5cb54771d858348fb2093394a2423626a70d88e30ab17cfb9cec5867.jpg)



Fig. 14. The average values of diverse evaluation indicators across different vehicle types, with a total flow rate of 2500 vehicles per hour.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/e1f8351aaa1915cdac4c0cee33638ecc1a1b0f5b99f18efcb04dc28280280106.jpg)



(a)TET


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/9197fae97fdc40cc9ad6696d6e3cf65d98a2b53dad285b040c64f950b1c5c394.jpg)



(b) TETMP


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/7dd142a55d9e5eddfcd464bdebe690f19b9a3b1daca69022b1c27aa127cd755c.jpg)



(c) CPMR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/a5d5e3ad747178b923e124665580a18f0e0d45aa9002edab13aa708246a56ce5.jpg)



(d) Delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/87f1d86f038e8c83116146339fca092de0c0f71a8deeee18e8c0c92d47de9c04.jpg)



(e)CD



Fig. 15. The average values of diverse evaluation indicators across different control modes, with a total flow rate of 3500 vehicles per hour.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/a02fd479ff9c1ebd96f153466c3ab513a16d36bdf89aa17c8c213cfa99d4d707.jpg)



(a)TET


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/ebab55b210fcb24c201154d943484e5f621a1fa424a64621cf32687bda124a15.jpg)



(b) TETMP


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/b15ca8c00cbf8907ccbdc2acc545745a286d058360f74a92557ba23b94b28b16.jpg)



(c) CPMR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/1f43c03797d1e8bb98401a67a0db0b840ff334ed3eeffb35651a9b13140e5681.jpg)



(d) Delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/d8fef370e394c863094c1f3b6a024f1c7b6bfe176648026d84dd0bc66ed3f48b.jpg)



(e) CD



Fig. 16. The average values of diverse evaluation indicators across different control modes, with a total flow rate of 2500 vehicles per hour.


merging safety originates from the merging control component. Additionally, the reduction in vehicle delay under mild congestion conditions is attributed to the implementation of lane-changing control, as indicated in Fig. 15 (d). 

# 5.3.4. Sensitivity analysis of flow rate

Flow rate serves as a crucial parameter influencing traffic conditions within the on-ramp area and can impact the effectiveness of control strategies. Previous sections have substantiated this with results presented at total flow rates of 3500 veh/h and 2500 veh/h. This section will conduct a sensitivity analysis specifically on flow rate parameter to explore it effects on safety, efficiency, and ride comfort in the on-ramp area. 

To achieve this objective, simulation experiments were conducted across a total flow rate range of 2500–3500 veh/h. Within this range, the ramp flow rate was fixed at 500 veh/h, while each lane on the mainline ranged between 1000–1500 veh/h. Fig. 17 depicts the average outcomes from 100 simulation rounds, detailing various evaluation indicators under cooperative control and their relative decline rates compared to non-cooperative scenarios. 

Figs. 17 (a) to (d) illustrate the substantial impact of flow rate on traffic conditions within the on-ramp system, where increased flow rate correlates with decreased safety, efficiency, and ride comfort. Analysis of decline rates in evaluation metrics, as shown in Fig. 17 (e) to (h), indicates that most areas exhibit positive trends. Notably, except for delay, other indicators generally show increasing decline rates with higher penetration rates, with delay reduction particularly pronounced under congested traffic conditions. These findings underscore the effectiveness of cooperative control strategies for connected and automated vehicles across all flow rates. 

In addition to adjusting the total flow rate, it is crucial to investigate how the distribution of flow rates across each lane affects traffic conditions in the on-ramp area. To address this, we conducted a sensitivity analysis on the flow rate ratios. Keeping the total flow rate constant at 3000 vehicles per hour, we varied the flow rate ratio from the mainline to the ramp between 2:1 and 12:1. The results for each evaluation indicator under cooperative control are illustrated in Fig. 18. 

The analysis reveals a correlation between the evaluation indicators and the flow rate ratio. Higher ramp flow rates correspond to reduced safety, efficiency, and ride comfort within the on-ramp system. However, the relationship between the flow rate ratio and these metrics appears to be weak. These indicators are primarily influenced by CAV penetration rate and the total flow rate. 

# 5.3.5. Analysis of simulation results at the microscopic level

To comprehensively examine the behaviors of vehicles under varying control modes at a microscopic level, this study extracted a segment of vehicle trajectories from simulations conducted with a CAV penetration rate of 0.5, and a flow rate of 3500 veh/h, as depicted in Figs. 19 and 20. Within these figures, alterations in line color or the presence/absence of lines signify lane changes. For instance, the transition from the blue line to the red line in the figures indicates successful merging of vehicles from the ramp onto the Outside Lane. 

A comparison of the findings in Figs. 19 and 20 reveals notable differences. In the cooperative control group, a majority of ramp vehicles seamlessly merge into the mainline immediately upon crossing the merging boundary, thereby mitigating merging conflicts. Conversely, in the non-cooperative control group, many vehicles only manage to merge into the mainline midway through the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/df2c2e1a33ec8e512d25cac0f1c011826b3ecd6618d7100985d92dddbc17c8cb.jpg)



(a) TET value


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/41600378fcd710c1fc853c660532e55426c5a8d1952ba6a2b8d259ea27d43b43.jpg)



(b) CPMR value


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/cd79d560651a6c10ee516f716ebacdcbd89a5c8ed0f737e40d941608e215fc0e.jpg)



(c) Delay value


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/32bf9dfde447c3765e5e2d0caeb2ed8a1b6b3a286bff3b344da08b84950a5b8c.jpg)



(d) CD value


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/be86ed83f4ca19a24055e859076bdde27f31a110fd640896d8b0328fd409092b.jpg)



(e) TET decline rate


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/a1120bac7c3bf8a471c8b74af2e36b48a6913b9207596bf3beaac7baa1e3bdb9.jpg)



(f) CPMR decline rate


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/418932fe05f9fc6a8dac144a1e40d0991586769315a2323043d99a8e2f275ba5.jpg)



(g) Delay decline rate


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/2b9ed622162b223d1272965f13876014b62e436878c9a29ea006ec09a08d71b4.jpg)



(h) CD decline rate



Fig. 17. The average values of various evaluation indicators under cooperative control at varying total flow rates, alongside their relative decline rates compared to non-cooperative scenarios.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/54c6361adb8187876c90836776bc6eb5faec43dc58b242b3f3b7dd86799f190d.jpg)



(a) TET value


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/d60c2aa749577dfb36b8d0aecfc82c8f2cd2a927c1b0a801bef750c03fbcb1c3.jpg)



(b) CPMR value


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/53481b8b1c1548098bf78b418b8ce2db8cd10cf6433a77dcc338403f2212bf17.jpg)



(c) Delay value


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/7c55c6307790e5054bce7575b98660bd2e0bea286e035343c275056ad96eb00b.jpg)



(d) CD value



Fig. 18. The average values of various evaluation indicators under cooperative control at varying flow rate ratios.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/a266c2c31125f63ee3ae9d4884a439fb925cc830d1c2df7a48e9e717eb100709.jpg)



(a) Outside Lane and ramp vehicles


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/9cf9c4c42295aa4938d039e64baa9c560cd1b29e5d7b107620bfb28e6e95688d.jpg)



(b) Inside Lane vehicles



Fig. 19. The trajectories of vehicles within the cooperative control group.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/bfaf7d50d04a766b4c094e31dfce6461675b8e073e33eb0092fdf0bbdd3ef2aa.jpg)



(a) Outside Lane and ramp vehicles


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/6a172727acbd11c34f1e1b8fa5e7af63d6da88c8f1b6f413defea90ab7ffaf06.jpg)



(b) Inside Lane vehicles



Fig. 20. The trajectories of vehicles within the non-cooperative control group.


acceleration lane. This observation is further supported by the frequency density distribution of merging positions illustrated in Fig. 21. 

This discrepancy can be attributed to two main factors. Firstly, prior to reaching the merging boundary, cooperative control mechanisms for CAVs on the Outside Lane and ramp work to minimize the number of unreliable VBs, allowing for the orderly formation of vehicle platoons on these lanes before merging. Secondly, through the utilization of lane-changing control features, some CAVs on the Outside Lane execute early lane changes to the Inside Lane. This strategic approach significantly reduces the risk of merging-related incidents, thereby preempting the need for emergency braking triggered by merging conflicts. Consequently, both vehicle longitudinal safety and passenger comfort are enhanced as a result of these measures. 

# 5.4. Discussion on capacity drop

Bottlenecks on highways typically occur at on-ramp merging areas, work zones, and accident sites. These bottlenecks are triggered when traffic demand exceeds highway capacity. The concept of “capacity drop” refers to the phenomenon where, once congestion forms upstream of a bottleneck, the maximum flow rate downstream is significantly lower than the nominal capacity of the bottleneck (Chen and Ahn, 2018; Leclercq et al., 2011). Specifically, Wang et al. (2023) provide a detailed simulation method of merging areas at highway on-ramps and the modeling techniques used to capture the capacity drop effect. This study builds upon the approach pre sented by Wang et al. (2023) to replicate the capacity drop phenomenon within the proposed simulation framework, while also exploring the impact of the proposed cooperative control strategies on this effect. 

As shown in Fig. 22, similar to the micro-simulation framework introduced by Wang et al. (2023), this study also includes four flow 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/1f4a59e244c181b00b48aead72784718ca513b05b350729bc42640075c47f207.jpg)



Fig. 21. The distribution of merging positions for vehicles at a CAV penetration rate of 0.5 and a flow rate of 3500 veh/h. (The density curve has been smoothed using the kernel smoothing method.).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/6543c4fc2cd6f200d030fc44d8e9e2fa34564685f5be6f3c90507e4789a34f87.jpg)



Fig. 22. Locations of the flow rate observation points.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/0241205d8249becde23bafc5caec7dc864606e842558925eb3bd5652422f6770.jpg)



(a) Group A


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/d3f7fbe0db814b8978e2daf3e75eef93069ae1147e7d82e24ba3988382ff096a.jpg)



(b) Group B



Fig. 23. Traffic flow generation in the simulation scenarios within a pure HDV environment.


rate observation points along the highway mainline: Points 1, 2, 3, and 4. In the simulation, the number of vehicles passing each observation point is recorded every minute, and the values are then scaled by a factor of 60 to represent the hourly flow rate for each observation point. 

Firstly, we measured the nominal capacity of the two-lane mainline in a pure HDV environment, which was found to be approximately 3056 veh/h. We then simulated two traffic flow generation scenarios: Group A and Group B, as shown in Fig. 23. In Fig. 23(a), the traffic flow generated shows that the mainline flow rate increases from 0 to 3000 veh/h within the first 60 min, approaching the maximum throughput. Meanwhile, the ramp flow rate remains at 0 until minute 80, then gradually increases to 500 veh/h between minutes 80 and 160, resulting in a total flow rate of 3500 veh/h. This exceeds the maximum throughput, causing congestion at the bottleneck. Fig. 23 (b) presents a comparison scenario in which the ramp flow rate stays at 0, while the mainline flow rate increases from 3000 to 3500 veh/h between minutes 80 and 160. As a result, the total flow rate also reaches 3500 veh/h, surpassing the nominal capacity and causing congestion. However, since there is no traffic on the ramp, no bottleneck is formed. 

Under these conditions, the simulation was run for 360 min, and the flow rate changes at four observation points in both simulation scenarios were recorded, as shown in Fig. 24. It is evident that in Group A, a capacity drop occurred, while no such drop was observed in Group B. From these results, we can draw two conclusions: (1) The simulation framework proposed in this study accurately replicates the capacity drop phenomenon. In a pure HDV environment, the flow rate downstream of the congestion bottleneck decreased from approximately 3056 veh/h to around 2492 veh/h, a reduction of about $1 8 . 5 \%$ . (2) The conditions for a capacity drop are not only that the total flow rate exceeds the maximum throughput but also that a traffic bottleneck is formed. In Group B, although the total flow rate exceeded the maximum throughput, no bottleneck formed, and consequently, no capacity drop was observed. 

Furthermore, we examined the impact of the proposed cooperative control strategy on the capacity drop phenomenon. As shown in Fig. 25, we simulated the generation of bottleneck traffic flow for CAV penetration rates of 0.5 and 1, using the same methodology. Simulations were conducted both with and without cooperative control, and the flow rate changes at Point 1 were recorded, as depicted in Fig. 26. 

From Fig. 26, it is clear that a capacity drop occurred in all cases. However, under the cooperative control mode, this capacity drop was mitigated. Specifically, with a CAV penetration rate of 0.5, the maximum flow rate downstream of the bottleneck decreased from approximately 4265 veh/h to about 3585 veh/h (a reduction of $1 5 . 9 ~ \%$ ) without cooperative control. In contrast, with cooperative control, the maximum flow rate only decreased to around 3787 veh/h, representing a smaller reduction of $1 1 . 2 ~ \%$ . When the CAV penetration rate was 1, the phenomenon was more pronounced. Without cooperative control, the maximum flow rate dropped from approximately 6762 veh/h to 5230 veh/h, a decrease of about $2 2 . 7 ~ \%$ . With cooperative control, the flow rate decreased to around 6090 veh/h, showing a decline of only $9 . 9 ~ \%$ . 

The improvement in the capacity drop under the proposed cooperative control method is primarily attributed to its merging control strategy. The goal of this strategy is to organize vehicles into an optimal arrangement before they reach the merging point, minimizing merge conflicts as much as possible. This not only enhances safety but also reduces the extent of the capacity drop. Additionally, as shown in Fig. 26(b), at simulation times of around 140 min, 170 min, and $2 8 0 \mathrm { m i n }$ , when severe bottlenecks occurred, the cooperative control strategy was able to quickly adjust the traffic flow and restore it to a mild bottleneck state—something that could not be achieved under the non-cooperative control mode. 

# 5.5. Comparation to the ramp metering methods

Ramp metering is a widely adopted strategy for traffic control on highways. Its significance has been consistently demonstrated through numerous field applications. Among various ramp metering strategies, ALINEA stands out as a particularly popular and efficient approach. Developed by Papageorgiou et al. (1991) based on feedback control theory, ALINEA has been extensively implemented worldwide for nearly four decades. Its effectiveness as a control strategy has been well-documented (Papageorgiou et al., 2008). The primary design objectives of ALINEA are: 

$$
r (n) = r (n - 1) + K _ {\mathrm {R}} [ \widehat {o} - o _ {\text {o u t}} (n) ] \tag {79}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/ba9cbdc866f7c14f409c220691844698cf826a44d6fcca5a552a4eb8a78d0267.jpg)



(a) Group A


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/2e48c49dd950e7693ef2aa4e300db2180631fa373a17c33646e58c0e97b0f9a0.jpg)



(b) Group B



Fig. 24. Flow rate changes at four observation points in the simulation scenarios within a pure HDV environment.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/95334ff7cfc453bfcdc3dfef32f42980d8117512982547036442bc328f37686e.jpg)



$( \mathrm { a } ) p _ { \mathrm { C A V } } = 0 . 5$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/784502df3657c4f1a7e212eb6be5ec2d7b82e28c911a315991a21ac5034c2f82.jpg)



$( \mathsf { b } ) p _ { \mathsf { C A V } } = 1$



Fig. 25. Traffic flow generation in the simulation scenarios with CAV infiltration.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/e2c5bde6e7ac22959148b9e9514317e6a6e195ef6bb17eb55fdea8036125342c.jpg)



$( \mathrm { a } ) p _ { \mathrm { C A V } } = 0 . 5$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/816dcbe23ed6db1f890b79f4899ad7214e490aea11cbf3a6ba59a217f62efb83.jpg)



$( \mathsf { b } ) p _ { \mathsf { C A V } } = 1$



Fig. 26. Flow rate changes at Point 1 in the simulation scenarios with CAV infiltration.


where $n$ is the discrete time index. $o _ { \mathrm { o u t } } ( n )$ denotes lane-averaged mainstream occupancy measurements collected during the control time interval $( ( n - 1 ) T _ { \mathrm { R M } } , n T _ { \mathrm { R M } } ]$ . $T _ { \mathrm { R M } }$ is the cycle of ramp metering within the range 20–60 s. r(n) represents the on-ramp inflow applied over $[ n T _ { \mathrm { R M } } , ( n + 1 ) T _ { \mathrm { R M } } )$ ; $\widehat { \pmb { o } }$ is a set (desired) value for the occupancy and typically selected equal to the critical occupancy $o _ { \mathrm { c r } }$ based on the aforementioned goal of flow maximization. $K _ { \mathrm { R } } > 0$ is a regulator parameter. $r ( n )$ , determined with Eq. (79), is truncated if it exceeds a range $[ r _ { \operatorname* { m i n } } , r r _ { \operatorname* { m a x } } ( n ) ]$ , where $r _ { \mathrm { m i n } }$ is a minimum admissible ramp inflow, and $r r _ { \operatorname* { m a x } } ( n )$ is determined by the following function: 

$$
r r _ {\max } (n) = \min  \left\{r _ {\max }, q _ {r} (n - 1) + 4 0 0 \right\} \tag {80}
$$

where $r _ { \mathrm { m a x } }$ denoting the ramp’s flow capacity, $q _ { r } ( n - 1 )$ denoting the real (measured) ramp inflow during the last control time interval $( ( n { - } 1 ) T _ { \mathrm { R M } } , n T _ { \mathrm { R M } } ]$ , and 400 vehicles/h being an empirical value (Wang et al., 2014). 

However, the effectiveness of the ALINEA strategy may be compromised in specific scenarios where bottlenecks with reduced capacity occur, such as uphill or curved sections, tunnels, bridges, lane drops, or downstream uncontrolled on-ramps. This limitation primarily stems from the significant time delay between the implementation of ramp metering actions and their subsequent impact on traffic flow dynamics at the bottleneck location. To overcome this challenge, Wang et al. (2014) developed the PI-ALINEA control strategy, which has been rigorously validated over the past decade. Extensive empirical studies have consistently demonstrated the superior performance of this enhanced control strategy (Kan et al., 2016). PI-ALINEA strategy is designed to be: 

$$
r (n) = r (n - 1) - K _ {\mathrm {P}} \left[ o _ {\text {o u t}} (n) - o _ {\text {o u t}} (n - 1) \right] + K _ {\mathrm {R}} \left[ \widehat {o} - o _ {\text {o u t}} (n) \right] \tag {81}
$$

where $K _ { \mathrm { P } } > 0$ is the regulator parameter of the additional proportional term. 

This section presents a comparative analysis of the proposed cooperative control strategy against two established ramp metering methods, ALINEA and PI-ALINEA, within the proposed simulation framework. It is important to note that both ALINEA and PI-ALINEA are primarily designed to address congestion at on-ramps and are therefore not applicable in relatively free-flow traffic conditions. For instance, in scenarios where the total flow rate is 2500 veh/h (as shown in Fig. 12) or 3500 veh/h with high CAV penetration rates (as illustrated in Fig. 11), where the total flow remains below the ramp’s capacity, traditional ramp metering strategies become inoperative, precluding any meaningful comparison of control effectiveness under such free-flow conditions. 

Following the methodology outlined by Wang et al. (2014), the implementation of ALINEA and PI-ALINEA strategies in this study 

utilizes the section density $K ( n )$ as a substitute for $o _ { \mathrm { o u t } } ( n )$ , with critical density $K _ { \mathrm { c r } }$ replacing critical occupancy $o _ { \mathrm { c r } }$ . The determination of $K _ { \mathrm { c r } }$ is crucial as it directly influences the control efficacy of the ramp metering strategies. Since critical density represents the density at which traffic flow reaches its maximum in the fundamental diagram, understanding the fundamental diagram model − which describes the interrelationship among the three traffic flow parameters λ (flow rate), K (traffic density), and v (speed) − is essential for accurate $K _ { \mathrm { c r } }$ estimation. 

In this study, the car-following behaviors within the simulation framework are characterized by multiple car-following models. The behaviors are categorized into nine distinct types based on vehicle classifications. Specifically, these include: CAV following CAV scenarios (utilizing both IDM (1) and PATH CACC model (2)), CAV following non-CAV scenarios (employing IDM (3) and PATH ACC model (4)), AV following vehicle scenarios (implementing IDM (5) and PATH ACC model (6)), and HDV following vehicle scenarios (applying IDM (7), LCM (8), and Gipps model (9)). Consequently, the interrelationships among the three fundamental traffic flow parameters in our simulation environment can be mathematically represented by the following models: 

$$
\left\{ \begin{array}{c} K = \frac {1}{p _ {1} \left(\frac {S _ {0} + t _ {\mathrm {C}} v}{\sqrt {1 - \left(\frac {v}{v _ {\mathrm {f}}}\right) ^ {4}}} + L\right) + p _ {2} \left(t _ {\mathrm {C}} v + L + S _ {0}\right) + \left(p _ {3} + p _ {5}\right) \left(\frac {S _ {0} + t _ {\mathrm {A}} v}{\sqrt {1 - \left(\frac {v}{v _ {\mathrm {f}}}\right) ^ {4}}} + L\right) + \left(p _ {4} + p _ {6}\right) \left(t _ {\mathrm {A}} v + L + S _ {0}\right)} \\ + p _ {7} \left(\frac {S _ {0} + t _ {\mathrm {H}} v}{\sqrt {1 - \left(\frac {v}{v _ {\mathrm {f}}}\right) ^ {4}}} + L\right) + p _ {8} \left(\gamma v ^ {2} + \tau v + L + S _ {0}\right) \left(1 - \ln \left(1 - \frac {v}{v _ {\mathrm {f}}}\right)\right) + p _ {9} \left(1. 5 \tau v + L + S _ {0}\right) \\ \lambda = K v \end{array} \right. \tag {82}
$$

where $p _ { 1 } { \cdot } p _ { 9 }$ represent the proportion of the nine car-following behaviors mentioned above, and their calculation methods are as follows: 

$$
p _ {1} = p _ {2} = p _ {\mathrm {C A V}} \cdot p _ {\mathrm {C A V}} / 2
$$

$$
p _ {3} = p _ {4} = p _ {\mathrm {C A V}} \cdot \left(1 - p _ {\mathrm {C A V}}\right) / 2 \tag {83}
$$

$$
p _ {5} = p _ {6} = p _ {\mathrm {A V}} / 2
$$

$$
p _ {7} = p _ {8} = p _ {9} = p _ {\mathrm {H D V}} / 3
$$

Accordingly, fundamental diagrams of traffic flow can be constructed for CAV penetration rates of 0.1, 0.5, and 1, as illustrated in Fig. 27. It should be noted that the proportions of AVs and HDVs at any given CAV penetration rate are determined by Eqs. 77–78. 

Initially, a simulation set was designed for a CAV penetration rate of 0.1, with a total flow rate of 3500 veh/h. This configuration consists of 1500 veh/h on the two mainline lanes and 500 veh/h on the ramp, consistent with the settings in Section 5.3.1. Regarding the parameters for ALINEA and PI-ALINEA strategies, except for the critical density $K _ { \mathrm { c r } }$ which was determined according to Fig. 27, all other parameters were maintained as per Wang et al. (2014). Specifically, the ALINEA model parameters were set as $K _ { \mathrm { R } } = 4 0 ~ \mathrm { k m } ^ { \ast }$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/632be27118a9aaf8d6e59875b32eda17c9818f4f9681a0d60bd1ca7ef36c19e0.jpg)



Fig. 27. Relationships among the three traffic flow parameters under different CAV penetration rates.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/f507e8a840544c1bf8dc4ff859a09d732de1cf821970a63de7572052623ba0a3.jpg)



Fig. 28. Evaluation indicators for each group under a CAV penetration rate of 0.1, with a mainline flow rate of 1500 veh/h (across two lanes) and a ramp flow rate of 500 veh/h.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/217ad65795d0e226d95b2e7c96ca9b06eabc9d1b4612cd294d8de922c0db4a7c.jpg)



Fig. 29. Evaluation indicators for each group under a CAV penetration rate of 0.1, with a mainline flow rate of 1200 veh/h (across two lanes) and a ramp flow rate of 1100 veh/h.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/3bebecc2209644fa9d8f5701d2bfb0e178e1c78d88b8d549c210f333fa956bbb.jpg)



Fig. 30. Evaluation indicators for each group under a CAV penetration rate of 0.5.


lane/h, while the PI-ALINEA model parameters were $K _ { \mathrm { R } } = 4 ~ { \mathrm { k m } } \cdot { \mathrm { s } } \ { \mathrm { l a n e / h } } , K _ { \mathrm { P } } = 1 0 0 ~ { \mathrm { k m } } \cdot { \mathrm { l a n e / h } }$ . $T _ { \mathrm { R M } } = 3 0 s$ , with $r _ { \mathrm { m i n } } = 3 0 0$ veh/h and $r _ { \mathrm { m a x } } = 2 0 0 0 ~ \mathrm { v e h / h }$ . All other simulation parameters remained consistent with those in Section 5.3.1. 

The simulation results are presented in Fig. 28. Analysis reveals that under this flow rate configuration, ramp metering did not improve traffic conditions in the merging area. This phenomenon may be attributed to the relatively low ramp flow rate, which limited the effectiveness of the ramp metering strategies. Consequently, an additional simulation set was designed with modified flow rates: 1200 veh/h on the two mainline lanes and 1100 veh/h on the ramp, while maintaining the total flow rate at 3500 veh/h. The corresponding results are shown in Fig. 29. 

The findings demonstrate that under this revised configuration, both ALINEA and PI-ALINEA significantly reduced vehicle delay values, indicating their effectiveness in enhancing traffic efficiency in the merging area. However, it is noteworthy that these ramp metering strategies resulted in increased average TET values, potentially elevating collision risks. This phenomenon may be explained by the frequent stop-and-go operations required by vehicles on the ramp when implementing ramp metering strategies, which inherently increases the probability of collisions. 

Furthermore, two additional simulation sets were conducted, corresponding to CAV penetration rates of 0.5 and 1 (representing a pure CAV environment), respectively. In the 0.5 CAV penetration scenario, the flow rate was consistently set at 1400 veh/h across all three lanes. For the pure CAV scenario, the flow rates were adjusted to 2400 veh/h for the two mainline lanes and 2000 veh/h for the ramp. The corresponding simulation results are illustrated in Figs. 30 and 31. 

Analysis of the results indicates the following key findings: At the 0.5 CAV penetration rate, the cooperative control strategy outperformed traditional ramp metering approaches across all performance metrics, including delay reduction. In the pure CAV scenario, while ramp metering strategies achieved better results in reducing delays, the cooperative control strategy retained a clear and decisive advantage in critical safety and ride comfort measures. 

In summary, a comparison between the proposed method in this study and traditional ramp metering approaches yields the following conclusions: 

(1) Traditional ramp metering methods require less traffic infrastructure investment and impose no specific vehicle type requirements, making them easier to implement. In contrast, the proposed coordinated control strategy necessitates connected and automated technology, with specific demands on roadside facilities and vehicle types, resulting in greater implementation complexity. 

(2) Conventional ramp metering techniques are primarily effective under congested traffic conditions. Moreover, it shows limited performance when the flow rate proportion of ramp is low. Conversely, the proposed cooperative control strategy demonstrates effectiveness across both congested and free-flow traffic conditions, regardless of ramp flow rate proportions. 

(3) While traditional ramp metering methods significantly reduce average vehicle delay in on-ramp areas and improve traffic efficiency, their stop-and-go operation may increase collision risks. The proposed cooperative control strategy, however, achieves superior performance in enhancing traffic efficiency, safety, and ride comfort simultaneously. 

# 5.6. Analysis of the speed update perturbations

Robustness is a critical criterion for evaluating the effectiveness of control strategies. In real-world traffic scenarios, traffic flow is subject to numerous uncertainties. For instance, vehicle speeds do not follow the predefined patterns used in simulations but instead exhibit significant fluctuations. Therefore, it is essential to investigate whether control strategies remain effective under such con ditions. This section presents a series of experiments designed to examine the robustness of control strategies under speed update perturbations. 

In this section, speed fluctuations in real-world traffic are simulated by introducing a proportional perturbation to the vehicle acceleration at each simulation time step. Specifically: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/b00fe240ef6ed1ed92b2ced37132229dec8c5b29d1511bbf0ebc413c500de686.jpg)



Fig. 31. Evaluation indicators for each group under a CAV penetration rate of 1.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/de0ac3e0a0218c1d2569a057849617aeeccbb4f6bf11a367f63ee583b11d7b39.jpg)



(a)TET


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/1c07e4ac641c5271f09c99de019fea4568840f2481d70ede8b28ba28e0acbcb8.jpg)



(b)TETMP


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/b1239495d68d30905659d914462ff4bbda4f7f97c6905646c416784df5eb2160.jpg)



(c) CPMR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/ef153886f6dc969b13130f5fdf3fa364eb6fc2ab11fa5d23475c5737f39384d6.jpg)



(d) Delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/d67d8d465ed9b802cadddcad1b7d4af8c111a34c2a416c2d2254735ecc3bfcf4.jpg)



(e)CD



Fig. 32. The average values of diverse evaluation indicators under different speed update perturbation modes, with a total flow rate of 3500 vehicles per hour.


$$
a _ {i} (t) = a _ {i} (t) \cdot (1 + \varepsilon) \tag {84}
$$

where $\varepsilon$ represents the perturbation to vehicle acceleration, randomly assigned within the range of $- 1 0 \%$ to $1 0 \%$ for each vehicle at 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/e27d17386ca3010cb7e7b1dd9ddf2766c557f2addc86230c05a9a5f6fc6a70b3.jpg)



(a)TET


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/418e5661efdd35858f4cbefe4d2d69891ffe18b59414c49deb93361c4a97dca9.jpg)



(b) TETMP


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/6ef50e747f48e499c0024126a58686d6c41a94cd949dc4fd2b34557535d9976a.jpg)



(c) CPMR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/6834022e5181292ac832059c8ed3bb9bc63963e2027b7b1fcc3f168aa954aa1a.jpg)



(d) Delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/f0bc9130833ac3dd4e29e1094cd56ea168617984374a83e8a110452ade60d2e4.jpg)



(e)CD



Fig. 33. The average values of diverse evaluation indicators under different speed update perturbation modes, with a total flow rate of 2500 vehicles per hour.


# every simulation step.

Following the same configuration as in Section 5.3.1, simulations were conducted under both speed update perturbation and general settings. Two sets of simulations were performed with total flow rates of 3500 veh/h and 2500 veh/h, respectively, with each set comprising 50 simulation rounds. The results are illustrated in Figs. 32 and 33. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/a83a9ad4fc58b1341fb1aa5fb4a2d0ae48ff0966cd858287c84d90258a731248.jpg)



(a)TET


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/95f1ac6ebaaae1aea5c754e375bb5cb554001e7508905cfbee39d56a47a85e04.jpg)



(b)TETMP


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/8cee2e9f6f194291a11ddcaa0be512c4b81aab91b9e40330c050390422972b28.jpg)



(c) CPMR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/d897d9554b18fc27e6e117b40d33b68dc838497cb111f15bc94734db2fafc927.jpg)



(d) Delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/2d3184c5-2c49-4e21-9fd5-a9d0bf58c6fe/742e12d1754c7c144bfc065acb959eca3067dd9032e5664bff951dcea63e78a9.jpg)



(e) CD



Fig. 34. The average values of diverse evaluation indicators across different lane-changing control modes, with a total flow rate of 1500 vehicles per hour.


The figures reveal that while the average values of evaluation indicators exhibit minor fluctuations under speed update perturbation compared to the general setting, these variations are not substantial. More importantly, regardless of whether speed update perturbation is applied, the evaluation indicators for the cooperative control group consistently remain lower than those for the noncooperative control group, with similar magnitudes of reduction. This demonstrates that the control strategy significantly improves traffic conditions even in the presence of speed fluctuations, indicating its robustness. 

The robustness of the strategy lies in its real-time update mechanism, which does not rely on speed predictions. It only depends on the positions and speeds of vehicles within the control area at the current time, which are provided by high-precision vehicle detectors. Moreover, in the simulation framework, vehicle behavior is also constrained by basic safety limitations. For example, acceleration updates must ensure safety from the preceding vehicle, and lane changes must satisfy lane-changing conditions. This ensures that even if high-precision vehicle detectors make occasional errors, the basic safety of the vehicles is maintained. 

# 5.7. Discussion on lane-changing control effectiveness under low demand

In this study, the lane-changing control strategy is based on equalizing traffic flow characteristics in the mainline, specifically focusing on equilibrium of both average speed and traffic density. Nonetheless, under conditions of low traffic demand—where density is characteristically minimal and speeds approach their zenith—a pivotal question emerges: Is it imperative to balance both speed and density, or would it be adequate to concentrate on a singular factor? Furthermore, the efficacy of such a control strategy, which aims to equilibrate traffic flow characteristics, warrants scrutiny. 

To address these questions, we established three comparison groups for lane-changing control effectiveness comparison. Both the lane-changing control group and the three comparison groups implemented lane-changing control strategies exclusively, without incorporating merging control strategies. Comparison group (1) implemented lane-changing control considering only speed equilibrium, while comparison group (2) focused solely on traffic density equilibrium. Comparison group $( 3 )$ employed a model proposed by Ramezani and Ye (2019), which identifies CAVs in the mainline that might potentially interfere with ramp vehicle merging. When interference is detected, the model suggests these CAVs change lanes before the merging boundary to create additional space for merging vehicles. 

The simulation replicated low-demand conditions with a flow rate of 500 veh/h for both mainline lanes and the ramp. Other simulation parameters remained consistent with those in Section 5.3.1. As illustrated in Fig. 34, the simulation results demonstrate that comparison group (1) yielded the least effective control outcomes, indicating that considering speed equilibrium alone is inadequate. Comparative analysis between comparison group (2) and the lane-changing control group reveals that under low-demand conditions, the control effectiveness of balancing both speed and density is comparable to that of considering density alone, as evidenced by the proximity of evaluation indicator values. 

Notably, when comparing comparison group (3) with the lane-changing control group, the latter demonstrates significantly lower values in TET, TETMP, and CPMR metrics, indicating superior performance in enhancing traffic safety compared to the Ramezani and Ye (2019) model. Regarding traffic delay, the lane-changing control group shows lower delays when CAV penetration rates are below 0.8, with comparable delays at higher rates. In terms of CD metrics, the lane-changing control group maintains lower values across most penetration rates, except at full CAV penetration (1.0) where both groups show similar results. 

In summary, under low-demand conditions, the control strategy proposed in this study demonstrates excellent performance in enhancing traffic safety, improving traffic efficiency, and ensuring driving comfort. 

# 6. Conclusions

This paper presents a cooperative control strategy for CAVs in on-ramp areas under heterogeneous traffic flow conditions. It begins with an overview of the environmental context of on-ramp areas, focusing on the integration of connected and automated technol ogies. This is followed by a detailed description of the cooperative control strategy, which comprises two key components. 

The first component addresses merging control, with an emphasis on coordinating the movements of CAVs on the mainline Outside Lane and those on the ramp. This coordination is achieved by adjusting right-of-way allocation, thereby facilitating a smooth merging process between vehicles in these lanes. The goal is to optimize platoon dynamics before reaching the merging boundary, thus reducing the likelihood of conflicts. 

The second component focuses on lane-changing control, which enables CAVs to make informed decisions about lane changes on the mainline. This process involves managing traffic density and vehicle speed across the two mainline lanes, ensuring a balanced and efficient flow of traffic. 

To assess the effectiveness of the proposed strategy, a simulation framework was developed, incorporating calibrated parameters that reflect real-world conditions. The simulation results indicate that the integration of AVs or CAVs significantly enhances traffic conditions on on-ramp systems. Notably, CAVs demonstrate superior benefits in improving traffic conditions compared to AVs, especially at higher penetration rates. The evaluations further examine the extent to which the proposed cooperative control strategy for CAVs enhances traffic conditions. Under this cooperative control strategy, the safety, traffic efficiency, and ride comfort of the onramp system show marked improvements. In a typical simulation scenario, the average reduction rates of TET, TETMP, and CPMR exceed $9 0 \%$ . Moreover, delay and CD values can be reduced by up to $4 0 \%$ . Even at lower CAV penetration rates, this strategy achieves significant results. Furthermore, simulations reveal that the cooperative control approach mitigates the capacity drop phenomenon, enhancing overall merge-zone efficiency. 

Looking ahead, future research will focus on exploring cooperative control strategies for CAVs in a broader range of contexts. In 

addition, we aim to expand our simulation methodologies by incorporating more real-world experiments, which will further enhance the depth and robustness of our findings. 

# CRediT authorship contribution statement

Wenzhang Yang: Writing – review & editing, Writing – original draft, Supervision, Software, Methodology, Funding acquisition, Formal analysis, Conceptualization. Changyin Dong: Writing – review & editing, Supervision, Methodology, Funding acquisition. Ziqian Zhang: Writing – review & editing, Formal analysis. Hui Zhang: Writing – review & editing, Formal analysis. Hao Wang: Writing – review & editing, Supervision, Methodology, Funding acquisition, Conceptualization. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Acknowledgements

This work was sponsored by the National Science and Technology Major Project (No. 2022ZD0115600), the National Natural Science Foundation of China (No.52072067; No. 52302405), the Natural Science Foundation of Jiangsu Province (No. BK20210249), the SEU Innovation Capability Enhancement Plan for Doctoral Students (CXJH_SEU 24178), the Postgraduate Research & Practice Innovation Program of Jiangsu Province (KYCX24_0451), and the Postdoctoral Fellowship Program of CPSF (No. GZC20230431). 

# Data availability

Data will be made available on request. 

# References



Chen, D., Ahn, S., 2018. Capacity-drop at extended bottlenecks: Merge, diverge, and weave. Transp. Res. B Methodol. 108, 1–20. 





Chen, H., Wang, J., 2019. A decision-making method for lane changes of automated vehicles on freeways based on driver’s dissatisfaction. China J. Highway Transport 32 (12), 1–9 (in Chinese). 





Chen, T., Wang, M., Gong, S., Zhou, Y., Ran, B., 2021. Connected and automated vehicle distributed control for on-ramp merging scenario: a virtual rotation approach. Transp. Res. Part C Emerging Technol. 133, 103451. 





Chen, X., Dong, C., Yang, W., Hou, Y., Wang, H., 2024. Platoon control and external human-machine interfaces: innovations in pedestrian-autonomous vehicle interactions. Transportmetrica A: Transport Science 20, 1–32. 





Chen, X., Li, X., Hou, Y., Yang, W., Dong, C., Wang, H., 2025. Effect of eHMI-equipped automated vehicles on pedestrian crossing behavior and safety: a focus on blind spot scenarios. Accid. Anal. Prev. 212, 107915. 





Ding, H., Di, Y., Zheng, X., Bai, H., Zhang, W., 2021. Automated cooperative control of multilane freeway merging areas in connected and autonomous vehicle environments. Transportmetrica B: Transport Dynamics 9 (1), 437–455. 





Fang, Y., Min, H., Wu, X., Wang, W., Zhao, X., Mao, G., 2022. On-Ramp merging strategies of connected and automated vehicles considering communication delay. IEEE Trans. Intell. Transp. Syst. 23 (9), 15298–15312. 





Gipps, P.G., 1981. A behavioural car-following model for computer simulation. Transp. Res. B Methodol. 15, 105–111. 





Han, L., Zhang, L., Guo, W., 2023. Multilane freeway merging control via trajectory optimization in a mixed traffic environment. IET Intelligent Transport System 17, 1891–1907. 





Hayward, J.C., 1972. Near-miss determination through use of a scale of danger. Highw. Res. Rec. 384, 24–385. 





He, X., Lou, B., Yang, H., Lv, C., 2023. Robust decision making for autonomous vehicles at highway on-ramps: a constrained adversarial reinforcement learning approach. IEEE Trans. Intell. Transp. Syst. 24 (4), 4103–4113. 





Hou, K., Zheng, F., Liu, X., Guo, G., 2023. Cooperative on-ramp merging control model for mixed traffic on multi-lane freeways. IEEE Trans. Intell. Transp. Syst. 24 (10), 10774–10790. 





ISO 2631-1, 1997. Mechanical vibration and shock - Evaluation of human exposure to whole-body vibration - Part 1: General requirements. https://www.iso.org/obp/ ui/en/#iso:std:iso:2631:-1:ed-2:v2:en. 





Jia, B., Jiang, R., Wu, Q., 2005. The effects of accelerating lane in the on-ramp system. Physica A 345 (1–2), 218–226. 





Jing, S., Hui, F., Zhao, X., Rios-Torres, J., Khattak, A.J., 2019. Cooperative game approach to optimal merging sequence and on-ramp merging control of connected and automated vehicles. IEEE Trans. Intell. Transp. Syst. 20 (11), 4234–4244. 





Kan, Y., Wang, Y., Papageorgiou, M., Papamichail, I., 2016. Local ramp metering with distant downstream bottlenecks: a comparative study. Transp. Res. Part C Emerging Technol. 62, 149–170. 





Karimi, M., Roncoli, C., Alecsandru, C., Papageorgiou, M., 2020. Cooperative merging control via trajectory optimization in mixed vehicular traffic. Transp. Res. Part C Emerging Technol. 116, 102663. 





Krajewski, R., Bock, J., Kloeker, L., Eckstein, L., 2018. The highD dataset: a drone dataset of naturalistic vehicle trajectories on german highways for validation of highly automated driving systems. 2018 21st International Conference on Intelligent Transportation Systems (ITSC), Maui, HI, USA, pp. 2118-2125. 





Leclercq, L., Laval, J.A., Chiabaut, N., 2011. Capacity drops at merges: an endogenous model. Transp. Res. B Methodol. 45 (9), 1302–1313. 





Li, M., Li, Z., Wang, S., Zheng, S., 2023. Enhancing cooperation of vehicle merging control in heavy traffic using communication-based soft actor-critic algorithm. IEEE Trans. Intell. Transp. Syst. 24 (6), 6491–6506. 





Li, L., Qian, C., Gan, J., Zhang, D., Qu, X., Xiao, F., Ran, B., 2024a. DCoMA: a dynamic coordinative merging assistant strategy for on-ramp vehicles with mixed traffic conditions. Transp. Res. Part C Emerging Technol. 165, 104700. 





Li, L., Gan, J., Cui, C., Ma, H., Qu, X., Wang, Q., Ran, B., 2024b. Potential field-based modeling and stability analysis of heterogeneous traffic flow. App. Math. Model. 125, 485–508. 





Liao, X., Wang, Z., Zhao, X., Han, K., Tiwari, P., Barth, M.J., Wu, G., 2022. Cooperative ramp merging design and field implementation: a digital twin approach based on vehicle-to-cloud communication. IEEE Trans. Intell. Transp. Syst. 23 (5), 4490–4500. 





Lin, J., Yu, C., Wang, L., Liu, G., Wang, J., Ma, W., 2023. Optimization of lane-changing advisory in mixed traffic of connected vehicles and human-driven vehicles at expressway bottlenecks. IEEE Transactions on Intelligent Vehicles. 





Liu, J., Zhao, W., Xu, C., 2022. An efficient on-ramp merging strategy for connected and automated vehicles in multi-lane traffic. IEEE Trans. Intell. Transp. Syst. 23 (6), 5056–5067. 





Liu, H., Zhuang, W., Yin, G., Li, Z., Cao, D., 2023. Safety-critical and flexible cooperative on-ramp merging control of connected and automated vehicles in mixed traffic. IEEE Trans. Intell. Transp. Syst. 24 (3), 2920–2934. 





Luo, X., Li, X., Shaon, M.R.R., Zhang, Y., 2022. Multi-lane-merging strategy for connected automated vehicles on freeway ramps. Transportmetrica B: Transport Dynamics 11 (1), 127–145. 





McCartt, A.T., McCartt, V.S., Retting, R.A., 2004. Types and characteristics of ramp-related motor vehicle crashes on urban interstate roadways in Northern Virginia. J. Saf. Res. 35, 107–114. 





Milan´es, V., Shladover, S.E., 2014. Modeling cooperative and autonomous adaptive cruise control dynamic responses using experimental data. Transp. Res. Part C Emerging Technol. 48, 285–300. 





Minderhoud, M.M., Bovy, P.H., 2001. Extended time-to-collision measures for road traffic safety assessment. Accid. Anal. Prev. 33 (1), 89–97. 





Moers, T., Vater, L., Krajewski, R., Bock, J., Zlocki, A., Eckstein, L., 2022. The exiD dataset: a real-world trajectory dataset of highly interactive highway scenarios in germany. 2022 IEEE Intelligent Vehicles Symposium (IV), Aachen, Germany, pp. 958-964. 





Mu, C., Du, L., Zhao, X., 2021. Event triggered rolling horizon based systematical trajectory planning for merging platoons at mainline-ramp intersection. Transp. Res. Part C Emerging Technol. 125, 103006. 





Nagalur Subraveti, H.H.S., Srivastava, A., Ahn, S., Knoop, V.L., van Arem, B., 2021. On lane assignment of connected automated vehicles: strategies to improve traffic flow at diverge and weave bottlenecks. Transp. Res. Part C Emerging Technol. 127, 103126. 





Ni, D., 2016. Traffic Flow Theory: Characteristics, Experimental Methods, and Numerical Techniques. Elsevier. 





Papageorgiou, M., Hadj-Salem, H., Blosseville, J.M., 1991. ALINEA: a local feedback control law for on-ramp metering. Transp. Res. Rec. 1320, 58–64. 





Papageorgiou, M., Kosmatopoulos, E., Papamichail, I., Wang, Y., 2008. A misapplication of the local ramp metering strategy ALINEA. IEEE Trans. Intell. Transp. Syst. 9 (2), 360–365. 





Ramezani, M., Ye, E., 2019. Lane density optimisation of automated vehicles for highway congestion control. Transportmetrica B: Transport Dynamics 7 (1), 1096–1116. 





Rengaraju, V.R., Rao, V.T., 1995. Vehicle-arrival characteristics at urban uncontrolled intersections. J. Transp. Eng. 121 (4), 317–323. 





Rios-Torres, J., Malikopoulos, A.A., 2017. Automated and cooperative vehicle merging at highway on-ramps. IEEE Trans. Intell. Transp. Syst. 18 (4), 780–789. 





Roncoli, C., Bekiaris-Liberis, N., Papageorgiou, M., 2017. Lane-changing feedback control for efficient lane assignment at motorway bottlenecks. Transp. Res. Rec. 2625, 20–31. 





Sarvi, M., Kuwahara, M., Ceder, A., 2010. Observing freeway ramp merging phenomena in congested traffic. J. Adv. Transp. 41 (2), 145–170. 





Shi, J., Li, K., Chen, C., Kong, W., Luo, Y., 2023. Cooperative merging strategy in mixed traffic based on optimal final-state phase diagram with flexible highway merging points. IEEE Trans. Intell. Transp. Syst. 24 (10), 11185–11197. 





Simon, P.M., Gutowitz, H.A., 1998. Cellular automaton model for bidirectional traffic. Phys. Rev. E: Statistical Phys., Plasmas, Fluids, Related Interdiscip. Topics 57 (2 Pt B), 2441–2444. 





Sun, Z., Huang, T., Zhang, P., 2020. Cooperative decision-making for mixed traffic: a ramp merging example. Transp. Res. Part C Emerging Technol. 120, 102764. 





Tadaki, S., Kikuchi, M., 1995. Self-organization in a two-dimensional cellular automaton model of traffic flow. J. Phys. Soc. Jpn. 64 (12), 4504–4508. 





Treiber, M., Hennecke, A., Helbing, D., 2000. Congested traffic states in empirical observations and microscopic simulations. Phys. Rev. E: Statistical Phys., Plasmas, Fluids, Related Interdiscip. Topics 62 (2 Pt A), 1805–1824. 





Wang, Y., Kosmatopoulos, E., Papageorgiou, M., Papamichail, I., 2014. Local ramp metering in the presence of a distant downstream bottleneck: theoretical analysis and simulation study. IEEE Trans. Intell. Transp. Syst. 15 (5), 2024–2039. 





Wang, Y., Wang, L., Yu, X., Guo, J., 2023. Capacity drop at freeway ramp merges with its replication in macroscopic and microscopic traffic simulations: a tutorial report. Sustainability 15, 2050. 





Xiong, B., Jiang, R., Li, X., 2022. Managing merging from a CAV lane to a human-driven vehicle lane considering the uncertainty of human driving. Transp. Res. Part C Emerging Technol. 142, 103775. 





Xue, Y., Zhang, X., Cui, Z., Yu, B., Gao, K., 2023. A platoon-based cooperative optimal control for connected autonomous vehicles at highway on-ramps under heavy traffic. Transp. Res. Part C Emerging Technol. 150, 104083. 





Yang, W., Dong, C., Wang, H., 2023a. A cooperative merging speed control strategy of CAVs based on virtual platoon in on-ramp merging system. Transportmetrica B: Transport Dynamics 11 (1), 1432–1454. 





Yang, W., Dong, C., Chen, X., Chen, Y., Wang, H., 2023b. A cooperative control method for safer on-ramp merging process in heterogeneous traffic flow. Accid. Anal. Prev. 193, 107324. 





Yang, W., Dong, C., Zhang, Z., Chen, X., Wang, H., 2025. A dual-module cooperative control method for on-ramp area in heterogeneous traffic flow using reinforcement learning. Eng. Appl. Artif. Intel. 150, 110584. 





Yao, Z., Ma, Y., Ren, T., Jiang, Y., 2024. Impact of the heterogeneity and platoon size of connected vehicles on the capacity of mixed traffic flow. App. Math. Model. 125, 367–389. 





Yu, W., Hua, X., Ngoduy, D., Wang, W., 2023. On the assessment of the dynamic platoon and information flow topology on mixed traffic flow under connected environment. Transp. Res. Part C Emerging Technol. 154, 104265. 





Zhu, J., Tasic, I., 2021. Safety analysis of freeway on-ramp merging with the presence of autonomous vehicles. Accid. Anal. Prev. 152, 105966. 

