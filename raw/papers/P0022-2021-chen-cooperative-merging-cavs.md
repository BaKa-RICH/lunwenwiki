# A Hierarchical Model-Based Optimization Control Approach for Cooperative Merging by Connected Automated Vehicles

Na Chen , Bart van Arem , Senior Member, IEEE, Tom Alkim, and Meng Wang , Member, IEEE 

Abstract— Gap selection and dynamic speed profiles of interacting vehicles at on-ramps affect the safety and efficiency of highway merging sections. This paper puts forward a hierarchical control approach for Connected Automated Vehicles (CAVs) to achieve efficient and safe merging operations. A tactical layer controller employs a second-order car-following model with a cooperative merging mode to represent a cooperative merging process and generates an optimal vehicle merging sequence and time instants when on-ramp CAVs start to adapt their speeds and positions to prepare merging into the target gaps respectively. An operational layer controller is designed based on Model Predictive Control (MPC). It uses a third-order vehicle dynamics model and optimizes desired accelerations for CAVs and the time instants when the on-ramp CAVs initiate the lane-changing executions respectively. Both the tactical layer controller and operational layer controller derive their control commands by minimizing an objective function for different time horizons. The objective function penalizes deviations of CAVs’ inter-vehicle gaps to their desired values, relative speeds to their direct predecessors, and actual or desired accelerations, subject to constraints on velocities, actual or desired accelerations, and inter-vehicle gaps. The performance of the proposed hierarchical control framework and a benchmark on-ramp merging method using a first-in-firstout rule to determine the merging sequence is demonstrated under 135 scenarios with different initial conditions, desired time gap settings, and numbers of on-ramp vehicles. The experimental results show the superiority of the hierarchical control approach. 

Index Terms— Connected automated vehicles (CAVs), on-ramp merging, merging sequence, optimization control. 

# NOTATION

$\mathbf { Z ^ { t } }$ State variable of the tactical layer controller 

$\mathbf { U ^ { t } }$ Control variable of the tactical layer controller 

$T$ Prediction time horizon of the tactical layer controller 

$\Delta \hat { t }$ Time step used in the tactical layer controller 

$\mathbf { Z ^ { 0 } }$ State variable of the operational layer controller 

$\mathbf { U ^ { \mathbf { 0 } } }$ Control variable of the operational layer controller 

$T _ { p }$ Prediction time horizon of the operational layer controller 

Manuscript received May 24, 2019; revised January 10, 2020 and June 2, 2020; accepted June 26, 2020. Date of publication July 21, 2020; date of current version November 29, 2021. This work was supported in part by the Rijkswaterstaat and in part by the China Scholarship Council. The Associate Editor for this article was N. Bekiaris-Liberis. (Corresponding author: Na Chen.) 

Na Chen, Bart van Arem, and Meng Wang are with the Department of Transport and Planning, Delft University of Technology, 2628 CN Delft, The Netherlands (e-mail: na.chen@tudelft.nl; b.vanarem@tudelft.nl; m.wang@tudelft.nl). 

Tom Alkim is with the Rijkswaterstaat, Ministry of Infrastructure and Water Management, 2515 XP The Hague, The Netherlands (e-mail: tom.alkim@ec.europa.eu). 

Digital Object Identifier 10.1109/TITS.2020.3007647 

<table><tr><td>Δt</td><td>Time step used in the operational layer controller</td></tr><tr><td>x</td><td>Vehicle position</td></tr><tr><td>v</td><td>Vehicle speed</td></tr><tr><td>a</td><td>Actual acceleration</td></tr><tr><td>i,N</td><td>Index</td></tr><tr><td>t0</td><td>Updated starting time instant of the operational layer controller</td></tr><tr><td>r</td><td>Initial on-ramp vehicle index</td></tr><tr><td>f_r</td><td>Merging sequence</td></tr><tr><td>t^p</td><td>Speed-adaptation time instant for the on-ramp vehicle</td></tr><tr><td>k</td><td>Vehicle order of the first on-ramp vehicle after merging</td></tr><tr><td>D_i, c_i</td><td>Parameters</td></tr><tr><td>s</td><td>Inter-vehicle distance or spacing, or abbreviation for second</td></tr><tr><td>Δs</td><td>Gap error</td></tr><tr><td>l_veh</td><td>Vehicle length</td></tr><tr><td>td</td><td>Desired time gap</td></tr><tr><td>s0</td><td>Minimum inter-vehicle distance at standstill</td></tr><tr><td>Δv</td><td>Relative speed</td></tr><tr><td>J, i, ψ</td><td>Objective function</td></tr><tr><td>a_com</td><td>Maximum comfortable acceleration</td></tr><tr><td>d_com</td><td>Minimum comfortable deceleration</td></tr><tr><td>a_max</td><td>Maximum acceleration</td></tr><tr><td>d_max</td><td>Minimum deceleration</td></tr><tr><td>vlimits</td><td>Speed limits</td></tr><tr><td>y_r</td><td>Lateral position of the on-ramp vehicle r</td></tr><tr><td>ξ_r</td><td>Lane-changing acceptability</td></tr><tr><td>t^l</td><td>Lane-changing initiation time instant</td></tr><tr><td>u</td><td>Desired acceleration</td></tr><tr><td>M</td><td>Total vehicle number in f_r</td></tr><tr><td>tg</td><td>Acceptable time gap for lane changing</td></tr><tr><td>xs</td><td>Starting position of the acceleration lane</td></tr><tr><td>xe</td><td>Ending position of the acceleration lane</td></tr><tr><td>λi</td><td>Co-state variable</td></tr><tr><td>L</td><td>Control zone length</td></tr></table>

# I. INTRODUCTION

HIGHWAY traffic congestion and traffic incidents aresocietal problems, and they bring great economic loss to the public. On-ramps on highways are typical bottlenecks where improper on-ramp merging behavior brings loss to traffic efficiency and safety easily [1]. The loss to a great 

extent is caused by merging sequences and motions of involved vehicles during merging processes [2]–[7]. 

With the development of control and telematic technologies, Connected Automated Vehicles (CAVs) potentially improve highway operations near on-ramps [8]–[14]. In high driving automation CAVs exchange their current and/or anticipated information with each other via Vehicle-to-Vehicle (V2V) communication and/or with the road infrastructure via Vehicleto-Infrastructure (V2I) communication to enhance situation awareness and/or maneuver in a coordinated way [8], [13], [15], [16]. With cooperative merging strategies, using shared vehicular information, CAVs have the potential to follow selected or established merging sequences, and to accomplish or to facilitate difficult merging tasks automatically by behaving cooperatively. Different methods such as (cooperative) adaptive cruise control, optimal control, fuzzy control, and sliding mode control are used for trajectory planning of the merging process in extensive literature [1], [10], [13]. 

By contrast, fewer methods are researched to establish merging sequences for improving traffic operations. To improve traffic efficiency, mainline vehicles are allowed to yield for merging of on-ramp vehicles [11], [13], [17]. The cooperative merging strategies generally utilize proactive merging sequences, given before on-ramp vehicles reaching at merging points [13], [17], [18]. 

This paper aims to design a cooperative merging strategy for CAVs to achieve safe and efficient traffic under $100 \%$ CAV market penetration. The cooperative merging strategy is based on a hierarchical control approach, where a tactical controller and an operational layer controller work together to select gaps for the merging of on-ramp CAVs, to regulate CAVs’ desired accelerations, and to determine time instants when the on-ramp CAVs initiate lane-changing executions respectively. The superiority of the proposed cooperative hierarchical control approach over a benchmark control approach, using a first-in-first-out method to determine merging sequences and the same operational layer controller to regulate vehicular motions, is verified numerically at a microscopic level under 135 scenarios with different initial conditions and desired time gap settings. 

The remainder of the paper is organized as follows. In Section II the relevant literature on establishing merging sequences is critically reviewed and summarized. The following section presents the designed cooperative merging control architecture. Section IV elaborates on the design of the tactical controller and operational layer controller. After that, we introduce simulation experiments design and performance indicators in Section V, followed by an analysis and a discussion of simulation results in Section VI. Finally, Section VII concludes the study. 

# II. LITERATURE REVIEW ON ESTABLISHING MERGING SEQUENCES

Existing cooperative merging strategies have two types of means to establish merging sequences. One means is based on explicit rules, called ‘rule-based methods’ for simplicity. Another means is based on a global or local performance 

indicator relating to traffic operations, called ‘optimal methods’ for simplicity. 

The rule-based methods include virtual mapping, the firstin-first-out method, heuristic methods, and others. The virtual mapping method selects a fixed merging point and establishes merging sequences by comparing initial path lengths of vehicles to the selected merging point [1], [13], [17]. A vehicle closer to the merging point passes through the merging point earlier. When a control zone is defined, merging sequences can be established by comparing the enter times of vehicles into the control zone, which is called the first-in-first-out method [11]. A vehicle that enters into the control zone earlier leaves earlier. An upper layer controller of a two-layer local merging control method utilizes a heuristic method to establish merging sequences [19], [20]. The upper layer controller prescribes a constant merging velocity. It makes vehicles entering into the control zone to adjust their speeds first to the merging velocity based on constant accelerations and then continues to move; thus, the expected leaving times of vehicles can be calculated. Sorting the expected leaving times of vehicles, it establishes a merging sequence. others includes all other methods using plausibly reasonable rules to establish merging sequences, such as selecting one mainline CAV to yield for merging of an on-ramp vehicle [2] or appointing virtual slots for CAVs [2], [21], [22]. In [2], the first downstream mainline CAV, which is estimated within a safety zone when an on-ramp human-driven vehicle arrives at a merging point, yields for merging of an on-ramp human-driven vehicle. Because human-driven vehicles’ arriving times and speeds at the start of an acceleration lane are not perfectly predicted, sometimes mainline CAVs generate unnecessarily large gap for merging of on-ramp human-driven vehicles. Since yielding of human-driven vehicles for merging of on-ramp vehicles cannot be controlled, mainline CAVs can act as leaders to collect gaps for merging of on-ramp vehicles by using the fundamental diagram in traffic flow theory [21]. 

Optimal methods evaluate all or some selected merging sequences by a performance indicator relating to traffic operations and establish the optimal one for merging of on-ramp vehicles. [23] uses optimal platooning control to generate accelerations of vehicles and selects a merging sequence that brings the minimal value of an objective function during on-ramp merging process. On-ramp merging processes with different merging sequences are evaluated under optimal platooning control before an optimal merging sequence is chosen. It is easy to understand the optimality of the established optimal merging sequence. However, the process to establish the optimal merging sequence may be time-consuming when many vehicles are involved. An optimal merging sequence can also be established during a merging process [24]. Reference [24] utilizes a trajectory equation with uncertain parameters as potential merging paths of an on-ramp vehicle and designs on-ramp merging control based on MPC, optimizing uncertain parameters in the potential merging paths together with the vehicles’ longitudinal accelerations. Reference [18] calculates safe vehicular speeds by considering several vehicles ahead within a specified distance to represent CAVs’ movements. Thus the nature arriving times of CAVs, where no merging 

exists, at a merging point can be estimated. Reference [18] compares those estimated arriving times to obtain reasonable merging sequences, within which the merging sequence that incurs minimal merging delay is selected as an optimal one. Reference [25] proposes a bi-level programming model for autonomous intersection control. An upper-level controller estimates the earliest and latest arrival time of CAVs into an intersection and establishes an optimal passing sequence of vehicles by minimizing the sum of arriving times of CAVs on two different roads with safe minimal time intervals. A lower-level controller uses Intelligent Driver Model (IDM) to update vehicles’ speeds and locations, follows the allocated arrival time of CAVs into the intersection and maximizes entering speeds of CAVs into the intersection. Reference [26] uses a car-following model to update vehicles’ accelerations, assumes vehicles’ accelerations to be constant in divided time intervals, and gives optimal merging sequences through a genetic approach. Reference [27] proposes a model-based bilevel control strategy for splitting a platoon of trucks near network merges. A supervisory tactical strategy uses a first-order Newell car-following model with bounded acceleration and deceleration to describe the follower-the-leader behavior of vehicles, projects vehicles’ position-time with the maximum flow speed along a shock wave on two lanes to a shock wave starting from a leader’s position to achieve natural ordered sequence, and establishes an optimal ordering sequence that makes the projections in a time-ordered set. The existing optimal methods establishing merging sequences tend to arrange passing times of vehicles over a merging point or repeat future detailed merging process exhaustively with different merging sequences to find an optimal one. 

Both the rule-based methods and the optimal methods establish merging sequences by using numerical criteria. The numerical criteria employed by the rule-based methods are based on values related to vehicles’ initial or estimated future positions and/or speeds, without considering many possible merging sequences. To this end, compared with other possible merging sequences, merging sequences selected by utilizing the rule-based methods do not have obvious advantages in bringing benefits to traffic operations. Requiring accurate vehicle dynamics models, utilizing detailed control processes to regulate vehicular trajectories, and adopting the same time steps used for trajectory planning, the optimal methods repeat future detailed merging process exhaustively with different merging sequences to have optimal ones. Compared with the rule-based methods, the optimal methods evaluate all or some merging sequences and adopt selected global or local performance indicators relating to traffic operations to establish optimal ones. The optimal methods to a great extent ensure an improvement in traffic operations. However, the existing optimal methods rely on accurate vehicle dynamics models and detailed trajectory planning process, their flexibility is limited. They are not suitable when mismatches exist. Besides, with the existing optimal methods, on-ramp CAVs start to adapt their speeds and positions to prepare merging into selected gaps respectively when they enter into on-ramp lanes. That neglects the possibilities of allowing on-ramp vehicles to drive with their desired speeds for certain time periods respectively 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/098d462fc164dd3115c48d1c7d054fbc00305bbaa81d2202dad12fbe04e18b83.jpg)



Fig. 1. A typical on-ramp merging scenario.


to reduce their speed deviations to mainline vehicles’ or adjust their position to have large inter-vehicle distances. Chances to improve traffic operations may be ignored to some extent. This paper proposes a novel hierarchical model-based optimization control approach to plan vehicular trajectories for CAVs. It can establish optimal merging sequences when mismatches exist and allow on-ramp vehicles to travel with their desired speeds for certain time periods respectively. 

# III. COOPERATIVE MERGING CONTROL ARCHITECTURE

Fig. 1 shows a typical on-ramp merging scenario considered in this paper. All vehicles are CAVs with SAE Level 4 Automation, and they are assumed to be automatically controlled by the operational layer controller. On-ramp CAVs need to merge into mainstream traffic before reaching the end of an acceleration lane. Located near the start of the acceleration lane, a roadside centralized controller, which acts as the tactical layer controller, regularly collects vehicular information provided by in-vehicle estimators through V2I communication. The operational layer controller is located in CAVs, regulating CAVs’ motions. 

A hierarchical control architecture is designed to achieve safe and efficient merging of the on-ramp CAVs, as shown in Fig. 2. The tactical layer controller and operational layer controller assume that the estimator equipped on each CAV gives accurate vehicular information detected by sensors, including position, speed, and actual acceleration of that CAV. With $\mathbf { Z ^ { t } } ( 0 )$ , the value of a state variable defined by the tactical layer controller at time $_ \mathrm { ~ 0 ~ } s$ , the tactical layer controller computes optimal future vehicle merging sequences (or equivalently selects gaps for the on-ramp CAVs to merge respectively) and speed-adaptation time instants for on-ramp vehicles to maximize efficiency and comfort while respecting safety and maneuver constraints in a time horizon T . A speedadaptation time instant is the time instant when an on-ramp CAV starts to adapt its speed and position to prepare merging into the target gap. The maximal efficiency and comfort are to be achieved when the value of an objective function is minimal. The objective function is a weighted sum of deviations of inter-vehicle gaps to desired gaps, relative speeds to their direct predecessors, and actual accelerations of all the vehicles, subject to constraints on velocities, actual accelerations, and inter-vehicle gaps. To predict CAVs’ future dynamics in the merging process, the tactical layer controller employs a second-order multi-regime model with a car-following mode and a cooperative merging mode. The transition of the two 

modes is separated by an on-ramp CAV’s speed-adaptation time instant and a time instant when it accomplishes the lateral maneuver. The tactical layer controller transmits the optimal future vehicle merging sequence and speed-adaptation time instants to the operational layer controller as a command with a fixed frequency, $1 / \Delta \hat { t }$ , if the command is accepted by the tactical layer controller. If the command is rejected and a request is made by the operational layer controller, a new command is to be established by the tactical layer controller before $\Delta \hat { t }$ . 

With the command received from the tactical layer controller and ${ \bf { Z } } ^ { \bf { 0 } } ( t _ { 0 } )$ , the value of the state variable defined by the operational layer controller at the current time $t _ { 0 }$ , the operational layer controller rejects the command when no feasible solution is found for an on-ramp vehicle. If the on-ramp vehicle is far away from the end of the acceleration lane, the operational layer controller then requests a new command from the tactical layer controller. A request is a trigger event for the tactical layer controller to establish a new decision without waiting until $\Delta \hat { t }$ . However, if the on-ramp vehicle is close to the end of the acceleration lane, the operational layer controller chooses the next slot after the established target slot directly for the on-ramp vehicle. 

When the tactical command is accepted, the operational layer controller computes longitudinal desired acceleration trajectories for CAVs and lane-changing initiation time instants in a shorter time horizon $T _ { p } ~ < ~ T$ by using MPC. A lanechanging initiation time instant is the time instant when a merging vehicle initiates the lane-changing execution. The operational layer controller utilizes a third-order longitudinal dynamics model as a state prediction model and minimizes the same specification of the objective function as the tactical layer controller. When an on-ramp vehicle has a sufficient gap, it steers towards the main lane and executes merging. The gap acceptance criterion for the on-ramp CAV is that its current and predicted inter-vehicle time gaps to its future direct predecessor and follower in the whole prediction horizon $T _ { p }$ are larger than a certain time gap, depending on the on-ramp vehicle’s location on the acceleration lane. When the on-ramp CAV’s lane-changing initiation time is given, its lateral motion is modeled with a lateral trajectory equation [28], which is elaborated in Appendix A. The operational layer controller updates its commands with a fixed frequency 1/-t. 

# IV. MERGING CONTROL FORMULATION

This section elaborates on the design of the tactical layer controller and operational layer controller. For clarity, only one on-ramp vehicle $r$ is considered to establish a merging sequence and its speed-adaptation time instant. The process applies to scenarios where multiple on-ramp vehicles exist as well. 

# A. Tactical Layer Controller Establishing a Merging Sequence and Speed-Adaptation Time Instant

For the tactical layer controller, the state variable is defined as $\mathbf { Z ^ { \mathsf { t } } } = ( x _ { 1 } , \upsilon _ { 1 } , a _ { 1 } , x _ { 2 } , \upsilon _ { 2 } , a _ { 2 } , \ldots , a _ { N } , x _ { r } , \upsilon _ { r } , a _ { r } ) ^ { T }$ , where $x _ { i }$ , $v _ { i }$ , and $a _ { i }$ $( i = 1 , 2 , . . . , N )$ , $x _ { r }$ , $\upsilon _ { r }$ , and $a _ { r }$ denote mainline 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/b613e35a5aa130cf044ccedc5751c524fa8cd32d73920154d34cefbeb6aba95e.jpg)



Fig. 2. Hierarchical architecture of the merging control system.


CAV i’s location, speed, and actual acceleration, on-ramp CAV’s location, speed, and actual acceleration respectively. For notation simplicity, the time argument is dropped when no ambiguity exists. The decision variable is defined as $\mathbf { U ^ { t } } =$ $( \vec { f } _ { r } , t ^ { p } ) ^ { \check { T } }$ , where $\vec { f } _ { r }$ is a row vector denoting the merging sequence and $t ^ { p }$ stands for the speed-adaptation time instant of the on-ramp CAV. When $t \ < \ t ^ { p }$ , the size of $\vec { f } _ { r }$ is $N$ , and the value of $\hat { \vec { f } } _ { r }$ is $( 1 , 2 , . . . , N )$ . After $t ^ { p }$ , the on-ramp vehicle starts to adapt its speed and position to prepare merging into the target gap and the size of $\vec { f } _ { r }$ is increased to $N { + 1 }$ , and the value of the vector is $( 1 , 2 , . . . , k \mathrm { - } 1 , r , k , . . . N )$ , with ${ \vec { f } } _ { r } ( k ) = r$ , $\vec { f } _ { r } ( k \textrm { -- } 1 ) = k \textrm { -- } 1$ , and ${ \vec { f } } _ { r } ( k + 1 ) \ = \ k$ . To this end, $k$ is the on-ramp CAV’s position in the mainline platoon after accomplishing merging. 

1) Closed Loop System Dynamics Model: A second-order model with a feedback law is used to express the longitudinal behavior of a CAV. The open-loop system dynamics for each vehicle are described in (1). Because the second-order vehicle dynamics model is used, no extra time is needed to reach a new desired acceleration. Actual accelerations equal to desired accelerations. 

$$
\dot {x} _ {i} = v _ {i}, \dot {v} _ {i} = a _ {i}, \quad i = 1, 2, \dots , N, r \tag {1}
$$

Considering cases when there is a conflict between the merging vehicle and the mainline traffic during the on-ramp merging process, vehicles’ motions are categorized into two modes: car-following and cooperative merging. The cooperative merging mode only applies to the on-ramp CAV and its potential direct follower from $t ^ { p }$ to the first time instant when the on-ramp CAV is on the main lane. 

The car-following operation is modeled by a Helly car-following model, as shown in (2) [30]. 

$$
\begin{array}{l} a _ {\vec {f} _ {r} (i)} ^ {c f} (t) = D _ {1} \cdot \Delta v _ {\vec {f} _ {r} (i)} (t - \Delta \hat {t}) \\ + D _ {2} \cdot \left(s _ {\vec {f} _ {r} (i)} (t - \Delta \hat {t}) - s _ {\vec {f} _ {r} (i)} ^ {d} (t - \Delta \hat {t})\right) \tag {2} \\ \end{array}
$$

where, D1 and D2 are parameters, -v f- (i) = v f- (i 1) − v f- (i), $D _ { 1 }$ $D _ { 2 }$ $\Delta \upsilon _ { \vec { f } _ { r } ( i ) } = \upsilon _ { \vec { f } _ { r } ( i - 1 ) } - \upsilon _ { \vec { f } _ { r } ( i ) }$ s f- r (i ) = x f- r (i −1) − x f- r (i ) − lv eh , and s d f- ( $s _ { \vec { f } _ { r } ( i ) } = x _ { \vec { f } _ { r } ( i - 1 ) } - x _ { \vec { f } _ { r } ( i ) } - l _ { \upsilon e h }$ $s _ { \vec { f } _ { r } ( i ) } ^ { d } = \upsilon _ { \vec { f } _ { r } ( i ) } \cdot t _ { d } + s _ { 0 }$ 

are CAV $\vec { f } _ { r } ( i )$ ’s relative speed, inter-vehicle gap and desired inter-vehicle gap to its (potential) direct predecessor. $l _ { v e h }$ , $t _ { d }$ , and $s _ { 0 }$ denote vehicle length, desired time gap and the minimum inter-vehicle gap at standstill respectively. 

For the on-ramp vehicle, before $t ^ { p }$ , it travels to reach its desired speed $v ^ { \mathrm { l i m i t s } }$ as shown in (3), a special car-following mode. When multiple on-ramp vehicles exist, a following on-ramp vehicle uses the vehicular information of its direct preceding on-ramp vehicle in the car-following mode to generate its actual acceleration if its direct preceding vehicle is close to it. 

$$
a _ {r} = D _ {3} \cdot \left(v ^ {\text {l i m i t s}} - v _ {r} (t - \Delta \hat {t})\right) \tag {3}
$$

The cooperative merging mode works by adjusting the inter-vehicle gaps between the on-ramp CAV (CAV $\vec { f } _ { r } ( k ) )$ and its potential direct follower (CAV $\vec { f } _ { r } ( k + 1 ) )$ and predecessor (CAV $\vec { f } _ { r } ( k - 1 ) )$ till these gaps are large enough for the on-ramp CAV to execute merging. During the adjustment, the on-ramp CAV and its potential follower accelerate or decelerate comfortably to create suitable inter-vehicle gaps. We utilize the same criterion of acceptable time gap for lane changing in our previous work [31]. For lane changing, the onramp vehicle tends to accept a smaller inter-vehicle time gap to its potential direct predecessor and follower when it is approaching the acceleration lane’s end as shown in (4) [31], where $x _ { s }$ , $x _ { e }$ , and $t _ { g } ^ { \mathrm { m i n } }$ denote the start and end longitudinal position of the acceleration lane, and the minimum acceptable time gap respectively. 

$$
t _ {g} (t) = \left(x _ {\vec {f} _ {r} (k) (t)} - a c _ {s}\right) \cdot \left(t _ {g} ^ {\min } - t _ {d}\right) / \left(a c _ {e} - a c _ {s}\right) + t _ {d} \tag {4}
$$

The cooperative merging operation is modeled by a piecewise function, as shown in (5). To ensure comfort, when a vehicle is in the cooperative merging mode, its actual acceleration is bounded within $[ d _ { c o m } , a _ { c o m } ]$ , standing for the acceptable range of acceleration during the cooperative merging process. 

$$
a _ {f _ {r} (j)} = \left\{ \begin{array}{l l} \min  \left(a _ {c o m}, \min  \left(a _ {f _ {r} (j)} ^ {c f}, a _ {\max }\right)\right), & a _ {f _ {r} (j)} ^ {c f} \geq 0, \\ \max  \left(d _ {c o m}, \max  \left(a _ {f _ {r} (j)} ^ {c f}, d _ {\max }\right)\right), & a _ {f _ {r} (j)} ^ {c f} <   0, \end{array} \right. \tag {5}
$$

where, the value of $j$ is $k$ or $k + 1$ . $a _ { \mathrm { m a x } }$ and $d _ { \mathrm { m a x } }$ denote maximum positive and minimum negative acceleration of vehicles respectively. $a _ { \mathrm { m a x } }$ and $d _ { \mathrm { m a x } }$ are assumed constant for all CAVs simply, but they can be different for different CAVs in the design. 

2) Tactical Decision Problem Formulation: To improve traffic efficiency and safety, the tactical layer controller aims to make the following vehicles to have the same speed as the first downstream vehicle, ensure inter-vehicle spacing s f (i) $s _ { \vec { f } _ { r } ( i ) }$ to be as desired value $\begin{array} { l } { { s _ { \vec { f } _ { r } ( i ) } ^ { d } } } \\ { { . } } \end{array}$ , and reduce the effort of changing vehicular states which is reflected by actual accelerations. The formulation is as shown in (6) and (7). The time period $T$ is long enough for the on-ramp vehicle to merge in the 

mainstream lane and relax to the equilibrium state. 

$$
\begin{array}{l} \min  _ {\mathbf {U} ^ {\mathrm {t}}} J (\mathbf {Z} ^ {\mathrm {t}}, \mathbf {U} ^ {\mathrm {t}}) = \min  _ {\mathbf {U} ^ {\mathrm {t}}} \left(\int_ {0} ^ {0 + T} \iota (\mathbf {Z} ^ {\mathrm {t}}, \mathbf {U} ^ {\mathrm {t}}) d t\right) \\ + c _ {4} \cdot \left(\sum_ {2} ^ {N + 1} \left(\Delta v _ {\vec {f} _ {r} (i)} (0 + T)\right) ^ {2}\right) \\ + c _ {5} \cdot \left(\sum_ {2} ^ {N + 1} \left(\Delta s _ {\vec {f} _ {r} (i)} (0 + T)\right) ^ {2}\right) (6) \\ \iota = c _ {1} \cdot \sum_ {i} (\Delta s _ {\vec {f} _ {r} (i)}) ^ {2} + c _ {2} \cdot \sum_ {i} (\Delta v _ {\vec {f} _ {r} (i)} ^ {2}) \\ + c _ {3} \cdot \sum_ {i} \left(a _ {\vec {f} _ {r} (i)}\right) ^ {2} (7) \\ \Delta s _ {\vec {f} _ {r} (i)} = s _ {\vec {f} _ {r} (i)} - s _ {\vec {f} _ {r} (i)} ^ {d}, i = 2, 3, \dots , M (t) \\ \end{array}
$$

subject to: 

• the system dynamics model shown in(1), car − f ollowing mode shown in(2) and(3) and cooperative merging mode shown in(5). 

• the initial condition $: \mathbf { Z } ^ { \mathbf { t } } ( 0 ) = \widetilde { \mathbf { Z } } ^ { \mathbf { t } } ( 0 )$ 

• speed constraints $: 0 \leq \upsilon _ { \vec { f } _ { r } ( i ) } \leq \upsilon ^ { \mathrm { l i m i t s } }$ 

• gap constraints $: s _ { \vec { f } _ { r } ( i ) } \geq s _ { 0 }$ . 

• acceleration constraints : dmax ≤ a f- (i) ≤ amax. $\begin{array} { r } { d _ { \operatorname* { m a x } } \leq a _ { \vec { f } _ { r } ( i ) } \leq a _ { \operatorname* { m a x } } . } \end{array}$ (8) 

where, -s f- (i) $\Delta s _ { \vec { f } _ { r } ( i ) }$ denotes vehicle $\vec { f } _ { r } ( i )$ ’s gap error, $c _ { 1 } , \ c _ { 2 } , \ c _ { 3 }$ , $c _ { 4 }$ , and $c _ { 5 }$ are weight parameters, and $M ( t )$ is the size of $\vec { f } _ { r } ( t )$ . Before $t ^ { p }$ , $M ( t ) = N$ and the on-ramp CAV is not included. During $t \ < \ t ^ { p }$ , the on-ramp CAV travels with its desired speeds, generating zero value of the objective function. While $t ~ \geq ~ t ^ { p }$ , $M ( t ) = N { + } 1$ , including the on-ramp CAV at $t ^ { p }$ . The on-ramp vehicle steers towards the main lane when its lane changing cconditions are: 1) $d _ { c o m } \ \leq \ a _ { \vec { f } _ { r } ( k ) } ^ { c f }$ $a _ { \vec { f } _ { r } ( k + 1 ) } ^ { c f } \ \leq \ a _ { c o m } , \ 2$ nging) onramp CAV ${ \vec { f } } _ { r } ( k )$ is on the acceleration lane, and 3) on-ramp CAV ${ \vec { f } } _ { r } ( k )$ ’s inter-vehicle time gaps to its potential direct predecessor and follower are larger than $t _ { g }$ , as shown in (4). After a lane changing maneuver time $t _ { m }$ , the on-ramp CAV accomplishes on-ramp merging process and is on the main lane. 

The tactical layer controller is formulated as a mixed-integer quadratic programming problem. The on-ramp CAV needs to change lane before reaching the end of the acceleration lane. Thus, $t ^ { p }$ has an upper bound. Besides, we discretize the possible values of $t ^ { p }$ to be multiples of the time step $\Delta \hat { t }$ . As the choices of $k$ and $t ^ { p }$ are finite, the problem can be solved iteratively by giving different values to $k$ and $t ^ { p }$ . The optimal $\mathbf { U ^ { t } }$ is then transmitted to the operational layer controller. To ensure safety, the tactical layer controller does not give the on-ramp CAV’s lane-changing initiation time instant as a command, because the tactical controller and operational layer controller have mismatches regarding vehicle dynamics model and vehicular motions. According to current and predicted inter-vehicle time gaps, the operational layer controller then decides lane-changing initiation time based on a gap acceptance criterion [31]. 

# B. Operational Layer Controller Regulating Vehicular Trajectory

1) Operational Layer Controller Formulation: Receiving the optimal combination of the merging sequence $\vec { f } _ { r }$ and $t ^ { p }$ of the on-ramp vehicle, the operational layer controller regulates vehicles’ longitudinal desired accelerations and determines the on-ramp CAV’s lane-changing initiation time instant $t ^ { l }$ to reach efficient and safe traffic performance. Before $t ^ { l }$ is determined, the evaluation frequency of the desired accelerations and $t ^ { l }$ by the operational layer controller is a fixed $1 / \Delta t$ . After the on-ramp vehicle starts to steer towards the main lane at $t ^ { l }$ , $t ^ { l }$ is not evaluated. The operational layer controller is designed based on MPC. With the vehicular information at time $t _ { 0 }$ , the operational layer controller generates the optimal longitudinal desired accelerations and determines $t ^ { l }$ within future $T _ { p }$ time horizon, shorter than $T$ . 

For the operational layer controller, the state variable is defined as Zo = (s f- r (1) , -v f- r (1) , -a f- r (1) , . . . , $\begin{array} { r l r } { { \bf Z } ^ { \bf { o } } } & { { } = } & { ( s _ { \vec { f } _ { r } ( 1 ) } , \Delta \upsilon _ { \vec { f } _ { r } ( 1 ) } , \Delta a _ { \vec { f } _ { r } ( 1 ) } , \cdot \cdot \cdot , } \end{array}$ $\begin{array} { r l } & { \Delta a _ { \vec { f } _ { r } ( M ( t ) ) } , y _ { r } ) ^ { T } } \\ & {  } \end{array}$ , where $\Delta a _ { \vec { f } _ { r } ( i ) } = a _ { \vec { f } _ { r } ( i - 1 ) } \ \cdot \ a _ { \vec { f } _ { r } ( i ) }$ is CAV $\vec { f } _ { r } ( \dot { i } )$ ’s relative actual acceleration to its (future) direct predecessor. The control variable is defined as $\begin{array} { r l } { \mathbf { U ^ { 0 } } } & { { } = } \end{array}$ $( u _ { \vec { f } _ { r } ( 1 ) } , \cdot \cdot \cdot , u _ { \vec { f } _ { r } ( M ( t ) ) } , \xi _ { r } , t ^ { l } ) ^ { T }$ , where $u _ { \vec { f } _ { r } ( i ) }$ is the desired acceleration of CAV $\vec { f } _ { r } ( i )$ and $\xi _ { r }$ is the lane-changing acceptability of the on-ramp vehicle ${ \vec { f } } _ { r } ( k )$ . When lane-changing conditions are not met, $\xi _ { r } ( t )$ equals to 0. When the on-ramp vehicle accepts the lane-changing conditions, $\xi _ { r } ( t )$ becomes 1, the on-ramp vehicle starts to steer towards the main lane, and the corresponding time instant is $t ^ { l }$ . The longitudinal vehicle dynamics model used by the operational layer controller is expressed with a third-order model, as shown in Eqs. (9), (10) and (11) [32]–[34]. An actuator lag $\tau ^ { A }$ is the time duration needed for a vehicle $\vec { f } _ { r } ( i )$ to change its actual acceleration $\underset { \bullet } { a } { \Vec { \mathcal { I } } } _ { r } ( i )$ to its given desired acceleration $u _ { \vec { f } _ { r } ( i ) }$ . $\tau ^ { A }$ of vehicles herein are assumed constant, but there is no restriction on their homogeneity in our design. 

$$
\dot {s} _ {\vec {f} _ {r} (i)} = \Delta v _ {\vec {f} _ {r} (i)}, i = 2, 3, \dots , M (t) \tag {9}
$$

$$
\Delta \dot {v} _ {\vec {f} _ {r} (i)} = \Delta a _ {\vec {f} _ {r} (i)} \tag {10}
$$

$$
\Delta \dot {a} _ {\vec {f} _ {r} (i)} = \frac {u _ {\vec {f} _ {r} (i - 1)} - u _ {\vec {f} _ {r} (i)} - \Delta a _ {\vec {f} _ {r} (i)}}{\tau^ {A}} \tag {11}
$$

When the on-ramp vehicle starts to change lane, i.e. $\xi _ { r } ( t ) = 1$ , its lateral path during the lane changing process is designed to follow a polynomial equation [28], as shown in (21) and (22) in Appendix A. 

We use a MPC method to formulate the control problem of the operational layer controller [15], [16], as shown in (12). The objective function specification is as shown in (13). 

$$
\begin{array}{l} \min  _ {\mathbf {U} ^ {0}} \zeta (\mathbf {Z} ^ {0}, \mathbf {U} ^ {0}) = \min  _ {\mathbf {U} ^ {0}} \left(\int_ {t _ {0}} ^ {t _ {0} + T _ {p}} \psi (\mathbf {Z} ^ {0}, \mathbf {U} ^ {0}) d t\right) \\ + c _ {4} \cdot \sum_ {2} ^ {M (t)} \left(\Delta v _ {\vec {f} _ {r} (i)} \left(t _ {0} + T _ {p}\right)\right) ^ {2} \\ + c _ {5} \cdot \sum_ {2} ^ {M (t)} \left(\Delta s _ {\vec {f} _ {r} (i)} \left(t _ {0} + T _ {p}\right)\right) ^ {2} \tag {12} \\ \end{array}
$$

$$
\begin{array}{l} \psi = \underbrace {c _ {1} \cdot \sum_ {i} (\Delta s _ {i}) ^ {2}} _ {\text {s a f e t y}} + \underbrace {c _ {2} \cdot \sum_ {i} (\Delta v _ {i} ^ {2})} _ {\text {e f f i c i e n c y}} \\ + \underbrace {c _ {3} \cdot \sum_ {i} \left(u _ {i}\right) ^ {2}} _ {\text {c o n t r o l}} \quad i = 2, 3, \dots , M (t) \tag {13} \\ \end{array}
$$

The operational layer controller has the same specification of an objective function as the tactical layer control. However, the operational layer controller generates the CAVs’ desired accelerations by minimizing the objective function. Minimizing the first two items implies that vehicles tend to reach equilibrium states, where the inter-vehicle gaps are their desired values and relative speeds are zeros, safety and efficiency being ensured. Penalizing large positive or small negative accelerations saves control effort. The lane-changing acceptability $\xi _ { r }$ is not controlled as the longitudinal accelerations, but it is affected by the predicted inter-vehicle gaps and speeds. For an open-loop control of the operational layer controller, the lane-changing acceptability $\xi _ { r }$ is determined by using (14). When the on-ramp vehicle is on the acceleration lane and the inter-vehicle gaps between it, ordering $k$ after merging, and its future direct predecessor and follower are larger enough within future time horizon $T _ { p }$ , it changes lane. 

$$
\begin{array}{l} \xi_ {r} = \prod_ {j = t _ {0}} ^ {t _ {0} + T _ {p}} \left(s _ {\vec {f} _ {r} (k)} (j) - v _ {\vec {f} _ {r} (k)} \cdot t _ {g} - s _ {0} \geq 0\right) \\ \cdot \left(s _ {\vec {f} _ {r} (k + 1)} (j) - v _ {\vec {f} _ {r} (k + 1)} \cdot t _ {g} - s _ {0} \geq 0\right) \tag {14} \\ \end{array}
$$

where, $t _ { g }$ is calculated by using the position of the on-ramp vehicle at $t _ { 0 } , \ x _ { \vec { f } _ { r } ( k ) } ( t _ { 0 } )$ , when the on-ramp vehicle is on the acceleration lane. 

The control process is subject to below constraints: 

• the system dynamics model shown in (9), (10) and (11). 

• an initial state: $\mathbf { Z ^ { 0 } } ( t _ { 0 } ) = \widetilde { \mathbf { Z ^ { 0 } } } ( t _ { 0 } )$ 

• speed constraints: $0 \leq \upsilon _ { \vec { f } _ { r } ( i ) } \leq \upsilon ^ { \mathrm { l i m i t s } }$ 

• gap constraints: $s _ { \vec { f } _ { r } ( i ) } \geq s _ { 0 }$ 

• acceleration constraints: $d _ { \operatorname* { m a x } } \leq u _ { \vec { f } _ { r } ( i ) } \leq a _ { \operatorname* { m a x } }$ 

2) Solution to the Optimal Control Problem: The generation of optimal longitudinal desired accelerations for the formulated MPC problem is achieved by using Pontryagin’s Minimum Principle [27], [35]. 

$$
X _ {1} = \left(s _ {\vec {f} _ {r} (1)}, \dots , s _ {\vec {f} _ {r} (M (t))}\right) ^ {T} \tag {15}
$$

$$
X _ {2} = \left(\Delta v _ {\vec {f} _ {r} (1)}, \dots , \Delta v _ {\vec {f} _ {r} (M (t))}\right) ^ {T} \tag {16}
$$

$$
X _ {3} = \left(\Delta a _ {\vec {f} _ {r} (1)}, \dots , \Delta a _ {\vec {f} _ {r} (M (t))}\right) ^ {T} \tag {17}
$$

$$
S ^ {d} = \left(s _ {\vec {f} _ {r} (1)} ^ {d}, \dots , s _ {\vec {f} _ {r} (M (t))} ^ {d}\right) ^ {T} \tag {18}
$$

We define $X _ { 1 }$ , $X _ { 2 }$ , $X _ { 3 }$ , and $S ^ { d }$ as shown in (15)-(18) and create the corresponding Hamiltonian function of the optimization problem as shown in (19). For the first mainline vehicle, its relative speeds, relative actual accelerations and gap errors are 

zeros, if it travels with a constant speed. 

$$
\begin{array}{l} H = c _ {1} \cdot \left(X _ {1} - S ^ {d}\right) ^ {2} + c _ {2} \cdot X _ {2} ^ {2} + c _ {3} \cdot \sum_ {i} u _ {\vec {f} _ {r} (i)} ^ {2} \\ + \lambda_ {1} \cdot X _ {2} + \lambda_ {2} \cdot X _ {3} \\ + \lambda_ {3} \cdot \sum_ {i} \frac {u _ {\vec {f} _ {r} (i - 1)} - u _ {\vec {f} _ {r} (i)}}{\tau^ {A}} - \lambda_ {3} \cdot \frac {X _ {3}}{\tau^ {A}} \tag {19} \\ \end{array}
$$

$$
\dot {\lambda} _ {1} = - \frac {\partial H}{\partial X _ {1}}; \dot {\lambda} _ {2} = - \frac {\partial H}{\partial X _ {2}}; \dot {\lambda} _ {3} = - \frac {\partial H}{\partial X _ {3}} \tag {20}
$$

where, $\lambda _ { 1 } , \lambda _ { 2 }$ , and $\lambda _ { 3 }$ are co-state variables of $X _ { 1 } , \ X _ { 2 }$ , and $X _ { 3 }$ respectively. To have the optimal longitudinal desired accelerations, (9), (10), (11) and (20) need to be solved. The terminal conditions for (20) are $\lambda _ { 1 } ( t _ { 0 } + T _ { p } ) = 2 \cdot c _ { 5 } \cdot ( X _ { 1 } ( t _ { 0 } +$ $T _ { p } ) - S ^ { d } ( t _ { 0 } + T _ { p } ) )$ , $\lambda _ { 2 } ( t _ { 0 } + T _ { p } ) = 2 \cdot c _ { 4 } \cdot ( X _ { 2 } ( t _ { 0 } + T _ { p } ) )$ , and $\lambda _ { 3 } ( t _ { 0 } + T _ { p } ) = 0$ . We are faced with a two-point boundaryvalue problem which is solved by using an iterative algorithm used in [29]. 

For the on-ramp CAV, before $t ^ { p }$ , it runs with its desired speeds until reaching the speed limits. It utilizes (12) to generate its desired acceleration by making $\Delta \upsilon _ { r } = \upsilon ^ { \mathrm { l i m i t s } } - \upsilon _ { r }$ and $\Delta s _ { r } = 0$ . When multiple on-ramp vehicles exist, a following on-ramp vehicle utilizes its direct preceding vehicle’s information to regulate its desired acceleration by (12) and the generated value of the objective function is included in the tactical layer controller and the operational layer controller to calculate the total value of the objective function. 

# V. SIMULATION EXPERIMENTS DESIGN AND PERFORMANCE INDICATORS

In this section, we describe numerical experiment settings to test the designed hierarchical cooperative merging strategy and give its detailed parameter settings. Performance indicators used to show the traffic operations with the proposed strategy are given. 

# A. Simulation Scenarios

To test the performance of the proposed hierarchical control approach, we design 135 scenarios with different initial conditions, desired time gap settings, and different numbers of on-ramp vehicles. The initial conditions include the on-ramp CAVs’ initial speed and the initial relative position (RP) of the first on-ramp CAV to the space between mainline CAV 3 and 4. For simplicity, we use percentages to represent RPs. When the first on-ramp CAV and mainline CAV 3 enter into the control zone, used in a benchmark control method, at the same time, or CAV 4 as shown in Fig. 1, the RP is indicated by $0 \%$ or $100 \%$ respectively. The RPs are set to be $0 \%$ , $20 \%$ , $40 \%$ , $60 \%$ and $80 \%$ . The desired time gap $t _ { d }$ varies among 0.6 s, 0.8 s, and $1 \ s$ . The on-ramp CAVs’ initial speed changes among $1 5 m / s$ , $2 0 m / s$ , and $2 5 m / s$ . The acceleration lane’s longitudinal start point is 0 meter $( m )$ , and its endpoint is $3 0 0 m$ . The initial first on-ramp vehicle’s rear position is $- 6 2 ~ m$ . 

There are five mainline CAVs, $N = 5$ . Their initial speeds are $2 5 ~ m / s$ . Initially, for 90 scenarios, one on-ramp CAV 

exists. Mainline vehicles start in equilibrium states for 45 scenarios and in non-equilibrium states for the other 45 scenarios respectively. When vehicles start in non-equilibrium states, the inter-vehicle distance between initial vehicle 1 and 2 is 0.5 times of the desired inter-vehicle distance of the vehicle 2 and other vehicles have desired inter-vehicle distances to their direct preceding vehicles respectively. Another 45 scenarios starting with two on-ramp CAVs are included as well. For these 45 scenarios, all vehicles start from equilibrium states. 

The first mainline CAV is set to travel with $2 5 ~ m / s$ all the time. Besides, a fixed feedback delay $\tau ^ { S } = 0 . 2 ~ s$ is also considered: $\widetilde { { \mathbf Z } ^ { \mathrm { t } } } ( 0 ) = { \mathbf Z } ^ { \mathrm { t } } ( 0 - \tau ^ { S } )$ and $\widetilde { { \mathbf Z } ^ { 0 } } ( t _ { 0 } ) = { \mathbf Z } ^ { { \mathbf 0 } } ( t _ { 0 } - \tau ^ { S } )$ , during the experiments. 

# B. Benchmark Control Method for Comparison

To show the advantage of the designed hierarchical control approach, we compare it with the benchmark control strategy. The benchmark control strategy uses a first-in-first-out method, a vehicle entering into a control zone earlier leaving it earlier, to determine a merging sequence and implements the same herein designed operational layer controller to generate vehicular motions. The control zone is delimited, with a distance L, as shown in Fig. 1. The distance L is within the transmission ranges of Dedicated Short-Range Communication (DSRC). For the benchmark control strategy, $t ^ { p }$ is $_ \mathrm { ~ 0 ~ } s$ . The corresponding future mainline vehicle order for the first on-ramp vehicle can be $k = 4$ for all scenarios and $k = 3$ o r 4 when the on-ramp CAV and mainline CAV 3 enter into the control zone at the same time. When $k$ can be 3 or 4 and on-ramp vehicles’ initial speeds are $2 5 ~ m / s$ , the future vehicle order of the second on-ramp vehicle after merging can be 5 or 6; otherwise, the future vehicle order of the second on-ramp vehicle after merging is 6. 

# C. Parameter Settings

For our designed tactical and operational layer controller, their common parameters use the same values respectively. The parameter values representing vehicles’ maximum positive and minimum negative accelerations, vehicles’ length, vehicles’ desired time gap, etc., are collected through V2V or V2I communication. We herein refer to parameter settings assumed in others’ experiments to determine parameters’ values in our experiments. The parameters are set as follows: $L = 6 2 \ m$ , $\textit { T } = 5 0 \textit { s }$ , $T _ { p } ~ = ~ 6 ~ s$ [29], $\upsilon ^ { \mathrm { l i m i t s } } ~ = ~ 3 0 ~ m / s$ , $d _ { c o m } =$ $- 4 \ m / s ^ { 2 }$ , $\hat { a _ { c o m } } = 2 ~ m / s ^ { 2 }$ , $d _ { \operatorname* { m a x } } = - 4 ~ m / s ^ { 2 }$ [36], $a _ { \mathrm { m a x } } =$ $2 \ m / s ^ { 2 }$ [36], $t _ { g } ^ { \mathrm { m i n } } = 0 . 2 5 ~ s$ [31], $\Delta t = 0 . 1 \ s$ , $\Delta \hat { t } = 0 . 5 \ s$ , $x _ { s } = 0 \ m$ , $x _ { e } = 3 0 0 ~ m$ , $l _ { \mathit { v e h } } = 4 \ m$ , $D _ { 1 } = 0 . 2$ , $D _ { 2 } = 0 . 7$ , $D _ { 3 } = 2$ , $c _ { 1 } = 0 . 1$ , $c _ { 2 } = 0 . 5$ , $c _ { 3 } = 0 . 5$ , $c _ { 4 } = 0 . 1$ , $c _ { 5 } = 0 . 1$ , $t _ { m } = 5 ~ s$ , $h = - 3 . 5$ , $s _ { 0 } = 2 ~ m$ , and $N = 5$ . The values of weights $c _ { 1 }$ , c2, c3, c4, and $c _ { 5 }$ were manually tuned to give stable closed loop performance. Systematic tuning methods of MPC can be found in [37]. 64-bit MATLAB R2018a on windows 7 system conducts the experiments with different initial settings. The third-order vehicle dynamic model is chosen to represent the behavior of vehicles. The operational layer controller regulates vehicular longitudinal accelerations and the lane-changing initiation time instants for lane changers 

as shown in (12). When a lane changer steers towards the main lane and executes merging, its lateral positions change according to (21). For each experiment, the simulation time is $5 0 ~ s$ , long enough for the on-ramp vehicle to merge into the mainline traffic. 

# D. Performance Indicators

Selected performance indicators are related to the actual vehicular trajectories in the simulation time and control objectives, representing the overall traffic operations. We aim to achieve efficient and safe merging of the on-ramp vehicle and to generate smooth trajectories for ride comfort. To this end, the selected performance indicators are the overall value of the objective function calculated by using the weighted sum of the actual gap errors, relative speeds, and the desired accelerations of CAVs during the merging process and the occurrence of collision. The weight parameters on gap errors, relative speeds, and the desired accelerations are $c _ { 1 }$ , $c _ { 2 }$ , and $c _ { 3 }$ respectively. Besides, the terminal inter-vehicle gap errors with a weight parameter $c _ { 5 }$ and relative speeds with a weight parameter $c _ { 4 }$ are also included in the objective function. 

# VI. SIMULATION RESULTS AND DISCUSSION

In this section, simulation results with two different on-ramp merging control methods under the 135 experimental scenarios are given and discussed. 

# A. Safe Performance

In all the 135 scenarios, no collision exists for the two on-ramp merging control methods. One example of the evolution of inter-vehicle gaps and the desired accelerations with the proposed hierarchical control approach (HCA) under one of the extremely challenging scenarios are as shown in Fig. 3. In this scenario, only one on-ramp vehicle exists. The desired time gap $t _ { d }$ is $1 \ s$ , the on-ramp vehicle’s initial speed $v _ { r } ( 0 )$ is $1 5 ~ m / s$ , and RP is $0 \%$ , the on-ramp CAV and mainline CAV 3 entering into the control zone at the same time. With the hierarchical control approach, the future on-ramp CAV’s vehicle order after merging is $k = 4$ , and $t ^ { p }$ is $2 \ s$ , as shown in Table I. The dashed black line illustrates that the on-ramp vehicle is still on the on-ramp or acceleration lane, while the solid black line indicates it is on the main lane. Obviously, the merging process does not have collisions; thus, it is safe. At around $2 0 s$ , the inter-vehicle gaps and desired accelerations relax to the equilibrium values. 

# B. Performance of the Proposed Hierarchical Control Approach

1) One On-Ramp Vehicle: Mainline Vehicles Starting From Equilibrium States: When one on-ramp vehicle exists and mainline vehicles start from equilibrium states, for the possible 45 scenarios with different initial conditions and desired time gap settings, experimental results show that the proposed hierarchical control approach outperforms the benchmark control method in 34 scenarios, and behaves as good as the benchmark control method in 11 scenarios. When the on-ramp vehicle’s 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/58e4ea143051644236c269700799899631ac8cd8bdc6f037a6201c7101a3619a.jpg)



(a) Inter-vehicle gaps


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/23a2139013521da895ca5aa0fcf797b19a33f3c92213d4472fe205f0d0e819c6.jpg)



(b) Desired accelerations



Fig. 3. Vehicular trajectories with the proposed hierarchical control approach under a scenario where the on-ramp CAV and mainline CAV 3 enter into the control zone at the same time.



TABLE I EXPERIMENT RESULTS OF THE SCENARIOS WITH vr (0) IS $1 5 m / s$


<table><tr><td rowspan="2">td(s); RP (%)</td><td colspan="3">Objective function value</td><td rowspan="2">k;tp(s)</td><td rowspan="2">Improvement (%)</td></tr><tr><td>k=3,tp=0</td><td>k=4,tp=0</td><td>HCA</td></tr><tr><td>0.6;0</td><td>8414.83</td><td>2023.63</td><td>778.90</td><td>5;4</td><td>90.74 &amp; 61.51</td></tr><tr><td>0.6;20</td><td></td><td>2386.19</td><td>660.01</td><td>5;4</td><td>72.34</td></tr><tr><td>0.6;40</td><td></td><td>3092.92</td><td>728.09</td><td>5;4</td><td>76.46</td></tr><tr><td>0.6;60</td><td></td><td>4171.99</td><td>967.60</td><td>5;3</td><td>76.81</td></tr><tr><td>0.6;80</td><td></td><td>5652.86</td><td>1200.77</td><td>5;6.5</td><td>78.76</td></tr><tr><td>0.8;0</td><td>9690.12</td><td>2099.76</td><td>1625.89</td><td>4;7</td><td>83.22 &amp; 22.57</td></tr><tr><td>0.8;20</td><td></td><td>2344.72</td><td>1192.44</td><td>5;4</td><td>49.14</td></tr><tr><td>0.8;40</td><td></td><td>3098.95</td><td>957.02</td><td>5;4</td><td>69.12</td></tr><tr><td>0.8;60</td><td></td><td>4398.80</td><td>1004.74</td><td>5;4</td><td>57.15</td></tr><tr><td>0.8;80</td><td></td><td>6296.09</td><td>1247.11</td><td>5;2.5</td><td>59.76</td></tr><tr><td>1;0</td><td>11130.34</td><td>2337.90</td><td>1837.97</td><td>4;2</td><td>83.49 &amp; 21.38</td></tr><tr><td>1;20</td><td></td><td>2402.95</td><td>2044.39</td><td>4;8</td><td>14.92</td></tr><tr><td>1;40</td><td></td><td>3170.85</td><td>1519.02</td><td>5;4</td><td>52.09</td></tr><tr><td>1;60</td><td></td><td>4687.61</td><td>1275.86</td><td>5;4</td><td>72.78</td></tr><tr><td>1;80</td><td></td><td>7032.86</td><td>1366.88</td><td>5;3</td><td>80.56</td></tr></table>

initial speed $v _ { r } ( 0 )$ is $1 5 ~ m / s$ , 0.6 times of the speed of the mainline traffic $2 5 ~ m / s$ , using HCA for on-ramp merging control brings pronounced improvements in traffic operations as shown in Table I. In Table I, the first column includes different combinations of desired time gaps $t _ { d }$ and RP. The overall value of the objective function is calculated with the weighted sum of the actual gap errors, relative speeds, and the desired accelerations of CAVs during the merging process with a given merging sequence and $t ^ { p }$ generated by using the first-in-first-out method or HCA are given in columns 2, 3, and 4. The established decisions from the HCA are presented in column 5. Column 6 indicates the improvement in traffic operations by using the proposed HCA, all higher than $1 4 . 9 2 \%$ . The improvement percentage is calculated by dividing the objective function value caused by using the firstin-first-out method into the deviation of the objective function value caused by using the first-in-first-out method and the HCA. Initially, the on-ramp CAV’s speed deviation to the speed of the mainline traffic is large. Using the first-in-firstout method to establish a merging sequence does not give 


TABLE II EXPERIMENT RESULTS OF THE SCENARIOS WHERE THE ON-RAMP CAV AND MAINLINE CAV 3 ENTER INTO THE CONTROL ZONE AT THE SAME TIME


<table><tr><td rowspan="2">td(s);vr(0)(m/s)</td><td colspan="3">Objective function value</td><td rowspan="2">k;tp(s)</td><td rowspan="2">Improvement (%)</td></tr><tr><td>k=3,tp=0</td><td>k=4,tp=0</td><td>HCA</td></tr><tr><td>0.6;15</td><td>8414.83</td><td>2023.63</td><td>778.90</td><td>5;4</td><td>90.74 &amp; 61.51</td></tr><tr><td>0.8;15</td><td>9690.12</td><td>2099.76</td><td>1625.89</td><td>4;7</td><td>83.22 &amp; 22.57</td></tr><tr><td>1;15</td><td>11130.34</td><td>2337.90</td><td>1837.97</td><td>4;2</td><td>83.49 &amp; 21.38</td></tr><tr><td>0.6;20</td><td>2562.47</td><td>1106.06</td><td>741.53</td><td>4;2</td><td>71.06 &amp; 32.96</td></tr><tr><td>0.8;20</td><td>3411.90</td><td>1579.01</td><td>1183.04</td><td>4;1.5</td><td>65.33 &amp; 25.08</td></tr><tr><td>1;20</td><td>4396.84</td><td>2131.91</td><td>1691.02</td><td>4;1.5</td><td>61.54 &amp; 20.68</td></tr><tr><td>0.6;25</td><td>1335.10</td><td>1335.10</td><td>1121.98</td><td>3;1.5</td><td>15.96</td></tr><tr><td>0.8;25</td><td>1985.48</td><td>1985.48</td><td>1058.95</td><td>3;2</td><td>46.67</td></tr><tr><td>1;25</td><td>2758.56</td><td>2758.56</td><td>1984.06</td><td>3;3</td><td>28.08</td></tr></table>

time for the on-ramp vehicle to increase its speed. Its potential direct follower needs to brake strongly to facilitate on-ramp CAV’s merging, causing large values of desired accelerations. By contrast, HCA gives the on-ramp CAV several seconds $t ^ { p }$ to accelerate to increase its speed; and then makes the on-ramp vehicle to adapt its speed and position to its target gap. After merging, the mainline vehicle order for the on-ramp CAV is 4 or 5. 

With the on-ramp CAV’s initial speed $v _ { r } ( 0 )$ increases to $2 0 ~ m / s$ or $2 5 ~ m / s$ , the HCA still outperforms the benchmark control method under scenarios where the on-ramp CAV and mainline CAV 3 enter into the control zone at the same time, RP being $0 \%$ , as shown in Table II. The improvements in traffic operations by using the proposed HCA are all higher than $1 5 . 9 6 \%$ . When the on-ramp CAV’s initial speed $v _ { r } ( 0 )$ is $2 0 ~ m / s$ , the HCA chooses 4 or 5 as the on-ramp CAV’s future mainline vehicle order, and gives $t ^ { p }$ a positive value, several seconds. It is noticeable that when RP is $0 \%$ , choosing $k = 3$ or $k = 4$ by the benchmark control method for on-ramp merging does matter when $v _ { r } ( 0 )$ is not $2 5 ~ m / s$ . The merging sequences with $k = 4$ work better. When $v _ { r } ( 0 )$ is $2 5 ~ m / s$ , choosing $k = 3$ or $k = 4$ by the benchmark control method achieves the same value of the objective function, and thus makes no difference to the traffic operations. 

When the on-ramp CAV’s initial speed $v _ { r } ( 0 )$ is $2 0 ~ m / s$ , compared with the benchmark control method, using HCA brings at least $1 3 . 4 7 \%$ improvement in traffic operations where RP is $20 \%$ or $80 \%$ . HCA tends to give the same merging sequence as the benchmark control method when the on-ramp CAV’s initial position is around the middle of the mainline CAV 3 and 4, as shown in Table III. With the desired time gap increases, the possibility of the HCA to give the same merging sequence as the benchmark control method increases. 


TABLE III EXPERIMENT RESULTS OF THE SCENARIOS WITH $v _ { r }$ (0) IS $2 0 m / s$ AND RP IS NOT $0 \%$


<table><tr><td rowspan="2">td(s)</td><td rowspan="2">RP (%)</td><td colspan="2">Objective function value</td><td rowspan="2">k;tp(s)</td><td rowspan="2">Improvement (%)</td></tr><tr><td>k=4,tp=0</td><td>HCA</td></tr><tr><td>0.6</td><td>20</td><td>873.77</td><td>700.84</td><td>4;2</td><td>19.79</td></tr><tr><td>0.6</td><td>40</td><td>871.97</td><td>848.00</td><td>4;2</td><td>2.75</td></tr><tr><td>0.6</td><td>60</td><td>1127.47</td><td>1076.66</td><td>4;3.5</td><td>4.51</td></tr><tr><td>0.6</td><td>80</td><td>1657.77</td><td>942.28</td><td>5;2</td><td>43.16</td></tr><tr><td>0.8</td><td>20</td><td>1201.85</td><td>1014.07</td><td>4;1.5</td><td>15.62</td></tr><tr><td>0.8</td><td>40</td><td>1128.47</td><td>1123.15</td><td>4;1.5</td><td>0.47</td></tr><tr><td>0.8</td><td>60</td><td></td><td></td><td>4;0</td><td>0</td></tr><tr><td>0.8</td><td>80</td><td>2185.79</td><td>1594.65</td><td>5;1.5</td><td>27.05</td></tr><tr><td>1</td><td>20</td><td>1593.79</td><td>1379.06</td><td>4;1.5</td><td>13.47</td></tr><tr><td>1</td><td>40</td><td>1439.35</td><td>1438.58</td><td>4;1</td><td>0.5</td></tr><tr><td>1</td><td>60</td><td></td><td></td><td>4;0</td><td>0</td></tr><tr><td>1</td><td>80</td><td>2723.37</td><td>1981.38</td><td>4;5.5</td><td>27.25</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/527f7cc8b0c287fdc19676ca1b0912a4b2c6f83642de0782c56e8134a57c4ea8.jpg)



Fig. 4. The performance of the hierarchical control approach compared with the benchmark control method.


When the on-ramp CAV’s initial speed is $2 5 ~ m / s$ , the same initial speed as the mainline traffic, the two control methods behave the same when initial RP is within $[ 2 0 \% , 6 0 \% ]$ . 

Compared with the benchmark control method, the performance of the HCA under the 45 scenarios are marked in Fig. 4. In Fig. 4, a circle means that using HCA brings improvement in traffic operations; a star means that HCA gives the same decision as the benchmark control method. By observing Table I, Table II, Table III, and Fig. 4, we conclude that the HCA outperforms the benchmark control method when the on-ramp CAV’s initial speed is $1 5 m / s$ , when the desired time gap is $_ { 0 . 6 \textit { s } }$ or when the on-ramp CAV’s relative position to mainline CAV 3 and 4 is $0 \%$ , $20 \%$ , and $80 \%$ . When the on-ramp CAV’s initial speed is $2 0 ~ m / s$ , the HCA also outperforms the benchmark control method when the on-ramp CAV’s relative position to mainline CAV 3 and 4 is $40 \%$ . Under the remaining scenarios, the HCA gives the same decisions as the benchmark control method. 

2) One On-Ramp Vehicle: Mainline Vehicles Starting From Non-Equilibrium States: In Fig. 3, after the on-ramp vehicle accomplishes lane changing, small inter-vehicle gaps exist. To this end, the two control methods are further tested with a small inter-vehicle gap existing in mainline traffic, checking 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/0055b1cb5acb1da1e5024ac5127899ca1c32221ca3f33e5c17990568a13bf73d.jpg)



Fig. 5. The performance of the hierarchical control approach compared with the benchmark control method when a small gap exists.


their performance when a new on-ramp vehicle shows up after the first on-ramp vehicle changes lane. For the 45 scenarios with mainline vehicles starting from non-equilibrium states, a small inter-vehicle distance $0 . 5 { \cdot } v _ { 2 } { \cdot } t _ { d }$ is given to initial vehicle 2 and other following mainline vehicles start from the equilibrium states. Before $t ^ { p }$ , initially mainline CAV 2 decelerates to have its desired inter-vehicle distance, reducing its speed. Mainline CAV 3 decelerates to reduce relative speed to CAV 3. With these changes in vehicular states, the performance of the HCA is as shown in Fig. 5. 

By comparing with Fig. 4, the differences exist in 5 scenarios. 3 of them are with $v _ { r } ( 0 )$ being $2 5 ~ m / s$ , RP being $80 \%$ , and $t _ { d }$ being $0 . 6 \ s , \ 0 . 8 \ s$ , or $1 \ s$ . The remaining 2 scenarios are: (1) $\upsilon _ { r } ( 0 ) = 2 0 ~ m / s$ , $\mathrm { R P } = 6 0 \%$ , and $t _ { d } ~ = ~ 0 . 6 ~ s $ ; (2) $\upsilon _ { r } ( 0 ) ~ = ~ 2 0 ~ m / s$ , $\mathrm { R P } ~ = ~ 4 0 \%$ , and $t _ { d } ~ = ~ 1 ~ s$ . For these 5 scenarios, the HCA establishes the same decision as the firstin-first-out method instead of outperforming in Fig. 4. As a result, under 16 scenarios, the two control methods give the same decision; under the remaining 29 scenarios, the HCA outperforms the first-in-first-out method, averagely bringing $3 3 . 0 1 \%$ improvement in traffic operations. 

When RP is $0 \%$ , for the first-in-first-out method using $k = 4$ outperforms $k = 3$ when v $_ { r } ( 0 ) \ < 2 5 \ m / s$ . However, when $v _ { r } ( 0 )$ is $2 5 ~ m / s$ , choosing $k = 4$ or $k = 3$ leads to the same value of the objective function. The finding is the same as shown in Table II. 

3) Two On-Ramp Vehicles: Mainline Vehicles Starting From Equilibrium States: When two on-ramp vehicles exist on the on-ramp lane and the second on-ramp vehicle has the desired inter-vehicle distance to the first one, the second on-ramp vehicle’s future vehicle order after merging is 6 or 5 decided by the first-in-first-out method. Choosing 5 as the future vehicle order of the second on-ramp vehicle is only possible when RP is $0 \%$ and $v _ { r } ( 0 )$ is $2 5 ~ m / s$ . For the HCA, the future vehicle order of the second on-ramp vehicle is 6 under 42 scenarios. For the remaining three scenarios where $v _ { r } ( 0 )$ is $2 5 ~ m / s$ and RP is $40 \%$ , the HCA gives 5 as the second on-ramp vehicle’s future vehicle order and generates $5 . 5 \ s$ or $_ \textit { 6 5 }$ as its speed-adaptation time instant. Given the same initial condition for the first on-ramp vehicle in Fig. 3, by adding the second on-ramp vehicle, the HCA gives $2 . 5 \ s$ as the speed-adaptation time instant for the two on-ramp vehicles 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/0ca959373108e5f2171eb83962a08e536c38585c0ee93f5903a58e59cf9335da.jpg)



(a) first-in-first-out method


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/d195ce67534f749272069b3aa396437f701bc0afce143d2bb699d60aa656a806.jpg)



(b)HCA



Fig. 6. Vehicular trajectories with the hierarchical control approach under a scenario where the on-ramp CAV and mainline CAV 3 enter into the control zone at the same time.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/c4d0dd523d5351256415c2d895d18b0b43277b09e423fe213add9ecdd680643c.jpg)



Fig. 7. The performance of the proposed hierarchical control approach compared with the benchmark control method under scenarios starting with two on-ramp vehicles.


respectively. The desired acceleration trajectories of vehicles are as shown in Fig. 6. The black or dashed blue line illustrates that the first or second on-ramp vehicle is still on the on-ramp or acceleration lane respectively, while the solid black or blue line indicates the vehicle is on the main lane respectively. For the first-in-first-out method, the on-ramp vehicles are on the main lane at $8 . 7 s$ and $1 0 . 7 s$ respectively, bringing 5732.25 as the objective function value. 

In Fig. 6(b), the second on-ramp vehicle follows the first on-ramp vehicle before $2 . 5 ~ s$ , bringing 37.90 to the objective function value. After $2 . 5 ~ s$ , the two on-ramp vehicles’ trajectories are regulated together with mainline vehicles. At $1 0 . 8 ~ s$ and $1 0 . 6 \ s$ , the two on-ramp vehicles are on the main lane respectively. The merging process produces in total 3473,94 to be the objective function value, making $3 9 . 4 0 \%$ improvement compared with the first-in-first-out method. 

The comparison results of the two control methods are as shown in Fig. 7. An upward-pointing triangle shows that the HCA deteriorates traffic operations compared with the firstin-first-out method. By comparison, for 7 scenarios, the two control methods generate the same decisions. For 4 scenarios, the HCA deteriorates traffic operations, averagely binging $1 . 2 \%$ deterioration. However, for the remaining 34 scenarios, the HCA makes an averagely $2 6 . 6 5 \%$ improvement. To this end, the HCA still has superiority. 

Under scenarios where two on-ramp vehicles exist and are close to each other, when RP is $0 \%$ and $v _ { r } ( 0 )$ is $2 5 ~ m / s$ , choices of $k = 3$ or $k = 4$ for the first on-ramp or of using 

5 or 6 as the future vehicle order of the second on-ramp vehicle by the first-in-first-out method work the same as scenarios where only one on-ramp vehicle exist. When RP is $0 \%$ and $v _ { r } ( 0 )$ is less than $2 5 ~ m / s$ , using $k = 4$ and 6 as the future vehicle order of the second on-ramp vehicle by the firstin-first-out method brings improvement in traffic operations compared with other choices. 

# C. Results of and Recommendations on Using the first-in-first-out Method

Because the first-in-first-out method is a simple way to determine a merging sequence, compared with the proposed hierarchical control approach, we give recommendations on when to use the first-in-first-out method reasonably and suitably to traffic operators and researchers. For all the scenarios where the first on-ramp CAV and the mainline CAV 3 enter into the control zone at the same time, using the first-in-firstout method to establish merging sequences lose quite some traffic benefits, as shown in Table II, Fig. 4, Fig. 5, and Fig. 7, with $k = 4$ having an overall better performance than with $k = 3$ for the first-in-first-out method. To this end, priority can be given to mainline traffic when a mainline vehicle and an on-ramp vehicle enter into the control zone at the same time. When the first on-ramp vehicle’s initial speed $v _ { r } ( 0 )$ is $1 5 ~ m / s$ , 0.6 times of the speed of the mainline traffic $2 5 ~ m / s$ , the first-in-first-out method, does not reach a good overall traffic performance as the proposed hierarchical control approach, as shown in Table I. To this end, using the first-infirst-out to establish merging sequences is not suitable when the initial speed of the first on-ramp vehicle is significantly lower than the mainline traffic. When the first on-ramp CAV enters into the control zone between two mainline CAVs, with the on-ramp vehicle’s initial speed increasing to 20 $m / s$ , the first-in-first-out method is possibly suitable as shown in Table III and Fig. 4. The possibility is higher when CAV 2 has a small inter-vehicle gap compared to its desired value as shown in Fig. 5. When the on-ramp vehicle’s initial speed reaches $2 5 ~ m / s$ , the possibility of using the first-in-first-out method to have the same decision as the proposed hierarchical control approach greatly increases, as shown in Fig. 4. 

Compared with the optimal vehicle merging sequences and the speed-adaptation time instants of on-ramp vehicles under 135 scenarios, determined by the proposed hierarchical control approach, we recommend researchers or traffic operators to use the first-in-first-out method when the initial speed of the first on-ramp vehicle $v _ { r } ( 0 )$ is close to the mainline traffic and its initial relative position to two mainline vehicles is within $[ 4 0 \% , 6 0 \% ]$ . When $v _ { r } ( 0 )$ is slower than the speed of the mainline traffic, it is better for the on-ramp vehicle to accelerate for several seconds to reach or slightly exceed the speed of the mainline traffic before using the first-in-firstout method to establish a merging sequence. The distance of the control zone L is thus shrinking with the rear of the on-ramp vehicle. If the on-ramp CAV has the same speed as the mainline traffic and enters into the control zone at the same time instant as a mainline CAV, the first-in-first-out method is not recommended to be implemented immediately, as shown 

in Table II; the on-ramp CAV is recommended to accelerate for 1 or $2 \ s$ and to choose an anterior slot or gap for merging, compared to initial option decided by first-in-first-out method. 

# D. Discussion

The proposed hierarchical control approach generates a combination of an optimal merging sequence and speed-adaptation time instants of the on-ramp merging vehicles. Instead of making an on-ramp vehicle to adapt its speed and position for merging immediately after it enters into an on-ramp lane employed by existing methods, our tactical layer controller allows an on-ramp vehicle to move with desired speeds for a certain time period before it starts to adapt its speed and position to prepare merging into the target gap. The time period allows the on-ramp vehicle to increase its speed, reducing speed deviation to the mainline traffic, and to adjust its relative position to two mainline vehicles where the target gap locates. As a result of the speed and position adaptation, its direct follower does not need to brake strongly to facilitate the merging maneuver, when the initial speed of the on-ramp vehicle is significantly lower than the mainline traffic, or when the on-ramp CAV and a mainline CAV enter into the control zone at the same time. 

The proposed hierarchical control approach overall works better than the first-in-first-out method in improving traffic operations. The experimental results show the superiority of the proposed hierarchical control approach. To this end, without repeating the detailed merging process exhaustively with the operational layer controller, an optimal merging sequence can also be established. Besides, considering a speed-adaptation time instant for an on-ramp vehicle can bring extra improvement in traffic operations even though the idea is not explicitly addressed in other researches. Preparing on-ramp vehicles to reach a merging or certain speed before establishing a merging sequence implicitly supports the idea of considering speed-adaptation time instant [19], [20]. 

The third-order vehicle dynamics model rests on a linearization approach to create a linear representation of a nonlinear longitudinal vehicle dynamics model [34]. The linearized model captures driveline dynamics, finite bandwidth of vehicle actuators, and time lag for the torque available at the tires to achieve a desired acceleration. The third-order vehicle dynamics model is preferred than the second-order model because it is closer to real vehicle behavior and brings reasonable control commands for real-world implementation [34]. Besides, parameter uncertainties in the vehicle dynamics model can be considered using the third-order vehicle dynamics model [16]. The tactical layer controller usually uses a large value, $0 . 5 ~ s$ or $1 \ s$ , larger than the actuator lag, as the time step to save computation time; thus, the third-order vehicle dynamics model is not necessary and the second-order vehicle dynamics model is employed. If for some automated vehicles, actuator lags are quite large, a third-order vehicle dynamics model can be used in the tactical layer controller to reduce the mismatch in vehicle dynamics models. Besides, a car-following mode and a cooperative merging mode are utilized by the tactical layer controller to generated actual 

accelerations based on analytical models rather than numerical optimization in the operational layer. These differences make the computation time of the tactical layer controller tractable. In all our experiments, these differences or mismatches do not contradict the feasibility and applicability of the tactical layer controller to generate optimal merging sequences. This finding may support other researchers to explore simpler optimal control methods to establish merging sequences under different market penetrations of CAVs. 

When one on-ramp vehicle exists and five mainline vehicles exist, with a looking-ahead horizon $T = 5 0 \ : s$ , the computation time of the tactical layer controller is $0 . 3 2 s$ . When the number of on-ramp vehicles increases to two, the computation of the tactical layer controller becomes $4 . 8 s$ when all the possible merging sequences and speed-adaptation time instants are evaluated. The incremental computation time is caused by the added numbers of possible combinations and the selected solution method: enumeration algorithm. If the merging sequences or speed-adaptation time instants can be restricted to limited choices according to experimental results, the computation time can be reduced. Besides, efficient solutions for mixed-integer programming problems may also reduce computation time, which is one of our future research directions. It takes the operational layer controller around 0.91 s to solve the problem of 6 vehicles with a time horizon $_ { \mathrm { ~ 6 ~ } s }$ . The computation time of the operational layer controller turns to be around $1 . 1 2 \ s$ when 7 vehicles are involved. In practical usage, the computation time of the operational layer controller should be considered when it is large. The computation time of the operational layer controller can be reduced with distributed model predictive control [38]. 

In our work, imperfect state observation/estimation is already included with a small state delay in the tactical layer. For our 135 experiments, a feedback delay is included, which means the tactical layer controller uses previous vehicular information to establish merging sequences and the merging sequences are established at $_ \mathrm { ~ 0 ~ } s$ , without using the designed feedback nature. The experimental results show that the established merging sequences are feasible. Besides, with feedback nature, the tactical layer controller has a self-correction mechanism already, though it may update at larger intervals, e.g. 5 to $1 0 ~ s$ . To this end, small disturbances in vehicular information do not likely change the feasibility of the established merging sequences. However, we cannot prove that feasibility is guaranteed with the finite number of experiments, especially when the state observation deviates largely from the ground truth. To this end, we add another mechanism in our control architecture. The additional function allows the operational layer controller to reject decisions from the tactical layer controller if no feasible solution is found for an on-ramp vehicle among $\Delta \hat { t }$ . If no feasible solution can be found by the operational controller under the current tactical command and the on-ramp vehicle is far away from the end of the acceleration lane, the operational layer controller then requests a new command from the tactical layer controller. Triggered by the rejection event, the tactical layer controller establishes new decisions before $\Delta \hat { t }$ . To address safety-critical situations where no feasible solution exists and the on-ramp vehicle is 

close to the end of the acceleration lane, the operational layer controller is given the autonomy to choose the next gap after the previous target gap for the on-ramp vehicle directly to accomplish merging. 

In the tactical layer, the Helly car-following model is employed to predict the future vehicular longitudinal accelerations of a CAV instead of using the operational layer controller. At this stage, all vehicles are assumed to be CAVs. However, our design can be extended to adapt to mixed traffic where human-driven vehicles coexist with CAVs. To include human-driven vehicles, reasonable car-following and lane-changing models can be assumed to represent the behaviors of human-driven vehicles for both the tactical and operational controllers to predict the future development of the surrounding traffic scene. Safety should be ensured at the operational layer controller. To ensure safety, the current and predicted inter-vehicle distances should be large enough for a lane changer to change lane as shown in (14). Besides, because the human-driven vehicles do not tend to cooperate to facilitate a lane changing process and their behaviors can not be perfectly modeled or predicted, a trade-off between merging efficiency and the risk to collide can be considered at the operational layer controller in the future. 

Noise in actuators or sensors may deteriorate the performance of the controllers to regulate vehicular motions. Noise in detected measurements can be filtered out with data fusion methods in the hierarchical architecture of the merging control system if a filter is added to the estimator. When the uncertainties in actuators cause actuator lag to vary in a small range of values, the deterioration is small. However, when the uncertainties bring a large range of values of the actuator lag, a robust control method is needed to ensure the string stability of the operational layer controller [16]. 

Because the first-in-first-out method is common and easy to be implemented, we give recommendations for using the firstin-first-out method to get the same or similar decisions as or to the proposed hierarchical control approach. To improve traffic operations, traffic operators and researchers can use those recommendations when using the first-in-first-out method to establish merging sequences. One point should not be neglected that optimal merging sequences are established based on a certain performance indicator. For different performance indicators, different merging sequences may be optimal. 

# VII. CONCLUSIONS AND FUTURE RESEARCH

This paper puts forward a hierarchical control approach for efficient and safe on-ramp merging of Connected Automated Vehicles (CAVs). A tactical layer controller uses a car-following and a cooperative merging mode to represent the regimes to generate vehicular trajectories during the merging process and gives optimal tactical decisions that bring efficient traffic operations. During the optimization, on-ramp vehicles are allowed to drive with their desired speeds for certain time periods respectively before they start to adapt their speeds and positions to prepare merging into the target gaps respectively. An operational layer controller is designed based on model predictive control. It employs a third-order vehicle 

dynamics model, regulates desired accelerations of CAVs, and gives commands on the lane-changing executions of the on-ramp vehicles based on current and predicted inter-vehicle time gaps. The performance of the proposed hierarchical control approach and a benchmark control approach, using the first-in-first-out method to determine merging sequences, is tested under 135 scenarios with different initial conditions and desired time gap settings. Experimental results show that the proposed hierarchical control approach outperforms the benchmark control method and the superiority is kept when multiple on-ramp vehicles exist. 

We conclude that different settings of initial conditions and the desired time gap do affect an optimal combination of a merging sequence and time instants when on-ramp CAVs start to adapt their speeds and positions to prepare merging into the target gaps respectively. The proposed hierarchical control approach brings pronounced improvements in traffic operations when the initial speed of the on-ramp vehicle is significantly lower than the mainline traffic, when the desired time gap is small, such as $0 . 6 s$ , or when an on-ramp CAV and a mainline CAV enter into the control zone at the same time. Allowing on-ramp vehicles to travel with their desired speeds for certain time periods respectively can bring improvements in traffic operations. 

After comparing the simulation results of the proposed hierarchical control approach and the benchmark on-ramp merging method, we give recommendations to use the firstin-first-out method to establish merging sequences. The main idea of the recommendations is to adapt the initial speed and position of the on-ramp CAV to meet conditions where the first-in-first-out method probably gives the same decision as the tactical controller of the proposed hierarchical control approach. 

The future research will dive into merging with multiple main lanes. The cooperative merging strategy should be extended to allow CAVs on the outermost main lane to perform courtesy lane change. The future research will also focus on on-ramp merging under mixed traffic by extending the proposed hierarchical control approach. Macroscopic characteristics of traffic flow will be analyzed to evaluate the benefits of our design on traffic operations. 

# APPENDIX A A POLYNOMIAL EQUATION FOR A VEHICLE’S LATERAL MOTION DURING THE LANE CHANGING MANEUVER

$$
y _ {r} (t) = \left\{ \begin{array}{l l} y _ {r} \left(t _ {0}\right) & t <   t ^ {l}, \xi_ {r} (t) = 0 \\ f (t) & t ^ {l} \leq t \leq t ^ {l} + t _ {m}, \xi_ {r} \left(t ^ {l}\right) = 1 \\ y _ {r} \left(t _ {0}\right) + h & t > t ^ {l} + t _ {m} \end{array} \right. \tag {21}
$$

$$
\begin{array}{l} f (t) = \frac {- 6 h}{t _ {m} ^ {5}} \cdot (t - t _ {0}) ^ {5} + \frac {1 5 h}{t _ {m} ^ {4}} \cdot (t - t _ {0}) ^ {4} \\ + \frac {- 1 0 h}{t _ {m} ^ {3}} \cdot (t - t _ {0}) ^ {3} + y _ {r} (t _ {0}) \tag {22} \\ \end{array}
$$

where, $h$ denotes maximum lateral position variation whose absolute value equals to lane width. For changing lane to the left side of the road, $h$ is a negative value. 

# REFERENCES



[1] V. Milanes, J. Godoy, J. Villagra, and J. Perez, “Automated on-ramp merging system for congested traffic situations,” IEEE Trans. Intell. Transp. Syst., vol. 12, no. 2, pp. 500–508, Jun. 2011. 





[2] R. Pueboobpaphan, F. Liu, and B. van Arem, “The impacts of a communication based merging assistant on traffic flows of manual and equipped vehicles at an on-ramp using traffic flow simulation,” in Proc. 13th Int. IEEE Conf. Intell. Transp. Syst., Sep. 2010, pp. 1468–1473. 





[3] A. Morales and H. Nijmeijer, “Merging strategy for vehicles by applying cooperative tracking control,” IEEE Trans. Intell. Transp. Syst., vol. 17, no. 12, pp. 3423–3433, Dec. 2016. 





[4] Z. Li, L. Elefteriadou, and S. Ranka, “Signal control optimization for automated vehicles at isolated signalized intersections,” Transp. Res. C, Emerg. Technol., vol. 49, pp. 1–18, Dec. 2014. 





[5] Y. Feng, K. L. Head, S. Khoshmagham, and M. Zamanipour, “A realtime adaptive signal control in a connected vehicle environment,” Transp. Res. C, Emerg. Technol., vol. 55, pp. 460–473, Jun. 2015. 





[6] L. Chen and C. Englund, “Cooperative intersection management: A survey,” IEEE Trans. Intell. Transp. Syst., vol. 17, no. 2, pp. 570–586, Feb. 2016. 





[7] K. Yang, S. I. Guler, and M. Menendez, “Isolated intersection control for various levels of vehicle technology: Conventional, connected, and automated vehicles,” Transp. Res. C, Emerg. Technol., vol. 72, pp. 109–129, Nov. 2016. 





[8] B. van Arem, C. J. G. van Driel, and R. Visser, “The impact of cooperative adaptive cruise control on traffic-flow characteristics,” IEEE Trans. Intell. Transp. Syst., vol. 7, no. 4, pp. 429–436, Dec. 2006. 





[9] L. Jin, M. Ciˇ ˇ ci´c, S. Amin, and K. H. Johansson, “Modeling the impact of vehicle platooning on highway congestion,” in Proc. 21st Int. Conf. Hybrid Syst., Comput. Control (Part CPS Week), Apr. 2018, pp. 237–246. 





[10] I. A. Ntousakis, I. K. Nikolos, and M. Papageorgiou, “Optimal vehicle trajectory planning in the context of cooperative merging on highways,” Transp. Res. C, Emerg. Technol., vol. 71, pp. 464–488, Oct. 2016. 





[11] J. Rios-Torres and A. A. Malikopoulos, “Automated and cooperative vehicle merging at highway on-ramps,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 4, pp. 780–789, Apr. 2017. 





[12] S. E. Shladover, D. Su, and X.-Y. Lu, “Impacts of cooperative adaptive cruise control on freeway traffic flow,” Transp. Res. Rec., J. Transp. Res. Board, vol. 2324, no. 1, pp. 63–70, Jan. 2012. 





[13] J. Rios-Torres and A. A. Malikopoulos, “A survey on the coordination of connected and automated vehicles at intersections and merging at highway on-ramps,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 5, pp. 1066–1077, May 2017. 





[14] M. Zhou, X. Qu, and S. Jin, “On the impact of cooperative autonomous vehicles in improving freeway merging: A modified intelligent driver model-based approach,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 6, pp. 1422–1428, Jun. 2017. 





[15] M. Wang, W. Daamen, S. P. Hoogendoorn, and B. van Arem, “Rolling horizon control framework for driver assistance systems—Part II: Cooperative sensing and cooperative control,” Transp. Res. C, Emerg. Technol., vol. 40, pp. 290–311, Mar. 2014. 





[16] N. Chen, M. Wang, T. Alkim, and B. van Arem, “A robust longitudinal control strategy of platoons under model uncertainties and time delays,” J. Adv. Transp., vol. 2018, Jan. 2018, Art. no. 9852721. 





[17] Y. Wang, G. Lu, W. E, G. Yu, D. Tian, and W. Tang, “Automated onramp merging control algorithm based on Internet-connected vehicles,” IET Intell. Transp. Syst., vol. 7, no. 4, pp. 371–379, Dec. 2013. 





[18] T. Awal, L. Kulik, and K. Ramamohanrao, “Optimal traffic merging strategy for communication- and sensor-enabled vehicles,” in Proc. 16th Int. IEEE Conf. Intell. Transp. Syst. (ITSC ), Oct. 2013, pp. 1468–1474. 





[19] G. Schmidt and B. Posch, “A two-layer control scheme for merging of automated vehicles,” in Proc. 22nd IEEE Conf. Decis. Control, Dec. 1983, pp. 495–500. 





[20] B. Posch and G. Schmidt, “A comprehensive control concept for merging of automated vehicles under a broad class of traffic conditions,” IFAC Proc. Volumes, vol. 16, no. 4, pp. 187–194, Apr. 1983. 





[21] R. Scarinci, B. Heydecker, and A. Hegyi, “Analysis of traffic performance of a merging assistant strategy using cooperative vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 16, no. 4, pp. 2094–2103, Aug. 2015. 





[22] D. Marinescu, J. Curn, M. Bouroche, and V. Cahill, “On-ramp traffic merging using cooperative intelligent vehicles: A slot-based approach,” in Proc. 15th Int. IEEE Conf. Intell. Transp. Syst., Sep. 2012, pp. 900–906. 





[23] M. Athans, “A unified approach to the vehicle-merging problem,” Transp. Res., vol. 3, no. 1, pp. 123–133, Apr. 1969. 





[24] W. Cao, M. Mukai, T. Kawabe, H. Nishira, and N. Fujiki, “Gap selection and path generation during merging maneuver of automobile using realtime optimization,” SICE J. Control, Meas., Syst. Integr., vol. 7, no. 4, pp. 227–236, 2014. 





[25] W. Zhao, R. Liu, and D. Ngoduy, “A bilevel programming model for autonomous intersection control and trajectory planning,” Transportmetrica A, Transp. Sci., to be published, doi: 10.1080/23249935.2018.1563921. 





[26] L. Xu, J. Lu, B. Ran, F. Yang, and J. Zhang, “Cooperative merging strategy for connected vehicles at highway on-ramps,” J. Transp. Eng., A, Syst., vol. 145, no. 6, Jun. 2019, Art. no. 04019022. 





[27] A. Duret, M. Wang, and A. Ladino, “A hierarchical approach for splitting truck platoons near network discontinuities,” Transp. Res. Proc., vol. 38, pp. 627–646, Feb. 2019. 





[28] S. Samiee, S. Azadi, R. Kazemi, and A. Eichberger, “Towards a decisionmaking algorithm for automatic lane change manoeuvre considering traffic dynamics,” PROMET Traffic Transp., vol. 28, no. 2, pp. 91–103, Apr. 2016. 





[29] M. Wang, W. Daamen, S. P. Hoogendoorn, and B. van Arem, “Rolling horizon control framework for driver assistance systems.—Part I: Mathematical formulation and non-cooperative systems,” Transp. Res. C, Emerg. Technol., vol. 40, pp. 271–289, Mar. 2014. 





[30] M. Brackstone and M. McDonald, “Car-following: A historical review,” Transp. Res. F, Traffic Psychol. Behav., vol. 2, no. 4, pp. 181–196, Dec. 1999. 





[31] N. Chen, M. Wang, T. Alkim, and B. Van Arem, “A flexible strategy for efficient merging maneuvers of connected automated vehicles,” in Proc. CICTP, Jul. 2018, pp. 46–55. 





[32] S. Sheikholeslam and C. A. Desoer, “Longitudinal control of a platoon of vehicles with no communication of lead vehicle information: A system level study,” IEEE Trans. Veh. Technol., vol. 42, no. 4, pp. 546–554, Nov. 1993. 





[33] C.-Y. Liang and H. Peng, “Optimal adaptive cruise control with guaranteed string stability,” Vehicle Syst. Dyn., vol. 32, nos. 4–5, pp. 313–330, Nov. 1999. 





[34] M. Wang, S. P. Hoogendoorn, W. Daamen, B. van Arem, B. Shyrokau, and R. Happee, “Delay-compensating strategy to enhance string stability of adaptive cruise controlled vehicles,” Transportmetrica B, Transp. Dyn., vol. 6, no. 3, pp. 211–229, Jul. 2018. 





[35] M. Wang, S. P. Hoogendoorn, W. Daamen, B. van Arem, and R. Happee, “Game theoretic approach for predictive lane-changing and car-following control,” Transp. Res. C, Emerg. Technol., vol. 58, pp. 73–92, Sep. 2015. 





[36] L. Xiao, M. Wang, W. Schakel, and B. van Arem, “Unravelling effects of cooperative adaptive cruise control deactivation on traffic flow characteristics at merging bottlenecks,” Transp. Res. C, Emerg. Technol., vol. 96, pp. 380–397, Nov. 2018. 





[37] J. L. Garriga and M. Soroush, “Model predictive control tuning methods: A review,” Ind. Eng. Chem. Res., vol. 49, no. 8, pp. 3505–3515, Apr. 2010. 





[38] E. Camponogara, D. Jia, B. H. Krogh, and S. Talukdar, “Distributed model predictive control,” IEEE Control Syst., vol. 22, no. 1, pp. 44–52, Feb. 2002. 



![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/097625b7fbac169cb27079a03f6dd1ab2a2429ad04ab4983f6c40d3685b1a5b4.jpg)


Bart van Arem (Senior Member, IEEE) received the M.Sc. and Ph.D. degrees in applied mathematics from the University of Twente, Enschede, The Netherlands, in 1986 and 1990, respectively. From 1992 to 2009, he was a Researcher and a Program Manager with TNO, working on intelligent transport systems, in which he has been active in various national and international projects. From 2009 to 2018, he was the Chair Professor of transport modeling with the Department of Transport and Planning, Delft University of Technology, The 

Netherlands, where he is currently a full-time Professor, focusing on the impact of intelligent transport systems on mobility. His research interests include transport modeling and intelligent vehicle systems. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/680081577a35cc0e7035710e8da1bc5664349b1ee2594b4be73d89bfd543c449.jpg)


Tom Alkim is currently a Policy Officer Connected and Automated driving with the European Commission, Directorate General Research and Innovation. He has over 20 years of experience in the field of ITS, C-ITS and automated driving and was a constant factor for the Dutch Ministry of Infrastructure and Water Management with Rijkswaterstaat. He was a part of the core team that was responsible for the Declaration of Amsterdam and the European Truck Platooning Challenge during the Dutch EU presidency in 2016. Since December 2019, he has 

been working with the European Commission on advancing Connected and Automated Driving in a responsible manner to deliver societal benefits. In this capacity, he was also a co-organizer of the Second European Conference on Connected and Automated Driving which took place in April 2019 (connectedautomateddriving.eu/eucad2019). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/99ab5b4e9d85db1794c4f15a13106fd94d5e334b6ccb0d1041edb5ec9544240c.jpg)


Na Chen received the B.Sc. degree in traffic and transportation and the M.Sc. degree in traffic and transportation planning and management from Beijing Jiaotong University, Beijing, China, in 2013 and 2016, respectively. She is currently the Ph.D. Researcher with the Delft University of Technology, under the supervision of Dr. Bart van Arem and Dr. Meng Wang. Her research interests include intelligent vehicle systems and traffic management. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/ab809eec-84e0-46be-973e-13f6d5d0c972/b66ec2306074e784e3f8ea9b9c00721b8cd7509d26c9e77a198f672187c11cb4.jpg)


Meng Wang (Member, IEEE) received the M.Sc. degree in transportation engineering from the Research Institute of Highway, China, in 2006, and the Ph.D. degree in transport and planning from the Delft University of Technology, The Netherlands, in 2014. From 2014 to 2015, he worked as a Post-Doctoral Researcher with the Department of BioMechanical Engineering, Delft University of Technology. He is currently an Assistant Professor with the Department of Transport and Planning, Delft University of Technology. His main research 

interests include driver behavior modeling and control approaches for intelligent vehicle systems. 