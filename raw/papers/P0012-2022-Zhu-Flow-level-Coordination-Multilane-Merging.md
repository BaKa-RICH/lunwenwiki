# Flow-level coordination of connected and autonomous vehicles in multilane freeway ramp merging areas

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/9efbde10fe9f2234bdf5f666cfa913cafaa00f957ea13c6b57378fcc00c45cf6.jpg)


Jie Zhu, Ivana Tasic, Xiaobo Qu∗ 

Department of Architecture and Civil Engineering, Chalmers University of Technology, Gothenburg 41296, Sweden 

# a r t i c l e i n f o

Keywords: 

Coordinative ramp merging 

Connected and autonomous vehicles 

Multilane freeway 

Optimization 

Microscopic traffic simulation 

# a b s t r a c t

On-ramp merging areas are deemed to be typical bottlenecks for freeway networks due to the intensive disturbances induced by the frequent merging, weaving, and lane-changing behaviors. The Connected and Autonomous Vehicles (CAVs), benefited from their capabilities of real-time communication and precise motion control, hold an opportunity to promote ramp merging operation through enhanced cooperation. The existing CAV cooperation strategies are mainly designed for single-lane freeways, although multilane configurations are more prevailing in the real-world. In this paper, we present a flow-level CAV coordination strategy to facilitate merging operation in multilane freeways. The coordination integrates lane-change rules between mainstream lanes, proactive creation of large merging gaps, and platooning of ramp vehicles for enhanced benefits in traffic flow stability and efficiency. The strategy is formulated under an optimization framework, where the optimal control plan is determined based on real-time traffic conditions. The impacts of tunable model parameters on the produced control plan are discussed in detail. The efficiency of the proposed multilane strategy is demonstrated in a micro-simulation environment. The results show that the coordination can substantially improve the overall ramp merging efficiency and prevent recurrent traffic congestions, especially under high traffic volume conditions. 

# 1. Introduction

On-ramp merging areas are deemed to be typical bottlenecks for freeway networks, as the merging of ramp vehicles impose frequent disturbances on the traffic flow and cause various problems, such as traffic oscillations, increased energy use and pollutions, accidents, and recurrent traffic congestions (Cassidy and Bertini, 1999; Mergia et al., 2013; Srivastava and Geroliminis, 2013; Han and Ahn, 2018; Wang et al., 2019;). Many efforts are devoted to facilitating the merging operation at freeway on-ramps. Prior approaches mainly focus on the active traffic management strategies, such as ramp metering (Papageorgiou et al., 1991; Smaragdis et al., 2004; Gomes and Horowitz, 2006 Papamichail et al., 2010), variable speed limit (Carlson et al., 2011; Zhang et al., 2013; Chen et al., 2014;), hard-shoulder running (Mirshahi et al., 2007), and the combinations of them (Hegyi et al., 2005; Papamichail et al., 2008; Carlson et al., 2010; Lu et al., 2011;). However, the benefits of such systems are limited because they cannot address the randomness and heterogeneity in the microscopic dynamics of individual vehicles. 

The emerging Connected and Autonomous Vehicles (CAVs) present an opportunity to regulate individual vehicles and achieve cooperative driving in various bottleneck areas (Zhou et al., 2017; Debada and Gillet, 2018; Mirheli et al., 2019; Qu et al., 2020; Wu et al., 2020; Zhou et al., 2020; Cao et al., 2021; Wu et al., 2021; Zhu and Tasic, 2021). Compared to the Human-Driven Vehicles (HDVs), CAVs can obtain more accurate and comprehensive traffic information through the vehicle communication technologies, and they are capable of more precise and timely execution of the dynamic driving tasks. In the literature, a number of CAV-enabled cooperation 

strategies are proposed to facilitate the merging traffic at freeway on-ramps, as summarized in Scarinci and Heydecker (2014) and Rios-Torres and Malikopoulos (2017b). These strategies may differ in, for example, adopted assumptions, required vehicle capabilities (i.e., connected, autonomous, or connected and autonomous), penetration rate of “intelligence” (i.e., $1 0 0 \%$ CAVs or a mix of CAVs and HDVs), and hierarchy of control (i.e., centralized, decentralized, or combined), while sharing the common objective to improve merging operational performance. Most of these strategies focus on the lower-level decisions of individual vehicles (e.g., trajectory design of CAVs), whereas the upper-level considerations (e.g., traffic flow efficiency and stability) are only discussed to a very limited extent. Further, the existing studies are primarily designed for single-lane freeways where free lane-changes between mainstream lanes are neglected, whereas a comprehensive discussion on how to achieve merging cooperation in the more prevailing multilane freeways is missing. 

In view of the limitations of existing CAV merging strategies, we propose in this paper an upper-level coordination strategy to promote the ramp merging operation in multilane freeways. The proposed strategy, as a significant extension to Zhu et al. (2021), coordinates the ramp traffic with the mainline traffic in the outermost lane by proactively creating large gaps on the main road and leading ramp vehicles into the created gaps in the form of platoons. The free lane-changes between the mainstream lanes are incorporated in the coordination, and the mainline-ramp coordination is combined with the one-sided lane-change prohibition rule to protect the created outer lane gaps from being occupied by the inner lane vehicles. The coordination is formulated as an optimization problem based on microscopic and macroscopic traffic flow models. The formulation clearly considers traffic stability and efficiency gains at the continuous traffic flow level. The benefits of the proposed coordination are demonstrated through a case study conducted on a microscopic simulation platform. 

The remaining of this paper is structured as follows: Section 2 reviews the state-of-the-arts of CAV ramp merging strategies and summarizes the contributions of this work. Section 3 formulates the multilane coordination strategy and provides extended discussions on relevant issues. Section 4 introduces the case study and discusses the efficiency of CoMC under various traffic conditions. The conclusion is drawn in Section 5. 

# 2. Literature review

CAV ramp merging strategies, deemed to be a promising approach to facilitate traffic operation in the freeway on-ramp bottlenecks, have received great attention in recent research efforts. The existing efforts are divided into two categories: trajectory planning methods and aggregated control methods. 

A majority of the existing studies falls into the first category. These studies usually use an optimization framework to formulate the lower-level motion plan of multiple vehicles, subject to vehicle dynamics, safety requirements, and technical constraints, but major differences lie in the control direction (e.g., longitudinal, lateral, or both), the objective (e.g., efficiency, safety, energy use, passenger comfort, or combined cost), and the control variables (e.g., acceleration, jerk, and/or lane-change decisions). For example, Cao et al. (2015) describe the states and actions of a ramp merging vehicle and its mainline competitor in a two-dimensional coordinate system and design their optimal paths, defined by the longitudinal acceleration and the optimal merging point, by minimizing a penalty combined of acceleration, speed deviation, and inter-vehicle distance. Similarly, Zhou et al. (2019a, 2019b) solve the merging trajectories of a ramp merging vehicle and a mainline facilitating vehicle at a minimal acceleration cost, while restraining the negative safety impacts of the merging maneuver. Karimi et al. (2020) look at the mixed CAV-HDV traffic flow and control the cooperative motions of CAVs for different types of merging triplets. The above studies focus on the interaction between a ramp merging vehicle and its direct neighbors on the main road, whereas some other studies assume the presence of an upper-level merging sequence and jointly plan the trajectories of a series of vehicles within the merging control zone. For example, Ntousakis et al. (2016), Rios-Torres and Malikopoulos (2017a) and Sonbolestan et al. (2021) minimize the overall acceleration/jerk efforts in favor of energy use and passenger comfort. The models are analytically solved using Hamiltonian analysis. Letter and Elefteriadou (2017) and Xie et al. (2017) formulate models targeting at maximum collective speed, while taking into account the safety distance between vehicles. The strategy of Letter and Elefteriadou (2017) is later extended to a two-lane freeway configuration, where a centralized lane-changing controller is integrated to reallocate a number of mainstream vehicles from the outer lane to the inner lane (Hu et al., 2019). Further, Omidvar et al. (2020) apply Letter and Elefteriadou (2017) in a mixed CAV-HDV traffic condition, where a model predictive control framework is used to address the deviations in HDV behaviors. Some recent studies integrate the choice of merging sequence into the motion planning problem. For example, Ding et al. (2020) use a series of rules to adjust the merging order of vehicles and plan the motion of each vehicle accordingly. Xu et al. (2021) formulate the merging sequence choice as an optimization problem combining the mainline travel time and the merging throughput and solve the problem through generic algorithms. Alternatively, Jing et al. (2019), Chen et al. (2020) and Sun et al. (2020) integrate the gap choice and path planning of merging vehicles into an optimization model. The model compares the path costs to lead a ramp vehicle into different gaps, so as to find the optimal gap and the corresponding path with the lowest cost. In addition to the optimization method, alternative approaches to determine vehicle trajectories at ramp merging are proposed. For example, Marinescu et al. (2012) and Wang et al. (2013) utilize the idea of virtual vehicle/slot to reserve mainline space for the merging vehicles. Fukuyama (2020). develop a dynamic game-based framework where each vehicle chooses the most beneficial action based on the estimated action of a competing vehicle. Karbalaieali et al. (2020) considers a two-lane freeway and choose from various alternative actions (i.e., speeding up, slowing down, or changing lanes) the one that minimizes the total travel time of a ramp vehicle and its mainline competitors. In summary, the above studies are dedicated to facilitating ramp merging operation through joint trajectory planning of relevant vehicles. Though presenting encouraging results, these methods mainly focus on the microscopic interactions between individual vehicles, whereas their performance in a continuous traffic flow is not ensured. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/52ca5e6184517af46e0e2df3f3de997c211904e63cf7c4ff9f280208832dbfac.jpg)



Fig. 1. Conceptual illustration of the CoMC strategy.


The second category, aggregated control methods, is less covered in the literature. It refers to the ramp merging strategies that control the operation of traffic flow instead of the step-by-step action of individual vehicles at a more aggregated level. An example is Scarinci et al. (2017), where the mainline traffic is periodically compacted to create large merging gaps, and the ramp traffic is released into the gaps via a ramp metering signal. This strategy ensures the fluent operation of mainline traffic, but arises a fairness concern between the two traffic streams, as the release of ramp traffic is fully dependent on the main road condition under such a system. In Chen et al. (2021), a similar idea of periodic gap creation is adopted and combined with a batch merging strategy to close the extra gaps induced by lane-changes. The benefits of the proposed system are demonstrated in theory, but no numerical or simulation experiment is carried out. Recently, Zhu et al. (2021) develop a coordination strategy that creates on-demand gaps on the main road upon formations of proper ramp merging platoons. The coordination makes adaptive coordination decisions according to the real-time traffic state. Case study results show the strategy’s ability to improve traffic efficiency and prevent congestions at ramp merging. It is noticed in the review that the existing flow-level coordination strategies focus on the single-lane freeway configuration and ignore the free lane-changes between mainstream lanes, so a thorough discussion about how to implement merging coordination in a multilane freeway configuration is desired. 

In summary, in the current literature, only very few CAV merging strategies are designed for the multilane freeway environment, such as Hu and Sun (2019) and Karbalaieali et al. (2020), and the existing multilane strategies focus on the lower-level decisions of individual vehicles, whereas the options to improve traffic flow performance are not sufficiently discussed. 

Therefore, we are motivated to propose in this paper a flow-level strategy, leveraging the CAV capabilities, to coordinate the two streams of traffic (instead of individual vehicles) in the multilane freeway ramp merging areas. 

# 3. Coordinative Merging Control (CoMC) in multilane freeway

# 3.1. Formulation of multilane CoMC

The Coordinative Merging Control (CoMC) strategy for multilane freeways is developed based on the coordination framework in Zhu et al. (2021b). The underlying idea is to coordinate the outer-lane mainline traffic and the ramp traffic through proactive gap creation on the main road and platoon formation on the ramp. Specifically, as shown in Fig. 1, the on-ramp vehicles stop at a pre-determined Waiting Position (WP) on the ramp and register themselves with the control center upon arrival. The control center counts the number of vehicles waiting on the ramp and initiates a coordinative merging request when a certain number of ramp vehicles has accumulated. With the merging request, the control center first appoints a vehicle in the mainstream outer lane as the facilitating vehicle and requires it to slow down at the Speed-Change (SC) position, so that a gap is proactively created between the facilitating vehicle and its leader on the main road. Then, the control center releases the vehicles waiting on the ramp as a platoon by specifying their moving trajectories towards the Merging Point (MP). In order to smoothly guide the merging platoon into the created gap, the centralized control makes a joint decision on the coordination decisions, including the SC position and cooperative speed of the facilitating vehicle and the size and moving trajectory of the merging platoon, so as to satisfy the following three requirements at merging: (1) the created mainline gap should be large enough for the merging platoon (the requirement of size); (2) the platoon should reach the same speed as the mainline facilitating vehicle at the MP (the requirement of merging speed); and (3) the gap should be just available at the MP when the platoon arrives there (the requirement of arrival time). This entire course of creating a gap and guiding a merging platoon into the gap is defined as a coordinative merging cycle, and the CoMC strategy functions by recurrently implementing the merging cycles. 

Note that, the essence of such coordination is to compact the mainline traffic by reducing the traffic speed and collecting enough space for the merging of ramp vehicles. We assume that the mainline traffic is originally in a stable equilibrium state (state O) before the coordination is initiated. When the facilitating vehicle decelerates in response to a coordination request, the mainline vehicles 


Table 1 Notation.


<table><tr><td>Variable</td><td>Description</td><td>Role</td></tr><tr><td>n</td><td>Merging platoon size</td><td>decision variable</td></tr><tr><td>d</td><td>Cooperative distance (i.e., distance between SC and MP)</td><td>decision variable</td></tr><tr><td>VC</td><td>Mainline cooperative speed</td><td>decision variable</td></tr><tr><td>wm</td><td>Weight of mainline traffic</td><td>input parameter</td></tr><tr><td>wR</td><td>Weight of ramp traffic</td><td>input parameter</td></tr><tr><td>Dmain</td><td>Delay to theith mainline cooperative vehicle</td><td>function of vCand d</td></tr><tr><td>Dramp</td><td>Delay to thejth ramp vehicle in the merging platoon</td><td>function of n, vC, and d</td></tr><tr><td>r</td><td>Frequency of the merging cycles</td><td>function of n</td></tr><tr><td>qO</td><td>Mainline flow rate in the original state</td><td>input parameter</td></tr><tr><td>kO</td><td>Mainline density in the original state</td><td>input parameter</td></tr><tr><td>vO</td><td>Mainline vehicle speed in the original state</td><td>input parameter</td></tr><tr><td>hO</td><td>Mainline headway in the original state</td><td>input parameter</td></tr><tr><td>qc</td><td>Mainline flow rate in the cooperative state</td><td>function of vC</td></tr><tr><td>kC</td><td>Mainline density in the cooperative state</td><td>function of vC</td></tr><tr><td>hC</td><td>Mainline headway in the cooperative state</td><td>function of vC</td></tr><tr><td>m</td><td>Number of mainline cooperative vehicles</td><td>function of vCand d</td></tr><tr><td>ω</td><td>Shockwave speed</td><td>function of vC</td></tr><tr><td>d&#x27;</td><td>Distance between MP and EM</td><td>input parameter</td></tr><tr><td>vr</td><td>Arrival speed of ramp vehicles</td><td>input parameter</td></tr><tr><td>vcrit</td><td>Critical speed of mainline traffic</td><td>input parameter</td></tr><tr><td>λ</td><td>Arrival rate of ramp vehicles</td><td>input parameter</td></tr><tr><td>b</td><td>Braking rate of ramp vehicles when approaching WP</td><td>input parameter</td></tr><tr><td>amax</td><td>Maximum allowable acceleration of ramp vehicles</td><td>input parameter</td></tr><tr><td>nmax</td><td>Maximum length of a merging platoon</td><td>input parameter</td></tr></table>

following the facilitating vehicle (i.e., cooperative vehicles in Fig. 1) also slow down and accept a shorter car-following distance corresponding to the reduced speed. This transfers the mainline traffic behind the facilitating vehicle into a cooperative state (state C), characterized by a higher density and an increased flow rate in comparison to the original state. The transition of mainline traffic state provides space for the merging traffic; however, it also generates a shockwave that negatively affects the mainline traffic. If the coordination is initiated too frequently, the shockwaves may accumulate and eventually trigger traffic breakdowns in the merging area. To this end, it should be ensured in the coordination that the merging traffic is facilitated without breaking the mainline stability. 

Further, in a multilane freeway, vehicles in the inner lanes may change into the gaps created in the outer lane, if no additional control is applied, leading to a failure of the mainline-ramp coordination. Therefore, we recommend combining CoMC with the one-sided lane-change prohibition rule, which allows vehicles in the outermost lane to change into the inner lanes (the facilitating vehicle should not change lanes), while prohibiting vehicles in the inner lanes from entering the outermost lane. The lane-change prohibition covers the entire control segment (i.e., from the speed-change position to the end-of-merging position as shown in Fig. 1) and be effective during the whole coordination period. This measure prevents the created gaps from being occupied by the inner lane vehicles and at the meantime speed up the dissipation of shockwaves by allowing the outer lane vehicles to change lanes. 

The following assumptions are applied throughout this work: 

• $1 0 0 \%$ penetration rate of CAVs in the freeway network. 

• All vehicles are highly automated corresponding to SAE (2016) level 4. 

• The control center and relative vehicles are capable of real-time communication through vehicle to infrastructure (V2I) technologies. 

Note that, in each coordinative cycle, CoMC only controls the facilitating vehicle and the merging platoon leader, whereas the other vehicles obey the regular car-following rules. The main purpose of requiring a $1 0 0 \%$ CAV penetration rate is to ensure that any vehicle in the network can take the role of facilitating vehicle (for mainline vehicles) or platoon leader (for ramp vehicles). In addition, as CoMC adopts a centralized control framework, vehicle to vehicle (V2V) communication is not required, although it may benefit the system performance in terms of more efficient information transmission. 

The CoMC strategy is analytically formulated as a constrained optimization problem, incorporating macroscopic and microscopic traffic flow models, as defined through (1)–(15) with the notation in Table 1. The model minimizes the total delay to all vehicles passing through the ramp merging area, including the mainline cooperative vehicles and the ramp vehicles. Three variables are determined by the model, i.e., the merging platoon size $n _ { \scriptscriptstyle  { d } }$ , the mainline cooperative distance $d$ , and the cooperative speed $v _ { C }$ . The requirements on coordination, traffic stability, and vehicle dynamics are explicitly considered through the model constraints, where (7) requires the created mainline gap to be no smaller than the space needed for the merging platoon, (8) and (9) stipulate that the mainline traffic does not break due to the cooperative behaviors, (10) ensures a feasible acceleration rate of the merging platoon, and (14) and (15) describe the nature of the decision variables. In addition, this model expresses $q _ { C }$ , $k _ { C }$ , and $h _ { C }$ as functions of $v _ { C }$ , because the relationships between these variables are essentially defined by the fundamental diagram of traffic flow, which can be fitted to field data or derived from a recognized car-following model Jin, 2016). Theoretically, CoMC is compatible with any 

form of fundamental diagram. Without loss of generality, we use the fundamental diagram derived from the Wiedemann 99 carfollowing model (Wiedemann, 1991) in this paper, as defined in ((11)–(13). We refer to Zhu et al. (2021) for detailed derivations and explanations on the model formulation and the solution methods. 

$$
\min  D = \left(w _ {m} \cdot \sum_ {i = 1} ^ {m} D _ {\text {m a i n}} ^ {i} + w _ {r} \cdot \sum_ {j = 1} ^ {n} D _ {\text {r a m p}} ^ {j}\right) \times r \tag {1}
$$

with 

$$
\sum_ {i = 1} ^ {m} D _ {m a i n} ^ {i} = \frac {m \cdot (v _ {O} - v _ {C})}{v _ {C}} \times \left[ \frac {d + d ^ {\prime}}{v _ {O}} - \frac {(m - 1) \omega h _ {O}}{2 (v _ {O} - \omega)} \right] \tag {2}
$$

$$
\sum_ {j = 1} ^ {n} D _ {r a m p} ^ {j} = n \times \left(\frac {v _ {r}}{2 b} + \frac {d + d ^ {\prime}}{v _ {C}} - n h _ {C} - \frac {d - n h _ {C} v _ {C}}{2 v _ {r}} - \frac {d ^ {\prime}}{v _ {O}} + \frac {n - 1}{2 \lambda}\right) \tag {3}
$$

$$
r = \frac {3 6 0 0 \lambda}{n} \tag {4}
$$

$$
m = \left[ \frac {d + d ^ {\prime}}{h _ {O}} \times \left(\frac {1}{\omega} - \frac {1}{v _ {O}}\right) \right] \tag {5}
$$

$$
\omega = \frac {q _ {C} - q _ {O}}{k _ {C} - k _ {O}} \tag {6}
$$

subject to 

$$
h _ {O} + \frac {d}{v _ {C}} - \frac {d}{v _ {O}} \geq (n + 1) \cdot h _ {C} \tag {7}
$$

$$
\frac {n}{\lambda} \geq \frac {d + d ^ {\prime}}{\omega} \tag {8}
$$

$$
v _ {c r i t} \leq v _ {C} \leq v _ {O} \tag {9}
$$

$$
a \leq a _ {\max } \tag {10}
$$

$$
h _ {C} = \frac {C C 0 + L + C C 1 * v _ {C}}{v _ {C}} \tag {11}
$$

$$
q _ {C} = 1 / h _ {C} \tag {12}
$$

$$
k _ {C} = q _ {C} / v _ {C} \tag {13}
$$

$$
n \leq n _ {\max }, n \in \mathbb {N} ^ {+} \tag {14}
$$

$$
d > 0 \tag {15}
$$

Note that, in a multilane configuration, the ramp traffic is coordinated with the mainline traffic in the outer lane. Thus, the traffic volume in the outer lane should be estimated and used as the original flow rate of coordination $\left( q _ { O } \right)$ . Under the CoMC control, when the facilitating vehicle decelerates, the vehicles following it in the outer lane tend to change into the inner lanes to maintain a higher speed. We assume a two-lane freeway where the traffic volume in the upstream road segment is evenly distributed between lanes (see Fig. 2), and the number of vehicles changing into the inner lane depends on the ability of the inner lane to accommodate extra vehicles. The remaining outer lane volume for coordination is estimated as 

$$
q _ {O} = q _ {m} - \rho \cdot (C - q _ {m}) \tag {16}
$$

where $q _ { m }$ is the upstream mainline volume per lane, $C$ is the theoretical capacity of the inner lane which is defined by the fundamental diagram of traffic flow, and $\rho \epsilon [ 0 , 1 ]$ captures the number of lane-changing vehicles as a fraction of the reserved inner lane capacity (i.e., $C - q _ { m } )$ . The impacts of $\rho$ is discussed in detail in Section 3.3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/c6bf67004f42365ddf16f2c9dddb54b5d42c4fea058d4b36800f8a7a9265f5de.jpg)



Fig. 2. Effective outer lane flow rate.



Table 2 Input parameter.


<table><tr><td>Parameter</td><td>Value</td><td>Unit</td><td>Source</td></tr><tr><td>\( v_{O} \)</td><td>120</td><td>km/h</td><td>TRB (2016)</td></tr><tr><td>\( v_{r} \)</td><td>60</td><td>km/h</td><td>TRB (2016)</td></tr><tr><td>\( d^{\prime } \)</td><td>457.2</td><td>m</td><td>TRB (2016)</td></tr><tr><td>\( v_{crit} \)</td><td>75</td><td>km/h</td><td>Geistefeldt et al. (2017)</td></tr><tr><td>b</td><td>2.75</td><td>\( m/s^{2} \)</td><td>AASHTO (2018)</td></tr><tr><td>\( a_{max} \)</td><td>2.75</td><td>\( m/s^{2} \)</td><td>AASHTO (2018)</td></tr><tr><td>\( n_{max} \)</td><td>20</td><td>veh</td><td>-</td></tr><tr><td>ρ</td><td>0.5</td><td>-</td><td>-</td></tr><tr><td>CC0</td><td>1.5</td><td>m</td><td>PTV (2018)</td></tr><tr><td>CC1</td><td>0.9</td><td>s</td><td>PTV (2018)</td></tr><tr><td>L</td><td>4.37</td><td>m</td><td>PTV (2018)</td></tr></table>


Table 3 Sensitivity analysis on weight parameters.


<table><tr><td colspan="12">(a) CoMC control plan for mainline volume 2000 veh/h/ln and ramp volume 500 veh/h</td></tr><tr><td>wm</td><td>0.0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td><td>1.0</td></tr><tr><td>wr</td><td>1.0</td><td>0.9</td><td>0.8</td><td>0.7</td><td>0.6</td><td>0.5</td><td>0.4</td><td>0.3</td><td>0.2</td><td>0.1</td><td>0.0</td></tr><tr><td>VC(km/h)</td><td>85.4</td><td>85.4</td><td>85.4</td><td>85.4</td><td>85.4</td><td>85.4</td><td>85.4</td><td>85.4</td><td>85.4</td><td>88.0</td><td>89.6</td></tr><tr><td>d(m)</td><td>1044</td><td>1044</td><td>1044</td><td>1044</td><td>1044</td><td>1044</td><td>1044</td><td>1044</td><td>1044</td><td>1260</td><td>1458</td></tr><tr><td>n(veh)</td><td>11</td><td>11</td><td>11</td><td>11</td><td>11</td><td>11</td><td>11</td><td>11</td><td>11</td><td>12</td><td>13</td></tr><tr><td colspan="12">(b) CoMC control plan for mainline volume 2200 veh/h/ln and ramp volume 500 veh/h</td></tr><tr><td>wm</td><td>0.0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td><td>1.0</td></tr><tr><td>wr</td><td>1.0</td><td>0.9</td><td>0.8</td><td>0.7</td><td>0.6</td><td>-0.5</td><td>-0.4</td><td>-0.3</td><td>-0.2</td><td>-0.1</td><td>-0.0</td></tr><tr><td>VC(km/h)</td><td>81.1</td><td>81.1</td><td>81.1</td><td>81.1</td><td>81.1</td><td>81.1</td><td>81.1</td><td>81.1</td><td>84.8</td><td>84.8</td><td>86.6</td></tr><tr><td>d(m)</td><td>1136</td><td>1136</td><td>1136</td><td>1136</td><td>1136</td><td>1136</td><td>1136</td><td>1136</td><td>1391</td><td>1391</td><td>1593</td></tr><tr><td>n(veh)</td><td>14</td><td>14</td><td>14</td><td>14</td><td>14</td><td>14</td><td>14</td><td>14</td><td>15</td><td>15</td><td>16</td></tr></table>

# 3.2. Impacts of weight choice

The weight parameters $w _ { m }$ and $w _ { r }$ adjust the priority of the mainline and ramp traffic in the coordination and have an impact on the optimal CoMC decisions. We conduct a sensitivity analysis where the values of $w _ { m }$ and $w _ { r }$ vary from 0 to 1 (with $w _ { m } + w _ { r } = 1 \textgreater$ ) for the parameters in Table 2. The results for two demand scenarios (mainline volume 2000 and 2200 veh/h/ln with ramp volume 500 veh/h) are presented in Table 3. 

As Table 3 shows, when the mainline traffic is prioritized (i.e., larger $w _ { m } .$ ), CoMC tends to form larger merging platoons to reduce the frequency of coordination, and the mainline cooperative speed is higher in comparison with the case of lower mainline priority. In addition, it is noted for both demand levels that the coordinationd decisions remain the same when $w _ { m }$ changes between 0 and 0.7, implying that CoMC tends to prioritize the ramp efficiency when the mainline and ramp traffic have similar weights. For example, see Table 3, the case $w _ { m } = w _ { r } = 0 . 5$ has the same coordination decisions as the case $w _ { m } = 0$ at both demand levels. This is because under such coordination where the ramp vehicles are forced to stop and give way to the mainline vehicles, the ramp traffic inherently experiences larger delays in comparison to the mainline traffic, so the control tends to minimize the dominating ramp delay for an improvement in the overall efficiency. In the following analysis, we use $w _ { m } = w _ { r }$ to treat each vehicle (regardless of whether it is from mainline or on-ramp) evenly. 

# 3.3. Impacts of cooperative lane changes

The parameter $\rho$ describes the proportion of reserved inner lane capacity that is utilized by the vehicles changing from the outer lane. Its value affects the effective outer lane flow rate in the original state $\left( q _ { O } \right)$ and thus the control decisions of CoMC. Fig. 3 shows the maximum on-ramp flow that is accommodated by CoMC with respect to the mainline volume for the parameters in Table 2 and $w _ { m } = w _ { r }$ . With a larger value of $\rho$ (i.e., more outer lane vehicles changing to the inner lane ), more space can be collected in the outer 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/d7b295468d5b66ec4116604a6ce24a365d6405b3ac3ac6fb21f4ef07023a4db0.jpg)



Fig. 3. Maximum on-ramp flow with respect to mainline flow.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/70120902f910de9dcc60ec06a16b21b03dae64f1bbd7f8c5a45d4c41e0198b4b.jpg)



Fig. 4. Graphical representation of the simulation network.



Table 4 CoMC control plan for different $\rho$ values (mainline volume 2000 veh/h/ln, ramp volume 500 veh/h, $w _ { m } = w _ { r }$ ??)


<table><tr><td>ρ</td><td>0.0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td><td>1.0</td></tr><tr><td>vc(km/h)</td><td>No</td><td>80.1</td><td>83.5</td><td>83.3</td><td>85.0</td><td>85.4</td><td>84.9</td><td>82.9</td><td>86.1</td><td>82.8</td><td>85.5</td></tr><tr><td>d(m)</td><td>solution</td><td>1331</td><td>1324</td><td>1142</td><td>1120</td><td>1044</td><td>930</td><td>781</td><td>878</td><td>692</td><td>765</td></tr><tr><td>n(veh)</td><td></td><td>17</td><td>15</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>9</td><td>8</td><td>8</td></tr></table>

lane to facilitate the merging of ramp vehicles, so the maximum accommodated on-ramp flow increases. For example, the maximum ramp flow increases from 551 veh/h to 690 veh/h (approximately $2 5 . 2 \%$ ) when $\rho$ increases from 0.2 to 0.8 at a mainline volume of 2000 veh/h/ln. 

Table 4 presents the CoMC decisions of an example scenario (mainline volume 2000 veh/h/ln and ramp volume 500 veh/h) under different values of $\rho$ . It shows that the required merging platoon size $\mathbf { \mu } ( { n } )$ decreases as $\rho$ increases. This is because when more vehicles change into the inner lane, the shockwave in the outer lane dissipates faster, and the coordination is implemented more frequently (i.e., at the formation of a smaller merging platoon with fewer vehicles). The frequent coordination improves the efficiency of ramp vehicles by reducing their waiting time on the ramp. In addition, since a smaller merging platoon requires less space on the main road, the facilitating vehicle decelerates at a later SC position (i.e., smaller value of $d$ ) and maintains a higher cooperative speed (i.e., larger value of $v _ { C }$ ) with the larger $\rho$ value. 

In summary, a larger value of $\rho$ implies more changes from the outer lane to the inner lane, which promotes the merging operation because it essentially makes fuller use of the inner lane space for the merging of ramp vehicles. A low value of $\rho$ may lead to a waste of the inner lane capacity and even result in failed coordination (e.g., the model has no solution for $\rho = 0$ in Table 4). On the other hand, an excessively high value of $\rho$ , implying frequent changes into the inner lane, may overload the inner lane and break the stability of the upstream traffic. Thus, it is important to determine a reasonable $\rho$ value that balances the merging efficiency and the mainline stability. Note that, with the presence of a centralized control system, it is possible to centrally determine the optimal value of $\rho$ and plan the cooperative lane changes based on real-time traffic conditions. Such a system is part of our on-going research. 


(a) Travel time (mainline flow 160o veh/h)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/cf3d80776bddc95e7de7611e0161883f3e33d6a92c04aea5bad672c794d7d22f.jpg)



(b)Travel time (mainline flow 180o veh/h)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/9464e37c9ceddfcd85ecc621eea5b4c57cdf7e2aecf37efad058807e026fef5e.jpg)



(c)Delay (mainline flow 160o veh/h)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/6c54bf242e56cbf7aedff281628fcaf7cad26c23b5e16c8c386099aa323bf8d4.jpg)



(d) Delay (mainline flow 180o veh/h)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/db5d25a1227b97bf743899941c1ea1c1243bd26b8883ff3e1496780c3d896198.jpg)



Fig. 5. Changes in travel time and delay.



Table 5 Simulation scenarios and CoMC control plan.


<table><tr><td>Scenario</td><td></td><td>1A</td><td>1B</td><td>1C</td><td>2A</td><td>2B</td><td>2C</td><td>Unit</td></tr><tr><td rowspan="2">Volume</td><td>qm</td><td>2000</td><td>2000</td><td>2000</td><td>2200</td><td>2200</td><td>2200</td><td>veh/h/ln</td></tr><tr><td>qr</td><td>300</td><td>400</td><td>500</td><td>300</td><td>400</td><td>500</td><td>veh/h</td></tr><tr><td>CoMC</td><td>VC</td><td>98.5</td><td>92.9</td><td>85.4</td><td>100.0</td><td>90.1</td><td>81.1</td><td>km/h</td></tr><tr><td rowspan="2">Control</td><td>d</td><td>687</td><td>909</td><td>1044</td><td>934</td><td>917</td><td>1137</td><td>m</td></tr><tr><td>n</td><td>4</td><td>7</td><td>11</td><td>5</td><td>8</td><td>14</td><td>veh</td></tr></table>

# 4. Case study

In this section, we conduct an illustrative case study through microscopic simulation to demonstrate the efficiency of CoMC in a multilane freeway configuration. Section 4.1. introduces the simulation experiments, and the results and discussions are provided in Section 4.2. 

# 4.1. Simulation experiment

The experiments are conducted on a VISSIM-based microscopic simulation platform, where the internal VISSIM model is used to create the road network, generate traffic demands, control regular following/lane-changing decisions of vehicles, and record raw data for the performance analysis (PTV, 2018). It is shown that the default VISSIM following/lane-changing models are capable of reproducing realistic traffic dynamics at on-ramp merging (Marinescu et al., 2012 Scarinci et al., 2017; Xie et al., 2017; Hu and Sun, 2019;). The centralized control of CoMC is compiled in Python and called by VISSIM via the COM interface. Specifically, VISSIM passes real-time traffic information (e.g., path, position, and speed of vehicles) to Python at each time step, and Python calculates the decisions of CoMC accordingly and return them to VISSIM. When the coordination is in progress, the dynamics of the facilitating vehicle and the merging platoon leader (i.e., the required speed adaption) is controlled by external driving models coded in $^ { \mathrm { C + + } }$ . The activation and deactivation of external driving models are determined in the Python script. 

Fig. 4 shows the simulation network of a merging area with two lanes on the freeway and one-lane on the ramp. The freeway consists of a 2000 m upstream segment, a 240 m merging area, and a $5 0 0 ~ \mathrm { m }$ downstream segment. A 700 m on-ramp is connected to the merging area via a parallel acceleration lane. Only one-direction traffic is modeled, as the opposing traffic operates in a symmetrical way. One-sided lane-change prohibition is applied in and near the merging area as introduced in Section 3.1. 

The performance of CoMC is evaluated in six demand scenarios with relatively high traffic demands, combing two levels of mainstream volume (2000 and 2200 veh/h/ln) and three levels of on-ramp volume (300, 400, and 500 veh/h). The scenarios and the corresponding CoMC decisions, solved for parameters in Table 2 and $w _ { m } = w _ { r }$ , are summarized in Table 5. We focus on high traffic volume scenarios because CoMC is dedicated to stabilizing traffic and promoting merging in the critical near-capacity situations. Under low demand situations where the traffic is well self-sustained, a centralized control like CoMC may not be needed. Relevant issues on this point is discussed in detail in Zhu et al. (2021). For each demand scenario, we conduct 10 simulation runs with different random seeds (each lasting 7200 simulation seconds) for the cases with CoMC (i.e., the CoMC case) and without CoMC (i.e., the base case). Based on the results aggregated over 10 runs, the efficiency of the CoMC and base cases are compared to each other in terms of travel time, delay, and vehicle speed. 

To reproduce the fluctuating nature of traffic flow, vehicles are generated at randomized intervals in the simulation. Therefore, the original distance between a facilitating vehicle and its leader on the main road is different across merging cycles. When a large original gap already exists before the coordination, the facilitating vehicle can decelerate at a later position and still expand the gap to the required size. The deferred deceleration reduces the delay to the mainline vehicles without affecting the effectiveness of coordination. In view of this, we introduce a microscopic mechanism to fine-tune the actual speed-change position in each merging cycle according to the initial position of the facilitating vehicle, as in (17). 

$$
d ^ {*} = d - \frac {\left(P _ {f} - d\right) v _ {C}}{v _ {f} - v _ {C}} \tag {17}
$$

Here, $d ^ { * }$ is the actual speed-change position defined by its distance to the merging point. $P _ { f }$ and $v _ { f }$ are the position and speed of the facilitating vehicle when it accepts the coordination request. During the simulation, CoMC always appoints the first mainline vehicle behind the SC position as the facilitating vehicle, so $P _ { f } \geq d$ always holds. At the micro-level, $d$ and $v _ { C }$ are determined by the macroscopic CoMC decisions and remain unchanged across merging cycles, whereas $P _ { f }$ and $v _ { f }$ are updated in each merging cycle to determine $d ^ { * }$ . This adaption enhances the adaptivity of CoMC by taking into account traffic variations at the micro-level. 

# 5. Result and discussion

Table 6 and Fig. 5 present the travel time and delay results. Travel time is measured as the total time that a vehicle takes to pass across the road network, except for the first $1 0 0 ~ \mathrm { { m } }$ of the upstream links and the last $1 0 0 ~ \mathrm { { m } }$ of the downstream link. Delay is the difference between the measured travel time and the theoretical ideal travel time that corresponds to the length and design speed of links in the vehicle path. The travel time and delay are measured separately for the mainline and ramp vehicles, so as to reveal the different effects of CoMC on vehicles in different paths. The results over all vehicles are also reported to indicate the overall traffic efficiency. According to the results, the effects of CoMC is less remarkable in the scenarios with relatively low volumes, such as 1A and 1B, because the traffic only experience minor delays (overall less than 10 s) even without external control. For scenarios 1A to 2B, CoMC mainly improves the efficiency of ramp traffic, because in the uncontrolled base cases, the ramp vehicles hardly find acceptable merging gaps due to the high mainline volume, whereas CoMC solves this problem by creating readily available gaps at 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/11d01042257ba5ce09e87dfca20b80ceb2bcadda29a87a74be88428c3c82fe62.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/3ef714eebb0b30d4674c73732f1bb5469c65f4017ec693e12eaf50a2d9ffafea.jpg)



Fig. 6. Speed contour.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/ced5b3c3c6b554a4ee206c158f77edc2ed1aca94f066d6c5f5f3be2d29911306.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/3a8d86d79cf9a1afc1b112724a607359c392bd9225af7f1728e0cdc2909823bb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/10874d848cb6e3b705e6db250dba1d111a42faba394c2564e519b623ee46ce29.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/21be5400ffca53c96a8a8d84485fd65e5086308c4dbbe94550b679da214a3757.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/8293ccebae071a6b86107fa5f5efeb1ea4c1adf4580bc84145e790d59f03c8e7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/e894456e131a3bed5180521847cce37ff7011156e1edb79343c4e250db3f6af1.jpg)



Fig. 6. Continued


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/9654b763517af8966ed3ef99a4bde1e9d92a6942005158f7eac6237b3ee6054e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/7cf05040fc968f9d2b981bdf9bada23d83bc3765887902a1b276c13a88ce1bdf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/bff414f67d5bfc1e70fa4f87fe9fac3985c99f6d00ea8e734408a6eb1fe309e8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/2e2530c5-7a0f-4c60-98b5-1ace2abaa695/03ad20c3810506818ca1db67ff9dc15379ad62966002c60bb8d9ba5e940bd7c6.jpg)



Fig. 6. Continued



Table 6 Travel time and delay results.


<table><tr><td>Scenario</td><td></td><td>Mainline travel time [s]</td><td>Ramp travel time [s]</td><td>Overall travel time [s]</td><td>Mainline delay [s]</td><td>Ramp delay [s]</td><td>Overall delay [s]</td></tr><tr><td>1A</td><td>base</td><td>77.89</td><td>89.35</td><td>78.68</td><td>1.69</td><td>34.15</td><td>3.93</td></tr><tr><td>(2000,300)</td><td>CoMC</td><td>77.43</td><td>76.46</td><td>77.36</td><td>1.23</td><td>21.26</td><td>2.63</td></tr><tr><td>1B</td><td>base</td><td>79.62</td><td>97.16</td><td>81.22</td><td>3.42</td><td>41.96</td><td>6.93</td></tr><tr><td>(2000,400)</td><td>CoMC</td><td>77.72</td><td>86.69</td><td>78.53</td><td>1.52</td><td>31.49</td><td>4.24</td></tr><tr><td>1C</td><td>base</td><td>83.10</td><td>106.45</td><td>85.70</td><td>6.90</td><td>51.25</td><td>11.83</td></tr><tr><td>(2000,500)</td><td>CoMC</td><td>78.41</td><td>97.05</td><td>80.48</td><td>2.21</td><td>41.85</td><td>6.61</td></tr><tr><td>2A</td><td>base</td><td>81.18</td><td>115.29</td><td>83.35</td><td>4.98</td><td>60.09</td><td>8.49</td></tr><tr><td>(2200,300)</td><td>CoMC</td><td>78.41</td><td>84.22</td><td>78.78</td><td>2.21</td><td>29.02</td><td>3.92</td></tr><tr><td>2B</td><td>base</td><td>88.82</td><td>124.13</td><td>91.67</td><td>12.62</td><td>68.93</td><td>17.17</td></tr><tr><td>(2200,400)</td><td>CoMC</td><td>79.66</td><td>91.93</td><td>80.68</td><td>3.46</td><td>36.73</td><td>6.23</td></tr><tr><td>2C</td><td>base</td><td>155.52</td><td>129.74</td><td>152.83</td><td>79.32</td><td>74.54</td><td>78.82</td></tr><tr><td>(2200,500)</td><td>CoMC</td><td>81.90</td><td>110.25</td><td>84.78</td><td>5.70</td><td>55.05</td><td>10.72</td></tr></table>

the merging point. For the most critical scenario 2C, CoMC is shown to improve both the mainline and ramp efficiencies substantially with an $8 6 . 4 \%$ reduction in the overall delay in comparison to the base case. 

In Fig. 6, we illustrate how the aggregated vehicle speed changes across space and time in different scenarios. The speed data are collected at five-minutes intervals on the road segment between $5 0 0 \mathrm { m }$ and $2 0 0 0 \mathrm { m }$ along the mainline freeway at a space resolution of $1 0 0 ~ \mathrm { { m } }$ . This range covers the merging area (i.e., between 2000 to $2 2 4 0 ~ \mathrm { m }$ ) and the upstream and downstream influence areas as defined in TRB (2016). The results are aggregated over all lanes (i.e., three lanes in the merging area and two lanes in the upstream and downstream segments) and all simulation runs of a scenario. According to the results, the CoMC case outperforms the base case 

at all demand levels in terms of less reductions in the vehicle speed. With CoMC, the speed remains above $9 5 \mathrm { k m / h }$ across the entire road segment and simulation period. In the base case of the most critical 2C scenario, the pattern of speed reduction persists and extends backwards along the main road (see Fig. 6k). The speed even drops below the critical mainline speed in the later stage of the simulation, indicating onsets of traffic congestions. Such congestions are successfully prevented when CoMC is applied (Fig. 6l). In addition, it is noted that speed reduction in the base cases mainly originates from the merging area , whereas in the CoMC cases, the speed reduction is evenly distributed in the merging area and the upstream segment corresponding to the cooperative range. This implies that CoMC essentially shifts part of the disturbances in the merging area to the nearby road segments, thereby reducing the intensity of the negative impacts. 

# 6. Conclusion

In this paper, we present a flow-level CAV coordination strategy as a significant extension to Zhu et al. (2021) to facilitate the merging operation in multilane freeway on-ramp bottlenecks. The strategy considers lane-changes between mainstream lanes and coordinates the ramp merging traffic with the mainline traffic in the outermost lane through proactive gap creation and platoon merging. One-sided lane-change prohibition rule is integrated to protect the created outer lane gaps from being occupied by the inner lane vehicles. The strategy is formulated as an optimization problem which determines the most efficient coordination plan adaptive to the real-time traffic state. Extended discussions on mainline-ramp priority and the proportion of lane-changes on the main road are provided. The efficiency of the proposed coordination is further demonstrated in a microsimulation-based case study where traffic from a one-lane on-ramp merge into a two-lane freeway. The results show that the coordination functions as expected in the simulated multilane environment and substantially improves the traffic flow efficiency at ramp merging, especially under high traffic volume conditions. The main contributions of this paper are summarized as below: (1) it coordinates the two streams of traffic (instead of individual vehicles) for the flow-level efficiency gains at ramp merging; (2) it applies to the more prevailing multilane freeway configurations. 

It is worth noting that in a multilane configuration, the lane-changing behaviors between mainstream lanes are important to the performance of traffic operation, as discussed in Section 3.3. Therefore, it is beneficial to determine the optimal proportion of lane-changing vehicles, or more sophisticated, the exact vehicles to change lanes, based on the traffic conditions. This leaves an open question for future research. Further, the current strategy requires a $1 0 0 \%$ penetration rate of CAVs to ensure that any vehicle in the network can take the role of facilitating vehicle or platoon leader. This limit can be relaxed in the future research by adding a mechanism to assign the vehicles’ roles based on their capabilities, so that the strategy is transferred to the mixed CAV-HDV traffic. In addition, as this study focuses on the formulation and validation of the proposed multi-lane strategy, assumptions on CAV capabilities, such as instantaneous communications and precise motion controls, are adopted. These should be further investigated in the future for an implementation in the real-world. 

# Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Acknowledgment

The authors are grateful to the Area of Advance Transport at Chalmers University of Technology for funding this research. 

# Reference



AASHTO, 2018. A Policy on Geometric Design of Highways and Streets, 7th ed. American Association of State Highway and Transportation Officials, Washington, D.C.. 





Cao, D., Wu, J., Wu, J., Kulcsár, B., Qu, X., 2021. A platoon regulation algorithm to improve the traffic performance of highway work zones. Comput. Aided Civ. Infrastruct. Eng. 36 (7), 941–956. 





Cao, W., Mukai, M., Kawabe, T., Nishira, H., Fujiki, N., 2015. Cooperative vehicle path generation during merging using model predictive control with real-time optimization. Control Eng. Pract. 34, 98–105. 





Carlson, R.C., Papamichail, I., Papageorgiou, M., 2011. Local feedback-based mainstream traffic flow control on motorways using variable speed limits. IEEE Trans. Intell. Transp. Syst. 12 (4), 1261–1276. 





Carlson, R.C., Papamichail, I., Papageorgiou, M., Messmer, A., 2010. Optimal motorway traffic flow control involving variable speed limits and ramp metering. Transp. Sci. 44 (2), 238–253. 





Cassidy, M.J., Bertini, R.L., 1999. Some traffic features at freeway bottlenecks. Transp. Res. Part B Methodol. 33 (1), 25–42. 





Chen, D., Ahn, S., Hegyi, A., 2014. Variable speed limit control for steady and oscillatory queues at fixed freeway bottlenecks. Transp. Res. Part B Methodol. 70, 340–358. 





Chen, D., Srivastava, A., Ahn, S., 2021. Harnessing connected and automated vehicle technologies to control lane changes at freeway merge bottlenecks in mixed traffic. Transp. Res. Part C Emerg. Technol. 123, 102950. 





Chen, N., van Arem, B., Alkim, T., Wang, M., 2020. A hierarchical model-based optimization control approach for cooperative merging by connected automated vehicles. IEEE Trans. Intell. Transp. Syst. (Early Access). 





Debada, E.G., Gillet, D., 2018. Virtual vehicle-based cooperative maneuver planning for connected automated vehicles at single-lane roundabouts. IEEE Intell. Transp. Syst. Mag. 104, 35–46. 





Ding, J., Li, L., Peng, H., Zhang, Y., 2020. A rule-based cooperative merging strategy for connected and automated vehicles. IEEE Trans. Intell. Transp. Syst. 21 (8), 3436–3446. 





Fukuyama, S., 2020. Dynamic game-based approach for optimizing merging vehicle trajectories using time-expanded decision diagram. Transp. Res. Part C Emerg. Technol. 120, 102766. 





Geistefeldt, J., Giuliani, S., Busch, F., Schendzielorz, T., Haug, A., Vortisch, P., Leyn, U., Trapp, R., 2017. HBS-konforme simulation des Verkehrsablaufs auf Autobahnen. Berichte der Bundesanstalt fuer Strassenwesen. Unterreihe Verkehrstechnik(279). 





Gomes, G., Horowitz, R., 2006. Optimal freeway ramp metering using the asymmetric cell transmission model. Transp. Res. Part C Emerg. Technol. 14 (4), 244–262. 





Han, Y., Ahn, S., 2018. Stochastic modeling of breakdown at freeway merge bottleneck and traffic control method using connected automated vehicle. Transp. Res. Part B Methodol. 107, 146–166. 





Hegyi, A., De Schutter, B., Hellendoorn, H., 2005. Model predictive control for optimal coordination of ramp metering and variable speed limits. Transp. Res. Part C Emerg. Technol. 13 (3), 185–209. 





Hu, X., Sun, J., 2019. Trajectory optimization of connected and autonomous vehicles at a multilane freeway merging area. Transp. Res. Part C Emerg. Technol. 101, 111–125. 





Jin, W.L., 2016. On the equivalence between continuum and car-following models of traffic flow. Transp. Res. Part B Methodol. 93, 543–559. 





Jing, S., Hui, F., Zhao, X., Rios-Torres, J., Khattak, A.J., 2019. Cooperative game approach to optimal merging sequence and on-ramp merging control of connected and automated vehicles. IEEE Trans. Intell. Transp. Syst. 20 (11), 4234–4244. 





Karbalaieali, S., Osman, O.A., Ishak, S., 2020. A dynamic adaptive algorithm for merging into platoons in connected automated environments. IEEE Trans. Intell. Transp. Syst. 21 (10), 4111–4122. 





Karimi, M., Roncoli, C., Alecsandru, C., Papageorgiou, M., 2020. Cooperative merging control via trajectory optimization in mixed vehicular traffic. Transp. Res. Part C Emerg. Technol. 116, 102663. 





Letter, C., Elefteriadou, L., 2017. Efficient control of fully automated connected vehicles at freeway merge segments. Transp. Res. Part C Emerg. Technol. 80, 190–205. 





Lu, X., Varaiya, P., Horowitz, R., Su, D., Shladover, S.E., 2011. Novel freeway traffic control with variable speed limit and coordinated ramp metering. Transp. Res. Rec. 2229 (1), 55–65. 





Marinescu, D., Čurn, J., Bouroche, M., Cahill, V., 2012. On-ramp traffic merging using cooperative intelligent vehicles: a slot-based approach. In: Proceedings of the 15th International IEEE Conference on Intelligent Transportation Systems, IEEE. 





Mergia, W.Y., Eustace, D., Chimba, D., Qumsiyeh, M., 2013. Exploring factors contributing to injury severity at freeway merging and diverging locations in Ohio. Accident Anal. Prev. 55, 202–210. 





Mirheli, A., Tajalli, M., Hajibabai, L., Hajbabaie, A., 2019. A consensus-based distributed trajectory control in a signal-free intersection. Transp. Res. Part C Emerg. Technol. 100, 161–176. 





Mirshahi, M., Obenberger, J., Fuhs, C.A., Howard, C.E., Krammes, R.A., Kuhn, B.T., Mayhew, R.M., Moore, M.A., Sahebjam, K., Stone, C.J., 2007. Active Traffic Management: The Next Step in Congestion Management, United States. Federal Highway Administration. 





Ntousakis, I.A., Nikolos, I.K., Papageorgiou, M., 2016. Optimal vehicle trajectory planning in the context of cooperative merging on highways. Transp. Res. Part C Emerg. Technol. 71, 464–488. 





Omidvar, A., Elefteriadou, L., Pourmehrab, M., Letter, C., 2020. Optimizing freeway merge operations under conventional and automated vehicle traffic. J. Transp. Eng. Part A Syst. 146 (7), 04020059. 





Papageorgiou, M., Hadj-Salem, H., Blosseville, J.M., 1991. ALINEA: a local feedback control law for on-ramp metering. Transp. Res. Rec. 1320 (1), 58–67. 





Papamichail, I., Kampitaki, K., Papageorgiou, M., Messmer, A., 2008. Integrated ramp metering and variable speed limit control of motorway traffic flow. IFAC Proc. Vol. 41 (2), 14084–14089. 





Papamichail, I., Kotsialos, A., Margonis, I., Papageorgiou, M., 2010. Coordinated ramp metering for freeway networks–a model-predictive hierarchical control approach. Transp. Res. Part C Emerg. Technol. 18 (3), 311–331. 





PTV, 2018. PTV VISSIM 11 user manual. Karlsruhe, PTV AG. 





Qu, X., Yu, Y., Zhou, M., Lin, C.T., Wang, X., 2020. Jointly dampening traffic oscillations and improving energy consumption with electric, connected and automated vehicles: a reinforcement learning based approach. Appl. Energy 257, 114030. 





Rios-Torres, J., Malikopoulos, A.A., 2017a. Automated and cooperative vehicle merging at highway on-ramps. IEEE Trans. Intell. Transp. Syst. 18 (4), 780–789. 





Rios-Torres, J., Malikopoulos, A.A., 2017b. A survey on the coordination of connected and automated vehicles at intersections and merging at highway on-ramps. IEEE Trans. Intell. Transp. Syst. 18 (5), 1066–1077. 





SAE, 2016. Taxonomy and definitions for terms related to on-road motor vehicle automated driving systems: 16-25. 





Scarinci, R., Hegyi, A., Heydecker, B., 2017. Definition of a merging assistant strategy using intelligent vehicles. Transp. Res. Part C Emerg. Technol. 82, 161–179. 





Scarinci, R., Heydecker, B., 2014. Overview of algorithms for freeway on-ramp merging using intelligent vehicles. In: Proceedings of the 93rd Annual Meeting Transportation Research Board. Washington DC, United States. 





Smaragdis, E., Papageorgiou, M., Kosmatopoulos, E., 2004. A flow-maximizing adaptive local ramp metering strategy. Transp. Res. Part B Methodol. 38 (3), 251–270. 





Sonbolestan, M.R., Monajjem, S., Rouhani, E., 2021. Impact of optimal selection of merging position on fuel consumption at highway on-ramps. J. Transp. Eng. Part A Syst. 147 (5), 04021023. 





Srivastava, A., Geroliminis, N., 2013. Empirical observations of capacity drop in freeway merges with ramp control and integration in a first-order model. Transp. Res. Part C Emerg. Technol. 30, 161–177. 





Sun, Z., Huang, T., Zhang, P., 2020. Cooperative decision-making for mixed traffic: a ramp merging example. Transp. Res. Part C Emerg. Technol. 120, 102764. 





TRB, 2016. Highway Capacity Manual - A Guide for Multimodal Mobility Analysis, 6th ed. Transportation Research Board. 





Wang, L., Abdel-Aty, M., Lee, J., Shi, Q., 2019. Analysis of real-time crash risk for expressway ramps using traffic, geometric, trip generation, and socio-demographic predictors. Accident Anal. Prev. 122, 378–384. 





Wang, Y., E, W., Tang, W., Tian, D., Lu, G., Yu, G., 2013. Automated on-ramp merging control algorithm based on Internet-connected vehicles. IET Intell. Transport Syst. 7 (4), 371–379. 





Wiedemann, R., 1991. Modelling of RTI-elements on multi-lane roads. In: Proceedings of the Drive Conference. Brussels, Belgium. 





Wu, J., Ahn, S., Zhou, Y., Liu, P., Qu, X., 2021. The cooperative sorting strategy for connected and automated vehicle platoons. Transp. Res. Part C Emerg. Technol. 123, 102986. 





Wu, J., Kulcsár, B., Ahn, S., Qu, X., 2020. Emergency vehicle lane pre-clearing: from microscopic cooperation to routing decision making. Transp. Res. Part B Methodol. 141, 223–239. 





Xie, Y., Zhang, H., Gartner, N.H., Arsava, T., 2017. Collaborative merging strategy for freeway ramp operations in a connected and autonomous vehicles environment. J. Intell. Transp. Syst. 21 (2), 136–147. 





Xu, Y., Zheng, Y., Yang, Y., 2021. On the movement simulations of electric vehicles: a behavioral model-based approach. Appl. Energy 283, 116356. 





Zhang, H., Li, Z., Liu, P., Xu, C., Yu, H., 2013. Control strategy of variable speed limits for improving traffic efficiency at merge bottleneck on freeway. Procedia Soc. Behav. Sci. 96, 2011–2023. 





Zhou, M., Qu, X., Jin, S., 2017. On the impact of cooperative autonomous vehicles in improving freeway merging: a modified intelligent driver model-based approach. IEEE Trans. Intell. Transp. Syst. 18 (6), 1422–1428. 





Zhou, M., Yu, Y., Qu, X., 2020. Development of an efficient driving strategy for connected and automated vehicles at signalized intersections: a reinforcement learning approach. IEEE Trans. Intell. Transp. Syst. 21 (1), 433–443. 





Zhou, Y., Cholette, M.E., Bhaskar, A., Chung, E., 2019a. Optimal vehicle trajectory planning with control constraints and recursive implementation for automated on-ramp merging. IEEE Trans. Intell. Transp. Syst. 20 (9), 3409–3420. 





Zhou, Y., Chung, E., Bhaskar, A., Cholette, M.E., 2019b. A state-constrained optimal control based trajectory planning strategy for cooperative freeway mainline facilitating and on-ramp merging maneuvers under congested traffic. Transp. Res. Part C Emerg. Technol. 109, 321–342. 





Zhu, J., Tasic, I., 2021. Safety analysis of freeway on-ramp merging with the presence of autonomous vehicles. Accident Anal. Prev. 152, 105966. 





Zhu, J., Tasic, I., Qu, X., 2021. Improving freeway merging efficiency via flow-level coordination of connected and autonomous vehicles. arXiv:2108. 01875 

