# HCOMC: A Hierarchical Cooperative On-Ramp Merging Control Framework in Mixed Traffic Environment on Two-Lane Highways

Tianyi Wang $^{1\dagger}$ , Yangyang Wang $^{2}$ , Jie Pan $^{3}$ , Junfeng Jiao $^{4}$ , Christian Claudel $^{1}$ 

Abstract—Highway on-ramp merging areas are common bottlenecks to traffic congestion and accidents. Currently, a cooperative control strategy based on connected and automated vehicles (CAVs) is a fundamental solution to this problem. While CAVs are not fully widespread, it is necessary to propose a hierarchical cooperative on-ramp merging control (HCOMC) framework for heterogeneous traffic flow on two-lane highways to address this gap. This paper extends longitudinal car-following models based on the intelligent driver model and lateral lane-changing models using the quintic polynomial curve to account for human-driven vehicles (HDVs) and CAVs, comprehensively considering human factors and cooperative adaptive cruise control. Besides, this paper proposes a HCOMC framework, consisting of a hierarchical cooperative planning model based on the modified virtual vehicle model, a discretionary lane-changing model based on game theory, and a multi-objective optimization model using the elitist nondominated sorting genetic algorithm to ensure the safe, smooth, and efficient merging process. Then, the performance of our HCOMC is analyzed under different traffic densities and CAV penetration rates through simulation. The findings underscore our HCOMC's pronounced comprehensive advantages in enhancing the safety of group vehicles, stabilizing and expediting merging process, optimizing traffic efficiency, and economizing fuel consumption compared with benchmarks. 

# I. INTRODUCTION

Highway on-ramp merging areas are common bottlenecks to traffic congestion and accidents. Notably, the speed differences between mainline vehicles and on-ramp vehicles often lead to traffic delays. With the development of automotive technology, cooperative control based on connected and automated vehicles (CAVs) has emerged as a fundamental solution to improve vehicle safety and alleviate traffic congestion [1]. However, due to current technological and economic constraints, CAVs cannot completely replace traditional human-driven vehicles (HDVs) in the near term [2]. Consequently, how to control CAVs' motion states in the cooperative planning area considering the mixed traffic flow involving HDVs and CAVs, thereby ensuring merging safety and traffic efficiency, becomes a key challenge to tackle. 

The feedback control method based on the virtual vehicle theory was initially introduced by Uno et al. [3], involving 

mapping the on-ramp merging vehicles to the main lane based on their distance from a fixed merging point and implementing speed control. Building upon this, Milanés et al.[4], [5] proposed a safe distance control method to optimize the longitudinal motion of mainline vehicles to reserve a desired gap for on-ramp vehicles to merge. Wang et al.[6], [7] mapped on-ramp vehicles to the same main lane to ensure safe car-following behaviors and constructed a feedback function including distance error and speed error to achieve cooperative control within a given on-ramp merging control region. Despite these efforts, virtual vehicle theory may not align with actual traffic dynamics without considering the speed differences between the vehicles in different lanes. Besides, while most research only analyzed traffic flow performance on single main-lane highways, neglecting the potential for lateral cooperation among vehicles on multi-lane highways and simplifying lateral behavior details make it unconvincing to derive the comprehensive advantages of CAV technologies and inevitably wastes traffic capacity. 

In addition to the virtual vehicle theory, previous studies investigated CAV-based cooperative control incorporating game theory [8], optimal control [9], and reinforcement learning[10]. Ntousakis et al. [11] established two merging sequence decision rules: first in first out (FIFO) and linear prediction of vehicle speed, which can ensure safety, but had limited adaptability to real-world traffic characteristics. Building on the FIFO model, Jing et al. [12] introduced a game mechanism to establish a decision model for merging sequences, which improved fuel economy, passenger comfort, and overall traffic efficiency by using the Pareto optimal algorithm. Moreover, Wang et al. [13] proposed an optimal cooperative control method for on-ramp merging on multi-lane highways, improving traffic stability, speed, and efficiency of traffic flow. Yu et al. [14] integrated interactive Monte Carlo tree search with deep reinforcement learning, aiming to enhance interaction rationality, efficiency and safety of CAVs. Most studies were based on pure CAV traffic scenarios without the consideration of actual complex mixed traffic environments involving HDVs. Meanwhile, only a few studies considered overall traffic attributes, i.e. safety, stability, economy, comfort and efficiency. 

Recently, several methods have been proposed for highway on-ramp merging problems in mixed traffic environment. Rios-Torres et al. [15] proposed an on-ramp merging control architecture in mixed traffic environments, where HDVs were built based on the Gips model and CAVs' trajectories were planned by an unconstrained optimal control method, which guided CAVs to arrive at a specified merging point according 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/4da0a142-e908-4aaf-aa60-d570a3215395/0524f2bdd086834657957ae94b7321710706039603c2049408d8c5d29e91e2d2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/4da0a142-e908-4aaf-aa60-d570a3215395/ec890015080a36795868269d77b02fd5b620ed752fb27761a232520f65d0a825.jpg)



Fig. 1. Framework of the proposed hierarchical cooperative on-ramp merging control (HCOMC) framework


to a pre-defined merging time. Sun et al. [16] utilized the Gipps model and the intelligent driver model (IDM) to characterize HDVs and CAVs, respectively, and then they used a rule-based approach for trajectory planning. The above research ignored the uncertainty of HDVs' behaviors, which was not in line with the actual characteristics of human drivers. To address this, Liao et al. [17], [18] designed cooperative rules based on game theory, and verified the effectiveness of the proposed merging method through software simulation and digital twin experiments. Hou et al. [19] proposed a CORMC model to ensure efficient and safe merging of the vehicles in the multi-lane merging zone under mixed traffic environments. However, most current studies assumed that HDVs' behaviors strictly conformed to a specific vehicle model, and the degree of HDV cooperation was expected to be too high. 

According to the analysis above, this paper makes three contributions to existing research: 

- This paper modifies the longitudinal car-following models and lateral lane-changing models to capture the distinct driving characteristics of mixed traffic flow on two-lane highways. 

- This paper proposes HCOMC (Figure 1), a framework making up of the hierarchical cooperative planning model, the discretionary lane-changing model, and the multi-objective optimization model to ensure the safe, smooth, and efficient merging process. 

- The simulation is conducted to verify the effectiveness of our HCOMC under different typical working conditions, considering varying traffic densities and CAV penetration rates, and comprehensive evaluation indexes are designed to prove our model's overall optimality. 

# II. PROBLEM FORMULATION

# A. Traffic Environment

This paper focuses on a two-lane highway on-ramp merging area, which consists of six key vehicles as shown in Figure 1, i.e. vehicle on ramp (VR), vehicle in lane 1 to cooperate VR (VMC), vehicle in lane 1 in front of VMC (VMF), vehicle in lane 1 in rear of VMC (VMR), vehicle in lane 2 in front of VMC (VNF), and vehicle in lane 2 in rear of VMC (VNR). 

# B. Heterogeneous Traffic Flow Model

1) Longitudinal Car-Following Model: IDM is adopted as the basic model to construct the car-following models of HDVs and CAVs. 

$$
\left\{ \begin{array}{l} a _ {n} \left(s _ {n}, v _ {n}, \Delta v _ {n}\right) = a \left(1 - \left(\frac {v _ {n}}{v _ {0}}\right) ^ {\delta} - \left(\frac {s ^ {*} \left(v _ {n} , \Delta v _ {n}\right)}{s _ {n}}\right) ^ {2}\right) \\ s ^ {*} \left(v _ {n}, \Delta v _ {n}\right) = s _ {0} + \max  \left(0, v _ {n} T _ {s} + \frac {v _ {n} \cdot \Delta v _ {n}}{2 \sqrt {a b}}\right) \end{array} \right. \tag {1}
$$

Where, $a_{n}$ is the desired acceleration; $s_n$ is the actual carfollowing distance; $\nu_{n}$ is the actual speed; $\Delta \nu_{n}$ means the actual speed difference between the subject vehicle and its leading vehicle; $a$ means the maximum desired acceleration; $\nu_{0}$ is the desired speed; $\delta$ means the acceleration index; $s_0$ represents the desired car-following distance; $s^{*}(\nu_{n},\Delta \nu_{n})$ is the static safety distance; $T_{s}$ is the safety time headway; and $b$ is the comfort deceleration. 

a) Human-Driven Vehicle: This paper introduces human driver's reaction time and estimation error to IDM. According to our previous work [20], the HDV longitudinal car-following model incorporating reaction delay time and estimation error is expressed as: 

$$
a _ {n} ^ {\mathrm {H D V}} = f \left(s _ {n} ^ {\mathrm {e s t}} \left(t - \tau_ {s _ {n}}\right), v _ {n} \left(t - \tau_ {v _ {n}}\right), \Delta v _ {n} ^ {\mathrm {e s t}} \left(t - \tau_ {\Delta v _ {n}}\right)\right) \tag {2}
$$

Where, $s_n^{\mathrm{est}}$ is the estimated car-following distance; $\Delta \nu_n^{\mathrm{est}}$ is the estimated speed difference; and $\tau_{s_n}$ , $\tau_{\nu_n}$ and $\tau_{\Delta \nu_n}$ are the reaction time with respect to the actual car-following distance, the actual speed and the actual speed difference. 

b) Connected and Automated Vehicle: This paper integrates the constant acceleration heuristic into IDM to account for CAVs. According to our previous work [20], the CAV longitudinal car-following model is expressed as: 

$$
a _ {n} ^ {\mathrm {C A V}} = (1 - c) a _ {\mathrm {I D M}} + c \left(a _ {\mathrm {C A H}} + b \tanh  \left(\frac {a _ {\mathrm {I D M}} - a _ {\mathrm {C A H}}}{b}\right)\right) \tag {3}
$$

Where, $a_{\mathrm{CAH}}$ denotes the maximum acceleration leading to no crashes; $a_{\mathrm{IDM}}$ is the acceleration of the traditional IDM; and $c$ is the cooling factor. 

2) Lateral Lane-Changing Model: Quintic polynomial curve is adopted as the basic model to construct the lane-changing trajectories of HDVs and CAVs. 

$$
y (x) = a _ {0} + a _ {1} x + a _ {2} x ^ {2} + a _ {3} x ^ {3} + a _ {4} x ^ {4} + a _ {5} x ^ {5}, \quad x \in [ x _ {0}, x _ {f} ] \tag {4}
$$

Where, $y$ is the lateral displacement; $a_{i}$ is the polynomial corresponding coefficient; $x$ is the longitudinal displacement; and $x_0$ and $x_{f}$ are longitudinal displacement at the beginning and end of lane change, respectively. 

a) Human-Driven Vehicle: This paper introduces the HDV longitudinal car-following model in Equation (2) to the lateral lane-changing model: 

$$
\left\{ \begin{array}{l} x ^ {\mathrm {H D V}} = x _ {0} + u (t - t _ {0}) + \int_ {t _ {0}} ^ {t _ {f}} \left(\int_ {t _ {0}} ^ {t _ {f}} a _ {n} ^ {\mathrm {H D V}} d t\right) d t \\ y ^ {\mathrm {H D V}} = y (x ^ {\mathrm {H D V}}) \end{array} \right. \tag {5}
$$

Where, $x^{\mathrm{HDV}}$ and $y^{\mathrm{HDV}}$ represent the longitudinal and lateral displacement of HDV, respectively; $t_0$ and $t_f$ are the beginning and end moment of lane change, respectively; and $u$ is the longitudinal speed at the beginning of lane change. 

Referring to the lane-changing time on the common high-speed condition [21], this paper sets the HDV lane-changing time $(t_f - t_0)$ as a constant, which is 4 seconds. 

b) Connected and Automated Vehicle: This paper introduces the CAV longitudinal car-following model in Equation (3) to the lateral lane-changing model: 

$$
\left\{ \begin{array}{l} x ^ {\mathrm {C A V}} = x _ {0} + u (t - t _ {0}) + \int_ {t _ {0}} ^ {t _ {f}} \left(\int_ {t _ {0}} ^ {t _ {f}} a _ {n} ^ {\mathrm {C A V}} d t\right) d t \\ y ^ {\mathrm {C A V}} = y \left(x ^ {\mathrm {C A V}}\right) \end{array} \right. \tag {6}
$$

Where, $x^{CAV}$ and $y^{CAV}$ represent the longitudinal and lateral displacement of CAV, respectively. 

The CAV lane-changing time is dynamic, which can be obtained by the HCOMC framework introduced later. 

# C. Collision Detection Model

The collision scenarios include rear-end collision and side-impact collision. To streamline the computation process, this paper leverages computer graphics methods and implements a rapid collision judgment scheme based on the principles of quick rejection tests and straddle tests. 

1) Quick Rejection Test: Assume that $P_{1}P_{2}$ and $Q_{1}Q_{2}$ are the two potential collision boundaries within the rectangular vehicle model. The purpose of the quick rejection test is to provide a preliminary assessment to exclude the case that $P_{1}P_{2}$ and $Q_{1}Q_{2}$ do not intersect, which would indicate that the two vehicles are not involved in a collision situation. If the quick rejection test is passed, it suggests that $P_{1}P_{2}$ and $Q_{1}Q_{2}$ may intersect, thereby necessitating the subsequent execution of the straddle tests to determine whether the two-line segments intersect, which may lead to collisions. 

2) Straddle Test: When $P_{1}P_{2}$ intersects with $Q_{1}Q_{2}$ , it means that the endpoints $P_{1}$ and $P_{2}$ lie on opposite sides of the line where $Q_{1}Q_{2}$ is located, while $Q_{1}$ and $Q_{2}$ lie on opposite sides of the line where $P_{1}P_{2}$ is located. This judgment can be achieved by calculating the cross product: 

$$
\left\{ \begin{array}{l} \left(P _ {1} Q _ {1} \times Q _ {1} Q _ {2}\right) \cdot \left(P _ {2} Q _ {1} \times Q _ {1} Q _ {2}\right) <   0 \\ \left(Q _ {1} P _ {1} \times P _ {1} P _ {2}\right) \cdot \left(P _ {2} P _ {1} \times P _ {1} P _ {2}\right) <   0 \end{array} \right. \tag {7}
$$

By identifying the dangerous boundaries in different collision scenarios and applying the quick rejection tests and straddle tests, collision safety can be determined. And for each feasible merging trajectory of VR, the merging sequence is then determined based on the collision safety between VR and its surrounding vehicles, i.e. VMC and VMR in Figure 1. 

# III. METHODOLOGY

# A. Hierarchical Cooperative Planning Model

When VMC is a CAV, a hierarchical cooperative planning model is established for the two-lane highway on-ramp merging area, including a first-order longitudinal and a second-order lateral cooperative planning model. 

1) First-Order Longitudinal Cooperative Planning Model: In this paper, an improved virtual vehicle model in main lane 1 based on traffic flow motion boundaries is proposed. 

$$
\left\{ \begin{array}{l} x _ {V V 1} \left(t _ {0} ^ {\prime}\right) = x _ {V M F} \left(t _ {0} ^ {\prime}\right) \\ v _ {V V 1} \left(t _ {0} ^ {\prime}\right) = v _ {V M F} \left(t _ {0} ^ {\prime}\right) \\ x _ {V V 1} \left(t _ {f} ^ {\prime}\right) = x _ {V R} \left(t _ {f} ^ {\prime}\right) \\ v _ {V V 1} \left(t _ {f} ^ {\prime}\right) = v _ {V R} \left(t _ {f} ^ {\prime}\right) \end{array} \right. \tag {8}
$$

Where, $x_{VV1}$ and $v_{VV1}$ represent the displacement and speed of the virtual vehicle of VR; and $t_0'$ and $t_f'$ are the beginning and end moment of VR planning. 

The longitudinal motion trajectory equation and the speed equation are shown as follows: 

$$
\left( \begin{array}{c c} x _ {V M F} (t _ {0} ^ {\prime}) & x _ {V R} (t _ {f} ^ {\prime}) \\ v _ {V M F} (t _ {0} ^ {\prime}) & v _ {V R} (t _ {f} ^ {\prime}) \end{array} \right) =
$$

$$
\left( \begin{array}{l l l l} b _ {1 1} & b _ {1 2} & b _ {1 3} & b _ {1 4} \\ b _ {1 2} & 2 b _ {1 3} & 3 b _ {1 4} & 0 \end{array} \right) \left( \begin{array}{c c} 1 & 1 \\ t _ {0} ^ {\prime} & t _ {f} ^ {\prime} \\ t _ {0} ^ {\prime 2} & t _ {f} ^ {\prime 2} \\ t _ {0} ^ {\prime 3} & t _ {f} ^ {\prime 3} \end{array} \right) \tag {9}
$$

The undetermined coefficients $b_{ij}$ in the state equation can 

be obtained by solving: 

$$
\left( \begin{array}{l} b _ {1 1} \\ b _ {1 2} \\ b _ {1 3} \\ b _ {1 4} \end{array} \right) = \left( \begin{array}{c c c c} 1 & t _ {0} ^ {\prime} & t _ {0} ^ {\prime 2} & t _ {0} ^ {\prime 3} \\ 1 & t _ {f} ^ {\prime} & t _ {f} ^ {\prime 2} & t _ {f} ^ {\prime 3} \\ 0 & 1 & 2 t _ {0} ^ {\prime} & 3 t _ {0} ^ {\prime 2} \\ 0 & 1 & 2 t _ {f} ^ {\prime} & 3 t _ {f} ^ {\prime 2} \end{array} \right) ^ {- 1} \left( \begin{array}{c} x _ {V M F} \left(t _ {0} ^ {\prime}\right) \\ x _ {V R} \left(t _ {f} ^ {\prime}\right) \\ v _ {V M F} \left(t _ {0} ^ {\prime}\right) \\ v _ {V R} \left(t _ {f} ^ {\prime}\right) \end{array} \right) \tag {10}
$$

After the longitudinal motion trajectory equation and the speed equation are obtained during the cooperative planning process of the virtual vehicle of VR, the acceleration variation equation of the virtual vehicle of VR can be calculated by derivation. Then, according to the heterogeneous traffic flow model, the longitudinal acceleration of the virtual vehicle of VR can be obtained. 

2) Second-Order Lateral Cooperative Planning Model: Similar to the longitudinal cooperative planning model, the motion planning equations of the virtual vehicle of VMC in main lane 2 can be obtained: 

$$
\left\{ \begin{array}{l} x _ {V V 2} \left(t _ {0} ^ {\prime \prime}\right) = x _ {V N F} \left(t _ {0} ^ {\prime \prime}\right) \\ v _ {V V 2} \left(t _ {0} ^ {\prime \prime}\right) = v _ {V N F} \left(t _ {0} ^ {\prime \prime}\right) \\ x _ {V V 2} \left(t _ {f} ^ {\prime \prime}\right) = x _ {V M C} \left(t _ {f} ^ {\prime \prime}\right) \\ v _ {V V 2} \left(t _ {f} ^ {\prime \prime}\right) = v _ {V M C} \left(t _ {f} ^ {\prime \prime}\right) \end{array} \right. \tag {11}
$$

$$
\left( \begin{array}{c c} x _ {V N F} \left(t _ {0} ^ {\prime \prime}\right) & x _ {V M C} \left(t _ {f} ^ {\prime \prime}\right) \\ v _ {V N F} \left(t _ {0} ^ {\prime \prime}\right) & v _ {V M C} \left(t _ {f} ^ {\prime \prime}\right) \end{array} \right) =
$$

$$
\left( \begin{array}{c c c c} c _ {1 1} & c _ {1 2} & c _ {1 3} & c _ {1 4} \\ c _ {1 2} & 2 c _ {1 3} & 3 c _ {1 4} & 0 \end{array} \right) \left( \begin{array}{c c} 1 & 1 \\ t _ {0} ^ {\prime \prime} & t _ {f} ^ {\prime \prime} \\ t _ {0} ^ {\prime \prime 2} & t _ {f} ^ {\prime \prime 2} \\ t _ {0} ^ {\prime \prime 3} & t _ {f} ^ {\prime \prime 3} \end{array} \right) \tag {12}
$$

$$
\left( \begin{array}{l} c _ {1 1} \\ c _ {1 2} \\ c _ {1 3} \\ c _ {1 4} \end{array} \right) = \left( \begin{array}{c c c c} 1 & t _ {0} ^ {\prime \prime} & t _ {0} ^ {\prime \prime 2} & t _ {0} ^ {\prime \prime 3} \\ 1 & t _ {f} ^ {\prime \prime} & t _ {f} ^ {\prime \prime 2} & t _ {f} ^ {\prime \prime 3} \\ 0 & 1 & 2 t _ {0} ^ {\prime \prime} & 3 t _ {0} ^ {\prime \prime 2} \\ 0 & 1 & 2 t _ {f} ^ {\prime \prime} & 3 t _ {f} ^ {\prime \prime 2} \end{array} \right) ^ {- 1} \left( \begin{array}{c} x _ {V N F} \left(t _ {0} ^ {\prime \prime}\right) \\ x _ {V M C} \left(t _ {f} ^ {\prime \prime}\right) \\ v _ {V N F} \left(t _ {0} ^ {\prime \prime}\right) \\ v _ {V M C} \left(t _ {f} ^ {\prime \prime}\right) \end{array} \right) \tag {13}
$$

Where, $x_{VV2}$ and $v_{VV2}$ represent the displacement and speed of the virtual vehicle of VMC; and $t_0''$ and $t_f''$ are the beginning and end moment of VMC planning. 

During the merging process, VMC changes lane and its leading vehicle shifts from VMF to VNF. The state differences between VMF and VNF trigger a sudden jump in the output of the IDM-based model. Therefore, a hyperbolic tangent transition function is introduced to achieve a smooth lane-changing maneuver: 

$$
\left\{ \begin{array}{l} a _ {t a r} = \Psi (\tau) a _ {n e w} + (1 - \Psi (\tau)) a _ {o r i} \\ \Psi (\tau) = \frac {1}{2} [ \tanh  (\lambda \tau - \gamma) + 1 ] \end{array} \right. \tag {14}
$$

Where, $a_{tar}$ represents the desired acceleration with transition function; $a_{ori}$ and $a_{new}$ are the desired acceleration before and after lane change, respectively; $\Psi(\tau)$ is the transition function, which satisfies $\Psi(t_0) = 0$ and $\Psi(t_f) = 1$ ; $\tau$ means the timing of lane change; and $\gamma$ and $\lambda$ are the parameters reflecting the phase and speed of the transition, respectively. 

# B. Discretionary Lane-Changing Decision Model

Discretionary lane-changing behavior is one of the most common highway operations, which seriously affects traffic efficiency and safety. Generally, the subject vehicle (SV) in the main lane has priority in making driving decisions as it encounters traffic situations earlier than its follower vehicle (FV) in the adjacent lane, and its decisions are rarely restrained by FV. Therefore, the interactions between SV and FV can be modeled as a two-player Stackelberg game with SV as the leader. For SVs with lane-changing intentions, their action set includes changing lanes and keeping car-following. FVs, according to varying driving styles, have actions including changing lane and keeping car-following (i.e., at constant speed, accelerating and decelerating). 

Initially, assuming SV as a CAV, it gathers essential information from its surrounding environment using cooperative adaptive cruise control (CACC) technologies. Subsequently, SV and FV engage in a strategic game. Applying Stackelberg game principles and Harsanyi transformation theory, the payoff functions are computed across various action combinations, aiming to identify an optimal action for both SV and FV. In scenarios where SV conducts lane changes, dynamic safety domains and optimal lane-changing trajectories are calculated to enhance collision safety and lateral stability [20]. Simultaneously, if FV is also a CAV, modified virtual vehicle models are adopted, otherwise transition models are accepted, in order to improve cooperation between CAVs, thereby enhancing traffic efficiency and ride comfort. According to the idea of mixed-strategy Nash equilibrium, SV takes the minimization of the expectation of its own payoff functions as the optimal strategy, and the combination of the strategy space and the mixed-strategy probability distribution of FV can be used to compute the expected payoff functions under different strategies (i.e. change lane and not changing lane) of SV. 

# C. Multi-Objective Optimization Model

In the cooperative planning model for highway on-ramp merging areas presented in this paper, three primary aspects require optimization: (1) the optimal merging position of VR; (2) the merging trajectory of VR; (3) the cooperation mode of VMC. Consequently, the optimal cooperative planning approach proposed in this paper can be framed as a multi-objective optimization problem. 

1) Optimization Objectives: According to the optimization problem, this paper sets three key evaluation indexes to form cost functions: safety, economy, and efficiency. 

a) Safety: The critical acceleration, which is used as the safety evaluation criterion at the end of on-ramp merging, represents the minimum acceleration required for the rear vehicle to avoid rear-end collision when the front vehicle suddenly decelerates in an emergency. Thus, the safety index $U_{safe}$ is set to the critical acceleration, satisfying: 

$$
U _ {s a f e} = a _ {c r} = \frac {v _ {r} ^ {2}}{2 \left(d _ {c r i} - D - v _ {r} T + \frac {v _ {f} ^ {2}}{2 a _ {m e r g}}\right)} \tag {15}
$$

Where, $a_{cr}$ is the critical acceleration; $\nu_{r}$ and $\nu_{f}$ are the speed of the subject vehicle and its leading vehicle, respectively; $T$ is the delay time; $a_{\text{merg}}$ is the acceleration in emergency; $D$ is the minimum distance; and $d_{cri}$ is the critical distance. 

b) Economy: The economy index $U_{fuel}$ is defined as the total fuel consumption of VMC and VR throughout the merging process. The fuel consumption rate is obtained: 

$$
\left\{ \begin{array}{l} \dot {f} e = \dot {f} _ {\text {c r u i s e}} + \dot {f} _ {\text {a c c e l}} \\ \dot {f} _ {\text {c r u i s e}} (t) = [ 1 v (t) v (t) ^ {2} v (t) ^ {3} ] Q ^ {T} \\ \dot {f} _ {\text {a c c e l}} (t) = a (t) [ 1 v (t) v (t) ^ {2} ] R ^ {T} \\ U _ {\text {f u e l}} = \int_ {t _ {0}} ^ {t _ {f}} \dot {f} e _ {V R} (t) d t + \int_ {t _ {0}} ^ {t _ {f}} \dot {f} e _ {V M C} (t) d t \end{array} \right. \tag {16}
$$

Where, $\dot{f}_{e}$ denotes the fuel consumption rate; $Q$ and $R$ are the fuel consumption parameter matrix for cruising and acceleration, respectively; and $\dot{f}_{\mathrm{cruise}}$ and $\dot{f}_{\mathrm{accel}}$ represent the fuel consumption rates during cruising and acceleration. 

c) Efficiency: For the efficiency index $U_{eff}$ in merging process, we refer to the acceleration incentive model: 

$$
U _ {e f f} = a _ {(V R) n e w} - a _ {(V R) o r i} + \eta \cdot \sum_ {i = 1} ^ {N} \left(a _ {(i) n e w} - a _ {(i) o r i}\right) \tag {17}
$$

Where $a_{(i)\text{new}}$ and $a_{(i)\text{ori}}$ are the acceleration before and after lane change, respectively, and $i$ represents different vehicles, i.e. VMC, VNR and VMR; and $\eta$ is the politeness factor, determining to which degree these vehicles influence the lane-changing decision. 

2) Optimization Algorithm: Elitist non-dominated sorting genetic algorithm (NSGA-II) can quickly find the Pareto boundary while maintaining the diversity of the population. In this paper, NSGA-II is adopted due to its high efficiency, good real-time performance, and strong versatility in optimization algorithm. The expression of the multi-objective optimization model is shown in: 

$$
\left\{ \begin{array}{l} \min  F (x) = \left(f _ {1} (x), f _ {2} (x), \dots , f _ {m} (x)\right) \\ \text {s . t .} x \in \Omega \end{array} \right. \tag {18}
$$

Where, $\Omega$ is the decision space; and $F(x)$ is the target space for the spatial domain conversion from $\Omega$ to $R^m$ . 

In the multi-objective optimization problem described above, if there is a solution $x^{*} \in \Omega$ , and meanwhile, there is no other solution to make $F(x)$ dominate $F(x^{*})$ , then $x^{*}$ can be called the Pareto optimal solution of the equation, and $F(x^{*})$ can be called the Pareto optimal vector. 

After getting the Pareto optimal solution set of NSGA-II, the unique optimal solution needs to be picked out as the final output of the optimization model. The steps to select the unique solution from the Pareto optimal solution set are as follows: (1) If $U_{safe} > 4$ , then, select the merging planning with the smallest $U_{safe}$ . (2) If $U_{safe} \leq 4$ , normalize the efficiency cost and the economy cost in the merging solutions of $U_{safe} \leq 4$ , and sum up the normalized results to select the unique optimal solution. 

$$
U = \frac {U _ {\text {e f f}} - \min \left(U _ {\text {e f f}}\right)}{\max \left(U _ {\text {e f f}}\right) - \min \left(U _ {\text {e f f}}\right)} + \frac {U _ {\text {f u e l}} - \min \left(U _ {\text {f u e l}}\right)}{\max \left(U _ {\text {f u e l}}\right) - \min \left(U _ {\text {f u e l}}\right)} \tag {19}
$$

# IV. EXPERIMENTS

The superiority of the NSGA-II model is verified by comparing it with other benchmarks, i.e. the particle swarm optimization (PSO) model [22] and the simulated annealing (SA) model [23]. Furthermore, simulations conducted across multiple traffic densities and CAV penetration rates validate the comprehensive advantages of the proposed HCOMC framework compared to the FIFO model [11] and the game theory model [17]. Specific typical working conditions are displayed in TABLE I. The simulation results of different multi-objective optimization models and on-ramp merging control models are shown in TABLE II and TABLE III. 


TABLEI PARAMETERS IN SPECIFIC SIMULATION CONDITIONS


<table><tr><td>Number</td><td>Average Time Headway in Main Lane 1 (s)</td><td>Average Time Headway in Main Lane 2 (s)</td><td>CAV Penetration Rate (/)</td></tr><tr><td>Condition 1</td><td>5</td><td>5</td><td>90%</td></tr><tr><td>Condition 2</td><td>5</td><td>7</td><td>90%</td></tr><tr><td>Condition 3</td><td>5</td><td>3</td><td>90%</td></tr><tr><td>Condition 4</td><td>5</td><td>5</td><td>60%</td></tr><tr><td>Condition 5</td><td>5</td><td>5</td><td>30%</td></tr></table>


TABLE II RESULTS OF DIFFERENT MULTI-OBJECTIVE OPTIMIZATION MODELS


<table><tr><td>Number</td><td>Model</td><td>Crit. Dist. (m)</td><td>Aver. Acc. \( \left( {\mathrm{m}/{\mathrm{s}}^{2}}\right) \)</td><td>Stab. Time (s)</td><td>LSRV \( \left( {\mathrm{m}}^{2}\right) \)</td><td>Fuel Cons. (L)</td></tr><tr><td rowspan="4">Condition 1</td><td>PSO</td><td>108.37</td><td>0.0244</td><td>19.3</td><td>3.9024</td><td>8.0433</td></tr><tr><td>SA</td><td>108.45</td><td>0.0243</td><td>19.1</td><td>3.9021</td><td>8.0424</td></tr><tr><td>NSGA-II</td><td>114.21</td><td>0.0225</td><td>16.6</td><td>3.8879</td><td>8.0375</td></tr><tr><td>PSO</td><td>150.97</td><td>0.0475</td><td>9.3</td><td>3.0009</td><td>8.3909</td></tr><tr><td rowspan="3">Condition 2</td><td>SA</td><td>150.97</td><td>0.0475</td><td>9.3</td><td>3.0009</td><td>8.3937</td></tr><tr><td>NSGA-II</td><td>149.17</td><td>0.0477</td><td>11.8</td><td>2.9996</td><td>8.3982</td></tr><tr><td>PSO</td><td>106.18</td><td>0.0517</td><td>19.5</td><td>5.7177</td><td>8.0780</td></tr><tr><td rowspan="2">Condition 3</td><td>SA</td><td>106.19</td><td>0.0517</td><td>19.7</td><td>5.7177</td><td>8.0779</td></tr><tr><td>NSGA-II</td><td>112.01</td><td>0.0494</td><td>17.2</td><td>5.7021</td><td>8.0442</td></tr></table>

# A. Safety of Group Vehicles

The most critical distance (Crit. Dist.) is chosen as the evaluation index of the safety of group vehicles. Under Condition 1 and Condition 3, where VMC implements longitudinal cooperation, NSGA-II can improve the traffic safety significantly, which increases by $5.39\%$ $5.31\%$ and $5.49\%$ $5.48\%$ compared with PSO and SA, respectively. When VMC implements lateral cooperation under Condition 2, although NSGA-II performs inferior to the other two models, the difference is only about $1\%$ . It can be seen in TABLE III that our HCOMC improves the safety of group vehicles in all conditions. Compared to the FIFO 


TABLE III RESULTS OF DIFFERENT ON-RAMP MERGING CONTROL MODELS


<table><tr><td>Number</td><td>Model</td><td>Crit. Dist. (m)</td><td>Aver. Acc. (m/s2)</td><td>Stab. Time (s)</td><td>LSRV (m2)</td><td>Fuel Cons. (L)</td></tr><tr><td rowspan="3">Condition 1</td><td>FIFO</td><td>104.67</td><td>0.0267</td><td>22.5</td><td>3.9122</td><td>8.0660</td></tr><tr><td>Game</td><td>108.64</td><td>0.0242</td><td>19.0</td><td>3.9016</td><td>8.0409</td></tr><tr><td>HCOMC</td><td>114.21</td><td>0.0225</td><td>16.6</td><td>3.8879</td><td>8.0375</td></tr><tr><td rowspan="3">Condition 2</td><td>FIFO</td><td>85.47</td><td>0.0442</td><td>26.1</td><td>3.1131</td><td>8.1516</td></tr><tr><td>Game</td><td>80.33</td><td>0.0513</td><td>25.4</td><td>3.1444</td><td>8.0598</td></tr><tr><td>HCOMC</td><td>149.17</td><td>0.0477</td><td>11.8</td><td>2.9996</td><td>8.3982</td></tr><tr><td rowspan="3">Condition 3</td><td>FIFO</td><td>102.30</td><td>0.0545</td><td>22.9</td><td>5.7286</td><td>8.1057</td></tr><tr><td>Game</td><td>106.53</td><td>0.0515</td><td>19.2</td><td>5.7168</td><td>8.0744</td></tr><tr><td>HCOMC</td><td>112.01</td><td>0.0494</td><td>17.2</td><td>5.7021</td><td>8.0442</td></tr><tr><td rowspan="3">Condition 4</td><td>FIFO</td><td>104.67</td><td>0.0267</td><td>22.5</td><td>3.9125</td><td>8.0510</td></tr><tr><td>Game</td><td>108.64</td><td>0.0242</td><td>19.0</td><td>3.9019</td><td>8.0220</td></tr><tr><td>HCOMC</td><td>114.21</td><td>0.0225</td><td>16.6</td><td>3.8882</td><td>8.0148</td></tr><tr><td rowspan="3">Condition 5</td><td>FIFO</td><td>125.62</td><td>0.0427</td><td>20.4</td><td>3.9506</td><td>8.0093</td></tr><tr><td>Game</td><td>115.68</td><td>0.0482</td><td>23.1</td><td>3.9727</td><td>7.9763</td></tr><tr><td>HCOMC</td><td>129.99</td><td>0.0360</td><td>18.8</td><td>3.9494</td><td>7.8927</td></tr></table>

model and the game theory model, the proposed HCOMC improves the critical distance by $9.11\%$ and $5.13\%$ , respectively. What is noteworthy is that under Condition 2, where VMC implements longitudinal cooperation both in FIFO and game theory, while implementing lateral cooperation in our HCOMC, the maximum increase rate can reach over $46\%$ . 

# B. Stability and Rapidity of Merging

In this paper, the average acceleration (Aver. Acc.) of the six key vehicles and the time required to stabilize after merging (Stab. Time) are selected as the stability and rapidity evaluation indexes. Almost under all the working conditions, the proposed HCOMC improves both of the evaluation indexes, which indicates the great improvements in rapidity and stability of merging. Under Condition 2, compared with FIFO and game theory, the proposed HCOMC model can shorten the time to stabilize after merging by $54.79\%$ and $53.53\%$ , respectively, benefiting from the lateral cooperation mode of VMC at the expense of stability due to additional lane-changing behaviors. The results under Condition 1, Condition 4, and Condition 5 indicate that the performance of our HCOMC maintains superiority and stable under different CAV penetration rates. 

# C. Efficiency of Traffic Flow

This paper uses low-speed region volume (LSRV) as the evaluation index of traffic efficiency. The low-speed region volume is computed by integrating the product of velocity, longitudinal displacement, and time. Under Condition 1 and Condition 3, where VMC implements longitudinal cooperation, NSGA-II reduces the low-speed region volume by 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/4da0a142-e908-4aaf-aa60-d570a3215395/85ad982d701948ff963ebfc3e6d7f1542adc368b88d9a88510926ad47c111196.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/4da0a142-e908-4aaf-aa60-d570a3215395/57dea308451eb4280c55ef807497ca4388d13c3b08851e784e98528f4efecb06.jpg)



(1) FIFO


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/4da0a142-e908-4aaf-aa60-d570a3215395/4e4d4cde7135e3ffceed409cd1d2f938641d5441e0a8cf64042847d07b978913.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/4da0a142-e908-4aaf-aa60-d570a3215395/e504181e3d44cdf7eebd33a7d6b0992ac228bd1a615cfce933304d6cd7508425.jpg)



(2) Game Theory


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/4da0a142-e908-4aaf-aa60-d570a3215395/603c61afcaed7e23eaf904e6977c02df89a3d43d53f89d5c22c2cf4732581ee5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/4da0a142-e908-4aaf-aa60-d570a3215395/fac69c8881a5d232747b7030c699dc837135daf590b5b71a7510bc93a6b57733.jpg)



(3) HCOMC



Fig. 2. Volume contour map response of two lanes under Condition 2


$0.37\%$ $0.36\%$ and both $0.27\%$ compared with PSO and SA, respectively. In contrast, VMC implements lateral cooperation under Condition 2, where NSGA-II also performs the best in this case. The volume contour maps in Figure 2 shows that our HCOMC has smoother speed fluctuations and a smaller impact time frame in the mode of lateral cooperation (Condition 2), indicating that our HCOMC outperforms other models in traffic efficiency. Simulation results also showcase that the decreases in the number of CAVs lead to higher total low-speed region volumes, which indicates the significant role of CAVs in improving the efficiency of traffic flow. 

# D. Fuel Consumption Economy

In this paper, the total fuel consumption (Fuel Cons.) of the traffic flow is utilized as the evaluation index for fuel consumption economy. Under Condition 1 and Condition 3, NSGA-II outperforms the other two optimization algorithms, which indicates the advantages of NSGA-II in improving the overall fuel consumption performance of traffic flow. Under Condition 2, NSGA-II performs inferior to the other two models, but the difference is only about $1\%$ . Our HCOMC reduces the total fuel consumption by $0.35\%$ and $0.04\%$ compared with the FIFO model and the game theory model under Condition 1. However, under Condition 2, the fuel consumption of the HCOMC is larger than that of the FIFO 

model and the game theory model, which is attributed to the additional lateral cooperation maneuvers of VMC. 

# E. Discussion

Results show that NSGA-II consistently performs best under almost all the working conditions, particularly in longitudinal cooperation mode. This demonstrates that the NSGA-II model is more effective than other optimization algorithms in improving overall performance under varying traffic conditions. Under some isolated conditions, the stability index of merging of the HCOMC may be worse than that of the FIFO model. However, it consistently ensures safe car-following and lane-changing, and improves traffic efficiency, with its stability index only marginally lower than that of the FIFO model. Furthermore, the HCOMC significantly outperforms both the other two on-ramp merging control models in terms of rapidity of merging and fuel consumption economy under most traffic conditions. Considering its comprehensive performance across various metrics under different traffic densities and CAV penetration rates, our HCOMC enhances overall traffic flow performance in the two-lane highway on-ramp merging areas compared to the other two models. 

# V. CONCLUSIONS

This paper proposes an innovative HCOMC framework, specifically designed for heterogeneous traffic flow involving CAVs and HDVs on two-lane highways. The HCOMC model consists of three key components: a longitudinal-lateral cooperative planning model, a discretionary lane-changing decision model and a multi-objective optimization model. Finally, comprehensive simulations are conducted to validate the effectiveness of the HCOMC under typical working conditions, i.e. varying traffic densities and CAV penetration rates. The results show that the HCMOC improves the traffic flow efficiency, ensures good fuel consumption economy, and improves the rapidity and stability of merging while maintaining safety standards compared with the benchmarks. These findings highlight the substantial impact of CAV technologies on advanced mixed traffic flow and lay foundation for developing cooperative control strategies tailored to heterogeneous traffic flow to ease traffic congestion and reduce accident risk in bottlenecks. 

# REFERENCES



[1] Y. Wang and T. Wang, "Research on dual clutch intelligent vehicle infrastructure cooperative control based on system delay prediction of two lane highway on ramp merging area," Automotive Innovation, vol. 7, pp. 588-601, 2024. 





[2] T. Wang, Q. Guo, C. He, H. Li, Y. Xu, Y. Wang, and J. Jiao, "Impact of connected and automated vehicles on longitudinal and lateral performance of heterogeneous traffic flow in shared autonomy on two-lane highways," SAE Technical Paper, no. 2025-01-8098, 2025. 





[3] A. Uno, T. Sakaguchi, and S. Tsugawa, "A merging control algorithm based on inter-vehicle communication," in Proceedings 199 IEEE/IEEJ/JSAI International Conference on Intelligent Transportation Systems (Cat. No. 99TH8383). IEEE, 1999, pp. 783-787. 





[4] V. Milanés, J. Godoy, J. Villagrá, and J. Pérez, "Automated on-ramp merging system for congested traffic situations," IEEE Transactions on Intelligent Transportation Systems, vol. 12, no. 2, pp. 500-508, 2010. 





[5] V. Milanés, J. Villagrá, J. Pérez, and C. González, "Low-speed longitudinal controllers for mass-produced cars: A comparative study," IEEE Transactions on Industrial Electronics, vol. 59, no. 1, pp. 620-628, 2011. 





[6] Z. Wang, G. Wu, and M. Barth, "Distributed consensus-based cooperative highway on-ramp merging using v2x communications," SAE Technical Paper, no. 2018-01-1177, 2018. 





[7] Z. Wang, G. Wu, K. Boriboonsomsin, M. J. Barth, K. Han, B. Kim, and P. Tiwari, "Cooperative ramp merging system: Agent-based modeling and simulation using game engine," SAE International Journal of Connected and Automated Vehicles, vol. 2, no. 2, 2019. 





[8] L. Yang, J. Zhan, W.-L. Shang, S. Fang, G. Wu, X. Zhao, and M. Deveci, "Multi-lane coordinated control strategy of connected and automated vehicles for on-ramp merging area based on cooperative game," IEEE Transactions on Intelligent Transportation Systems, vol. 24, no. 11, pp. 13448-13461, 2023. 





[9] X. Hu and J. Sun, "Trajectory optimization of connected and autonomous vehicles at a multilane freeway merging area," Transportation Research Part C: Emerging Technologies, vol. 101, pp. 111-125, 2019. 





[10] M. Zhang, Z. Fang, T. Wang, S. Lu, X. Wang, and T. Shi, "Ccma: A framework for cascading cooperative multi-agent in autonomous driving merging using large language models," Expert Systems with Applications, vol. 282, p. 127717, 2025. 





[11] I. A. Ntousakis, I. K. Nikolos, and M. Papageorgiou, "Optimal vehicle trajectory planning in the context of cooperative merging on highways," Transportation research part C: emerging technologies, vol. 71, pp. 464-488, 2016. 





[12] S. Jing, F. Hui, X. Zhao, J. Rios-Torres, and A. J. Khattak, "Integrated longitudinal and lateral hierarchical control of cooperative merging of connected and automated vehicles at on-ramps," IEEE Transactions on Intelligent Transportation Systems, vol. 23, no. 12, pp. 24248-24262, 2022. 





[13] Y. Wang, X. Cao, G. Ren, Y. Zou, and H. Deng, "Research on cooperative control for on-ramp merging with multiple lanes in connected and automated environments," Transportation research record, vol. 2678, no. 6, pp. 598-618, 2024. 





[14] L. Yu, T. Wang, J. Jiao, F. Shan, H. Chu, and B. Gao, "Bida: A bilevel interaction decision-making algorithm for autonomous vehicles in dynamic traffic scenarios," arXiv preprint arXiv:2506.16546, 2025. 





[15] J. Rios-Torres and A. A. Malikopoulos, "Impact of partial penetrations of connected and automated vehicles on fuel consumption and traffic flow," IEEE Transactions on Intelligent Vehicles, vol. 3, no. 4, pp. 453-462, 2018. 





[16] Z. Sun, T. Huang, and P. Zhang, "Cooperative decision-making for mixed traffic: A ramp merging example," Transportation research part C: emerging technologies, vol. 120, p. 102764, 2020. 





[17] X. Liao, X. Zhao, Z. Wang, K. Han, P. Tiwari, M. J. Barth, and G. Wu, "Game theory-based ramp merging for mixed traffic with unity-sumo co-simulation," IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 52, no. 9, pp. 5746-5757, 2021. 





[18] X. Liao, Z. Wang, X. Zhao, K. Han, P. Tiwari, M. J. Barth, and G. Wu, "Cooperative ramp merging design and field implementation: A digital twin approach based on vehicle-to-cloud communication," IEEE Transactions on Intelligent Transportation Systems, vol. 23, no. 5, pp. 4490-4500, 2021. 





[19] K. Hou, F. Zheng, X. Liu, and G. Guo, "Cooperative on-ramp merging control model for mixed traffic on multi-lane freeways," IEEE Transactions on Intelligent Transportation Systems, vol. 24, no. 10, pp. 10774-10790, 2023. 





[20] T. Wang, C. He, H. Li, Y. Li, Y. Xu, Y. Wang, and J. Jiao, "Hlchg: A hierarchical lane-changing gaming decision model for heterogeneous traffic flow on two-lane highways," Transportation Research Record, p. 03611981251342246, 2025. 





[21] R. Jiang, Q. Wu, and Z. Zhu, "Full velocity difference model for a car-following theory," Physical Review E, vol. 64, no. 1, p. 017101, 2001. 





[22] D. Wang, D. Tan, and L. Liu, "Particle swarm optimization algorithm: an overview," Soft computing, vol. 22, no. 2, pp. 387-408, 2018. 





[23] F. Y. Vincent, H. Susanto, P. Jodiawan, T.-W. Ho, S.-W. Lin, and Y.-T. Huang, "A simulated annealing algorithm for the vehicle routing problem with parcel lockers," IEEE Access, vol. 10, pp. 20764-20782, 2022. 

