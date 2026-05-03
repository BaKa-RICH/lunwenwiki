# Automated and Cooperative Vehicle Merging at Highway On-Ramps

Jackeline Rios-Torres, Member, IEEE, and Andreas A. Malikopoulos, Member, IEEE 

Abstract—Recognition of necessities of connected and automated vehicles (CAVs) is gaining momentum. CAVs can improve both transportation network efficiency and safety through control algorithms that can harmonically use all existing information to coordinate the vehicles. This paper addresses the problem of optimally coordinating CAVs at merging roadways to achieve smooth traffic flow without stop-and-go driving. We present an optimization framework and an analytical closed-form solution that allows online coordination of vehicles at merging zones. The effectiveness of the efficiency of the proposed solution is validated through a simulation, and it is shown that coordination of vehicles can significantly reduce both fuel consumption and travel time. 

Index Terms—Connected and automated vehicles, cooperative driving, cooperative merging control, highway on-ramps, merging highways, vehicle coordination. 

# I. INTRODUCTION

# A. Motivation

HE widespread use of the automobile is the source of traffic congestion and increasing traffic accidents. Although driver responses to various disturbances can cause congestion [1], intersections and merging roadways are the primary sources of bottlenecks [2]. In 2014, congestion caused people in urban areas to spend 6.9 billion hours more on the road and to purchase an extra 3.1 billion gallons of fuel, resulting in a total cost estimated at $\$ 160$ billion [3]. Moreover, traffic congestion can produce driver discomfort, distraction, and frustration, which may encourage more aggressive driving behavior [4] and further slow the process of recovering free traffic flow [5]. 

Connected and automated vehicles (CAVs) can provide shorter gaps between vehicles and faster responses while improving highway capacity. Several efforts reported in the literature have aimed at enhancing our understanding of the potential benefits 

Manuscript received August 10, 2015; revised December 13, 2015, February 25, 2016, April 20, 2016, and June 3, 2016; accepted June 25, 2016. Date of publication August 5, 2016; date of current version March 27, 2017. This manuscript has been authored by UT-Battelle, LLC, under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy (DOE). The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a nonexclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow others to do so, for United States Government purposes. This research was supported in part by the Laboratory Directed Research and Development Program of the Oak Ridge National Laboratory, Oak Ridge, TN 37831 USA, managed by UT-Battelle, LLC, for the DOE, and in part by DOE’s SMART Mobility Initiative. The Associate Editor for this paper was V. Punzo. 

The authors are with the Energy and Transportation Science Division, Oak Ridge National Laboratory, Oak Ridge, TN 37831 USA (e-mail: andreas@ ornl.gov). 

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org. 

Digital Object Identifier 10.1109/TITS.2016.2587582 

of connected vehicle technologies. Li, Wen and Yao [6] recently surveyed relevant research on improving transportation safety and efficiency using traffic lights and vehicle-to-infrastructure communication. There has been also a significant amount of work in developing approaches for improving both safety and traffic flow through vehicle coordination at intersections and merging roadways. A survey of the research efforts in this area that have been reported in the literature to date can be found in [7]. 

# B. Literature Review

Research efforts using either centralized or decentralized approaches have focused on coordinating CAVs in specific traffic scenarios, e.g., intersections, merging highways, etc. The overarching goal of such efforts is to yield a smooth traffic flow avoiding stop-and-go driving. In this paper, we categorize an approach as centralized if there is at least one task in the system that is globally decided for all vehicles by a single central controller. In decentralized approaches, the vehicles are treated as autonomous agents that attempt, through strategic interaction, to maximize their own efficiency. In this framework, each vehicle obtains information from other vehicles and roadside infrastructure to optimize specific performance criteria, e.g., efficiency, travel time, while satisfying the transportation system’s physical constraints, e.g., stop signs, traffic signals. The majority of such efforts have been concentrated on intersections and merging highways. 

1) Automated Intersection Control: In 2004, Dresner and Stone [8] proposed an approach for automated vehicle intersection control based on the use of a reservation algorithm. Since then, numerous approaches have been reported in the literature to achieve safe and efficient control of traffic through intersections using centralized and decentralized control algorithms. Dresner and Stone [9], Au and Stone [10], de la Fortelle [11], Huang et al. [12] and Zhang et al. [13] proposed the use of reservation schemes. In general, in this approach there is a centralized controller, or intersection manager, that coordinates the reservation, or crossing schedule, based on the requests and information received from the vehicles located inside the communication range. The intersection is divided into cells or points, which are to be assigned, or reserved, for only one vehicle at each instant of time to avoid collisions. The main challenges in this case are associated with the heavy communication requirements and the possible occurrence of deadlocks. The communication becomes a critical issue, particularly when vehicles are required to communicate several times with the central controller until their reservation request is approved. 

Other approaches have focused on the formulation of an optimization problem in which the objective function involves the travel time [14]–[19]. Lee and Park [20] proposed a different approach based on minimizing the overlap in the position of vehicles inside the intersection rather than arrival time, where a centralized controller adjusts the vehicle trajectories to avoid two vehicles crossing the intersection at the same time. This work was later extended to the case of an urban corridor [21]. Miculescu and Karaman [22] used queuing theory and they modeled the problem as a polling system with two queues and one server that determines the sequence of times assigned to the vehicles on each road. 

In decentralized control, each vehicle determines its own control policy based on the information received from the other vehicles on the road, or a coordinator. One of the main challenges faced in the implementation of decentralized approaches is the possibility of having deadlocks in the solutions as a consequence of the use of local information. Milanes et al. [23] used fuzzy logic to design a controller that allows a fully automated vehicle to yield to an incoming vehicle in the conflicting road or to cross, if it is feasible and collision risk is not present. Alonso et al. [24] proposed two conflict resolution schemes in which an autonomous vehicle could make a decision about the appropriate crossing schedule to avoid collision with other manually driven vehicles on the road. Colombo and Del Vecchio [25] constructed the invariant set for the control inputs that avoids collisions. The problem is then translated into a scheduling problem for exact and approximated solutions. A decentralized optimal control framework whose solution yields for each vehicle the optimal acceleration/deceleration at any time in the sense of minimizing fuel consumption was presented in [26]. The solution, when it exists, allows the vehicles to cross the intersections without the use of traffic lights, without creating congestion on the connecting road, and under the hard safety constraint of collision avoidance. Makarem et al. [27] used MPC to solve the decentralized problem where each vehicle defines its constraints by using the information it receives from other vehicles and solves a linear quadratic optimal control problem accordingly. MPC has been also used by Kim and Kumar [28] to solve a local optimization problem. 

2) Automated Highway Merging Control: Ramp metering is a common method used to regulate the flow of vehicles merging into freeways to decrease traffic congestion [29]. Although it has been shown that ramp metering can aim at improving the overall traffic flow and safety on freeways, there are several challenges associated with the interference between the traffic flows on adjacent roads. Different approaches to address these challenges, including the use of feedback control theory [30]–[34], optimal control [35]–[37] and heuristic algorithms [38], [39], have been reported in the literature to date [40]. 

Given the recent technological developments, several research efforts have considered approaches to achieve safe and efficient coordination of merging maneuvers with the intention to avoid severe stop-and-go driving. One of the very early efforts in this direction was proposed in 1969 by Athans [41]. Assuming a given merging sequence, Athans formulated the merging problem as a linear optimal regulator, proposed by Levine and Athans [42] to control a single string of vehicles, 

with the aim of minimizing the speed errors that will affect the desired headway between each consecutive pair of vehicles. Later, Schmidt and Posch [43] proposed a two-layer control scheme based on heuristic rules that were derived from observations of the non-linear system dynamics behavior. Similar to the approach proposed by Athans [41], Awal, Kilik and Ramamohanrao [44] developed an algorithm that starts by computing the optimal merging sequence to achieve reduced merging times for a group of vehicles that are closer to the merging point. 

Kachroo and Li [45] in 1997 used sliding mode control and designed longitudinal and lateral controllers to guide the vehicle until the merging maneuver is completed. The same year, Antoniotti et al. [46], [47] proposed a decentralized hybrid controller for keeping a safe headway between the vehicles in the merging process. In their work, there is no vehicle to vehicle communication but each vehicle decides the time to merge, yield, or exit the freeway based on the local information received from its own sensors. Ran et al. [48] used three levels of assistance for the merging process to select the available gap in the main road for the vehicle that is entering the merging ramp. Uno et al. [49] used the concept of virtual vehicle platooning for autonomous merging control. In this approach, a virtual vehicle is mapped onto the main road before the actual merging occurs. This concept was explored further by Lu and Hedrick [50] and Lu et al. [51], where a central controller identifies and interchanges relevant information with the vehicles that will be involved in the merging maneuver and each vehicle assumes its own control actions to satisfy the assigned time and reference speed. 

Raravi et al. [52] proposed an approach in which, once a merging sequence have been defined, an optimization problem is solved to find the minimum time that each vehicle in the control area will take to reach the intersection. Milanes et al. [53] presented a fuzzy controller that uses the local information received to decide the accelerator and brake pedal position for each vehicle to achieve a smooth merging maneuver. The approach proposed by Marinescu et al. [54] builds upon the concept of slot-based traffic management, in which the intelligent vehicles drive inside a virtual slot. Ntousakis et al. [55] proposed two decentralized algorithms for automated merging control in which each vehicle uses information of the vehicles inside a cooperation area to determine the appropriate sequence to merge into the main road. Results showed that both algorithms performed safely and the traffic flow was kept at reasonable rates. More recently, the concept of cooperative merging, in which the vehicles on the main road adjust its speed to facilitate the merging process of the vehicle attempting to merge, was presented in [56]. 

# C. Contribution of the Paper

Although previous research reported in the literature has aimed at enhancing our understanding of coordinating vehicles either at intersections, or merging roadways, deriving online an optimal closed-form solution for vehicle coordination in terms of fuel consumption still remains a challenging control problem. This paper has two main objectives: (1) to formulate 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/7f7445efb3dffb355762c7256674a66555ed05f5c47775af28213887d661eca6.jpg)



Fig. 1. Merging roads with connected and automated vehicles controlled by a centralized controller.


the problem of optimal vehicle coordination at merging roadways in terms of fuel consumption under the hard constraint of collision avoidance and (2) to derive online a closed-form solution in a centralized fashion. A preliminary effort in this direction was reported in [57]. 

The contributions of this paper are (1) an analytical, closedform solution using Hamiltonian analysis, and (2) the validation of the optimal solution through simulation and quantification of the implications for fuel consumption and travel time. 

# D. Organization of the Paper

The structure of the paper is as follows. In Section II we formulate the problem of vehicle coordination at merging roadways. In Section III we provide the analytical solution. Finally, we provide simulation results in Section IV and concluding remarks in Section V. 

# II. PROBLEM FORMULATION

Merging roadways are among the primary sources of bottlenecks generating traffic congestion resulting in severe stopand-go driving and thus excessive fuel consumption. Fig. 1 illustrates a common scenario in which a secondary one-lane road merges onto a main one-lane road. Typically, the vehicles on the secondary road have to yield to the vehicles on the main road and wait until the safest opportunity to merge onto the main road. On highly congested roads the merging process is even more tedious and undesirable stop-and-go traffic flow becomes unavoidable. 

We consider the merging roadways of Fig. 1. The region of potential lateral collision of the vehicles is called merging zone and has a length S. There is also a control zone and a centralized controller that can control the vehicles traveling inside the control zone. The distance from the entry of the control zone until the entry of the merging zone is $L$ . 

# A. Modeling Framework

We consider an increasing number of CAVs $N ( t ) \in \mathbb { N }$ , where $t \in \mathbb { R }$ is the time, entering the control zone (see Fig. 1). When a vehicle reaches the control zone at some instant $t$ , the con-

troller assigns a unique identity $i = N ( t ) + 1$ that is an integer corresponding to the location of the CAV in a first-in-first-out (FIFO) queue for the control zone. If two, or more vehicles enter the control zone at the same time, then the controller selects randomly their position in the queue. The number $N ( t )$ can be reset only if no vehicles are inside the control zone. 

Let $\mathcal { N } ( t ) = \{ 1 , . . . , N ( t ) \}$ , be the queue associated with the control zone. We model each vehicle i, $i \in \mathcal { N } ( t )$ , as a point mass moving along a specified lane with a state equation 

$$
\dot {x _ {i}} = f (t, x _ {i}, u _ {i}), \quad x _ {i} \left(t _ {i} ^ {0}\right) = x _ {i} ^ {0} \tag {1}
$$

where $t \in \mathbb { R } ^ { + }$ is the time, $x _ { i } ( t )$ , $u _ { i } ( t )$ are the state of the vehicle and control input, $t _ { i } ^ { 0 }$ is the time that vehicle $i$ enters the control zone, and $x _ { i } ^ { 0 }$ is the value of the initial state. For simplicity, we assume that each vehicle is governed by a second order dynamics 

$$
\dot {p} _ {i} = v _ {i} (t) \tag {2}
$$

$$
\dot {v} _ {i} = u _ {i} (t)
$$

where $p _ { i } ( t ) \in \mathcal { P } _ { i }$ , $v _ { i } ( t ) \in \mathcal { V } _ { i }$ , and $u _ { i } ( t ) \in \mathcal { U } _ { i }$ denote the position, speed and acceleration/deceleration (control input) of each vehicle $i$ . Let $x _ { i } ( t ) = [ p _ { i } ( t ) v _ { i } ( t ) ] ^ { T }$ denote the state of each vehicle $i$ , with initial value $x _ { i } ^ { 0 } = \left[ 0 v _ { i } ^ { 0 } \right] ^ { T }$ , taking values in the state space $\mathcal { X } _ { i } = \mathcal { P } _ { i } \times \mathcal { V } _ { i }$ . The sets $\mathcal { P } _ { i }$ , $\nu _ { i }$ , and $\mathcal { U } _ { i }$ , $i \in \mathcal { N } ( t )$ , are complete and totally bounded subsets of $\mathbb { R }$ . The state space $\mathcal { X } _ { i }$ for each vehicle $i$ is closed with respect to the induced topology on $\mathcal { P } _ { i } \times \mathcal { V } _ { i }$ and thus, it is compact. 

# B. Optimization Problem Formulation

We seek to address the problem of coordinating online an increasing number of CAVs on two merging roadways. The objective is to derive an analytical solution that yields the optimal control input at any time in terms of fuel consumption. For the latter, we use the polynomial metamodel proposed in [58] that yields vehicle fuel consumption as a function of the speed, $v$ , and control input, $u$ 

$$
\dot {f} _ {v} = \dot {f} _ {\text {c r u i s e}} + \dot {f} _ {\text {a c c e l}} \tag {3}
$$

where $t \in \mathbb { R } ^ { + }$ is the time, $\dot { f } _ { \mathrm { c r u i s e } } = q _ { 0 } + q _ { 1 } \cdot v ( t ) + q _ { 2 } .$ $v ^ { 2 } ( t ) + q _ { 3 } \cdot v ^ { 3 } ( t )$ estimates the fuel consumed by a vehicle traveling at a constant speed $v ( t )$ , and ${ \dot { f } } _ { \mathrm { a c c e l } } = u ( t ) \cdot ( r _ { 0 } + r _ { 1 } \cdot$ $\boldsymbol { v } ( t ) + \boldsymbol { r } _ { 2 } \cdot \boldsymbol { v } ( t ) ^ { 2 } )$ is the additional fuel consumption caused by acceleration $u ( t )$ . The polynomial coefficients $q _ { n }$ , $n = 0 , \ldots , 3$ , and $r _ { m }$ $r _ { m } , m = 0 , 1 , 2$ are calculated from experimental data. The model does not yield fuel consumption for braking, i.e., when $u ( t )$ takes negative values. However, braking is not generally a major concern because the deceleration fuel cutoff (DFCO) in vehicles terminates fuel injection at braking and the engine does not consume any fuel. DFCO is enabled when the driver hits the brake pedal although, in some cases, it is also enabled when the driver’s foot is off the accelerator pedal. Fuel automatically begins flowing back to the engine when the driver accelerates again. Therefore, in our approach braking is directly related to zero fuel consumption. 

For the vehicle parameters reported in [58], where the vehicle mass is $M _ { v } = 1 { , } 2 0 0 ~ \mathrm { k g }$ , the drag coefficient is $C _ { D } = 0 . 3 2$ , 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/b12c348595a23683d803f9e68f8e3a1b5181edc76df45c770f63e8cfb0d44839.jpg)



Fig. 2. Fuel consumption model.


the air density is $\rho _ { a } = 1 . 1 8 4 \mathrm { k m / m ^ { 3 } }$ , the frontal area is $A _ { f } =$ $2 . 5 \ \mathrm { m ^ { 2 } }$ , and the rolling resistance coefficient is $\mu = 0 . 0 1 5$ , the polynomial coefficients are: $q _ { 0 } = 0 . 1 5 6 9$ , $q _ { 1 } = 2 . 4 5 \cdot 1 0 ^ { - 2 }$ , $q _ { 2 } = - 7 . 4 1 5 \cdot 1 0 ^ { - 4 }$ , $q _ { 3 } = 5 . 9 7 5 \cdot 1 0 ^ { - 5 } .$ , $r _ { 0 } = 0 . 0 7 2 2 4$ , $r _ { 1 } =$ $9 . 6 8 1 \cdot 1 0 ^ { - 2 }$ , and $r _ { 2 } = 1 . 0 7 5 \cdot 1 0 ^ { - 3 }$ . Fig. 2 illustrates the fuel consumption variation with respect to the vehicle speed and acceleration. Evidently, there is a monotonic behavior of fuel consumption with respect to the acceleration, which becomes even more significant at higher vehicle speeds. In general, by minimizing acceleration we essentially minimize transient engine operation that has direct benefits in fuel consumption since internal combustion engines are optimized over steady state operating points (constant torque and speed) [59]. 

To ensure that the control input and vehicle speed are within a given admissible range, the following constraints are imposed. 

$$
\begin{array}{l} u _ {\min } \leq u _ {i} (t) \leq u _ {\max }, \quad \text {a n d} \\ 0 \leq v _ {\min } \leq v _ {i} (t) \leq v _ {\max }, \quad \forall t \in \left[ t _ {i} ^ {0}, t _ {i} ^ {f} \right] \tag {4} \\ \end{array}
$$

where $u _ { \mathrm { m i n } }$ , $u _ { \mathrm { m a x } }$ are the minimum deceleration and maximum acceleration, and $v _ { \operatorname* { m i n } } , v _ { \operatorname* { m a x } }$ are the minimum and maximum speed limits respectively, $t _ { i } ^ { 0 }$ is the time that vehicle $i$ enters the control zone, and $t _ { i } ^ { f }$ is the time that vehicle $i$ exits the merging zone. 

To ensure the absence of rear-end collision of two consecutive vehicles traveling on the same lane, the position of the preceding vehicle should be greater than, or equal to the position of the following vehicle plus a predefined safe distance $\delta$ . Apparently, when there is only one vehicle in the control zone there is no concern of either rearend collision, or lateral collision in the merging zone. Thus the following definition refer to the case when the queue $\mathcal { N } ( t )$ contains more than one vehicle. 

Definition 2.1: For each vehicle $i$ , we define the control interval $R _ { i }$ as 

$$
\begin{array}{l} R _ {i} \triangleq \left\{u _ {i} (t) \in [ u _ {\min }, u _ {\max } ] \mid p _ {i} (t) \leq p _ {k} (t) - \delta , v _ {i} (t) \in [ v _ {\min }, v _ {\max } ], \right. \\ \left. \forall i \in \mathcal {N} (t), | \mathcal {N} (t) | > 1, \quad \forall t \in \left[ t _ {i} ^ {0}, t _ {i} ^ {f} \right] \right\} \tag {5} \\ \end{array}
$$

where vehicle $k$ is immediately ahead of $i$ on the same road. 

Definition 2.2: For each vehicle $i$ , we define the set $\Gamma _ { i }$ as the set of all positions along the lane where a lateral collision is possible, namely 

$$
\begin{array}{l} \Gamma_ {i} \triangleq \left\{p _ {i} (t) \mid p _ {i} (t) \in [ L, L + S ], \quad \forall i \in \mathcal {N} (t), \right. \\ \left. \left| \mathcal {N} (t) \right| > 1, \quad \forall t \in \left[ t _ {i} ^ {0}, t _ {i} ^ {f} \right] \right\}. \tag {6} \\ \end{array}
$$

To avoid lateral collision for any two vehicles $i$ and $j$ on different roads, the following constraint should hold 

$$
\Gamma_ {i} \bigcap \Gamma_ {j} = \varnothing , \quad \forall t \in \left[ t _ {i} ^ {0}, t _ {i} ^ {f} \right]. \tag {7}
$$

The above constraint implies that only one vehicle, at a time, can be crossing the merging zone. If the length of the merging zone is long, then this constraint might not be realistic resulting in dissipating space and capacity of the road. However, the constraint is not restrictive in the problem formulation and it can be modified appropriately as described in the following section. 

We impose the following assumption that is intended to enhance safety awareness. 

Assumption 2.3: The vehicle speed inside the merging zone is constant. 

We consider the problem of minimizing the control input at any time for each vehicle from the time $t _ { i } ^ { 0 }$ it enters the control zone until the time $t _ { i } ^ { m }$ that enters the merging zone while reducing the gaps between the vehicles, under the hard safety constraints to avoid rear-end and lateral collision. The control problem of coordinating $N ( t )$ vehicles can be formulated as 

$$
\begin{array}{l} \min  _ {u _ {i} \in \mathcal {R} _ {i}} \left(w _ {1} \frac {1}{2} \sum_ {i = 1} ^ {N (t)} \int_ {t _ {i} ^ {0}} ^ {t _ {i} ^ {f}} u _ {i} ^ {2} (t) d t \right. \\ \left. + w _ {2} \sum_ {i = 2} ^ {N (t)} \left| t _ {i} ^ {m} \left(u _ {(1: i)} (t)\right) - t _ {i - 1} ^ {m} \left(u _ {(1: i - 1)} (t)\right) \right|\right) \\ \end{array}
$$

Subject to : (2), ∀ i ∈ N (t) 

$$
(7), \quad \forall i, j \in \mathcal {N} (t), i \neq j \tag {8}
$$

where $w _ { 1 } , w _ { 2 }$ are weighting factors that normalize the two terms in (8). Based on the Assumption (2.3), $t _ { i } ^ { m }$ is given by 

$$
t _ {i} ^ {m} = t _ {i} ^ {f} - \frac {S}{v _ {i} \left(t _ {i} ^ {f}\right)} \tag {9}
$$

where $t _ { i } ^ { f }$ is the time that each vehicle $i$ exits the merging zone. The second term in (8) aims at minimizing the gaps between the vehicles, and thus fully exploiting the capacity of the road to avoid potential congestion. However, future research should investigate the existence of a potential trade-off between the two terms in (8). 

# III. ANALYTICAL SOLUTION

# A. Vehicle Coordination

When a vehicle enters a control zone, it receives a unique identity $i$ from the centralized controller, as described in the previous section. Recall that $\mathcal { N } ( t ) = \{ 1 , . . . , N ( t ) \}$ is the FIFO queue of vehicles in control zone. A vehicle index $i \in \mathcal { N } ( t )$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/05f442961590d6aa8a856f96fdb6c3d91196978403f30fefb28e7a43ea8d10a7.jpg)



Fig. 3. Illustration of time constraints for vehicles that are entering the merging zone from different roads.


also indicates which vehicle is closer to the merging zone, i.e., for any $i , k \in \mathcal { N } ( t )$ with $i < k$ then $p _ { i } < p _ { k }$ . 

Definition 3.1: Each vehicle $i \in \mathcal { N } ( t )$ belongs to at least one of the following two subsets: 1) $\mathcal { L } _ { i } ( t )$ contains all vehicles traveling on the same road with $i$ , and 2) $\mathcal { C } _ { i } ( t )$ contains all vehicles traveling on different roads from $i$ . 

The time $t _ { i } ^ { f }$ that the vehicle $i$ exits the merging zone is based on imposing constraints aimed at avoiding congestion in the sense of maintaining vehicle speeds above a certain value. There are two cases to consider: 

1) If vehicle $i - 1$ belongs to $\mathcal { L } _ { i } ( t )$ , then to satisfy the second term of (8) both $i - 1$ and $i$ should have the minimal safe distance allowable, denoted by $\delta$ , by the time vehicle $i - 1$ enters the merging zone, i.e., 

$$
t _ {i} ^ {f} = t _ {i - 1} ^ {f} + \frac {\delta}{v _ {i} \left(t _ {i} ^ {f}\right)} \tag {10}
$$

where $v _ { i } ( t _ { i } ^ { f } ) = v _ { i } ( t _ { i } ^ { 0 } )$ as we designate the vehicles to exit the merging zone with the same speed they had when they entered the control zone. However, this is just a matter of specifying the final conditions of the vehicles when they exit the merging zone, and as such other alternatives could be considered depending on how we wish to formulate the problem. 

2) If vehicle $i - 1$ belongs to $\mathcal { C } _ { i } ( t )$ , we constrain the merging zone to contain only one vehicle so as to avoid a lateral collision. Therefore, vehicle $i$ is allowed to enter the merging zone only when vehicle $i - 1$ exits the merging zone (see Fig. 3), where $t _ { i } ^ { m }$ is the time that the vehicle $i$ enters the merging zone), i.e., 

$$
t _ {i} ^ {f} = t _ {i - 1} ^ {f} + \frac {S}{v _ {i} \left(t _ {i} ^ {f}\right)} \tag {11}
$$

where $v _ { i } ( t _ { i } ^ { f } ) = v _ { i } ( t _ { i } ^ { 0 } )$ . However, this constraint is not restrictive and we can easily modify it by relaxing (11) and either use only (10) for both cases, or use instead of $S$ in (11) another desired value. 

Note that this recursive relationship over vehicles in a control zone queue satisfies both the rearend and lateral collision avoidance constraints. The rear-end collision avoidance constraint is 

satisfied at $t _ { i } ^ { f }$ through $t _ { i } ^ { f } = t _ { i - 1 } ^ { f } + ( \delta / v _ { i } ( t _ { i } ^ { f } ) )$ and the lateral collision avoidance constraint through $t _ { i } ^ { f } = t _ { i - 1 } ^ { f } + ( S / v _ { i } ( t _ { i } ^ { f } ) )$ . The recursion is initialized whenever a vehicle enters a control zone, i.e., it is assigned $i = 1$ . In this case, $t _ { 1 } ^ { f }$ can be externally assigned as the desired exit time of this vehicle whose behavior is unconstrained except for (4). Thus the time $t _ { i } ^ { f }$ is fixed for each vehicle $i$ . 

Consequently instead of solving (8) for $w _ { 2 } \gg w _ { 1 }$ , we can solve an optimization problem for each vehicle in the queue separately 

$$
\min  _ {u _ {i}} \qquad \frac {1}{2} \int_ {t _ {i} ^ {0}} ^ {t _ {i} ^ {m}} u _ {i} ^ {2} d t
$$

$\mathrm { S u b j e c t t o : ~ } ( 2 ) , ~ ( 4 ) \quad \forall i \in \mathcal { N } ( t ) .$ (12) 

# B. Hamiltonian Analysis

For the analytical solution and online implementation of the problem (12), we apply Hamiltonian analysis [60]. In our analysis, we consider that when the vehicles enter the control zone, the constraints are not active. However, this might not be in general true. For example, a vehicle may enter the control zone with speed higher than the speed limit. In this case, we need to solve an optimal control problem starting from an infeasible state. To address this situation requires additional analysis which is the subject of ongoing research. 

To simplify the analysis we consider the unconstrained problem, and thus the optimal solution would not provide limits for the state and control. The constrained problem formulation is discussed in [61], and it requires the constrained and unconstrained arcs of the state and control input to be pieced together to satisfy the Euler-Lagrange equations and necessary condition of optimality. So our approach yields the optimal solution as long as the control input and speed of each vehicle is within the imposed limits. 

From (12) and the state equations (2), the Hamiltonian function can be formulated for each vehicle $i \in \mathcal { N } ( t )$ as follows 

$$
H _ {i} (t, x (t), u (t)) = L _ {i} (t, x (t), u (t)) + \lambda^ {T} \cdot f _ {i} (t, x (t), u (t)). \tag {13}
$$

Thus 

$$
H _ {i} (t, x (t), u (t)) = \frac {1}{2} u _ {i} ^ {2} + \lambda_ {i} ^ {p} \cdot v _ {i} + \lambda_ {i} ^ {v} \cdot u _ {i} \tag {14}
$$

where $\lambda _ { i } ^ { p }$ and $\lambda _ { i } ^ { v }$ are the co-state components. The necessary condition for optimality is 

$$
\frac {\partial H _ {i}}{\partial u _ {i}} = u _ {i} + \lambda_ {i} ^ {v} = 0. \tag {15}
$$

From the last equation, the optimal control is given 

$$
u _ {i} + \lambda_ {i} ^ {v} = 0, \quad i \in \mathcal {N} (t). \tag {16}
$$

The Euler-Lagrange equations yield 

$$
\dot {\lambda} _ {i} ^ {p} = - \frac {\partial H _ {i}}{\partial p _ {i}} = 0 \tag {17}
$$

$$
\dot {\lambda} _ {i} ^ {v} = - \frac {\partial H _ {i}}{\partial v _ {i}} = - \lambda_ {i} ^ {p}. \tag {18}
$$

From (17) we have $\lambda _ { i } ^ { p } = a _ { i }$ and (18) implies $\lambda _ { i } ^ { v } = - ( a _ { i } t + b _ { i } )$ , where $a _ { i }$ and $b _ { i }$ are constants of integration corresponding to each vehicle i. Consequently, the optimal control input (acceleration/deceleration) as a function of time is given by 

$$
u _ {i} ^ {*} (t) = a _ {i} t + b _ {i}. \tag {19}
$$

Substituting the last equation into the vehicle dynamics equations (2) we can find the optimal speed and position for each vehicle, namely 

$$
v _ {i} ^ {*} (t) = \frac {1}{2} a _ {i} t ^ {2} + b _ {i} t + c _ {i} \tag {20}
$$

$$
p _ {i} ^ {*} (t) = \frac {1}{6} a _ {i} t ^ {3} + \frac {1}{2} b _ {i} t ^ {2} + c _ {i} t + d _ {i} \tag {21}
$$

where $c _ { i }$ and $d _ { i }$ are constants of integration. These constants can be computed by using the initial and final conditions. Since we seek to derive the optimal control (19) online, we can designate initial values $p _ { i } ( t _ { i } ^ { 0 } )$ and $v _ { i } ( t _ { i } ^ { 0 } )$ , and initial time, $t _ { i } ^ { 0 }$ , to be the current values of the states $p _ { i } ( t )$ and $v _ { i } ( t )$ and time $t$ , where $t _ { i } ^ { 0 } \leq t \leq t _ { i } ^ { f }$ . Therefore the constants of integration will be functions of time and states, i.e., $a _ { i } ( t , p _ { i } , v _ { i } )$ , $b _ { i } ( t , p _ { i } , v _ { i } )$ , $c _ { i } ( t , p _ { i } , v _ { i } )$ , and $d _ { i } ( t , p _ { i } , v _ { i } )$ . To derive online the optimal control for each vehicle $i$ , we need to update the integration constants at each time $t$ . Equations (20) and (21), along with the initial and final conditions defined above, can be used to form a system of four equations of the form $\mathbf { T } _ { i } \mathbf { b } _ { i } = \mathbf { q } _ { i }$ , namely 

$$
\left[ \begin{array}{c c c c} \frac {1}{6} t ^ {3} & \frac {1}{2} t ^ {2} & t & 1 \\ \frac {1}{2} t ^ {2} & t & 1 & 0 \\ \frac {1}{6} \left(t _ {i} ^ {f}\right) ^ {3} & \frac {1}{2} \left(t _ {i} ^ {f}\right) ^ {2} & t _ {i} ^ {f} & 1 \\ \frac {1}{2} \left(t _ {i} ^ {f}\right) ^ {2} & t _ {i} ^ {f} & 1 & 0 \end{array} \right] \cdot \left[ \begin{array}{l} a _ {i} \\ b _ {i} \\ c _ {i} \\ d _ {i} \end{array} \right] = \left[ \begin{array}{l} p _ {i} (t) \\ v _ {i} (t) \\ p _ {i} \left(t _ {i} ^ {f}\right) \\ v _ {i} \left(t _ {i} ^ {f}\right) \end{array} \right]. \tag {22}
$$

Hence we have 

$$
\mathbf {b} _ {i} (t, p _ {i} (t), v _ {i} (t)) = \left(\mathbf {T} _ {i}\right) ^ {- 1}. \mathbf {q} _ {i} (t, p _ {i} (t), v _ {i} (t)) \tag {23}
$$

where $\mathbf { b } _ { i } ( t , p _ { i } ( t ) , v _ { i } ( t ) )$ contains the four integration constants $a _ { i } ( t , p _ { i } , v _ { i } )$ , $b _ { i } ( t , p _ { i } , v _ { i } )$ , $c _ { i } ( t , p _ { i } , v _ { i } )$ , di(t, pi, vi). Thus (19) can be written as 

$$
u _ {i} ^ {*} (t, p _ {i} (t), v _ {i} (t)) = a _ {i} (t, p _ {i} (t), v _ {i} (t)) t + b _ {i} (t, p _ {i} (t), v _ {i} (t)). \tag {24}
$$

Since (22) can be computed online, the controller can yield the optimal control online for each vehicle $i$ , with feedback indirectly provided through the re-calculation of the vector $\mathbf { b } _ { i } ( t , p _ { i } ( t ) , v _ { i } ( t ) )$ in (23). 

# IV. SIMULATION RESULTS

To validate the effectiveness of the efficiency of our analytical solution we simulated the merging scenario presented in previous sections in MATLAB. In our simulation, the length of the control and merging zones is $L = 4 0 0 \mathrm { m }$ and $S = 3 0 \mathrm { m }$ . We assume that each vehicle travels at a constant speed of $1 3 . 4 \mathrm { m / s }$ before entering the control zone. When a vehicle reaches the control zone then the centralized controller designates its 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/632dbd5ca3213e5e843fac893715b688d96feac12fd4dd08bcc5ac7eea93261b.jpg)



Fig. 4. Initial vehicle positions on each road for case study 1.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/f32ef342efaf76a823d11fdf3559b489693be231d935ad4a0ded8097873e5874.jpg)



Fig. 5. Position trajectories of the four vehicles for case study 1.


acceleration/deceleration until the vehicle exits the merging zone. All vehicles are assumed to have the characteristics described in Section II-B. 

We considered four case studies: (1) coordination of 4 vehicles, 2 for each road, (2) coordination of 30 vehicles, 15 for each road, (3) coordination of 30 vehicles assuming the vehicles on the secondary road reach the control zone at a lower speed of $1 1 . 2 \mathrm { m } / \mathrm { s }$ , and (4) coordination of 30 vehicles that enter the control zone with $2 9 \mathrm { m } / \mathrm { s }$ . The solutions were compared to a baseline scenario where it was assumed that the vehicles on the main road have the right-of-way. That is, the vehicles on the secondary road have to come to a full stop before entering the merging zone. To quantify the benefits in fuel consumption, we used the polynomial metamodel in [58], as discussed in Section II-B. 

# A. Case Study 1: Coordination of 4 Vehicles

In this case study, we implemented the analytical solution for the coordination of 4 vehicles. The vehicles depart from the same position on each road (see Fig. 4). The purpose of this scenario is to validate that the controller will coordinate each vehicle to enter the merging zone only after the previous vehicle has already left. Even though the vehicles start at the same initial positions on each road, the controller was able to derive online the optimal acceleration/deceleration by allowing 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/ed75719516fd6e4bc6c9ab91ea4c8f56e53eb28351a563b2c0da1c3611b7a75d.jpg)



Fig. 6. Control input of the four vehicles for case study 1.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/c96c7f20c72bc945c8ff5fec798a66879178455815d0060f00816ace55deaadd.jpg)



Fig. 7. Speed profiles of the four vehicles for case study 1.


only one vehicle at a time in the merging zone (see Fig. 5). The optimal acceleration/deceleration and speed profile for each vehicle are illustrated in Figs. 6 and 7. Vehicle 1 accelerates first since it is cruising on the main road and has the right-ofway following by vehicle 2. 

# B. Case Study 2: Coordination of 30 Vehicles

In this case study, the centralized controller coordinates 30 vehicles moving on two merging roads (15 vehicles on each road) with random initial positions and no limitations on the minimum or maximum speed, i.e., unconstrained problem. The controller is able to derive online the optimal control input for each vehicle by avoiding collision in the merging zone (see Fig. 8). We note that as the number of vehicles in the control zone on each road increases this has an impact on the acceleration/deceleration of each vehicle (see Fig. 9). The controller accelerates the vehicles closer to the merging zone to create more space in the road for the following vehicles. 

However, as the number of vehicles on the road increases and reaches its maximum capacity, eventually, the vehicles entering the control zone will need to decelerate, or even come to a full stop as imposed by the road capacity constraints. This is evident in Fig. 10, where the vehicles that are back in the queue need to decelerate as imposed by the safety constraints. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/c934e83835da5c2c7b52fef813964ee28369a13f948d06618c151264db92396c.jpg)



Fig. 8. Position trajectories of the vehicles for case study 2.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/2d964a520062b5d0ea4da1dac4ba168439eff4e3f2e213d3725046381d6ab251.jpg)



Fig. 9. Control input of the vehicles for case study 2.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/219e987caf661473059add4c257e04e97e20559a8f9c0854ee9f23b8f11c53f1.jpg)



Fig. 10. Speed profiles of the vehicles for case study 2.


# C. Case Study 3: Coordination With Different Initial Speed for Each Road

In this case, we considered the coordination of 30 vehicles with different initial speeds for the main and secondary roads. The vehicles on the main road arrive at $1 3 . 4 \mathrm { ~ m } / \mathrm { s }$ and the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/20c792e4e422ff1a19a6b59c4ed11f5ab6c544998541acd2f8c7bbbe87eef4ec.jpg)



Fig. 11. Position trajectories of the vehicles for case study 3.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/7b08d7db5b3dd2b5ffd2ef6b0cef65f1b8db95c1eecab85367c2f8fe917cc962.jpg)



Fig. 12. Speed profiles of the vehicles for case study 3.


vehicles on the secondary road will arrive at $1 1 . 2 \mathrm { m } / \mathrm { s }$ . All the vehicles exit the merging zone at a desired speed of $1 3 . 4 ~ \mathrm { m / s }$ . The position trajectory of the vehicles is illustrated in Fig. 11. The vehicles are able to merge without collision. Note also that the vehicles on the main road reach higher speed values (see Fig. 12) than in the case study 2. 

# D. Fuel Consumption and Travel Time Results

To compare fuel consumption benefits of vehicle coordination we considered a baseline scenario, in which the vehicles on the secondary road have to stop before the intersection to allow the vehicles in the main road to cross the merging zone. Only after all the vehicles on the main road have crossed, the vehicles on the secondary road start accelerating to reach again the maximum allowed speed. 

The cumulative fuel consumption is higher in the baseline case compared to the case studies 2 and 3 where the vehicles are coordinated through the centralized controller (see Fig. 13). In particular, optimal vehicle coordination improves overall fuel consumption by $5 2 . 7 \%$ for the case study 2, and $4 8 . 1 \%$ for the case study 3 compared to the baseline scenario. The total travel time is also improved by $7 . 1 \%$ , and $1 3 . 5 \%$ , respectively (see Fig. 14). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/f38987e461c16eaece53a36566f7d0a4b54965b5c52da14c26a2863e389c8bf1.jpg)



Fig. 13. Cumulative fuel consumption for the baseline, case study 2, and case study 3.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/7c124ea49bae64dd87bc96ffdc6f84c28e5cbe14c6bd4413e8d949f13a86c6ef.jpg)



Fig. 14. Total travel time for the baseline, case study 2, and case study 3.


# E. Case Study 4: Vehicle Coordination at 29 m/s

Merging roadways are very common in highways. Thus we also considered a scenario where the vehicles enter the control zone at $2 9 \mathrm { m } / \mathrm { s }$ . The maximum and minimum speed limits inside the control zone were specified to be equal to $3 1 . 3 ~ \mathrm { m / s }$ and $2 2 . 4 \ : \mathrm { m / s }$ respectively. 

In this case, however, the controller was unable to satisfy the safety constraints within the length of the control zone and the speed limits. To address this issue, we have two options: 1) increase the length of the control zone and 2) increase the speed limit. Since increasing the speed limit beyond $3 1 . 3 ~ \mathrm { m } / \mathrm { s }$ might raise several safety concerns, we increased the length of the control zone to $^ { 1 , 2 0 0 \mathrm { ~ m ~ } }$ . However we recognize that this might be unrealistically a long zone, and as such this fact indicates the potential limitations of the proposed approach. Nevertheless, the controller was able to coordinate the vehicles but some of the vehicles had to reach the speed limits, which indicates that eventually increasing also the speed limit might be inevitable. 

# V. CONCLUDING REMARKS

In this paper, we addressed the problem of optimal coordination of CAVs at merging roadways. We formulated the problem 

as an unconstrained optimal control problem and we applied Hamiltonian analysis to derive an analytical, closed-form solution. The effectiveness of the efficiency of the proposed solution was validated through simulation and it was shown that vehicle coordination can reduce significantly both fuel consumption and travel time. The proposed approach allows the vehicles to merge without creating congestions and under the hard constraint of collision avoidance. 

Ongoing research investigates the feasibility of the solution when at the time the vehicles enter the control zone some of the constraints are active and the computational implications. Future research should consider a more sophisticated transportation simulation model including more advanced vehicle models aimed at providing the practical implications of implementing such approach. Future research should also consider a diversity of vehicles and also investigate the existence of a potential trade-off between fuel consumption and congestion. 

# ACKNOWLEDGMENT

The authors would like to thank P. Pisu for the general discussions. 

# REFERENCES



[1] A. A. Malikopoulos and J. P. Aguilar, “An optimization framework for driver feedback systems,” IEEE Trans. Intell. Transp. Syst., vol. 14, no. 2, pp. 955–964, Jun. 2013. 





[2] R. Margiotta and D. Snyder, “An agency guide on how to establish localized congestion mitigation programs,” U.S. Dept. Transp. Federal Highway Admin., Washington, DC, USA, Tech. Rep., 2011. [Online]. Available: http://ops.fhwa.dot.gov/publications/fhwahop11009/fhwahop11009.pdf 





[3] B. Schrank, B. Eisele, T. Lomax, and J. Bak, “2015 urban mobility scorecard,” Texas A & M Transp. Inst., College Station, TX, USA, Tech. Rep., 2015. 





[4] A. A. Malikopoulos and J. P. Aguilar, “Optimization of driving styles for fuel economy improvement,” in Proc. IEEE 15th Int. Conf. Intell. Transp. Syst., 2012, pp. 194–199. 





[5] V. L. Knoop, H. J. Van Zuylen, and S. P. Hoogendoorn, “Microscopic traffic behaviour near accidents,” in Proc. 18th Int. Symp. Transp. Traffic Theory, 2009, pp. 1–22. 





[6] L. Li, D. Wen, and D. Yao, “A survey of traffic control with vehicular communications,” IEEE Trans. Intell. Transp. Syst., vol. 15, no. 1, pp. 425–432, Feb. 2014. 





[7] J. Rios-Torres and A. A. Malikopoulos, “A survey on coordination of connected and automated vehicles at intersections and merging at highway on-ramps,” IEEE Trans. Intell. Transp. Syst., to be published. 





[8] K. Dresner and P. Stone, “Multiagent traffic management: A reservationbased intersection control mechanism,” in Proc. 3rd Int. Joint Conf. Autonomous Agents Multiagents Syst., 2004, pp. 530–537. 





[9] K. Dresner and P. Stone, “A multiagent approach to autonomous intersection management,” J. Artif. Intell. Res., vol. 31, no. 1, pp. 591–653, Jan. 2008. 





[10] T.-C. Au and P. Stone, “Motion planning algorithms for autonomous intersection management,” in Proc. AAAI Workshop Bridging Gap BTAMP, 2010, pp. 1–8. 





[11] A. de La Fortelle, “Analysis of reservation algorithms for cooperative planning at intersections,” in Proc. IEEE 13th Int. Conf. Intell. Transp. Syst., Sep. 2010, pp. 445–449. 





[12] S. Huang, A. Sadek, and Y. Zhao, “Assessing the mobility and environmental benefits of reservation-based intelligent intersections using an integrated simulator,” IEEE Trans. Intell. Transp. Syst., vol. 13, no. 3, pp. 1201–1214, Sep. 2012. 





[13] K. Zhang, A. D. L. Fortelle, D. Zhang, and X. Wu, “Analysis and modeled design of one state-driven autonomous passing-through algorithm for driverless vehicles at intersections,” in Proc. IEEE 16th Int. Conf. Comput. Sci. Eng., Dec. 2013, pp. 751–757. 





[14] Q. Jin, G. Wu, K. Boriboonsomsin, and M. Barth, “Multi-agent intersection management for connected vehicles using an optimal scheduling approach,” in Proc. IEEE ICCVE, Dec. 2012, pp. 185–190. 





[15] I. H. Zohdy, R. K. Kamalanathsharma, and H. Rakha, “Intersection management for autonomous vehicles using iCACC,” in Proc. IEEE 15th Int. Conf. Intell. Transp. Syst., Sep. 2012, pp. 1109–1114. 





[16] F. Yan, M. Dridi, and A. El Moudni, “Autonomous vehicle sequencing algorithm at isolated intersections,” Proc. IEEE 12th Int. Conf. Intell. Transp. Syst., Oct. 2009, pp. 1–6. 





[17] L. Li and F.-Y. Wang, “Cooperative driving at blind crossings using intervehicle communication,” IEEE Trans. Veh. Technol., vol. 55, no. 6, pp. 1712–1724, Nov. 2006. 





[18] F. Zhu and S. V. Ukkusuri, “A linear programming formulation for autonomous intersection control within a dynamic traffic assignment and connected vehicle environment,” Transp. Res. C, Emerging Technol., vol. 55, pp. 363–378, Jan. 2015. 





[19] J. Wu, F. Perronnet, and A. Abbas-Turki, “Cooperative vehicle-actuator system: A sequence-based framework of cooperative intersections management,” IET Intell. Transp. Syst., vol. 8, no. 4, pp. 352–360, Jun. 2014. 





[20] J. Lee and B. Park, “Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment,” IEEE Trans. Intell. Transp. Syst., vol. 13, no. 1, pp. 81–90, Mar. 2012. 





[21] J. Lee, B. B. Park, K. Malakorn, and J. J. So, “Sustainability assessments of cooperative vehicle intersection control at an urban corridor,” Transp. Res. C, Emerging Technol., vol. 32, pp. 193–206, Jul. 2013. 





[22] D. Miculescu and S. Karaman, “Polling-systems-based control of highperformance provably-safe autonomous intersections,” in Proc. IEEE 53rd Conf. Dec. Control, 2014, pp. 1417–1423. 





[23] V. Milanés, J. Pérez, and E. Onieva, “Controller for urban intersections based on wireless communications and fuzzy logic,” IEEE Trans. Intell. Transp. Syst., vol. 11, no. 1, pp. 243–248, Mar. 2010. 





[24] J. Alonso, V. Milanés, J. Pérez, E. Onieva, C. González, and T. de Pedro, “Autonomous vehicle control systems for safe crossroads,” Transp. Res. C, Emerging Technol., vol. 19, no. 6, pp. 1095–1110, Dec. 2011. 





[25] A. Colombo and D. Del Vecchio, “Least restrictive supervisors for intersection collision avoidance: A scheduling approach,” IEEE Trans. Autom. Control, vol. 60, no. 6, pp. 1515–1527, Jun. 2015. 





[26] Y. Z. Zhang, A. A. Malikopoulos, and C. G. Cassandras, “Optimal control and coordination of connected and automated vehicles at urban traffic intersections,” in Proc. Amer. Control Conf., 2016, pp. 6227–6232. 





[27] L. Makarem, D. Gillet, and S. Member, “Model predictive coordination of autonomous vehicles crossing intersections,” in Proc. IEEE 16th Int. ITSC, 2013, pp. 1799–1804. 





[28] K.-D. Kim and P. Kumar, “An MPC-based approach to provable systemwide safety and liveness of autonomous ground traffic,” IEEE Trans. Autom. Control, vol. 59, no. 12, pp. 3341–3356, Dec. 2014. 





[29] Ramp Metering: A Proven, Cost-Effective Operational Strategy—A Primer, U.S. Dept. Transp. Federal Highway Admin., Washington, DC, USA. [Online]. Available: http://www.ops.fhwa.dot.gov/publications/ fhwahop14020/sec1.htm 





[30] M. Papageorgiou, H. Hadj-Salem, and J.-M. Blosseville, “ALINEA: A local feedback control law for on-ramp metering,” Nat. Acad. Sci., Eng., Med., Washington, DC, USA, Transp. Res. Rec. 1320, 1991. 





[31] I. Papamichail and M. Papageorgiou, “Traffic-responsive linked rampmetering control,” IEEE Trans. Intell. Transp. Syst., vol. 9, no. 1, pp. 111–121, Mar. 2008. 





[32] R. C. Carlson, I. Papamichail, and M. Papageorgiou, “Local feedbackbased mainstream traffic flow control on motorways using variable speed limits,” IEEE Trans. Intell. Transp. Syst., vol. 12, no. 4, pp. 1261–1276, Dec. 2011. 





[33] G.-R. Iordanidou, C. Roncoli, I. Papamichail, and M. Papageorgiou, “Feedback-based mainstream traffic flow control for multiple bottlenecks on motorways,” IEEE Trans. Intell. Transp. Syst., vol. 16, no. 2, pp. 1–12, Apr. 2014. 





[34] S. Agarwal, P. Kachroo, S. Contreras, and S. Sastry, “Feedbackcoordinated ramp control of consecutive on-ramps using distributed modeling and Godunov-based satisfiable allocation,” IEEE Trans. Intell. Transp. Syst., vol. 16, no. 5, pp. 2384–2392, Oct. 2015. 





[35] A. Alessandri, A. Di Febbraro, A. Ferrara, and E. Punta, “Optimal control of freeways via speed signalling and ramp metering,” Control Eng. Pract., vol. 6, pp. 771–780, 1998. 





[36] A. Kotsialos and M. Papageorgiou, “Nonlinear optimal control applied to coordinated ramp metering,” IEEE Trans. Control Syst. Technol., vol. 12, no. 6, pp. 920–933, Nov. 2004. 





[37] C. Pasquale, I. Papamichail, C. Roncoli, S. Sacone, S. Siri, and M. Papageorgiou, “Two-class freeway traffic regulation to reduce congestion and emissions via nonlinear optimal control,” Transp. Res. C, Emerging Technol., vol. 55, pp. 85–99, Jun. 2015. 





[38] L. N. Jacobson, K. C. Henry, and O. Mehyar, “Real-time metering algorithm for centralized control,” Transp. Res. Rec. Urban Traffic Syst. Oper., vol. 1232, pp. 17–26, 1989. 





[39] J. Hourdakis and P. Michalopoulos, “Evaluation of ramp control effectiveness in two Twin Cities freeways,” in Proc. Transp. Res. Board 81st Annu. Meet., Washington, D.C., USA, 2002, pp. 1–20. 





[40] M. Papageorgiou and A. Kotsialos, “Freeway ramp METERING: An overview,” IEEE Trans. Intell. Transp. Syst., vol. 3, no. 4, pp. 271–281, Dec. 2002. 





[41] M. Athans, “A unified approach to the vehicle-merging problem,” Transp. Res., vol. 3, no. 1, pp. 123–133, Apr. 1969. 





[42] W. Levine and M. Athans, “On the optimal error regulation of a string of moving vehicles,” IEEE Trans. Autom. Control, vol. 11, no. 3, pp. 355–361, Jul. 1966. 





[43] G. Schmidt and B. Posch, “A two-layer control scheme for merging of automated vehicles,” in Proc. IEEE 22nd Conf. Dec. Control, 1983, pp. 495–500. 





[44] T. Awal, L. Kulik, and K. Ramamohanrao, “Optimal traffic merging strategy for communication- and sensor-enabled vehicles,” in Proc. IEEE 16th Int. ITSC, 2013, pp. 1468–1474. 





[45] P. Kachroo and Z. L. Z. Li, “Vehicle merging control design for an automated highway system,” in Proc. Conf. Intell. Transp. Syst., 1997, pp. 224–229. 





[46] M. Antoniotti, A. Deshpande, and A. Girault, “Microsimulation analysis of automated vehicles on multiple merge junction highways,” in Proc. IEEE Int. Conf. Syst., Man, Cybern., 1997, pp. 839–844. 





[47] M. Antoniotti, A. Desphande, and A. Girault, “Microsimulation analysis of multiple merge junctions under autonomous AHS operation,” in Proc. IEEE Intell. Transp. Syst. Conf., 1997, pp. 147–152. 





[48] B. Ran, S. Leight, and B. Chang, “A microscopic simulation model for merging control on a dedicated-lane automated highway system,” Transp. Res. C, Emerging Technol., vol. 7, no. 6, pp. 369–388, 1999. 





[49] A. Uno, T. Sakaguchi, and S. Tsugawa, “A merging control algorithm based on inter-vehicle communication,” in Proc. IEEE/IEEJ/JSAI Int. Conf. Intell. Transp. Syst. (Cat. No. 99TH8383), 1999, pp. 783–787. 





[50] X.-Y. Lu and K. Hedrick, “Longitudinal control algorithm for automated vehicle merging,” in Proc. IEEE 39th Conf. Dec. Control, 2000, pp. 450–455. 





[51] X.-Y. Lu, H.-S. Tan, S. E. Shladover, and J. K. Hedrick, “Automated vehicle merging maneuver implementation for AHS,” Veh. Syst. Dyn., vol. 41, no. 2, pp. 85–107, 2004. 





[52] G. Raravi, V. Shingde, K. Ramamritham, and J. Bharadia, “Merge algorithms for intelligent vehicles,” in Proc. Next Gener. Des. Verification Methodol. Distrib. Embedded Control Syst., 2007, pp. 51–65. 





[53] J. Milanes, V. Godoy, J. Villagra, and J. Perez, “Automated on-ramp merging system for congested traffic situations,” IEEE Trans. Intell. Transp. Syst., vol. 12, no. 2, pp. 500–508, Jun. 2011. 





[54] D. Marinescu, J. Curn, M. Bouroche, and V. Cahill, “On-ramp traffic ˇ merging using cooperative intelligent vehicles: A slot-based approach,” in Proc. IEEE ITSC, 2012, pp. 900–906. 





[55] I. Ntousakis, K. Porfyri, I. Nikolos, and M. Papageorgiou, “Assessing the impact of a cooperative merging system on highway traffic using a microscopic flow simulator,” in Proc. Int. Mech. Eng. Congr. Expo., 2014, pp. 1–10. 





[56] W. Cao, M. Mukai, T. Kawabe, H. Nishira, and N. Fujiki, “Cooperative vehicle path generation during merging using model predictive control with real-time optimization,” Control Eng. Pract., vol. 34, pp. 98–105, 2015. 





[57] J. Rios-Torres, A. A. Malikopoulos, and P. Pisu, “Online optimal control of connected vehicles for efficient traffic flow at merging roads,” in Proc. IEEE 18th Int. Conf. Intell. Transp. Syst., 2015, pp. 2432–2437. 





[58] M. Kamal, M. Mukai, J. Murata, and T. Kawabe, “Model predictive control of vehicles on urban roads for improved fuel economy,” IEEE Trans. Control Syst. Technol., vol. 21, no. 3, pp. 831–841, May 2013. 





[59] A. A. Malikopoulos, P. Y. Papalambros, and D. N. Assanis, “Online identification and stochastic control for autonomous internal combustion engines,” J. Dyn. Syst., Meas., Control, vol. 132, no. 2, 2010, Art. no. 024504. 





[60] L. S. Pontryagin, L. S. Pontryagin: Mathematical Theory of Optimal Processes. Boca Raton, FL, USA: CRC Press, 1987. 





[61] A. A. Malikopoulos, C. G. Cassandras, and Y. Zhang, “Decentralized optimal control for connected and automated vehicles at an intersection,” in Proc. 55th Conf. Dec. Control, 2016. 



![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/db22c760b13f6b2e493b11889bf3f1d0c514c3c54e48aa8ce75533e989fd15d9.jpg)


Jackeline Rios-Torres (M’15) received the B.S. degree in electronic engineering from the Universidad del Valle, Cali, Colombia, in 2008 and the Ph.D. degree in automotive engineering from Clemson University (CU), Clemson, SC, USA, in 2015. 

She is currently a Eugene P. Wigner Fellow with the Energy and Transportation Science Division, Oak Ridge National Laboratory, Oak Ridge, TN, USA and a GATE fellow with the Center for Research and Education in Sustainable Vehicle Systems, CU-International Center for Automotive 

Research (ICAR), Greenville, SC. Her research interests include connected and automated vehicles, intelligent transportation systems, and modeling and energy management control of hybrid electric vehicles/plug-in hybrid electric vehicles. 

Dr. Rios-Torres was a recipient of the Southern Automotive Women Forum Scholarship and the Smith Fellowship at CU-ICAR. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-26/852ae77c-8ab9-4733-a9d4-c7260898207f/0742acdf1f52f305ca121ed6920744beacb685d18b94f5eabe2685136272736b.jpg)


Andreas A. Malikopoulos (M’06) received the Diploma in mechanical engineering from the National Technical University of Athens, Athens, Greece, in 2000 and the M.S. and Ph.D. degrees from the University of Michigan, Ann Arbor, MI, USA, in 2004 and 2008, respectively. 

He was a Senior Researcher with General Motors Global Research & Development, where he conducted research in the area of stochastic optimization and control of advanced propulsion systems. He is currently the Deputy Director of the Urban Dynam-

ics Institute, Oak Ridge National Laboratory, Oak Ridge, TN, USA, where he is an Alvin M. Weinberg Fellow with the Energy and Transportation Science Division. His research interests include analysis, optimization, and control of complex systems; decentralized systems; stochastic scheduling and resource allocation problems; and energy, transportation, and operations researches. 