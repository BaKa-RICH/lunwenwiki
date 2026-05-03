# Optimizing On-Ramp Merging for Connected and Automated Vehicles: A Hierarchical Approach Using Deep Reinforcement Learning and Optimal Control

Abu Jafar Md Muzahida,1, Yang Shia,1, Zejiang Wangb, Anye Zhoub, Adian Cookb, Chieh Ross Wangb and Zhenbo Wanga,∗ 

aDepartment of Mechanical and Aerospace Engineering, The University of Tennessee, Knoxville, 37996, USA 

bApplied Research for Mobility Systems Group, Oak Ridge National Laboratory, Oak Ridge, 37831, USA 

# A R T I C L E I N F O

Keywords: 

Connected and Automated Vehicles 

On-Ramp Merging 

Vehicle Control Systems 

Virtual Traffic Signal 

Deep Reinforcement Learning 

Model Predictive Control. 

# A B S T R A C T

On-ramp merging for Connected and Automated Vehicles (CAVs) presents significant challenges in dynamic traffic environments. Traditional methods and recent learning-based approaches often fail to simultaneously address decision-making complexity and execution precision under fluctuating conditions. This study introduces a novel hierarchical framework that combines: (1) a high-level Deep Reinforcement Learning (DRL) module that coordinates merging sequences through Virtual Traffic Signals (VTS) with Yield/Green phases and (2) a low-level optimal controller generating collision-free speed trajectories via pseudospectral convex optimization. A convolutional autoencoder compresses high-dimensional traffic states to enhance responsiveness. Extensive simulations demonstrate a $1 2 . 5 \%$ improvement in mainline throughput a $2 8 \%$ reduction in emergency braking events, and $3 1 . 6 6 \%$ lower fuel consumption compared to baseline methods. The framework’s effectiveness in coordinating CAV merges highlights its potential for real-world deployment. Future work will extend validation to multilane scenarios with mixed traffic and large-scale multiple merging points. 

# 1. Introduction

On-ramp merging is a critical area prone to congestion and accidents due to vehicles adopting cautious behaviors to avoid collisions Ding, Peng, Zhang and Li (2020). This issue is exacerbated for connected and automated vehicles (CAVs) by mileage anxiety Dehman and Farooq (2021). However, CAVs’ capabilities for optimized motion and speed profiles can mitigate congestion while enhancing time and energy efficiency and reducing emissions Rahman and Thill (2023); Eskandarian, Wu and Sun (2019). 

Leveraging these CAV capabilities, we address the onramp merging problem for improved efficiency and scalability. This problem is challenging due to the demand for exact coordination between multiple vehicles and traffic components in real-world scenarios Zhu, Easa and Gao (2022). The presence of unpredictable human-driven vehicles (HDVs) alongside CAVs poses a serious threat to system performance, making optimal control especially difficult in mixedtraffic environments Fernandez, Marinho, Vakilzadeh and Vinel (2021). Substantial research has focused on control approaches for fully automated traffic, often categorized 

as optimization-based or cooperative learning-based Aziz, Wang, Young, Sperling and Beck (2017); Zhu et al. (2022); Fernandez et al. (2021). These typically focus on decisionmaking and the safe execution of those decisions. Despite progress, existing methods often struggle to simultaneously optimize merging sequences, ensure safe execution, and maintain computational efficiency and real-world applicability Eskandarian et al. (2019). 

This study addresses the on-ramp merging problem by focusing on two core challenges: (a) determining the optimal merging sequence and (b) planning vehicle movements via improved speed profiles Fernandez et al. (2021); Zhu et al. (2022). The complexity of these tasks lies in the algorithmic difficulty of decision-making and ensuring the control mechanism safely executes those decisions el abidine Kherroubi, Aknine and Bacha (2021a); Kherroubi (2020a,b). 

We propose a novel hierarchical approach that reduces computational complexity and operational costs while ensuring safety and efficiency. A key innovation is the simplification of the Deep Reinforcement Learning (DRL) agent’s action space to two options—Yield and Green—which allows the model to focus on optimizing merge timing. Inspired by the Learning Options Framework Stolle and Precup (2002), this design enables temporally extended, macroaction-like behavior, boosting learning efficiency and robustness without explicitly defining complex macro-actions. 

Unlike conventional single-agent methods Lin, McPhee and Azad (2022), our framework distinctly separates functions: a high-level module manages the merging sequence, while a low-level module executes safe and optimal vehicle trajectories Liu, Zhao and Xu (2021); Triest, Villaflor and 

Dolan (2020). This separation improves scalability and realtime performance. By incorporating advanced technologies Zhang, Liu, Wolshon and Sheng (2020), this VTS-based framework balances simplicity and performance, addressing a key challenge in the field Fernandez et al. (2021) and holding promise for tackling real-world issues like HDV integration and imperfect data Fernandez et al. (2021); Zhu et al. (2022), thereby paving the way for safer and more sustainable urban mobility Zhang et al. (2020). 

Fig. 1 illustrates the proposed coordinating framework. A DRL agent processes real-time data from RSUs to generate preliminary merging decisions (Yield or Green) using a simplified action space. These decisions are refined by an Optimal Control Problem (OCP) solver, which computes precise speed profiles—via methods such as pseudospectral convex optimization—to create optimal merging sequences. Vehicles then select and follow these prescribed sequences and speed profiles for smooth merging. Unlike traditional ramp metering, our framework dynamically adapts to realtime conditions, significantly improving responsiveness and efficiency. A Convolutional Autoencoder (CAE) further enhances state representation for adapting to dynamic traffic Muzahid, Kamarulzaman, Rahman and Alenezi (2022). This study assumes ideal communication for the VTS system. 

This study makes the following key contributions: 

1. A novel hierarchical control framework integrating a high-level DRL decision layer for merge sequencing with a low-level OCP execution layer for optimal speed profile computation. 

2. Pioneering the integration of VTS into the on-ramp merging process. The proposed methodology simplifies decision making by limiting the DRL action space to just two options (Yield or Green), reducing decision complexity and allowing the model to focus on optimizing the merging timing rather than continuously evolving signal states. 

3. Enhanced state representation for the DRL agent using a CAE to better adapt to dynamic traffic. 

4. Extensive simulations demonstrating significant improvements in traffic flow, safety, and fuel efficiency. 

The remainder of this paper is structured as follows: Section 2 reviews related literature. Section 3 details the proposed framework. Section 4 provides a detailed methodological design. Sections 5 and 6 present and validate the results, respectively. Sections 7 and 8 discuss scalability, limitations, and future work. Section 9 concludes the paper. 

# 2. Related Work

On-ramp merging for CAVs has been extensively researched, particularly in relation to efficient merging decisions and merging speed profiles that optimize vehicle integration into main traffic flows Zhu et al. (2022); Fernandez et al. (2021); Li, Ma and Chen (2024). Merging sequence determination employs rule-based (e.g., first-in-first-out) or optimization-based methods, including genetic algorithms 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/ed55b0039748619a08fd411e2bc4bf3275cd5e9d483cb4f63c93298ac883d261.jpg)



Figure 1: Illustration of the proposed control framework and the on-ramp merging scenario of this study.


Scholte, Zegelaar and Nijmeijer (2022); Wang, Zhou, Cook, Shao, Xu and Chen (2023b); Xu, Lu, Ran, Yang and Zhang (2019). Subsequently, motion planning algorithms generate merging speed profiles to enhance traffic flow and fuel efficiency Wang, Cook, Shao, Xu and Chen (2023a); Shi, Wang, Wang and Shao (2023b). Control strategies are either centralized or decentralized Zhu et al. (2022), often formulated as multi-objective optimizations considering travel time, fuel consumption, and comfort. 

Recent work integrates sequence allocation with speed profile optimization. Frameworks based on multi-player games Jing, Hui, Zhao, Rios-Torres and Khattak (2019a); Muzahid, Rahim, Murad, Kamarulzaman and Rahman (2021) and hierarchical model predictive control (MPC) Chen, van Arem, Alkim and Wang (2020a) have been proposed for coordinated merging. Virtual traffic signals (VTS) offer a promising alternative to traditional signals by minimizing stop-and-go waves, improving safety and reducing congestion in merging zones Zhang et al. (2020). 


Table 1 Comparison of merging control approaches.


<table><tr><td>Characteristic</td><td>Optimization-Based</td><td>RL-Based</td><td>Proposed Framework</td></tr><tr><td>Core methodology</td><td>Mathematical programming (e.g., GA, MPC)</td><td>Learning from interaction</td><td>Data-driven + model-based</td></tr><tr><td>Real-time performance</td><td>Computationally intensive</td><td>Sensitive to delays</td><td>VTS-optimized sequencing</td></tr><tr><td>Uncertainty handling</td><td>Model-dependent</td><td>Adaptive but data-hungry</td><td>Prior knowledge + real-time adaptation</td></tr><tr><td>Control granularity</td><td>Motion planning focus</td><td>Action-level control</td><td>Hierarchical decision-action decoupling</td></tr><tr><td>Key advantage</td><td>Optimal under constraints</td><td>Handles complex states</td><td>Balanced robustness &amp; efficiency</td></tr></table>

Reinforcement learning (RL) is increasingly used for merging control. Applications include RL-based lane selection to balance traffic flow Liu et al. (2021) and hybrid models combining artificial neural networks (ANN) with DRL to predict behavior and control acceleration el abidine Kherroubi, Aknine and Bacha (2021b). However, RL models often face real-time performance issues and communication delays Gao, Ji, Wu, Wei and Grech (2023); Ma, Wu, Chen, Ji and Ding (2023). While deep learning can map sensory inputs directly to controls, it struggles with dynamic uncertainties Ruan, Li, Zhu and Liu (2022). Compressed representations (e.g., from autoencoders) can reduce training time but require careful design Wilmot, Baldassarre and Triesch (2021); Zhang, Fan, Zhou and Gao (2024). 

Integrating low-level controllers with RL remains an active area. Advanced representation learning techniques (e.g., hierarchical, task-induced) can improve RL agent adaptability Yamada, Pertsch, Gunjal and Lim (2022); Kim, Rho, Kim and Jung (2022); Muzahid, Zhao and Wang (2024), though multi-sensory inputs pose additional challenges Murray and Shams (2023). Overall, developing hierarchical systems that combine low-level control with high-level RL ( Table 1) aims to create robust behaviors for dynamic environments, necessitating empirical validation and adaptive learning mechanisms Wang, Xing, Chen and Liu (2024). 

# 3. Proposed Framework

This section presents a hierarchical control framework for real-time on-ramp merging, integrating Vehicle-to-Infrast (V2I) communication with OCP techniques. The architecture consists of a high-level DRL module for coordinating merge sequences and a low-level optimal controller for precise trajectory execution. By processing live traffic data, the system enhances merging efficiency, safety, and fuel economy through adaptive decision-making and speed optimization, as depicted in Fig. 1. 

The framework partitions the merging process into three functional zones: data acquisition, decision-making, and control execution. Spatially, it defines a 400-meter control area, subdivided into a 100-meter prediction zone, a 100- meter decision zone, and a 200-meter control zone, followed by a 100-meter merging area. These dimensions, 

adapted from prior research Zhu and Tasic (2021); el abidine Kherroubi et al. (2021a); Kherroubi (2020a), are tunable based on traffic conditions—extendable in congested settings and reducible in high-speed environments. This framework balances simplicity and effectiveness by incorporating advanced technology Zhang et al. (2020) and addressing complex traffic challenges Fernandez et al. (2021). The DRL agent’s action space is streamlined to “Yield” or “Green,” optimizing merge timing rather than signal states. This design, based on temporally extended actions from the Learning Options Framework Stolle and Precup (2002), enhances decision-making efficiency and robustness without delving into intricate macro-actions. 

# 3.1. Assumptions

The proposed framework considers the following fundamental assumptions. 

Assumption 1: All vehicles are CAVs with 100% market penetration. Each CAV possesses: A) Real-time V2X communication capabilities, B) Centimeter-accurate positioning (e.g., GPS-RTK), and C) Standard vehicle-to-infrastructure (V2I) interfaces. 

Assumption 2: The framework operates under ideal communication conditions during normal operation, with A) Zero-latency data transmission, B) Perfect sensor accuracy, and C) Continuous system availability. Communication failures and sensor errors are excluded from the current modeling scope. 

Assumption 3: During communication interruptions or turesystem failures, CAVs immediately activate onboard failsafe protocols including conservative car-following models and graceful degradation to autonomous emergency braking, framework control authority is suspended, and safety responsibility reverts to vehicle-level autonomy. 

# 3.2. Data Acquisition

The framework operates across three functional zones: prediction, decision-making, and control. In the Prediction Zone, real-time traffic data—including vehicle speed, position, and flow rates—is collected using sensors and RSUs. The DRL agent processes this data using a CAE to compress and extract relevant traffic features. This compression helps 

enhance the agent’s ability to adapt to dynamic traffic conditions by reducing the dimensionality of input data while preserving essential traffic patterns. The resulting traffic state representations form the basis for the agent’s decisionmaking process. 

# 3.3. High-Level Decision-Making Layer

This layer reduces algorithmic complexity and computational cost using VTS technology. Inspired by the Learning Options Framework Stolle and Precup (2002), it employs temporally extended actions to reduce decision frequency. This allows commitment to sequences (e.g., keep Green until the mainline vehicle appears) and leverages prior knowledge (e.g., if no car, signal Green), enhancing learning efficiency and robustness without complex macro-actions. Merging is structured into discrete time windows where on-ramp and mainline vehicles select slots, improving decision efficiency while enabling real-time adaptation. 

The VTS two-phase signal replaces fixed systems (e.g., ramp metering), dynamically guiding vehicles using realtime conditions to optimize flow and safety. Signal logic switches between Yielding (Y) and Green (G) as follows: 

# 1) Mainline Vehicle Priority:

A) If the new vehicle is on the mainline road and an optimal merging window is available (or can be created), it selects this window. 

B) If the optimal window is unavailable, the vehicle merges into the first available window following the optimal slot. 

# 2) Ramp Vehicle Behavior:

A) If the last vehicle in the merging sequence is on the on-ramp, the system selects the first available window for the next vehicle. 

B) Otherwise, the system iterates through available merging windows, checking for gaps after the preceding vehicle. 

C) If sufficient space exists (or can be created), the window is selected, ensuring smooth and efficient merging. 

The VTS signal transitions between Yielding (Y) and Green $( G )$ based on the availability of merging gaps and the priority of vehicles: 

1. Switch from Yielding to Green $Y  G ,$ ): Occurs when a sufficient gap $( \geq 2 . 0 \mathrm { s }$ time gap or $\ge 1 5 \mathrm { m }$ distance gap at merging point) is detected in mainline traffic and the merging vehicle is prepared. The Green phase permits ramp entry while maintaining traffic flow, and may extend to accommodate multiple vehicles when large gaps exist. 

2. Switch from Green to Yielding $( G \to Y )$ : Triggers if merging is not completed within the allocated window (4.0s maximum) or when insufficient gaps $( < 2 . 0 s$ time gap) are detected, preventing disruptive merge attempts. 

Note: The quantitative thresholds above represent baseline values used in our simulations. The actual VTS switching mechanism is intrinsically linked to the DRL action space design and merging sequence optimization, which are formalized in Sections 4.4.2 and 4.5.2 through our reinforcement learning framework. Specifically, the agent dynamically adjusts these thresholds based on real-time traffic states during the sequence determination process. 

Within this framework, our DRL agent employs a CNNbased dueling network to approximate action Q-values. By continuously evaluating traffic states through CAEenhanced representations, the agent applies a reward function penalizing delays, fuel inefficiency, and safety violations to dynamically determine merging sequences. This integration enables more robust, context-aware decisions than traditional ramp metering, with the VTS two-phase signal serving as an integrated communication channel that ensures efficient merging while minimizing disruptions. 

# 3.4. Low-Level Control Layer

Once the DRL agent makes a decision, the OCP module refines the chosen action by calculating the precise control actions, such as the optimal speed and trajectory, required to implement the merging sequence effectively. These decisions are executed within the control zone, defined as the final 200 meters before the merge point. This distance was selected based on standard operational requirements to ensure vehicles have sufficient time to adjust their speed and trajectory effectively for smooth merging. It should be noted, however, that the optimal length of the Control Zone may vary depending on traffic speed and conditions. Higher traffic speeds, for instance, may require an extended Control Zone to accommodate the time needed for safe adjustments, while lower speeds may allow for a shorter zone. The VTS continues to play a critical role, providing real-time guidance to vehicles in the merging zone based on the optimal speed profiles generated by the OCP. This helps ensure that vehicles follow smooth trajectories without abrupt braking or acceleration, improving both safety and efficiency. 

Real-time communication through the VTS ensures that all vehicles are synchronized with the merging strategy, resulting in reduced delays, improved traffic flow, and decreased fuel consumption. By dynamically adjusting speed profiles and merging sequences, the system mitigates congestion and optimizes vehicle interactions, thus validating the framework’s ability to enhance merging efficiency compared to traditional, more rigid systems. 

# 3.5. Baseline Control Approach

This study employs SUMO’s default Krauss model as a conventional benchmark. This widely adopted car-following model simulates vehicle dynamics by adjusting speed based on headway, desired velocity, and acceleration constraints. Within merging scenarios, it operates without explicit control strategies; vehicles merge reactively based on innate carfollowing logic, representing an uncontrolled baseline. 

While effective for general traffic simulation, the Krauss model is inherently limited. It lacks the capacity to optimize 

merging operations or adapt to real-time traffic states. This contrasts sharply with our proposed DRL based hierarchical control system, which is explicitly designed for dynamic, data-driven optimization. 

A review of the literature confirms that a hierarchical framework integrating data-driven and model-based methods remains unexplored for on-ramp merging. Consequently, the Krauss model is selected as a pertinent and widely recognized comparative baseline. Future research will expand this comparison to include traditional ramp metering strategies, evaluating performance gains in merging efficiency, safety, and fuel consumption across more complex, multilane mixed traffic environments. 

# 4. Methodologies

This section details the methodology for implementing and evaluating the proposed hybrid control framework for CAVs. The methodology includes the design of a DRLbased controller, the optimization of merging sequences, and the formulation of an OCP to compute optimal vehicle speed profiles. We begin by outlining the theoretical foundation of the framework, followed by a description of the simulation environment, including traffic scenarios, vehicle parameters, and the software tools used for modeling and simulations. The core OCP formulation has been addressed in our previous studies Shi, Wang, LaClair, Wang and Yuan (2022); Shi, Wang, LaClair, Wang and Shao, and readers are encouraged to refer to those works for details. 

# 4.1. DRL Insights

This subsection delves into key DRL techniques, including DQN and its advanced variants—Double DQN, Dueling DQN, and Prioritized Experience Replay—that enhance the efficiency and stability of learning processes in complex environments 

# 4.1.1. Deep Q-Network (DQN)

DQN combines Q-learning with deep neural networks to approximate the optimal action-value function in highdimensional state spaces, useful for complex tasks like traffic signal control and merging decisions Deniz, Wu, Shi and Wang (2024); Muzahid et al. (2022). 

• $Q$ -Learning Objective: The Q-value function $Q ( s , a )$ estimates the expected reward of taking action ?? in state $s$ : 

$$
Q (s, a) = \mathbb {E} \left[ r _ {t} + \gamma \max _ {a ^ {\prime}} Q (s ^ {\prime}, a ^ {\prime}) \mid s, a \right]
$$

where $r _ { t }$ is the immediate reward, ?? the discount factor, and $s ^ { \prime } , a ^ { \prime }$ the next state and action. 

• Loss Function: The Q-network is trained by minimizing the difference between predicted and target Qvalues: 

$$
L (\theta) = \mathbb {E} _ {(s, a, r, s ^ {\prime})} \left[ \left(r + \gamma \max  _ {a ^ {\prime}} Q (s ^ {\prime}, a ^ {\prime}; \theta^ {-}) \right. \right.
$$

$$
\left. - Q (s, a; \theta)) ^ {2} \right]
$$

Here, $\theta$ are the Q-network parameters, and $\theta ^ { - }$ are the periodically updated target network parameters. 

In our study, DQN optimizes vehicle merging decisions using traffic parameters (vehicle speed and position) as input states and traffic efficiency as a reward. 

# 4.1.2. Double DQN

Double DQN reduces overestimation bias in DQN by decoupling action selection from target Q-value evaluation Van Hasselt, Guez and Silver (2016). 

• Target Q-Value: 

$$
Q _ {\text {t a r g e t}} (s, a) = r + \gamma Q \left(s ^ {\prime}, \arg \max  _ {a ^ {\prime}} Q \left(s ^ {\prime}, a ^ {\prime}; \theta\right); \theta^ {-}\right)
$$

The online network parameters $\theta$ select the action, while $\theta ^ { - }$ evaluates it. 

In the merging scenario, Double DQN improves decision accuracy by mitigating overestimation, enhancing traffic flow and safety. 

# 4.1.3. Dueling DQN

Dueling DQN separates the state-value function and the advantage function to improve learning efficiency Wang, Schaul, Hessel, Hasselt, Lanctot and Freitas (2016). 

• Dueling Architecture: 

$$
Q (s, a; \theta) = V (s; \theta) + \left(A (s, a; \theta) - \frac {1}{| A |} \sum_ {a ^ {\prime}} A (s, a ^ {\prime}; \theta)\right)
$$

This architecture distinguishes valuable states and advantageous actions, improving decision-making in merging scenarios. 

# 4.1.4. Prioritized Experience Replay

Prioritized Experience Replay enhances learning by sampling transitions with higher Temporal Difference (TD) error, accelerating learning in critical scenarios Deniz et al. (2024). 

• Priority Calculation: 

$$
p _ {i} = \left| r + \gamma \max _ {a ^ {\prime}} Q (s ^ {\prime}, a ^ {\prime}; \theta^ {-}) - Q (s, a; \theta) \right| + \epsilon
$$

• Sampling Probability: 

$$
P (i) = \frac {p _ {i} ^ {\alpha}}{\sum_ {k} p _ {k} ^ {\alpha}}
$$

• Importance Sampling Weights: 

$$
w _ {i} = \left(\frac {1}{N} \cdot \frac {1}{P (i)}\right) ^ {\beta}
$$

In merging scenarios, transitions with high TD errors, such as critical merging decisions, are prioritized to improve learning efficiency. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/a43a85eba04711fefbd6e658c108fc25fa4b7e543f99251147658fad82db16a4.jpg)



Figure 2: Depiction of the merging scenario used in simulations.


# 4.2. Optimal Merging Speed Control of CAVs

The optimal merging speed control for CAVs can be formulated as a nonlinear OCP to minimize a cost function over a time horizon, optimizing speed profiles while considering factors like fuel consumption, safety, and passenger comfort Zhou, Wang and Cook (2023). 

• OCP Formulation: 

$$
\begin{array}{l} J = \int_ {0} ^ {T} \left(\alpha_ {1} \dot {v} (t) ^ {2} + \alpha_ {2} (v (t) - v ^ {*}) ^ {2} + \alpha_ {3} \left(\frac {1}{d (t)}\right) ^ {2} \right. \\ \left. + \alpha_ {4} a (t) ^ {2}\right) d t \\ \end{array}
$$

where $v ( t )$ is the speed, $d ( t )$ the distance to the preceding vehicle, and $a ( t )$ the comfort term. 

# 4.2.1. Vehicle Dynamics and Problem Formulation

Vehicle dynamics can be expressed as Rios-Torres and Malikopoulos (2016): 

$$
m \dot {v} = \frac {T _ {e}}{r _ {g}} - F _ {b} - F _ {\text {a e r o}} - F _ {\text {o t h e r}}
$$

with forces such as aerodynamic resistance $F _ { \mathrm { a e r o } }$ and frictional forces ??other. $F _ { \mathrm { o t h e r } }$ 

• Constraints: 

$$
v _ {\min } \leq v (t) \leq v _ {\max }, \quad x _ {p} (t) - x (t) \geq R _ {0}
$$

# 4.2.2. MPC

MPC solves the OCP iteratively over a rolling time horizon, applying the first control input and updating the state at each time step Zhou et al. (2023). This real-time approach allows for dynamic adjustments, ensuring optimal speed control during merging processes. 

• Iterative Solution: 

$$
\min  _ {u (t)} \int_ {0} ^ {T} L (x (t), u (t)) d t + \phi (x (T))
$$

subject to system dynamics: 

$$
\dot {x} (t) = f (x (t), u (t)), \quad x (0) = x _ {0}
$$

The rolling horizon approach continuously updates state and control variables based on real-time data, optimizing the merging process dynamically. 

# 4.3. Role of the DRL Agent

In the simulation, the traffic signal at the merging area is controlled by a DRL agent. The agent receives continuous updates on traffic states and reward signals from the environment, enabling it to take actions that optimize traffic flow. By learning from these interactions, the agent adapts its strategy to ensure efficient and safe merging. 

# 4.4. Simulation Environment

This subsection outlines the core elements of the simulation environment, including the encoding of traffic states, action space, reward signal, and the DRL structure used to optimize traffic management. 

# 4.4.1. Encoding Traffic States

Similar to DRL-based intersection management Shi, Wang, LaClair, Wang, Shao and Yuan (2023a), the traffic state in the merging zone is represented by the position and speed information of vehicles, encoded into a discrete matrix format Genders and Razavi (2016). The simulated intersection shown in Fig. 2 is divided into mesh grids, represented as an $N \times N$ matrix. Each grid cell contains two values: a binary indicator of vehicle presence and a numerical value for vehicle speed. For instance, Fig. 3 illustrates a $1 0 0 \times 3$ traffic state matrix. 

More specifically, each matrix entry encapsulates two essential pieces of information regarding the vehicles: 

1. A binary value $( b )$ indicating vehicle presence: 

• $b = 1$ : A vehicle is present in the grid (yellow grid). 

• $b = 0$ : The grid is vacant. 

2. A numerical value (??) representing the speed of the vehicle (measured in meters per second, $m / s$ ), applicable only if $b = 1$ . 

As an illustrative example, consider the traffic state in a $1 0 0 \times 3$ matrix, as depicted in Fig. 3. This matrix is defined as follows: 

$$
M = \left[ \begin{array}{c c c} (1, 2 0) & (0, 0) & (1, 1 5) \\ (1, 2 5) & (0, 0) & (1, 1 0) \\ \vdots & \vdots & \vdots \\ (0, 0) & (0, 0) & (1, 5) \end{array} \right]
$$

In this matrix, $M$ , each tuple like (1, 20) indicates that a vehicle is present and is traveling at a speed of $2 0 ~ m / s$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/92339277a8c5bcbfbcf66acea0757f4f4819ca064cc19cf98b5e39c800e38b12.jpg)



Figure 3: Example of a traffic state matrix.


A tuple $( 0 , 0 )$ signifies an empty grid cell, indicating the absence of a vehicle. 

# 4.4.2. Action Space

In RL-based signal control, the action space involves selecting traffic signal phases. For this research, we define a discrete action space with two options: 

1. Green Phase (G) 

2. Yielding Phase (Y) 

The agent selects actions at fixed intervals $\Delta t$ , determining whether to maintain or switch the current phase. Mathematically: 

$$
a _ {t} \in \{G, Y \}, \quad a _ {t + 1} = \left\{ \begin{array}{l l} a _ {t} & \text {i f p h a s e c o n t i n u e s} \\ \text {n o t} a _ {t} & \text {i f p h a s e s w i t c h e s} \end{array} \right.
$$

We balance simplicity and effectiveness by simplifying the DRL agent’s action space to just two options—Yield or Green. This design, which draws inspiration from the concept of temporally extended actions in the Learning Options Framework Stolle and Precup (2002), allows the agent to focus on optimizing merge timing rather than managing continuously evolving signal states. 

This approach enhances both learning efficiency and decision robustness without the need to define complex macro-actions. 

# 4.4.3. Rewards Signal

The reward signal is crucial in RL-based signal control, guiding the agent’s learning objectives. In traffic signal control, the goal is to enhance system efficiency by increasing throughput or reducing waiting times. Since traffic signal control lacks a terminal state, continuous action assessment is essential, and the reward must reflect the immediate outcomes of each action. 

Common performance indices include travel delay, queue length, and average vehicle speed Guo, Li and Ban (2019), which influence strategy outcomes: 

1. Average Vehicle Speed: High average speed can indicate improved traffic flow. The reward $R$ is defined as: 

$$
R = \bar {V} = \frac {1}{T} \sum_ {t = 1} ^ {T} \frac {1}{N} \sum_ {i = 1} ^ {N} v _ {i}, \tag {1}
$$

where $v _ { i }$ is the speed of vehicle ??, ?? is the signal cycle length, and $N$ is the number of vehicles. 

2. Cumulative Waiting Time: This measures the total time vehicles travel below a minimal speed (e.g., 0.1 m/s), incrementing by $+ 1$ whenever a vehicle is in slow traffic. 

3. Vehicle Density: Calculated as the number of vehicles divided by the road length, this metric reflects realtime congestion. The reward can be defined as $\begin{array} { r } { R = \frac { 1 } { D } } \end{array}$ , where $D$ is vehicle density, rewarding the agent for reducing congestion. 

Each reward type influences agent behavior differently. Using average speed promotes efficient flow but may lead to strategies that increase fuel consumption due to frequent signal changes. Focusing on waiting time or density can make the agent overly reactive to immediate conditions. Carefully defining reward signals helps tailor RL algorithms to optimize traffic control under varied conditions. 

# 4.4.4. DRL Structure

The DRL model used in this study is based on a threelayer convolutional neural network (CNN), a fully connected layer, and a dueling network architecture depicted in Fig. 4. The CNN extracts features from traffic state matrices, converting them into feature vectors. The fully connected layer approximates the Q-value function, estimating potential rewards for different actions based on the current state. At the end of each control cycle, the traffic state matrices are input into the network, which calculates the Q-values for all possible actions. The agent selects the action with the highest Q-value, thereby maximizing the expected reward and executing the corresponding action. 

The hyperparameters summarized in Table 3 play a crucial role in determining the model’s performance. The choice of 3,600 simulated time steps per episode ensures sufficient training data for the agent to explore the environment and refine its decision-making. The replay memory size of 20,000 is designed to store a diverse set of experiences, which helps prevent overfitting and promotes generalization. A minibatch size of 64 balances the need for computational efficiency with stability in training, ensuring meaningful updates to the model. The discount factor of 0.99 enables the agent to appropriately value long-term rewards, while the target network update rate of 0.001 maintains stability by preventing drastic changes in the target network during training. The exploration parameters—starting at 1 and decaying to 0.01—ensure that the agent initially explores the environment thoroughly before exploiting the learned policy as training progresses. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/72866763a48cecd666871923bdee1d540413bab7c8536e9cff99a3927b63f9f2.jpg)



Figure 4: Structure of the proposed DRL model.


Additionally, the model incorporates advanced techniques such as Double DQN Van Hasselt et al. (2016), dueling network architecture Wang, Schaul, Hessel, Van Hasselt, Lanctot and De Freitas (2015), and prioritized experience replay Schaul, Quan, Antonoglou and Silver (2015). These methods improve the accuracy of Q-value estimation, increase training efficiency, and enhance the agent’s ability to learn from more significant experiences, respectively. The pseudocode for the training process is provided in Algorithm 1. The combination of these parameter choices and network structure directly influences the DRL model’s ability to efficiently solve the problem, making it well-suited for realtime decision-making in complex traffic scenarios. Future work will further explore the impact of varying network depth, convolutional layer configurations, and explorationexploitation trade-offs on performance. 

# 4.5. Merging Decision and Speed Optimization

After obtaining the merging decision, we aim to optimize the overall process flow of the proposed framework using three techniques, implemented across three consecutive phases. The framework efficiently handles merging decisions and optimizes vehicle speeds through a combination of DRL and OCP solvers. The DRL decision-making process is computationally efficient, enabling real-time adjustments to traffic conditions by selecting optimal merging sequences within short time windows (e.g., 3 seconds). This aligns well with the requirements of real-time traffic management systems. While the OCP solver may require longer computation times, especially in high-density traffic scenarios, the system leverages parallel computing and precomputation techniques to maintain efficiency and ensure real-time operation. A detailed hardware description can be found in section 7.3. 

# 4.5.1. Compressed Traffic State Representation

An effective and compact representation of the traffic state is essential for robust data-driven control. Traditional methods, which often rely on raw positional and velocity data of CAVs, provide a snapshot at the end of a control cycle but fail to encapsulate the evolving spatial and temporal patterns within that interval. 

To overcome this limitation, we employ a CAE to learn a low-dimensional latent representation of the traffic state. 


Algorithm 1: DQN Algorithm


Input: mini batch size $B$ pre-train step $t_p$ training episode length $N$ , learning rate $\alpha$ greedy $\epsilon$ discount factor $\gamma$ target network update rate $\tau$ , target network update frequency $K$ Output: Trained primary network $Q_{\theta}$ Initialize primary network $Q_{\theta}$ , target network $Q_{\theta^{-}}$ replay memory $D$ with capacity $M$ .   
while each episode do Initialize simulator environment ; Initialize time step $t = 0$ . Observe current state $S_{t}$ . while time step $t <   N$ do With probability $\epsilon$ select action $A_{t}$ randomly; otherwise select $A_{t}\gets \arg \max Q_{\theta}(S_{t},a)$ Execute action then observe next state $S_{t + 1}$ and reward $R_{t}$ . Store $(S_{t},A_{t},R_{t},S_{t + 1})$ in replay memory $D$ .. $S_{t}\gets S_{t + 1}$ . if current step $t >$ pre-training step $t_p$ then Sample a minibatch of $B$ experience tuples $(S_{t},A_{t},R_{t},S_{t + 1})$ from $D$ . Compute target Q values for each experience: ; $Q^{*}(S_{t},A_{t})\approx R_{t}+$ $\gamma Q_{\theta^{-}}(S_{t + 1},\arg \max_{a^{\prime}}Q_{\theta}(S_{t + 1},a^{\prime}))$ Perform a gradient descent step with loss $\frac{1}{B}\| Q^{*}(S_{t},A_{t}) - Q_{\theta}(S_{t},A_{t})\|^{2}$ end Update target network $\theta^{-}$ every $K$ steps: $\theta^{-}\gets \tau \theta +(1 - \tau)\theta^{-}$ . t $\leftarrow t + 1$ end 

This approach compresses complex input data into a dense feature vector that preserves critical spatial relationships and patterns, thereby mitigating the curse of dimensionality and providing a more informative state signal for reinforcement learning. 

Inspired by architectures such as VGG networks Simonyan and Zisserman (2014), a convolutional encoderdecoder model is trained to reconstruct its input, forcing the encoder to learn efficient representations of the underlying traffic structure. The resulting compressed state vectors serve as a rich input feature space for the DRL agent. 

This compressed representation is integrated directly into the DRL control loop. The encoder module generates real-time state embeddings, which condition the agent’s policy and enable more efficient learning and decision-making, as implemented in the DQN algorithm (Algorithm 1). 

# 4.5.2. Merging Sequence Determination

The method first-in-first-out is a popular and straightforward approach, which prioritizes vehicles by arrival time or distance from the merging zone. Although FIFO is efficient in optimizing travel time, it neglects fuel efficiency, as shown in previous research Jing, Hui, Zhao, Rios-Torres and Khattak (2019b), Chen, van Arem, Alkim and Wang (2020b). These studies have introduced various optimization techniques for merging sequences, but as the number of vehicles increases, the computational complexity increases factorially, limiting real-time applications. 

To tackle this, cooperative rules Shi et al. (2022) were developed to balance efficiency and solution quality, though they may not perform well under dynamic traffic conditions. This research employs DRL to enhance merging operations in complex environments, offering adaptability and realtime decision-making capabilities, unlike static rule-based methods Zhou, Peeta, Zhou, Laval, Wang and Cook (2024). 

The merging process is divided into equal time windows, during which a vehicle from different roads can merge. For example, with a 3-second window, the DRL agent generates a sequence for each control cycle, and CAVs select their merging windows. The sequence is generated at the start of one cycle and executed at the end. Experimental training determined the optimal merging window length and sequence size, affecting the action space of the DRL agent. For instance, a sequence of 10 windows yields 1,024 possible actions. 

Signal Cycle Length: The signal cycle length in the experiments was set to 5 seconds, establishing a minimum green window duration of 5 seconds for on-ramp vehicles. Given a maximum vehicle speed of $3 0 \mathrm { m / s }$ , this duration is slightly longer than necessary for a single vehicle to merge. The VTS on the ramp road was implemented to regulate vehicle merging and prevent interference with mainline road traffic. The green window length is designed to match the available gaps between vehicles on the mainline road and can be extended if a large gap can accommodate multiple vehicles. 

# 4.5.3. Optimal Merging Speed Control of CAVs using DRL Results

Following the determination of merging windows by the DRL controller, vehicles are assigned reference speed 

profiles obtained from a nonlinear OCP. This OCP minimizes a cost function incorporating fuel consumption, safety distance, desired speed, and passenger comfort. Rather than employing a terminal constraint, the merging window itself defines the speed reference. The solution is implemented in real-time through a MPC framework applied over a rolling horizon T, as detailed in Shi et al.. 

Control objectives differ between on-ramp and mainline vehicles. Reflecting real-world traffic norms, on-ramp vehicles yield to mainline traffic, typically reducing speed to merge safely. This prioritization helps maintain mainline flow, though alternative strategies under low-density conditions present a valuable direction for future research. 


Algorithm 2: Pseudocode for the selection of merging window


Input: Vehicle entry type (ramp or mainline), traffic data   
Output: Selected merging window   
Function SelectMergingWindow(): if vehicle_entry_type $= =$ "mainline" then if is_optimal_merging_window-available( ) then return select_window("optimal"); else return selec_twindow("first-available_after_optimal"); else if is_lastvehicle_on_ramp() then else foreach window in get_avail- able_windows_after_last_rampvehicle( ) do if is_space_afterVehicle窗口) then Select the window i; break; else Select the window i;

Vehicles encounter two scenarios when selecting a merging window: 

1. Entering the Control Zone: As shown in Algorithm 2, mainline vehicles aim to maintain fuel efficiency by driving at a desired speed, while on-ramp vehicles must merge at the first available window to optimize flow and road capacity. 

2. New Merging Sequence: When a new merging sequence is determined, unassigned vehicles are allocated windows. On-ramp vehicles take the first available window, and mainline vehicles may accelerate to the nearest available window if needed. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/9883053898a259cea54ac87d06bb2138c8f8608d76bd7d4f2631c8a03885a9d2.jpg)



Figure 5: The structure of the proposed CAE for traffic state representation.



Table 2 Parameters of vehicle dynamics.


<table><tr><td colspan="2">Parameter (Unit)</td><td>Value</td><td colspan="2">Parameter (Unit)</td><td>Value</td></tr><tr><td>m</td><td>(kg)</td><td>1200</td><td>uemax</td><td>(m/s2)</td><td>3</td></tr><tr><td>ρ</td><td>(kg/m3)</td><td>1.184</td><td>ubmax</td><td>(m/s2)</td><td>3</td></tr><tr><td>A</td><td>(m2)</td><td>2.5</td><td>vmax</td><td>(m/s)</td><td>20</td></tr><tr><td>CD</td><td>(lengthless)</td><td>0.32</td><td>vmin</td><td>(m/s)</td><td>0</td></tr><tr><td>g</td><td>(m/s2)</td><td>9.8</td><td>μ</td><td>imensionless)</td><td>0.015</td></tr><tr><td>α0</td><td>(mL/s)</td><td>0.1569</td><td>β0</td><td>(mLs/m)</td><td>0.07224</td></tr><tr><td>α1</td><td>(mL/m)</td><td>2.450e-2</td><td>β1</td><td>(mLs2/m2)</td><td>9.681e-2</td></tr><tr><td>α2</td><td>(mLs/m2)</td><td>-7.415e-4</td><td>β2</td><td>(mLs3/m3)</td><td>1.075e-3</td></tr><tr><td>α3</td><td>(mLs2/m3)</td><td>5.975e-5</td><td>R0</td><td>(m)</td><td>2.5</td></tr><tr><td>thd</td><td>(s)</td><td>1.3</td><td></td><td></td><td></td></tr></table>

# 5. Validation of the Control Module

This section focuses on the validation of the DRL module, starting with the setup and tools used for implementation. It covers the performance evaluation of the CAE, integration with the new DRL model, and presents key simulation results, including analyses of signal cycle length, traffic state optimization, merging sequences, and speed profiles. 

# 5.1. Setup and Tools

The simulation environment was built using SUMO (Simulation of Urban MObility), a microscopic, spacecontinuous traffic simulation software that provides detailed information about the simulated objects and allows for parameter adjustments at each time step Lopez, Behrisch, Bieker-Walz, Erdmann, Flötteröd, Hilbrich, Lücken, Rummel, Wagner and WieBner (2018). This setup enables precise modeling and simulation of the traffic environment, facilitating the development and testing of the DRL-based control model. Fig. 2 depicts the traffic environment considered for this study, with the two sharp arrows indicating vehicle motions and the blue line marking the beginning of the control zone. Fig. 1 clearly illustrates this setup. 

# 5.2. Primary Results and Analysis

The simulation environment was configured with a 400- meter control zone and a 100-meter merging zone, using a 5-meter traffic state grid resolution. Vehicles were generated stochastically on each road with a $2 0 \%$ probability per second, corresponding to an average arrival rate of one vehicle 

every 5 seconds. All vehicles shared identical kinematic parameters (Tab. 2), with a maximum speed set at $3 0 \mathrm { m / s }$ . 

The DRL agent was trained using three distinct reward signals. Training results, summarized in Fig. 6, indicate a consistent improvement in performance across episodes: average waiting time decreased, average vehicle speed increased, and cumulative rewards rose. These trends confirm the agent’s capability to learn effective control policies autonomously. 

A comparative analysis of the reward structures revealed similar learning efficiency among all three. However, the reward signal corresponding to the results in Fig. 6 yielded superior convergence behavior, as evidenced by smoother learning curves and more optimized performance metrics in both waiting time and vehicle speed. 

# 5.3. Implementation and Training of CAE

The architecture of the proposed CAE, shown in Fig. 5, consists of two main components: the encoder and the decoder, arranged in a mirror structure. The CAE is trained to reconstruct the original input through a designated bottleneck layer, denoted as h. The input and output of the CAE are traffic state matrices with dimensions $1 0 0 \times 3 \times 2$ . The encoder comprises two pairs of convolution-pooling layers, followed by two fully-connected layers, while the decoder mirrors this structure. The dimensions of the output at each layer are defined by specific notations. 

The CAE is implemented and trained using TensorFlow Pang, Nijkamp and Wu (2020), with the Adam optimization algorithm Kingma and Ba (2014) and Mean Squared Error (MSE) as the cost function. L2 regularization is applied to the weights of the network to prevent overfitting and ensure generalization. The number of CNN filters, neurons, and other hyperparameters are determined through crossvalidation experiments. The input state matrix undergoes normalization, scaling the velocity between 0 and 1 based on the maximum allowable speed of the road. 

# 5.3.1. Performance Evaluation

We test how well the CAE works with a validation set that makes up $1 0 \%$ of the whole dataset. With the help of SUMO, we can model the traffic signal control system and create a training dataset in real time. At startup, each vehicle is given a random flow rate. In Fig. 7, we can see a sample training session that used one million samples and achieved minimum reconstruction errors of 6.37e−4 for 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/c0ed644820898bcf91dd041f1855e82e46a23cbda45954e32786f11c1556d56e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/243770ea305b2451f38719e7cac1811d22cd8a9576764e51d0d5deba360a8fbd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/32e0416584be430fec53995c0246d91d5ee8a59ac0331aa09076704da7ac4d80.jpg)



Figure 6: Training history of DRL agent with average speed as reward signal.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/1352a2a0d2cb75e26280aca76ed2713fcd1190bd37998a04a7fc605b730636e6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/8476e1ad8628c6ab16396311d91fe1447603be4f4e21a7aca3814ec9eedd5ca9.jpg)



Figure 7: Training history of the proposed CAE.


training and 6.35e−4 for validation. Reconstruction errors are higher when the buried layer size in Fig. 8 is smaller. 

The main purpose of employing a CAE is to extract intrinsic traffic properties while simultaneously compressing the dimensions of the traffic state. The efficiency of the CAE is therefore confirmed within the reinforcement learning control framework. Though they may have an adverse effect on the performance of the reinforcement learning method, larger hidden layer sizes can decrease reconstruction loss. The training of DRL agents involves experimenting with different hidden layer sizes. 

# 5.3.2. Integration with New DRL Model

The next step involves integrating the trained CAE with the DRL-based signal control model. The encoder generates traffic state representations, which serve as intermediate 

variables to guide the DRL agent’s decision-making process. The DRL model enables the agent to learn optimal policies using the reinforcement learning algorithm described in Algorithm 1. 

# 5.3.3. Simulation Results of New DRL Model

The integration of the new DRL model was evaluated by examining the cumulative rewards per episode, validating the convergence of the DRL training algorithm. In Fig. 9, the first plot shows the average waiting time per episode, the second plot presents the average vehicle speed, and the third plot illustrates the cumulative rewards per episode. As the training progresses, we observe a steady reduction in average waiting time and a corresponding increase in average vehicle 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/81a6e1fba6159619a2ca6d9f2cf61d57ff3f7a6405cce004db880d4c6648f35c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/a32be324ad7252bc74490dcb1b982e65ed3c839eb1c809892ef5040d0891507e.jpg)



Figure 8: Training history of the proposed convolutional AutoEncoder (smaller size of hidden layer h).


speed, indicating improved traffic flow management and better coordination between vehicles. 

The results in Fig. 9 demonstrate that the new DRL agent, which utilizes compressed traffic states, converges more quickly and achieves slightly improved performance compared to the traditional DRL model. The smoother curves in Fig. 9 indicate better optimization, with a noticeable reduction in vehicle delays (represented by the decrease in waiting time) and an increase in traffic flow efficiency. 

In summary, the new DRL model demonstrates improved traffic flow management, with reduced waiting time and enhanced vehicle speeds, confirming its effectiveness in optimizing signal control and minimizing vehicle delays. 

# 5.3.4. Analysis of Signal Cycle Length

The experiments above set the signal cycle length to 5 seconds, resulting in a minimum green window duration of 5 seconds for on-ramp vehicles. Considering the maximum vehicle speed of $3 0 \mathrm { m / s }$ , this duration is slightly longer than necessary for a single vehicle to merge. The goal of using a VTS on the ramp road is to regulate vehicle merging and avoid interference with mainline road traffic. Therefore, the green window length should match the available gaps between vehicles on the mainline road. Additionally, we can extend the green window if there is a large gap that can accommodate multiple vehicles. 

To determine the suitable signal cycle length, a series of simulations were performed. As shown in Fig. 10, when the signal cycle length is set to 3 seconds, the training curves exhibit greater fluctuations. Although the maximum average speed achieved is similar to that in Fig. 9, the results do not appear to converge. 

In Fig. 10, further training could potentially improve performance, but this raises another issue: determining the appropriate time for the agent to plan the next signal for an upcoming vehicle. Currently, the agent decides the next signal every few seconds. This setup prevents both the agent and drivers from anticipating the exact merging time until the vehicle is very close to the merging zone, leading to three problems: 

- The agent focuses more on short-term rewards and cannot learn a policy to manage traffic flow across the entire scenario. 

- To avoid sudden stops, vehicles cannot confidently approach the merging zone at higher speeds. 

- The virtual light cannot assist CAVs in planning their trajectory in advance. Based on these considerations, extending the signal control cycle length while shortening phase durations is reasonable. Instead of deciding one phase at a time, the agent outputs a sequence of signal phases, allowing vehicles to plan their trajectory. This approach improves overall performance by providing more comprehensive control policies. In Fig. 11, the signal control cycle length is set to 30 seconds with each phase duration of 3 seconds. This setup shows more evident convergence, with slightly improved average waiting times and vehicle speeds. A 15-second control cycle with 3-second phase durations was also tested, as shown in Fig. 12, resulting in faster convergence but poorer performance compared to Fig. 11. Additionally, Fig. 13 presents the training history of a DRL agent with a 20-second signal control cycle and a 2-second phase duration, demonstrating faster convergence than Fig. 11 while achieving similar performance. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/1cede04b1c584f2f8223c320b4148b64278f38b0d045a35bc6c87e1e3483591c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/b3b03f2019bbc7ebb6cc3fb8f42ab80e11ab5b37ff90e99d6957913c97b678f4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/892fa8066490439666169bd42f1e9b999a17fbd96c98244255e4853bf1d4a44e.jpg)



Figure 9: Training history of DRL agent with compressed traffic states and average speed as reward signal.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/75f76555721442c97186de68f276ee4ae34103f9a08938273334896ef34867ac.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/31c763b72f20f66f55ba424829f015ad958b54cff2d228c0c14120ee3c755f66.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/c03bba5f6495ed227a8f14c8573c53873f1c54578fb955ab07ca49b1117da7fb.jpg)



Figure 10: Training history of DRL agent with a signal cycle length of 3 seconds and average vehicle speed as reward signal.


# 5.3.5. Determining Optimal Size of Traffic State

To determine the optimal size of the input traffic state, various training experiments with different trained encoders were conducted. For brevity, we present Fig. 14, which shows the training history with a traffic state size of 32. 

The first plot in the figure demonstrates the average waiting time per episode, the second plot shows the average vehicle speed, and the third plot illustrates the cumulative rewards per episode. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/fbd698f1266080fa24d2e59055f388630384c190967fbd941c1a8cda33284a2f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/f8818235badfce39d08e4ed785b5f6349f3a9798a3ccc03fe542f122ab2828ad.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/dae364f9a38921096f1d403e6be0d1c28a566d8db65563807cabe9553384eb33.jpg)



Figure 11: Training history of DRL agent with a signal cycle length of 30 seconds and average vehicle speed as reward signal.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/94f088e8a9cbb22d2a736d76adfedb8264e250835a8bb567b8b010618ec1fa25.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/d3d5f0abc2f25b13f787a9fc600a8012ee38ea69bcdb674a84ac67c4a525a377.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/eef0b71ab83c236bdc680ffd46c143763d8cdd9540f3f12a4e432b26d679457e.jpg)



Figure 12: Training history of DRL agent with a signal cycle length of 15 seconds and average vehicle speed as reward signal.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/c734cb9877e58704a688dd716426e342facfa0a5af3077c01b87fc75b64cba1e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/ff1ce273b5e6174c6d2778108278bf394a485f1294f9b65c2088fc417d1c48c3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/e6d899d12a2b0bd7115946506eca3d4b814c53098b13402c502e9936839db789.jpg)



Figure 13: Training history of DRL agent with a signal cycle length of 20 seconds and average vehicle speed as reward signal.


Despite the improvements observed during training, the results from the training history in Fig. 14 indicate that a traffic state size of 32 is suboptimal. The trends in the figure show that although there are some improvements, the system’s performance does not reach satisfactory levels with this traffic state size. This suggests that a larger or different traffic state size may be necessary for optimizing the system’s performance. 

# 5.4. Analysis of Merging Sequence Determination

Initial implementation of the first-in-first-out (FIFO) rule provided a simple, travel-time efficient merging strategy. However, its limitations in optimizing fuel efficiency became apparent. While sequence optimization methods exist Jing et al. (2019b); Chen et al. (2020b), they face computational intractability for real-time application due to factorial complexity growth with increasing vehicle numbers. 

In contrast, the DRL approach demonstrated superior adaptability in handling complex, uncertain traffic conditions compared to static rule-based methods Shi et al. (2022); Zhou et al. (2024). The DRL agent enabled real-time adaptation to dynamic traffic states, resulting in improved traffic 


Table 3 Adopted parameters of simulation environment.


<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Lane length</td><td>500 m</td></tr><tr><td>Vehicle length</td><td>2.5 m</td></tr><tr><td>Maximum vehicle speed</td><td>30 m/s</td></tr><tr><td>Maximum vehicle acceleration</td><td>3 m/s²</td></tr><tr><td>Maximum vehicle deceleration</td><td>3 m/s²</td></tr><tr><td>Minimum gap between vehicles</td><td>4.5 m</td></tr><tr><td>Traffic volume</td><td>720 vehicles per lane and per hour</td></tr></table>

flow and reduced fuel consumption and emissions through continuous learning. 

Experimental results indicated that a 3-second merging window optimally balanced action space size with operational requirements, while a 5-second signal cycle effectively regulated merging operations. The green phase duration was strategically aligned with mainline gap availability, minimizing traffic disruption. Extension protocols for larger gaps further enhanced merging performance. These findings substantiate the advantages of DRL-based control systems over conventional methods for managing complex merging dynamics in dynamic traffic environments. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/55cc9d555ec0d8fa489eaa11575a30f3439b9225f072bd20a5c8c78de2fa90a2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/d80fd10df2af6ee020e881024e1ef02809a41e08ef1a16a6e7820608fb54a962.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/d73c47a5a15f0c105d78c444211259b7a60435652f24ed27e77d07e7f8a392e6.jpg)



Figure 14: Training history of DRL agent with a compressed traffic state of size 32 and average speed as reward signal.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/b17eeb4b59a67a1067c67b4dbb379fea080fd9f5a08e4309a51d68d5e3773bf0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/948bde9cf52f8bcb38023347c0bf54f0cfce690adfbb14bd51757932bd031c2b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/65ad40aefd11531b234b5b5d65cd38ff408896468ca210687d15e98fa45ab707.jpg)



Figure 15: Convergence of the proposed DRL network.


# 5.5. Analysis of Speed Profile Results

Simulations consider a typical three-legged highway junction, as shown in Fig. 1. Simulation parameters are detailed in Tab. 3. Vehicles are randomly initialized with a $2 0 \%$ probability of emitting a vehicle per second. The slopes of both the mainline and ramp roads are constant at $0 \%$ throughout the simulation. All vehicles have identical parameters listed in Tab. 2. The desired speed for each vehicle, calculated as $v ^ { * } = 1 3 . 4 6 ~ \mathrm { m / s }$ , is the fuel-optimal speed. Maximum and minimum speed limits for both roads are set to $v ^ { \mathrm { m a x } } = 3 0 \mathrm { m / s }$ and $v ^ { \mathrm { m i n } } = 0 \mathrm { m / s }$ , respectively. 

# 6. Validation and Comparative Analysis of the Control Framework

To validate the robustness and applicability of the proposed hierarchical control framework, the DRL network was evaluated through simulations in SUMO Lopez et al. (2018). The assessment focused on traffic efficiency, safety, and fuel consumption under varied conditions. This section details the simulation setup, results, and implications for traffic control systems. 


Table 4 Hyper-parameters of DRL network.


<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Simulated time steps for each episode</td><td>3,600</td></tr><tr><td>Replay memory size</td><td>20,000</td></tr><tr><td>Minibatch size</td><td>64</td></tr><tr><td>Pre-train steps</td><td>2,000</td></tr><tr><td>Target network update interval</td><td>64 control cycles</td></tr><tr><td>Target network update rate</td><td>0.001</td></tr><tr><td>Discount factor</td><td>0.99</td></tr><tr><td>Optimizer</td><td>Adam Kingma and Ba (2014)</td></tr><tr><td>Learning rate</td><td>1 × 10-4</td></tr><tr><td>Initial probability of exploration</td><td>1</td></tr><tr><td>Final probability of exploration</td><td>0.01</td></tr><tr><td>Ending step for exploration probability</td><td>40,000</td></tr></table>

The DRL network was integrated with SUMO using TensorFlow Pang et al. (2020) and Python. Training consisted of structured episodes, each spanning 3,600 time steps (equivalent to one simulated hour). Variations in vehicle generation were introduced via random seeds to ensure diversity and robustness, aligning with established reinforcement learning and traffic simulation practices Huang, Sheng, Ma and Chen (2024). Hyperparameters, including learning 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/16d4e209e88bdda8209a020cdbce2db5d845672ea0311c5b2ce0b09c4b1825c9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/077664c7a15f8174117d7b903d1fbf752010084dd02f270b8468a3dbf5c96f04.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/13edb7687dec63524520e1603d1800a8c4393128447985fb31059e8d640395c8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/502c1beaedb12a7c1b8618a3a87a2398ccbc02286943c0d8708e88d1cefbea4c.jpg)



(a) Traffic flow of 360 and 720 fully CAVs per hour on each leg.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/1ebf11831982627ac33d2cb56dbd03abcea42dcf162b10cff784c55bfd2510d2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/ccaed6253a4c0d9a04f2401bea58b67fbd0bc41def54d88b09e47ef6e352c31c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/3a88b6bfaebe8a17ec9e88007b2bbc630b392cc70f76d23d4c072c52d3998e9a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/fa2f645105684d6b8b89f4f7dd5e4bca30df8e84af8be4365e3e192d723e8129.jpg)



(b) Traffic flow of 360 and 720 vehicles (mixed traffic with $50 \%$ penetration rate of CAVs) per hour on each leg.



Figure 16: Vehicle trajectories in the merging zone under varying traffic conditions: 360 and 720 vehicles per hour with a) fully and b) $50 \%$ CAV penetration in a mixed traffic environment.


rate and discount factor (see Tab. 4), were selected based on domain knowledge and empirical methods, consistent with advanced traffic control frameworks Li, Gong, Peng, Nie, Wang, Chen, Xie, Wang and Zhang (2023); Chen, Zhou, Duan and Yu (2023). 

Performance was evaluated using cumulative rewards, average vehicle speed, and waiting time per episode. As illustrated in Fig. 15, cumulative rewards increased rapidly during initial episodes and stabilized upon policy convergence. Notably, while average vehicle speed improved consistently, a slight increase in waiting time was observed in later training stages. This reflects a known trade-off in traffic optimization, where emphasis on speed maximization can marginally increase waiting times Zhou, Yang, Zhang, Huang, Chen and Yu (2022). This outcome aligns with contemporary traffic signal control studies that prioritize overall efficiency over minimal delay. 

# 6.1. Case Study 1: Merging with CAVs

This case study demonstrates the capability of the proposed DRL-based controller to manage merging scenarios involving CAVs. To evaluate the potential of the model, we considered two traffic conditions: light and saturated traffic. The light traffic scenario simulates a vehicle concession of 6 vehicles per minute, while the saturated traffic scenario doubles the vehicle concession to 12 vehicles per minute. This setup, especially in a single-lane environment without alternatives like lane changes, reflects real-world challenges, particularly under high congestion. 

# 6.1.1. Microscopic Analysis of Performance

The overall performance of the DRL-based controller, in terms of throughput and emergency braking reduction, is evident in the simulation results. Additionally, a more detailed microscopic analysis—focusing on vehicle trajectories and speed changes—reveals the controller’s strong potential in handling both light and saturated traffic conditions. Fig. 16a illustrates simulated vehicle trajectories under two control strategies: the sequential convex programming algorithm Shi et al. (2022); Shi et al. combined with the trained DRLbased controller. The rolling time horizon $( T )$ was set to 10 seconds, with vehicles entering the simulation randomly based on traffic volume settings. 

Light Traffic Conditions (360 vehicles/hour): As shown in Fig. 16a, under light traffic conditions, the merging process is smooth, with minimal disruption to the mainline traffic. The vehicle trajectories remain stable, and velocity changes are gradual, reflecting the controller’s ability to manage merging efficiently and maintain smooth traffic flow with minimal fluctuations. This demonstrates the framework’s ability to optimize traffic flow even in less demanding conditions. 

Saturated Traffic Conditions (720 vehicles/hour): In Fig. 16a, under saturated traffic conditions, the framework still performs effectively, ensuring smooth merging and efficient traffic flow. While velocity fluctuations are more noticeable, the DRL controller maintains optimal merging sequences and adjusts vehicle speeds appropriately to accommodate the increased traffic density. The trajectories demonstrate the controller’s resilience, showing that it can still maintain reasonable stability and minimize disruptions, even under more challenging traffic scenarios. 

# 6.1.2. Extended Microscopic Analysis in Mixed-Traffic Conditions

In this case study, we expand the evaluation of the DRLbased controller to include a mixed-traffic environment, which incorporates both CAVs and HDVs. Although the primary focus of the study has been on a fully CAV environment, the introduction of mixed traffic is a critical extension, reflecting real-world traffic scenarios where a combination of CAVs and HDVs is the norm. This analysis evaluates the controller’s ability to manage such a mixed environment, paying particular attention to the interaction between VTS technology and HDV in varying traffic densities. In addition, the study investigates the potential impact of sensor and communication delays on overall system performance. 

Mixed traffic simulation uses the human-driven vehicle model of SUMO, specifically selecting the default vehicle type equipped with the Krauss car following model Krauß (1998a). The primary objective of this experiment is to assess the interaction dynamics between the DRL-based controller and HDVs, while also exploring how sensor and communication delays could influence system efficiency in mixed-traffic conditions. Performance analysis in this mixed-traffic scenario builds upon findings from the fully CAV environment but introduces more complexity due to the interaction with HDVs. Fig. 16b illustrates the vehicle trajectories and speed profiles in mixed traffic conditions. 

Light Traffic Conditions (360 vehicles/hour): As shown in Fig. 16b, under light mixed traffic conditions, the merging process remains relatively smooth, similar to the complete CAV environment. However, HDVs exhibit less smooth behavior, as evidenced by the more erratic trajectories and the higher frequency of speed fluctuations. This highlights the controller’s ability to interact with HDVs, though the overall flow is slightly less stable compared to the purely CAV scenario. The interaction with HDVs introduces some variability in velocity changes, particularly when human drivers are not following optimal speed profiles. 

Saturated Traffic Conditions (720 vehicles/hour): In Fig. 16b, the DRL-based controller continues to effectively manage traffic flow, even in high-density conditions. However, the integration of HDVs presents additional challenges. The controller adapts well to these challenges, minimizing disruptions and maintaining relatively stable merging sequences. The velocity fluctuations are more noticeable, especially since HDVs may not always follow optimal trajectories or adjust speeds in real-time with the CAVs. Despite this, the controller’s performance remains commendable, demonstrating its robustness in mixed-traffic scenarios. 

Impact of Sensor and Communication Delays: A key aspect of the mixed-traffic simulation is the evaluation of sensor and communication delays. In real-world applications, delays in data transmission and sensor feedback can significantly impact system performance. While our simulation does not directly account for these delays, we observe that the interaction between CAVs and HDVs already introduces some delays in the merging process due to human reaction time and non-optimal driving behaviors. Future 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/c777b9e1dfb3b99b0ad6a8dc6f4f654fb52a8fa1d1ce1a9bd3fc0dfb641d1569.jpg)



Figure 17: Performance comparison with SUMO simulation.


work will focus on incorporating these delays into the simulation and assessing their impact on the DRL controller’s performance. 

# 6.1.3. Discussion on OCP Solver and MPC Performance

The convex optimization solver effectively optimizes speed profiles and mitigates collision risks, maintaining smooth traffic flow even under elevated density conditions. MPC enhances this adaptability through real-time speed adjustments. Their integration ensures robust performance across varying traffic densities while maintaining computational tractability. 

However, performance limitations emerge in near-saturated, single-lane conditions where gap creation becomes challenging. While necessitating mainline speed reductions to facilitate merging—potentially disrupting traffic flow—the system still demonstrates favorable throughput and safety metrics, as evidenced in Figs. 18 and 19. Nevertheless, extreme congestion may induce near-stop-and-go conditions, attenuating system benefits. Future work will refine DRL training protocols and reward structures to enhance performance in high-congestion scenarios. 

# 6.2. Case Study 2: Continuous Simulation

This case study quantitatively evaluates the effectiveness of the proposed method in enhancing traffic efficiency and fuel consumption. Results were compared with SUMO’s default Krauss model Krauß (1998b), which prioritizes fast and safe driving. Due to computational constraints, simulations for CAV merging with optimal control strategies are deferred to future work. 

Fig. 17 presents box plots of simulation results over 3,600 seconds. Key observations include: 

Vehicle Speed: As shown in Fig. 17, DRL-based merging control results in slightly lower vehicle speeds compared to SUMO simulations due to merging regulations. However, this reduction is compensated by improvements in fuel efficiency and safety metrics. 

Fuel Consumption: Fuel consumption improved significantly $( 3 1 . 6 6 \% )$ ) under DRL control compared to SUMO, as resolving conflicts during merging reduced unnecessary accelerations and decelerations. Fuel consumption was calculated using SUMO’s built-in HBEFA-based emission model, which accounts for vehicle dynamics such as speed and 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/64e4fce62f51ad602cabe975ee8d8d2515012e7986d06293e6193b4587782555.jpg)



Figure 18: Cumulative vehicles passing in light traffic conditions (360 vehicles/hour).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/49979a1b15ad961aec83ae26efe1297212ece2610d0a72094841209fffce53a8.jpg)



Figure 19: Cumulative emergency braking events during simulation.


acceleration Biramo and Mekonnen (2022). The fuel consumption data were aggregated over the simulation period and converted to miles per gallon (MPG) for comparison. Average vehicle speed was computed as the total distance traveled divided by the total simulation time. 

To further enrich the analysis in Case Study 2, we acknowledge that merging traffic has the potential to negatively affect mainline traffic flow. In scenarios where vehicles merge into a mainline stream, disruptions such as reduced headway and sudden braking events can occur, leading to unstable traffic flow and an increased likelihood of accidents. 

To assess this impact, we conducted an additional analysis of the mainline traffic parameters under the DRLbased merging control and SUMO simulation. The metrics evaluated include mainline traffic flow (vehicles/hour) and the number of instances of emergency braking. The results indicate that the DRL-based control method effectively mitigates conflicts at merge points by minimizing unnecessary accelerations and decelerations. This, in turn, reduces the ripple effects on mainline traffic. Specifically, we observed: 

Mainline Traffic Efficiency: Under DRL control, the mainline throughput increased by $1 2 . 5 \%$ compared to SUMO simulations as shown in Fig. 18. Throughput improvement was calculated using the following formula: 

$$
\text {Improvement} (\%) = \left(\frac {F _ {\mathrm {DRL}} - F _ {\mathrm {SUMO}}}{F _ {\mathrm {SUMO}}}\right) \times 100,
$$


Table 5 Performance metrics for DRL-based and SUMO control methods.


<table><tr><td>Metric</td><td>Unit</td><td>DRL Control</td><td>SUMO Control</td><td>Improvement (%)</td></tr><tr><td>Average Vehicle Speed</td><td>m/s</td><td>26.80</td><td>28.00</td><td>-4.29</td></tr><tr><td>Fuel Consumption</td><td>MPG</td><td>31.66</td><td>18.34</td><td>31.66</td></tr><tr><td>Traffic Efficiency (Throughput)</td><td>vehicles/hour</td><td>720</td><td>640</td><td>12.50</td></tr><tr><td>Safety (Emergency Braking)</td><td>Events/Simulation</td><td>72</td><td>100</td><td>-28.00</td></tr></table>

where $F _ { \mathrm { D R L } } ~ = ~ 7 2 0$ vehicles/hour and $F _ { \mathrm { S U M O } } ~ = ~ 6 4 0 $ vehicles/hour. 

Traffic Safety Efficiency: Instances of emergency braking on the mainline decreased by $2 8 \%$ in the DRL-based approach compared to SUMO simulations as can be seen from Fig. 19. Reduction in emergency braking was calculated using the following formula: 

$$
\text{Reduction} (\%) = \left(\frac{\text{BrakingEvent s}_{\text{SUMO}} - \text{BrakingEvent s}_{\text{DRL}}}{\text{BrakingEvent s}_{\text{SUMO}}}\right)\times 100,
$$

where BrakingEventsSUMO $= 1 0 0$ and BrakingEventsDRL $=$ 72. 

These findings underline the ability of DRL-based merging control to enhance overall traffic efficiency and safety, not only for merging vehicles but also for mainline traffic. 

Note that negative percentages in Improvement indicate a reduction, which is desirable for metrics such as fuel consumption and emergency braking events. The results demonstrate that the proposed DRL-based framework is effective in handling complex traffic scenarios, particularly in reducing fuel consumption and improving safety metrics. While the framework shows slight limitations in saturated traffic conditions, these can be addressed through more advanced training methodologies. Future work will expand the analysis to include additional traffic scenarios and real-world data to further validate the robustness of the framework. 

# 7. Scalability and Real-World Feasibility Insights

This section addresses the critical challenges in transitioning the proposed hierarchical control framework from simulation to real-world deployment, focusing on computational scalability, decision complexity, and control accuracy under diverse traffic conditions. 

# 7.1. Computational Cost, Decision Complexity, and Control Accuracy

The integration of a DRL agent for decision-making and an OCP solver for trajectory optimization demonstrates promising performance in simulated environments. However, practical implementation necessitates careful consideration of computational efficiency, decision complexity, and control precision. 

# 7.1.1. Computational Cost

The OCP solver utilizes convex optimization techniques to maintain computational efficiency and scalability, which are crucial for real-time traffic management. As demonstrated in our prior work Shi et al. (2023b), convex optimization ensures that large-scale problems can be solved 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/7b2d7412e028ab007a5ccd0f08d628bc559293a60d8e7bcc2ea7d256655df82c.jpg)



Figure 20: Runtime distribution for the devised optimal control scheme.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/3080e383-a20e-4426-8032-e81988884aec/309171d04402094edb23e55016f1d1a06c296c4fb0084bd7d5cf28bf1a3ec8eb.jpg)



Figure 21: Computational time per time step recorded for a randomly selected vehicle when applying the proposed optimal control solver.


effectively. The primary advantage of convex optimization is its ability to deliver fast and reliable solutions even as the problem size increases Shi et al. (2022). 

The time complexity of the OCP is polynomial $( O ( n ^ { 3 } ) )$ , which remains efficient in moderate traffic conditions. As shown in prior experiments, convex optimization significantly reduces computational time compared to nonlinear programming (NLP) solvers. For example, solving Problem 2 in Shi et al. (2023b) using Gurobi took approximately 50 ms per iteration, while an NLP solver such as IPOPT required around 127 s to generate the baseline trajectory in MATLAB on a standard laptop (MacBook Pro, 64-bit OS, Intel Core i7 2.2 GHz). This stark difference in computation times highlights the advantages of convex optimization in practical applications. 

Figs. 20 and 21 from our previous work in Shi et al. (2023b) demonstrate the computational efficiency of the OCP solver. Fig. 20 presents the computational time required to generate 50 trajectories with 20,817 data points, revealing that $7 0 \%$ of the cases achieve convergence within a single iteration. Fig. 21 illustrates the computational time for a randomly selected vehicle, showing that the computational cost remains consistently below 100 ms for the majority of the merging process, further confirming the real-time applicability of our approach. 

In addition, the computational cost of the proposed method can be further reduced by employing higher convergence tolerances or fewer discretization nodes. Implementing the solver in a compiled programming environment or on more powerful hardware could also improve performance. 

Notably, convex optimization solvers guarantee convergence within a finite number of iterations, even without usersupplied initial guesses, as long as the problem is feasible Wang (2024). 

# 7.1.2. Decision Complexity

The decision-making process is simplified through the use of a two-option action space (Yield or Green) for each vehicle, which reduces the complexity of decision-making while maintaining operational effectiveness. This simplification ensures the DRL agent can focus on optimizing the timing of merges without being overwhelmed by excessive state transitions. In future research, further advances in hybrid models combining DRL and rule-based methods will be explored to balance efficiency and scalability, especially in higher-density traffic environments. 

# 7.1.3. Control Accuracy

The OCP solver ensures that vehicles merge in a safe and efficient manner by generating optimal speed profiles. As traffic density increases, maintaining control accuracy becomes increasingly important. The current system effectively handles moderate congestion, but in more densely packed traffic, the ability to create sufficient merging gaps may be limited. Future work will focus on improving the DRL training process to enhance control accuracy in highdensity scenarios, while also integrating adaptive control techniques to ensure the system continues to function smoothly even under more challenging conditions. 

# 7.2. Addressing Scalability and Real-Time Performance

The current framework has demonstrated success in a single merging point scenario, integrating for decisionmaking and OCP solvers for vehicle speed optimization. However, scalability to corridor-level or network-level scenarios (with multiple merging points) introduces new challenges. This section outlines how the proposed approach can be extended to handle more complex scenarios, including mixed traffic and multilane environments, while ensuring real-time operation. 

# 7.2.1. Scaling to Multiple Merging Points:

In a highway network with multiple on-ramps, there are several options for scaling the current framework. The approach can be implemented in one of the following ways: 

1. Distributed DRL Agents for Each Ramp: In this configuration, each on-ramp would be controlled by its own DRL agent and VTS. Each agent would independently make decisions for the ramp it controls, optimizing the merge sequence and vehicle speeds in real time. This distributed setup is similar to multi-agent systems, where each agent operates autonomously but can exchange information with others to ensure smooth traffic flow across the entire network. 

2. Centralized DRL Agent for Multiple Ramps: Alternatively, a centralized system could control multiple merge points using a single DRL agent. In this scenario, the DRL agent would take into account the states of all ramps and 

make decisions based on the overall network condition. The advantage of a centralized system is that it can optimize traffic flow across the entire highway network, avoiding conflicts between merge points. However, this would require more sophisticated coordination and communication among the ramps and might increase the computational load. 

Given the complexity of network-level scenarios, future work will focus on developing hybrid solutions that combine both centralized and distributed approaches, depending on the network’s size and complexity. 

# 7.2.2. Scalability in Mixed and Multilane Traffic:

Scaling the framework to mixed traffic and multilane environments will require modifications to the decisionmaking and control layers. The DRL agent must be able to adapt to diverse vehicle types and manage lane-changing behavior in addition to merging decisions. In multilane conditions, vehicles may choose the optimal lane to merge, requiring the DRL agent to not only manage merge sequences but also optimize lane allocation for vehicles entering the mainline. 

The OCP solver will need to handle multilane interactions and adjust vehicle speed profiles accordingly. This increases the computational complexity, but techniques such as parallel computation and simplified models for less congested lanes can help ensure real-time operation. 

# 7.3. Ensuring Real-Time Operation on Available Hardware

To ensure real-time operation of the proposed framework on available hardware, several strategies will be employed to balance computational demands. While the DRL decision process (neural network forward pass) is fast, the OCP solver, which optimizes vehicle speed profiles, can require more computational time, particularly in complex traffic scenarios. To address this, we will optimize the OCP by using precomputed speed profiles for typical conditions, applying incremental updates to reduce recalculation costs, and leveraging parallel computation to distribute tasks across multiple processors or GPUs for faster processing. Additionally, hardware acceleration through GPUs or FPGAs will be utilized to speed up both DRL and OCP computations. Lastly, asynchronous data processing and buffering mechanisms will be implemented to manage delays in communication or data acquisition, ensuring the system remains responsive even during high-traffic conditions. 

# 8. Future Work

Several research directions emerge to enhance the robustness and applicability of the proposed hierarchical control framework. For example, communication reliability will be addressed through robust protocols, predictive delay compensation, and redundant channels to mitigate vulnerabilities in vehicle-to-everything (V2X) networks Yang, Dong, Zhang, Chen and Wang (2025). The framework will be extended to multi-lane environments with mixed traffic flows, incorporating lane-change dynamics Wu, Jiang, Lu, Rui, 

Ngoduy and Ran (2025) and coordination strategies for HDVs informed by hybrid control research Wang, Zhao, Sun and Liu (2022). Additionally, scalability to large-scale networks with multiple merge points will be explored via Multi-Agent Reinforcement Learning (MARL) architectures Berahman, Karalakou, Rostami-Shahrbabaki and Bogenberger (2025), maintaining the OCP solver for trajectory optimization. Enhanced DRL training protocols and hybrid decision-making strategies He and Lv (2023) will be developed to improve performance in near-saturated traffic conditions Sheikh and Peng (2023). Furthermore, comparative analyses against state-of-the-art ramp metering algorithms Tang, Zhu, Zhang, Iryo-Asano and Nakamura (2022); Yasak, Heerwan and Aparow (2025) will be conducted using both macroscopic and microscopic metrics Feng, Lin, Shi, Wu, Wang, Zhang and Tan (2024). Advanced neural architectures will be investigated to minimize information loss during traffic state encoding. Finally, robust error-handling techniques will be implemented to ensure operational stability when confronting infeasible OCP instances. 

# 9. Conclusion

This study introduced a hierarchical control framework for freeway on-ramp merging of CAVs. The architecture integrates a high-level DRL agent utilizing a VTS to coordinate merging sequences, with a low-level OCP solver that generates collision-free trajectories through pseudospectral optimization. A CAE compresses traffic state data into a computationally efficient latent representation for the DRL agent. Simulation results demonstrate significant performance improvements: a $1 2 . 5 \%$ increase in mainline throughput, a $2 8 \%$ reduction in emergency braking events, and up to $3 1 . 6 6 \%$ enhancement in fuel efficiency compared to conventional models. The VTS-based approach provides a pragmatic transition strategy from existing signal-based infrastructure to future cooperative systems. While evaluated in an idealized environment, future work will focus on validation in mixed-traffic scenarios to ensure robustness for real-world deployment. 

# Acknowledgment

This material is based upon work supported by the US Department of Energy, Office of Energy Efficiency Renewable Energy, Vehicle Technologies Office. 

# Disclosure Statement

The authors are not aware of any affiliations, memberships, funding, or financial holdings that might be perceived as affecting the objectivity of this review. 

# Conflicts of Interest

The authors declare that they have no conflicts of interest. 

# References



Aziz, H.A., Wang, H., Young, S., Sperling, J., Beck, J.M., 2017. Synthesis Study on Transitions in Signal Infrastructure and Control Algorithms for Connected and Automated Transportation. Technical Report. Oak Ridge National Laboratory Report, ORNL/TM-2017/280. 





Berahman, M., Karalakou, A., Rostami-Shahrbabaki, M., Bogenberger, K., 2025. Multi-task lane-free driving strategy for connected and automated vehicles: A multi-agent deep reinforcement learning approach. Engineering Applications of Artificial Intelligence 154, 110797. 





Biramo, Z.B., Mekonnen, A.A., 2022. Modeling the potential impacts of automated vehicles on pollutant emissions under different scenarios of a test track. Environmental Systems Research 11, 28. 





Chen, J., Zhou, Z., Duan, Y., Yu, B., 2023. Research on reinforcementlearning-based truck platooning control strategies in highway on-ramp regions. World Electric Vehicle Journal 14, 273. 





Chen, N., van Arem, B., Alkim, T., Wang, M., 2020a. A hierarchical model-based optimization control approach for cooperative merging by connected automated vehicles. IEEE Transactions on Intelligent Transportation Systems 22, 7712–7725. 





Chen, N., van Arem, B., Alkim, T., Wang, M., 2020b. A hierarchical model-based optimization control approach for cooperative merging by connected automated vehicles. IEEE Transactions on Intelligent Transportation Systems . 





Dehman, A., Farooq, B., 2021. Are work zones and connected automated vehicles ready for a harmonious coexistence? a scoping review and research agenda. Transportation research part C: emerging technologies 133, 103422. 





Deniz, S., Wu, Y., Shi, Y., Wang, Z., 2024. A reinforcement learning approach to vehicle coordination for structured advanced air mobility. Green Energy and Intelligent Transportation 3, 100157. 





Ding, J., Peng, H., Zhang, Y., Li, L., 2020. Penetration effect of connected and automated vehicles on cooperative on-ramp merging. IET Intelligent Transport Systems 14, 56–64. 





Eskandarian, A., Wu, C., Sun, C., 2019. Research advances and challenges of autonomous and connected ground vehicles. IEEE Transactions on Intelligent Transportation Systems 22, 683–711. 





Feng, J., Lin, K., Shi, T., Wu, Y., Wang, Y., Zhang, H., Tan, H., 2024. Cooperative traffic optimization with multi-agent reinforcement learning and evolutionary strategy: Bridging the gap between micro and macro traffic control. Physica A: Statistical Mechanics and its Applications 647, 129734. 





Fernandez, S.A., Marinho, M.A., Vakilzadeh, M., Vinel, A., 2021. Highway on-ramp merging for mixed traffic: Recent advances and future trends, in: 2021 IEEE 29th International Conference on Network Protocols (ICNP), IEEE. pp. 1–6. 





Gao, Y., Ji, Z., Wu, J., Wei, C., Grech, R., 2023. Hierarchical reinforcement learning-based mapless navigation with predictive exploration worthiness, in: 2023 IEEE International Conference on Mechatronics and Automation (ICMA), IEEE. pp. 636–643. 





Genders, W., Razavi, S., 2016. Using a deep reinforcement learning agent for traffic signal control. arXiv preprint arXiv:1611.01142 . 





Guo, Q., Li, L., Ban, X.J., 2019. Urban traffic signal control with connected and automated vehicles: A survey. Transportation research part C: emerging technologies . 





He, X., Lv, C., 2023. Toward personalized decision making for autonomous vehicles: a constrained multi-objective reinforcement learning technique. Transportation research part C: emerging technologies 156, 104352. 





Huang, Z., Sheng, Z., Ma, C., Chen, S., 2024. Human as ai mentor: Enhanced human-in-the-loop reinforcement learning for safe and efficient autonomous driving. Communications in Transportation Research 4, 100127. 





Jing, S., Hui, F., Zhao, X., Rios-Torres, J., Khattak, A.J., 2019a. Cooperative game approach to optimal merging sequence and on-ramp merging control of connected and automated vehicles. IEEE Transactions on Intelligent Transportation Systems 20, 4234–4244. 





Jing, S., Hui, F., Zhao, X., Rios-Torres, J., Khattak, A.J., 2019b. Cooperative game approach to optimal merging sequence and on-ramp merging 





control of connected and automated vehicles. IEEE Transactions on Intelligent Transportation Systems 20, 4234–4244. 





el abidine Kherroubi, Z., Aknine, S., Bacha, R., 2021a. Novel decisionmaking strategy for connected and autonomous vehicles in highway onramp merging. IEEE Transactions on Intelligent Transportation Systems 23, 12490–12502. 





el abidine Kherroubi, Z., Aknine, S., Bacha, R., 2021b. Novel decisionmaking strategy for connected and autonomous vehicles in highway onramp merging. IEEE Transactions on Intelligent Transportation Systems 23, 12490–12502. 





Kherroubi, Z.E.A., 2020a. Novel off-board decision-making strategy for connected and autonomous vehicles (Use case: Highway on-ramp merging). Ph.D. thesis. Université Claude Bernard Lyon 1. 





Kherroubi, Z.E.A., 2020b. Novel off-board decision-making strategy for connected and autonomous vehicles (Use case: Highway on-ramp merging). Ph.D. thesis. Université Claude Bernard Lyon 1. 





Kim, M., Rho, K., Kim, Y.d., Jung, K., 2022. Action-driven contrastive representation for reinforcement learning. Plos one 17, e0265456. 





Kingma, D.P., Ba, J., 2014. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980 . 





Krauß, S., 1998a. Microscopic modeling of traffic flow: Investigation of collision free vehicle dynamics . 





Krauß, S., 1998b. Microscopic modeling of traffic flow: Investigation of collision free vehicle dynamics . 





Li, T., Gong, B., Peng, Y., Nie, J., Wang, Z., Chen, Y., Xie, G., Wang, K., Zhang, H., 2023. Analysis and comparative study of signalized and unsignalized intersection operations and energy-emission characteristics based on real vehicle data. Energies 16, 6235. 





Li, Y., Ma, Y., Chen, Z., 2024. How can connected and automated vehicles improve merging efficiency at freeway on-ramps? Transportmetrica A: transport science 20, 2149286. 





Lin, Y., McPhee, J., Azad, N.L., 2022. Co-optimization of on-ramp merging and plug-in hybrid electric vehicle power split using deep reinforcement learning. IEEE Transactions on Vehicular Technology 71, 6958–6968. 





Liu, J., Zhao, W., Xu, C., 2021. An efficient on-ramp merging strategy for connected and automated vehicles in multi-lane traffic. IEEE Transactions on Intelligent Transportation Systems 23, 5056–5067. 





Lopez, P.A., Behrisch, M., Bieker-Walz, L., Erdmann, J., Flötteröd, Y.P., Hilbrich, R., Lücken, L., Rummel, J., Wagner, P., WieBner, E., 2018. Microscopic traffic simulation using sumo, in: 2018 21st International Conference on Intelligent Transportation Systems (ITSC), IEEE. pp. 2575–2582. 





Ma, J., Wu, F., Chen, Y., Ji, X., Ding, Y., 2023. Effective multimodal reinforcement learning with modality alignment and importance enhancement. arXiv preprint arXiv:2302.09318 . 





Murray, C.A., Shams, L., 2023. Crossmodal interactions in human learning and memory. Frontiers in Human Neuroscience 17, 1181760. 





Muzahid, A.J.M., Kamarulzaman, S.F., Rahman, M.A., Alenezi, A.H., 2022. Deep reinforcement learning-based driving strategy for avoidance of chain collisions and its safety efficiency analysis in autonomous vehicles. IEEE Access 10, 43303–43319. 





Muzahid, A.J.M., Rahim, M.A., Murad, S.A., Kamarulzaman, S.F., Rahman, M.A., 2021. Optimal safety planning and driving decision-making for multiple autonomous vehicles: A learning based approach, in: 2021 Emerging Technology in Computing, Communication and Electronics (ETCCE), IEEE. pp. 1–6. 





Muzahid, A.J.M., Zhao, X., Wang, Z., 2024. Survey on human-vehicle interactions and ai collaboration for optimal decision-making in automated driving. arXiv preprint arXiv:2412.08005 . 





Pang, B., Nijkamp, E., Wu, Y.N., 2020. Deep learning with tensorflow: A review. Journal of Educational and Behavioral Statistics 45, 227–248. 





Rahman, M.M., Thill, J.C., 2023. Impacts of connected and autonomous vehicles on urban transportation and environment: A comprehensive review. Sustainable Cities and Society , 104649. 





Rios-Torres, J., Malikopoulos, A.A., 2016. A survey on the coordination of connected and automated vehicles at intersections and merging at highway on-ramps. IEEE Transactions on Intelligent Transportation Systems 18, 1066–1077. 





Ruan, X., Li, P., Zhu, X., Liu, P., 2022. A target-driven visual navigation method based on intrinsic motivation exploration and space topological cognition. Scientific Reports 12, 3462. 





Schaul, T., Quan, J., Antonoglou, I., Silver, D., 2015. Prioritized experience replay. arXiv preprint arXiv:1511.05952 . 





Scholte, W., Zegelaar, P.W., Nijmeijer, H., 2022. A control strategy for merging a single vehicle into a platoon at highway on-ramps. Transportation research part C: emerging technologies 136, 103511. 





Sheikh, M.S., Peng, Y., 2023. A collision avoidance model for on-ramp merging of autonomous vehicles. KSCE Journal of Civil Engineering 27, 1323–1339. 





Shi, Y., Wang, Z., LaClair, T.J., Wang, C., Shao, Y., . Real-time control of connected vehicles in signalized corridors using pseudospectral convex optimization. Optimal Control Applications and Methods . 





Shi, Y., Wang, Z., LaClair, T.J., Wang, C., Shao, Y., Yuan, J., 2023a. A novel deep reinforcement learning approach to traffic signal control with connected vehicles. Applied Sciences 13, 2750. 





Shi, Y., Wang, Z., LaClair, T.J., Wang, C.R., Yuan, J., 2022. Realtime on-ramp merging control of connected and automated vehicles using pseudospectral convex optimization, in: 2022 American Control Conference (ACC), IEEE. pp. 2000–2005. 





Shi, Y., Wang, Z., Wang, C.R., Shao, Y., 2023b. Pseudospectral convex optimization for on-ramp merging control of connected vehicles. Journal of the Franklin Institute 360, 10972–10999. 





Simonyan, K., Zisserman, A., 2014. Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556 . 





Stolle, M., Precup, D., 2002. Learning options in reinforcement learning, in: Abstraction, Reformulation, and Approximation: 5th International Symposium, SARA 2002 Kananaskis, Alberta, Canada August 2–4, 2002 Proceedings 5, Springer. pp. 212–223. 





Tang, Z., Zhu, H., Zhang, X., Iryo-Asano, M., Nakamura, H., 2022. A novel hierarchical cooperative merging control model of connected and automated vehicles featuring flexible merging positions in system optimization. Transportation research part C: emerging technologies 138, 103650. 





Triest, S., Villaflor, A., Dolan, J.M., 2020. Learning highway ramp merging via reinforcement learning with temporally-extended actions, in: 2020 IEEE Intelligent Vehicles Symposium (IV), IEEE. pp. 1595–1600. 





Van Hasselt, H., Guez, A., Silver, D., 2016. Deep reinforcement learning with double q-learning, in: Thirtieth AAAI conference on artificial intelligence. 





Wang, G., Xing, H., Chen, Y., Liu, Y., 2024. A dynamic exploratory hybrid modelling framework for simulating complex and uncertain system. Journal of Safety Science and Resilience 5, 167–178. 





Wang, S.H., Zhao, M., Sun, D.H., Liu, X., 2022. A merging strategy based on optimal control of main-lane downstream and on-ramp vehicles. KSCE Journal of Civil Engineering 26, 4777–4792. 





Wang, Z., 2024. A survey on convex optimization for guidance and control of vehicular systems. Annual Reviews in Control 57, 100957. 





Wang, Z., Cook, A., Shao, Y., Xu, G., Chen, J.M., 2023a. Cooperative merging speed planning: A vehicle-dynamics-free method, in: 2023 IEEE Intelligent Vehicles Symposium (IV), IEEE. pp. 1–8. 





Wang, Z., Schaul, T., Hessel, M., Hasselt, H., Lanctot, M., Freitas, N., 2016. Dueling network architectures for deep reinforcement learning, in: International conference on machine learning, PMLR. pp. 1995–2003. 





Wang, Z., Schaul, T., Hessel, M., Van Hasselt, H., Lanctot, M., De Freitas, N., 2015. Dueling network architectures for deep reinforcement learning. arXiv preprint arXiv:1511.06581 . 





Wang, Z., Zhou, A., Cook, A., Shao, Y., Xu, G., Chen, M., 2023b. Energycentric cooperative onramp merging strategy: An analytical solution, in: 2023 IEEE International Automated Vehicle Validation Conference (IAVVC), IEEE. pp. 1–7. 





Wilmot, C., Baldassarre, G., Triesch, J., 2021. Learning abstract representations through lossy compression of multimodal signals. IEEE Transactions on Cognitive and Developmental Systems 15, 348–360. 





Wu, R., Jiang, J., Lu, W., Rui, Y., Ngoduy, D., Ran, B., 2025. A duallayer path planning approach for ramp merging with integrated risk management. Expert Systems with Applications 276, 127167. 





Xu, L., Lu, J., Ran, B., Yang, F., Zhang, J., 2019. Cooperative merging strategy for connected vehicles at highway on-ramps. Journal of Transportation Engineering, Part A: Systems 145, 04019022. 





Yamada, J., Pertsch, K., Gunjal, A., Lim, J.J., 2022. Task-induced representation learning. arXiv preprint arXiv:2204.11827 . 





Yang, W., Dong, C., Zhang, Z., Chen, X., Wang, H., 2025. A dualmodule cooperative control method for on-ramp area in heterogeneous traffic flow using reinforcement learning. Engineering Applications of Artificial Intelligence 150, 110584. 





Yasak, M., Heerwan, P., Aparow, V., 2025. Collision avoidance strategies in autonomous vehicles and on-ramp scenario: A review. Annual Reviews in Control 59, 100986. 





Zhang, T., Fan, J., Zhou, N., Gao, Z., 2024. Highly self-adaptive pathplanning method for unmanned ground vehicle based on transformer encoder feature extraction and incremental reinforcement learning. Machines 12, 289. 





Zhang, Z., Liu, F., Wolshon, B., Sheng, Y., 2020. Virtual traffic signals: Safe, rapid, efficient and autonomous driving without traffic control. IEEE Transactions on Intelligent Transportation Systems 22, 6954– 6966. 





Zhou, A., Peeta, S., Zhou, H., Laval, J., Wang, Z., Cook, A., 2024. Implications of stop-and-go traffic on training learning-based car-following control. Transportation Research Part C: Emerging Technologies , 104578. 





Zhou, A., Wang, Z., Cook, A., 2023. Model predictive control-based trajectory shaper for safe and efficient adaptive cruise control, in: 2023 IEEE International Automated Vehicle Validation Conference (IAVVC), IEEE. pp. 1–7. 





Zhou, Z., Yang, Z., Zhang, Y., Huang, Y., Chen, H., Yu, Z., 2022. A comprehensive study of speed prediction in transportation system: From vehicle to traffic. Iscience 25. 





Zhu, J., Easa, S., Gao, K., 2022. Merging control strategies of connected and autonomous vehicles at freeway on-ramps: A comprehensive review. Journal of intelligent and connected vehicles 5, 99–111. 





Zhu, J., Tasic, I., 2021. Safety analysis of freeway on-ramp merging with the presence of autonomous vehicles. Accident Analysis & Prevention 152, 105966. 

