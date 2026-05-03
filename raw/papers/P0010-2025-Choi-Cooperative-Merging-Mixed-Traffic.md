# Cooperative Merging in Mixed Traffic Based on Strategic Influence of Connected Automated Vehicles on Human-Driven Vehicle Behavior

Kyunghwan Choi,\* Seongjae Shin, and Minseok Seo 

Cooperative on-ramp merging control for connected and automated vehicles (CAVs) can significantly enhance traffic flow and fuel efficiency at highway merging points. However, in mixed traffic scenarios where CAVs coexist with human-driven vehicles (HDVs), the unpredictable behavior of HDVs poses challenges to safety and coordination. While many cooperative merging strategies focus on individual CAV control, fewer have addressed the coordination of multiple CAVs in such settings. This study introduces an optimization-based cooperative merging strategy for all CAVs within a control zone, considering interactions with HDVs of uncertain intentions. A key innovation is the strategic influence of CAVs on HDV behavior by slowing down the CAV preceding HDVs, thereby allowing other CAVs on the adjacent road to merge in front of the HDVs with reduced uncertainty. The optimal slowdown pattern is identified by evaluating CAV throughput across various candidate patterns, with dynamic optimization applied at each time a new vehicle enters the control zone to effectively manage HDV uncertainties. Experimental results from various mixed-traffic scenarios show that the proposed strategy reduces the average travel time delay by up to $31\%$ compared to an existing optimization-based approach. 

# 1. Introduction

# 1.1. Motivation

The advent of connected and automated vehicle (CAV) technologies offers a transformative opportunity to enhance traffic flow and safety, reduce energy consumption, and minimize 

K. Choi, S. Shin  
Department of Mechanical and Robotics Engineering  
Gwangju Institute of Science and Technology  
Gwangju 61005, Republic of Korea  
E-mail: khchoi@gist.ac.kr 

M. Seo  
Al Graduate School  
Gwangju Institute of Science and Technology  
Gwangju 61005, Republic of Korea 

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/aisy.202400797. 

© 2025 The Author(s). Advanced Intelligent Systems published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. 

DOI: 10.1002/aisy.202400797 

greenhouse gas emissions. By leveraging connectivity and automation, CAVs have the potential to significantly improve transportation efficiency across various scenarios, particularly in complex environments such as highway on-ramp merging points[1,2] and signalized intersections.[3] Numerous studies have highlighted the benefits of optimizing CAV operations through advanced control and optimization strategies, such as time and energy-optimal control strategies,[4-8] game-theoretic strategies,[9-12] and reinforcement learning (RL)[13-16] (see refs. [17,18] for surveys). However, these studies often assume a complete penetration of CAVs, which is not expected to be the reality until at least 2060.[19] Until then, CAVs must coexist with human-driven vehicles (HDVs), creating mixed-traffic environments that present unique challenges and opportunities. 

In mixed-traffic conditions, the presence of HDVs introduces unpredictability in traffic flow due to the diverse driving 

behaviors of human drivers. This variability poses significant challenges for effective coordination and control of CAVs. Individual CAVs, while beneficial, may not suffice to optimize overall traffic conditions without coordination. For instance, one study has demonstrated that the isolated operation of automated vehicles can lead to suboptimal traffic performance unless the vehicles are connected and share information.[20] Thus, it becomes imperative to develop cooperative strategies that enable CAVs to work together to improve the entire mixed traffic environment. 

Addressing this problem involves three key challenges. First, control methods for CAVs must incorporate human driving behavior and interactions between CAVs and HDVs. Ignoring these factors could lead to overly cautious CAV behavior that prioritizes safety at the expense of efficiency. Second, optimizing CAV behavior requires considering multiple CAVs and HDVs within the control and merging zones, rather than focusing solely on a small number of vehicles in the merging zone, to fully harness the potential of CAVs. Finally, optimizing CAV behavior necessitates considering a variety of standard metrics, including safety, fuel efficiency, average travel time, and the naturalness of vehicle movements.[21] This article seeks to address the coordination challenges of multiple CAVs in mixed traffic, using merging scenarios as a representative example. These scenarios are 

critical traffic bottlenecks and frequent sites of accidents. The primary focus is on how CAVs can interact with and influence HDV behavior, taking into account interactions involving multiple vehicles. 

# 1.2. Literature Review

This section presents a state-of-the-art review of cooperative merging strategies in mixed traffic, categorized into two main areas: 1) merging control for CAVs at a single- or dual-vehicle level and 2) merging control at a multivehicle level. Within each category, control methods are further classified into two approaches: optimization-based methods and RL. Additionally, how HDV behavior is modeled and handled in each control method is discussed. 

# 1.2.1. Merging Control in Mixed Traffic for CAVs at a Single- or Dual-Vehicle Level

In mixed traffic, a fundamental challenge is enabling a CAV to merge from an on-ramp into the main traffic flow, which consists of both CAVs and HDVs. This requires predicting HDV behavior and integrating these predictions into the CAV's motion planning strategy. 

Optimization-Based Methods: Optimization-based methods explicitly incorporate HDV behavior through assumptions and predictions. The most straightforward approach assumes that HDVs maintain a constant speed, which is then used to formulate an optimal control problem and determine the optimal merging trajectory for a CAV entering the main lane.[22,23] Model predictive control (MPC) has been widely used to account for uncertainties in HDV trajectories, treating them as disturbances. Even under the assumption of constant HDV speed[24,25] or short-term predictability (e.g., a few seconds),[26] MPC has been shown to effectively derive optimal merging decisions involving interactions between three vehicles (including one or two CAVs). 

Some studies have enhanced trajectory prediction by incorporating car-following models or machine learning techniques.[27-29] Jiang et al.[27] utilized the intelligent driver model (IDM) to describe HDV behavior when a CAV performs a lane change based on MPC. Han et al.[28] employed the Gipps car-following model to represent HDV merging maneuvers and optimize the merging profile of a single CAV. Karimi et al.[30] adopted the linear Helly model to predict HDV behavior and integrated it into an MPC framework, mitigating the effects of conservative HDV predictions and ensuring safe merging. Venkatesh et al.[29] trained an encoder-decoder model using the NGSIM dataset to predict HDV trajectories and incorporated these predictions into an MPC framework, improving the CAV's ability to avoid lateral collisions. 

Game theory has also been leveraged to model HDV-CAV interactions, as it provides a structured way to predict HDV behavior in response to CAV movements.[31,32] Jiang et al.[31] proposed a bilevel game-theoretic framework where the upper-level controller determines the merging strategy of the ramp CAV while interacting with main-lane vehicles (both HDVs and CAVs). The lower-level controller then predicts HDV trajectories 

based on IDM. Du et al.[32] classified HDV driving styles into three categories using a Gaussian mixture model-support vector machine approach and employed a pure-strategy Nash equilibrium to model HDV responses, ultimately optimizing the merging strategy of the ramp CAV based on HDV speed and spacing conditions. 

RL-based Methods: RL-based approaches allow agents to implicitly learn HDV behaviors and make high-level control decisions, such as acceleration, deceleration, and lane changes, for the target CAVs.[33-35] Although RL can inherently model HDV behavior, studies have shown that its performance improves when an explicit HDV intention estimation model is used as an input.[36] For example, in ref. [36] a probabilistic model predicts human drivers' intentions, which is then fed into an RL model to optimize the longitudinal acceleration of a ramp CAV. 

A major drawback of RL-based approaches is their lack of stability guarantees when deployed in real-world scenarios. To address this, several studies have incorporated safety filters to ensure robust decision-making. Methods such as control barrier function (CBF)-based safety filters[37,38] and MPC-based safety filters[39,40] have been applied to enhance safety and reliability in RL-based merging control strategies. 

# 1.2.2. Merging Control in Mixed Traffic for CAVs at a Multivehicle Level

The previous strategies primarily focused on interactions between a single ramp vehicle and its immediate neighbors, typically involving two or three vehicles (CAVs and HDVs). However, coordinating multiple CAVs in mixed traffic can further enhance overall traffic efficiency and safety in merging areas. Despite its potential benefits, relatively few studies have tackled this coordination problem using RL and optimization-based methods. 

RL-Based Methods: Multiagent RL (MARL) enables multiple CAVs to learn cooperative control strategies while implicitly modeling HDV behaviors. Similar to single-vehicle-level approaches, MARL-based methods optimize high-level control decisions, such as acceleration, deceleration, and lane changes, based on reward functions that prioritize collision avoidance and traffic efficiency. 

Valiente et al.[41] introduced a decentralized MARL framework in which each RL agent controls a single CAV, sharing learnt policies among agents. Their approach demonstrated adaptability to diverse HDV driving behaviors in scenarios with 4 CAVs and 18 HDVs. To improve scalability, Chen et al.[42] developed a centralized MARL framework with curriculum learning, effectively handling up to six CAVs and five HDVs while improving coordination in mixed traffic. 

To better model complex interactions in multilane on-ramp merging, Liu et al.[43] integrated graph structures into MARL, enhancing the generalization capability of RL policies across various traffic scenarios. Additionally, to improve social coordination between CAVs and human drivers, Toghi et al.[44] incorporated the concept of social value orientation into the reward function, enabling more human-like cooperative decision-making. 

Despite these advancements, MARL-based approaches still struggle to ensure complete collision avoidance. Zhang et al.[45] addressed this issue by refining MARL strategies to improve success rates in mixed merging scenarios, yet fully eliminating collision risks remains a challenge. 

Optimization-Based Methods: Optimization-based approaches aim to determine optimal control actions for multiple CAVs while maintaining real-time safety constraints. Le et al.[46] proposed an optimal control framework that computes time-optimal trajectories for CAVs in mixed traffic, using Newell's car-following model to predict HDV trajectories. To account for possible deviations in HDV behavior, the framework incorporates a CBF-based safety filter. However, since the trajectories are computed only once when a CAV enters the control zone, the framework cannot guarantee optimality if actual HDV behavior deviates from the predictions. 

Shi et al.[47] and Zhao and Yildirimoglu[48] explored sequence scheduling and motion planning in mixed traffic environments, where individual CAVs, CAV platoons, and mixed platoons coexist. Instead of explicitly predicting HDV trajectories, they incorporated HDVs into mixed platoons led by a CAV, modeling their behavior using standard car-following models. This approach allowed the focus to remain on optimizing CAV movements and merging strategies. However, the potential benefits of CAVs merging within other platoons were not considered, which could further enhance overall traffic efficiency. 

# 1.3. Contribution of the Article

This study explores a cooperative merging strategy for all CAVs within a control zone using an optimization approach. The literature review highlights the following limitations in existing works based on the optimization approach. 

Insufficient Consideration on the Dynamic Behavior of HDVs: Existing methods often predict HDV trajectories only once when CAVs enter the control zone[46] or incorporate HDVs in mixed platoons led by a CAV, ignoring their interactions with other CAVs.[47,48] HDV behavior can vary during merging scenarios and react to CAV actions, making it challenging to predict accurately. There is a need for an effective method that accounts for this dynamic behavior. 

Limited Consideration of Interactive Cooperation Among All CAVs: In some approaches, time-optimal trajectories for each CAV are determined sequentially based on their entry order into the control zone.[46] Others focus on platoon-level coordination,[47,48] excluding the possibility of individual vehicles merging within other Platoons. It is essential to consider interactions among all vehicles simultaneously to further enhance traffic efficiency. 

The novel contributions of this study, addressing the concerns identified in existing works, include the following. 

Leveraging CAVs' Strategic Influence on HDV Behavior. Instead of accurately predicting HDV behaviors, this approach considers HDVs as reactive agents to CAV actions, where HDV speeds are controlled by slowing down their preceding CAV. This strategy allows other CAVs on the adjacent road to merge ahead of the HDVs. 

Incorporating All CAVs in the Cooperation: The optimal slowdown pattern is determined by evaluating CAV throughput across various cooperation actions involving all CAVs. 

Adopting Dynamic Optimization: Recognizing that HDV behaviors can change in real time and may not be precisely controlled or predicted despite CAV influence, the optimization problem is solved dynamically each time a new vehicle enters the control zone. This approach effectively manages the variations in HDV behaviors. 

It is worth noting that the concept of strategic slowdown for CAVs was initially introduced in ref. [26]. However, the method in ref. [26] focused solely on facilitating the merging sequence of three or fewer vehicles and did not address the mitigation of HDV trajectory uncertainty, as it assumed HDV trajectories to be predictable. Additionally, the study employed a rule-based control approach for managing interactions. In contrast, the proposed method generalizes this concept by addressing its limitations, offering a more robust and flexible framework for mitigating HDV uncertainties while facilitating cooperative merging. 

# 1.4. Organization of the Article

The article is outlined as follows. Section 2 introduces the problem formulation. Section 3 provides the solutions to the proposed problems. The results are reported in Section 4. Section 5 concludes with an outlook on future work. 

# 2. Problem Formulation

# 2.1. Modeling Framework

The target problem is coordinating multiple CAVs, co-existing with HDVs, in a scenario where one main road and one on-ramp intersect at a merging point; see Figure 1. The control zone is defined as the area where a coordinator can monitor the movement of all vehicles, including both CAVs and HDVs, and transmit control signals to CAVs for cooperative merging. The merging zone is where the actual merging occurs. The following assumption applies to the merging process in this study. 

Assumption 1: All CAVs are controllable and free from control errors (e.g., communication delays and packet loss).[49] 

Assumption 2: Cooperative merging control is completed within the control zone by creating sufficient gaps between vehicles to safely pass through the merging point. 

This assumption implies that CAVs navigate through the merging zone using their own autonomous driving algorithms, ensuring no collisions with other vehicles due to the successful cooperative merging control. 

Let $\mathcal{N}(t) = \{1, \dots, N(t)\}$ be the set of vehicles present in the control zone at time $t$ , where $N(t)$ is the total number of vehicles. Let $\mathcal{A}(t) \subset \mathcal{N}(t)$ and $\mathcal{H}(t) \subset \mathcal{N}(t)$ be the sets of CAVs and HDVs, respectively. Vehicle index $i \in \mathcal{N}(t)$ is initialized based on the order of entry into the control zone, with the earliest being assigned the lowest number. Let $r_i$ be the road that vehicle $i \in \mathcal{N}(t)$ belongs to, 0 if vehicle $i$ is in the main road and 1 otherwise. The set $\mathcal{N}(t)$ is updated at every sample time, enabling 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/b35c47518d550740d071c0d3a8fd228f1ed52b4678769d4031f0e0fc5ef8c926.jpg)



Figure 1. Merging scenario with one main road and one on-ramp intersecting at a merging point. The yellow and blue areas represent the control zone and merging zone, respectively.


continuous tracking of vehicles entering and exiting the control zone. Note that HDVs may exit the control zone via lane changes when influenced by the strategic slowdown of preceding CAVs. 

The dynamics of vehicle $i$ in the control zone are described by a double-integrator model. 

$$
\dot {p} _ {i} (t) = v _ {i} (t)
$$

$$
\dot {v} _ {i} (t) = u _ {i} (t) \tag {1}
$$

where $p_i, \nu_i,$ and $u_i$ denote the longitudinal position, speed, and control input (acceleration) of the vehicle, respectively. Note that $p_i = 0$ is set to be the merging point. The control input is bounded by 

$$
u _ {\min } \leq u _ {i} (t) \leq u _ {\max } \tag {2}
$$

where $u_{\mathrm{min}} < 0$ and $u_{\mathrm{max}} > 0$ are the minimum and maximum control inputs given by the physical acceleration and braking limits of the vehicles. The speed limits are defined by 

$$
0 \leq v _ {i} (t) \leq v _ {\max } \tag {3}
$$

where $\nu_{\mathrm{max}} > 0$ is the maximum allowable speed. The coordinator determines the control inputs for the CAVs by considering these limits and then transmits them to the CAVs. In contrast, the control inputs for the HDVs are determined by their drivers, who may violate the upper-speed limit. 

To prevent a lateral collision between vehicle $i$ and all vehicles traveling on the adjacent road, a safe time gap $T_{\mathrm{lat}} > 0$ is required between their arrival times at the merging point as follows. 

$$
\left| T _ {i} - T _ {j} \right| \geq T _ {\text {l a t}}, \forall j \quad \text {s u c h} \quad r _ {j} \neq r _ {i} \tag {4}
$$

where $T_{i}$ and $T_{j}$ represent the arrival times of vehicles $i$ and $j$ at the merging point, that is, the time at which $p_{i}(T_{i}) = 0$ and $p_{j}(T_{j}) = 0$ . 

To prevent a rear-end collision between vehicle $i$ and its immediate preceding vehicle $j$ traveling on the same road, the following is generally imposed. 

$$
p _ {j} (t) - p _ {i} (t) \geq d _ {\min } + T _ {\min } v _ {i} (t), j = \max  \left\{k \mid r _ {k} = r _ {i}, k <   i \right\} \tag {5}
$$

where $d_{\min} > 0$ and $T_{\min} > 0$ are the minimum standstill distance and the minimum time headway. In this study, an alternative expression of constraint (5) is also presented as 

$$
T _ {i} - T _ {j} \geq T _ {\text {r e a r}}, j = \max  \left\{k \mid r _ {k} = r _ {i}, k <   i \right\} \tag {6}
$$

which is an equivalent form to constraint (4) with a safe time gap $T_{\mathrm{rear}} > 0$ and will ease the problem formulation in Section 2.2.1. The relationship of $T_{\mathrm{rear}} \leq T_{\mathrm{lat}}$ is recommended, considering lane change behavior within the merging zone. The control zone of the merging scenario presented in Figure 1 is re-expressed in the arrival time domain in Figure 2, where the arrival times of all vehicles are ideally coordinated to satisfy constraints (4) and (6), assuming the arrival time of vehicle 1 is accurately known. In the arrival time domain, vehicle index $i \in \mathcal{N}(t)$ is renumbered based on its arrival time, with the earliest arrival being assigned the lowest number. Note that the numbering of vehicles 3 and 4 is interchanged between in Figure 1 and 2. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/bb4c97ad18cf7b0299c0f24f1049ee03b90630b86ad17afaaf403b118de323b1.jpg)



Figure 2. Merging scenario presented in Figure 1 is re-expressed in the arrival time domain, where the arrival times of all vehicles are ideally coordinated to satisfy constraints (4) and (6), assuming the arrival time of vehicle 1 is accurately known.


# 2.2. Optimization Problem Formulation

This section presents a hierarchical optimization approach, dividing the optimal coordination problem into an upper-level (i.e., arrival time optimization) problem and a lower-level (energy-optimal control) problem. The overall optimization scheme is illustrated in Figure 3. The arrival time optimization determines the optimal values of the CAV arrival times at the current time $t_0$ (i.e., $T_i^*$ , $\forall i \in \mathcal{A}(t_0)$ ) to enhance traffic flow and avoid lateral and rear-end collisions. The energy-optimal control determines the optimal control input for each CAV at the current time (i.e., $u_i^*(t_0)$ , $\forall i \in \mathcal{A}(t_0)$ ) to reach the merging point at $T_i^*$ with minimum energy consumption. The hierarchical optimization utilizes the position and velocity information of all vehicles (i.e., $p_i(t_0)$ , $\nu_i(t_0)$ , $\forall i \in \mathcal{N}(t_0)$ ) provided by the coordinator. The formulations of the upper- and lower-level problems are presented in the following sections, respectively. 

# 2.2.1. Arrival Time Optimization Problem

The upper-level problem, that is, the arrival time optimization problem, is formulated as 

$$
\min  _ {T _ {i}, \forall i \in \mathcal {A} (t _ {0})} \sum_ {i \in \mathcal {N} (t _ {0})} T T D _ {i} ^ {2} \tag {7}
$$

subject to (1), (2), (3), (4), (6), $\forall i\in \mathcal{A}(t_0)$ 

This optimization considers the entire vehicle group $(i\in \mathcal{N}(t_0))$ by minimizing the sum of the squares of the travel time delays (TTDs) of all CAVs and HDVs. The TTD of vehicle $i$ is defined as 

$$
T T D _ {i} = T _ {i} - T _ {i} ^ {\mathrm {d e s}} \tag {8}
$$

where $T_{i}^{des}$ represents the desired arrival time, determined at the moment vehicle $i$ enters the control zone, and is given by 

$T_{i}^{\mathrm{des}} = \mathrm{Time}$ of vehicle $i$ entering the control zone 

$$
+ \frac {\text {C o n t r o l z o n e l e n g t h}}{\nu_ {\max }} \tag {9}
$$

The arrival time $T_{i}$ coincides with $T_{i}^{\mathrm{des}}$ when vehicle $i$ travels at the maximum speed $\nu_{\mathrm{max}}$ within the control zone, resulting in a zero TTD value. The TTD has been widely used as an objective function or performance metric in previous studies.[47,50,51] Constraint (6) is used instead of constraint (5) to describe this 

problem only using arrival times. The solution to Problem (7) is denoted by $T_{i}^{*}, \forall i \in \mathcal{A}(t_{0})$ . 

Problem (7) can be rewritten in vector form using the (desired) arrival time vector $\mathbf{T}_{\mathcal{X}}^{(\mathrm{des})}(t_0) = [T_i^{(\mathrm{des})}]_{\forall i\in \mathcal{X}(t_0)}$ , where $\mathcal{X} = \mathcal{N},\mathcal{A}$ and $\mathcal{H}$ , as follows. 

$$
\min  _ {\mathbf {T} _ {A} (t _ {0})} \left\| \mathbf {T} _ {\mathcal {N}} \left(t _ {0}\right) - \mathbf {T} _ {\mathcal {N}} ^ {\mathrm {d e s}} \left(t _ {0}\right) \right\| ^ {2} \tag {10}
$$

subject to $\mathbf{f}(\mathbf{T}_{\mathcal{A}}(t_0),\mathbf{T}_{\mathcal{H}}(t_0))\geq \mathbf{0}$ 

where $\mathbf{f}(\cdot, \cdot)$ represents the vector form of all constraints from problem (7). The rewritten form clearly demonstrates that the problem depends on the arrival times of the HDVs. However, the HDV arrival times are difficult to predict accurately and may vary according to the CAV arrival times (i.e., $\mathbf{T}_{\mathcal{H}}(t_0) = \mathbf{g}(\mathbf{T}_{\mathcal{A}}(t_0)))$ because the HDVs react to the CAV behavior. A solution to this problem should consider this interaction between the CAVs and HDVs and should not heavily depend on the prediction of the HDVs' future behavior. 

# 2.2.2. Energy-Optimal Control Problem

Upon determining the optimal arrival times of the CAVs (i.e., $T_{i}^{*}, \forall i \in \mathcal{A}(t_{0})$ ), the energy-optimal control is applied to each CAV $i \in \mathcal{A}(t_0)$ based on the following problem. 

$$
\min  _ {u _ {i} (t), t _ {0} \leq t \leq T _ {i} ^ {*}} \frac {1}{2} \int_ {t _ {0}} ^ {T _ {i} ^ {*}} u _ {i} ^ {2} (t) d t \tag {11}
$$

subject to (1), (2), (3), (5), $p_i(T_i^*) = 0$ , $u_i(T_i^*) = 0$ 

This optimization aims to control CAV $i$ to reach the merging point at optimal arrival time $T_{i}^{*}$ (i.e., $p_{i}(T_{i}^{*}) = 0$ ) with minimum control input effort (i.e., $u_{i}^{2}(t)$ ) and zero control input at the end (i.e., $u_{i}(T_{i}^{*}) = 0$ ) while satisfying the vehicle dynamics (1), control input and speed constraints (2) and (3), and avoiding a rear-end collision (5). Minimizing the control input effort is a common way to minimize energy consumption.[52] Note that (4) is not included in this lower-level problem because lateral collision prevention is considered in the determination of $T_{i}^{*}$ in the upper-level problem. 

Constraint (5) in problem (11) is difficult to rigorously address due to the challenges in accurately predicting the trajectory information of $p_j(t)$ when vehicle $j$ is an HDV. Therefore, a relaxed version of constraint (5) is introduced and used instead, as follows. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/b68198e59e416688123b2230191bbd17266a1f52a4df0442cd23491978856c58.jpg)



Figure 3. Schematic diagram of the proposed approach: a hierarchical optimization method that divides the optimal coordination problem into an upper-level (arrival time optimization) and a lower-level (energy-optimal control) problem.


$$
\begin{array}{l} p _ {j} \left(t _ {0} + t _ {\mathrm {s}}\right) - p _ {i} \left(t _ {0} + t _ {\mathrm {s}}\right) \geq d _ {\min } + T _ {\min } v _ {i} \left(t _ {0} + t _ {\mathrm {s}}\right), \tag {12} \\ j = \max  \left\{k \mid r _ {k} = r _ {i}, k <   i \right\} \\ \end{array}
$$

where $t_{\mathrm{s}}$ denotes the sampling time for the control process, which applies constraint (5) only at the next time step (i.e., $t_0 + t_{\mathrm{s}}$ ). 

In case none of the state constraints (3) and (12) and input constraint (2) are active, the unconstrained solution to problem (11) is presented in ref. [46] as follows. 

$$
u _ {i} ^ {\mathrm {u c}} \left(t _ {0} + \Delta t\right) = 6 a _ {i} \Delta t + 2 b _ {i} \tag {13}
$$

$$
\nu_ {i} ^ {\mathrm {u c}} \left(t _ {0} + \Delta t\right) = 3 a _ {i} (\Delta t) ^ {2} + 2 b _ {i} \Delta t + c _ {i} \tag {14}
$$

$$
p _ {i} ^ {\mathrm {u c}} \left(t _ {0} + \Delta t\right) = a _ {i} (\Delta t) ^ {3} + b _ {i} (\Delta t) ^ {2} + c _ {i} \Delta t + d _ {i} \tag {15}
$$

where the superscript uc denotes the unconstrained solution, and the coefficients $a_{i}, b_{i}, c_{i}$ , and $d_{i}$ are given by 

$$
\begin{array}{l} \left[ \begin{array}{l} a _ {i} \\ b _ {i} \\ c _ {i} \\ d _ {i} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ \left(T _ {i} ^ {*} - t _ {0}\right) ^ {3} & \left(T _ {i} ^ {*} - t _ {0}\right) ^ {2} & \left(T _ {i} ^ {*} - t _ {0}\right) & 1 \\ 6 \left(T _ {i} ^ {*} - t _ {0}\right) & 2 & 0 & 0 \end{array} \right] ^ {- 1} \left[ \begin{array}{c} p _ {i} \left(t _ {0}\right) \\ v _ {i} \left(t _ {0}\right) \\ 0 \\ 0 \end{array} \right] (16) \\ = \left[ \begin{array}{c} \frac {p _ {i} \left(t _ {0}\right)}{2 \left(T _ {i} ^ {*} - t _ {0}\right) ^ {3}} + \frac {v _ {i} \left(t _ {0}\right)}{2 \left(T _ {i} ^ {*} - t _ {0}\right) ^ {2}} \\ - \frac {3 p _ {i} \left(t _ {0}\right)}{2 \left(T _ {i} ^ {*} - t _ {0}\right) ^ {2}} - \frac {3 v _ {i} \left(t _ {0}\right)}{2 \left(T _ {i} ^ {*} - t _ {0}\right)} \\ v _ {i} \left(t _ {0}\right) \\ p _ {i} \left(t _ {0}\right) \end{array} \right] (17) \\ \end{array}
$$

The solution to problem (11), considering the state and control input constraints, will be presented in Section 3.2. 

# 3. Solutions to Optimization Problems

Solutions to the arrival time optimization problem and the energy-optimal control problem are proposed in Sections 3.1 and 3.2, respectively. 

# 3.1. Solution to Arrival Time Optimization Problem

Problem (7) (or equivalently, problem (10)) is easily solved when all vehicles in the control zone are CAVs; see Figure 4a. The optimal solution to problem (7) is simply to assign the minimum time gap $T_{\mathrm{lat}}$ or $T_{\mathrm{rear}}$ between consecutive vehicles, unless constraints (2) or (3) become active. However, when CAVs coexist with HDVs, it is difficult to immediately assign optimal arrival times due to the uncertain intentions of the HDVs; see Figure 4b. The arrival times of CAVs 2, 3, and 4 can be determined to have the minimum time gap $T_{\mathrm{safe}}$ between consecutive vehicles, assuming the arrival time of HDV 1 is accurately known. In contrast, the arrival times of CAVs 6 and 7 cannot be immediately determined due to the uncertain future intentions (equivalently, arrival times) of HDVs 5 and 8. Many previous studies, including refs. [29,36,46,53], have predicted the future trajectories or intentions of HDVs to mitigate uncertainty in optimization; 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/fbfc85595611f8f2590584fbbd1dbfc523e9a10a6fdfe4162cbd4bde9b6661c3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/9a144f42d1f8ac88243bf7dbb012d0389e57cd0e40418a01c0b0ee75c58c9652.jpg)



Figure 4. Example merging scenarios. a) When all vehicles in the control zone are CAVs, the optimal solution to Problem (7) is to assign the minimum time gap $T_{\mathrm{lat}}$ or $T_{\mathrm{rear}}$ between consecutive vehicles (unless constraints (2) or (3) become active). b) When CAVs coexist with HDVs, it is difficult to immediately assign optimal arrival times due to the uncertain intentions of the HDVs.


however, accurately predicting human driver maneuvers remains challenging. 

In this study, a novel approach is presented where HDV arrival times are controlled by slowing down their preceding CAVs, causing the HDV drivers to slow down as well to maintain a safe time gap $(\geq T_{\mathrm{rear}})$ in arrival times with the vehicles ahead. This strategy allows other CAVs on the adjacent road to merge ahead of the HDVs. This strategic influence on HDV behavior is achieved through cooperation among the CAVs, which is described in Figure 5. As shown in Figure 5a, groups of consecutive CAVs on each road (CAVs 2 and 4, and CAVs 3, and 6, 7) can form a cooperation candidate set c. In this cooperation candidate set, CAV 4 serves as the strategic CAV, and its strategic slowdown determines the cooperative pattern. If the strategic CAV does not choose to slow down, as shown in Figure 5b (Pattern 0), CAVs 2, 3, and 4 form the cooperation group C, which can adjust their arrival times to maintain the minimum time gap $T_{\mathrm{lat}}$ or $T_{\mathrm{rear}}$ between them. However, CAVs 6 and 7 form the noncooperation group N, which must find their arrival times to avoid lateral collisions with HDVs 5 and 8. This pattern is the same as in Figure 4b. If the strategic CAV chooses to slow down to have a later arrival time than CAV 6, as shown in Figure 5c (Pattern 1), then CAV 6 is also included in C and can merge ahead of the HDVs. In this case, only CAV 7 remains in N and needs to avoid lateral collisions with the HDVs. If the strategic CAV further slows down to have a later arrival time than even CAV 7, as shown in Figure 5d (Pattern 2), then CAV 7 is also included in C and can merge ahead of the HDVs. In this case, the strategic CAV would then belong to N and needs to avoid lateral collisions with the HDVs following CAV 7 (e.g., HDV 9 in this figure). The best cooperative pattern will be determined by evaluating the objective function of Problem (7) for each pattern and selecting the one with the minimum objective function value. Although Pattern 1 or 2 may be a better solution than Pattern 0 because more CAVs are included in C, the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/188eb35dad48991a947b7689b85c8f2a7499325c27f83dbc7bba88ed7b1d8c37.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/6c16fb3c8b26c0996c20a00c06709d0b876a51abcbca48759485b729516d3f3c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/63532cb0eb50193da2bac0d1f7c9e54dafd991e23ecb09e7ae2d5af3199bd730.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/7269ba5bbe0b9603593d3a668fe0649f28a9ac3d3cfda64a628d49b057228246.jpg)



Figure 5. Description of cooperation candidate set c, cooperation group C, noncooperation group N, strategic CAV, and strategic slowdown. a) Groups of consecutive CAVs on each road can form a cooperation candidate set c. b) Pattern 0: Strategic CAV does not choose to slow down. c) Pattern 1: Strategic CAV chooses to slow down to have a later arrival time than CAV 6. d) Pattern 2: Strategic CAV further slows down to have a later arrival time than even CAV 7.


strategic slowdown of CAV 4 may increase the objective function. Therefore, the objective function must be evaluated for every pattern. 

The detailed procedure for solving problem (7) based on the proposed approach is explained step by step as follows. 

Initialize the arrival times for all vehicles considering constraints (1), (2), (3), and (6). 

Initial values of the arrival times for both CAVs and HDVs are required before evaluating the cooperative patterns. To this end, the vehicle indices $i \in \mathcal{N}(t_0)$ are first initialized based on their order of entry into the control zone. Next, approximated arrival times are calculated without considering any collisions with other vehicles; these times are referred to as unconstrained arrival times (i.e., $T_i^{\mathrm{uc}}$ ); see Figure 6a. The unconstrained arrival times for CAVs are calculated by determining the unconstrained optimal speed profile (14) that reaches the merging point at $T_i^{\mathrm{uc}}$ (i.e., $p_i(T_i^{\mathrm{uc}}) = 0$ ) with the maximum speed at the end (i.e., $\nu_i(T_i^{\mathrm{uc}}) = \nu_{\mathrm{max}}$ ), as follows. 

$$
T _ {i} ^ {\mathrm {u c}} = t _ {0} + \frac {- 3 p _ {i} \left(t _ {0}\right)}{2 v _ {\max } + v _ {i} \left(t _ {0}\right)}, \forall i \in \mathcal {A} \left(t _ {0}\right) \tag {18}
$$

If this $T_{i}^{\mathrm{uc}}$ is unattainable within the control input and speed constraints (2) and (3), it should be adjusted to be no less than the value obtained under the assumption of maximum acceleration $(u(t) = u_{\mathrm{max}})$ until the speed reaches its maximum value $\nu_{\mathrm{max}}$ , after which it maintains this speed up to the merging point. This adjustment ensures that constraints (1), (2), and (3) are satisfied. The unconstrained arrival times for HDVs are calculated based on the constant speed assumption (i.e., $\nu_{i}(t) = \nu_{i}(t_{0})$ for $t > t_{0}$ ) as follows. 

$$
T _ {i} ^ {\mathrm {u c}} = t _ {0} + \frac {0 - p _ {i} \left(t _ {0}\right)}{v _ {i} \left(t _ {0}\right)}, \forall i \in \mathcal {H} \left(t _ {0}\right) \tag {19}
$$

The validity of the constant speed assumption is discussed in Remark 1. 


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/6191fbd69dc834e81aaffc776cc98a881cb1d7755d13dc57df6951e198e5d305.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/f7a5751ecc3d2d86f6adc1cf9018b5e16cd54f3b7ba3f0df0910e12e6cd6c6c4.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/d07c03633788b351a1ff9c20934e0e4c31612aa780982525879ef823e2d6697f.jpg)



Figure 6. Initialization of arrival times. a) Calculation of unconstrained arrival times. b) Initialization of arrival times. c) Renumbering vehicle indices in ascending order of arrival times. The numbering of vehicles 2 and 4, as well as vehicles 7 and 8, is interchanged between (b,c).


Then, the initial values of $T_{i}$ are obtained by sequentially adjusting the unconstrained arrival times to satisfy constraint (6) as follows. 

$$
T _ {i} \leftarrow \max  \left(T _ {i} ^ {\mathrm {u c}}, T _ {j} + T _ {\text {r e a r}}\right) \tag {20}
$$

in increasing order of $i$ , where $j = \max \{k|r_k = r_i,k < i\}$ represents the index of the immediate preceding vehicle traveling on the same road; refer to Figure 6b. The initial values of $T_{i}$ obtained through this process satisfy the rear-end collision constraint (6). 

Finally, renumber the vehicle indices in ascending order of arrival times $T_{i}$ , so that the lowest index corresponds to the earliest arrival time and has the priority in computing the optimal arrival times; refer to Figure 6c. Additionally, define a new variable $s_i$ for each CAV, representing the optimization status, where $s_i = 1$ if the optimization is completed and $s_i = 0$ otherwise. Initialize all $s_i$ to 0. 

Optimize the arrival times sequentially in ascending order of vehicle index, minimizing the objective function while accounting for constraints (4) and (6): 

Starting with the CAV that has the lowest vehicle index (i.e., the highest priority) with $s = 0$ (indicating it has not yet been optimized), the arrival times of the CAVs are sequentially optimized to achieve their minimum feasible value (thereby minimizing the objective function) while ensuring that constraints 

(4) and (6) are satisfied. This process is repeated for each CAV in ascending order of priority. Let $i$ be the current CAV being updated. First, determine the cooperation flag $\text{Flag}_c$ , which indicates whether cooperation between CAV $i$ and other CAVs is required (1) or not (0). To determine this, define the lateral collision candidates for CAV $i$ as 

$$
\mathbf {l} _ {i} = \{k \mid r _ {k} \neq r _ {i}, k <   \min  \{j \in \mathcal {A} (t _ {0}) \mid r _ {j} \neq r _ {i}, j > i, s _ {j} = 0 \} \} \tag {21}
$$

This set includes the first consecutive HDVs and CAVs with completed optimization ( $s = 1$ ) on the adjacent road. CAVs on the adjacent road with indices higher than $i$ and not yet optimized are excluded from the candidate set, as they can be controlled later to avoid lateral collisions. Five cases are considered to determine $\text{Flag}_c$ , as illustrated in Figure 7. 

Case 1: No vehicle is present on the adjacent road (see Figure 7a where $i = 4$ ). In this case, cooperation is not needed, so set Flagc to 0. 

Case 2: The vehicles on the adjacent road consist solely of HDVs and/or CAVs whose optimizations are completed $(s = 1)$ ; see Figure 7b where $i = 4$ . In this case, cooperation is not required, and Flagc is set to 0. However, CAVs on the same road as CAV $i$ must be optimized to avoid lateral collisions with the HDVs and/or optimized CAVs on the adjacent road. The arrival time of CAV $i$ is optimized by solving 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/a5fcd7988123cf39d1800fc3af1d4cd8029da86169d1f0d376242e142933a03b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/4a15dbab3721707364e4d8d1bc2fd3762ddf84cb0dba5f63ccf5ba0a2d92895d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/ff65299ca3293cd65a46ffe1b7533735c4ed5b4b3143bb045525eeedac40d8a5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/453ba05a70550587928e9ec5d121e97599743fd322ac1f8438e12edf999b67f6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/48ba496a2c7d3fde6793ed53c5360859d7ef26d480d96bdf62bbb3f6d25545a9.jpg)



Figure 7. Five cases considered in determining the cooperation flag $\mathsf{Flag}_c$ : a) Case 1 with $\mathsf{Flag}_c = 0$ , b) Case 2 with $\mathsf{Flag}_c = 0$ , c) Case 3a with $\mathsf{Flag}_c = 0$ , d) Case 3b with $\mathsf{Flag}_c = 1$ , and e) Case 4 with $\mathsf{Flag}_c = 1$ .


$T_{i}\gets \min T$ subject to $T\geq T_{i},\quad |T - T_{j}|\geq T_{\mathrm{lat}},\forall j\in \mathbf{l}_{i}$ (22) 

The first constraint in (22) ensures that $T_{i}$ does not decrease below its initial value, while the second constraint enforces the lateral collision avoidance requirement as defined in (4). If $T_{i}$ increases from its initial value, the arrival times of the vehicles following CAV $i$ on the same road must be adjusted to maintain the rear-end collision constraint (6) as follows. 

$$
\begin{array}{l} T _ {k} \leftarrow \max  \left(T _ {k}, T _ {j} + T _ {\text {r e a r}}\right), \quad \forall j \quad \text {a n d} \quad \forall k \quad \text {s u c h t h a t} \tag {23} \\ r _ {i} = r _ {k} = r _ {j} \quad \text {a n d} \quad i <   j <   k \\ \end{array}
$$

Case 3: The vehicles on the adjacent road begin with an HDV or a CAV whose optimization is completed $(s = 1)$ and include at least one not-yet-optimized CAV $(s = 0)$ further along. In this case, first, optimize the arrival time of CAV $i$ to avoid lateral collisions with the lateral collision candidates $\mathbf{l}_i$ , which includes the first HDV or optimized CAV, using (22). 

* Case 3a: The updated value of $T_{i}$ is smaller than the maximum arrival time of $\mathbf{l}_i$ (i.e., CAV $i$ arrives at the merging point before the vehicle with the highest index in $\mathbf{l}_i$ ). In this case, CAV $i$ does not affect the CAVs with higher indices (i.e., those with later arrival times than $T_{i}$ ); see Figure 7c where $i = 4$ . Set $\mathrm{Flag}_{\mathrm{c}} = 0$ . If $T_{i}$ increases from its initial value, the arrival times of the vehicles following CAV $i$ on the same road must be adjusted to maintain the rear-end collision constraint, as described in Equation (23). 

* Case 3b: $T_{i}(t) > T_{j}(t)$ for all $j \in \mathbf{l}_i$ (i.e., CAV $i$ arrives at the merging point after all vehicles in $\mathbf{l}_i$ ). In this case, cooperation between CAV $i$ and some CAVs with higher indices needs to be considered; see Figure 7d where $i = 4$ . Set Flag to 1. 

Case 4: The first vehicle on the adjacent road is a CAV that has not yet been optimized. Cooperation between CAVs including this CAV and CAV $i$ needs to be considered; see Figure 7e. Set $\mathsf{Flag}_{\mathsf{c}}$ to 1 where $i = 1$ . 

If $\mathsf{Flag}_{\mathsf{c}} = 0$ , terminate the optimization for CAV $i$ by setting $s_i$ to 1 and proceed to the next CAV in order of priority. Otherwise, the following process is conducted to facilitate cooperation between CAV $i$ and its nearby CAVs. 

First, define the cooperation candidate sets for each road as follows. 

$$
\mathbf {c} ^ {s} := \left\{k \in \mathcal {A} \left(t _ {0}\right) \mid r _ {k} = r _ {i}, i \leq k <   \min  \left\{j \in \mathcal {H} \left(t _ {0}\right) \mid r _ {j} = r _ {i}, T _ {j} \geq T _ {i} \right\} \right\} \tag {24}
$$

$$
\mathbf {c} ^ {a} := \left\{k \in \mathcal {A} \left(t _ {0}\right) \mid r _ {k} \neq r _ {i}, i <   k <   \min  \left\{j \in \mathcal {H} \left(t _ {0}\right) \mid r _ {j} \neq r _ {i}, T _ {j} \geq T _ {i} \right\} \right\} \tag {25}
$$

where $\mathbf{c}^{\mathrm{s}}$ and $\mathbf{c}^{\mathrm{a}}$ represent the cooperation candidate sets on the same road as CAV $i$ ( $r_k = r_i$ ) and the adjacent road ( $r_k \neq r_i$ ), respectively. Each set includes the first group of consecutive CAVs on each road with indices equal to or higher than $i$ . The overall cooperation candidate set $\mathbf{c}$ is defined as 

$$
\mathbf {c} := \operatorname {s o r t} \left(\mathbf {c} ^ {s} \cup \mathbf {c} ^ {a}\right) \tag {26}
$$

with elements sorted in ascending order. 

Three cooperation modes exist, as described below, with illustrations in Figure 8. 

Mode 1: The cooperation candidate set $\mathbf{c}$ does not have any following HDVs on either roads; see Figure 8a where $i = 2$ and $\mathbf{c} = \{2,3,4,5,6\}$ . In this case, the cooperation problem is straightforward, and no strategic CAV is needed. All CAVs in $\mathbf{c}$ form the cooperation group $\mathbf{C}$ (i.e., $\mathbf{C} := \mathbf{c}$ ). Optimize the arrival times of the cooperation group $\mathbf{C}$ to avoid lateral and rear-end collisions within the group, prioritizing in ascending order of their positions in the group, as follows. 

$$
T _ {\mathbf {C} [ k + 1 ]} \leftarrow \max  \left(T _ {\mathbf {C} [ k + 1 ]}, T _ {\mathbf {C} [ k ]} + T _ {\mathrm {l a t / r e a r}}\right), \quad k = 1, 2, \dots \tag {27}
$$

Mode 2: The cooperation candidate set $\mathbf{c}$ has following HDVs on only one of the main or ramp roads, and the CAV immediately preceding these HDVs has a higher index than all CAVs in $\mathbf{c}$ on the adjacent road; see Figure 8b where $i = 2$ and $\mathbf{c} = \{2,3,4,5\}$ . In this case, this CAV acts as the strategic CAV by having the largest arrival time among $\mathbf{c}$ , allowing the vehicles following the strategic CAV to be disregarded in the optimization. The optimal solution to the cooperation problem mirrors Mode 1 once the vehicles following the strategic CAV are ignored. With $\mathbf{C} = \mathbf{c}$ , optimize the arrival times of the cooperation group $\mathbf{C}$ using the same method as Mode 1 in (27). Finally, adjust the arrival times of the vehicles following $\mathbf{C}$ to avoid rear-end collisions with their preceding vehicles, as the arrival times of $\mathbf{C}$ may increase during the optimization process, as follows. 

$$
\begin{array}{l} T _ {k} \leftarrow \max  \left(T _ {k}, T _ {j} + T _ {\text {r e a r}}\right), \quad \forall k > \max  (\mathbf {C}), \tag {28} \\ j = \max  \{m \mid r _ {m} = r _ {k}, m <   k \} \\ \end{array}
$$

Mode 3: This is the most common scenario, where $\mathbf{c}$ has following HDVs on either one or both roads, and the CAV immediately preceding the HDVs has a lower index than at least one CAV in $\mathbf{c}$ on the adjacent road; see Figure 8c,d. In this mode, only some CAVs in $\mathbf{c}$ form the cooperation group $\mathbf{C}$ , while the others 


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/be728e1930aa80c24c9f06a5dcc45d557ce4fd824e8e5ad760dc254f3834ea24.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/07258148a7af8e8cd43a5e8ecbef2b40d047ba22ad4d731658066c8baeec63f0.jpg)


constitute the noncooperation group $\mathbf{N}$ . Among the two CAVs with the highest indices in $\mathbf{c}$ on each road, the one with the lower index serves as the strategic CAV, indexed as $n$ . Let $q$ be the number of CAVs in $\mathbf{c}$ with indices greater than $n$ . These $q$ CAVs comprise $\mathbf{N}$ , while the remaining belong to $\mathbf{C}$ . The composition of $\mathbf{C}$ and $\mathbf{N}$ depends on the strategic slowdown of the strategic CAV, which can occur in $q + 1$ patterns, including no slowdown and incrementally delaying the strategic CAV to a greater arrival time than each of the $q$ CAVs. The position of the strategic CAV within this sorted set $\mathbf{c}$ is given by $p \coloneqq \operatorname{argmax}_i (\mathbf{c}[i] = n)$ , indicating the index $p$ where the strategic CAV (with index $n$ ) is located within $\mathbf{c}$ . Refer Figure 9a for a detailed description of these definitions. 

The strategic slowdown patterns are evaluated to find the optimal scenario with the lowest objective function value by incrementally shifting the strategic CAV's position within c. For each increment $l$ , the cooperation candidate set is rearranged as follows. 

$$
\begin{array}{l} \mathbf {c} \leftarrow \operatorname {s o r t} (\mathbf {c}), \quad \operatorname {t e m p} \leftarrow \mathbf {c} [ p ], \quad \mathbf {c} [ p: p + l - 1 ] \leftarrow \mathbf {c} [ p + 1: p + l ], \tag {29} \\ \mathbf {c} [ p + l ] \leftarrow \text {t e m p} \\ \end{array}
$$

The cooperation group $\mathbf{C}$ includes the CAVs in $\mathbf{c}$ that can merge ahead of the HDVs following $\mathbf{c}$ due to the strategic slowdown, comprising CAVs positioned lower in $\mathbf{c}$ than the strategic CAV and the strategic CAV itself, unless it is the last in the set. The cooperation group $\mathbf{C}$ can coordinate their arrival times independently of the HDVs that follow them. The noncooperation group $\mathbf{N}$ includes the remaining CAVs in $\mathbf{c}$ , which must consider lateral collisions with nearby HDVs when setting their arrival times. The groups are defined as follows. 

$$
\begin{array}{l} \mathbf {C} := \mathbf {c} [ 1: \min  (p + l, p + q - 1) ], \tag {30} \\ \mathbf {N} := \mathbf {c} [ \min  (p + l + 1, p + q): p + q ] \\ \end{array}
$$

Refer Figure 9b for a description of the above definitions. 

Next, optimize the arrival times of the cooperation group $\mathbf{C}$ to prevent lateral and rear-end collisions within the group, prioritizing the optimization in ascending order of their positions 


(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/563a6e35572972ca2f967e368401bd136b0304bf58bed0ca7506ba925a9ce142.jpg)



(d)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/3656905ed1337e287b5dee6197fdfbf03bfd8d6009c72aa090dc01163aa7f68a.jpg)



Figure 8. Three cooperation modes exist: a) Mode 1, b) Mode 2, and c,d) Mode 3.



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/9c67e473eda6118e863f7e6c431becbe4f8d813ddfcbcb82960ee1a7925bad08.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/36f6334ce07059a7b3b015556dbfb85603989aefbd0f610a08f13b2bc88b0135.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/c849f626112c61fdee92b549d88d42b8ceefc4f8c9ae26c86db30dbef1d1aca9.jpg)



(d)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/6992142209f8ba2fec4301543ae1a4d76fa79d04a6046417d4e77b706b165a09.jpg)



Figure 9. Description of the optimization process in Mode 3. a) Definitions of $c, n, q,$ and $p,$ b) Definitions of rearranged $\mathbf{c}$ , $\mathbf{C}$ , and $\mathbf{N}$ for a 1-position increment of the strategic CAV in the set $\mathbf{c}$ (i.e., $l = 1$ ). c) Description of optimizing the cooperation group $\mathbf{C}$ and adjusting the vehicles following $\mathbf{C}$ for the slowdown pattern depicted in (b). d) Description of optimizing the noncooperation group $\mathbf{N}$ and adjusting the vehicles following $\mathbf{N}$ for the slowdown pattern depicted in (b).


using Equation (27). Due to the optimization process, the arrival times of C may increase, necessitating adjustments to the arrival times of vehicles following the cooperation group (both CAVs and HDVs) to maintain rear-end collision constraints. This adjustment is performed using Equation (28). Similar to the control of HDV arrival times through strategic slowdown, these adjustments treat HDV arrival times as controllable variables. 

Refer Figure 9c for detailed illustrations of optimizing the cooperation group C and adjusting the arrival times of vehicles following C. 

The arrival times of the noncooperation group $\mathbf{N}$ are optimized to avoid lateral collisions within nearby HDVs, prioritizing the optimization in the order of their positions within the group, as follows. 

$$
\begin{array}{l} T _ {\mathbf {N} [ k ]} \leftarrow \min  T \quad \text {s u b j e c t t o} \quad T \geq T _ {\mathbf {N} [ k ]}, \quad | T - T _ {j} | \geq T _ {\mathrm {l a t}}, \tag {31} \\ k = 1, 2, \dots , \quad \forall j \in \mathbf {l} _ {\mathbf {N} [ k ]} \\ \end{array}
$$

Subsequently, adjust the arrival times of the vehicles following $\mathbf{N}$ to prevent rear-end collisions with their preceding vehicles, as the arrival times of $\mathbf{N}$ may increase during the optimization process. 

$$
\begin{array}{l} T _ {k} \leftarrow \max  \left(T _ {k}, T _ {j} + T _ {\text {r e a r}}\right), \quad \forall k > \max  (\mathbf {N}), \tag {32} \\ j = \max  \{m \mid r _ {m} = r _ {k}, m <   k \} \\ \end{array}
$$

Refer Figure 9d for a detailed description of optimizing the noncooperation group $\mathbf{N}$ and rearranging the arrival times of the vehicles that follow $\mathbf{N}$ . 

Save the outcome of this optimization and adjustment process for the current increment $l$ as $\mathbf{T}_{\mathcal{N}}^{(l)}(t_0) = [T_i]_{\forall i \in \mathcal{N}(t_0)}$ . Repeat this process for all increments (i.e., all strategic slowdown patterns). 

Identify the optimal slowdown pattern by finding $l^{*} = \arg \min_{l}\| \mathbf{T}_{\mathcal{N}}^{(l)}(t_0) - \mathbf{T}_{\mathcal{N}}^{\mathrm{des}}(t_0)\| ^2$ , and set the optimal arrival times as $[T_i^* ]_{\forall i\in \mathcal{N}(t_0)}\gets \mathbf{T}^{(l^*)}$ . 

Mark the completion of the optimization for all $k \in \mathbf{c}$ by setting $s_k = 1$ . The CAVs not included in the cooperation candidate $\mathbf{c}$ will be optimized subsequently, as they can be identified by $s = 0$ . The validity of this sequential optimization approach is further discussed in Remark 2. 

# Determine the optimal arrival times:

The optimal arrival times for all CAVs (i.e., $[T_i^*]_{\forall i \in A(t_0)}$ ) are determined sequentially in ascending order of priority. These optimal arrival times are then used as the output of the arrival time optimization problem and serve as inputs to the subsequent energy-optimal control problem. This dynamic optimization (DO) process should be repeated each time a new vehicle enters the control zone. 

The procedure described above is outlined in Algorithm 1. Note that the strategic slowdown is applied only when it is determined to effectively facilitate overall traffic flow, based on the criteria outlined in Algorithm 1. 

Remark 1 (Validity of the constant speed assumption for HDVs): 

The constant speed assumption is used to calculate the unconstrained arrival time for HDVs, as shown in (19). Although this assumption may oversimplify the uncertainties associated with HDVs, two key elements in the proposed strategy help validate its use. First, the simple calculation in (19) is bounded by rear-end collision constraints, as seen in (20), (28), and (32). These are physics-based constraints that even human drivers are expected to adhere to when controlling their vehicles. Second, the proposed strategy employs DO, where the optimization problem is repeated at every current time $t_0$ . The constant speed assumption becomes increasingly accurate as HDVs approach the merging point. 

# Remark 2 (Validity of the sequential optimization)

Ideally, solving Problem (7) would yield the optimal arrival times for all CAVs simultaneously; however, this direct approach is impractical due to the uncertainties associated with HDVs. Therefore, this study employs a sequential optimization 

approach, prioritizing CAVs closer to the merging point. This method is justified for two reasons. First, the uncertainties in HDV movement decrease as vehicles approach the merging point, as discussed in Remark 1, enhancing overall optimality when focusing on CAVs with lower associated uncertainties. Second, CAVs near to the merging point have less time to adjust their maneuvers to avoid collisions, necessitating higher priority in the optimization process. $\diamond$ 

# 3.2. Solution to Energy-Optimal Control Problem

The unconstrained solution to problem (11) was presented in (13). Because constraint (3) was already considered in the arrival time optimization problem when calculating the unconstrained arrival time $T_{i}^{\mathrm{uc}}$ , only the input constraint (2) and the relaxed rear-end collision constraint (12) need to be further addressed. 

Constraint (12) can be reformulated as an input constraint when translated into the discrete time domain. The position and speed of vehicle $i$ are expressed as 

$$
p _ {i} \left(t _ {0} + t _ {s}\right) = p _ {i} \left(t _ {0}\right) + t _ {s} v _ {i} \left(t _ {0}\right) + \frac {1}{2} t _ {s} ^ {2} u _ {i} \left(t _ {0}\right) \tag {33}
$$

$$
v _ {i} \left(t _ {0} + t _ {s}\right) = v _ {i} \left(t _ {0}\right) + t _ {s} u _ {i} \left(t _ {0}\right) \tag {34}
$$

The position of vehicle $j$ is obtained under the constant speed assumption 

$$
p _ {j} \left(t _ {0} + t _ {s}\right) = p _ {j} \left(t _ {0}\right) + t _ {s} v _ {j} \left(t _ {0}\right) \tag {35}
$$

By substituting (33), (34), and (35) into (12), the following input constraint is derived 

$$
\begin{array}{l} u _ {i} (t _ {0}) \leq \frac {p _ {j} (t _ {0}) - p _ {i} (t _ {0}) + t _ {\mathrm {s}} (v _ {j} (t _ {0}) - v _ {i} (t _ {0})) - d _ {\min } - T _ {\min } v _ {i} (t _ {0})}{T _ {\min } t _ {\mathrm {s}} + t _ {\mathrm {s}} ^ {2} / 2} \\ := u _ {\text {s a f e}} \left(t _ {0}\right) \tag {36} \\ \end{array}
$$

Next, the effect of the input constraint (2) on the unconstrained solution $u_{i}^{\mathrm{uc}}(t_{0} + \Delta t) = 6a_{i}\Delta t + 2b_{i}$ is analyzed. This solution starts with a positive or negative value at $t_0$ and linearly decreases or increases to 0 at $T_{i}^{*}$ . As shown in Figure 10, when the input constraint (2) becomes active, the constrained solution must be bounded within the constraint during the time interval where the unconstrained solution would violate it. The magnitude of the solution should be increased during the remaining time to compensate for the limitation. Therefore, the constrained solution at $t_0$ considering the input constraint (2) is obtained by bounding the unconstrained solution value at $t_0$ within the constraint, as follows 

$$
u _ {i} ^ {*} \left(t _ {0}\right) \leftarrow \min  \left(\max  \left(u _ {i} ^ {u c} \left(t _ {0}\right), u _ {\min }\right), u _ {\max }\right) \tag {37}
$$

Finally, the constrained solution must also be bounded again within the reformulated rear-end collision constraint (36) as follows. 

$$
u _ {i} ^ {*} \left(t _ {0}\right) \leftarrow \min  \left(u _ {i} ^ {*} \left(t _ {0}\right), u _ {\text {s a f e}} \left(t _ {0}\right)\right) \tag {38}
$$


Algorithm 1. Solution to arrival time optimization problem.


1 for Each time $t_0$ , if a new vehicle enters the control zone, do   
2 Input: Vehicle indices ordered by their entry into the control zone, along with position $p_i(t_0)$ and speed $v_{i}(t_{0})$ for all $i\in \mathcal{N}(t_0)$ 3 for each vehicle $i = 1,2,\ldots ,N(t_0)$ do   
4 Compute the unconstrained arrival time of vehicle $i$ $(T_{i}^{uc})$ using (18) or (19). Initialize the arrival time of vehicle $i$ $(T_{i})$ using (20).   
5   
6 Renumber the vehicle indices in ascending order of $T_{i}$ 7 Set $s_i\gets 0,\forall i\in \mathcal{N}(t_0)$ 8 for each $i\in \mathcal{A}(t_0)$ such that $s_i = 0$ , in ascending order of vehicle index do   
9 Determine the cooperation status Flagc by identifying the case to which the current scenario belongs to among Case 1, Case 2, Case 3a, Case 3b, and Case 4. if Flagc $= 0$ then Set $s_i\gets 1$ . else   
13 Define the cooperation candidate set c using (24), (25), and (26). Identify the cooperation mode. switch Cooperation mode case Mode 1 Define the cooperation group as $\mathbf{C} = \mathbf{c}$ Optimize the arrival times of C using (27). case Mode 2 Define the cooperation group as $\mathbf{C} = \mathbf{c}$ Optimize the arrival times of C using (27). Adjust the arrival times of the vehicles following C using (28).   
case Mode 3 Calculate $n,q$ and $p$ for $l = 0,1,\dots ,q$ do Rearrange the cooperation candidate set c using (29). Define the cooperation group C and non-cooperation group N using (30). Optimize the arrival times of C using (27). Adjust the arrival times for the vehicles following C using (28). Optimize the arrival times of N using (31). Rearrange the arrival times for the vehicles following N using (32). Store the result of the optimization and adjustment process as $\mathbf{T}_{\mathcal{N}}^{(l)}(t_0) = [T_i]_{\forall i\in \mathcal{N}(t_0)}$ Find the optimal result by $l^{*} = \arg \min_{l}\left\| \mathbf{T}_{\mathcal{N}}^{(l)}(t_0) - \mathbf{T}_{\mathcal{N}}^{des}(t_0)\right\| ^2$ , and set the optimal arrival times as $[T_i^* ]_{\forall i\in \mathcal{N}(t_0)}\gets \mathbf{T}_N^{(l^*)}(t_0)$ Set $s_k\gets 1,\forall k\in \mathbf{c}$ .   
34 Output: $[T_i^* ]_{\forall i\in A(t_0)}$ 

# 4. Results

# 4.1. Setup

The proposed strategy was implemented in MATLAB R2023a on a personal computer equipped with an AMD Ryzen 7 5800X 8-Core Processor at $3.80\mathrm{GHz}$ and 16 GB RAM. The experiment scenario mirrors that shown in Figure 1, with various combinations of CAVs and HDVs tested. The control zone length was set to $200\mathrm{m}$ (i.e., $p_i = -200\mathrm{m}$ when vehicle $i$ enters and $p_i = 0\mathrm{m}$ when it exits the control zone), and the merging zone length was set to $50\mathrm{m}$ (i.e., $p_i = 50\mathrm{m}$ when vehicle $i$ exits the merging zone). CAVs within the control zone were managed by the proposed strategy or comparison strategies, while HDVs were simulated using the widely adopted IDM,[54] described by 

$$
u _ {i} (t) = a _ {\max } \left(1 - \left(\frac {v _ {i} (t)}{v _ {\max }}\right) ^ {4} - \left(\frac {d _ {\min } + T _ {\min } v _ {i} (t) - \frac {v _ {i} (t) \left(v _ {j} (t) - v _ {i} (t)\right)}{2 \sqrt {a _ {\max } b _ {c}}}}{p _ {j} (t) - p _ {i} (t) - L}\right) ^ {2}\right) \tag {39}
$$

where $j$ is the index of the immediate preceding vehicle, $a_{\mathrm{max}} > 0$ is the desired maximum acceleration, $b_{\mathrm{c}} > 0$ is the comfortable deceleration, and $L$ is the vehicle length. The immediate preceding vehicle was selected within the same road until the HDV reached the position of $p_i = -50\mathrm{m}$ ; after that, vehicles in the adjacent road were also considered, accounting for visibility between the two roads. In the merging zone $(0\mathrm{m}\leq p_i\leq 50\mathrm{m})$ , both CAVs and HDVs were controlled by the IDM, which was expected to enable smooth merging behaviors. The parameters 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/7914cfecc879fd963f45951c8554036590d29e7121b8324b8d6229d0d431a798.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/75d1ad4e5075554889724d408f1ab8def87d963860549b4088dad59c0be56f95.jpg)



Figure 10. Effect of input constraint (2) on the unconstrained solution $u_{i}^{\mathrm{uc}}(t)$ : a) when $u_{i}^{\mathrm{uc}}(t_{0}) > 0$ and b) $u_{i}^{\mathrm{uc}}(t_{0}) < 0$ .


of the IDM and the proposed strategy are listed in Table 1, which were derived from ref. [55] and slightly adjusted to fit the given scenario in this study. 

Two experiments were conducted in this study. Experiment 1 used a 4-vehicle group consisting of two CAVs and two HDVs as a case study to demonstrate the detailed working process of the proposed strategy. Two key features of the proposed strategy were strategic slowdown and DO. The proposed strategy was 


Table 1. Parameters used in the experiments.


<table><tr><td>Parameters</td><td>Symbols</td><td>Values</td></tr><tr><td>Safe time gap to prevent lateral collisions</td><td>Tlat</td><td>1.5 s</td></tr><tr><td>Safe time gap to prevent rear-end collisions</td><td>Trear</td><td>1.5 s</td></tr><tr><td>Maximum allowable speed</td><td>νmax</td><td>30 m s-1</td></tr><tr><td>Maximum control input</td><td>u max</td><td>3 ms-2</td></tr><tr><td>Minimum control input</td><td>u min</td><td>-6 m s-2</td></tr><tr><td>Minimum standstill distance</td><td>d min</td><td>3.5 m</td></tr><tr><td>Minimum time headway</td><td>Tmin</td><td>1.5 s</td></tr><tr><td>Sampling time</td><td>ts</td><td>0.1 s</td></tr><tr><td>Desired maximum acceleration</td><td>a max</td><td>3 m s-2</td></tr><tr><td>Comfortable deceleration</td><td>bc</td><td>3 m s-2</td></tr><tr><td>Vehicle length</td><td>L</td><td>4.5 m</td></tr></table>

compared with a case where the strategic slowdown was intentionally disabled, retaining only DO. The DO was implemented by setting $l^{*} = 0$ in Algorithm 1, effectively removing the strategic slowdown component. 

Experiment 2 statistically evaluated the effectiveness of the proposed strategy in enhancing traffic flow using 20-vehicle groups. Various penetration rates were tested, defined by the ratio of CAVs to the total number of vehicles. For instance, a $30\%$ penetration rate indicates that 6 out of 20 vehicles are CAVs. The proposed strategy was compared with two optimization-based approaches: the static optimization (SO) strategy and the DO strategy. The SO strategy was implemented by solving Problem (7), where only the arrival time of a newly entering vehicle was optimized. That is, the arrival times of previously entered vehicles had already been optimized upon their entry into the control zone and remained fixed, reflecting the static nature of this approach. The SO strategy is identical to the one presented in ref. [46], except for the prediction model of HDV behavior. While ref. [46] employed Newell's car-following model for prediction, we assumed a constant speed for HDVs in all three strategies (SO, DO, and the proposed strategy) to minimize the influence of the prediction model. Notably, the same lower-level control method was applied to both the SO and DO strategies as in the proposed strategy. 

Two performance indices were used in the experiments. The first was the average TTD (ATTD), used in ref. [50] defined as 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/b2dd5ba6078343cae93f706dad10ec35bb62c20e1b71e64df3dab146ea10e63d.jpg)



Figure 11. Scenario of Experiment 1.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/ce32c4b4809f9d8b8f076dc36533a82d3c5fcd6da4b5aa72e50199ae61577ca6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/8e3cd8e6ae59b6aa3fc01811961a8f29aa13f34e94a48b4e920ba596360e8af7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/48602bc2176e04b042ccce82ed409915deca1206dabaf557eaced211b1cdb67c.jpg)



DO strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/95131912fae297f4769892dd563a89fe431e7c1c0c6eeb2f44e8a4673e839881.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/4a8dd20aba2ef5c419ecd2ee460bb740fcbdc9af66e8325de72b9ff1e0cef1e1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/1ad03a0b638432e81be95347fa99835e73371af613eb6fb589724c5176ce7986.jpg)



Proposed strategy



Figure 12. Position, speed, and acceleration profiles obtained using a) the DO strategy and b) the proposed strategy in Experiment 1. Red lines represent vehicles on the main road, and blue lines represent vehicles on the ramp road. Solid lines indicate CAVs, while dashed lines indicate HDVs.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/824a93fe0da50e4268222de9d1a7f80641adb5c80d556919d55fd38f21cb0bc3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/24ab18f2d5b93b3b34ddf0603375ef32bea11023dea3777701c8d4634a06977c.jpg)



DO strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/185610b73690d54e97777737b21cb50a9a01618ac465c60f6018e1269c382412.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/c166cc4d6fb8707f7396b768763736366e0488474704e7764f2e88b667a45fe5.jpg)



Proposed strategy



Figure 13. Arrival times obtained using a) the DO strategy and b) the proposed strategy in Experiment 1. Red lines represent vehicles on the main road, and blue lines represent vehicles on the ramp road. Solid lines indicate CAVs, while dashed lines indicate HDVs.


$$
\mathrm {A T T D} = \frac {1}{M} \sum_ {i = 1} ^ {M} \mathrm {T T D} _ {i} \tag {40}
$$

where $M$ is the total number of vehicles passing through the control and merging zones. Note that the TTD is the objective function in the arrival time optimization problem. The second performance index was the control cost, calculated by 

$$
\text {C o n t r o l} = \sum_ {i = 1} ^ {M} \int_ {0} ^ {\infty} u _ {i} ^ {2} (t) d t \tag {41}
$$

which reflects the energy consumption of the vehicles. 

# 4.2. Experiment 1: Investigating the Effects of Strategic Slowdown Using a 4-Vehicle Group

Vehicles 1, 2, 3, and 4 were designated CAV, CAV, HDV, and HDV, respectively, with $r_1 = r_3 = r_4 = 1$ and $r_2 = 0$ , indicating that only CAV 2 was on the main road. They entered the control zone at $t = 1$ , 1.5, 2, and 3 s with initial speeds of 24, 30, 24, and $24\mathrm{ms}^{-1}$ , respectively. The scenario is illustrated in Figure 11. 

The results obtained by the DO and proposed strategies are presented in Figure 12 and 13, respectively. Figure 12 compares the position, speed, and acceleration (i.e., control input) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/3f144380e90beb820bfc43069482cc1c51c7e5ddf15da6f24ebbbd580e492988.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/0712521b82d8ff6fd1866b905098da94b405d5d154ec029f97c2968e64e41a6f.jpg)



Figure 14. Comparison of performance indices between the DO and the proposed strategies in Experiment 1. a) ATTD. b) Control cost.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/ca5ca32b7a4419c3ad256aa84c4cf94238acbcef411fb33e368794aa1bcd3b42.jpg)



$T_{g} = 0.5$ s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/3db9743accfbc61844b6c046924381aa7b01cc0c6ddec2b1df9632ee55d3b675.jpg)



$T_{g} = 1$ s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/45cea11a4fa3082e2f07baf66eb80f73508eb66ba43c653f0276638202e63fdf.jpg)



$T_{g} = 1.5\mathrm{s}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/0ef160ed21e03b57022016de0024572ee465f902ac40dc6f9698ba8b2d61d0e0.jpg)



$T_{g} = 2\mathrm{s}$



Figure 15. Comparison of ATTD between the SO, DO, and proposed strategies across different penetration rates for a) $T_{\mathrm{g}} = 0.5$ s, b) $T_{\mathrm{g}} = 1$ s, c) $T_{\mathrm{g}} = 1.5$ s, and d) $T_{\mathrm{g}} = 2$ s in Experiment 2.


trajectories of the DO strategy (see Figure 12a) and the proposed strategy (see Figure 12b). The proposed strategy allowed CAV 2 to exit the control zone first and provided smooth speed and acceleration profiles. In contrast, the DO strategy caused CAV 2 to exit the control zone last, with significant changes in speed and acceleration. 

The difference between the strategies arose from the use of strategic slowdown in the proposed strategy, as illustrated in Figure 13. In the DO strategy, the arrival time of CAV 2 was placed after the HDVs when each HDV entered the control zone due to the lack of a safe time gap between CAV 1 and HDV 3 and between HDV 3 and HDV 4. Conversely, in the proposed strategy, the arrival time of CAV 2 was positioned before CAV 1, owing to the strategic slowdown of CAV 1, which acted as the strategic CAV. This strategic slowdown was chosen to minimize the objective function. 

This strategic slowdown led the proposed strategy to achieve a $16\%$ reduction in ATTD and a $65\%$ reduction in control cost compared to the DO strategy, as shown in Figure 14. Although control cost was not explicitly considered in the optimization, the proposed strategy benefited from the strategic slowdown, which mitigated merging uncertainties and resulted in smoother control actions. 

The results of Experiment 1 were reproduced in an open-source simulator, Carla 0.9.15, which uses the physics engine Unreal Engine, and are available at https://github.com/GIST-MIC-Lab/Cooperative-merging-in-mixed-traffic. 

# 4.3. Experiment 2: Investigating the Effects of the Proposed Strategy on Traffic Flow Using 20-Vehicle Groups

Ten vehicles traveled on both the main and ramp roads. Ten penetration rates, ranging from $10\%$ to $100\%$ in $10\%$ increments, were tested to determine the number of CAVs, with the vehicle type (CAV or HDV) randomly assigned. The time of entry into the control zone for vehicle $i$ was randomly determined as $iT_{\mathrm{g}} + 0.8T_{\mathrm{g}}x$ , where $x$ is a random variable uniformly distributed between $-1$ and $1$ , ensuring that the time gap between two vehicles entering the control zone was greater than $0.4T_{\mathrm{g}}$ . If the entering time of a vehicle resulted in a smaller gap to its preceding vehicle on the same road than $T_{\mathrm{rear}}$ , its entry time was adjusted to ensure a time gap at least $T_{\mathrm{rear}}$ . Four difference values of $T_{\mathrm{g}}$ were considered: $T_{\mathrm{g}} = 0.5$ , $1$ , $1.5$ , and $2\mathrm{s}$ . The initial speeds of vehicles on the main and ramp roads were randomly set between [26, 30] and [13, 15] m/s, respectively. The initial speeds were adjusted as needed to comply with the rear-end collision constraint (5). Each combination of penetration rate and $T_{\mathrm{g}}$ was tested 1000 times. 

Figure 15 compares the ATTD values between the SO, DO, and proposed strategies across different penetration rates for $T_{\mathrm{g}} = 0.5$ , 1, 1.5, and 2 s. The ATTD decreased in all strategies as the value of $T_{\mathrm{g}}$ increased, since a larger $T_{\mathrm{g}}$ reduced the likelihood of conflicts between vehicles. In the SO strategy, ATTD increased up to a penetration rate of $50\%$ and then dropped 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/d5f33ddb2c6b6527675a2f0e9b915e9b52436810c158ceff7cf07ed96023316c.jpg)



$T_{g} = 0.5\mathrm{s}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/5d15780b312b5b00ef7391d4d97d0846b90cfeeaa0bda5914983a545c106e248.jpg)



$T_{g} = 1$ s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/4c1ec80d4e3896e5919a3be8373309a7fdda00f4c64b25da897267073111d631.jpg)



$T_{g} = 1.5\mathrm{s}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/20ef827c377ace93089bbdbe01946c13156ed2fc0b2ed57972a0b07e469b428f.jpg)



$T_{g} = 2\mathrm{s}$



Figure 16. Comparison of ATTD reduction by the DO and proposed strategies relative to the SO strategy across different penetration rates for a) $T_{\mathrm{g}} = 0.5 \, \mathrm{s}$ , b) $T_{\mathrm{g}} = 1 \, \mathrm{s}$ , c) $T_{\mathrm{g}} = 1.5 \, \mathrm{s}$ , and d) $T_{\mathrm{g}} = 2 \, \mathrm{s}$ in Experiment 2.


sharply. While the proposed strategy consistently yielded lower ATTD values than the SO strategy across various combinations of $T_{\mathrm{g}}$ and penetration rates, the DO strategy exhibited higher ATTD values than the SO strategy at lower penetration rates when $T_{\mathrm{g}} \leq 1.5$ s. 

This trend is more clearly illustrated in Figure 16, which presents the ATTD reduction rates of the DO and proposed strategies relative to the SO strategy across different penetration rates for $T_{\mathrm{g}} = 0.5$ , 1, 1.5, and 2 s. The ATTD reduction rate of the DO strategy reached up to $20\%$ under certain low-penetration conditions, suggesting that DO alone may not effectively handle HDV uncertainties when the proportion of CAVs is small. In contrast, the proposed strategy consistently mitigated the adverse effects of DO, reducing its limitations when DO underperformed and further enhancing its benefits when DO was effective. This demonstrates that the strategic slowdown mechanism of the proposed strategy helps stabilize traffic flow across different conditions. 

The proposed strategy outperformed the SO strategy in terms of ATTD reduction at penetration rates above 30, 40, 50, and $10\%$ for $T_{\mathrm{g}} = 0.5$ , 1, 1.5, and $2\mathrm{s}$ , respectively. Based on these results, we estimate that the minimum penetration rate required for the proposed strategy to be effective ranges between $30\%$ and $50\%$ . Notably, at a penetration rate of $70\%$ with $T_{\mathrm{g}} = 2\mathrm{s}$ , the proposed strategy achieved an ATTD reduction of up to $31\%$ , demonstrating substantial improvements. The 

peak reduction effect was observed at penetration rates of $60\%$ to $70\%$ across all $T_{\mathrm{g}}$ values. At a $100\%$ penetration rate (i.e., when all vehicles are CAVs), where cooperation becomes trivial, all strategies yielded nearly identical ATTD values. 

Figure 17 presents the control costs of the SO, DO, and proposed strategies across different penetration rates for $T_{\mathrm{g}} = 0.5$ , 1, 1.5, and 2 s. Overall, control costs tended to decrease across all strategies as $T_{\mathrm{g}}$ and the penetration rate increased, indicating that larger entry time gaps between vehicles and a higher proportion of CAVs led to reduced acceleration and deceleration effort. 

The control costs for the DO and proposed strategies were generally higher than those of the SO strategy under most conditions, likely due to the active adjustment of control actions driven by DO and strategic slowdown. Future research should explore smoother control strategies that maintain a similar ATTD reduction effect while minimizing energy consumption (i.e., reducing control costs). 

When comparing the proposed strategy and the DO strategy, the proposed strategy demonstrated better efficiency, achieving lower ATTD values while maintaining nearly identical control costs (see Figure 15 and 16). 

For a case study of the results from Experiment 2, a scenario with a penetration rate of $70\%$ and $T_{\mathrm{g}} = 1.5 \mathrm{~s}$ was selected from the 1000 repetitions. The position, speed, and acceleration trajectories for this scenario are presented in Figure 18, 19, and 20, respectively. As shown in Figure 18, the last vehicle exited the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/fccfb41ba3a7b1217617ec4cf96f27b18da52d1cc3239906d36e1a47bcb92432.jpg)



$T_{g} = 0.5\mathrm{s}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/3000bbda843efab04a579674e8e2d91de9f169d586f4560ba82bb54d8ba92e74.jpg)



$T_{g} = 1$ s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/092b156934d011631d04dea419174a7c6fe32b58a6e76e62b2dea69bc7c8dd32.jpg)



$T_{g} = 1.5\mathrm{s}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/4e92821532101e9db6ac01f0603ad83c79e6236e8cd79da71a389cec1b8c945c.jpg)



$T_{g} = 2\mathrm{~s}$



Figure 17. Comparison of control costs for the SO, DO, and proposed strategies across different penetration rates for a) $T_{\mathrm{g}} = 0.5$ s, b) $T_{\mathrm{g}} = 1$ s, c) $T_{\mathrm{g}} = 1.5$ s, and d) $T_{\mathrm{g}} = 2$ s in Experiment 2.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/1c0d12fac6be0e86a4aa22ef955685f6c38fa06237625aa779a1eb9be20e38b7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/6388d3284028bcd37d90d89fd353b17ef0a121a0830f56f595ff032c69c4a091.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/f3b6227bd5635efd9b29eaef6fe09cef7c4734fbc45c9b5d907aaf20b6d6e4e8.jpg)



Figure 18. Position trajectories obtained using a) the SO, b) DO, and c) proposed strategies for a scenario with $T_{\mathrm{g}} = 1.5$ s and a penetration rate of $70\%$ . Red lines represent vehicles on the main road, and blue lines represent vehicles on the ramp road. Solid lines indicate HDVs, while dashed lines indicate CAVs.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/e9d1f207dce80e7ab170c3c5ad846b5851958659b8f9a1f4b56055122780064b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/6fd07101b87e5e7a78198f8dfad1c81c0add132ab28e2fbaec5246e7813240fc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/700e34e1cdda4aa3bece8516920cda638d629427af82a3ec9cb8f3110698188c.jpg)



Figure 19. Speed trajectories obtained using a) the SO, b) DO, and c) proposed strategies for a scenario with $T_{\mathrm{g}} = 1.5$ s and a penetration rate of $70\%$ . Red lines represent vehicles on the main road, and blue lines represent vehicles on the ramp road. Solid lines indicate HDVs, while dashed lines indicate CAVs.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/884c5f7b0c828386497b4f927d9189d0512c605cfab2b918b5252ff648bce73e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/1cddfa838ca8960f2bfc37a9109611f72bf21164578e421e17f61f73d6ae9b7c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/6f618183-fdaf-4010-b242-0769ba8fb6e2/017f164fd26d46dccfa40bb82c8f65efe496df5263372491d1b3e541e77a8b51.jpg)



Figure 20. Acceleration trajectories obtained using a) the SO, b) DO, and c) proposed strategies for a scenario with $T_{\mathrm{g}} = 1.5$ s and a penetration rate of 70%. Red lines represent vehicles on the main road, and blue lines represent vehicles on the ramp road. Solid lines indicate HDVs, while dashed lines indicate CAVs.



Table 2. Comparison of computation times for the results shown in Figure 18-20.


<table><tr><td>Strategy</td><td>Mean [μs]</td><td>Standard deviation [μs]</td><td>Maximum [ms]</td></tr><tr><td>SO</td><td>32.0</td><td>101</td><td>2.78</td></tr><tr><td>DO</td><td>62.4</td><td>325</td><td>5.74</td></tr><tr><td>Proposed</td><td>79.3</td><td>467</td><td>9.04</td></tr></table>

control zone the earliest (40.5 s) with the proposed strategy, compared to 47.1 and 45.8 s for the SO and DO strategies, respectively. This earliest exit (equivalently, the lowest ATTD) was made possible by a strategic slowdown at $\approx 25$ s. The proposed strategy also resulted in smoother speed profile compared to the other strategies. 

The computation times for these results were measured using tic-toc function in MATLAB and are compared in Table 2. The mean computation times were less than $80~\mu \mathrm{s}$ for all strategies, indicating their feasibility for real-time implementation. However, the maximum computation times for the DO and proposed strategies were 5.74 and $9.04\mathrm{ms}$ , respectively, which were more than twice that of the SO strategy. Nevertheless, computation times at the millisecond level remain sufficiently low for real-time applications. 

# 5. Concluding Remarks

This study presented an optimization-based cooperative merging strategy for CAVs in mixed traffic. The strategy utilized a hierarchical optimization framework, with the upper level optimizing CAV arrival times at the merging point and the lower level determining energy-efficient control inputs for each CAV. The key contributions of this study lie in the upper-level optimization. Strategic Influence of CAVs on HDV Behavior: The approach strategically slows down the preceding CAV to influence following HDVs, allowing other CAVs to merge ahead with reduced uncertainty, without relying on precise HDV predictions. 

Full CAV Cooperation: The strategy evaluates various cooperative actions among all CAVs to determine the optimal slowdown pattern, maximizing overall traffic efficiency. 

Dynamic Optimization: The optimization is performed in real time at each time a new vehicle enters the control zone, effectively adapting to variations in HDV behavior. 

These features enable the proposed strategy to effectively coordinate multiple CAVs and manage uncertainties associated with HDVs in complex merging scenarios, demonstrating its potential for real-world mixed traffic conditions. Results demonstrated that the proposed strategy significantly reduces the ATTD by up to $31\%$ compared to the SO strategy. 

Future research will focus on developing a more articulated approach for multi-lane settings considering detailed lane-change behaviors of HDVs when they are subject to the strategic slowdown by their preceding CAVs. An idea of this is to consider probabilistic reactions of HDVs when subject to the strategic slowdown. An HDV may take a lane change with a certain probability depending on its driving characteristic. This probabilistic 

behavior is expected to be learnt through data-driven methods and can be incorporated into the optimization process. 

# Supporting Information

Supporting Information is available from the Wiley Online Library or from the author. 

# Acknowledgements

This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (RS-2025-00554087). 

# Conflict of Interest

The authors declare no conflict of interest. 

# Author Contributions

Kyunghwan Choi: conceptualization (supporting); funding acquisition (lead); methodology (supporting); supervision (lead); writing—review & editing (lead). Seongjae Shin: data curation (lead); investigation (lead); visualization (lead); writing—original draft (lead). Minseok Seo: data curation (supporting); validation (equal). 

# Data Availability Statement

The data that support the findings of this study are openly available in Github at https://github.com/GIST-MIC-Lab/Cooperative-merging-in-mixed-traffic. 

# Keywords

connected and automated vehicles, cooperative control, human-driven vehicles, mixed traffic, on-ramp merging 

Received: September 16, 2024 

Revised: March 12, 2025 

Published online: April 10, 2025 



[1] J. Rios-Torres, A. A. Malikopoulos, IEEE Trans. Intell. Veh. 2018, 3, 453. 





[2] J. Ding, H. Peng, Y. Zhang, L. Li, IET Intell. Transp. Syst. 2020, 14, 56. 





[3] W. Lin, X. Hu, J. Wang, Adv. Intell. Syst. 2024, 6, 2300692. 





[4] J. Rios-Torres, A. A. Malikopoulos, IEEE Trans. Intell. Transp. Syst. 2016, 18, 780. 





[5] Z. Tang, H. Zhu, X. Zhang, M. Iryo-Asano, H. Nakamura, Transp. Res. Part C Emerg. Technol. 2022, 138, 103650. 





[6] N. Chen, B. van Arem, T. Alkim, M. Wang, IEEE Trans. Intell. Transp. Syst. 2020, 22, 7712. 





[7] J. Wu, Y. Wang, Z. Zhang, Y. Wen, L. Zhong, P. Zheng, Sustainability 2022, 14, 11120. 





[8] H. Pei, S. Feng, Y. Zhang, D. Yao, IEEE Trans. Veh. Technol. 2019, 68, 11646. 





[9] P. Hang, C. Lv, C. Huang, Y. Xing, Z. Hu, IEEE Trans. Intell. Transp. Syst. 2021, 23, 3829. 





[10] R. Chen, Z. Yang, IEEE Trans. Intell. Transp. Syst. 2022, 23, 19213. 





[11] Q. Yuan, F. Yan, Z. Yin, L. Chen, J. Hu, D. Wu, Y. Li, Adv. Intell. Syst. 2023, 5, 2300177. 





[12] L. Yang, J. Zhan, W.-L. Shang, S. Fang, G. Wu, X. Zhao, M. Deveci, IEEE Trans. Intell. Transp. Syst. 2023, 24, 13448. 





[13] O. Nassef, L. Sequeira, E. Salam, T. Mahmoodi, IEEE Internet Things J. 2020, 8, 2540. 





[14] S. K. S. Nakka, B. Chalaki, A. A. Malikopoulos, in 2022 American Control Conf. (ACC), IEEE, Piscataway, NJ 2022 pp. 3297-3302. 





[15] G. Li, W. Zhou, S. Lin, S. Li, X. Qu, Automotive Innov. 2023, 6, 453. 





[16] C. Chen, C. Yong, X. Guo, X. Pei, Adv. Intell. Syst. 2023, 5, 2300081. 





[17] J. Guanetti, Y. Kim, F. Borrelli, Annu. Rev. Control 2018, 45, 18. 





[18] J. Zhu, S. Easa, K. Gao, J. Intell. Connect. Veh. 2022, 5, 99. 





[19] A. Alessandrini, A. Campagna, P. Delle Site, F. Filippi, L. Persia, Transp. Res. Proc. 2015, 5, 145. 





[20] Y. Wang, L. Wang, J. Guo, I. Papamichail, M. Papageorgiou, F.-Y. Wang, R. Bertini, W. Hua, Q. Yang, Transp. Res. Part C Emerg. Technol. 2022, 138, 103478. 





[21] M. Cui, Y. Hu, S. Xu, J. Wang, Z. Bing, B. Li, A. Knoll, Adv. Intell. Syst. 2023, 5, 2300269. 





[22] E. Sabouni, C. G. Cassandras, IFAC-PapersOnLine 2023, 56, 2353. 





[23] A. Li, A. S. C. Armijos, C. G. Cassandras, Automatica 2025, 174, 112169. 





[24] H. Liu, G. Yin, W. Zhuang, R. Li, in 2021 5th CAA Inter. Conf. on Vehicular Control and Intelligence (CVCI), IEEE, Piscataway, NJ 2021, pp. 1-7. 





[25] H. Liu, W. Zhuang, G. Yin, Z. Li, D. Cao, IEEE Trans. Intell. Transp. Syst. 2023, 24, 2920. 





[26] Z. Sun, T. Huang, P. Zhang, Transp. Res. Part C Emerg. Technol. 2020, 120, 102764. 





[27] Y. Jiang, Z. Man, Y. Wang, Z. Yao, Expert Syst. Appl. 2024, 252, 124163. 





[28] L. Han, L. Zhang, W. Guo, IET Intell. Transp. Syst. 2023, 17, 1891. 





[29] N. Venkatesh, V.-A. Le, A. Dave, A. A. Malikopoulos, in 2023 62nd IEEE Conf. on Decision and Control (CDC), IEEE, Piscataway, NJ 2023, pp. 92-97. 





[30] M. Karimi, C. Roncoli, C. Aleksandru, M. Papageorgiou, Transp. Res. Part C Emerg. Technol. 2020, 116, 102663. 





[31] Y. Jiang, H. Chen, G. Xiao, H. Cong, Z. Yao, Transp. Lett. 2024, 1. 





[32] Z. Du, H. Xie, P. Zhai, S. Yuan, Y. Li, J. Wang, J. Wang, K. Liu, Appl. Sci. 2024, 14, 7375. 





[33] M. Bouton, A. Nakhaei, K. Fujimura, M. J. Kochenderfer, in 2019 IEEE Intelligent Transportation Systems Conf. (ITSC), IEEE, Piscataway, NJ 2019, pp. 3441-3447. 





[34] Z. Chen, Y. Wang, H. Hu, Z. Zhang, C. Zhang, S. Zhou, Mathematics 2024, 12, 3859. 





[35] R. Zhao, Z. Sun, A. Ji, in 2022 IEEE 25th Inter. Conf. on Intelligent Transportation Systems (ITSC), IEEE, Piscataway, NJ 2022, pp. 3800-3806. 





[36] Z. el abidine Kherroubi, S. Aknine, R. Bacha, IEEE Trans. Intell. Transp. Syst. 2021, 23, 12490. 





[37] S. Udatha, Y. Lyu, J. Dolan, in 2023 IEEE Inter. Conf. on Robotics and Automation (ICRA), IEEE, Piscataway, NJ 2023, pp. 5625-5630. 





[38] E. Sabouni, H. S. Ahmad, V. Giammarino, C. G. Cassandras, I. C. Paschalidis, W. Li, in IEEE 63rd Conf. on Decision and Control (CDC), Vol. 2024, IEEE, Piscataway, NJ 2024, pp. 401-406. 





[39] Q. Liu, F. Dang, X. Wang, X. Ren, in 2022 IEEE 25th Inter. Conf. on Intelligent Transportation Systems (ITSC), IEEE, Piscataway, NJ 2022, pp. 1063-1069. 





[40] B. Brito, A. Agarwal, J. Alonso-Mora, IEEE Trans. Intell. Transp. Syst. 2022, 23, 18808. 





[41] R. Valiente, B. Toghi, R. Pedarsani, Y. P. Fallah, IEEE Open J. Intell. Transp. Syst. 2022, 3, 397. 





[42] D. Chen, M. R. Hajidavalloo, Z. Li, K. Chen, Y. Wang, L. Jiang, Y. Wang, IEEE Trans. Intell. Transp. Syst. 2023, 24, 11623. 





[43] L. Liu, X. Li, Y. Li, J. Li, Z. Liu, IEEE Internet Things J. 2024. 





[44] B. Toghi, R. Valiente, D. Sadigh, R. Pedarsani, Y. P. Fallah, IEEE Trans. Intell. Transp. Syst. 2022, 23, 24791. 





[45] X. Zhang, L. Wu, H. Liu, Y. Wang, H. Li, B. Xu, IEEE Internet Things J. 2023. 





[46] V.-A. Le, H. M. Wang, G. Orosz, A. A. Malikopoulos, in 2023 62nd IEEE Conf. on Decision and Control (CDC), IEEE, Piscataway, NJ 2023, pp. 4150-4155. 





[47] J. Shi, K. Li, C. Chen, W. Kong, Y. Luo, IEEE Trans. Intell. Transp. Syst. 2023, 24, 11185. 





[48] W. Zhao, M. Yildirimoglu, Transp. Res. Part C Emerg. Technol. 2024, 169, 104859. 





[49] H. Jiang, Z. Yao, Y. Zhang, Y. Jiang, Z. He, Transp. Res. Part C Emerg. Technol. 2024, 163, 104623. 





[50] C. Chen, J. Wang, Q. Xu, J. Wang, K. Li, Transp. Res. Part C Emerg. Technol. 2021, 127, 103138. 





[51] H. Xu, Y. Zhang, C. G. Cassandras, L. Li, S. Feng, Transp. Res. Part C Emerg. Technol. 2020, 120, 102773. 





[52] W. Xiao, C. G. Cassandras, Automatica 2021, 123, 109333. 





[53] V.-A. Le, A. A. Malikopoulos, in 2022 IEEE 61st Conf. on Decision and Control (CDC), IEEE, Piscataway, NJ 2022, pp. 6272-6277. 





[54] M. Treiber, A. Hennecke, D. Helbing, Phys. Rev. E 2000, 62, 1805. 





[55] K. Hou, F. Zheng, X. Liu, G. Guo, IEEE Trans. Intell. Transp. Syst. 2023, 24, 10774. 

