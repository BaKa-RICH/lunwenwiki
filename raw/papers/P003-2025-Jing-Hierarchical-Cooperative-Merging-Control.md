# A hierarchical cooperative merging control strategy for the mixed traffic of CAVs and HDVs


Dian Jing a, Rongsheng Chen a ,∗, Enjian Yao a ,∗, Monica Menendez b 

a Key Laboratory of Transport Industry of Big Data Application Technologies for Comprehensive Transport, Beijing Jiaotong University, Beijing, 100044, China 

b Division of Engineering, New York University Abu Dhabi, Abu Dhabi, 129138, United Arab Emirates 

# A R T I C L E I N F O

Keywords: 

Connected and automated vehicles 

Mixed traffic 

Freeway merging zones 

Merging sequencing 

Consensus controller 

Platoon stability 

# A B S T R A C T

The interactions between vehicles in freeway merging zones can lead to traffic congestion and potential collision risks, resulting in economic loss and environmental pollution. With the development of connected and automated vehicle (CAV) technologies, it is expected to address these issues through trajectory-level vehicular control. However, due to the large number of human-driven vehicles (HDVs) currently in operation, achieving a pure CAV environment will take time. This motivates us to explore the merging control strategies that can deal with a mixed traffic environment involving both CAVs and HDVs. To accomplish this goal, this study proposes a hierarchical cooperative control strategy consisting of a merging sequencing layer and a motion planning layer to facilitate the smooth merging of CAVs in freeway merging zones. First, the globally optimal merging sequence is determined considering traffic efficiency, safety, and driving comfort using the real-time information collected by roadside units. A zero–one integer programming model is built to convert merging sequencing into a shortest-path search problem, enhancing the solving efficiency. Next, a consensus controller with communication delays is proposed considering the state error of all vehicles in the platoon to deal with the future mixed-traffic environment. The local and string stability conditions are derived to establish parameter-setting criteria. Finally, several experiments are conducted to evaluate the performance of the proposed consensus controller and to analyze the impact of CAVs equipped with the proposed controller on traffic flow. The results show that (1) a more reasonable merging sequence can be provided by the proposed algorithm to reduce potential conflicts and help CAVs merge efficiently, and (2) increasing the penetration rates of CAVs can improve the anti-disturbance performance, robustness, and stability of traffic flow in the merging zone. The related algorithms and findings can be adopted in future autonomous driving systems. 

# 1. Introduction

In 2019, traffic congestion in the United States resulted in economic losses exceeding $\$ 88$ billion (Guzman et al., 2023). Congestion reduces traffic efficiency, increases the risk of collisions, and leads to excessive fuel consumption and environmental pollution (de Souza et al., 2017; Jing et al., 2019). A key area of concern is freeway merging zones, which frequently become traffic bottlenecks due to the complex interactions between on-ramp and mainline vehicles (Min et al., 2020; Xiao et al., 2018). On-ramp vehicles must find suitable gaps in the mainline traffic stream while maintaining a safe distance by adjusting their speed. 

Meanwhile, mainline vehicles must decide whether to yield, often adjusting their speed as well. Due to the lack of communication between vehicles in merging zones, they may compete for the right of way, resulting in three main problems: (1) the chosen gap may be too small, increasing the risk of collisions; (2) mainline vehicles may be forced to decelerate abruptly, causing traffic oscillations and jams; and (3) on-ramp vehicles might not be able to merge smoothly, creating a queue on the on-ramps that could spill over to surface streets (Jing et al., 2019). Traditional macroscopic control methods, such as (1) ramp metering, which limits the flow from on-ramps (Cassidy and Rudjanakanoknad, 2005; Ferrara et al., 2015; Papageorgiou et al., 1990), and (2) variable speed limits, which dynamically adjust mainline speed to manage traffic flow and reduce these conflicts (Chen et al., 2020b). However, the effectiveness of macroscopic control is limited as they cannot directly control individual vehicles (Wang et al., 2022). 

With the development of connected and automated vehicle (CAV) technologies, it is promising to achieve smooth merging through microscopic trajectory control (Guler et al., 2014; Jing et al., 2023; Yang et al., 2016b; Jing et al., 2024; Yang et al., 2016a; Jing et al., 2025a). CAVs combine the advantages of connected vehicles (CVs) and automated vehicles (AVs), allowing them to gather real-time information via vehicle-to-everything (V2X) communication and execute precise control through automation technologies. As a result, CAVs enable effective trajectory-level cooperative merging control. However, a pure CAV environment remains challenging due to the slow increase in CAV penetration rates and the large ownership of human-driven vehicles (HDVs). CAVs and HDVs are expected to coexist in traffic for an extended period (Gong and Du, 2018). Unlike CAVs, HDVs are usually uncontrollable for central managers and exhibit high levels of randomness and uncertainty. Therefore, it is intractable to develop a merging control strategy that considers the interactions between CAVs and HDVs in the future long-term mixed traffic environment. 

In recent years, numerous cooperative merging strategies have been proposed to address the aforementioned challenges. However, several gaps remain, which can be summarized as follows: (1) Most studies that adopt hierarchical control frameworks typically decompose the problem into a sequencing layer and a planning layer. However, they either focus on fully autonomous CAV environments or fail to adequately consider the uncertainties of HDV behavior (Chen et al., 2024; Sun et al., 2020), making them less suitable for mixed-traffic scenarios. (2) Most of the existing studies determine the merging sequence based on preset rules or logic, which neither guarantees optimal merging nor accurately captures inter-vehicle interactions. Some studies attempt to optimize merging sequences and motion planning jointly (Xie et al., 2024). However, due to the inherent nonlinearity of these problems, the computational burden is often high, limiting real-time applications. (3) Many existing controllers assume that all the following vehicles in the platoon can adjust their speed to match that of platoon leader, which can achieve a consensus state effectively and more suitable in the pure CAV environment (Di Bernardo et al., 2015; Salvi et al., 2017; Zhao et al., 2022a). However, in the mixed-traffic environment, these controllers do not always guarantee the stability of the platoon due to the uncertainty of HDVs, resulting in potential safety concerns. 

Motivated by these research gaps, this study proposes a hierarchical cooperative merging control strategy that accounts for HDV uncertainty in mixed-flow platoons. The proposed strategy ensures high computational efficiency and robustness, enabling real-time implementation in mixed-traffic environments. The contributions of this study are threefold: 

• The proposed controller systematically models the stochasticity of human car-following behavior, which can help CAVs better interact with HDVs in mixed-traffic environments, ultimately improving regional traffic efficiency. Additionally, the hierarchical structure enhances the flexibility and computational efficiency of the proposed approach. 

• A merging sequencing model is developed and solved in an optimization framework. Compared with traditional rule-based approaches, the proposed model enables CAVs to make more reasonable and adaptive merging decisions. The optimal merging sequence can be determined solely based on real-time kinematic states, which is convenient to modify or integrate with other control algorithms. Moreover, the optimization-based model has lower computational complexity than existing freeway merging approaches, making it more suitable for real-time applications. 

• A consensus controller with communication delays is designed considering the state errors between the platoon leader and all its following vehicles. The proposed controller enhances the robustness and applicability in mixed-traffic platoons. Additionally, local and string stability conditions are analyzed to establish criteria for selecting appropriate gain factors, providing valuable guidance for engineering applications. 

The remainder of this paper is organized as follows: Section 2 reviews the control approaches for CAVs presented in existing studies. Section 3 details the methodology of the proposed CAV merging control algorithm. Section 4 presents the experiments conducted to evaluate the algorithm’s performance and discusses the results. Section 5 concludes with a summary of the findings and suggestions for future studies. 

# 2. Literature review

Cooperative merging control strategies can be divided into two categories: (1) centralized control and (2) decentralized control. In centralized control, a central manager determines the motion planning of all CAVs in the control zone simultaneously based on real-time state information (Chen et al., 2020a; Tilg et al., 2018), and the controlled vehicles fully comply the instructions sent by the central manager. Centralized control can be solved by an optimization-based approach, which aims to minimize a specific objective function while satisfying a set of real-world constraints (Hu and Sun, 2019). The objectives often focus on factors such as traffic efficiency, driving comfort, fuel consumption, and others (Cao et al., 2015; Hu and Sun, 2019; Li et al., 2022; Mu et al., 2021; Tajalli et al., 2022; Zhou et al., 2018). For instance, Min et al. (2020) proposed a centralized merging control algorithm that constructs the globally optimal merging sequence using game-theoretic methods. Sun et al. (2020) explored cooperative decision-making in mixed 

traffic, employing bi-level dynamic programming to address the problem. Jing et al. (2019) developed a cooperative multi-agent, game-based optimization model focused on minimizing global payoffs to control CAVs in merging zones. 

Although centralized control approaches provide globally optimal solutions, they can face significant computational challenges as the number of CAVs increases, particularly in heavy traffic conditions (Liu et al., 2023). Additionally, if the centralized controller suffers a cyber-attack, regional traffic might become uncontrollable. To address these limitations, decentralized control approaches have gained attention due to their flexibility, scalability, and fault tolerance, making them more resilient than centralized systems (Xu et al., 2019; Jing et al., 2024). In decentralized control models, each vehicle operates using independent control logic to handle decision-making and motion planning. For example, Xu and Shen (2022) proposed a decentralized optimization model based on Pontryagin’s Maximum Principle (PMP) to minimize energy consumption and travel time. Xie et al. (2024) introduced a hierarchical optimization model comprising a merging sequencing layer and a trajectory optimization layer to provide individualized merging strategies for each CAV. Chen et al. (2024) developed a solution for cooperative merging by optimizing both trajectories and merging sequences through mixed-integer nonlinear programming (MINLP), focusing on efficiency and safety. Ntousakis et al. (2016) presented an optimal control model aimed at minimizing engine effort and passenger discomfort. Liu et al. (2023) designed a two-level hierarchical control algorithm to manage cooperative merging. 

Virtual-platoon strategy is a type of decentralized approach designed for cooperative merging control (Zhou et al., 2022), which was first proposed by Uno et al. (1999). Its core idea is to transform the merging control problem into a car-following (CF) problem by virtually mapping on-ramp vehicles onto the mainline road to form a virtual platoon (Lu et al., 2004; Uno et al., 1999). In the virtual platoon, vehicles can adjust their longitudinal speed using CF controllers to maintain the desired spacing and achieve smooth merging (Chen et al., 2021; Li et al., 2022; Mu et al., 2021; Scholte et al., 2022; Wang et al., 2013; Xue et al., 2023). With advances in wireless communication, CF controllers in a platoon can leverage more information from surrounding vehicles to assist merging decision-making and planning (Milanes et al., 2014). Existing studies on virtual-platoon control primarily focused on three aspects: (1) enhancing cooperation to resist external disturbances using consensus-based CF controllers (Ahmed et al., 2020; Di Bernardo et al., 2015; Li et al., 2013; Olfati-Saber and Murray, 2004; Salvi et al., 2017; Su et al., 2024); (2) mitigating the negative impact of time delays in wireless communications (Abbasi and Marquez, 2024; Fang et al., 2022; Wang et al., 2020; Zhao et al., 2022b); and (3) reducing computational costs and control frequency by implementing event-triggered mechanisms (Abbasi and Marquez, 2024; Yang and Liu, 2014; Ferrara et al., 2015; Selivanov and Fridman, 2016; Silva et al., 2024). For example, Hu et al. (2021) introduced a two-layer merging control framework combining centralized sequencing with distributed control. The controller addresses nonlinear vehicle dynamics and time-varying uncertainties based on the Udwadia–Kalaba approach and Lyapunov stability theory. Meng et al. (2024) proposed a spatial-dependent robust control strategy for CAV merging. Fang et al. (2022) developed an on-ramp cooperative merging control strategy accounting for communication delays by using a statistic-based delay estimation model. Additionally, Silva et al. (2024) studied cooperative adaptive cruise control (CACC) systems employing a predecessor–follower topology under eventtriggered communication and uncertainties. They derived sufficient conditions for designing a switched dynamic event-trigger controller to ensure local and string stability. 

In recent years, another decentralized control algorithm, reinforcement learning (RL), has been widely applied in cooperative merging control strategies (Liu et al., 2024). In RL algorithms, agents learn merging control policies by continuously interacting with the environment and receiving feedback (Li et al., 2024; Lu et al., 2023). However, RL models typically require a large amount of data for training, making the process time-consuming and computationally expensive. Additionally, they can be unstable in some edge scenarios and lack interpretability. 

In summary, existing studies on cooperative merging control face several challenges and require further investigation. Specifically, existing studies often omit competitive-cooperative behavior and inadequately evaluate optional merging sequences, which limits their applicability to real-world merging interactions. Moreover, most existing studies focus on pure CAV environments, assuming that all the following vehicles can adjust their speeds to reach a consensus with the platoon leader. However, this assumption is hard to achieve in mixed-traffic platoons, where HDVs cannot be directly controlled. As a result, existing control strategies lack the robustness needed for future mixed-traffic scenarios. This study is therefore motivated by the need to address these issues. 

# 3. Methodology

# 3.1. Problem description

The CAVs in this study are assumed to be high-level (L4 or L5 defined by Society of Automotive Engineers) autonomous vehicles equipped with communication devices. CAVs can receive the information about surrounding vehicles collected via roadside units (RSUs) and vehicle-to-infrastructure (V2I) technologies. In contrast, HDVs can only observe information from the first preceding vehicle due to their limited perception abilities. The road scenario in this study consists of a multi-lane mainline and a ramp, as illustrated in Fig. 1. A merging point is predetermined by the configuration of the merge. By that point, all on-ramp vehicles are required to have entered the mainline. Moreover, vehicles in the merging zone are not allowed to make continuous lane-changing or overtaking maneuvers. In particular, vehicles in the inner lane are not allowed to change lanes to the outer lane. In contrast, when the flow in the inner lane is lower than that in the outer lane and the safety conditions are met, vehicles in the outer lane can change lanes to the inner lane. As shown in Fig. 5(b), road management can add a lane marking that allows lane changes from the outer lane to the inner lane, while prohibiting changes in the opposite direction. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/67d8c75875cd3a191c6fe4dc3b576bc0c809495dcc83249aed2f42c3a7ba2268.jpg)



Fig. 1. Problem setting and the proposed hierarchical merging framework.


Due to the nonlinearity between merging sequencing and motion planning, we decompose the integrated optimization into a hierarchical optimization framework, which includes a merging sequencing layer and a motion planning layer. This approach reduces computational costs (Chen et al., 2024). Specifically, centralized managers can determine the globally optimal merging sequence based on predicted motions in all leader–follower relationships calculated by the motion planning module and then communicate this sequence to the CAVs. Each CAV, based on the merging sequence, can identify its first preceding vehicle and plan the motion to achieve smooth and efficient merging control. 

This section will elaborate on the hierarchical optimization framework. 

# 3.2. Merging sequencing

As illustrated in Fig. 2, the merging sequencing layer aims to find the lowest-cost path that visits all vehicles, starting with vehicle 0, while satisfying specific constraints. To accomplish this, we first create a directed graph to describe the topological relationships between all vehicles (represented by nodes). The edge connecting two nodes represents the leader–follower relationship between two vehicles. For example, Node 1 points to Node 2, indicating that Node 1 is the leader and Node 2 is the follower. We design a function to calculate the cost of each edge based on predicted motion states. Finally, the lowest-cost path can be solved by an optimization-based approach. 

# 3.2.1. Physical network

First, we construct a directed graph to describe the physical network for all vehicles in the merging zone. Consider $N + 1$ vehicles traveling in a merging zone, including the platoon leader numbered 0 and $N$ following vehicles numbered ?? where $i \in \mathcal { N }$ and $\mathcal { N } = \{ 0 , 1 , 2 , \dotsc , i , \dotsc , j , \dotsc , N \}$ is the set of all vehicles in the platoon. Let $r \in \mathcal { R } , \mathcal { R } = \{ 1 , 2 , \dotsc , R \}$ be the index of lanes and vehicle ?? belonging to lane $r$ can be represented as $i \in \mathcal { N } _ { r }$ . Therefore, the set of all vehicles $\mathcal { N }$ can also be represented as $\mathcal { N } = \mathcal { N } _ { 1 } \cup \ldots \mathcal { N } _ { r } \cup \ldots \mathcal { N } _ { R }$ . Let $( i , j )$ be the edge from ?? to its follower $j$ in the two-vehicle leader–follower relationship. 

# 3.2.2. Cost function

A function $c _ { i j }$ is designed to calculate the cost of each edge $( i , j )$ , consisting of two components: self-dependent and pairwise terms. The self-dependent term $c _ { i , s \mathrm { e l f } } \left( t \right)$ at time ?? consists of traffic efficiency ????,efficiency (??) and driving comfort $c _ { i , \mathrm { c o m f o r t } } \left( t \right)$ , and the pairwise term $c _ { i j , \mathrm { p a i r w i s e } } \left( t \right)$ $c _ { i j }$ at time $t$ is traffic safety $c _ { i j , s a f e } \left( t \right)$ , as Eqs. (1)–(4). 

$$
c _ {i j} (t) = \beta_ {1} c _ {i, \text {e f f i c i e n c y}} (t) + \beta_ {2} c _ {i, \text {c o m f o r t}} (t) + \beta_ {3} c _ {i j, \text {s a f e}} (t) \tag {1}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/1e2f0fe5ac991c7c2642f0ca787aac2e819d0b769025a512da58b10247307759.jpg)



Fig. 2. Illustration of the directed graph, feasible sequences, and infeasible sequences of a platoon.


$$
c _ {i, \text {e f f i c i e n c y}} (t) = \sum_ {t ^ {\prime} = t} ^ {t + t _ {0}} \left(v _ {i} \left(t ^ {\prime}\right) - v _ {\exp}\right) ^ {2} \tag {2}
$$

$$
c _ {i, \text {c o m f o r t}} (t) = \sum_ {t ^ {\prime} = t} ^ {t + t _ {0}} a _ {i} ^ {2} \left(t ^ {\prime}\right) \tag {3}
$$

$$
c _ {i j, \text {s a f e}} (t) = \sum_ {l = t ^ {\prime}} ^ {t + t _ {0}} \sum_ {j <   i, j \in \mathcal {N}} \max  \left(d _ {i j, \text {s a f e}} - \left| p _ {i} \left(t ^ {\prime}\right) - p _ {j} \left(t ^ {\prime}\right) \right|, 0\right) \tag {4}
$$

where $t \in \tau$ and $\mathcal { T } = \{ 1 , 2 , \dots , T \}$ . $t _ { 0 }$ is the prediction time horizon. $c _ { i j }$ is an accumulated cost from time ?? to $t + t _ { 0 } . \mathrm { ~ } p _ { i } , \mathrm { ~ } v _ { i }$ , and $a _ { i }$ represent the longitudinal position, speed, and acceleration of vehicle ??, respectively. The parameters $\beta _ { 1 }$ to $\beta _ { 3 }$ are weighting factors that reflect human driving styles, $\beta _ { 1 } \sim \beta _ { 3 }$ are three positive numbers and the sum of the three weighting factors equals to 1. For example, $\beta _ { 1 }$ for aggressive drivers might be higher than that for cautious drivers since they prioritize higher traffic efficiency (Jing et al., 2025b). In contrast, $\beta _ { 2 }$ and $\beta _ { 3 }$ for cautious drivers might be higher than those for aggressive drivers due to their concern for safety and comfort. The term $c _ { i , \mathrm { e f f i c i e n c y } } ( t )$ represents the traffic efficiency cost, which decreases if the longitudinal speed is closer to the expected speed $v _ { \mathrm { e x p } }$ . The term $c _ { i , \mathrm { c o m f o r t } } ( t )$ represents the driving comfort cost, which decreases if the longitudinal acceleration is smaller. The safety distance $d _ { \mathrm { s a f e } }$ is defined as $d _ { i j , \mathrm { s a f e } } = \tau _ { i } ^ { * } \cdot v _ { i } ( t ) + l _ { j }$ , where $\boldsymbol { \tau } _ { i } ^ { * }$ is the desired headway and $l _ { j }$ is the length of vehicle $j$ . The safety cost $c _ { i j , s a f e } ( t )$ is zero if the longitudinal spacing is larger than the safety distance; otherwise, $c _ { i j , \mathrm { s a f e } } ( t ) = d _ { i j , \mathrm { s a f e } } - \Big | p _ { i } ( t ) - p _ { j } ( t ) \Big | .$ . 

The motion states (i.e., position $p _ { i } ( t )$ , speed $v _ { i } ( t )$ , and acceleration $a _ { i } ( t ) )$ of vehicles can be predicted with a given edge $( i , j )$ to estimate $c _ { i j } \left( t \right)$ . For CAVs, the trajectories can be calculated using the proposed controller in Section 3.3. For HDVs, we introduce the 2D-Intelligent Driver Model (2D-IDM) proposed by Xiong and Jiang (2022), which is represented by Eqs. (5)–(9). 2D-IDM can model the uncertainty of HDVs’ motion by randomly adjusting the desired time gap, in contrast to the classical IDM. The longitudinal acceleration of HDV ?? can be calculated as follows. 

$$
a _ {i} (t) = a \left(1 - \left(\frac {v _ {i} (t)}{v _ {\operatorname* {m a x}}}\right) ^ {4} - \left(\frac {d _ {i , \text {d e s i r e d}} (t)}{d _ {i} (t)}\right) ^ {2}\right) \tag {5}
$$

$$
d _ {i, \text {d e s i r e d}} (t) = s _ {0} + \max  \left(v _ {i} (t) T _ {i} (t) + \frac {v _ {i} (t) \left(v _ {i} (t) - v _ {i - 1} (t)\right)}{2 \sqrt {a b}}, 0\right) \tag {6}
$$

$$
d _ {i} (t) = p _ {i - 1} (t) - p _ {i} (t) - l _ {i - 1} \tag {7}
$$

$$
T _ {i, \text {t a r g e t}} (t) = \left\{ \begin{array}{l} T _ {1} + r \left(T _ {2} - T _ {1}\right), \text {i f} r _ {1} <   r _ {0} \\ T _ {i, \text {t a r g e t}} (t - \Delta t), \text {o t h e r w i s e} \end{array} \right. \tag {8}
$$

$$
T _ {i} (t) = \left\{ \begin{array}{l} T _ {i} (t - \Delta t), \text {i f} T _ {i} (t - \Delta t) = T _ {i, \text {t a r g e t}} (t) \\ \max  \left(T _ {i} (t - \Delta t) - \Delta T, T _ {i, \text {t a r g e t}} (t)\right), \text {i f} T _ {i} (t - \Delta t) > T _ {i, \text {t a r g e t}} (t) \\ \min  \left(T _ {i} (t - \Delta t) + \Delta T, T _ {i, \text {t a r g e t}} (t)\right), \text {i f} T _ {i} (t - \Delta t) <   T _ {i, \text {t a r g e t}} (t) \end{array} \right. \tag {9}
$$

where ?? is the maximum acceleration, $b$ is the safety deceleration. $d _ { i , \mathrm { d e s i r e d } } \left( t \right)$ is the desired spacing gap of vehicle ??, $s _ { 0 }$ is the minimum spacing gap. $T _ { i } \left( t \right)$ is the desired time gap, $T _ { i , \mathrm { t a r g e t } }$ is the target time gap. $r$ and $r _ { 1 }$ are two random numbers between 0 and 1. ???? is the maximum changing rate of the desired time gap, $T _ { 1 }$ and $T _ { 2 }$ are the minimum and maximum time gap, respectively. $r _ { 0 }$ is a random probability. The equations can describe the stochasticity of the motion of HDVs, i.e., the target time gap $T _ { i , \mathrm { t a r g e t } } ( t )$ can change stochastically in the range from $T _ { 1 }$ to $T _ { 2 }$ . 

Using the 2D-IDM model, a set of possible trajectory points can be generated through repeated simulations. Then we select the $\alpha$ -percentile trajectory, which satisfies $F ( p _ { i } ( t ) \leq p _ { i , \alpha } ( t ) ) = 1 - \alpha$ (Xiong et al., 2022). In this study, we perform 50 simulation runs and set $\alpha = 0 . 5$ . 

# 3.2.3. Mathematical model

A mathematical model is proposed to optimize the merging sequence, which can be represented as Eqs. (10)–(11): 

$$
\min  C (t) = \sum c _ {i j} (t) \cdot \xi_ {i j} (t), \forall t \in \mathcal {T} \tag {10}
$$

$$
\xi_ {i j} (t) = \left\{ \begin{array}{l} 1, \text {i f c h o o s e e d g e} (i, j) \\ 0, \text {o t h e r w i s e} \end{array} \right. \tag {11}
$$

where $C$ is the objective function representing the total cost of the merging sequence. $\xi _ { i j }$ is decision variable, which denotes whether edge $( i , j )$ is selected or not. 

subject to: 

$$
\sum_ {i \in \mathcal {N} _ {r}, j \in \mathcal {N} _ {s}} \xi_ {(i, j)} = 0, \forall r = s, i \geq j \tag {12}
$$

$$
\sum_ {i \in \mathcal {N} _ {r}, j \in \mathcal {N} _ {s}} \xi_ {(i, j)} = 0, \forall r = s, i <   j - 1 \tag {13}
$$

$$
\sum_ {i \in \mathcal {N} _ {r}, j \in \mathcal {N} _ {s}} \xi_ {(i, j)} = \sum_ {r \in \mathcal {R}} N _ {r} - 1 \tag {14}
$$

$$
\sum_ {j \in \mathcal {N} _ {s}, s \in \mathcal {R}} \xi_ {(i, j)} = 1, \forall j \in \mathcal {N} _ {r} \backslash \{0 \}, r \in \mathcal {R} \tag {15}
$$

$$
\sum_ {i \in \mathcal {N} _ {r}, r \in \mathcal {R}} \xi_ {(i, j)} = 1, \forall j \in \mathcal {N} _ {s} \backslash \left\{N _ {s} \right\}, s \in \mathcal {R} \tag {16}
$$

$$
\sum_ {i \in \mathcal {N} _ {r}, r \in \mathcal {R}} \xi_ {(i, j)} \leq 1, \forall j \in \mathcal {N} _ {s}, s \in \mathcal {R} \tag {17}
$$

$$
\sum_ {j \in \mathcal {N} _ {s}, s \in \mathcal {R}} \xi_ {(i, j)} \leq 1, \forall i \in \mathcal {N} _ {r}, r \in \mathcal {R} \tag {18}
$$

$$
\mu_ {i} - \mu_ {j} + \left(\sum_ {r \in \mathcal {R}} N _ {r} - 1\right) \xi_ {(i, j)} \leq \sum_ {r \in \mathcal {R}} N _ {r} - 1, \forall i \in \mathcal {N} _ {r}, j \in \mathcal {N} _ {s}, r, s \in \mathcal {R} \tag {19}
$$

$$
\xi_ {(i, j)} + \xi_ {\left(i ^ {\prime}, j ^ {\prime}\right)} \leq 1, \text {i f} \phi_ {1} \cdot \phi_ {2} <   0 \text {a n d} \phi_ {3} \cdot \phi_ {4} <   0 \tag {20}
$$

$$
\phi_ {1} = (s - r) \cdot \left(i ^ {\prime} - i\right) - (j - i) \cdot \left(r ^ {\prime} - r\right) \tag {21}
$$

$$
\phi_ {2} = (s - r) \cdot \left(j ^ {\prime} - i\right) - (j - i) \cdot \left(s ^ {\prime} - r\right) \tag {22}
$$

$$
\phi_ {3} = \left(s ^ {\prime} - r ^ {\prime}\right) \cdot \left(i - i ^ {\prime}\right) - \left(j ^ {\prime} - i ^ {\prime}\right) \cdot \left(r - r ^ {\prime}\right) \tag {23}
$$

$$
\phi_ {4} = \left(s ^ {\prime} - r ^ {\prime}\right) \cdot \left(j - i ^ {\prime}\right) - \left(j ^ {\prime} - i ^ {\prime}\right) \cdot \left(s - r ^ {\prime}\right) \tag {24}
$$

where $N _ { r }$ and $N _ { s }$ denote the index of the last vehicle on lane $r$ and $s$ , respectively. $\mu _ { i }$ and $\mu _ { j }$ are auxiliary variables that can denote the order of nodes in the sequence. 

Constraints (12)–(13) denote vehicles belonging to one lane cannot overtake, i.e., the passing order of the preceding vehicle is prior to the one of the following vehicle on the same lane, as illustrated in Fig. 2(a). Constraint (14) denotes that the sum of the chosen links must be equal to the total number of vehicles minus one, i.e., the indices of all vehicles in the control area must be in the final merging sequence, as illustrated in Fig. 2(b). Constraints (15)–(16) denote that the vehicles except for the first (last) vehicle in each lane must have an outgoing (incoming) edge, as illustrated in Fig. 2(c). Constraints (17)–(18) denote that each vehicle must have at most one incoming or outgoing edge, as illustrated in Fig. 2(d). Constraint (19) is the MTZ constraint (Miller et al., 1960) to eliminate subtours, as illustrated in Fig. 2(e). Constraint (20) denotes that only one of two intersecting edges can be chosen, as illustrated in Fig. 2(f). In Eqs. (21)–(24), $\forall r , s , r ^ { \prime } , s ^ { \prime } \in \mathcal { R } , i \in  { \mathcal { N } } _ { r } , j , \in  { \mathcal { N } } _ { s } , i ^ { \prime } \in  { \mathcal { N } } _ { r ^ { \prime } } , j ^ { \prime } \in  { \mathcal { N } } _ { s ^ { \prime } } .$ . 

# 3.2.4. Algorithm complexity

The computational complexity of the 0–1 integer programming problem is typically high, making it challenging to solve directly using exact algorithms. In this study, the MS problem can be reformulated as a shortest-path search with a fixed starting node, which allows for more efficient computations using Dijkstra’s algorithm (Dijkstra, 1959). To achieve this, we reconstruct the cost matrix to satisfy the constraints, setting the cost of the corresponding edges to infinity. The computational complexity of the proposed algorithm is $O \left( \left( N _ { \mathrm { r } } + N _ { \mathrm { m } } \right) ^ { 2 } \right)$ where $N _ { \mathrm { m } }$ and $N _ { \mathrm { r } }$ represent the number of mainline and on-ramp vehicles, respectively. 

We compare this complexity with two existing solution algorithms: (1) Dynamic Programming (DP): The DP-based method in Sun et al. (2020) has a complexity of $O ( N _ { \mathrm { r } } ( N _ { \mathrm { m } } + 1 ) ^ { 2 } )$ . (2) Monte Carlo Tree Search (MCTS): The MCTS algorithm in Tang et al. (2022) has a complexity of $O ( 8 ( N _ { \mathrm { m } } + N _ { \mathrm { r } } ) )$ . 

To determine when our method is computationally more efficient, the following conditions must hold: (1) Compared to DP: $( N _ { \mathrm { r } } + N _ { \mathrm { m } } ) ^ { 2 } < N _ { \mathrm { r } } ( N _ { \mathrm { m } } + 1 ) ^ { 2 }$ . (2) Compared to MCTS: $( N _ { \mathrm { r } } + N _ { \mathrm { m } } ) ^ { 2 } < 8 ( N _ { \mathrm { m } } + N _ { \mathrm { r } } )$ . 

Fig. 3 shows the calculation results: the blue and red dots indicate feasible regions where our algorithm outperforms DP and MCTS, respectively, while the dashed blue and red lines represent their corresponding boundary conditions. Using the speed–density relationship calibrated by Han et al. (2022), we also include three contour lines representing average speeds of $1 5 \mathrm { m } / s$ , $2 0 \mathrm { m } / s$ , and $2 5 ~ \mathrm { m } / s$ . The analysis shows that: (1) Compared to DP, our method is computationally advantageous when the number of on-ramp vehicles is lower than the square of the number of mainline vehicles—a condition typically met in real-world scenarios. (2) Compared to MCTS, our method is advantageous when the total number of vehicles is below eight or when the average speed exceeds $2 0 ~ \mathrm { m } / s$ , which can happen in free-flow conditions. 

# 3.3. Motion planning

This section proposes a controller for CAVs to adjust their longitudinal motion and achieve smooth merging control. This study assumes that CAVs can obtain information about all vehicles in the merging zone via roadside sensing devices and V2X technologies, whereas HDVs can only obtain information from their preceding vehicles. For HDVs, we use a stochastic car-following model, 2D-Intelligent Driver model (2D-IDM), proposed by Xiong and Jiang (2022), to model their longitudinal motions. Additionally, the local and string stability of the proposed controller are investigated and analyzed in this section. 

# 3.3.1. Communication network

Consider a platoon consisting of $N + 1$ vehicles, with the platoon leader numbered 0 and $N$ following vehicles. Platoon leader 0 can move freely and cannot be controlled by our algorithm; therefore, we focus on the following $N$ vehicles. The communication topology of the following vehicles is modeled as a directed graph $\mathcal { G } = ( \mathcal { V } , \mathcal { E } , \mathcal { H } )$ . $\mathcal { V } = \{ 1 , \dots , N \}$ denotes the set of nodes that can be controlled by the proposed merging algorithm. $\mathcal { E } = \{ ( i , j ) \} , i , j \in \mathcal { V }$ is the set of edges. $\mathcal { H } = \left[ h _ { i j } \right] \in \mathbb { R } ^ { N \times N }$ is a weighted adjacency matrix representing whether two vehicles have communications, where $h _ { i j }$ is the weight of edge $( i , j )$ . $h _ { i j } = 1$ if and only if $( i , j ) \in \mathcal { E }$ (i.e., vehicle ?? can receive information from vehicle $j )$ ; otherwise, $h _ { i j } = 0$ . The Laplacian matrix $\mathcal { L } = \left[ l _ { i j } \right] \in \mathbf { R } ^ { N \times N }$ can be calculated by $\mathscr { L } = D - \mathscr { H }$ , where $D = \mathrm { d i a g } \left( \delta _ { 1 } , \delta _ { 2 } , \dots , \delta _ { N } \right)$ . $\begin{array} { r } { \delta _ { i } = \sum _ { j = 1 } ^ { N } h _ { i j } } \end{array}$ denotes the in-degree of node $i$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/65b24ab65f21ef8a82cf32543340215af8116a5e992dfcfa682875948fd14c4d.jpg)



Fig. 3. Algorithm complexity comparison between the proposed MS algorithm and other two existing algorithms.


# 3.3.2. Spacing policy

Each vehicle in the platoon will adjust its longitudinal speed to maintain a constant headway with its preceding vehicle. This method is widely used in the literature and can effectively reduce disturbance propagation (Swaroop et al., 1994). Therefore, this study adopts the constant headway approach to determine the spacing policy. The headway between ?? and platoon leader 0 can be represented by Eq. (25). 

$$
g _ {i 0} = \sum_ {j = 1} ^ {i} \tau_ {j} ^ {*}, i \in \mathcal {V} \tag {25}
$$

where $g _ { i 0 }$ is the desired headway between ?? and platoon leader 0, and $\boldsymbol { \tau } _ { j } ^ { * }$ is the headway between $j$ and its first preceding vehicle. The expected spacing $d _ { i 0 } ^ { * }$ related to $g _ { i 0 }$ between ?? and platoon leader can be represented by Eq. (26). 

$$
d _ {i 0} ^ {*} (t) = v _ {i} (t) \cdot g _ {i 0} + \sum_ {j = 0} ^ {i - 1} \left(l _ {j} + d _ {\min }\right), i \in \mathcal {V} \tag {26}
$$

where $v _ { i } \left( t \right)$ is the speed of $i$ at time ??, $l _ { j }$ is the length of vehicle $j$ , and $d _ { \mathrm { m i n } }$ is a constant that denotes the minimum spacing between two adjacent vehicles. 

The deviation of the longitudinal position between ?? and the expected position, $\boldsymbol { \varDelta p _ { i } }$ , and the deviation of the longitudinal speed between ?? and platoon leader, $\Delta v _ { i }$ , can be represented by Eqs. (27)–(28). 

$$
\Delta p _ {i} (t) = p _ {i} (t) - p _ {i} ^ {*} (t), i \in \mathcal {V} \tag {27}
$$

$$
\Delta v _ {i} (t) = v _ {i} (t) - v _ {0} (t), i \in \mathcal {V} \tag {28}
$$

where $p _ { i }$ is the longitudinal position of $i$ , and $\boldsymbol { p } _ { i } ^ { * }$ is the expected position of ?? relative to the position of platoon leader 0, which can be calculated by $p _ { i } ^ { * } = p _ { 0 } - d _ { i 0 } ^ { * }$ . 

Fig. 4 illustrates the space policy in this study more intuitively. 

# 3.3.3. Dynamics

Let $\dot { \boldsymbol { x _ { i } } } \left( t \right) = \left[ \varDelta p _ { i } \left( t \right) , \varDelta v _ { i } \left( t \right) , a _ { i } \left( t \right) \right] ^ { \intercal }$ be the state vector of vehicle ?? at time ??. Here, $a _ { i }$ represents the longitudinal acceleration. This study describes the real-world nonlinear vehicle dynamics using a generalized vehicle dynamics (GLVD) equation from Yi (2001), as shown in Eq. (29). 

$$
\dot {a} _ {i} (t) = - \frac {1}{T _ {i , L}} a _ {i} (t) + \frac {K _ {i , L}}{T _ {i , L}} u _ {i} (t), i \in \mathcal {V} \tag {29}
$$

where $\dot { a } _ { i }$ is jerk, $u _ { i }$ is the desired acceleration generated by the designed control strategy (i.e., controller), $T _ { i , L }$ is the time lag for ?? to realize the acceleration, and $K _ { i , L }$ is the ratio of the demanded acceleration that can be realized. The parameters $T _ { i , L }$ and $K _ { i , L }$ can be adjusted dynamically to reflect the uncertain vehicular dynamics caused by the current road conditions. As suggested by Zhou et al. (2020), we set $K _ { i , L }$ to 1 and $T _ { i , L }$ to 0.45 in simulations. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/d864e4b601ec03557d2b522e0daf48116f37f44af3ba91c883d51b5b3ca3173d.jpg)



Fig. 4. Illustration of the space policy in this study.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/2520b076e798882c7d6a2f21a7c6a51c000af39cf98e5e63ef1aa40e8e6be1a9.jpg)



(a) Two-lane Merging Zone


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/16733be19bf7d24a8bade7c23a021f678f696b5d6e33bb590abe15cbab31fef8.jpg)



(b) Multi-lane Merging Zone



Fig. 5. Simulation scenario in this study: (a) a two-lane merging zone and (b) a multi-lane merging zone.


Based on Eqs. (25)–(29), the state–space system can be formulated as Eq. (30). 

$$
\dot {x} _ {i} (t) = A x _ {i} (t) + B u _ {i} (t) + D a _ {0} (t), i \in \mathcal {V} \tag {30}
$$

⎡0, 1, ????0 0 ⎡ 0 where ?? = ⎢⎢⎢0 , 0, 10 , 0, −1?? ⎥⎥⎥, ?? = ⎢⎢0????,?? ⎥⎥ , ?? = ⎢⎢ − 1 ⎥. ?? (??) is the acceleration of platoon leader, which can be obtained by CAVs via V2X ????,?? ⎥⎦ technologies. 

# 3.3.4. Consensus controller

For every $i \in \mathcal V$ , the objective of the designed controller is to keep $\boldsymbol { \varDelta p _ { i } }$ , $\varDelta v _ { i }$ , and $a _ { i }$ at zero, as shown in Eq. (31). 

$$
\lim  _ {t \rightarrow \infty} | \Delta p _ {i} (t) | = 0; \lim  _ {t \rightarrow \infty} | \Delta v _ {i} (t) | = 0; \lim  _ {t \rightarrow \infty} | a _ {i} (t) | = 0 \tag {31}
$$

In the connected environment, CAVs can obtain information about surrounding vehicles. Therefore, we design a decentralized consensus controller, which can be represented as Eq. (32). 

$$
u _ {i} (t) = \alpha K \sum_ {j = 1} ^ {N} h _ {i j} \left(x _ {j} (t) - x _ {i} (t)\right) \tag {32}
$$

where positio $\alpha > 0$ is a scations, r coupling gain that can be measureis the gain of speed deviations, and $\begin{array} { r } { \alpha = \frac { 1 } { \delta _ { i } } } \\ { . } \end{array}$ $\boldsymbol { K } = \left[ k _ { p } , k _ { v } , k _ { a } \right]$ is the gain vector where . $k _ { p }$ is the gain of $k _ { v }$ $k _ { a }$ 

In the real world, time delays exist in wireless communications. Therefore, we need to consider the impact of communication delays and set suitable gain factors to resist the disturbance of delays. The consensus controller with communication delays can be represented as Eq. (33): 

$$
u _ {i} (t) = \alpha K \sum_ {j = 1} ^ {N} h _ {i j} \left(x _ {j} (t - \theta) - x _ {i} (t - \theta)\right) \tag {33}
$$

where $\theta$ is constant communication delay. 

Thus, the state–space system with communication delays can be written as Eq. (34): 

$$
\begin{array}{l} \dot {x} _ {i} (t) = A x _ {i} (t) + B u _ {i} (t) + D a _ {0} (t) \\ = A x _ {i} (t) + B \alpha K \sum_ {j = 1} ^ {N} h _ {i j} \left(x _ {j} (t - \theta) - x _ {i} (t - \theta)\right) + D a _ {0} (t - \theta) \tag {34} \\ \end{array}
$$

Define a global state vector $X \left( t \right) = \left[ x _ { 1 } ^ { \top } \left( t \right) , x _ { 2 } ^ { \top } \left( t \right) , \ldots , x _ { N } ^ { \top } \left( t \right) \right] ^ { 1 }$ . Based on Eq. (34), the closed-loop dynamics of ?? can be simplified as Eq. (35). 

$$
\dot {X} (t) = I _ {N} \otimes A X (t) - \alpha \mathcal {L} \otimes B K X (t - \theta) + I _ {N} \otimes D A _ {0} (t - \theta) \tag {35}
$$

where $\otimes$ is the Kronecker product. $I _ { N }$ is an $N \times N$ identity matrix. $A _ { 0 } \left( t - \theta \right) = { \Big [ } a _ { 0 } \left( t - \theta \right) , \ldots , a _ { 0 } \left( t - \theta \right) { \Big ] } ^ { \mathsf { T } } . \ N$ $N$ is the number of ?? controlled vehicles. 

# 3.3.5. Lateral control

This study adopts a virtual-platoon approach to achieve cooperative merging control, converting the merging problem into a virtual car-following problem. Therefore, we primarily focus on longitudinal control and simplify the lateral lane-changing process. The lateral control is modeled as follows: If the lane-changing conditions in inequalities (36)–(37) are satisfied, vehicles will start lane-changing maneuver and move at a constant lateral speed until they reach the target mainline lane. Additionally, if vehicles reach the end of the merging zone without changing lanes, they will be forced to merge into the mainline. 

$$
p _ {i - 1} (t) - p _ {i} (t) \geq v _ {i} (t) \cdot \tau^ {*} + l _ {i - 1} + d _ {\min } \tag {36}
$$

$$
p _ {i} (t) - p _ {i + 1} (t) \geq v _ {i + 1} (t) \cdot \tau^ {*} + l _ {i} + d _ {\min } \tag {37}
$$

The conditions ensure that a vehicle can merge from ramp to mainline only if the gap between the vehicle and both its preceding and following vehicles exceeds the expected spacing. If the conditions are not satisfied, the vehicle will continue adjusting its longitudinal speed to find a suitable gap for merging. 

# 3.4. Stability analysis

The parameters in the controller should be carefully set to ensure that the system remains stable under the proposed control strategy. This section analyzes the stability conditions that the system should meet in order to provide parameter-setting criteria. 

# 3.4.1. Local stability

Local stability (or internal stability) refers to the ability of resolving local deviations in position, speed, and acceleration, which is crucial to a control system. This study uses the Lyapunov–Razumikhin theorem to investigate the system’s local stability condition. First, two theorems are introduced to prepare for the following proof. 

Theorem 1 (Lyapunov–Razumikhin Theorem (Hale and Lunel, 1993)). Consider the following delay differential equation $\begin{array} { r l } { \dot { x } \left( t \right) } & { { } = } \end{array}$ $f \left( t , x \left( t \right) , x \left( t - \theta \right) \right)$ where $x \in \mathbf { R } ^ { n }$ , and $\theta$ is a constant time delay. Let $V : \mathbb { R } \times \mathbb { R } ^ { n } \to \mathbb { R } _ { + }$ be a differentiable function which satisfies the conditions $V \left( x \right) > 0 , \forall x \neq 0$ and $V \left( 0 \right) = 0 ,$ . Let ?? be a continuous non-negative function, i.e., $w \left( \zeta \right) > 0 , \forall \zeta > 0 .$ . Let $\rho$ be a continuous non-decreasing function, i.e., $\rho \left( \zeta \right) > \zeta , \forall \zeta > 0$ . 

If $V \left( t + \theta , x \left( t + \theta \right) \right) \leq \rho \left( V \left( t , x \right) \right) , \forall \theta \in \left[ - h , 0 \right] _ { \mathrm { { z } } }$ , the following Eq. (38) holds: 

$$
\dot {V} (t, x) \leq - w (\| x (t) \|) \tag {38}
$$

which denotes the system is globally asymptotically stable. 

Theorem 2 (Stability Condition for Consensus Control (Lewis et al., 2014)). Let $\lambda _ { i }$ be the eigenvalues of Laplacian matrix . The stability properties of the system $\dot { X } \left( t \right) = I _ { N } \otimes A X \left( t \right) - \alpha \mathcal { L } \otimes B K X \left( t \right)$ are equivalent to the stability properties of the $N$ subsystems represented by Eq. (39). 

$$
\dot {x} _ {i} (t) = A x _ {i} (t) - \alpha \lambda_ {i} B K x _ {i} (t), i \in \mathcal {V} \tag {39}
$$

Proposition 1. The closed-loop system $\dot { X } \left( t \right) \ = \ I _ { N } \otimes A X \left( t \right) - \alpha \mathcal { L } \otimes B K X \left( t - \theta \right)$ under the proposed control strategy in Eq. (33) is asymptotically stable if the following condition (40) is satisfied. 

$$
\sum_ {k = 1} ^ {M} \sum_ {l = 1} ^ {M} A _ {k l} - \alpha \bar {\rho} | \lambda_ {i} | \sum_ {k = 1} ^ {M} \sum_ {l = 1} ^ {M} | B _ {k} K _ {l} | \leq 0, \forall i \in \mathcal {V} \tag {40}
$$

where $\bar { \rho }$ is a constant and $\bar { \rho } > 0$ . ?? is the number of the state of $x _ { i } \left( t \right)$ . 

Proof. Based on Theorem 1, let us consider the system in this study. Given the system $\dot { X } \left( t \right) = I _ { N } \otimes A X \left( t \right) + \alpha \mathcal { L } \otimes B K X \left( t - \theta \right) ,$ , we can construct a Lyapunov function (41): 

$$
V (t, X (t)) = \frac {1}{2} X (t) ^ {\top} X (t) \tag {41}
$$

Then, we have (42): 

$$
\dot {V} (t, X (t)) = X (t) ^ {\top} \left[ I _ {N} \otimes A X (t) - \alpha \mathcal {L} \otimes B K X (t - \theta) \right] \tag {42}
$$

Define $\rho \left( V \left( t , x \right) \right) = \bar { \rho } ^ { 2 } \cdot V \left( t , x \right)$ where $\bar { \rho }$ is a constant and $\bar { \rho } > 0$ . The following Eq. (43) should be satisfied to ensure the asymptotic stability. 

$$
\begin{array}{l} V (X (t - \theta)) \leq \tilde {\rho} ^ {2} \cdot V (t, X (t)) \\ \Rightarrow X (t - \theta) ^ {\top} X (t - \theta) \leq \bar {\rho} ^ {2} \cdot X (t) ^ {\top} X (t) \tag {43} \\ \Rightarrow | X (t - \theta) | \leq \bar {\rho} \cdot | X (t) | \\ \end{array}
$$

Based on Eq. (43), Eq. (42) can be simplified as Eq. (44). 

$$
\begin{array}{l} \dot {V} (t, X (t)) = X (t) ^ {\top} \left[ I _ {N} \otimes A X (t) - \alpha \mathcal {L} \otimes B K X (t - \theta) \right] \tag {44} \\ \leq X (t) ^ {\top} I _ {N} \otimes A X (t) - X (t) ^ {\top} | \alpha \mathcal {L} \otimes B K | \bar {\rho} \cdot | X (t) | \\ \end{array}
$$

Based on Theorem 2, the closed-loop system can be decomposed into $N$ subsystems, as Eq. (45). 

$$
\begin{array}{l} \dot {X} (t) = I _ {N} \otimes A X (t) - \alpha \mathcal {L} \otimes B K X (t - \theta) \tag {45} \\ = A x _ {i} (t) - \alpha \lambda_ {i} B K x _ {i} (t - \theta), i \in \mathcal {V} \\ \end{array}
$$

??  Similarly, term $\dot { X ( t ) } ^ { \top } \dot { I _ { N } } \otimes A X ( t ) - X ( t ) ^ { \top } \left| \alpha \mathcal { L } \otimes B K \right| \bar { \rho } \cdot \left| X \left( t \right) \right|$ can be written as a $N$ -subsystem form $\boldsymbol { x } _ { i } ( t ) ^ { \top } A \boldsymbol { x } _ { i } \left( t \right) - \boldsymbol { x } _ { i } ( t ) ^ { \top } \left| \alpha \boldsymbol { \lambda } _ { i } B K \right| \bar { \rho }$ ⋅ $\left| x _ { i } \left( t \right) \right| , i = 1 , 2 , \ldots , N$ , as Eq. (46). 

$$
\begin{array}{l} x _ {i} (t) ^ {\top} A x _ {i} (t) - x _ {i} (t) ^ {\top} \left| \alpha \lambda_ {i} B K \right| \bar {\rho} \cdot \left| x _ {i} (t) \right| \\ = \sum_ {k = 1} ^ {M} \sum_ {l = 1} ^ {M} A _ {k l} x _ {i} (t) ^ {\top} x _ {i} (t) - \alpha \bar {\rho} \left| \lambda_ {i} \right| \sum_ {k = 1} ^ {M} \sum_ {l = 1} ^ {M} \left| B _ {k} K _ {l} \right| x _ {i} (t) ^ {\top} x _ {i} (t) \tag {46} \\ = \left(\sum_ {k = 1} ^ {M} \sum_ {l = 1} ^ {M} A _ {k l} - \alpha \bar {\rho} \left| \lambda_ {i} \right| \sum_ {k = 1} ^ {M} \sum_ {l = 1} ^ {M} \left| B _ {k} K _ {l} \right|\right) V _ {i} (t, x _ {i} (t)), i \in \mathcal {V} \\ \end{array}
$$

Based on Theorem 1, the following condition (47) should be satisfied to ensure the globally asymptotic stability: 

$$
\sum_ {k = 1} ^ {M} \sum_ {l = 1} ^ {M} A _ {k l} - \alpha \bar {\rho} | \lambda_ {i} | \sum_ {k = 1} ^ {M} \sum_ {l = 1} ^ {M} | B _ {k} K _ {l} | \leq 0, \forall i \in \mathcal {V} \tag {47}
$$

# 3.4.2. String stability

String stability means that the magnitude of a disturbance is not amplified for each leader–follower pair through a vehicular string. In this section, we refer to the definition of eventual string stability (ESS) in Feng et al. (2019) to analyze the string stability condition. The linear system is frequency-domain string stable if the transfer function of outputs between vehicle ?? and platoon leader 0, denoted as $G _ { 0 , i }$ , satisfies $\left\| \boldsymbol { G } _ { 0 , i } \left( j \omega \right) \right\| _ { \infty } \leq 1 , i = 1 , \ldots , N$ . 

Proposition 2. The platoon is with ESS if the following inequalities (48)–(52) are satisfied. 

$$
k _ {a} \theta^ {3} T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \geq 0 \tag {48}
$$

$$
\left(- k _ {a} + \frac {1}{3} g _ {i 0} \theta^ {3} + \frac {1}{3} k _ {v} \theta^ {3}\right) \alpha K _ {i, L} \lambda_ {i} + T _ {i, L} ^ {2} + \left(- \frac {1}{3} k _ {p} \theta^ {3} + g _ {i 0} \theta^ {2} + k _ {v} \theta^ {2} + 2 k _ {a} \theta\right) T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \geq 0 \tag {49}
$$

$$
1 + \left(2 k _ {a} + k _ {p} \theta^ {2} - 2 g _ {i 0} \theta - 2 k _ {v} \theta\right) \alpha K _ {i, L} \lambda_ {i} + k _ {a} ^ {2} \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} - 2 \left(g _ {i 0} + k _ {v} - k _ {p} \theta\right) T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \geq 0 \tag {50}
$$

$$
- 2 k _ {p} \alpha K _ {i, L} \lambda_ {i} + \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} \left(- 2 k _ {a} k _ {p} + g _ {i 0} ^ {2} + 2 g _ {i 0} k _ {v} + k _ {v} ^ {2}\right) \geq 0 \tag {51}
$$

$$
\left(1 - k _ {p} ^ {2} - \omega^ {2} k _ {v} ^ {2}\right) \geq 0 \tag {52}
$$

Proof. Based on Eq. (29), we have (53): 

$$
\begin{array}{l} \dot {a} _ {i} (t) = \frac {- 1}{T _ {i , L}} a _ {i} (t) + \frac {K _ {i , L}}{T _ {i , L}} u _ {i} (t) \\ \Rightarrow \dot {a} _ {i} (t) = \frac {- 1}{T _ {i , L}} a _ {i} (t) + \frac {K _ {i , L}}{T _ {i , L}} \alpha K \sum_ {j = 1} ^ {N} h _ {i j} \left(x _ {j} (t - \theta) - x _ {i} (t - \theta)\right) \tag {53} \\ \Rightarrow \dot {\mathcal {A}} (t) = \frac {- 1}{T _ {i , L}} \mathcal {A} (t) - \frac {K _ {i , L}}{T _ {i , L}} \alpha \mathcal {L} \otimes K X (t - \theta) \\ \end{array}
$$

Notice that $\begin{array} { r } { \dot { \mathcal { A } } \left( t \right) = \frac { - 1 } { T _ { i , L } } \mathcal { A } \left( t \right) - \frac { K _ { i , L } } { T _ { i , L } } \alpha \mathcal { L } \otimes K X \left( t - \theta \right) } \end{array}$ −1  (??) − ????,?? ?? ⊗ ???? (?? − ??) can be written in the ??-subsystem form as Eq. (54): $N$ ????,?? ????,?? 

$$
\dot {a} _ {i} (t) = \frac {- 1}{T _ {i , L}} a _ {i} (t) - \alpha \frac {K _ {i , L}}{T _ {i , L}} \lambda_ {i} K x _ {i} (t - \theta), i = 1, \dots , N \tag {54}
$$

Therefore, we have Eq. (55) with Laplacian transformation: 

$$
s a _ {i} (s) = \frac {- 1}{T _ {i , L}} a _ {i} (s) - \alpha \frac {K _ {i , L}}{T _ {i , L}} \lambda_ {i} e ^ {- \theta s} K x _ {i} (s), i = 1, \dots , N \tag {55}
$$

And by $\begin{array} { r } { \varDelta v _ { i } \left( s \right) = \frac { a _ { i } \left( s \right) - a _ { 0 } \left( s \right) } { s } } \end{array}$ , and $\begin{array} { r } { \varDelta p _ { i } \left( s \right) = \frac { a _ { i } \left( s \right) - a _ { 0 } \left( s \right) } { s ^ { 2 } } + \frac { a _ { i } \cdot g _ { i 0 } } { s } } \end{array}$ , (48) can be simplified as Eq. (56): 

$$
\begin{array}{l} a _ {i} (s) = G _ {0, i} (s) \cdot a _ {0} (s) \\ = \frac {\alpha \frac {K _ {i , L}}{T _ {i , L}} \lambda_ {i} e ^ {- \theta s} \left(\frac {k _ {p}}{s ^ {2}} + \frac {k _ {v}}{s}\right)}{s + \frac {1}{T _ {i , L}} + \alpha \frac {K _ {i , L}}{T _ {i , L}} \lambda_ {i} e ^ {- \theta s} \left(\frac {k _ {p}}{s ^ {2}} + \frac {g _ {i 0} + k _ {v}}{s} + k _ {a}\right)} \cdot a _ {0} (s) \tag {56} \\ = \frac {\alpha K _ {i , L} \lambda_ {i} e ^ {- \theta s} (k _ {p} + s k _ {v})}{T _ {i , L} s ^ {3} + s ^ {2} + \alpha K _ {i , L} \lambda_ {i} e ^ {- \theta s} (k _ {p} + (g _ {i 0} + k _ {v}) s + k _ {a} s ^ {2})} \cdot a _ {0} (s), i = 1, \ldots , N \\ \end{array}
$$

where $G _ { 0 , i } \left( s \right)$ is the transfer function between platoon leader 0 and vehicle ??. 

By $e ^ { - j \theta \omega } = \cos { ( \theta \omega ) } - j \sin { ( \theta \omega ) } ,$ , we have (57): 

$$
\begin{array}{l} G _ {0, i} (j \omega) = \frac {\alpha K _ {i , L} \lambda_ {i} (\cos (\theta \omega) - j \sin (\theta \omega)) (k _ {p} + k _ {v} j \omega)}{- T _ {i , L} j \omega^ {3} - \omega^ {2} + \alpha K _ {i , L} \lambda_ {i} (\cos (\theta \omega) - j \sin (\theta \omega)) (k _ {p} + (g _ {i 0} + k _ {v}) j \omega - k _ {a} \omega^ {2})} \\ = \frac {\alpha K _ {i , L} \lambda_ {i} \left(k _ {p} \cos (\theta \omega) + k _ {v} \omega \sin (\theta \omega)\right) + j \cdot \alpha K _ {i , L} \lambda_ {i} \left(k _ {v} \cos (\theta \omega) \omega - k _ {p} \sin (\theta \omega)\right)}{- \omega^ {2} + \alpha K _ {i , L} \lambda_ {i} \left(\left(k _ {p} - k _ {a} \omega^ {2}\right) \cos (\theta \omega) + \omega \sin (\theta \omega) \left(g _ {i 0} + k _ {v}\right)\right)} \tag {57} \\ + j \cdot \left(- T _ {i, L} \omega^ {3} + \alpha K _ {i, L} \lambda_ {i} \left(\cos (\theta \omega) \left(g _ {i 0} + k _ {v}\right) \omega + \left(k _ {a} \omega^ {2} - k _ {p}\right) \sin (\theta \omega)\right)\right) \\ \end{array}
$$

The norm of $G _ { 0 , i } \left( j \omega \right)$ can be represented as (58): 

$$
\begin{array}{l} \left| G _ {0, i} (j \omega) \right| = \frac {\alpha^ {2} K _ {i , L} ^ {2} \lambda_ {i} ^ {2} \left(k _ {p} ^ {2} + \omega^ {2} k _ {v} ^ {2}\right)}{\omega^ {4} - 2 \omega^ {2} \alpha K _ {i , L} \lambda_ {i} \left(\left(k _ {p} - k _ {a} \omega^ {2}\right) \cos (\theta \omega) + \omega \sin (\theta \omega) \left(g _ {i 0} + k _ {v}\right)\right)} \tag {58} \\ + \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} \left(\left(k _ {p} - k _ {a} \omega^ {2}\right) ^ {2} + \omega^ {2} \left(g _ {i 0} + k _ {v}\right) ^ {2}\right) \\ + T _ {i, L} ^ {2} \omega^ {6} \\ - 2 T _ {i, L} \omega^ {3} \alpha K _ {i, L} \lambda_ {i} (\omega \cos (\theta \omega) (g _ {i 0} + k _ {v}) - (k _ {p} - k _ {a} \omega^ {2}) \sin (\theta \omega)) \\ \end{array}
$$

Given the complexity of the sinusoidal and cosinusoidal terms, we use the Taylor expansion to replace term cos $( \theta \omega )$ and sin (????) approximatively where $\theta \omega$ is a very small number, which can be represented as Eqs. (59)–(60): 

$$
\cos (\theta \omega) = 1 - \frac {(\theta \omega) ^ {2}}{2} + o (\theta \omega) \tag {59}
$$

$$
\sin (\theta \omega) = \theta \omega - \frac {(\theta \omega) ^ {3}}{3 !} + o (\theta \omega) \tag {60}
$$

Therefore, $\left| G _ { 0 , i } \left( j \omega \right) \right|$ can be written as Eq. (61): 

$$
\begin{array}{l} \left| G _ {0, i} (j \omega) \right| \\ = \frac {\alpha^ {2} K _ {i , L} ^ {2} \lambda_ {i} ^ {2} \left(k _ {p} ^ {2} + \omega^ {2} k _ {v} ^ {2}\right)}{\frac {1}{3} k _ {a} \theta^ {3} T _ {i , L} \alpha K _ {i , L} \lambda_ {i} \omega^ {8}} \\ + \left[ \begin{array}{l} \left(- k _ {a} + \frac {1}{3} g _ {i 0} \theta^ {3} + \frac {1}{3} k _ {v} \theta^ {3}\right) \alpha K _ {i, L} \lambda_ {i} + T _ {i, L} ^ {2} \\ + \left(- \frac {1}{3} k _ {p} \theta^ {3} + g _ {i 0} \theta^ {2} + k _ {v} \theta^ {2} + 2 k _ {a} \theta\right) T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \end{array} \right] \omega^ {6} \tag {61} \\ + \left[ \begin{array}{l} 1 + \left(2 k _ {a} + k _ {p} \theta^ {2} - 2 g _ {i 0} \theta - 2 k _ {v} \theta\right) \alpha K _ {i, L} \lambda_ {i} \\ + k _ {a} ^ {2} \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} - 2 \left(g _ {i 0} + k _ {v} - k _ {p} \theta\right) T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \end{array} \right] \omega^ {4} \\ + \left[ - 2 k _ {p} \alpha K _ {i, L} \lambda_ {i} + \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} \left(- 2 k _ {a} k _ {p} + g _ {i 0} ^ {2} + 2 g _ {i 0} k _ {v} + k _ {v} ^ {2}\right) \right] \omega^ {2} \\ + \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} k _ {p} ^ {2} \\ \end{array}
$$

Based on the definition of ESS, (i.e., $\left\| G _ { 0 , i } \left( j \omega \right) \right\| _ { \infty } \le 1 , i = 1 , \ldots , N )$ , we have the following inequality (62): 

$$
\begin{array}{l} \frac {1}{3} k _ {a} \theta^ {3} T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \omega^ {8} \\ + \left[ \begin{array}{l} \left(- k _ {a} + \frac {1}{3} g _ {i 0} \theta^ {3} + \frac {1}{3} k _ {v} \theta^ {3}\right) \alpha K _ {i, L} \lambda_ {i} \\ + T _ {i, L} ^ {2} + \left(- \frac {1}{3} k _ {p} \theta^ {3} + g _ {i 0} \theta^ {2} + k _ {v} \theta^ {2} + 2 k _ {a} \theta\right) T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \end{array} \right] \omega^ {6} \\ + \left[ \begin{array}{l} 1 + \left(2 k _ {a} + k _ {p} \theta^ {2} - 2 g _ {i 0} \theta - 2 k _ {v} \theta\right) \alpha K _ {i, L} \lambda_ {i} + k _ {a} ^ {2} \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} \\ - 2 \left(g _ {i 0} + k _ {v} - k _ {p} \theta\right) T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \end{array} \right] \omega^ {4} \tag {62} \\ + \left[ - 2 k _ {p} \alpha K _ {i, L} \lambda_ {i} + \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} \left(- 2 k _ {a} k _ {p} + g _ {i 0} ^ {2} + 2 g _ {i 0} k _ {v} + k _ {v} ^ {2}\right) \right] \omega^ {2} \\ + \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} k _ {p} ^ {2} \left(1 - k _ {p} ^ {2} - \omega^ {2} k _ {v} ^ {2}\right) \geq 0 \\ \end{array}
$$

Inequality (62) holds if the following inequalities (63)–(67) for $i = 1 , \ldots , N$ are satisfied. 

$$
k _ {a} \theta^ {3} T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \geq 0 \tag {63}
$$

$$
\left(- k _ {a} + \frac {1}{3} g _ {i 0} \theta^ {3} + \frac {1}{3} k _ {v} \theta^ {3}\right) \alpha K _ {i, L} \lambda_ {i} + T _ {i, L} ^ {2} + \left(- \frac {1}{3} k _ {p} \theta^ {3} + g _ {i 0} \theta^ {2} + k _ {v} \theta^ {2} + 2 k _ {a} \theta\right) T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \geq 0 \tag {64}
$$

$$
1 + \left(2 k _ {a} + k _ {p} \theta^ {2} - 2 g _ {i 0} \theta - 2 k _ {v} \theta\right) \alpha K _ {i, L} \lambda_ {i} + k _ {a} ^ {2} \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} - 2 \left(g _ {i 0} + k _ {v} - k _ {p} \theta\right) T _ {i, L} \alpha K _ {i, L} \lambda_ {i} \geq 0 \tag {65}
$$

$$
- 2 k _ {p} \alpha K _ {i, L} \lambda_ {i} + \alpha^ {2} K _ {i, L} ^ {2} \lambda_ {i} ^ {2} \left(- 2 k _ {a} k _ {p} + g _ {i 0} ^ {2} + 2 g _ {i 0} k _ {v} + k _ {v} ^ {2}\right) \geq 0 \tag {66}
$$

$$
\left(1 - k _ {p} ^ {2} - \omega^ {2} k _ {v} ^ {2}\right) \geq 0 \tag {67}
$$

# 4. Experiments and results

To evaluate the performance of the proposed controller, we first design several numerical simulation experiments using MATLAB. Next, we build a joint simulation platform using MATLAB and Simulation of Urban MObility (SUMO), an open-source microscopic traffic simulation software (Lopez et al., 2018), to analyze the impact of CAVs equipped with the proposed merging control strategy on traffic flow. Fig. 5 illustrates the simulation scenarios. The first scenario is a two-lane merging zone consisting of a mainline and a ramp, while the second scenario is a multi-lane merging zone consisting of a ramp, an inner lane, and an outer lane. The length of the control area is $2 0 0 ~ \mathrm { { m } }$ . The initial speed of mainline vehicles is $2 0 \ \mathrm { m } / s ,$ , while that of on-ramp vehicles is $1 5 \ \mathrm { m } / s .$ . CAVs will be controlled by the proposed merging algorithm if they enter the control area and HDVs will be controlled by 2D-IDM. 

The hyperparameters in the proposed algorithm are listed in Table 1. The weighting factors $\beta _ { 1 }$ , $\beta _ { 2 }$ , and $\beta _ { 3 }$ are set to 0.25, 0.25, and 0.5 based on the importance of the three objectives (also can be set to other values). The simulation timestep ???? and the communication delay $\theta$ are set to 0.1 s and 0.05 s, respectively. The desired time gap $\tau ^ { * }$ and the minimum safe distance $d _ { \mathrm { m i n } }$ are uniformly set to 2.5 s and $5 \textrm { m }$ , respectively. Two dynamics parameters $T _ { i , L } , K _ { i , L }$ are determined to be 0.45 and 0.1 (Zhou et al., 2020). The gain factors in the proposed algorithm should be set carefully to ensure the stability conditions. Therefore, we calculate the feasible region of the three gain factors $k _ { p } , k _ { v } , k _ { a }$ that satisfies the local and string stability conditions simultaneously, as shown in Fig. 6. Finally, we select a set of suitable parameters $( k _ { p } = 0 . 3 1 , k _ { v } = 1 . 4 8 , k _ { a } = - 0 . 6 4 )$ from the feasible region to achieve the best performance. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/6072b3a2619a310e97255a4831b8f3dbce7ed830e0feb5b596f220f70fe46495.jpg)



Fig. 6. Feasible region of the three gain factors under different hyperparameters.



Table 1 Hyperparameters in the proposed algorithm.


<table><tr><td>Hyperparameter</td><td>Value (unit)</td></tr><tr><td>β1,β2,β3</td><td>0.25, 0.25, 0.5</td></tr><tr><td>Δt,θ</td><td>0.1 s, 0.05 s</td></tr><tr><td>τ*,dmin</td><td>2.5 s, 5 m</td></tr><tr><td>Til,L,Kil,L</td><td>0.45, 0.1</td></tr><tr><td>kp,kv,ka</td><td>0.31, 1.48, -0.64</td></tr></table>

# 4.1. Numerical simulations

We design several experiments to evaluate the self-performance of the proposed controller, focusing on its (1) effectiveness and (2) anti-disturbance performance. 

# 4.1.1. Effectiveness

A well-performing controller should handle different driving conditions, enabling vehicles to execute quick and stable maneuvers according to the given merging sequence. To test the effectiveness of the proposed controller, we design two experiments including a two-vehicle case and a multi-vehicle case. 

# (1) Two-vehicle case

In this experiment, we place two vehicles in the merging zone: a background mainline vehicle (which maintains a preset speed) and an on-ramp vehicle (controlled by our algorithm). The results are illustrated in Fig. 7. In Fig. 7(a), the on-ramp vehicle is ahead of the mainline vehicle, with a position error of about $\mathtt { - 4 0 }$ . It is observed that the on-ramp vehicle slows down and allows the mainline vehicle to pass first within about 0.2 s. Fig. 7(b) shows that the on-ramp vehicle is behind the mainline vehicle, so it yields 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/59dbb7ca3844ccb80f20d8440c2670c19f4c5968f3ad2e72ab4167b6163cb6c3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/af2932a33e193ad684eac3298d6b4a3fd4cd0aae362febe034cd11f5ed25f46b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/d6c1a3d5ed7fc103233f2c09072c1a98ee83d0c75daca0aaa9e47e7572fc0e7c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/9817b256ec290a715679ae2c8c051cb2e58390b91de0596aaa0a113da39d94b8.jpg)



(a）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/72c7afc333816658d42c9f456b56c73a14d4d1808d87f16847b6f23e78cf4e65.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/e5a2738c852f294985a4658ba3af919c37eef03ca4c578cdb6d306f08f60f955.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/d140a6694c49185104f2723d3cdca1525ddcdce6b3969ad0131c5030ec8a2a0c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/aaf3b5449cfca08693d45f2fcd0da6ce53ba4d167302c8c1379b3192d1e17e37.jpg)



(b)



Fig. 7. The effectiveness of the proposed controller in the two-vehicle case: (a) An overtaking case, (b) A car-following case.


and continues to follow. The results demonstrate that the proposed controller enables CAVs to make reasonable maneuvers based on the surrounding environment quickly. 

# (2) Multi-vehicle case

In this experiment, the speed of platoon leader is set to $2 0 ~ \mathrm { m } / s _ { \cdot }$ , and the platoon size is set to 15. The following vehicles will adjust their speed using the proposed controller. As illustrated in Fig. 8, we record the deviations (including $\varDelta p , \ \varDelta v , \ a )$ , position, speed, and acceleration of each vehicle in the platoon under scenarios with different CAV penetration rates. The results show that the time to reach stability is approximately 1 s in the case of $0 \%$ CAV penetration rate and about 0.5 s in the case of $1 0 0 \%$ CAV penetration rate. In addition, as CAV penetration rates increase, the maximum control input of each vehicle decreases significantly. 

The results demonstrate that the proposed controller can stabilize the platoon efficiently, and its performance can be improved by increasing the CAV penetration rates. 

# 4.1.2. Anti-disturbance performance

As mentioned above, many existing controllers assume the speed of the platoon leader to be constant, which is unrealistic and has low anti-disturbance capability. Additionally, these controllers are not suitable for mixed-traffic environments where the platoon leader may change speed suddenly. Therefore, this study designs a controller that considers time-varying platoon leader speed to enhance the anti-disturbance capability of mixed-traffic platoons. 

In this section, we conduct an experiment to test the anti-disturbance performance of the platoon using the proposed controller. In the simulation, the acceleration of platoon leader is set to a sine function of time with a variation between $- 2 \mathbf { m } / s ^ { 2 }$ and $2 \mathrm { m } / s ^ { 2 }$ , and the platoon size is set to 15. As before, we record the deviation, position, speed, and acceleration of each vehicle in the platoon for different CAV penetration rates, as shown in Fig. 9. The results show a lag in speed and acceleration when the CAV penetration rate is $0 \%$ . As CAV penetration rates rise, the lag gradually decreases. Moreover, it can be observed that the speed variation of platoon leader is dampened gradually. The results show that enhancing the penetration rates of CAVs equipped with the proposed controller can improve the anti-disturbance performance and robustness of the platoon. 

# 4.2. Traffic-flow simulations

In this section, we simulate the impact of CAVs equipped with the proposed merging control strategy on traffic flow using SUMO (readers can watch the simulation video via https://youtu.be/-xCuYxraxjU). The traffic-flow simulations are conducted in two scenarios: a two-lane merging zone and a multi-lane merging zone. For each scenario, the traffic demand is set at two levels: 900 vehicles per hour (vph) per lane and 1200 vph per lane. The CAV penetration rate is set at $0 \%$ , $2 5 \%$ , $5 0 \%$ , $7 5 \%$ , and $1 0 0 \%$ . The simulation runs for 120 s. The results include the trajectories of all vehicles in the merging zone, as well as the average speed, acceleration, delay, and throughput of all vehicles in the zone (statistics are provided in the Appendix). 

In each simulation, we conduct cross-validation on two merging sequence strategies: (1) the First-Come-First-Served (FCFS) rule and (2) the proposed Merging Sequencing (MS) algorithm, as well as two car-following controllers: (1) the controller proposed by Zhou et al. (2020) (referred to as CF) and (2) the proposed Consensus Controller (CC). By combining the FCFS and MS algorithms with the CF and CC controllers, we establish four control strategies: FCFS+CF, FCFS+CC, $\mathrm { M S + C F }$ , and ${ \mathrm { M S } } { + } { \mathrm { C C } }$ , and evaluate their performance. Furthermore, we compare the proposed algorithm with the controllers in existing studies to further verify its effectiveness. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/84cc6ee462dd926374b4ee8908f8fd039f71b46b658713593c0d2305f4ca8f37.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/b374540146566c20df8792ef89fc403c92c26828ee75b4c161a88f9021c508d7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/bebe3bde339b77b16bac85d8f76042ebf3d6561766f95dfd3e4edb7d56ddda21.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/aebe22b5bbad5bd3090587059964f670209f5e9f00b400144b225eb56ae26a9d.jpg)



(a)0%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/e92611f345c7ffba785f06fcbd7f340e40651996ffd8c99c4a433882c54b40dd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/077034805762319cf2e8a2d40652ffb934cda473c50906cd16d4865a10313181.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/66872f9a05834fd5db76192d40e99e4c0f88e85b3f9b9128bf68737b83a49f42.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/c1759172adb19ee90dccfd52f0d9fb9c5c4bc6281671c9a5474d3fcb76fe6c02.jpg)



(c） $50 \%$ CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/ed44314f358392a47deb9dea5a267b7c72f171de3f9d908c600aee3057aaec99.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/07a5dbdca70cc7706baf68f960fbc9687c8f1717b14f7e776bde67d743c3fec1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/24f974272d9f0facf894266846c98837057153099b8c84d364364098c076f1f9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/4d9bc108285426c1fb9dd69f49e59feb2419ae5daf1cf2f40b5e7ad2d39e90ce.jpg)



(e)100%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/384d3e4cc9dafdc12b63ae6dcd60447a4f00d816e579ff2d86d16e081492dbad.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/090dc897ca27ecce64b752846c490b035da287585d34b124b2b58cdb97bdcf5a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/2c15fffb5af67bdf649c5ba55a8b2883250c21e9e370e834ccbd343692cf47f5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/7110300eec99f560ec74d4183a29500a5778b09d2475484466f5c312362ad25f.jpg)



(b)25%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/7f9dd29dfd91b8f8af9518b9c2c2a1f71552b59897d40174e1c81c7fa75fcb68.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/5f97cbe524d02d92a1298955fb602291faf4268acbb72c50faf11c3d92960887.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/83abf1c976b10875062dc1bd0b658d74bca9ffdb8440583ac3111a6c706c2c4a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/36d6f518f75f3c8090cf3a6410aba29a02ef3d2203d68decfd0b6f5cec573fd9.jpg)



(d)75%CAV



Fig. 8. Deviations, position, speed, and acceleration of each vehicle in the platoon of fifteen vehicles under different penetration rates of CAVs (a case of constant platoon leader speed).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/2df2ac78a53af6fb9df517495789cb8550471cb574297f1f2641d61177016db3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/7afd787379613a7d070cc727d99e64930cfdc1ff5eddabcd543b4ee1fe4bfaed.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/e05fe8014a9a8025a2581b5cd2fb3901fe8ee30105dd7841ec90226fd274fa06.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/c6915eca591d75fc2d85a6ef822d6effe30c6284daa0127cbb087f1313154b38.jpg)



(a)0%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/fe228dc6b28c26af1fc848945a25f62a5a7f0b2a897a1caa8e6d379b77e658fc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/04b0fd67a8c8b1912fa47a6578bb1d8c8820a93c8814886914af763a7f3027bf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/42aede4994d97be64a595af7c06aae27e0ed817527ced38737608eaf8e4dd3da.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/001ba9297d907d12162fea102c00aa3889f88d51b36bd80b04f85e47f4483eb8.jpg)



(c)50%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/41819ef0f5f0f5d7c4cb2323285e4cd1e4f6c188243b12043b78e442ea9ef2ec.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/f6716480da636c454ca3c814efbe5ad3c5a33eb1e27ee8fbcf6c6353d069f7c0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/b62d1b6e1e98e5ad8e52b9f17ee7018bcc671b37b4893ae552727a418e450612.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/ecb71f06b82be59b0d8adaab4b0210197c669e6d291ba43325ca1c643160a4c9.jpg)



(e)100%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/4755ba4edf17b7bd93ed167545adbdeacb6d177fa9722afff6e3146f6037f95d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/f11c4b1e0d516ca7474ae4febdf2414e34cdf12877507965ffa2edb2b9192188.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/5694f615ab592bfd1c28e97a38d04dbc3dea13f30761f3dd0433f98a8984c0b1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/eb6352c8ac86565772e9a34b24a2769521faf31994361099ce24e32b0410148d.jpg)



(b)25% CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/597fa7512c3d0858364008be42722f73e82f45f971c2bfba0f49c08015fa1435.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/748cafc527572fcfdc0c1c346c6d6d659931105975bdc2eeebdd60fd1a426fac.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/dcbfff0a12f7f19adc3b0430921c1ef6cf7ec21fde6ee11492bc541ee9b3f09f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/5a2dbb4c6ac446b461c653460663dcc1105593d7bf674071f0949e076946c76b.jpg)



(d)75%CAV



Fig. 9. Deviations, positions, speed, and acceleration of each vehicle in the platoon of fifteen vehicles under different penetration rates of CAVs (a case of time-varying platoon leader speed).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/d43312a767a6b29c8a1368c4c8f049a2e0bb476a391dbe4cbc6c3f34a9419f46.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/b612e67fdb1623f559779b4c8ac2025a304c1fb18514848cccdb23d49627ca40.jpg)



(a)25%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/37f6d59442d1a376d89e1645176689883f85cd831d1359a35adf4aa6e7a5a97a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/6391f7eb71ae6ceb76864ae29bf27fc32d9b3e69ee6bd8b8dbfe54d839d57ae7.jpg)



(b)50% CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/5ddc6584437a279e8de4040102c5153aa1c0a5710f8186d1394a98a2ae620d9e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/7c45a0f89eb21a4a4a5079c73f73efed5b7711e5f6d1ff613ca8f8f8ca58c2f5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/914e3e6f1792d85f4b09cb4a570c4689596b816ad1f824a25286d83469ab9155.jpg)



(c) 75% CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/398b7d1ef0a1bcfddd3b11cc02a90ee6b37501b829793a8c93d3a233563296d2.jpg)



(d) 100% CAV



Fig. 10. Trajectories of the vehicles with four controllers in the two-lane merging zone under different penetration rates (Demand = 900 vph/lane).


# 4.2.1. Two-lane scenario

# (1) Demand $= 9 0 0$ vph/lane

Fig. 10 shows the trajectories under a demand of 900 vph/lane for four control algorithms. The blue solid lines represent mainline vehicles, while the pink dashed lines indicate on-ramp vehicles. For the FCFS-based algorithms, the merging sequence is only determined by their arrival time, which is not realistic and may lead to traffic oscillation. In contrast, the proposed MS-based algorithms dynamically calculate the optimal merging sequence based on the real-time state of the vehicles, aligning more closely with real-world human driving behaviors. Additionally, the proposed CC controller can stabilize traffic flow more effectively than CF controller. 

Fig. 11 presents the average speed, acceleration, delay, and throughput in the merging zone under different CAV penetration rates for a demand of 900 vph/lane. As shown in the figure, the proposed $\mathrm { M S + C C }$ algorithm leads to higher traffic efficiency, with an average speed of approximately $2 4 ~ \mathrm { m } / s$ , while maintaining relatively low acceleration (not exceeding $1 . 1 \mathrm { ~ m ~ } / s ^ { 2 }$ ). The average delay with the proposed algorithm is 0.26 s, which is lower than that of the other three controllers. Furthermore, the maximum throughput reaches 896 vph per lane, which is close to the traffic demand. These results demonstrate that: (1) the merging sequence generated by the MS algorithm is more efficient than that of the FCFS approach, and (2) the proposed CC controller significantly improves traffic efficiency and contributes to flow stability. 

# (2) Demand $= 1 2 0 0$ vph/lane

Fig. 12 shows the trajectories in the merging zone under a traffic demand of 1200 vph/lane. It is observed that the merging trajectories based on $\mathrm { M S + C C }$ are smoother and more stable compared to the other algorithms. Additionally, traffic oscillations are reduced gradually as the CAV penetration rate increases. 

Fig. 13 presents the average speed, acceleration, delay, and throughput under different CAV penetration rates and a demand of 1200 vph/lane. Similar to the 900 vph/lane scenario, the proposed $\mathrm { M S + C C }$ algorithm leads to higher traffic efficiency compared to the other algorithms while maintaining relatively low acceleration levels. Moreover, the average delay is lower and the throughput is higher with the proposed approach compared with the other three controllers. These results indicate that the proposed algorithm can handle high traffic demand and facilitate efficient interactions between CAVs and HDVs. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/5f09bde1293ecc97ac472fdf0d05fd7f92d17f478aee954d442687d43419b385.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/823118e1bff88b3cba7b82363a35a2576add93ddcdac4c700a2a3c81e92dc03c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/b6f48580a66d1f1eadf7127777a435699bb38adade33e5bb542f96596278d084.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/28d6230d4e4989aaf86ce96fcfe783ded3277c38823d888a05ac7b1ac36f86a6.jpg)



Fig. 11. Average speed, acceleration, delay, and throughput with four controllers in the two-lane merging zone under different penetration rates (Demand $=$ 900 vph/lane).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/60116be5875ed1d11b6093f8ec91221b48ecd166a77ea2e0fd18ba9452b946aa.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/f6dd87e0d222f85cc66c3fc83b51c02563c2a51bf3d34d68b6726d65a2ae3663.jpg)



(a)25%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/da072142ee5728fb9d49238c6ebff5368cd48d00c99550b45c82646bd82c2aaf.jpg)



(b)50%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/1d44408fb1647b23243abd9e6aa2ce2215f77c3f4ff11e73a978989a382696b2.jpg)



(c) 75% CAV



(d)100%CAV



Fig. 12. Trajectories of the vehicles with four controllers in the two-lane merging zone under different penetration rates (Demand $=$ 1200 vph/lane).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/69fb82ea7acb6fe8b4e25099bbf3a1f19a4f0b0e7ae7bb2f2ca0e242202a96b4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/0a77fa91c0ae4497104d25dadfb4f471107cdec3f74022d3e15d0786fbb96a48.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/987cf8a46ddf4b138ba5f3ce293a2ba9156ba69b279f57c1bc7557a891b3b48f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/ea5d88a85184bcca9c9b2c7dbfea1b8b0dbfc645dbffce8fb3e3209e57d5bc3c.jpg)



Fig. 13. Average speed, acceleration, delay, and throughput with four controllers in the two-lane merging zone under different penetration rates (Demand $=$ 1200 vph/lane).


# 4.2.2. Multi-lane scenario

# (1) 900 vph/lane

Fig. 14 shows the trajectories of vehicles in the multi-lane merging zone under different penetration rates and a traffic demand of 900 vph/lane. The blue solid lines represent the inner mainline vehicles, the blue dashed lines represent the outer mainline vehicles, and the pink dashed lines represent the on-ramp vehicles. Fig. 15 shows the average speed, acceleration, delay, and throughput in the multi-lane merging zone under different penetration rates. 

# (2) 1200 vph/lane

Fig. 16 shows the trajectories of the vehicles in the multi-lane merging zone under different penetration rates and a traffic demand of 1200 vph/lane. Fig. 17 shows the average speed, acceleration, delay, and throughput in this scenario. The results are consistent with the previous experiments, indicating that the proposed algorithm maintains high traffic efficiency and stability even under higher traffic demand. 

# 4.2.3. Comparison with other algorithms

We design an experiment to compare the performance of the proposed merging algorithm with that of other controllers proposed by Zhou and Ahn (2019), Sun et al. (2020), and Han et al. (2023). The results are shown in Fig. 18. As observed, under a demand of 900 vph/lane, the proposed algorithm achieves the highest speed $( 2 4 . 2 2 \ : \mathrm { m } / s$ at $1 0 0 \%$ penetration) while maintaining relatively lower acceleration. Under the demand of 1200 vph/lane, traffic efficiency remains the highest $2 4 . 1 1 \ \mathrm { m } / s$ at $1 0 0 \%$ penetration). Moreover, the average delay using the proposed algorithm is the lowest and the throughput is the highest in all scenarios. The results demonstrate that the proposed algorithm outperforms the other models in terms of both traffic efficiency and driving comfort, particularly at a higher CAV penetration rate. 

# 4.2.4. Robustness against different HDV behavior

To evaluate the robustness of the proposed algorithm against different real-world HDV driving behavior, we conduct an experiment under different types of background HDV traffic flow conditions using four existing models: (1) IDM (Milanés and Shladover, 2014), (2) 2D-IDM (Xiong et al., 2022), (3) Krauss model (Krauss et al., 1997), and (4) General Motors (GM) model (Gazis et al., 1961). The results demonstrate that the proposed algorithm consistently achieves high traffic efficiency and driving comfort in all scenarios, indicating its robustness against different real-world HDV behaviors. (See Fig. 19.) 

# 5. Conclusions

This study proposes a hierarchical cooperative merging control strategy for CAVs in a mixed traffic environment involving both CAVs and HDVs. The strategy consists of two layers: a merging sequencing layer and a motion planning layer. In the merging 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/62b6c8c84743c5b9827e981a3fc07fdf1d598179f1580f7b7328950c833c8015.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/c7a9173e36ed69efb878e5de5f6a6dcbc8f8f13183155350ddf2fd5d25da9228.jpg)



(a)25%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/e6d1597ec992d670179fd7f1280e165ea2ba1e95075134f8b28e75377b07bb68.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/76051c76d524917eac4b39485ac4def9c0caddc43f04c369d05b6bbecb81754a.jpg)



(c) 75% CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/94515936a03e241abc6c576feebf0eb23fdc8a5a9a1a3648703d42cc2f305d80.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/4445a28952b1248f816e975a4cefd7fb077f8418593b853310b0d4d33a6a06f8.jpg)



(b)50%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/f1221bdeef0978221894652b6238cc058957db9a671b3e21d5cee159971e3db1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/4ecfe54339cfe72009d92bcb68abbbc6d1de402663cfe5558017b7bbdcb65c7a.jpg)



(d)100% CAV



Fig. 14. Trajectories of the vehicles with four controllers in the multi-lane merging zone under different penetration rates (Demand = 900 vph/lane).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/0746fa42997613444d1952bb37c1c10ffb07e2cffc8c7c7ef51d5a7c8697d4c3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/fe6edf351130d5ebcab0d6d6fff66768113a15a3cc0866bf17e91538d4890e0e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/d9d26b72e48565adfa6c7eb30c5f38802e772f22ffc7f182357a8b2451c75501.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/e7c14f23a44193c57a0386ef6aa9bcd43e37904896169e1d3650df5160dc42a4.jpg)



Fig. 15. Average speed, acceleration, delay, and throughput with four controllers in the multi-lane merging zone under different penetration rates (Demand $=$ 900 vph/lane).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/193bf595d820c5d5a176a7e857338b087c06e141586a912bb18086c5fb4a0bd8.jpg)



(a)25%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/775c95969bf6f0faad0d1aa271e3dcfaa424f5292ebedb2de09caedae26e42ca.jpg)



(c) 75%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/25ab13e4507dc62cbf464b90c6e5e8b62f9eefdd275ea0cf3921d45ff0a533ba.jpg)



(b)50%CAV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/a1af05769c0bf0c24a61d4bcfdbaf64d04ac1b8dfbb010e1f2e6772d88819e96.jpg)



(d)100% CAV



Fig. 16. Trajectories of the vehicles with four controllers in the multi-lane merging zone under different penetration rates (Demand = 1200 vph/lane).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/2191313db0de850bf38a7706f3c0708bf898913a35323f20e189fa1bef0ad24a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/d077ecc1c42cad25d4a702846e30527abff18db68b8c09f5068486ecab7c151b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/b540e9bfd2516271312f5b7e22a88ad3dd079907a8d0c4d7379b6fbd1ed2afd5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/053e90d2ea8159a2e04cd3a8b6d2007ca0169a92ac059c13f652217b8c8f9513.jpg)



Fig. 17. Average speed, acceleration, delay, and throughput with four controllers in the multi-lane merging zone under different penetration rates (Demand $=$ 1200 vph/lane).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/100cfa4f8b8223af163f49f83feef29a9581b3160eda750eaf96f4ec237bec15.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/a8c7041c10e629a04f280351eb7006adeb3646b694de238eb85a4e5bb8235c00.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/183443b20d602aa8b4eef254bf5e901c4a8800b9529ef09a29407af4cb7e3a15.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/edf56e12e7d95b2d03e36238af5deadb7f8f3b7c27ecd2ad2d9cfae3bedf189c.jpg)



(a) 900 vph/lane


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/c44349bed077075092008862df3283980b77eb8c3872415aadb9becf6e2109a9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/bfe878dbee7e5ec8ef02b65ca0d8be46e92a044e53504bb58657dc57e47306ae.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/1420055c466dc72ac8bf4435cea95b04ce79131b3917d21a61bfce7821d1f157.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/0f375bbe0df111116a6a3f7e50f0df7d0f7559d89b244570fec10896bb5a49e6.jpg)



(b) 1200 vph/lane



Fig. 18. Comparison with other three controllers.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/40d535a2a23f4ed308612d27b78c6c7034071e35f227eb6095ab13c16f9a6612.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/94a599d646c7257da8008534a9e9af85f4085c0e1748ded4d52650577147338d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/014d9a5dcab7e5e1841f0a5fcab3f5efa9332ce4945836034f22a696177b87c4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/93447b5e-26f7-4d4f-a035-29296b9a4ca9/cfca7959f1a1d1364416965e4ffddea7f86afed28103eb1176f6a1f9ef46af16.jpg)



Fig. 19. Average speed, acceleration, delay, and throughput with four HDV models under different penetration rates.


sequencing layer, a function combining traffic efficiency, safety, and driving comfort is developed to evaluate the cost of each leader–follower pair. The merging sequence problem is then reformulated as a shortest-path search problem and solved by Dijkstra algorithm to determine the globally optimal sequence, which reduces the computational burden significantly. In the motion planning layer, a consensus controller with communication delays is proposed to plan the motion for CAVs using the information of state errors between the platoon leader and all the following vehicles. The local and string stability of the consensus controller are analyzed theoretically, and the stability conditions based on these definitions are derived to provide parameter-setting criteria. 

To evaluate the performance of the proposed merging framework, several experiments are conducted to investigate the impact of CAVs on traffic flow in two-lane and multi-lane merging zones. The results show that: (1) The proposed strategy can provide a more efficient merging sequence, reducing potential conflicts and enabling smoother CAV merging. (2) The proposed consensus controller can enhance the mixed-traffic platoon’s anti-disturbance performance, robustness, stability, traffic efficiency, and driving comfort. 

Nevertheless, this study could be enhanced in the following aspects: Currently, some parameters in the merging sequencing algorithm are set empirically. In the future, the parameters could be calibrated using real-world datasets to better reflect human driving characteristics. The proposed controller only considers constant communication delays, while delays in real-world scenarios are often time-varying. Future research should also explore the performance of the proposed controller in real-world applications. 

# CRediT authorship contribution statement

Dian Jing: Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. Rongsheng Chen: Writing – review & editing, Writing – original draft, Supervision, Methodology, Investigation, Conceptualization. Enjian Yao: Writing – review & editing, Writing – original draft, Supervision, Project administration, Funding acquisition, Conceptualization. Monica Menendez: Writing – review & editing, Writing – original draft, Methodology, Investigation. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Acknowledgments

This work was supported by the National Key R&D Program of China under grant 2023YFB4302703. M. Menendez acknowledges the support of the New York University Abu Dhabi (NYUAD) Center for Interacting Urban Networks (CITIES), funded by Tamkeen under the NYUAD Research Institute Award CG001. 

# Appendix A

(1) Simulation results in the two-lane scenario: see Table 2. 

(2) Simulation results in the multi-lane scenario: see Table 3. 

(3) Simulation results based on different algorithms: see Table 4. 

(4) Simulation results based on four background HDV models: see Table 5. 


Table 2 Simulation results in the two-lane scenario under different penetration rates and traffic demands.


<table><tr><td rowspan="2">Algorithm</td><td rowspan="2">Demand (vph/lane)</td><td rowspan="2">Index</td><td colspan="5">Penetration rate</td></tr><tr><td>0%</td><td>25%</td><td>50%</td><td>75%</td><td>100%</td></tr><tr><td rowspan="8">FCFS + CF</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>18.09</td><td>18.20</td><td>18.43</td><td>19.17</td><td>20.12</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.86</td><td>0.99</td><td>1.07</td><td>1.24</td><td>1.28</td></tr><tr><td>Delay (s)</td><td>3.05</td><td>2.99</td><td>2.85</td><td>2.43</td><td>1.94</td></tr><tr><td>Throughput (vph/lane)</td><td>750</td><td>777</td><td>790</td><td>810</td><td>850</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.81</td><td>16.91</td><td>17.12</td><td>17.32</td><td>17.84</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.82</td><td>0.83</td><td>0.84</td><td>1.17</td><td>1.19</td></tr><tr><td>Delay (s)</td><td>3.90</td><td>3.83</td><td>3.68</td><td>3.55</td><td>3.21</td></tr><tr><td>Throughput (vph/lane)</td><td>1050</td><td>1065</td><td>1100</td><td>1132</td><td>1156</td></tr><tr><td rowspan="8">FCFS + CC</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>18.09</td><td>18.62</td><td>20.43</td><td>21.12</td><td>23.06</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.86</td><td>0.87</td><td>0.85</td><td>0.84</td><td>0.82</td></tr><tr><td>Delay (s)</td><td>3.05</td><td>2.74</td><td>1.79</td><td>1.47</td><td>0.67</td></tr><tr><td>Throughput (vph/lane)</td><td>750</td><td>785</td><td>794</td><td>817</td><td>852</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.81</td><td>17.53</td><td>19.11</td><td>19.90</td><td>21.51</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.82</td><td>0.83</td><td>0.80</td><td>0.78</td><td>0.86</td></tr><tr><td>Delay (s)</td><td>3.90</td><td>3.41</td><td>2.47</td><td>2.05</td><td>1.30</td></tr><tr><td>Throughput (vph/lane)</td><td>1050</td><td>1062</td><td>1067</td><td>1083</td><td>1094</td></tr><tr><td rowspan="8">MS + CF</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>18.09</td><td>18.79</td><td>19.85</td><td>21.13</td><td>23.85</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.86</td><td>1.04</td><td>1.02</td><td>1.02</td><td>0.89</td></tr><tr><td>Delay (s)</td><td>3.05</td><td>2.64</td><td>2.08</td><td>1.47</td><td>0.39</td></tr><tr><td>Throughput (vph/lane)</td><td>750</td><td>761</td><td>812</td><td>838</td><td>867</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.81</td><td>17.07</td><td>17.97</td><td>19.95</td><td>23.76</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.82</td><td>0.88</td><td>1.00</td><td>1.11</td><td>0.95</td></tr><tr><td>Delay (s)</td><td>3.90</td><td>3.72</td><td>3.13</td><td>2.02</td><td>0.42</td></tr><tr><td>Throughput (vph/lane)</td><td>1050</td><td>1078</td><td>1091</td><td>1108</td><td>1142</td></tr><tr><td rowspan="8">MS + CC</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>18.09</td><td>19.36</td><td>20.55</td><td>22.88</td><td>24.22</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.86</td><td>0.88</td><td>0.94</td><td>1.08</td><td>0.96</td></tr><tr><td>Delay (s)</td><td>3.05</td><td>2.33</td><td>1.73</td><td>0.74</td><td>0.26</td></tr><tr><td>Throughput (vph/lane)</td><td>750</td><td>781</td><td>801</td><td>831</td><td>896</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.81</td><td>17.85</td><td>19.75</td><td>21.51</td><td>24.11</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.82</td><td>0.87</td><td>0.92</td><td>0.93</td><td>1.09</td></tr><tr><td>Delay (s)</td><td>3.90</td><td>3.20</td><td>2.13</td><td>1.30</td><td>0.29</td></tr><tr><td>Throughput (vph/lane)</td><td>1050</td><td>1076</td><td>1092</td><td>1132</td><td>1167</td></tr></table>


Table 3 Simulation results in the multi-lane scenario under different penetration rates and traffic demands.


<table><tr><td rowspan="2">Algorithm</td><td rowspan="2">Demand (vph/lane)</td><td rowspan="2">Index</td><td colspan="5">Penetration rate</td></tr><tr><td>0%</td><td>25%</td><td>50%</td><td>75%</td><td>100%</td></tr><tr><td rowspan="8">FCFS + CF</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>17.31</td><td>17.55</td><td>17.90</td><td>18.38</td><td>20.07</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.15</td><td>1.09</td><td>1.07</td><td>1.08</td><td>1.09</td></tr><tr><td>Delay (s)</td><td>3.56</td><td>3.40</td><td>3.17</td><td>2.88</td><td>1.97</td></tr><tr><td>Throughput (vph/lane)</td><td>760</td><td>799</td><td>833</td><td>852</td><td>856</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.05</td><td>16.46</td><td>16.77</td><td>17.31</td><td>17.69</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.13</td><td>1.01</td><td>0.94</td><td>0.87</td><td>0.83</td></tr><tr><td>Delay (s)</td><td>4.46</td><td>4.15</td><td>3.93</td><td>3.55</td><td>3.31</td></tr><tr><td>Throughput (vph/lane)</td><td>1129</td><td>1141</td><td>1152</td><td>1176</td><td>1183</td></tr><tr><td rowspan="8">FCFS + CC</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>17.31</td><td>17.33</td><td>18.08</td><td>19.01</td><td>22.01</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.15</td><td>1.09</td><td>1.13</td><td>1.08</td><td>0.90</td></tr><tr><td>Delay (s)</td><td>3.56</td><td>3.54</td><td>3.06</td><td>2.52</td><td>1.09</td></tr><tr><td>Throughput (vph/lane)</td><td>760</td><td>813</td><td>849</td><td>862</td><td>865</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.05</td><td>16.36</td><td>16.98</td><td>17.57</td><td>18.89</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.13</td><td>1.04</td><td>0.99</td><td>0.99</td><td>1.05</td></tr><tr><td>Delay (s)</td><td>4.46</td><td>4.22</td><td>3.78</td><td>3.38</td><td>2.59</td></tr><tr><td>Throughput (vph/lane)</td><td>1129</td><td>1152</td><td>1169</td><td>1172</td><td>1184</td></tr><tr><td rowspan="8">MS + CF</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>17.31</td><td>18.68</td><td>18.73</td><td>20.62</td><td>22.20</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.15</td><td>1.03</td><td>1.15</td><td>1.05</td><td>1.18</td></tr><tr><td>Delay (s)</td><td>3.56</td><td>2.71</td><td>2.68</td><td>1.70</td><td>1.01</td></tr><tr><td>Throughput (vph/lane)</td><td>760</td><td>828</td><td>836</td><td>849</td><td>861</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.05</td><td>16.81</td><td>18.22</td><td>18.87</td><td>21.95</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.13</td><td>1.12</td><td>1.05</td><td>1.12</td><td>1.19</td></tr><tr><td>Delay (s)</td><td>4.46</td><td>3.89</td><td>2.97</td><td>2.60</td><td>1.11</td></tr><tr><td>Throughput (vph/lane)</td><td>1129</td><td>1158</td><td>1164</td><td>1172</td><td>1189</td></tr><tr><td rowspan="8">MS + CC</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>17.31</td><td>18.23</td><td>19.15</td><td>20.29</td><td>22.62</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.15</td><td>1.11</td><td>1.10</td><td>1.18</td><td>1.13</td></tr><tr><td>Delay (s)</td><td>3.56</td><td>2.97</td><td>2.44</td><td>1.86</td><td>0.84</td></tr><tr><td>Throughput (vph/lane)</td><td>760</td><td>847</td><td>859</td><td>862</td><td>876</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.05</td><td>17.27</td><td>18.59</td><td>19.05</td><td>22.50</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.13</td><td>1.11</td><td>1.10</td><td>1.21</td><td>1.16</td></tr><tr><td>Delay (s)</td><td>4.46</td><td>3.58</td><td>2.76</td><td>2.50</td><td>0.89</td></tr><tr><td>Throughput (vph/lane)</td><td>1129</td><td>1167</td><td>1181</td><td>1187</td><td>1195</td></tr></table>


Table 4 Simulation results based on different algorithms under different penetration rates and traffic demands.


<table><tr><td rowspan="2">Algorithm</td><td rowspan="2">Demand (vph/lane)</td><td rowspan="2">Index</td><td colspan="5">Penetration rate</td></tr><tr><td>0%</td><td>25%</td><td>50%</td><td>75%</td><td>100%</td></tr><tr><td rowspan="8">Zhou (2019)</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>18.09</td><td>18.20</td><td>18.43</td><td>19.17</td><td>20.12</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.86</td><td>0.99</td><td>1.07</td><td>1.24</td><td>1.28</td></tr><tr><td>Delay (s)</td><td>3.05</td><td>2.99</td><td>2.85</td><td>2.43</td><td>1.94</td></tr><tr><td>Throughput (vph/lane)</td><td>750</td><td>777</td><td>790</td><td>810</td><td>850</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.81</td><td>16.91</td><td>17.12</td><td>17.32</td><td>17.84</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.82</td><td>0.83</td><td>0.84</td><td>1.17</td><td>1.19</td></tr><tr><td>Delay (s)</td><td>3.90</td><td>3.83</td><td>3.68</td><td>3.55</td><td>3.21</td></tr><tr><td>Throughput (vph/lane)</td><td>1050</td><td>1065</td><td>1100</td><td>1132</td><td>1156</td></tr><tr><td rowspan="8">Sun (2020)</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>18.09</td><td>18.75</td><td>19.54</td><td>20.66</td><td>23.85</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.86</td><td>0.91</td><td>0.96</td><td>1.07</td><td>0.89</td></tr><tr><td>Delay (s)</td><td>3.05</td><td>2.66</td><td>2.23</td><td>1.68</td><td>0.39</td></tr><tr><td>Throughput (vph/lane)</td><td>750</td><td>800</td><td>816</td><td>832</td><td>854</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.81</td><td>17.23</td><td>17.97</td><td>20.36</td><td>21.76</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.82</td><td>0.84</td><td>0.94</td><td>1.07</td><td>0.95</td></tr><tr><td>Delay (s)</td><td>3.90</td><td>3.61</td><td>3.13</td><td>1.82</td><td>1.19</td></tr><tr><td>Throughput (vph/lane)</td><td>1050</td><td>1066</td><td>1077</td><td>1127</td><td>1149</td></tr><tr><td rowspan="8">Han (2023)</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>18.09</td><td>18.55</td><td>19.22</td><td>20.01</td><td>21.15</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.86</td><td>1.16</td><td>1.15</td><td>1.16</td><td>1.16</td></tr><tr><td>Delay (s)</td><td>3.05</td><td>2.78</td><td>2.41</td><td>2.00</td><td>1.46</td></tr><tr><td>Throughput (vph/lane)</td><td>750</td><td>782</td><td>803</td><td>828</td><td>865</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.81</td><td>16.70</td><td>18.08</td><td>19.97</td><td>20.16</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.82</td><td>1.03</td><td>1.19</td><td>1.13</td><td>1.17</td></tr><tr><td>Delay (s)</td><td>3.90</td><td>3.98</td><td>3.06</td><td>2.02</td><td>1.92</td></tr><tr><td>Throughput (vph/lane)</td><td>1050</td><td>1081</td><td>1102</td><td>1148</td><td>1172</td></tr><tr><td rowspan="8">Ours</td><td rowspan="4">900</td><td>Average Speed (m/s)</td><td>18.09</td><td>19.36</td><td>20.55</td><td>22.88</td><td>24.22</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.86</td><td>0.88</td><td>0.94</td><td>1.08</td><td>0.96</td></tr><tr><td>Delay (s)</td><td>3.05</td><td>2.33</td><td>1.73</td><td>0.74</td><td>0.26</td></tr><tr><td>Throughput (vph/lane)</td><td>750</td><td>791</td><td>801</td><td>831</td><td>876</td></tr><tr><td rowspan="4">1200</td><td>Average Speed (m/s)</td><td>16.81</td><td>17.85</td><td>19.75</td><td>21.51</td><td>24.11</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.82</td><td>0.87</td><td>0.92</td><td>0.93</td><td>1.09</td></tr><tr><td>Delay (s)</td><td>3.90</td><td>3.20</td><td>2.13</td><td>1.30</td><td>0.29</td></tr><tr><td>Throughput (vph/lane)</td><td>1050</td><td>1067</td><td>1109</td><td>1132</td><td>1199</td></tr></table>


Table 5 Simulation results based on four HDV models under different CAV penetration rates.


<table><tr><td rowspan="2">HDV model</td><td rowspan="2">Index</td><td colspan="5">Penetration rate</td></tr><tr><td>0%</td><td>25%</td><td>50%</td><td>75%</td><td>100%</td></tr><tr><td rowspan="4">IDM</td><td>Average Speed (m/s)</td><td>18.61</td><td>18.97</td><td>19.61</td><td>22.26</td><td>23.85</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.21</td><td>1.26</td><td>1.23</td><td>1.12</td><td>0.89</td></tr><tr><td>Delay (s)</td><td>2.74</td><td>2.54</td><td>2.20</td><td>0.98</td><td>0.39</td></tr><tr><td>Throughput (vph/lane)</td><td>752</td><td>766</td><td>817</td><td>843</td><td>867</td></tr><tr><td rowspan="4">2D-IDM</td><td>Average Speed (m/s)</td><td>18.09</td><td>18.79</td><td>19.85</td><td>21.13</td><td>23.85</td></tr><tr><td>Average Acceleration (m/s2)</td><td>0.86</td><td>1.04</td><td>1.02</td><td>1.02</td><td>0.89</td></tr><tr><td>Delay (s)</td><td>3.05</td><td>2.64</td><td>2.08</td><td>1.47</td><td>0.39</td></tr><tr><td>Throughput (vph/lane)</td><td>750</td><td>761</td><td>812</td><td>838</td><td>867</td></tr><tr><td rowspan="4">Krauss</td><td>Average Speed (m/s)</td><td>18.52</td><td>19.02</td><td>19.55</td><td>22.49</td><td>23.85</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.12</td><td>1.24</td><td>1.20</td><td>1.10</td><td>0.89</td></tr><tr><td>Delay (s)</td><td>2.80</td><td>2.52</td><td>2.23</td><td>0.89</td><td>0.39</td></tr><tr><td>Throughput (vph/lane)</td><td>763</td><td>778</td><td>827</td><td>852</td><td>867</td></tr><tr><td rowspan="4">GM</td><td>Average Speed (m/s)</td><td>18.74</td><td>19.19</td><td>20.73</td><td>22.78</td><td>23.85</td></tr><tr><td>Average Acceleration (m/s2)</td><td>1.16</td><td>1.23</td><td>1.20</td><td>1.08</td><td>0.89</td></tr><tr><td>Delay (s)</td><td>2.67</td><td>2.42</td><td>1.65</td><td>0.78</td><td>0.39</td></tr><tr><td>Throughput (vph/lane)</td><td>768</td><td>779</td><td>830</td><td>854</td><td>867</td></tr></table>

# References



Abbasi, M., Marquez, H.J., 2024. Observer-based event-triggered consensus control of multi-agent systems with time-varying communication delays. IEEE Trans. Autom. Sci. Eng. 1–11. http://dx.doi.org/10.1109/TASE.2023.3324526, URL https://ieeexplore.ieee.org/document/10289697/. 





Ahmed, Z., Khan, M.M., Saeed, M.A., Zhang, W., 2020. Consensus control of multi-agent systems with input and communication delay: A frequency domain perspective. ISA Trans. 101, 69–77. http://dx.doi.org/10.1016/j.isatra.2020.02.005, URL https://linkinghub.elsevier.com/retrieve/pii/S0019057820300550. 





Cao, W., Mukai, M., Kawabe, T., Nishira, H., Fujiki, N., 2015. Cooperative vehicle path generation during merging using model predictive control with real-time optimization. Control Eng. Pract. 34, 98–105. http://dx.doi.org/10.1016/j.conengprac.2014.10.005, URL http://dx.doi.org/10.1016/j.conengprac.2014.10.005. 





Publisher: Elsevier. 





Cassidy, M.J., Rudjanakanoknad, J., 2005. Increasing the capacity of an isolated merge by metering its on-ramp. Transp. Res. B 39 (10), 896–913. http: //dx.doi.org/10.1016/j.trb.2004.12.001, URL https://www.mendeley.com/catalogue/85d74acd-51aa-31c3-a794-9320b8c8072c/. Number: 10. 





Chen, R., Hu, J., Levin, M.W., Rey, D., 2020a. Stability-based analysis of autonomous intersection management with pedestrians. Transp. Res. C 114 (February), 463–483. http://dx.doi.org/10.1016/j.trc.2020.01.016, Publisher: Elsevier. 





Chen, T., Wang, M., Gong, S., Zhou, Y., Ran, B., 2021. Connected and automated vehicle distributed control for on-ramp merging scenario: A virtual rotation approach. Transp. Res. C 133, undefined–undefined. http://dx.doi.org/10.1016/j.trc.2021.103451, URL https://www.mendeley.com/catalogue/addd1868- 0425-3747-b738-66cc6703d289/. 





Chen, R., Zhang, T., Levin, M., 2020b. Effects of variable speed limit on energy consumption with autonomous vehicles on urban roads using modified cell-transmission model. J. Transp. Eng. Part A: Syst. 146 (7), http://dx.doi.org/10.1061/JTEPBS.0000379. 





Chen, J., Zhou, Y., Chung, E., 2024. An integrated approach to optimal merging sequence generation and trajectory planning of connected automated vehicles for freeway on-ramp merging sections. IEEE Trans. Intell. Transp. Syst. 25 (2), 1897–1912. http://dx.doi.org/10.1109/TITS.2023.3315650, URL https://ieeexplore.ieee.org/document/10268666/. 





de Souza, A.M., Brennand, C.A., Yokoyama, R.S., Donato, E.A., Madeira, E.R., Villas, L.A., 2017. Traffic management systems: A classification, review, challenges, and future perspectives. Int. J. Distrib. Sens. Networks 13 (4), 1550147716683612. http://dx.doi.org/10.1177/1550147716683612, Publisher: SAGE Publications. 





Di Bernardo, M., Salvi, A., Santini, S., 2015. Distributed consensus strategy for platooning of vehicles in the presence of time-varying heterogeneous communication delays. IEEE Trans. Intell. Transp. Syst. 16 (1), 102–112. http://dx.doi.org/10.1109/TITS.2014.2328439, URL https://ieeexplore.ieee.org/document/6891349. 





Dijkstra, E.W., 1959. A note on two problems in connexion with graphs. Numer. Math. 1 (1), 269–271. http://dx.doi.org/10.1007/BF01386390, URL https: //www.mendeley.com/catalogue/e1901ca9-8ee6-3af8-82da-22cf8a55b54e/. Number: 1. 





Fang, Y., Min, H., Wu, X., Wang, W., Zhao, X., Mao, G., 2022. On-ramp merging strategies of connected and automated vehicles considering communication delay. IEEE Trans. Intell. Transp. Syst. 23 (9), 15298–15312. http://dx.doi.org/10.1109/TITS.2022.3140219, URL https://ieeexplore.ieee.org/document/9678122/. 





Feng, S., Zhang, Y., Li, S.E., Cao, Z., Liu, H.X., Li, L., 2019. String stability for vehicular platoon control: Definitions and analysis methods. Annu. Rev. Control. 47, 81–97. http://dx.doi.org/10.1016/j.arcontrol.2019.03.001, URL https://linkinghub.elsevier.com/retrieve/pii/S1367578819300240. 





Ferrara, A., Sacone, S., Siri, S., 2015. Event-triggered model predictive schemes for freeway traffic control. Transp. Res. C 58, 554–567. http://dx.doi.org/10. 1016/j.trc.2015.01.020, URL https://www.mendeley.com/catalogue/3d8a8a74-af4c-3b84-b60d-c30f162689f9/. 





Gazis, D.C., Herman, R., Rothery, R.W., 1961. Nonlinear follow-the-leader models of traffic flow. Oper. Res. 9 (4), 545–567. http://dx.doi.org/10.1287/opre.9. 4.545, URL https://www.mendeley.com/catalogue/245e2e6d-c6d1-31a5-9451-3b12b813c365/. Number: 4. 





Gong, S., Du, L., 2018. Cooperative platoon control for a mixed traffic flow including human drive vehicles and connected and autonomous vehicles. Transp. Res. B 116, 25–61. http://dx.doi.org/10.1016/j.trb.2018.07.005, URL https://linkinghub.elsevier.com/retrieve/pii/S0191261517311827. 





Guler, S.I., Menendez, M., Meier, L., 2014. Using connected vehicle technology to improve the efficiency of intersections. Transp. Res. C 46, 121–131. http://dx.doi.org/10.1016/j.trc.2014.05.008, URL https://www.mendeley.com/catalogue/d8934804-8ef1-3cd0-8acd-804d9bbb3858/. 





Guzman, J.A., Morris, B.T., Nunez, F., 2023. A cyberphysical system for data-driven real-time traffic prediction on the las vegas I-15 freeway. IEEE Intell. Transp. Syst. Mag. 15 (1), 23–35. http://dx.doi.org/10.1109/MITS.2022.3211996, URL https://www.mendeley.com/catalogue/29d2003b-1278-3f42-b099- 9d1eaf0c3726/. Number: 1. 





Hale, J.K., Lunel, S.M.V., 1993. Introduction to functional differential equations. Appl. Math. Sci. (Switzerland) 99, 41–60, URL https://www.mendeley.com/ catalogue/b0a2b110-2b02-30e5-84ff-b57936e330fd/. 





Han, L., Zhang, L., Guo, W., 2023. Multilane freeway merging control via trajectory optimization in a mixed traffic environment. IET Intell. Transp. Syst. 17 (9), 1891–1907. http://dx.doi.org/10.1049/itr2.12382, URL https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/itr2.12382. 





Han, Y., Zhang, M., Guo, Y., Zhang, L., 2022. A streaming-data-driven method for freeway traffic state estimation using probe vehicle trajectory data. Phys. A 606, 128045. http://dx.doi.org/10.1016/j.physa.2022.128045, URL https://linkinghub.elsevier.com/retrieve/pii/S0378437122006537. 





Hu, Z., Huang, J., Yang, Z., Zhong, Z., 2021. Embedding robust constraint-following control in cooperative on-ramp merging. IEEE Trans. Veh. Technol. 70 (1), 133–145. http://dx.doi.org/10.1109/TVT.2021.3049866, URL https://ieeexplore.ieee.org/document/9316958/. 





Hu, X., Sun, J., 2019. Trajectory optimization of connected and autonomous vehicles at a multilane freeway merging area. Transp. Res. C 101, 111–125. http://dx.doi.org/10.1016/j.trc.2019.02.016, URL https://linkinghub.elsevier.com/retrieve/pii/S0968090X18304844. 





Jing, S., Hui, F., Zhao, X., Rios-Torres, J., Khattak, A.J., 2019. Cooperative game approach to optimal merging sequence and on-ramp merging control of connected and automated vehicles. IEEE Trans. Intell. Transp. Syst. 20 (11), 4234–4244. http://dx.doi.org/10.1109/TITS.2019.2925871, Publisher: IEEE. 





Jing, D., Yao, E., Chen, R., 2023. Moving characteristics analysis of mixed traffic flow of CAVs and HVs around accident zones. Phys. A 626, 129085. http://dx.doi.org/10.1016/j.physa.2023.129085, URL https://www.sciencedirect.com/science/article/pii/S0378437123006404. 





Jing, D., Yao, E., Chen, R., 2024. Decentralized human-like control strategy of mixed-flow multi-vehicle interactions at uncontrolled intersections: A game-theoretic approach. Transp. Res. C 167, 104835. http://dx.doi.org/10.1016/j.trc.2024.104835, URL https://linkinghub.elsevier.com/retrieve/pii/S0968090X24003565. 





Jing, D., Yao, E., Chen, R., 2025a. Driving style recognition based on a Bayesian belief-renewing method. Transp. A: Transp. Sci. 1–24. http://dx.doi.org/10. 1080/23249935.2025.2451678, URL https://www.tandfonline.com/doi/full/10.1080/23249935.2025.2451678. 





Jing, D., Yao, E., Chen, R., Menéndez, M., 2025b. Decentralized human-like ramp merging decision-making and control based on a stochastic potential game. IEEE Trans. Intell. Transp. Syst. 1–11. http://dx.doi.org/10.1109/TITS.2025.3576347. 





Krauss, S., Wagner, P., Gawron, C., 1997. Metastable states in a microscopic model of traffic flow. Phys. Rev. E - Stat. Phys. Plasmas, Fluids, Relat. Interdiscip. Top. 55 (5), 5597–5602. http://dx.doi.org/10.1103/PhysRevE.55.5597, URL https://www.mendeley.com/catalogue/e8b70b12-3abd-3ebb-b393-999c506e2a2c/. Number: 5. 





Lewis, F.L., Zhang, H., Hengster-Movric, K., Das, A., 2014. Cooperative control of multi-agent systems: Optimal and adaptive design approaches. Communications and Control Engineering, Springer London, London, http://dx.doi.org/10.1007/978-1-4471-5574-4, URL https://link.springer.com/10.1007/978-1-4471-5574- 4. 





Li, Q., Chen, Z., Li, X., 2022. A review of connected and automated vehicle platoon merging and splitting operations. IEEE Trans. Intell. Transp. Syst. 23 (12), 22790–22806. http://dx.doi.org/10.1109/TITS.2022.3193278, URL https://ieeexplore.ieee.org/document/9852980/. 





Li, W., Qiu, F., Li, L., Zhang, Y., Wang, K., 2024. Simulation of vehicle interaction behavior in merging scenarios: A deep maximum entropy-inverse reinforcement learning method combined with game theory. IEEE Trans. Intell. Veh. 9 (1), 1079–1093. http://dx.doi.org/10.1109/TIV.2023.3323138, URL https://ieeexplore.ieee.org/document/10274818/. 





Li, Z., Ren, W., Liu, X., Xie, L., 2013. Distributed consensus of linear multi-agent systems with adaptive dynamic protocols. Automatica 49 (7), 1986–1995. http://dx.doi.org/10.1016/j.automatica.2013.03.015, URL https://linkinghub.elsevier.com/retrieve/pii/S0005109813001842. 





Liu, L., Li, X., Li, Y., Li, J., Liu, Z., 2024. Reinforcement-learning-based multilane cooperative control for on-ramp merging in mixed-autonomy traffic. IEEE Internet Things J. 11 (24), 39809–39819. http://dx.doi.org/10.1109/JIOT.2024.3447039, URL https://ieeexplore.ieee.org/document/10643142/. 





Liu, H., Zhuang, W., Yin, G., Li, Z., Cao, D., 2023. Safety-critical and flexible cooperative on-ramp merging control of connected and automated vehicles in mixed traffic. IEEE Trans. Intell. Transp. Syst. 24 (3), 2920–2934. http://dx.doi.org/10.1109/TITS.2022.3224592, URL https://ieeexplore.ieee.org/document/ 10053376/. 





Lopez, P.A., Behrisch, M., Bieker-Walz, L., Erdmann, J., Flotterod, Y.P., Hilbrich, R., Lucken, L., Rummel, J., Wagner, P., Wiebner, E., 2018. Microscopic traffic simulation using SUMO. In: IEEE Conference on Intelligent Transportation Systems, Proceedings, ITSC. vol. 2018-November, http://dx.doi.org/10.1109/ITSC. 2018.8569938. 





Lu, C., Lu, H., Chen, D., Wang, H., Li, P., Gong, J., 2023. Human-like decision making for lane change based on the cognitive map and hierarchical reinforcement learning. Transp. Res. C 156, 104328. http://dx.doi.org/10.1016/j.trc.2023.104328, URL https://linkinghub.elsevier.com/retrieve/pii/S0968090X23003170. 





Lu, X.Y., Tan, H.S., Shladover, S.E., Hedrick, J.K., 2004. Automated vehicle merging maneuver implementation for AHS. Veh. Syst. Dyn. 41 (2), http: //dx.doi.org/10.1076/vesd.41.2.85.26497, URL https://www.mendeley.com/catalogue/bf6d4d03-2987-394e-ab57-72f69f91c5d6/. Number: 2. 





Meng, T., Huang, J., Hu, Z., Yang, Z., Chen, Y.-H., Yang, D., Zhong, Z., 2024. Spatial-dependent robust control strategy for on-ramp merging. IEEE Trans. Veh. Technol. 1–14. http://dx.doi.org/10.1109/TVT.2023.3326821, URL https://ieeexplore.ieee.org/document/10297589/. 





Milanés, V., Shladover, S.E., 2014. Modeling cooperative and autonomous adaptive cruise control dynamic responses using experimental data. Transp. Res. C 48, 285–300. http://dx.doi.org/10.1016/j.trc.2014.09.001, Publisher: Elsevier Ltd. 





Milanes, V., Shladover, S.E., Spring, J., Nowakowski, C., Kawazoe, H., Nakamura, M., 2014. Cooperative adaptive cruise control in real traffic situations. IEEE Trans. Intell. Transp. Syst. 15 (1), 296–305. http://dx.doi.org/10.1109/TITS.2013.2278494. 





Miller, C.E., Zemlin, R.A., Tucker, A.W., 1960. Integer programming formulation of traveling salesman problems. J. ACM 7 (4), 326–329. http://dx.doi.org/10. 1145/321043.321046, URL https://www.mendeley.com/catalogue/dd6a0a5b-04e6-3a0d-b3cd-fd4831e2a861/. Number: 4. 





Min, H., Fang, Y., Wang, R., Li, X., Xu, Z., Zhao, X., 2020. A novel on-ramp merging strategy for connected and automated vehicles based on game theory. J. Adv. Transp. 2020, 1–11. http://dx.doi.org/10.1155/2020/2529856, URL https://www.hindawi.com/journals/jat/2020/2529856/. 





Mu, C., Du, L., Zhao, X., 2021. Event triggered rolling horizon based systematical trajectory planning for merging platoons at mainline-ramp intersection. Transp. Res. C 125, 103006. http://dx.doi.org/10.1016/j.trc.2021.103006, URL https://linkinghub.elsevier.com/retrieve/pii/S0968090X21000383. 





Ntousakis, I.A., Nikolos, I.K., Papageorgiou, M., 2016. Optimal vehicle trajectory planning in the context of cooperative merging on highways. Transp. Res. C 71, 464–488. http://dx.doi.org/10.1016/j.trc.2016.08.007, URL http://dx.doi.org/10.1016/j.trc.2016.08.007. Publisher: Elsevier Ltd. 





Olfati-Saber, R., Murray, R., 2004. Consensus problems in networks of agents with switching topology and time-delays. IEEE Trans. Autom. Control 49 (9), 1520–1533. http://dx.doi.org/10.1109/TAC.2004.834113, URL http://ieeexplore.ieee.org/document/1333204/. 





Papageorgiou, M., Blosseville, J.M., Haj-Salem, H., 1990. Modelling and real-time control of traffic flow on the southern part of boulevard peripherique in Paris: Part II: Coordinated on-ramp metering. Transp. Res. Part A: Gen. 24 (5), 361–370, URL https://www.mendeley.com/catalogue/56cfeddc-6adf-3d86-bd72- 3a7b0b751f48/. Number: 5. 





Salvi, A., Santini, S., Valente, A.S., 2017. Design, analysis and performance evaluation of a third order distributed protocol for platooning in the presence of time-varying delays and switching topologies. Transp. Res. C 80, 360–383. http://dx.doi.org/10.1016/j.trc.2017.04.013, URL https://linkinghub.elsevier.com/ retrieve/pii/S0968090X17301250. 





Scholte, W.J., Zegelaar, P.W., Nijmeijer, H., 2022. A control strategy for merging a single vehicle into a platoon at highway on-ramps. Transp. Res. C 136 (April 2021), 103511. http://dx.doi.org/10.1016/j.trc.2021.103511, Publisher: Elsevier Ltd. 





Selivanov, A., Fridman, E., 2016. Event-triggered H∞ control: A switching approach. IEEE Trans. Autom. Control 61 (10), 3221–3226. http://dx.doi.org/10. 1109/TAC.2015.2508286, URL http://ieeexplore.ieee.org/document/7355303/. 





Silva, R., Nguyen, A.-T., Guerra, T.-M., Souza, F., Frezzatto, L., 2024. Switched dynamic event-triggered control for string stability of nonhomogeneous vehicle platoons with uncertainty compensation. IEEE Trans. Intell. Veh. 1–15. http://dx.doi.org/10.1109/TIV.2024.3385575, URL https://ieeexplore.ieee. org/document/10493189/. 





Su, Y., Yang, X., Shi, P., Wen, G., Xu, Z., 2024. Consensus-based vehicle platoon control under periodic event-triggered strategy. IEEE Trans. Syst. Man, Cybern.: Syst. 54 (1), 533–542. http://dx.doi.org/10.1109/TSMC.2023.3312068, URL https://ieeexplore.ieee.org/document/10255072/. 





Sun, Z., Huang, T., Zhang, P., 2020. Cooperative decision-making for mixed traffic: A ramp merging example. Transp. Res. C 120, 102764. http://dx.doi.org/ 10.1016/j.trc.2020.102764, URL https://linkinghub.elsevier.com/retrieve/pii/S0968090X20306768. 





Swaroop, D., Hedrick, J.K., Chien, C.C., Ioannou, P., 1994. A comparision of spacing and headway control laws for automatically controlled vehicles. Veh. Syst. Dyn. 23 (1), 597–625. http://dx.doi.org/10.1080/00423119408969077, URL https://www.mendeley.com/catalogue/8f311d21-40be-3971-9754- b978bcace5ac/. Number: 1. 





Tajalli, M., Niroumand, R., Hajbabaie, A., 2022. Distributed cooperative trajectory and lane changing optimization of connected automated vehicles: Freeway segments with lane drop. Transp. Res. C 143, 103761. http://dx.doi.org/10.1016/j.trc.2022.103761, URL https://linkinghub.elsevier.com/retrieve/pii/ S0968090X22001942. 





Tang, Z., Zhu, H., Zhang, X., Iryo-Asano, M., Nakamura, H., 2022. A novel hierarchical cooperative merging control model of connected and automated vehicles featuring flexible merging positions in system optimization. Transp. Res. C 138, 103650. http://dx.doi.org/10.1016/j.trc.2022.103650, URL https://linkinghub.elsevier.com/retrieve/pii/S0968090X22000936. 





Tilg, G., Yang, K., Menendez, M., 2018. Evaluating the effects of automated vehicle technology on the capacity of freeway weaving sections. Transp. Res. C 96, 3–21. http://dx.doi.org/10.1016/j.trc.2018.09.014, URL https://www.sciencedirect.com/science/article/pii/S0968090X18302730. 





Uno, A., Sakaguchi, T., Tsugawa, S., 1999. A merging control algorithm based on inter-vehicle communication. In: Proceedings 199 IEEE/IEEJ/JSAI International Conference on Intelligent Transportation Systems (Cat. No.99TH8383). pp. 783–787. http://dx.doi.org/10.1109/ITSC.1999.821160, URL https://ieeexplore. ieee.org/document/821160. 





Wang, C., Gong, S., Zhou, A., Li, T., Peeta, S., 2020. Cooperative adaptive cruise control for connected autonomous vehicles by factoring communication-related constraints. Transp. Res. C 113, 124–145. http://dx.doi.org/10.1016/j.trc.2019.04.010, URL https://linkinghub.elsevier.com/retrieve/ pii/S0968090X18317133. 





Wang, Y., Wei, C., Li, S., 2022. Qpnet: Lane-changing trajectory planning combining quadratic programming and neural network under the convex optimization framework. IET Intell. Transp. Syst. 16 (11), 1578–1599. http://dx.doi.org/10.1049/itr2.12234, URL https://www.mendeley.com/catalogue/c7fa33f5-da04- 32df-baf5-e17c7d195832/. Number: 11. 





Wang, Y., Wenjuan, E., Tang, W., Tian, D., Lu, G., Yu, G., 2013. Automated on-ramp merging control algorithm based on internet-connected vehicles. IET Intell. Transp. Syst. 7 (4), 371–379. http://dx.doi.org/10.1049/iet-its.2011.0228. 





Xiao, L., Wang, M., Schakel, W., Van Arem, B., 2018. Unravelling effects of cooperative adaptive cruise control deactivation on traffic flow characteristics at merging bottlenecks. Transp. Res. C 96, 380–397. http://dx.doi.org/10.1016/j.trc.2018.10.008, URL https://linkinghub.elsevier.com/retrieve/pii/ S0968090X1830528X. 





Xie, Y., Lu, G., Zheng, F., Cao, P., Liu, X., 2024. A hierarchical approach for integrating merging sequencing and trajectory optimization for connected and automated vehicles. IEEE Trans. Intell. Transp. Syst. 1–16. http://dx.doi.org/10.1109/TITS.2024.3350708, URL https://ieeexplore.ieee.org/document/ 10414392/. 





Xiong, B.-K., Jiang, R., 2022. Speed advice for connected vehicles at an isolated signalized intersection in a mixed traffic flow considering stochasticity of human driven vehicles. IEEE Trans. Intell. Transp. Syst. 23 (8), 11261–11272. http://dx.doi.org/10.1109/TITS.2021.3102430, URL https://ieeexplore.ieee. org/document/9511823/. 





Xiong, B.K., Jiang, R., Li, X., 2022. Managing merging from a CAV lane to a human-driven vehicle lane considering the uncertainty of human driving. Transp. Res. C 142 (January), 103775. http://dx.doi.org/10.1016/j.trc.2022.103775, Publisher: Elsevier Ltd. 





Xu, H., Feng, S., Zhang, Y., Li, L., 2019. A grouping-based cooperative driving strategy for cavs merging problems. IEEE Trans. Veh. Technol. 68 (6), 6125–6136. http://dx.doi.org/10.1109/TVT.2019.2910987, URL https://www.mendeley.com/catalogue/27c57bbf-6661-3f8d-9793-c939a096cbd5/. Number: 6. 





Xu, F., Shen, T., 2022. Decentralized optimal merging control with optimization of energy consumption for connected hybrid electric vehicles. IEEE Trans. Intell. Transp. Syst. 23 (6), 5539–5551. http://dx.doi.org/10.1109/TITS.2021.3054903, URL https://ieeexplore.ieee.org/document/9345993/. 





Xue, Y., Zhang, X., Cui, Z., Yu, B., Gao, K., 2023. A platoon-based cooperative optimal control for connected autonomous vehicles at highway on-ramps under heavy traffic. Transp. Res. C 150 (February), 104083. http://dx.doi.org/10.1016/j.trc.2023.104083, Publisher: Elsevier Ltd. 





Yang, K., Guler, S.I., Menendez, M., 2016a. Isolated intersection control for various levels of vehicle technology: Conventional, connected, and automated vehicles. Transp. Res. C 72, 109–129. http://dx.doi.org/10.1016/j.trc.2016.08.009, URL https://www.mendeley.com/catalogue/aca4eed9-4ef1-314b-8591- bb5e98910729/. 





Yang, Z., Huang, H., Yao, D., Zhang, Y., 2016b. Cooperative driving model for non-signalized intersections based on reduplicate dynamic game. IEEE Conf. Intell. Transp. Syst. Proc. ITSC 1366–1371. http://dx.doi.org/10.1109/ITSC.2016.7795735, Publisher: IEEE ISBN: 9781509018895. 





Yang, D., Liu, X., 2014. Event-triggered consensus for discrete-time linear multi-agent systems under general directed graphs. In: Proceeding of the 11th World Congress on Intelligent Control and Automation. IEEE, Shenyang, China, pp. 2693–2698. http://dx.doi.org/10.1109/WCICA.2014.7053151, URL http://ieeexplore.ieee.org/document/7053151/. 





Yi, K., 2001. Vehicle-to-vehicle distance and speed control using an electronic-vacuum booster. JSAE Rev. 22 (4), 403–412. http://dx.doi.org/10.1016/s0389- 4304(01)00123-0, URL https://www.mendeley.com/catalogue/9c4fd32f-2efe-3f20-bba7-22a897e4c71d/. Number: 4. 





Zhao, C., Chu, D., Wang, R., Lu, L., 2022a. Consensus control of highway on-ramp merging with communication delays. IEEE Trans. Veh. Technol. 71 (9), 9127–9142. http://dx.doi.org/10.1109/TVT.2022.3180757, URL https://ieeexplore.ieee.org/document/9793718/. 





Zhao, H.T., Li, H.Z., Qin, H., Zheng, L.H., 2022b. Two-lane mixed traffic flow model considering lane changing. J. Comput. Sci. 61, http://dx.doi.org/10.1016/ j.jocs.2022.101635, Publisher: Elsevier B.V.. 





Zhou, Y., Ahn, S., 2019. Robust local and string stability for a decentralized car following control strategy for connected automated vehicles. Transp. Res. B 125, 175–196. http://dx.doi.org/10.1016/j.trb.2019.05.003, URL https://linkinghub.elsevier.com/retrieve/pii/S0191261518306234. 





Zhou, Y., Ahn, S., Wang, M., Hoogendoorn, S., 2020. Stabilizing mixed vehicular platoons with connected automated vehicles: An H-infinity approach. Transp. Res. B 132, 152–170. http://dx.doi.org/10.1016/j.trb.2019.06.005, URL https://www.mendeley.com/catalogue/3b9db32b-809a-3b12-bbcf-049470756be5/. 





Zhou, Y., Cholette, M.E., Bhaskar, A., Chung, E., 2018. Constraints and recursive implementation for automated on-ramp merging. IEEE Trans. Intell. Transp. Syst. PP (9), 1–12, Publisher: IEEE. 





Zhou, A., Peeta, S., Yang, M., Wang, J., 2022. Cooperative signal-free intersection control using virtual platooning and traffic flow regulation. Transp. Res. C 138 (March), 103610. http://dx.doi.org/10.1016/j.trc.2022.103610, Publisher: Elsevier Ltd. 

