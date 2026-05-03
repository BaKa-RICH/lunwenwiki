# DCoMA: A dynamic coordinative merging assistant strategy for on-ramp vehicles with mixed traffic conditions

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/7d94b6329acc3ed79a6344bc0f0d7ebd91edfb1ff846f956b5094f61b7690ced.jpg)


Linheng Li a,b, Chen Qian a,b, Jing Gan c, Dapeng Zhang d, Xu Qu a,b,\*, Feng Xiao d, Bin Ran a,b 

$^{a}$ School of Transportation, Southeast University, Nanjing, Jiangsu Province, 211189 China 

b Institute on Internet of Mobility, Southeast University and University of Wisconsin-Madison, Southeast University, Nanjing, Jiangsu Province 

211189, China 

$^{c}$ School of Modern Posts, Nanjing University of Posts and Telecommunications, Nanjing, Jiangsu Province, 210003 China 

$^{\mathrm{d}}$ School of Management Science and Engineering, Southwestern University of Finance and Economics, Chengdu, Sichuan Province, 611130, China 

# ARTICLEINFO

Keywords: 

Cooperative merging control 

Connected and autonomous vehicles 

On-ramp metering 

Mixed traffic flow 

# ABSTRACT

Merging sections on highways are identified as traffic bottlenecks, leading to congestion and accidents. The emergence of Connected and Autonomous Vehicles (CAVs) technology promises an optimized solution to on-ramp merging issues. Existing cooperative merging strategies typically focus on determining the merging sequence of vehicles in specific merging areas, overlooking the influence of the macroscopic traffic flow conditions on the merging process. In this paper, we innovatively introduce the Dynamic Cooperative Merging Assistance (DCoMA) strategy, a traffic management approach designed to enhance merging operations under variable traffic demands. At the macroscopic level, DCoMA employs the fundamental diagram of traffic flow to develop a platoon formation algorithm for mainline vehicles, tailored to the dynamic macroscopic states of traffic. The algorithm adaptively adjusts the size of platoons based on the volumes of both the mainline and the on-ramp. Subsequently, the spatio-temporal dynamics of these platoons function as the 'red phase' of traffic signals, with the intervals between platoons analogous to the 'green phase'. This information is then converted into a time-series format and transmitted to all vehicles on the on-ramp. At the microscopic level, vehicles on the on-ramp alter their driving strategies in response to this time-series data, ensuring a seamless merging into the mainline flow without causing halting. Through simulations and comparative analysis with three existing strategies (i.e., CoopMA, ALINEA, and X-ALINEAQ), the proposed DCoMA strategy exhibits considerable potential for application across diverse traffic volumes and CAV penetration rates. The results indicate that the proposed approach can significantly improve the efficiency of the mainline and on-ramp, achieving a maximum improvement of $18.32\%$ . More importantly, the DCoMA strategy effectively enlarges merging gaps and, coupled with the speed control capabilities of CAVs, significantly mitigates the risk of accidents and reduces exhaust emissions. 

# 1. Introduction

Highway on-ramps are often identified as traffic bottlenecks, where vehicles from both the mainline and on-ramp decelerate and 

change lanes to merge safely (Zhu et al., 2022a). Under heavy traffic conditions, these maneuvers can initiate shockwaves. These shockwaves propagate upstream on both the mainline and on-ramp, causing significant traffic congestion and reducing traffic efficiency (Gao and Levinson, 2023; Jing et al., 2019; Scholte et al., 2022). To address the challenges of these non-smooth merging processes, research has focused on both macroscopic traffic flow and microscopic vehicle perspectives. The macroscopic approach regulates the entry of on-ramp vehicles onto the mainline and controls the speed of mainline vehicles, minimizing conflicts and improving the discharge rate (Kontorinaki et al., 2019; Larsson et al., 2021; Wang et al., 2014). The microscopic perspective optimizes individual vehicle behaviors, leveraging the advancements in Connected and Automated Vehicles (CAVs) technology (Di et al., 2023; Heshami and Kattan, 2021; Luo et al., 2023). 

Specifically, at the macro-level, various on-ramp merging methodologies have been proposed, predominantly including ramp metering (RM) and variable speed limit (VSL) strategies (Baskar et al., 2008; Chen and Hu, 2023; Cheng et al., 2022; Goatin et al., 2016; Han et al., 2022b, 2021; Hegyi et al., 2005; Papamichail and Papageorgiou, 2008; Shang et al., 2023). RM-based approaches utilize traffic signals at highway on-ramps to control the inflow rate, regulating the macroscopic traffic flow density or volume (Han et al., 2020; Heshami and Kattan, 2021; Jing et al., 2019). However, RM can cause a stop-and-go driving pattern, requiring vehicles at the on-ramp's end to stop and wait for merging permission (Larsson et al., 2021). As a macro-level traffic control mechanism, RM offers limited benefits in enhancing traffic efficiency due to its incapacity to regulate the behaviors of individual merging vehicles (Zhou et al., 2018). On the other hand, VSL-based approaches have proven effective in improving the efficiency of expressway traffic flow (Hegyi et al., 2008, 2005; Li et al., 2017). Nevertheless, these approaches face limitations in traffic flow regulation due to operational constraints and minimum speed limits, reducing their optimization impact on merging (Di et al., 2023). Recent efforts have aimed to integrate VSL with RM to achieve optimized control effects in the on-ramp areas (Di et al., 2023; Hegyi et al., 2005; Lu et al., 2011, 2010). 

In general, macroscopic approaches are designed to manage traffic at an aggregated level, rather than focusing on the granularity of individual vehicle behaviors. Consequently, these strategies typically present two primary limitations: 

(1) Limited Granularity: Macroscopic strategies often overlook the behavior or attributes of individual vehicles, which can be critical in effectively addressing unique traffic situations (Han et al., 2022a; Shang et al., 2023); (2) Temporal Response Delay: Due to their reliance on aggregated data and pre-established algorithms, macroscopic methods can exhibit latency in adapting to dynamic changes or unexpected incidents on roadways. (Fang et al., 2023; Han et al., 2022b). 

Recently, with the advancements in Vehicle-to-Vehicle (V2V) and Vehicle-to-Infrastructure (V2I) technologies, the emergence of CAVs promises enhanced solutions for on-ramp merging at the microscopic level (Ahmed et al., 2021; Li et al., 2020; Zhou et al., 2019). Existing research aims to improve traffic safety and efficiency in on-ramp areas by designing merging strategies for CAVs (Cui et al., 2021; Fukuyama, 2020; Rios-Torres and Malikopoulos, 2016; Scarinci and Heydecker, 2014; Yue et al., 2022). Among these, cooperative merging stands out as a promising method. It uses V2V or V2I communication to coordinate adjacent vehicles, preventing collisions and enhancing traffic performance. For instance, Ntousakis et al. (2016) developed a longitudinal trajectory planning algorithm for safe and efficient merging. Fukuyama (2020) proposed a vehicle trajectory optimization algorithm based on dynamic game theory. Karimi et al. (2020) developed a control algorithm for cooperative CAV trajectory optimization, ensuring efficient and smooth merging. Liu et al. (2023) built a layered cooperative control strategy for CAVs on-ramp merging, optimizing flexible trajectories and ensuring safety in mixed traffic. Liao et al. (2021) developed a game theory-based ramp merging strategy for optimal CAV coordination in mixed traffic, determining dynamic merging sequences and control. Wang et al. (2022) developed a cooperative merging sequence optimization method based on the reverse auction, proposing a strategy for all cooperative merging vehicles in mixed traffic. Liu et al. (2022) proposed a control algorithm for CAVs from the cyber-physical perspective, optimizing traffic conditions in merging zones. Chen et al. (2021) proposed a rotation-based CAV distributed cooperative control strategy for on-ramp merging, reducing voids and damping traffic oscillations in the merging area. 

However, most of the literature above primarily focuses on local vehicular control. Some studies integrate merging sequence determination and vehicle trajectory planning, but these approaches remain within the microscopic traffic flow perspective, considering only a few vehicles' trajectories. When traffic volumes on the mainline and ramps are high, local coordination may cause undispersed shockwaves on the mainline, impairing the overall traffic efficiency (Zhu et al., 2022a). To address this limitation, some cooperative merging strategies based on macroscopic traffic flow theory have been proposed (Chen et al., 2022; Scarinci et al., 2015; Zhu et al., 2022b). Notably, the Cooperative Merging Assistant (CoopMA) strategy developed by Scarinci et al. (2015) exemplifies this approach. This strategy orchestrates the deceleration of CAVs to facilitate denser platooning of mainline vehicles, thereby creating gaps for on-ramp vehicles to merge. Zhu et al., (2022b) proposed a bi-level cooperative merging strategy for dense mixed traffic conditions. However, these approaches typically generate constant-sized gaps, lacking adaptability to on-ramp flow variations. Moreover, the control of on-ramp flow can result in extended queues or overflows on the on-ramp. Consequently, these strategies are optimal for scenarios with dense on-ramp flows and sufficiently extended ramps. 

As cited above, approaches based solely on macroscopic or microscopic perspectives each have inherent limitations. Most studies addressing on-ramp optimization control for mixed traffic flow rely solely on local control approaches. Therefore, the existing on-ramp merging strategies remain an open area of inquiry, particularly regarding the integration between macroscopic and microscopic levels. However, formulating such integrated strategies is complex. A few studies have utilized macroscopic traffic flow theory to develop cooperative merging strategies, but balancing the efficiency of the mainline and on-ramp remains challenging due to the distinct 

behaviors of on-ramp vehicles due to the distinct behaviors of on-ramp vehicles (Sun et al., 2020). Moreover, most works do not account for the varying traffic flow on highways when optimizing on-ramp merging, potentially limiting their applicability in fluctuating traffic scenarios (Scholte et al., 2022). Overcoming these challenges could further enhance the efficacy of the proposed strategies. 

To address these challenges, we developed an innovative on-ramp cooperative merging strategy, termed the Dynamic Coordinative Merging Assistant (DCoMA). DCoMA integrates the macroscopic state of traffic flow with the microcosmic behaviors of individual vehicles during the merging process. It accounts for the variations in traffic flow within both mainline and on-ramp sectors. Utilizing the macroscopic fundamental diagram of traffic flow, we first analyze the evolution of macroscopic traffic state parameters during gap creation. This analysis, guided by the evolutionary mechanism of traffic flow and considering conditions on both the mainline and on-ramp, determines macroscopic target traffic flow state parameters. These parameters guide the micro-level vehicle control strategies. CAVs on the mainline that require coordination decelerate according to these target state parameters. This strategic deceleration fosters the formation of periodic vehicle platoons with suitable gaps for merging, akin to traffic lights where platoon areas represent the red phase and gaps represent the green phase. The frequency and dimensions of these gaps are used to orchestrate the movement of on-ramp vehicles, enabling smooth integration into mainline traffic without stopping. This approach mitigates gap wastage during low traffic conditions and creates adequate gaps during high traffic volumes, ensuring the efficiency and safety of the merging process. 

Major contributions of this paper are listed as follows: 

(1) We concurrently optimized the behaviors of both mainline and on-ramp vehicles to enhance the overall operational efficiency of the mixed traffic flow. 

(2) We combined macroscopic traffic flow theories with microscopic vehicle control methodologies to proactively generating gaps for on-ramp merging. 

(3) We designed a strategy that can be dynamically tailored based on the traffic volumes of the mainline and on-ramp, making it suitable for traffic scenarios with varying volumes. The proposed strategy significantly improves the efficiency of both the mainline and on-ramp, and reduce the risk of accidents and exhaust emissions. 

The remainder of the paper is organized as follows. Section 2 briefly introduces the optimization objectives and assumptions. In Section 3, the framework of the DCoMA strategy and the details of each module are presented. The simulation study and discussion of the efficiency of DCoMA under various traffic conditions are present in Section 4 and Section 5. The conclusion is drawn in Section 6. 

# 2. Optimization objectives and assumptions

In this study, we devised a cooperative merging strategy tailored for mixed traffic conditions in on-ramp areas. The essence of this strategy lies in modulating the behavior of mainline vehicles to systematically form periodic platoons, thereby creating viable gaps for vehicles on the on-ramp. To achieve these control objectives, we meticulously execute a series of steps based on the macroscopic traffic states of both the mainline and on-ramp, as well as the spatial distribution and velocities of individual CAVs. The procedure encompasses: (1) Determining the traffic flow parameters for the desired state of the mainline, considering the current macroscopic traffic conditions of the mainline and on-ramp; (2) Planning the platooning behavior of the mainline vehicles based on the parameters derived in the first step, and subsequently determining the size and frequency of potential mergeable gaps; and (3) Adjusting the merging behavior of on-ramp vehicles based on the gap frequency and size (e.g., updating behavior every 0.01 s). 

In this design, the merging geometry is characterized by a single lane from each road, as illustrated in Fig. 1. The DCoMA system relies on robust V2I communication, which includes the flow of information from vehicles to the infrastructure and vice versa (Fang et al., 2022; Kherroubi et al., 2022). On one front, vehicles on the mainline and on-ramp transmit crucial data regarding traffic flow state and CAV distribution to the control center. The acquisition of traffic flow state is facilitated by detection loops installed on the roadway (Arrows 1 and 6). The exchange of information about CAV distribution is achieved through the interactive capabilities between CAVs and the control center (Arrows 2 and 5). Conversely, the control center orchestrates traffic flow by periodically issuing 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/dcd3c7acf6e455768d9345a633774c5a96636f6ae199ec36db01920b19997867.jpg)



Fig. 1. Schematic diagram of on-ramp merging scenario.


deceleration commands to cooperative vehicles on the mainline, (Arrow 3). Additionally, the control center provides planned speeds to the CAVs on the on-ramp (Arrow 4). This strategy ensures that directives are exclusively communicated to CAVs, thereby avoiding potential non-compliance issues with human drivers. 

Before in-depth modeling, the subsequent assumptions were incorporated: 

- The CAVs are fully automated as defined by SAE (SAE, 2018), implying autonomous control capabilities. Furthermore, they possess the ability to communicate inter-vehicularly and with control center components. 

- The traffic flow on the mainline and the on-ramp consists of both HDVs and CAVs. 

- The gap created by the control strategy is protected. Except for on-ramp vehicles, other vehicles are not allowed to change lanes and enter the gap. 

- Communication delays are considered negligible due to the advancement in 5G communication technologies (Wijethilaka and Liyanage, 2021). 

- In the macroscopic strategy, cooperative CAVs decelerate utilizing a constant acceleration. As indicated by Scarinci et al. (2017), this deceleration method does not substantially influence the computation of pertinent strategy parameters. 

- HDVs can attempt to merge onto the main lanes via acceleration lanes even without clear gaps, reflecting the tendencies of human drivers under real traffic conditions. 

- This paper confines its investigation to the free-flow scenarios. When the freeway is in a congested state, other control methods should be used to return the freeway to a free-flow state. Therefore, the formation of the mainline gap is not impacted by downstream traffic. Under free-flow state, downstream merging behavior does not cause congestion that would affect the formation of the mainline gap (Zhu et al., 2022a). 

# 3. DCoMA: Dynamic Coordinative merging Assistant

The Dynamic Coordinative Merging Assistant (DCoMA) strategy was inspired by the CoopMA strategy proposed by Scarinci et al., (2017, 2015). The core principle of CoopMA centers on actively generating gaps through the formation of vehicle platoons on the mainline, allowing on-ramp vehicles to modulate their speeds to merge into these gaps. However, CoopMA also has many limitations: (1) The strategy is only applicable when all the vehicles on the mainline are CAVs and performs poorly under mixed traffic flows; (2) The gap size created is fixed and cannot be adapted to traffic flow changes. When the on-ramp traffic is high, a longer queue will be created on the on-ramp; (3) The on-ramp is controlled by traffic signal lights, causing frequent stopping and starting of on-ramp vehicles. Therefore, this paper builds on the main idea of CoopMA to create gaps using macroscopic FD and proposes a more refined DCoMA strategy. 

Specifically, as illustrated in Fig. 2(a), traffic flow on both the mainline and the on-ramp is captured using detectors placed on the road. The on-ramp Detection area A is designated to monitor the on-ramp traffic flow. For the mainline vehicle detection, two Detection areas are installed: Detection area B1 serves to measure mainline traffic flow and records the corresponding macroscopic state A, while Detection area B2 is utilized to identify the type and position of vehicles intended for planning. In this case, the vehicle type recognition can be realized by the interactive function between the CAVs and the infrastructure. Vehicles capable of interacting with the infrastructure for information purposes will be classified as CAVs, while all other vehicles are classified as HDVs. 

Initially, the control center collects data from the on-ramp Detection area A and mainline Detection area B1. Based on this data and the FD of traffic flow, the desired traffic state C for the mainline is determined. The determination process of the desired state C is illustrated in Fig. 2(b). Then, following the establishment of traffic state C, the control center uses the vehicle type information obtained from Detection area B2 to identify the CAVs required for collaboration, referred to as cooperative vehicles. When a cooperative vehicle decelerates, a platoon then forms within the gap formation area on the mainline. This process is iteratively applied to control other cooperative vehicles to decelerate, cyclically producing gaps for on-ramp vehicles to utilize, as depicted in Fig. 2(c). Consequently, the spatio-temporal information on the mainline is bifurcated into two categories: (1) Occupied spatio-temporal zones, represented by the areas encompassed by platoons, and (2) Unoccupied spatio-temporal zones, marked by the presence of gaps. This information can be analogized to the phases of traffic lights, with occupied zones representing the red phase and unoccupied zones symbolizing the green phase. Next, the control center captures and encodes these two types of spatio-temporal information into a time series format, which is then transmitted to all vehicles on the on-ramp. The on-ramp vehicles, in turn, calibrate their movements based on this time series data, seamlessly integrating into the mainline without the necessity of halting. This process termed the coordinated merging process, epitomizes the essence of the DCoMA strategy. Moreover, DCoMA possesses the capability to adaptively modify state C in response to fluctuating traffic conditions on both the mainline and the on-ramp, operationalizing through the iterative execution of merging cycles. 

Prior control strategies grounded in macroscopic traffic flow theory have predominantly been applied under the free-flow traffic state (Chen et al., 2022; Scarinci et al., 2015; Zhu et al., 2022b). This is because the control speed of the cooperative vehicle is always higher than the critical speed. Building upon these antecedent studies, the present paper also confines its investigation to the free-flow scenarios. The control strategy in congested traffic states is beyond the scope of this paper. When the freeway is in a congested state, other control methods should be used to return the freeway to a free-flow state. 

Fig. 3 illustrates the information flow of the strategy (Pooladsanj et al., 2023; Shi et al., 2023). In the following subsections, we will 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/82a8c517fd3ae6f1c081f04bc11bc735205991a04a3547608711dc8f479e7dda.jpg)



(a) Detection area layout for a freeway merging area.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/026684b54ad60031b60c75cfae485294d462e5dbe96d56fa722063dc2cf33c76.jpg)



(b) Determination process of desired state C.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/761626ceb8c55e26252a8fafd939749162830c0cd25759ea94b67fc6362d27d3.jpg)



(i) Spatiotemporal information of mainline after platooning


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/c5952bd3c7b9806f94d1acdb115dfe5ddb828aa54de26a41a032a5e60f32f47d.jpg)



(ii) Transforming temporal sequence to assist on-ramp vehicles in speed planning



(c) Spatio-temporal information of mainline under DCoMA.



Fig. 2. Schematic diagram of on-ramp merging scenario. (a) Detection area layout for a freeway merging area. (b) Determination process of desired state C.(c) Spatio-temporal information of mainline under DCoMA.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/c1a686e41f6bfa997e3f0ac694a1753a82aacaa873b8d8911fc6755d33788ab3.jpg)



Fig. 3. Information flow of DCoMA.


sequentially introduce the determination of state C, the optimization of vehicle platooning on the mainline, the cycle planning of DCoMA, and the motion planning for on-ramp vehicles. 

# 3.1. Determination of macro-level desired state

The determination of the desired state $C$ can be facilitated using the FD from traffic flow theory. The FD delineates the relationships among speed $\nu$ , flow $q$ , and density $k$ . These variables are employed to describe different traffic states at a macroscopic level. Each traffic state, denoted by $i$ , is uniquely characterized by the speed $\nu_{i}$ , flow $q_{i}$ , and density $k_{i}$ . As illustrated in Fig. 2(b), each point on the density-flow curve of the FD represents a distinct traffic state, with the slope of the line connecting the point to the origin representing the average speed of vehicles under that particular state. It is assumed that, in the absence of control, the traffic state resides at point A. When cooperative vehicles decelerate, the following vehicles, influenced by car-following behaviors, will also slow down. When the vehicle speed $\nu_{A}$ at state A decelerates to the speed $\nu_{C}$ at state C, a transition from state A to state C is realized. In state C, vehicles travel at a higher density $k_{C}$ , resulting in a shorter headway $h_{C}$ compared to the headway $h_{A}$ , thereby creating a gap. This gap starts to form between the vehicle platoons as the cooperative vehicle initiates deceleration and continuously extends as it progresses downstream. The spatiotemporal area occupied by the gap, being devoid of vehicles, can be defined as state O (with both traffic density and flow equal to zero). In practice, the fundamental relationship is inferred from either fitted empirical data or derived from calibrated car-following models (Zhu et al., 2022a). Without loss of generality, we refer to the FD derived from the IDM (Intelligent Driver Model) as an illustrative example (Treiber et al., 2013). Its specific form is as follows: 

$$
k _ {i} = \frac {\sqrt {1 - \left(v _ {i} / v _ {0}\right) ^ {4}}}{s _ {0} + v _ {i} \bullet T + l \bullet \sqrt {1 - \left(v _ {i} / v _ {0}\right) ^ {4}}} \tag {1}
$$

$$
q _ {i} = k _ {i} \bullet v _ {i} \tag {2}
$$

$$
h _ {i} = \frac {s _ {0} + v _ {i} \cdot T}{\sqrt {1 - \left(v _ {i} / v _ {0}\right) ^ {4}}} + l \tag {3}
$$

where, $T$ is the safe headway, $l$ is the vehicle length, $\nu_{i}$ is the equilibrium speed in traffic state $i$ , $\nu_{0}$ is the free flow speed, $s_0$ is the minimum safe stopping distance, and $h_i$ is the headway in traffic state $i$ . 

FD is not confined to the IDM but can also include others derived from empirical data fitting or calibrated car-following models, such as the Wiedemann 99 model(Zhu et al., 2022a). Notably, triangular fundamental diagrams are unsuitable for our strategy because they assume a uniform and stable traffic flow. In such diagrams, the desired state C would have the same speed as the initial state A, thus $h_{C} = h_{A}$ . However, this does not detract from the generality of our method. In on-ramp merging scenarios, the complex interactions between mainstream and merging streams result in non-uniform distributions of flow, speed, and vehicle density on FD. Hence, any FD that exhibits a variable slope is applicable to our strategy. 

From the aforementioned analysis, it becomes evident that the size of the gap is determined by state A, state C, and the number of vehicles $n_p$ between the two cooperative vehicles. Since the relationship between state A and state C can be switched by controlling vehicle speeds, the gap's size can be ascertained by determining the traffic flow speed $\nu_C$ in state C. The solution of $\nu_C$ is not well handled in existing studies. Scarinci et al. (2015) empirically determined the deceleration value of the mainline vehicles $\Delta \nu$ , and made $\nu_C = \nu_A - \Delta \nu$ . Although $\nu_C$ varies when the mainline flow varies, the size of the gap created is fixed since $\Delta \nu$ remains constant. Zhu et al., (2022b) developed an optimization model using delay as a loss function for solving the optimal combination of the length of platoon and $\nu_C$ . However, the optimization model makes each platoon on the mainline very long to minimize the delay. This approach can only be applied to scenarios where the on-ramp length is long enough. Nonetheless, the optimization model tends to extend the length of each platoon on the mainline as a means to minimize delay. As a result, vehicles also form long platoons on the on-ramp for 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/75cd6704d7d644f878b5abece68a33f65600e6e30b9161fa6dc17ebee83e0b36.jpg)



Fig. 4. Conceptual representation of the variables.


waiting gaps. Consequently, its applicability is restricted to scenarios where the on-ramp provides adequate space to accommodate these elongated platoons. In their simulation, the on-ramp length extended up to $1500\mathrm{m}$ , whereas our simulated ramp length is only $300\mathrm{m}$ . Hence, this study introduces a dynamic method to determine $\nu_{C}$ , considering the traffic flow conditions of both the mainline and on-ramp. 

Firstly, the control cycle proposed in this paper is defined, as illustrated in Figure 4. The cycle described here represents the time needed for the current cooperative vehicles to form a gap and for the convoy to pass through the merging point in state C. The cycle length $C_c$ is a direct outcome of the number of vehicles in one cycle $n_p$ in the initial state A and the headway $h_A$ of state A. Based on the description in (Scarinci et al., 2017), it can be defined as: 

$$
C _ {c} = h _ {A} \bullet n _ {p} \tag {4}
$$

The duration of the gap $G$ is defined as: 

$$
G = n _ {p} \bullet \left(h _ {A} - h _ {C}\right) \tag {5}
$$

The number of on-ramp vehicles that can merge into the gap $G$ is: 

$$
n _ {G} = \frac {G}{g _ {m}} \tag {6}
$$

where, $g_{m}$ represents the minimum headway required for a vehicle from the on-ramp to merge onto the mainline. Thus, the on-ramp traffic flow that can pass through during the cycle $C_{c}$ is: 

$$
q _ {r a m p} = \frac {n _ {G}}{C _ {c}} = \frac {h _ {A} - h _ {C} ^ {*}}{h _ {A} \cdot g _ {m}} \tag {7}
$$

By integrating Eq.(6) to Eq.(7), the headway in traffic state C can be derived: 

$$
h _ {C} ^ {*} = h _ {A} - q _ {\text {r a m p}} \bullet h _ {A} \bullet g _ {m} \tag {8}
$$

Finally, by combining Eq.(8) with Eq.(3), the ideal traffic flow speed parameter $\nu_{C}^{*}$ in traffic state C can be derived. The ideal state is the traffic flow state that mainline traffic needs to be in when it can accommodate all current on-ramp demands. 

The essence of this method is to prioritize the merging needs of the vehicles on the on-ramp. However, when the on-ramp flow is excessive, the calculated $\nu_{C}^{*}$ tends to have a very small value. This implies that the vehicles on the mainline would require a significant deceleration. Major speed fluctuations can lead to substantial traffic oscillations, potentially causing congestion in the mainline flow. Therefore, it's essential to constrain the value of $\nu_{C}$ to prevent a collapse of the mainline traffic flow due to an excessively low $\nu_{C}$ . The principle for determining the value of $\nu_{C}$ should be as large as possible while ensuring sufficient gap formation and minimizing the adverse effects on the mainline traffic flow caused by speed variations. 

Assuming the total number of vehicles to be scheduled is $N$ , where $N$ is a positive integer. To form effective gaps between the scheduled vehicles, the following condition should be satisfied: 

$$
\left[ \frac {N}{n p _ {\text {m i n}}} \right] \geq 2 \tag {9}
$$

where, $[ \bullet ]$ denotes the ceiling function, and $np_{\min}$ represents the minimum platoon size required to form an effective gap. 

Assuming the minimum effective gap length to be $g_{m}^{min}$ , this gap is precisely adequate for the merging of one on-ramp vehicle, implying that the gap length equates to the minimum headway required for an on-ramp vehicle to merge onto the mainline. From this, it follows that $g_{m}^{min} = g_{m}$ . The platoon size required to create this gap, denoted as $np_{\text{min}}$ , can be computed as follows: 

$$
n p _ {\min } = \left[ \frac {g _ {m}}{h _ {A} - h _ {C} ^ {\min }} \right] \tag {10}
$$

From this analysis, the lower bound of the headway for state C, denoted as $h_C^{min}$ , can be established. The minimum value of $\nu_{C}$ denoted as $\nu_{Cmin}$ , is determined based on Eq.(1-4). Ultimately, the speed for traffic state C is determined collaboratively by $\nu_{C}^{*}$ and $\nu_{C}^{min}$ 

$$
v _ {C} = \max  \left(v _ {C} ^ {*}, v _ {C} ^ {\min }\right) \tag {11}
$$

We use the Newton-Raphson method to calculate $\nu_{C}^{*}$ and $\nu_{C}^{min}$ and design the function as follows: 


Function 1: Newton-Raphson method.


Input: Model parameters of IDM (Desired speed $v_{0}$ , Time gap $T$ , Minimum gap $s_{0}$ ); Headway in traffic state C $h_{C}$ ; Parameter of convergence discriminant $\epsilon$ .  
Output: Velocity of state C (i.e., $v_{c}$ ).  
1: Function newton ( $v_{0}, T, s_{0}, h_{C}, \epsilon$ )  
2: BEGIN  
3: $x^{n} \gets x_{0}$ // Initial guess for the root-finding algorithm  
4: $f(x^{n}) \gets v_{0}^{4}(h_{C}x^{n})^{2} - (x^{n})^{4} - (s_{0} + x^{n}T)^{2}(x^{n})^{4}$ // $f(x^{n})$ is the function  
5: whose root we are trying to find, which comes from Equation (3)  
6: $E_{n} \gets \frac{\partial f}{\partial x^{n}}$ // $E_{n}$ is the derivative of $f(x^{n})$ at $x^{n}$ 7: $k \gets 0$ 10: // Loop until convergence, defined by the condition ( $g_{n} < \epsilon$ )  
11: WHILE ( $E_{n} < \epsilon$ )  
12: $x^{n} \gets x^{n} - \frac{E_{n}}{\nabla^{2}f(x^{n})}$ 13: $E_{n} \gets f'(x^{n})$ 14: RETURN $x^{n}$ 15: END 

Based on the aforementioned description, we designed an algorithm to determine the traffic flow speed $\nu_{C}$ in state C: the 'A Dynamic $\nu_{c}$ Resolve Algorithm'. 


Algorithm 1. A Dynamic $\nu_{c}$ Resolve Algorithm..


Input: Model parameters of IDM (Desired speed $\nu_{0}$ , Time gap $T$ , Minimum gap $s_0$ , Vehicle length l); On-ramp flow $q_{ramp}$ , Minimum gap for merging $g_{m}$ ; Number of mainline vehicles to be planned N; Parameter of convergence discriminant e.   
Output: Flow, density, velocity and headway of state C (i.e., $q_{c},k_{c},v_{c}andh_{c}$ -   
1: // Calculate minimum and ideal headway   
2: $h_{min}\gets h_A\frac{2g_m}{N}$ 3: $h_{ideal}\leftarrow h_A - q_{ramp}\cdot h_A\cdot g_m$ 4: // Find the minimum and ideal velocities using the Newton method   
5: $\nu_{C}^{\mathrm{min}}\gets \mathrm{newton}(\nu_{0},T,s_{0},h_{\mathrm{min}},\in)$ 6: $\nu_{C}^{*}\gets \mathrm{newton}(\nu_{0},T,s_{0},h_{\mathrm{ideal}},\in)$ 7: // Determine the final $\nu_{c}$ value   
8: IF $\nu_{C}^{*}\geq \nu_{C}^{min}$ THEN   
9: $\nu_{c}\gets \nu_{C}^{*}$ 10: ELSE   
11: $\nu_{c}\gets \nu_{C}^{min}$ 12: END IF   
13: // Calculate density, flow and headway of state C using IDM   
14: $s_c\gets s_0 + \frac{\nu_c*T}{\sqrt{1 - \left(\frac{\nu_c}{\nu_0}\right)^4}}$ 15: $\begin{array}{rl} & {\sqrt{1 - (\nu_c / \nu_0)^4}}\\ & {k_c\leftarrow \frac{\sqrt{1 - (\nu_c / \nu_0)^4}}{s_0 + \nu_c\bullet T + l\bullet\sqrt{1 - (\nu_c / \nu_0)^4}}}\\ & {q_c\leftarrow \nu_c^* k_c} \end{array}$ 

(continued) 

$$
\overline {{1 7 :}} \quad h _ {c} \leftarrow \frac {s _ {0} + v _ {c} \bullet T}{\sqrt {1 - \left(v _ {c} / v _ {0}\right) ^ {4}}} + l
$$

# 3.2. Optimization of vehicle platooning on the mainline

Most existing research assumes a $100\%$ penetration rate for CAVs on the mainline. This implies that once a control cycle is established, mainline vehicles are selected as cooperative vehicles at consistent intervals and locations. However, in scenarios where CAVs and HDVs are mixed, HDVs may not necessarily accept instructions to reduce speed. As a result, this study considers only CAVs as cooperative vehicles and identifies them based on their distribution. For this purpose, a 1 km-long Detection area B2 is set up on the mainline segment to identify vehicles awaiting planning. The detection results are then translated into binary strings using unsigned binary integers, where CAVs are denoted as '1' and HDVs as '0'. This binary representation facilitates the identification and random selection of CAVs from the detected vehicles, forming the initial set for platoon configuration. 

An optimization algorithm, inspired by genetic algorithms, is developed to efficiently manage vehicle platooning. The process begins with the computation of individual fitness values, derived from the objective function of the platooning optimization model. These fitness values then guide the selection, crossover, and mutation operations of potential platoon configurations. After a series of iterations, the algorithm converges on an optimal platooning configuration. Subsequent sections will elaborate on the details of establishing the platoon optimization model. 

In this study, we aim to minimize the total delay of all vehicles passing through the merging point. The objective function is formulated as follows: 

$$
\min  D = \omega_ {\text {m a i n}} \cdot \sum_ {i = 1} ^ {m} D _ {\text {m a i n}} ^ {i} + \omega_ {\text {r a m p}} \cdot \sum_ {j = 1} ^ {n} D _ {\text {r a m p}} ^ {j} \tag {12}
$$

where, $\omega_{main}$ and $\omega_{ramp}$ represent the weights for the mainline and on-ramp traffic respectively, $m$ is the total number of mainline vehicles to be scheduled, $n$ is the total number of on-ramp vehicles that can be accommodated, $D_{main}^{i}$ denotes the delay for the $i$ -th mainline vehicle, and $D_{ramp}^{j}$ indicates the delay for the $j$ -th on-ramp vehicle. 

Assuming that the current set of vehicles to be scheduled can form $C$ sub-cycles, we can determine the total number of on-ramp vehicles that can fit into these sub-cycles using Equation (7). 

$$
n = \sum_ {p = 1} ^ {c} \left[ \frac {m _ {p} \cdot \left(h _ {A} - h _ {C}\right)}{g _ {m}} \right] \tag {13}
$$

where $m_{p}$ represents the number of mainline vehicles in the $p$ -th cycle. 

The calculation of the delay for mainline vehicles is illustrated in Fig. 5. The delay for mainline vehicle $i$ is defined as the additional time taken due to the platooning of vehicles on the mainline. This is specifically expressed in Eq. (14). 

$$
D _ {\text {m a i n}} ^ {i} = t _ {m 1} ^ {i} - t _ {m 2} ^ {i} \tag {14}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/311bd11794db0e0001676ef28c7d75778bb6ca0fa3787e036b6d17c59f9c4788.jpg)



Fig. 5. Schematic representation of mainline vehicle delay calculation.


where $t_{m1}^{i}$ represents the actual arrival time of the $i$ -th vehicle at the merging point, while $t_{m2}^{i}$ indicates the arrival time of the $i$ -th mainline vehicle at the merging point without platooning behavior. 

Suppose the first vehicle in this cycle is the cooperative vehicle (i.e., $i = 1$ ) with a distance $d$ from the merging point. After receiving the deceleration command, the time $t_{AC}$ required for the platoon to transition from State A to State C is expressed as: 

$$
t _ {A C} = \frac {- s _ {A} \cdot \left(n _ {P} - 1\right)}{\nu_ {A C} - \nu_ {A}} \tag {15}
$$

$$
\nu_ {A C} = \frac {q _ {C} - q _ {A}}{k _ {C} - k _ {A}} \tag {16}
$$

where $\nu_{AC}$ represents the wave speed of the transition from State A to State C. 

Thus, the distance $x_{AC}$ required by the platoon to form the gap $G$ is given by: 

$$
x _ {A C} = t _ {A C} \hat {\mathbf {A}} \cdot v _ {A C} = \frac {q _ {c} - q _ {A}}{k _ {c} - k _ {A}} \cdot \frac {- s _ {A} \cdot \left(n _ {p} - 1\right)}{v _ {A C} - v _ {A}} \tag {17}
$$

As illustrated in Fig. 5, when the cooperating vehicle travels at a constant speed $\nu_{A}$ for a distance $(d - x_{AC})$ before decelerating, the actual arrival time of the last vehicle $t_{m1}^{m}$ in the platoon at the merging point is given by: 

$$
t _ {m 1} ^ {m} = \frac {d - x _ {A C}}{\nu_ {A}} + t _ {A C} \tag {18}
$$

For the sake of generality, the actual arrival time of the $i$ -th vehicle in the mainline platoon at the merging point is given by: 

$$
t _ {m 1} ^ {i} = \frac {d - x _ {A C}}{\nu_ {A}} + t _ {A C} - (m - i) \cdot h _ {C} \tag {19}
$$

When no vehicle platooning is executed, the mainline vehicles persistently remain in traffic state A, traveling uniformly at speed $\nu_{A}$ and sustaining a headway of $h_{A}$ . In such a scenario, the arrival time of the $i$ -th vehicle in the mainline $t_{m1}^{i}$ at the merging point can be expressed as: 

$$
t _ {m 2} ^ {i} = \frac {d}{v _ {A}} + (i - 1) \cdot h _ {A} \tag {20}
$$

The delay of the $j$ -th on-ramp vehicle is defined as the difference between its actual arrival time $t_{r1}^{j}$ and the original expected arrival time $t_{r2}^{j}$ in the absence of mainline vehicles, which can be expressed as: 

$$
D _ {r a m p} ^ {j} = t _ {r 1} ^ {j} - t _ {r 2} ^ {j} \tag {21}
$$

For the cooperative vehicle (the first vehicle, $i = 1$ ), since its arrival time is also the end time of gap $G$ , which means the arrival time of the last on-ramp vehicle ( $j = n$ ) at the merging point, we have: 

$$
t _ {r 1} ^ {n} = t _ {r 2} ^ {n} = t _ {m 1} ^ {1} \tag {22}
$$

When there are no vehicles on the mainline, the on-ramp vehicles travel at a constant on-ramp average speed $\nu_{r}$ and maintain a headway of $h_r$ . Referring to the study by Zhu et al. (2021), we define the arrival time of the on-ramp vehicle at the merging point as follows: 

$$
t _ {r 2} ^ {j} = t _ {m 1} ^ {1} - G + (i - 1) \cdot h _ {r} \tag {23}
$$

When the DCoMA strategy is implemented, the on-ramp vehicles move according to the motion planning algorithm (for details on the algorithm, refer to Section 3.4). Eventually, they arrive at the merging point in state C, with a headway of $h_c$ . Therefore, the actual arrival time of the on-ramp vehicle at the merging point is: 

$$
t _ {r 1} ^ {j} = t _ {m 1} ^ {1} - G + (i - 1) \cdot h _ {C} \tag {24}
$$

Integrating Eq.(19)-(20) and Eq. (23)-(24), the original objective function Eq.(13) can be reformulated as: 

$$
\min  D = w _ {m} \hat {\mathbf {A}} \cdot \sum_ {i = 1} ^ {m} \left(\frac {\mathbf {x} _ {A C}}{\nu_ {A}} + t _ {A C} - (m - i) \cdot h _ {C} - (i - 1) \cdot h _ {A}\right) + w _ {r} \hat {\mathbf {A}} \cdot \sum_ {j = 1} ^ {n} \left((i - 1) \cdot \left(h _ {C} - h _ {r}\right)\right) \tag {25}
$$

In addition, the platoon optimization model should also satisfy the following constraints: 

(1) Only CAV vehicles are selected as cooperative vehicles; 

(2) The distance between the cooperative vehicle and the merge point must be greater than or equal to the distance required to form the gap, i.e., $0 < x_{AC} \leq d$ . 

Through our enhanced analysis, which involves modeling the platoon formation process, we ascertained that the occurrence of extended platoons, specifically configurations like 9 consecutive HDVs following 1 CAV, is relatively rare. The detailed analysis process is described in the Appendix. However, given the high traffic volumes, these incidents may still occur multiple times per hour. Consequently, this paper will simulate and discuss the scenario of long HDV platoons in Section 4. 

We define the fitness calculation function as follows: 

Function 2: Calculation of Fitness.   
Input: Platoon scheme individual, the position of each vehicle in the platoon scheme position.   
Output: Fitness of the platoon scheme Fitness   
Function oneMaxFitness(individual,position) BEGIN Delay $\leftarrow$ Calculate delay based on the individual's characteristics (i.e.individual, position) using equation (25) Fitness--Delay // Adjust fitness based on delay penalty   
Return Fitness   
END 

The optimization of the platoon is performed as follows: 

# Algorithm 2. A Platoon Optimization Algorithm..

Input: Platoon scheme $P$ , Vehicle location list Position, Maximum number of generation $T$ 

Output: Optimal platoon scheme bestindividual 

Initialize $P(0) //$ Initialize the population 

$t\gets 0$ 

WHILE $(t <   = T)$ DO 

FOR $i = 0$ to $\mathrm{len}(P(t))$ do 

fitnessValues[i] $\leftarrow$ oneMaxFitness $(P(t)[i],\text{Position})$ 

END FOR 

FOR $i = 0$ to $\mathrm{len}(P(t))$ do 

$P(t)\gets$ Perform selection operation based on fitnessValues 

END FOR 

FOR $i = 0$ to $\mathrm{len}(P(t)) / 2$ do 

$P(t)\gets$ Perform crossover operation on selected individuals 

END FOR 

FOR $i = 0$ to $\mathrm{len}(P(t))$ do 

$P(t)\gets$ Perform mutation operation on individuals 

END FOR 

$P(t + 1)\gets P(t) / /$ Update the population for the next generation 

$t\gets t + 1$ 

END WHILE 

best_index←fitnessValues.index(max(fitnessValues)) 

bestindividual $\leftarrow P(t)$ [best_index] 

# 3.3. Cycle planning process in DCoMA

After determining the distribution of cooperative vehicles and the size of the platoon, it is imperative to further specify the control duration for these vehicles, as well as the commencement and termination times of the formed gaps, to finalize the cycle planning. 

Assuming that a command is sent to the cooperative vehicle at time $t$ to decelerate, the arrival time $t_{CV - arrive}$ of the cooperative vehicle at the merging point can be deduced from Eq. (17) and (18). 

$$
t _ {C V - a r r i v e} = t + t _ {A C} = t - \frac {s _ {A} \cdot \left(n _ {P} - 1\right)}{\nu_ {A C} - \nu_ {A}} \tag {26}
$$

This time also marks the end of the previous gap. Therefore, the arrival time of the previous gap at the merging point, based on the gap length $G$ , can be extrapolated backward as: 

$$
t _ {G - a r r i v e} = t + t _ {A C} - G = t - \frac {s _ {A} \cdot \left(n _ {P} - 1\right)}{\nu_ {A C} - \nu_ {A}} - n _ {P} \bullet \left(h _ {A} - h _ {C}\right) \tag {27}
$$

For the platoon in which the cooperative vehicle is located, the end time of its cycle $t_{end}$ can be obtained by the summation of the arrival time of the cooperative vehicle and the cycle length $C_c$ : 

$$
t _ {e n d} = t + t _ {A C} + C _ {c} = t - \frac {s _ {A} \cdot \left(n _ {P} - 1\right)}{\nu_ {A C} - \nu_ {A}} + h _ {A} \cdot n _ {P} \tag {28}
$$

# 3.4. Micro-level motion planning of on-ramp vehicles

One of the basic approaches to motion planning is the simple motion planning method (Xu et al., 2019), which consists of three scenarios: 'accelerate and cruise', 'decelerate and cruise', and 'cruise'. Another approach in the literature is the virtual vehicle mapping technique (Li and Wang, 2006), by using the concept of a virtual vehicle, the vehicle can perform smoother and safer control maneuvers. The third class of methods is based on optimal control techniques. Rios-Torres and Malikopoulos (2016) obtained a closed-form solution that can reduce fuel consumption. In this paper, we first determine the gap for on-ramp vehicle merging based on the cycle planning results and guide the CAVs to move using a motion planning method that integrates energy efficiency and comfort. 

Based on the results of the cycle planning in Section 3.3, the established cycle data is stored in the control center. When a CAV approaches the on-ramp area, the control center utilizes the cycle data to estimate the vehicle's arrival time at the on-ramp merging point. This assists the on-ramp CAVs in planning their movement to merge seamlessly into the mainline without stopping. Considering the tendency of human drivers to travel at the upper threshold of the speed limit (Fildes et al., 1991), this study posits that HDVs following CAVs will approach the merging point with a headway time distance of $h_c$ . This assumption allows for the effective control of the arrival timing of CAVs, and consequently, the subsequent arrival of HDVs. By managing the headway time distance of CAVs, the paper aims to indirectly regulate the flow and timing of HDVs in the traffic stream. 

As depicted in Fig. 6, the motion planning for the on-ramp CAVs can be divided into the following four steps: 

Step 1: Is the leading vehicle a CAV? If yes, proceed to Step 3; otherwise, proceed to Step 2. 

Step 2: Assuming that HDVs arrive at the merging point with a headway of $h_c$ , updating the list of cycles. Proceed to Step 3. 

Step 3: Are there any merging vehicles in the current cycle? If yes, proceed to Step 4; otherwise, proceed to Step 5. 

Step 4: Can the remaining gap in the current cycle accommodate the merging requirements of vehicle $j$ ? If yes, vehicle $j$ maintains a headway of $h_C$ with the preceding vehicle $j - 1$ upon reaching the merge point. If not, retrieve information for the next cycle and return to Step 3. 

Step 5: Can the vehicle $j$ reach the merge point before the end of the gap? If yes, proceed to Step 6. If not, retrieve information for the next cycle and return to Step 3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/bd2b01fbc6bb76b35fc26d23f6ff253b4d9454cf413033209e1fea1e9a5499de.jpg)



Fig. 6. Procedure to determine the on-ramp vehicle's arrival time at the merging point.


Step 6: Can vehicle $j$ reach the merge point concurrently with the gap? If yes, ensure that vehicle $j$ and the gap arrive simultaneously. If not, have vehicle $j$ move at its maximum speed to reach the merge point as soon as possible. 

After determining the arrival time of on-ramp vehicles, it's necessary to perform motion planning for the on-ramp vehicles to ensure them merge seamlessly without stopping. Since vehicles on the on-ramp don't change lanes or make turns, a linear dynamics model, as shown in Eq. (29), is utilized to represent the vehicle's longitudinal motion. 

$$
\dot {x} _ {i} (t) = A x _ {i} (t) + B u _ {i} (t)
$$

$$
\boldsymbol {x} _ {i} (t) = \left[ \begin{array}{l} p _ {i} (t) \\ \nu_ {i} (t) \\ a _ {i} (t) \end{array} \right]; A = \left[ \begin{array}{l l l} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right]; B = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] \tag {29}
$$

where $x_{i}(t)$ represents the state of vehicle $i$ at time $t$ ; $p_{i}(t)$ , $\nu_{i}(t)$ , and $a_{i}(t)$ represent the position, speed, and acceleration of vehicle $i$ respectively; and the control input variable $u_{i}(t)$ stands for the derivative of the vehicle's acceleration. 

The objective of the on-ramp vehicle motion planning primarily considers two aspects: (1) Comfortable: The on-ramp vehicles should reach the merging point and complete the lane change with a smooth speed transition; (2) Energy efficiency: During the movement on the on-ramp, the vehicles should consume as little fuel as possible. Based on these considerations, the following objective function is formulated: 

$$
\min  _ {u _ {i} (t)} \int_ {t _ {0} ^ {i}} ^ {t _ {f} ^ {i}} \left(\omega_ {e} a _ {i} ^ {2} + \omega_ {c} u _ {i} ^ {2}\right) d t \tag {30}
$$

At the same time, the following constraints should also be satisfied: 

$$
\nu_ {\min } \leq \nu_ {i} (t) \leq \nu_ {\max }, \forall t \in \left[ t _ {0} ^ {i}, t _ {f} ^ {i} \right] \tag {31}
$$

$$
a _ {\min } \leq a _ {i} (t) \leq a _ {\max }, \forall t \in \left[ t _ {0} ^ {i}, t _ {f} ^ {i} \right] \tag {32}
$$

$$
u _ {\min } \leq u _ {i} (t) \leq u _ {\max }, \forall t \in \left[ t _ {0} ^ {i}, t _ {f} ^ {i} \right] \tag {33}
$$

$$
t _ {f} ^ {i} \geq t _ {f} ^ {i - 1} + \frac {s _ {\text {s a f e}}}{\Delta t} \tag {34}
$$

where $t_0^i$ and $t_f^i$ are the time points when the vehicle arrives and leaves the on-ramp, which means the start and end times of the vehicle's movement on the on-ramp. $\omega_e$ and $\omega_c$ are the weights for energy efficiency and comfort. $\nu_{min}$ and $\nu_{max}$ are the minimum and maximum speeds allowed on the on-ramp. $a_{min}$ and $a_{max}$ are the minimum and maximum accelerations allowed on the on-ramp. $u_{min}$ and $u_{max}$ are the minimum and maximum jerk (rate of change of acceleration) allowed on the on-ramp. $s_{safe}$ denotes the minimum safety distance between vehicles. 

Constraint (34) ensures that the on-ramp vehicles consistently uphold this minimum safe separation throughout their trajectory, mitigating the possibility of collisions or other hazardous driving maneuvers. This implies that regardless of variations in the speed or acceleration of the on-ramp vehicles, the gap between it and its predecessor or successor never drops below $s_{\text{safe}}$ . Such a constraint is of paramount significance as it is intrinsically linked to the safety of both the vehicles and their occupants. 

To save computational time, the Pontryagin's Minimum Principle is employed to derive the analytical solution for the aforementioned problem(Liu et al., 2021; Xue et al., 2022). The corresponding Hamiltonian function can be expressed as: 

$$
H _ {i} \left(\boldsymbol {x} _ {i}, u _ {i}, \lambda_ {i}\right) = L _ {i} \left(\boldsymbol {x} _ {i}, u _ {i}\right) + \lambda^ {T} f _ {i} \left(\boldsymbol {x} _ {i}, u _ {i}\right) \tag {35}
$$

where, $\lambda$ is the co-state variable. Based on Eq. (29), the Hamiltonian function can be expressed as: 

$$
H _ {i} \left(x _ {i}, u _ {i}, \lambda_ {i}\right) = \omega_ {e} a _ {i} ^ {2} + \omega_ {c} u _ {i} ^ {2} + \lambda_ {1} ^ {i} v _ {i} + \lambda_ {2} ^ {i} a _ {i} + \lambda_ {3} ^ {i} u _ {i} \tag {36}
$$

where, $\lambda_1^i$ , $\lambda_2^i$ and $\lambda_3^i$ is the co-state variables of vehicle $i$ ( $\lambda = \left[\lambda_1^i \quad \lambda_2^i \quad \lambda_3^i\right]^T$ ). 

Taking the partial derivative of Eq. (36) with respect to $p_i, \nu_i$ and $a_i$ , we obtain the co-state equations: 

$$
\lambda_ {1} ^ {i} = - \frac {\partial H _ {i}}{\partial p _ {i}} = 0 \tag {37}
$$

$$
\dot {\lambda} _ {2} ^ {i} = - \frac {\partial H _ {i}}{\partial v _ {i}} = - \dot {\lambda} _ {1} ^ {i} \tag {38}
$$

$$
\lambda_ {3} ^ {i} = - \frac {\partial H _ {i}}{\partial a _ {i}} = - 2 \omega_ {e} a _ {i} - \lambda_ {2} ^ {i} \tag {39}
$$

Combining Eq. (37) with (38), we can derive $\lambda_1^i = c_1$ and $\lambda_2^i = -c_1t + c_2$ , where $c_{1}$ and $c_{2}$ are constants. 

Taking the partial derivative of Eq. (36) with respect to $u_{i}$ yields the control equation: 

$$
\frac {\partial H _ {i}}{\partial u _ {i}} = 2 \omega_ {c} a _ {i} + \lambda_ {3} ^ {i} = 0 \tag {40}
$$

Further, combining Eq. (39) with (40), we can derive: 

$$
2 \omega_ {c} \ddot {a} _ {i} - 2 \omega_ {e} a _ {i} + c _ {1} t - c _ {2} = 0 \tag {41}
$$

By solving the aforementioned second-order differential equation, we can obtain the acceleration of vehicle $i$ . 

$$
a _ {i} = c _ {3} e ^ {\sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t} - c _ {4} e ^ {- \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t} + \frac {c _ {1}}{2 \omega_ {e}} t - \frac {c _ {1}}{2 \omega_ {e}} \tag {42}
$$

By substituting Eq. (42) into Eq. (40), we can derive: 

$$
u _ {i} = c _ {3} \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} e ^ {\sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t} - c _ {4} \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} e ^ {- \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t} + \frac {c _ {1}}{2 \omega_ {e}} \tag {43}
$$

$$
v _ {i} = c _ {3} \sqrt {\frac {\omega_ {c}}{\omega_ {e}}} e ^ {\sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t} - c _ {4} \sqrt {\frac {\omega_ {c}}{\omega_ {e}}} e ^ {- \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t} + \frac {c _ {1}}{4 \omega_ {e}} t ^ {2} - \frac {c _ {2}}{2 \omega_ {e}} t + c _ {5} \tag {44}
$$

$$
p _ {i} = c _ {3} \frac {\omega_ {c}}{\omega_ {e}} e ^ {\sqrt {\frac {\omega_ {c}}{\omega_ {c}}} t} + c _ {4} \frac {\omega_ {c}}{\omega_ {e}} e ^ {- \sqrt {\frac {\omega_ {c}}{\omega_ {c}}} t} + \frac {c _ {1}}{1 2 \omega_ {e}} t ^ {3} - \frac {c _ {2}}{4 \omega_ {e}} t ^ {2} + c _ {5} t + c _ {6} \tag {45}
$$

where, $c_{3}, c_{4}, c_{5}$ and $c_{6}$ are all constants. 

At the endpoint of the on-ramp vehicle, the Hamiltonian function should satisfy: 

$$
H _ {i} \left(x _ {i} \left(t _ {f} ^ {i}\right), u _ {i} \left(t _ {f} ^ {i}\right), \lambda_ {i} \left(t _ {f} ^ {i}\right)\right) = 0 \tag {46}
$$

The states of vehicles when arriving and departing from the on-ramp area are defined as follows: At the initial state when the vehicle enters the ramp $p_i(t_0^i) = 0, \nu_i(t_0^i) = \nu_i^0, a_i(t_0^i) = 0$ . At the terminal state when the vehicle exits the on-ramp $p_i\left(t_f^i\right) = L_{ramp}$ , $\nu_i\left(t_f^i\right) = \nu_c, a_i\left(t_f^i\right) = 0$ , where $L_{ramp}$ represents the length of the on-ramp and the acceleration of the vehicle at arrival or departure time is set to zero. Consequently, a set of equations in the form $T_i h_i = q_i$ can be derived as follows: 

$$
\left[ \begin{array}{c c c c c c} \frac {t _ {0} ^ {i} - 1}{2 \omega_ {e}} & 0 & e ^ {\sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {0} ^ {i}} & - e ^ {- \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {0} ^ {i}} & 0 & 0 \\ \frac {t _ {0} ^ {i}}{4 \omega_ {e}} & - \frac {1}{2 \omega_ {e}} & \sqrt {\frac {\omega_ {c}}{\omega_ {e}}} e ^ {\sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {0} ^ {i}} & - \sqrt {\frac {\omega_ {c}}{\omega_ {e}}} e ^ {- \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {0} ^ {i}} & 1 & 0 \\ \frac {t _ {0} ^ {i ^ {3}}}{1 2 \omega_ {e}} & - \frac {t _ {0} ^ {i ^ {2}}}{4 \omega_ {e}} & \frac {\omega_ {c}}{\omega_ {e}} e ^ {\sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {0} ^ {i}} & \frac {\omega_ {c}}{\omega_ {e}} e ^ {- \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {0} ^ {i}} & t _ {0} ^ {i} & 1 \\ \frac {t _ {f} ^ {i} - 1}{2 \omega_ {e}} & 0 & e ^ {\sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {f} ^ {i}} & - e ^ {- \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {f} ^ {i}} & 0 & 0 \\ \frac {t _ {f} ^ {i ^ {2}}}{4 \omega_ {e}} & - \frac {1}{2 \omega_ {e}} \sqrt {\frac {\omega_ {c}}{\omega_ {e}}} & e ^ {\sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {f} ^ {i}} & - \sqrt {\frac {\omega_ {c}}{\omega_ {e}}} e ^ {- \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {f} ^ {i}} & 1 & 0 \\ \frac {t _ {f} ^ {i ^ {3}}}{1 2 \omega_ {e}} & - \frac {t _ {f} ^ {i ^ {2}}}{4 \omega_ {e}} & \frac {\omega_ {c}}{\omega_ {e}} e ^ {\sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {f} ^ {i}} & \frac {\omega_ {c}}{\omega_ {e}} e ^ {- \sqrt {\frac {\omega_ {e}}{\omega_ {c}}} t _ {f} ^ {i}} & t _ {f} ^ {i} & 1 \end{array} \right] \left[ \begin{array}{l} c _ {1} \\ c _ {2} \\ c _ {3} \\ c _ {4} \\ c _ {5} \\ c _ {6} \end{array} \right] = \left[ \begin{array}{l} a _ {i} (t _ {0} ^ {i}) \\ v _ {i} (t _ {0} ^ {i}) \\ p _ {i} (t _ {0} ^ {i}) \\ a _ {i} (t _ {f} ^ {i}) \\ v _ {i} (t _ {f} ^ {i}) \\ p _ {i} (t _ {f} ^ {i}) \end{array} \right] \tag {47}
$$

Based on the aforementioned equations, the constant $h_i$ can be determined as $h_i = [c_1, c_2, c_3, c_4, c_5, c_6]^T$ . Subsequently, the optimal control speed for each vehicle on the ramp at each step can be planned according to Eq. (44). 

# 4. Simulation study

# 4.1. Simulation design

This section introduces the simulations to validate the efficacy of the proposed DCoMA strategy. The macroscopic state planning of DCoMA, collaborative platoon behavior of mainline cooperative vehicles, and motion behavior of on-ramp vehicles are all programmed in Python and integrated with SUMO through the Traci interface (Tang et al., 2022). In this case, the IDM is used for the CAV following model and the Krauss model is used for the HDV following model. The lane change model uses the lc2013 model. The values of model parameters are shown in Table 1. In this context, the safe headway time $T$ for CAVs is $0.7 \, \text{s}$ , which also represents the $T$ value used for FD modeling when the market penetration rate (MPR) of CAV is $100\%$ . Due to the presence of HDVs, the $T$ values for FD are adjusted to $0.8 \, \text{s}$ and $0.9 \, \text{s}$ for MPRs of $60\%$ and $30\%$ , respectively. 

The simulation area is depicted in Figure 7. The simulation roadway extends $2000\mathrm{m}$ upstream from the merge area and $1250\mathrm{m}$ downstream, covering the merging impact area defined by HCM (Elefteriadou, 2016). A 300-meter-long on-ramp is connected to the mainline through a 250-meter acceleration lane. Detector A is placed at the beginning of the ramp, spanning $100\mathrm{m}$ ; Detection area B1 is located at the start of the mainline and spans $100\mathrm{m}$ , while Detection area B2 is situated $200\mathrm{m}$ from the start and covers $1000\mathrm{m}$ . The distribution of vehicles in Detection area B2 is updated every $10\mathrm{s}$ . 

This study conducts simulations under a mainline flow of 2000 veh/h, considering five levels of on-ramp flow (100, 200, 300, 400 and 500 veh/h) and three penetration rates of CAVs (30%, 60% and 100%). For each simulation scenario, four cases are set up: the ALINEA case, X-ALINEA/Q case, CoopMA-controlled case, and DCoMA-controlled case, all employing the same assumptions and models. ALINEA represents a classical macroscopic RM method, while X-ALINEA/Q is an advanced iteration of this approach (Smaragdis and Papageorgiou, 2003). Drawing from established parameter settings found in existing literature (Scarinci et al., 2017), this paper outlines the control parameters for both the ALINEA and X-ALINEA/Q cases, as well as for scenarios controlled using the CoopMA strategy. These parameters are comprehensively detailed in Tables 2 and 3, respectively. 

A key concept of the proposed strategy is the indirect control of HDVs through the management of CAVs. Consequently, the distribution of CAVs significantly influences the effectiveness of this control. To evaluate the strategy's effectiveness in scenarios involving long HDV platoons, we introduce the concept of platoon intensity (Yao et al., 2022). Typically denoted by the symbol $PI$ , platoon intensity ranges from -1 to 1. Higher values of $PI$ indicate a more concentrated distribution of CAVs. Figure 8 illustrates the structure of the mixed-vehicle platoon under varying platoon intensities with a $50\%$ CAV MPR. 

Specifically, Figure 8(a) shows that when the $PI = -1$ , CAVs and HDVs are alternately distributed within the mixed traffic flow, resulting in a disordered state. Transitioning to Figure 8(b), when the $PI$ ranges from $-1$ to $1$ , the traffic flow exhibits a random state. Within this range, the likelihood of CAVs forming a platoon increases as the $PI$ nears $1$ , and conversely decreases as it diverges from this value. Finally, as illustrated in Figure 8(c), when the $PI$ reaches $1$ , all CAVs follow each other, forming a coherent platoon. Similarly, all 


Table 1 Driving behavior model parameters.


<table><tr><td colspan="3">(a) IDM parameters</td></tr><tr><td>Parameter</td><td>Value</td><td>Unit</td></tr><tr><td>a max</td><td>3</td><td>m/s2</td></tr><tr><td>b conf</td><td>4.5</td><td>m/s2</td></tr><tr><td>δ</td><td>4</td><td>-</td></tr><tr><td>ν0</td><td>120</td><td>km/h</td></tr><tr><td>s0</td><td>2.5</td><td>m</td></tr><tr><td>T</td><td>0.7 (CAV, MPR = 100 %) 0.8 (MPR = 60 %)0.9 (MPR = 30 %)</td><td>s</td></tr></table>


(b) Krauss parameters


<table><tr><td>Parameter</td><td>Value</td><td>Unit</td></tr><tr><td>a max</td><td>2</td><td>m/s2</td></tr><tr><td>b conf</td><td>3</td><td>m/s2</td></tr><tr><td>σ</td><td>0.5</td><td>-</td></tr><tr><td>τ</td><td>1</td><td>s</td></tr><tr><td>speedFactor</td><td>normc(1,0.0083,0.017,1.983)</td><td>-</td></tr></table>


(c) Lane-changing parameters


<table><tr><td>Parameter</td><td>Description</td><td>CAV</td><td>HDV</td><td>Unit</td></tr><tr><td>Desired headway</td><td>default</td><td>0.1</td><td>1</td><td>s</td></tr><tr><td>lcCooperative</td><td>Willingness to perform cooperative lane changing. Lower values result in reduced cooperation.</td><td>1</td><td>0.8</td><td>-</td></tr><tr><td>lcTimeToImpatience</td><td>Time to reach maximum impatience. Impatience grows whenever a lane-change maneuver is blocked.</td><td>Infinity (default, no impatience growth)</td><td>180</td><td>s</td></tr><tr><td>lcImpatience</td><td>The dynamic factor for modifying lcAssertive. If the lane-changing maneuver is blocked, the impatience increases with time until successful lane changes</td><td>0</td><td>1</td><td>-</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/de2e692069d76ac3a4c566aecc9cdae185fc87d8d810cae3ed5ca2ce9d3baefe.jpg)



Fig. 7. Schematic diagram of simulation area.



Table 2 Parameter Settings for ALINEA Strategy and X-ALINEA/Q Strategy.


<table><tr><td>Parameter</td><td>Value</td><td>Unit</td></tr><tr><td>Cycle</td><td>100</td><td>s</td></tr><tr><td>KR</td><td>70</td><td>-</td></tr><tr><td>Oexp</td><td>0.3</td><td>veh/h</td></tr><tr><td>wexp</td><td>12</td><td>veh</td></tr></table>


Table 3 Parameter Settings for CoopMA Strategy.


<table><tr><td>Parameter</td><td>Value</td><td>Unit</td></tr><tr><td>np</td><td>10</td><td>veh</td></tr><tr><td>VC</td><td>27.22</td><td>m/s</td></tr><tr><td>Δv</td><td>2.78</td><td>m/s</td></tr><tr><td>CC</td><td>17</td><td>s</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/3999fcbcb6d381606929edf7d27889b4ddc6e52fed4aa6547e14efff3c1d9692.jpg)



Fig. 8. The structure of the mixed-vehicle platoon under varying platoon intensities.


HDVs follow each other within the mixed traffic flow. This formation highlights the self-organization and self-coordination capabilities of the CAV platoon, resulting in a more structured and orderly traffic flow. 

The DCoMA group will conduct simulations at $PI = 0$ and $PI = 1$ . At $PI = 0$ , the traffic flow is in a random state, which more accurately reflects real-world traffic conditions. At $PI = 1$ , CAVs follow one another in a line formation, with all HDVs also following suit. This scenario aims to study the performance of DCoMA strategies under extreme conditions. 

The input parameters for DCoMA are presented in Table 4. Each research scenario is repeated 10 times, with each experiment having a warm-up period of $300\mathrm{s}$ and a total simulation time of $1800\mathrm{s}$ . The analysis focuses on the aggregated data from the 10 repeated experiments for each scenario. 


Table 4 Parameter Settings for DCoMA Strategy.


<table><tr><td>Parameter</td><td>Value</td><td>Unit</td></tr><tr><td>ωmain</td><td>1</td><td>-</td></tr><tr><td>ωramp</td><td>1</td><td>-</td></tr><tr><td>ωe</td><td>5</td><td>-</td></tr><tr><td>ωc</td><td>1</td><td>-</td></tr><tr><td>vr</td><td>16.67</td><td>m/s</td></tr><tr><td>amax</td><td>3</td><td>m/s2</td></tr><tr><td>gm</td><td>3</td><td>s</td></tr></table>

# 4.2. Macroscopic planning results of DCoMA

# 4.2.1. Generated gap length

The central idea of the DCoMA strategy is to integrate macro-level mainline gap creation with microscopic-level on-ramp vehicle control, thereby facilitating on-ramp merging. At its core, the efficacy of this strategy at the macroscopic scale is reflected in the dimensions of the gaps it creates. To assess the macro-level planning performance of the DCoMA strategy, we examined the total and average lengths of the gaps, comparing the gap-creation capability of DCoMA and CoopMA strategies across varying CAV penetration rates and on-ramp traffic volumes. The 'total gap length' is quantified as the aggregate of all gap lengths produced by the strategy within an 1800-second interval. In parallel, the 'average gap' represents the mean of these gap lengths over the same duration. 

Fig. 9(a) illustrates the total gap length planned by the CoopMA and DCoMA cases at a CAV penetration rate of $100\%$ . This illustration serves to compare the gap planning proficiency of the two strategies under diverse on-ramp traffic volumes. Notably, the total gap length for CoopMA remains constant at $392~s$ . When the on-ramp traffic volume is low $(100\text{veh/h})$ , the capacity of the mainline is sufficient to accommodate the merging demand of the on-ramp vehicles. As such, there's no need for the DCoMA strategy to create excessive gaps, resulting in a total planned gap length of only $84.6~s$ . As the on-ramp traffic volume escalates, the merging demand from the on-ramp vehicles intensifies, necessitating DCoMA to increment the total gap length to ensure safe merging of the on-ramp vehicles. Therefore, as on-ramp traffic volume surges, the total gap length planned by the DCoMA strategy exhibits an upward trend. With an increase in on-ramp traffic to $500\text{veh/h}$ , the total gap duration augments to $766.4~s$ . This suggests that the DCoMA strategy can flexibly adjust the total gap length based on varying on-ramp traffic scenarios, optimizing traffic flow for safety and efficiency. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/a91902fc7baf0dcdcf2be7c424b472fbbe34ec3ef08af876f7d21c6ebd75a761.jpg)



(a) Aggregate data of 10 experiments


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/9e184fe0604c23fdc2bd929aafa85b9c3b39f7264e5b98e305edf6241a2c5caf.jpg)



(b) Data from Experiment.1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/06319a417cc696d58ef6a3eeeac962a35354a0d7afe47f12468547d28647b79e.jpg)



(c) Data from Experiment.2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/08aaf4539386569e438f0fc5fd80b24dacc91f60532382f5a851bd6369007096.jpg)



(d) Data from Experiment.3



Fig. 9. Total gap length planned by CoopMA and DCoMA cases at $100\%$ CAV penetration rate.


In Fig. 9(a), a notable increase in the total planned gap length is observed as the on-ramp flow escalates from $100\, \text{veh/h}$ to $200\, \text{veh/h}$ . However, it is important to recognize that Fig. 9(a) aggregates the average outcomes of all experimental groups, inclusive of those that experienced traffic flow collapses. These specific instances do not accurately represent the gap planning capabilities of the strategy under typical conditions. To address this, we selectively analyzed data from experimental groups that did not encounter traffic flow disruptions for each scenario, as detailed in Fig. 9(b) (c) (d). When compared to Fig. 9(a), the progression in total gap length planned by the DCoMA strategy in Fig. 9(b) (c) (d) is markedly more gradual. This nuanced increase in gap length underscores the adaptability of the DCoMA strategy in tailoring gap creation to varying traffic conditions, affirming its capacity to dynamically adjust the gap length. 

Fig. 10 illustrates the variations in average and total gap lengths planned by the CoopMA and DCoMA strategies under three on-ramp traffic volumes as the CAV penetration rate changes. In the figure, the bar graphs depict the total gap lengths planned by the strategies, while the line charts show the average gap lengths. 

In the CoopMA-controlled case, gap planning did not account for the effects of CAV penetration rate and the volume of traffic flow, thus the average gap length remained constant at a value of 4 s, and the total gap length was 392 s. Within the DCoMA-controlled cases, as the CAV penetration rate increased, there was a general upward trend in the total gap length, while the average gap length showed a downward trend. This can likely be attributed to the fact that at lower CAV penetration rates, the number of CAVs available for cooperation is limited, leading to fewer generated gaps and consequently a larger average gap length. However, with higher CAV penetration rates, the greater availability of CAVs facilitates the creation of more gaps, leading to a reduction in the average gap length. With shifts in on-ramp traffic flow, the DCoMA strategy demonstrates enhanced adaptability. When on-ramp flow is at a lower threshold (100 veh/h), the total gap length planned by the DCoMA strategy is less than that by CoopMA, avoiding superfluous gap wastage. Conversely, at higher ramp flows (300, 500 veh/h), the DCoMA strategy timely augments the gap length, dynamically catering to the merging demands of on-ramp vehicles. 

# 4.2.2. Average travel time

Table 5 shows the average travel time in different demand scenarios. For each scenario, three travel time values are separately measured from $a$ ) the total average travel time (including the mainline and the on-ramp); $b$ ) the mainline average travel time; and $c$ ) the on-ramp average travel time. 

In most scenarios, as mainline and ramp traffic volumes increase, there is a corresponding increase in overall travel time, mainline travel time, and on-ramp travel time. This increase is due to the excess merging vehicles further reducing traffic efficiency. This pattern aligns with the widely held understanding that higher traffic volumes generally result in longer driving times. 

When examining different demand scenarios, DCoMA consistently outperforms the other three strategies in reducing travel time. The overall reductions in travel time are less significant at lower traffic volumes compared to higher volumes. This suggests that at lower on-ramp volumes, multiple strategies demonstrate comparable effectiveness in optimizing system travel time. However, in scenarios of higher traffic flows, DCoMA markedly reduces the overall system travel time. Specifically, with a mainline flow of 2000 veh/h and an on-ramp flow of 500 veh/h, DCoMA achieves travel time reductions of $5.93\%$ (ALINEA), $5.68\%$ (X-ALINEA/Q), and $5.65\%$ (CoopMA). The substantial improvements brought about by DCoMA, particularly for on-ramp vehicles (with a delay reduction of $36.70\%$ compared to ALINEA), underscore its efficacy in facilitating smooth merging and significantly diminishing average travel time, thereby markedly enhancing the overall efficiency of the traffic system. 

Table 6 shows the average travel time under different PIs and MPRs. At an MPR of $30\%$ , both overall and on-ramp travel times increase with higher mainline and on-ramp traffic volumes. Despite variations in travel times under conditions of $PI = 0$ and 1, the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/e799fa99f6b525ea9699f0e52e0979b6642e68221b38e29aed25353039c989aa.jpg)



Fig. 10. Changes in average and total gap lengths under different strategies with varying CAV penetration rates.



Table 5 Results of average travel time under different traffic flows.


<table><tr><td colspan="11">Average travel time of ALINEA (s)</td></tr><tr><td colspan="2"></td><td colspan="3">Total travel time</td><td colspan="3">Mainline travel time</td><td colspan="3">On-ramp travel time</td></tr><tr><td colspan="2">Mainline flow (veh/h)</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td></tr><tr><td rowspan="5">Ramp flow (veh/h)</td><td>100</td><td>117.89</td><td>117.93</td><td>118.25</td><td>119.93</td><td>119.42</td><td>119.32</td><td>93.55</td><td>93.12</td><td>95.31</td></tr><tr><td>200</td><td>120.94</td><td>122.64</td><td>119.77</td><td>124.97</td><td>125.56</td><td>122.11</td><td>97.32</td><td>97.93</td><td>96.11</td></tr><tr><td>300</td><td>121.11</td><td>123.18</td><td>120.95</td><td>126.34</td><td>126.37</td><td>123.58</td><td>100.25</td><td>105.50</td><td>103.50</td></tr><tr><td>400</td><td>121.02</td><td>123.27</td><td>121.49</td><td>126.26</td><td>124.90</td><td>123.58</td><td>105.02</td><td>117.09</td><td>110.35</td></tr><tr><td>500</td><td>121.51</td><td>122.85</td><td>123.33</td><td>125.70</td><td>122.73</td><td>120.01</td><td>111.29</td><td>123.99</td><td>141.93</td></tr><tr><td colspan="11">Average travel time of X-ALINEAQ (s)</td></tr><tr><td colspan="2"></td><td colspan="3">Total travel time</td><td colspan="3">Mainline travel time</td><td colspan="3">On-ramp travel time</td></tr><tr><td colspan="2">Mainline flow (veh/h)</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td></tr><tr><td rowspan="5">Rampflow (veh/h)</td><td>100</td><td>117.89</td><td>117.93</td><td>118.25</td><td>119.93</td><td>119.42</td><td>119.32</td><td>93.55</td><td>93.12</td><td>95.31</td></tr><tr><td>200</td><td>120.94</td><td>122.64</td><td>119.77</td><td>12 4.97</td><td>125.56</td><td>122.11</td><td>97.32</td><td>97.93</td><td>96.11</td></tr><tr><td>300</td><td>121.11</td><td>123.18</td><td>120.95</td><td>126.34</td><td>126.37</td><td>123.58</td><td>100.25</td><td>105.50</td><td></td></tr><tr><td>400</td><td>121.02</td><td>123.27</td><td>121.49</td><td>126.26</td><td>124.90</td><td>123.58</td><td>105.02</td><td>117.09</td><td>110.35</td></tr><tr><td>500</td><td>121.87</td><td>122.64</td><td>123.01</td><td>125.13</td><td>122.58</td><td>120.07</td><td>113.78</td><td>123.62</td><td>140.78</td></tr><tr><td colspan="11">Average travel time of CoopMA (s)</td></tr><tr><td colspan="2"></td><td colspan="3">Total travel time</td><td colspan="3">Mainline travel time</td><td colspan="3">On-ramp travel time</td></tr><tr><td colspan="2">Mainline flow (veh/h)</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td></tr><tr><td rowspan="5">Rampfow (veh/h)</td><td>100</td><td>118.84</td><td>119.79</td><td>120.24</td><td>119.10</td><td>120.79</td><td>121.29</td><td>118.07</td><td>107.95</td><td>99.90</td></tr><tr><td>200</td><td>120.84</td><td>125.87</td><td>121.28</td><td>122.42</td><td>126.43</td><td>123.50</td><td>111.37</td><td>126.94</td><td>99.24</td></tr><tr><td>300</td><td>124.09</td><td>126.38</td><td>123.29</td><td>123.50</td><td>128.61</td><td>126.49</td><td>130.82</td><td>117.99</td><td>101.22</td></tr><tr><td>400</td><td>129.43</td><td>149.67</td><td>121.03</td><td>125.36</td><td>128.74</td><td>124.75</td><td>144.10</td><td>388.15</td><td>101.25</td></tr><tr><td>500</td><td>131.46</td><td>147.14</td><td>122.98</td><td>127.77</td><td>127.75</td><td>126.96</td><td>141.86</td><td>331.74</td><td>105.46</td></tr><tr><td colspan="11">Average travel time of DCoMA (s)</td></tr><tr><td colspan="2"></td><td colspan="3">Total travel time</td><td colspan="3">Mainline travel time</td><td colspan="3">On-ramp travel time</td></tr><tr><td colspan="2">Mainline flow (veh/h)</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td></tr><tr><td rowspan="5">Ramped flow (veh/h)</td><td>100</td><td>116.15</td><td>118.23</td><td>110.37</td><td>118.50</td><td>119.96</td><td>111.44</td><td>87.90</td><td>87.66</td><td>88.14</td></tr><tr><td>200</td><td>120.00</td><td>123.06</td><td>115.03</td><td>125.25</td><td>126.68</td><td>117.48</td><td>89.02</td><td>91.19</td><td>87.24</td></tr><tr><td>300</td><td>119.28</td><td>121.76</td><td>116.64</td><td>126.91</td><td>126.95</td><td>120.21</td><td>88.76</td><td>90.62</td><td>89.44</td></tr><tr><td>400</td><td>118.90</td><td>122.25</td><td>116.11</td><td>128.63</td><td>129.39</td><td>120.91</td><td>89.59</td><td>91.10</td><td>88.37</td></tr><tr><td>500</td><td>118.11</td><td>120.66</td><td>116.02</td><td>129.83</td><td>129.73</td><td>121.52</td><td>89.78</td><td>88.99</td><td>89.84</td></tr></table>

overall trend remains consistent: travel times increase with traffic volume. When the MPR increases to $60\%$ , data indicates a reduction in both overall and on-ramp travel times at the same traffic volumes compared to when the MPR is at $30\%$ . This suggests that a higher proportion of CAVs can enhance traffic flow efficiency and reduce travel times. This may be due to the lower MPR of CAVs resulting in longer platoons on the on-ramp. 

Under conditions of low mainline flow (1000, 1500 veh/h), the continuous distribution of CAVs $(PI = 1)$ slightly increases the overall travel time, with a maximum increase of $5.84\%$ (MPR = 60%, mainline flow = 1500 veh/h, onramp flow = 100 veh/h). This increase is likely due to the continuous operation of CAVs promoting more effective vehicle interactions, which may not align well with the DCoMA control strategy. For on-ramp travel times, data at $PI = 1$ generally indicate higher travel times than at $PI = 0$ under most traffic conditions. This suggests that a continuous CAV distribution leads to a more concentrated HDV distribution, complicating the timing adjustment of HDVs through CAVs at merge points, thus reducing the strategy's effectiveness. 

Notably, when the mainline flow increases to $2000\mathrm{veh / h}$ , a continuous CAV/HDV distribution enhances traffic efficiency, with the maximum improvement reaching $20.39\%$ (MPR = 30%, mainline flow = 2000 veh/h, onramp flow = 600 veh/h). This improvement occurs because higher flows increase the number of CAVs available for cooperation, thus not impairing strategy control. Moreover, the increased number of CAVs enhances vehicle interactions amongst CAVs, thereby reducing travel times. 

# 4.2.3. Overall speed spatio-temporal distribution

To investigate the temporal and spatial dynamics of traffic states under different strategies, a detailed analysis was conducted at three distinct time intervals for a scenario with a mainline flow of 2000 veh/h and an on-ramp flow of 500 veh/h. Fig. 11 illustrates the global speed spatio-temporal distributions for five cases, comparing the operation of the traffic system in the merging zone (spanning 0 m to 3250 m for the mainline and 0 m to 300 m for the on-ramp) under each strategy. In these visualizations, the varying shades represent different vehicle speeds. 

Fig. 11(a), (b), and (c) show the impact of the other three strategies on traffic. Here, mainline traffic begins to decelerate after $400\mathrm{s}$ under strategy control, accompanied by deceleration and queuing on the on-ramps. Over time, particularly by $1000\mathrm{s}$ , stop-and-go waves develop on the mainline, intensifying and expanding in both width and depth by $1500\mathrm{s}$ . While these strategies effectively 


Table 6 Results of average travel time under different PIs and MPRs.


<table><tr><td colspan="11">MPR = 30 %</td></tr><tr><td colspan="2">PI = 0</td><td colspan="3">Total travel time</td><td colspan="3">Mainline travel time</td><td colspan="3">On-ramp travel time</td></tr><tr><td colspan="2">Mainline flow (veh/h)</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td></tr><tr><td rowspan="5">Ramp flow (veh/h)</td><td>100</td><td>119.78</td><td>124.38</td><td>129.09</td><td>122.51</td><td>126.62</td><td>131.70</td><td>88.07</td><td>89.14</td><td>89.49</td></tr><tr><td>200</td><td>123.42</td><td>128.15</td><td>133.13</td><td>129.27</td><td>132.34</td><td>136.96</td><td>91.48</td><td>91.23</td><td>91.63</td></tr><tr><td>300</td><td>122.43</td><td>127.88</td><td>133.92</td><td>130.68</td><td>134.27</td><td>139.91</td><td>89.44</td><td>91.60</td><td>94.21</td></tr><tr><td>400</td><td>121.92</td><td>128.15</td><td>139.20</td><td>132.77</td><td>136.13</td><td>146.51</td><td>91.49</td><td>92.62</td><td>98.22</td></tr><tr><td>500</td><td>122.40</td><td>127.02</td><td>170.49</td><td>134.68</td><td>137.07</td><td>210.40</td><td>93.20</td><td>93.16</td><td>97.62</td></tr><tr><td colspan="2">PI = 1</td><td colspan="3">Total travel time</td><td colspan="3">Mainline travel time</td><td colspan="3">On-ramp travel time</td></tr><tr><td colspan="2">Mainline flow (veh/h)</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td></tr><tr><td rowspan="5">Ramp flow (veh/h)</td><td>100</td><td>124.34</td><td>128.59</td><td>132.31</td><td>127.84</td><td>131.04</td><td>134.17</td><td>91.70</td><td>90.95</td><td>93.68</td></tr><tr><td>200</td><td>126.93</td><td>130.43</td><td>132.03</td><td>133.25</td><td>135.48</td><td>136.15</td><td>91.92</td><td>92.08</td><td>91.36</td></tr><tr><td>300</td><td>125.59</td><td>131.20</td><td>133.87</td><td>134.79</td><td>137.92</td><td>139.71</td><td>91.58</td><td>94.10</td><td>94.72</td></tr><tr><td>400</td><td>125.21</td><td>130.71</td><td>134.31</td><td>137.30</td><td>139.45</td><td>141.04</td><td>93.88</td><td>95.23</td><td>95.97</td></tr><tr><td>500</td><td>126.51</td><td>129.91</td><td>135.72</td><td>140.06</td><td>140.36</td><td>144.52</td><td>95.59</td><td>95.16</td><td>96.91</td></tr><tr><td colspan="2">MPR = 60 %</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">PI = 0</td><td colspan="3">Total travel time</td><td colspan="3">Mainline travel time</td><td colspan="3">On-ramp travel time</td></tr><tr><td colspan="2">Mainline flow (veh/h)</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td></tr><tr><td rowspan="5">Ramp flow (veh/h)</td><td>100</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>200</td><td>119.64</td><td>122.96</td><td>130.51</td><td>124.91</td><td>126.86</td><td>133.97</td><td>88.70</td><td>89.83</td><td>91.06</td></tr><tr><td>300</td><td>121.52</td><td>124.40</td><td>131.90</td><td>129.03</td><td>129.68</td><td>137.24</td><td>91.73</td><td>91.45</td><td>93.96</td></tr><tr><td>400</td><td>119.55</td><td>122.45</td><td>131.09</td><td>129.40</td><td>129.64</td><td>138.03</td><td>89.44</td><td>89.60</td><td>92.87</td></tr><tr><td>500</td><td>119.70</td><td>122.74</td><td>159.90</td><td>131.85</td><td>131.62</td><td>203.39</td><td>90.51</td><td>91.19</td><td>97.34</td></tr><tr><td colspan="2">PI = 1</td><td colspan="3">Total travel time</td><td colspan="3">Mainline travel time</td><td colspan="3">On-ramp travel time</td></tr><tr><td colspan="2">Mainline flow (veh/h)</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td><td>1000</td><td>1500</td><td>2000</td></tr><tr><td rowspan="5">Ramp flow (veh/h)</td><td>100</td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3"></td></tr><tr><td>200</td><td>122.89</td><td>125.90</td><td>126.45</td><td>125.92</td><td>128.24</td><td>127.78</td><td>91.36</td><td>92.02</td><td>90.50</td></tr><tr><td>300</td><td>125.47</td><td>127.26</td><td>127.95</td><td>131.64</td><td>131.89</td><td>131.08</td><td>91.52</td><td>90.77</td><td>91.64</td></tr><tr><td>400</td><td>123.65</td><td>127.62</td><td>129.43</td><td>132.50</td><td>134.05</td><td>134.10</td><td>90.95</td><td>92.25</td><td>94.21</td></tr><tr><td>500</td><td>123.50</td><td>127.41</td><td>128.92</td><td>134.95</td><td>135.65</td><td>135.46</td><td>92.97</td><td>93.45</td><td>94.84</td></tr></table>

mitigate oscillations on the mainline compared to the base case, they induce prolonged on-ramp queuing, corroborating the findings of Section 5.1.1. Specifically, CoopMA demonstrates shorter on-ramp queues but more pronounced traffic waves on the mainline. 

In contrast, the DCoMA strategy, as shown in Fig. 11(d), optimizes the on-ramp traffic operations. Despite deceleration in the mainline, vehicles in the affected areas continue to travel at high speeds $(15~m / s)$ . A localized low-speed band forms on the on-ramp due to vehicles decelerating in response to the motion planning algorithm for timely merging into appropriate gaps. Compared to the other strategies, DCoMA can reduce congestion on the on-ramp while maintaining the efficiency of the mainline, showcasing its superiority in managing traffic dynamics. 

# 4.2.4. Fundamental diagram

A fundamental concept of the proposed strategy involves reducing the gap with CAVs. Vehicle gaps are closely associated with density and significantly impact FD characteristics. Fig. 12 displays the FDs of traffic at various penetration rates obtained through simulation. Data for State A, represented by blue points, were collected from uncontrolled sections, while data for State C, marked in red, were gathered from sections upstream of merge points. Points with zero density are denoted as State O, represented in green, signifying the generated gap. The black solid line illustrates the theoretical FD according to the IDM. Besides States A, C, and O, a fourth state exists, indicated by grey points in the diagram. This occurs as detectors placed upstream of merge points capture both States C and O, as well as their mixed states, where flow and density values lie between States C and O. 

Fig. 12(a), (b), and (c) demonstrate that the simulated scatter points closely align with the theoretical curve, with State C exhibiting greater flow and density than State A. This indicates that the strategy effectively transitions traffic flow from State A to State C, thereby increasing traffic density and creating gaps. Fig. 12(d) shows the FD at different penetration rates, where the peak values of FD increase as the penetration rate rises. This is attributed to the more coordinated driving of autonomous vehicles, which reduces instances of stopping and slow driving. 

# 4.3. Microscopic vehicle trajectory results of DCoMA

This section delves into the micro-level aspects, analyzing the spatio-temporal process of merging under the DCoMA strategy 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/da70611f91159db0f2dfb8ffc36f6f4a5b9683f4792aac0aa1e965e757d6e71d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/34e30fe16578dc8816ef78c4f75b6a2e7a24faa8ddce39f97751dad8282b52a1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/c9a2d56ed46369d7daef710799c7b417df486f2ca2c17ebbffa795b1ce36b828.jpg)



(a) ALINEA


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/e19206e82965b296e912511ceb51055871ad9fe644f54048e96b8771a06d28d1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/1574557aa247da997d0e4b1a723567c43ca7df58238d29b512727486fb44bea5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/5d83e5b14e28b5a29e4467a4743a704180e305a8e8771a8b999f5f067b894165.jpg)



(b) X-ALINEA/Q


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/d1a711d95a7181b5df9e693507f4489f6f71432dc6d649008b8595ddea01b6d9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/c25822a0c8002b0477be619a4a1462f958e1c1c70ccf0feb8bd3ba730c559a40.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/6fe83a30710f7de8b73fa2b644c2722ab404b60ddcd5cfd67220e43409ad8844.jpg)



(c) CoopMA


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/2e614688fe56143c257d1f6cbe260d59d89a050e67ec6c202b684ea68ca05adc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/2681d91239375124dfea244f054fe656e7cd1c5b050d93098ed90c24ad822e0a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/4d1023bce3175e7809a6595405e02c77675b84b8368829ce36e8376866efd443.jpg)



(d) DCoMA



Fig. 11. Speed spatiotemporal distribution diagram of mainline and on-ramp under different time slices.


through vehicle trajectory data. Fig. 13 presents the vehicle trajectories for three cases under varying on-ramp traffic volumes when the penetration rate is $100\%$ . The trajectories cover a 2500-meter stretch, inclusive of a 250-meter merging area, 1250-meter upstream of the merging zone, and 1000-meter downstream of the merging area. Within this, the gray solid lines depict the trajectories of the mainline vehicles, while the red solid lines represent the trajectories of the on-ramp vehicles. 

Fig. 13(a)-(i) demonstrate that, with an on-ramp traffic flow of $100\text{veh/h}$ , vehicles in all three groups seamlessly merge into the mainline. However, as the on-ramp flow increases to $300\text{veh/h}$ , differences in strategy effectiveness become evident. Fig. 13(e) and (f) show that in both the CoopMA and DCoMA strategy scenarios, on-ramp vehicles effectively utilize the created gaps for merging, causing minimal disruption to mainline flow. In contrast, on-ramp queues start forming in the X-ALINEA/Q scenarios, as depicted in Fig. 13(d). 

When the on-ramp traffic volume is 500 veh/h, the mainline remains relatively clear under ALINEA, X-ALINEA/Q, and CoopMA; however, significant queuing occurs on the on-ramps. This queuing is due to the number of merging vehicles being less than the number arriving at the on-ramp, as shown in Fig. 13(g)(h). In contrast, as illustrated in Fig. 13(i), the DCoMA strategy ingeniously increases the number and length of planned gaps based on traffic conditions, effectively preventing congestion on both the ramp and the mainline. This highlights DCoMA's ability to dynamically adjust planned gaps in response to on-ramp traffic fluctuations, thereby ensuring efficient and safe traffic flow. 

# 5. Result and discussion

To further demonstrate the effectiveness of the DCoMA strategy proposed in this paper, we evaluate its performance in the mixed traffic flow under various CAV penetration rates from three perspectives: (1) efficiency, (2) safety, and (3) environmental impact. We then compare the ALINEA case, the X-ALINEAQ case, the CoopMA-controlled case, and the DCoMA-controlled case. The detailed results of these three aspects will be elaborated upon in the following subsections of this section. 

# 5.1. Efficiency performance of DCoMA

Average travel time, mainline speed spatio-temporal distribution, and overall spatio-temporal speed distribution are employed to assess the efficiency of the mixed traffic flow. To evaluate the efficiency performance of DCoMA in different demand and CAV penetration rate scenarios, four levels of CAV penetration rates were given, i.e., $30\%$ , $60\%$ and $100\%$ . For each CAV penetration rate level, the different flows of on-ramp and mainline were defined (mainline:1000, 1500 and 2000 veh/h, on-ramp: 100, 200, 300, 400, 500 veh/h). Each simulation ran for $1800s$ including $300s$ for warming up and $1500s$ for performance measurements. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/aead78721cdee5a0954ad29d2c3723527c16215893ae9413bec191f02836a0a5.jpg)



(a) FD under MPR=30%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/a6ba87058ec52bccc26819caff78600c3bb86acfd1fd9f493fd6aa00a2816bb8.jpg)



(b) FD under MPR=60%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/c7c3d0bb78c7501f64ceec34f9516e089d195b653259b7cfc4ab67c2991c3a0b.jpg)



(c) FD under MPR=100%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/3abaedfab092fe7565b26b1ef1568d7c92595429e2563ff441b0116128112fe7.jpg)



(d) Comparison of FDs under different MPRs



Fig. 12. Fundamental diagrams under various penetration rates obtained by simulation.


The improvement effect of the DCoMA strategy on travel time is most significant when the mainline flow is 2000 $veh / h$ and the ramp flow is 500 $veh / h$ . Therefore, a detailed analysis of this scenario was carried out to explore the application effect of DCoMA under different CAV penetration rates. Fig. 14 shows the contour plots of the mainline speed for the five cases, comparing the performance of the mainline traffic in the merging area (from 2000 to 2250 m) and the upstream section of the merging area (from 500 to 3500 m). 

As evident from Fig. 14, at a $30\%$ MPR, the DCoMA strategy maintains higher speeds in the merging area, with upstream speeds remaining stable. In contrast, the X-ALINEA/Q and CoopMA strategies cause minor oscillations in mainline speeds. With the MPR increasing to $60\%$ , all strategies show improved speeds upstream of the merging areas. At a $100\%$ MPR, all three strategies reach peak speeds in the merging areas. 

Overall, DCoMA consistently demonstrates superior speed management across varying levels of MPR, particularly at higher rates. While X-ALINEA/Q and CoopMA also sustain high speeds at higher penetration rates, their performance on mainline speeds diminishes as the penetration rate decreases. 

# 5.2. Safety performance of DCoMA

To validate the beneficial impact of the DCoMA strategy on traffic safety, we employed two commonly used Surrogate Safety Measures (SSMs) (Formosa et al., 2020; Mahmud et al., 2017; Yang et al., 2022): Time To Collision (TTC) and Deceleration Rate to Avoid a Crash (DRAC). A larger TTC value suggests a broader safety gap between vehicles, denoting increased traffic safety. On the other hand, a smaller DRAC value indicates that vehicles require less deceleration to avert a collision, translating to higher traffic safety. Moreover, we calculated the traffic conflict rate (average conflicts per vehicle) based on several SSMs for further safety assessment. The parameters used in determining conflicts include TTC, DRAC, Modified DRAC (MDRAC), Post Encroachment Time (PET), Brake Rate (BR), Spacing (SGAP), and Time Headway (TGAP). Encounters are classified as conflicts if their measurements surpass a given threshold. Based on the research by Zhang et al. (2019), the SSMs employed in this study and their respective conflict determination thresholds can be found in Table 7. 

This research employs density plots to articulate the distribution of SSM data, thereby evaluating the impact of various traffic management strategies on safety. Fig. 15(a) illustrate the distributions of DRAC under diverse on-ramp flow conditions. The graph 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/d16fd59ab8e22aa4b7afc1ab07026d6d852b55d68e65e4c3f1b1d7b5ebc1d4dd.jpg)



(a) X-ALINEA/Q: 2000-100-100%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/cca4817052a770cd60f240f883a44732b0cc8113c9b351d7164b39a29cdf6def.jpg)



(b) CoopMA: 2000-100-100%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/e02e960da22b1938c1899c53d8035cff1cb91ca6fa86d5d25ca7ea55e3b3a25a.jpg)



(c) DCoMA: 2000-100-100%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/eb4c446ca2aba0d1e9852efb525cddaaf2d02fdb881e9719ac3ad21c7083e6bb.jpg)



(d) X-ALINEA/Q: 2000-300-100%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/b80a8fe091621a51a6310ec31d241b8053ba40a4efac7994148d32fc521479f4.jpg)



(e) CoopMA: 2000-300-100%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/aa66edf0d00d7d932528b9990995dcf330cc9d261573b79c3ba98339c7a60c80.jpg)



(f) DCoMA: 2000-300-100%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/d7e05f8ed151efbeaa2f3cd86351da5a6fcf71b6e1d176661746bc83d6cd210d.jpg)



(g) X-ALINEA/Q: 2000-600-100%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/a2550837eec0c24fce773e3fdb9f69a2cda9904375e23520f6fdf16adc20801c.jpg)



$(h)$ CoopMA: 2000-600-100%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/79ba848b6c79f5de2c82a7307fdc5528f6f378e61d2ea4dc4d035c25e35c5d51.jpg)



(i) DCoMA: 2000-600-100%



Fig. 13. Results of vehicle trajectories between 500 and $625\mathrm{s}$


illustrates that at low on-ramp traffic volumes (100 veh/h), the distribution of DRAC values across various strategies is fairly similar. However, as on-ramp traffic increases, the distribution for DCoMA is more concentrated at lower DRAC values, indicating smaller variations in speed and more stable traffic flow. In contrast, other strategies exhibit greater speed variability at higher traffic volumes. 

Fig. 15(b) displays the distribution of TTC. At an on-ramp traffic of $100\, \text{veh/h}$ , there is little variation in TTC distributions among the strategies. Yet, as traffic increases, the TTC values for ALINEA and X-ALINEAQ decrease, while CoopMA and DCoMA maintain higher TTC values, suggesting that the latter two may offer greater safety at higher traffic volumes. 

Fig. 15(c) presents the variations in safety metrics with traffic flow for the three scenarios, with a focus on the reciprocal of the TTC, denoted as 1/TTC, for comparative analysis. It is observed that the performance of 1/TTC in the DCoMA-controlled case is less than ideal when the on-ramp flow rate reaches $500\text{veh/h}$ . This suboptimal outcome could be attributed to the high on-ramp flow necessitating frequent acceleration and deceleration maneuvers by both mainline and on-ramp vehicles, thereby escalating the potential for conflicts. 

Nevertheless, the DCoMA-controlled scenario consistently surpasses the other cases across all safety metrics. This superiority aligns with the results observed in Fig. 15(a) and (b), where the DCoMA strategy demonstrated a significant optimization effect on both DRAC and 1/TTC. Furthermore, DCoMA consistently excels in reducing conflict rates. This enhanced performance can be credited to the strategy's efficacy in minimizing inter-vehicle collision risks by finely tuning the merging gaps and speed control. Such optimization not only enhances the safety of the merging process but also instills greater stability in traffic flow, leading to a reduction in conflict occurrences. 

In summary, the analysis encapsulated in Fig. 15 reinforces the beneficial impact of the DCoMA strategy on enhancing traffic safety. By judiciously allocating suitable merging gaps to on-ramp vehicles and refining speed control measures, DCoMA substantially diminishes the risk of inter-vehicle collisions. This contributes to a safer, more stable merging process, laying a solid foundation for the practical implementation of DCoMA in real-world transportation systems. Looking forward, the strategy's potential to significantly 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/2eecfa63df38de8661459c1065cad92959e8ec7322e844e2d28b30b3bf56e002.jpg)



Fig. 14. Mainline speed contour between different cases under different CAV penetration rates.



Table 7 Threshold values for conflict determination of various SSMs.


<table><tr><td>Parameter</td><td>Value</td><td>Unit</td></tr><tr><td>TTC</td><td>3.0</td><td>s</td></tr><tr><td>DRAC</td><td>3.0</td><td>m/s2</td></tr><tr><td>MDRAC</td><td>3.4</td><td>m/s2</td></tr><tr><td>PET</td><td>2.0</td><td>s</td></tr><tr><td>BR</td><td>0.0</td><td>m/s2</td></tr><tr><td>SGAP</td><td>0.2</td><td>m</td></tr><tr><td>TGAP</td><td>0.5</td><td>s</td></tr></table>

decrease traffic accidents and bolster road safety will be instrumental in future urban transportation planning, ensuring the well-being of all road users. 

# 5.3. Environment performance of DCoMA

Speed and acceleration are two important factors affecting motor vehicle fuel consumption and exhaust emissions (Wen et al., 2020; Zhang et al., 2014). As speed increases and acceleration decreases, exhaust emissions tend to decrease. In the low-speed range of less than $10\mathrm{km} / \mathrm{h}$ ( $2.8\mathrm{m} / \mathrm{s}$ ), emissions exhibit an exponential growth trend. This elucidates why reducing vehicle idling can significantly enhance environmental benefits. To evaluate the environmental performance of different strategies, we analyzed the speed distribution of three distinct strategies across the entire area, the mainline, and the on-ramp, as illustrated in Fig. 16. 

Many scholars have carried out various field experiments on the emissions during the operation of vehicles and obtained some useful empirical formulas (Ahn et al., 2002; Barth et al., 2000). In this study, the metric of a vehicle's fuel consumption or pollutant emission is referred to as a Measure of Effectiveness (MOE). Previous research (Ahn, 1998; Ahn et al., 2002) has demonstrated that the instantaneous MOE is a function of the vehicle's instantaneous speed and acceleration. Utilizing the fuel consumption model proposed by (Ahn et al., 2002), the fuel consumption performance of five different strategies was assessed and the results are presented in Table 8. 

Overall, under the DCoMA strategy, the speed distribution of mainline vehicles exhibits a narrow peak, concentrated in higher speed zones. This indicates that the mainline vehicle speeds are more uniform and tend towards higher velocities under the DCoMA strategy. Consequently, this led to a reduction in fuel consumption by $66.51\%$ (CoopMA), $61.27\%$ (ALINEA) and $62.84\%$ (X-ALINEA/Q). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/01535a603f71e659f9381214e5315d43e1fca39040ab610c3fa2bc5a184385d4.jpg)



(a) Distribution of DRAC


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/105728ca4dc79d694d74521528692ffff63410c6bee0fa63899c5fe899b05b5c.jpg)



(b) Distribution of TTC


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/20fdac4bbdae443f34017569892784c795e8e96479c94005b75c21e861cf9aec.jpg)



(c) Comparison of DRAC


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/568819dfda07d8a56eb7e62eaf5013ea56d395bc6f219a024672f099e5d568d1.jpg)



(d) Comparison of 1/TTC


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/86d87488ccb2b391fb9776d61421a582f7a18eb511c30f778d51e22ff063d004.jpg)



(d) Comparison of Conflict rate



Fig. 15. Safety performance of different strategies.


Specifically, for mainline vehicles, the DCoMA strategy results in higher fuel consumption than the other three strategies, owing to the increased fuel usage by mainline vehicles decelerating for merging optimization. 

Regarding the on-ramp vehicles, under the ALINEA, X-ALINEA/Q, and CoopMA strategies, severe queuing leads to extensive idling, with average speeds primarily in the low range $[0m / s,5m / s]$ . This causes a substantial increase in tailpipe emissions. In stark contrast, the DCoMA strategy considerably elevates the vehicle speed, predominantly within the medium range $[17m / s,30m / s]$ , thereby markedly enhancing emission performance. Compared to the three control strategies, the DCoMA strategy reduces fuel consumption by $80.01\%$ (CoopMA), $77.29\%$ (ALINEA), and $78.37\%$ (X-ALINEA/Q), highlighting its advantages in terms of environmental sustainability. 

# 6. Conclusions and future work

The current on-ramp merging models have limited research into the correlation between macroscopic and microscopic traffic flows. Few studies addressing macroscopic traffic conditions typically set fixed flows for both ramps and mainlines, to maintain a consistent gap in the mainline to reduce computational complexities. However, these methodologies overlook the dynamic nature of traffic flow evident in real-world scenarios. Moreover, existing research often assumes a $100\%$ penetration rate of CAVs in the mainline traffic flow when implementing cooperative strategies, overlooking the impact of the spatial distribution of CAVs in mixed traffic on mainline gap formation. This paper introduces a novel on-ramp merging strategy called DCoMA. Firstly, on the macroscopic level, it determines the ideal traffic state for the control strategy based on real-time flow distribution of the on-ramp and mainline. By considering the spatial distribution of CAVs in the mainline mixed traffic flow and focusing on the delay of vehicles on both the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/7fd97284a0c7ba08c6d434aecbb7d1195e7bb4644a2bd08e60e75cff23dd8c53.jpg)



(a) Speed distribution of mainline vehicles $[m / s]$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/7dc95736fd9023331471ca79cd98b12c2c8cdfc3f979064fa774e979074b7f56.jpg)



(b) Speed distribution of on-ramp vehicles $[m / s]$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/2d66e97f2885f478113329d719db16eb508b9b6b04dfd3658248d75eb6d70136.jpg)



(c) Speed distribution of all vehicles $[m / s]$



Fig. 16. Speed distribution of three strategies across the different areas. (a) the overall mean speed, (b) the mainline mean speed and (c) the on-ramp mean speed.



Table 8 Fuel consumption performance.


<table><tr><td colspan="5">Mainline fuel consumption</td></tr><tr><td></td><td>DCoMA</td><td>CoopMA</td><td>ALINEA</td><td>X-ALINEA/Q</td></tr><tr><td>Fuel consumption (mL/veh/km)</td><td>11.77</td><td>10.32</td><td>7.94</td><td>7.86</td></tr><tr><td>Improvement effect (%)</td><td>-</td><td>-14.05</td><td>-48.24</td><td>-49.75</td></tr><tr><td colspan="5">On-ramp fuel consumption</td></tr><tr><td></td><td>DCoMA</td><td>CoopMA</td><td>ALINEA</td><td>X-ALINEA/Q</td></tr><tr><td>Fuel consumption (mL/veh/km)</td><td>12.32</td><td>61.62</td><td>54.26</td><td>56.97</td></tr><tr><td>Improvement effect (%)</td><td>-</td><td>80.01</td><td>77.29</td><td>78.37</td></tr><tr><td colspan="5">Overall fuel consumption</td></tr><tr><td></td><td>DCoMA</td><td>CoopMA</td><td>ALINEA</td><td>X-ALINEA/Q</td></tr><tr><td>Fuel consumption (mL/veh/km)</td><td>12.05</td><td>35.97</td><td>31.10</td><td>32.42</td></tr><tr><td>Improvement effect (%)</td><td>-</td><td>66.51</td><td>61.27</td><td>62.84</td></tr></table>

mainline and on-ramp as the objective function, we implemented specific speed control measures for selected CAVs. It facilitates the formation of varied-sized gaps and vehicle platoons on the mainline. Subsequently, based on the spatio-temporal distribution of these gaps and platoons, a sequence information akin to a traffic signal cycle is recorded (where platoon occupancy is akin to the red light phase and gap occupancy to the green light phase). On-ramp vehicles then optimize their trajectory according to such sequence information, their motion status, and the distance to the merging point, ultimately joining the mainline without stopping. 

To evaluate the proposed DCoMA, simulations were conducted at different levels of traffic demands, and comparisons were made with the existing CoopMA-controlled case, ALINEA-controlled case and X-ALINEAQ-controlled case. The simulation results proved that the DCoMA strategy significantly improves mainline traffic efficiency, especially under high traffic demands. In the presence of the long HDV platoon, the strategy still achieves less negative control results, especially under high traffic volumes. In terms of safety performance, the DCoMA-controlled case consistently outperforms all the cases. This is achieved through larger merging gaps and optimized speed control, which in turn reduces collision risks and boosts traffic safety. In terms of environmental performance, DCoMA effectively increases the proportion of vehicles operating in the high-speed range. This reduces low-speed or idling intervals, leading to a noticeable reduction in harmful exhaust emissions. Overall, the DCoMA strategy holds promise for future urban traffic planning, presenting an effective solution to improve traffic efficiency, safety, and environmental sustainability. 

Despite the contributions mentioned above, this study has its limitations and could be further improved in the following aspects. Firstly, the research scenario of this paper is a single-lane highway. Future studies could attempt to introduce the concept of active lane-changing in multi-lane scenarios. Allowing for flexible lane changes among vehicles on the mainline, it may facilitate the creation and utilization of more gaps. Secondly, given that this strategy indirectly controls HDVs through the management of CAVs, its effectiveness is diminished at lower CAV MPR. Consequently, this strategy is more suitable for environments where the MPR is high (greater than $60\%$ ). A notable limitation of this study is the reliance on the FD of the IDM, which represents an overly idealized scenario. Recognizing this constraint, our future research endeavors will focus on establishing a FD derived from realistically collected data. Such an approach is aimed at capturing the stochastic characteristics inherent in real-world vehicle behavior. By incorporating data that more accurately reflect actual driving patterns, we can ensure that diverse vehicular behaviors are adequately considered in strategic control (Mohammadian et al., 2023). 

This methodology will allow for the development of traffic management strategies that are grounded in authentic traffic flow dynamics, offering a more realistic and effective approach to addressing the complexities of real-world traffic scenarios. 

# CRediT authorship contribution statement

Linheng Li: Writing - review & editing, Writing - original draft, Methodology, Conceptualization. Chen Qian: Writing - review & editing, Writing - original draft, Methodology, Conceptualization. Jing Gan: Writing - review & editing, Software. Dapeng Zhang: Writing - review & editing, Validation. Xu Qu: Writing - review & editing. Feng Xiao: Writing - review & editing, Supervision. Bin Ran: Writing - review & editing, Supervision. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Data availability

Data will be made available on request. 

# Acknowledgements

This work was supported by National Natural Science Foundation of China (Grant No.52202408, 72301217, 72025104), China Postdoctoral Science Foundation (No. 2022 M720719), Sichuan Science and Technology Program (No. 2024NSFSC1055), and the Natural Science Research Start-up Foundation of Recruiting Talents of Nanjing University of Posts and Telecommunications (Grant No. NY222030). 

# Appendix

# Analysis of platoon length

In addressing the issue of platoon length arising from the random distribution of CAVs, we adopt the platoon formation process model as proposed by Zhu et al. (2023). Previously, we defined the total number of vehicles within a mainline platoon as $n_p$ . In a mixed traffic scenario, this platoon comprises $n_C$ CAVs and $n_H$ HDVs, leading to the equation: 

$$
n _ {p} = n _ {C} + n _ {H} \tag {A1}
$$

Moreover, we consider the arrival sequence of vehicles in a platoon of length $n_p$ on the freeway mainline to be $\{X_1, X_2, X_3, \dots, X_{n_p}\}$ . In line with our prior assumptions, the lead vehicle in each platoon is necessarily a cooperative vehicle, and thus exclusively a CAV, 

making $X_{1}$ a CAV. The arrival of each subsequent vehicle after the head vehicle is treated as an independent event. The probability of any given vehicle being a CAV is denoted as $p$ , representing the CAV penetration rate. Consequently, the probability of forming a platoon with a CAV leading $(n_{C} = 1)$ and $n_{H}$ HDVs following is expressed as the probability function $p(n_{p})$ for a platoon length of $n_{p}$ . This results in the equation: 

$$
n _ {p} = 1 + n _ {H} \# \tag {A2}
$$

To model the vehicle arrival process, we approach it as an infinite Bernoulli process with a fixed probability of success $p$ , where 'success' equates to the arrival of a CAV, and 'failure' to the arrival of an HDV. In this model, $n_{H}$ (the number of HDVs) represents the count of failures preceding the first success (arrival of a CAV), conforming to a geometric distribution. The probability density function of this distribution is given by: 

$$
p \left(n _ {H}\right) = (1 - p) ^ {n _ {H} *} p, n _ {H} \in \{1, 2, 3 \dots \} \# \tag {A3}
$$

This probability $p(n_{H})$ is equivalent to the occurrence probability $p(n_{p})$ for a platoon of length $n_p$ . Figure A1 graphically presents the values of $p(n_p)$ across various CAV penetration rates. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/f49f2565-f0da-41ad-b00e-c352e96aa05e/40dbac2e7a4b4778c14549fba64983bc00221c76644a263e4bf81cb51faa1e1b.jpg)



Fig. A1. Results of the value of under different penetration rates.


According to Fig. 5, the occurrence of excessively long platoons is probable when the CAV penetration rate falls below $30\%$ . However, within the scope of penetration rates examined in this study ( $p$ ranging from $30\%$ to $100\%$ ), the formation of a platoon exceeding 10 vehicles in length becomes increasingly unlikely. Specifically, at a penetration rate of $30\%$ , the likelihood of encountering a 10-vehicle-long platoon is a mere $1.21\%$ . Consequently, this research does not take into account scenarios wherein a significant number of HDVs consecutively appear between two CAVs. 

# References



Ahmed, H.U., Huang, Y., Lu, P., 2021. A review of car-following models and modeling tools for human and autonomous-ready driving behaviors in micro-simulation. Smart Cities 4, 314-335. https://doi.org/10.3390/smartcities4010019. 





Ahn, K., Rakha, H., Trani, A., Van Aerde, M., 2002. Estimating vehicle fuel consumption and emissions based on instantaneous speed and acceleration levels. J. Transp. Eng. 128, 182-190. https://doi.org/10.1061/(ASCE)0733-947X(2002)128:2(182). 





Ahn, K., 1998. Microscopic fuel consumption and emission modeling. Ahn K. Microscopic fuel consumption and emission modeling. Virginia Tech, 1998. 





Barth, M., An, F., Younglove, T., Scora, G., Levine, C., Ross, M., Wenzel, T., 2000. The development of a comprehensive modal emissions model. NCHRP Web-Only Doc. 122, 11–25. 





Baskar, L.D., De Schutter, B., Hellendoorn, H., 2008. Dynamic speed limits and on-ramp metering for IVHS using model predictive control. In: 2008 11th International IEEE Conference on Intelligent Transportation Systems. IEEE, pp. 821-826. 





Chen, L.-W., Hu, T.-Y., 2023. Optimization of consecutive on-ramp control for urban freeways: An application of the store-and-forward approach. J. Transp. Eng. Part A Syst. 149, 4023004. 





Chen, T., Wang, M., Gong, S., Zhou, Y., Ran, B., 2021. Connected and automated vehicle distributed control for on-ramp merging scenario: A virtual rotation approach. Transp. Res. Part C Emerg. Technol. 133, 103451 https://doi.org/10.1016/j.trc.2021.103451. 





Chen, J., Zhou, Y., Chung, E., Ozbay, K., 2022. CAV-Based active congestion resolving for improving mainline traffic flow efficiency of a freeway on-ramp merging section. In: In: 2022 IEEE 25th International Conference on Intelligent Transportation Systems (ITSC). IEEE, pp. 216-223. 





Cheng, M., Zhang, C., Jin, H., Wang, Z., Yang, X., 2022. Adaptive coordinated variable speed limit between highway mainline and on-ramp with deep reinforcement learning. J. Adv. Transp. 2022. 





Cui, S., Cao, F., Yu, B., Yao, B., 2021. Modeling heterogeneous traffic mixing regular, connected, and connected-autonomous vehicles under connected environment. IEEE Trans. Intell. Transp. Syst. 23, 8579-8594. 





Di, Y., Zhang, W., Ding, H., Zheng, X., Bai, H., 2023. Integrated control for mixed CAV and CV traffic flow in expressway merge zones combined with variable speed limit, ramp metering, and lane changing. J. Transp. Eng. Part A Syst. 149, 4022140. 





Elefteriadou, L.A., 2016. The highway capacity manual 6th edition: A guide for multimodal mobility analysis. Ite journal. 86 (4). 





Fang, Y., Min, H., Wu, X., Wang, W., Zhao, X., Mao, G., 2022. On-ramp merging strategies of connected and automated vehicles considering communication delay. IEEE Trans. Intell. Transp. Syst. 23, 15298-15312. 





Fang, X., Péter, T., Tettamanti, T., 2023. Variable speed limit control for the motorway-urban merging bottlenecks using multi-agent reinforcement learning. Sustainability 15, 11464. 





Fildes, B.N., Rumbold, G., Leening, A., 1991. Speed behaviour and drivers' attitude to speeding. Monash University Accident Research Centre, Report, 1991, 16(186): 104-115. 





Formosa, N., Quddus, M., Ison, S., Abdel-Aty, M., Yuan, J., 2020. Predicting real-time traffic conflicts using deep learning. Accid. Anal. Prev. 136 https://doi.org/10.1016/j.aap.2019.105429. 





Fukuyama, S., 2020. Dynamic game-based approach for optimizing merging vehicle trajectories using time-expanded decision diagram. Transp. Res. Part C Emerg. Technol. 120, 102766. 





Gao, Y., Levinson, D., 2023. Lane changing and congestion are mutually reinforcing? Commun. Transp. Res. 3, 100101. 





Goatin, P., Gottlich, S., Kolb, O., 2016. Speed limit and ramp meter control for traffic flow networks. Eng. Optim. 48, 1121-1144. 





Han, Y., Ramezani, M., Hegyi, A., Yuan, Y., Hoogendoorn, S., 2020. Hierarchical ramp metering in freeways: An aggregated modeling and control approach. Transp. Res. Part C Emerg. Technol. 110, 1-19. 





Han, Y., Wang, M., He, Z., Li, Z., Wang, H., Liu, P., 2021. A linear Lagrangian model predictive controller of macro-and micro-variable speed limits to eliminate freeway jam waves. Transp. Res. Part C Emerg. Technol. 128, 103121. 





Han, Y., Hegyi, A., Zhang, L., He, Z., Chung, E., Liu, P., 2022a. A new reinforcement learning-based variable speed limit control approach to improve traffic efficiency against freeway jam waves. Transp. Res. Part C Emerg. Technol. 144, 103900. 





Han, Y., Wang, M., Li, L., Roncoli, C., Gao, J., Liu, P., 2022b. A physics-informed reinforcement learning-based strategy for local and coordinated ramp metering. Transp. Res. Part C Emerg. Technol. 137, 103584. 





Hegyi, A., De Schutter, B., Hellendoorn, H., 2005. Model predictive control for optimal coordination of ramp metering and variable speed limits. Transp. Res. Part C Emerg. Technol. 13, 185-209. 





Hegyi, A., Hoogendoorn, S.P., Schreuder, M., Stoelhorst, H., Viti, F., 2008. SPECIALIST: A dynamic speed limit control algorithm based on shock wave theory. In: 2008 11th International IEEE conference on intelligent transportation systems. IEEE, pp. 827-832. 





h h  t   a. 





Jing, S., Hui, F., Zhao, X., Rios-Torres, J., Khattak, A.J., 2019. Cooperative game approach to optimal merging sequence and on-ramp merging control of connected and automated vehicles. IEEE Trans. Intell. Transp. Syst. 20, 4234-4244. 





Karimi, M., Roncoli, C., Aleksandru, C., Papageorgiou, M., 2020. Cooperative merging control via trajectory optimization in mixed vehicular traffic. Transp. Res. Part C Emerg. Technol. 116, 102663 https://doi.org/10.1016/j.trc.2020.102663. 





Kherroubi, Z.e., Aknine, S., Bacha, R., 2022. Novel decision-making strategy for connected and autonomous vehicles in highway on-ramp merging. IEEE Trans. Intell. Transp. Syst. 23, 12490-12502. https://doi.org/10.1109/TITS.2021.3114983. 





Kontorinaki, M., Karafyllis, I., Papageorgiou, M., 2019. Local and coordinated ramp metering within the unifying framework of an adaptive control scheme. Transp. Res. Part A Policy Pract. 128, 89-113. 





Larsson, J., Keskin, M.F., Peng, B., Kulcsar, B., Wymeersch, H., 2021. Pro-social control of connected automated vehicles in mixed-autonomy multi-lane highway traffic. Commun. Transp. Res. 1, 100019. 





Li, L., Gan, J., Ji, X., Qu, X., Ran, B., 2020. Dynamic driving risk potential field model under the connected and automated vehicles environment and its application in car-following modeling. IEEE Trans. Intell. Transp. Syst. https://doi.org/10.1109/TITS.2020.3008284. 





Li, Z., Liu, P., Xu, C., Duan, H., Wang, W., 2017. Reinforcement learning-based variable speed limit control strategy to reduce traffic congestion at freeway recurrent bottlenecks. IEEE Trans. Intell. Transp. Syst. 18, 3204-3217. 





Li, L., Wang, F.-Y., 2006. Cooperative driving at blind crossings using intervehicle communication. IEEE Trans. Veh. Technol. 55, 1712-1724. 





Liao, X., Zhao, X., Wang, Z., Han, K., Tiwari, P., Barth, M.J., Wu, G., 2021. Game theory-based ramp merging for mixed traffic with unity-sumo co-simulation. IEEE Trans. Syst. Man Cybern. Syst. 52, 5746-5757. 





Liu, Z., Sun, D., Zhao, M., Huang, S., Wu, X., 2022. A freeway on-ramps BLVD-based virtual platoon control for mixed traffic: A cyber-physical perspective. In: 2022 IEEE 25th International Conference on Intelligent Transportation Systems (ITSC). IEEE, pp. 1516-1521. 





Liu, J., Zhao, W., Xu, C., 2021. An efficient on-ramp merging strategy for connected and automated vehicles in multi-lane traffic. IEEE Trans. Intell. Transp. Syst. 23, 5056-5067. 





Liu, H., Zhuang, W., Yin, G., Li, Z., Cao, D., 2023. Safety-critical and flexible cooperative on-ramp merging control of connected and automated vehicles in mixed traffic. IEEE Trans. Intell. Transp. Syst. 24, 2920-2934. 





Lu, X.-Y., Varaiya, P., Horowitz, R., Su, D., Shladover, S.E., 2010. A new approach for combined freeway variable speed limits and coordinated ramp metering. In: In: 13th International IEEE Conference on Intelligent Transportation Systems. IEEE, pp. 491-498. 





Lu, X.-Y., Varaiya, P., Horowitz, R., Su, D., Shladover, S.E., 2011. Novel freeway traffic control with variable speed limit and coordinated ramp metering. Transp. Res. Rec. 2229, 55-65. 





Luo, X., Li, X., Shaon, M., Zhang, Y., 2023. Multi-lane-merging strategy for connected automated vehicles on freeway ramps. Transp. B Transp. Dyn. 11, 127-145. 





Mahmud, S.M.S., Ferreira, L., Hoque, M.S., Tavassoli, A., 2017. Application of proximal surrogate indicators for safety evaluation: A review of recent developments and research needs. IATSS Res. 41, 153-163. https://doi.org/10.1016/j.iatssr.2017.02.001. 





Mohammadian, S., Zheng, Z., Haque, M.M., Bhaskar, A., 2023. Continuum modeling of freeway traffic flows: State-of-the-art, challenges and future directions in the era of connected and automated vehicles. Commun. Transp. Res. 3, 100107. 





Ntousakis, I.A., Nikolos, I.K., Papageorgiou, M., 2016. Optimal vehicle trajectory planning in the context of cooperative merging on highways. Transp. Res. Part C Emerg. Technol. 71, 464-488. 





Papamichail, I., Papageorgiou, M., 2008. Traffic-responsive linked ramp-metering control. IEEE Trans. Intell. Transp. Syst. 9, 111-121. 





Pooladsanj, M., Savla, K., Ioannou, P.A., 2023. Ramp metering to maximize freeway throughput under vehicle safety constraints. Transp. Res. Part C Emerg. Technol. 154, 104267. 





Rios-Torres, J., Malikopoulos, A.A., 2016. Automated and cooperative vehicle merging at highway on-ramps. IEEE Trans. Intell. Transp. Syst. 18, 780-789. 





SAE, 2018. Taxonomy and definitions for terms related to driving automation systems for on-road motor vehicles. SAE Int. 4970, 1-5. 





Scarinci, R., Heygi, A., Heydecker, B., 2017. Definition of a merging assistant strategy using intelligent vehicles. Transp. Res. Part C Emerg. Technol. 82, 161-179.  
Scarinci, R., Heydecker, B., 2014. Control concepts for facilitating motorway on-ramp merging using intelligent vehicles. Transp. Rev. 34, 775-797. 





Scarinci, R., Heydecker, B., Hegyi, A., 2015. Analysis of traffic performance of a merging assistant strategy using cooperative vehicles. IEEE Trans. Intell. Transp. Syst. 16, 2094-2103. 





Scholte, W.J., Zegelaar, P.W.A., Nijmeijer, H., 2022. A control strategy for merging a single vehicle into a platoon at highway on-ramps. Transp. Res. Part C Emerg. Technol. 136, 103511 https://doi.org/10.1016/j.trc.2021.103511. 





Shang, M., Wang, S., Stern, R.E., 2023. Extending ramp metering control to mixed autonomy traffic flow with varying degrees of automation. Transp. Res. Part C Emerg. Technol. 151, 104119. 





Shi, J., Li, K., Chen, C., Kong, W., Luo, Y., 2023. Cooperative merging strategy in mixed traffic based on optimal final-state phase diagram with flexible highway merging points. IEEE Trans. Intell. Transp Syst. 





Smaragdis, E., Papageorgiou, M., 2003. Series of new local ramp metering strategies: Emmanouil smaragdis and markos papageorgiou. Transp. Res. Rec. 1856, 74-86. 





Sun, Z., Huang, T., Zhang, P., 2020. Cooperative decision-making for mixed traffic: A ramp merging example. Transp. Res. Part C Emerg. Technol. 120, 102764. 





Tang, Z., Zhu, H., Zhang, X., Iryo-Asano, M., Nakamura, H., 2022. A novel hierarchical cooperative merging control model of connected and automated vehicles featuring flexible merging positions in system optimization. Transp. Res. Part C Emerg. Technol. 138, 103650. 





Treiber, M., Kesting, A., Treiber, M., Kesting, A., 2013. Car-following models based on driving strategies. Traffic Flow Dyn. Data, Model. Simul, 181-204. 





Wang, Y., Kosmatopoulos, E.B., Papageorgiou, M., Papamichail, I., 2014. Local ramp metering in the presence of a distant downstream bottleneck: Theoretical analysis and simulation study. IEEE Trans. Intell. Transp. Syst. 15, 2024-2039. 





Wang, S., Zhao, M., Sun, D., Liu, X., 2022. Merging sequence optimization based on reverse auction theory and merging strategy with active trajectory adjustment of heterogeneous vehicles. J. Adv. Transp. 2022. 





Wen, Y., Zhang, S., Zhang, J., Bao, S., Wu, X., Yang, D., Wu, Y., 2020. Mapping dynamic road emissions for a megacity by using open-access traffic congestion index data. Appl. Energy 260, 114357. 





Wijethilaka, S., Liyanage, M., 2021. Survey on network slicing for Internet of Things realization in 5G networks. IEEE Commun. Surv. Tutorials 23, 957-994. 





Xu, H., Feng, S., Zhang, Y., Li, L., 2019. A grouping-based cooperative driving strategy for CAVs merging problems. IEEE Trans. Veh. Technol. 68, 6125-6136. 





Xue, Y., Ding, C., Yu, B., Wang, W., 2022. A platoon-based hierarchical merging control for on-ramp vehicles under connected environment. IEEE Trans. Intell. Transp. Syst. 23, 21821-21832. 





Yang, X., Zou, Y., Chen, L., 2022. Operation analysis of freeway mixed traffic flow based on catch-up coordination platoon. Accid. Anal. Prev. 175, 106780. 





Yao, Z., Gu, Q., Jiang, Y., Ran, B., 2022. Fundamental diagram and stability of mixed traffic flow considering platoon size and intensity of connected automated vehicles. Phys. A Stat. Mech. Its Appl. 604, 127857. 





Yue, L., Abdel-Aty, M., Wang, Z., 2022. Effects of connected and autonomous vehicle merging behavior on mainline human-driven vehicle. J. Intell. Connect. Veh. 5, 36-45. 





Zhang, S., Wu, Y., Liu, H., Huang, R., Un, P., Zhou, Y., Fu, L., Hao, J., 2014. Real-world fuel consumption and CO2 (carbon dioxide) emissions by driving conditions for light-duty passenger vehicles in China. Energy 69, 247-257. https://doi.org/10.1016/j.energy.2014.02.103. 





Zhang, L., Yan, L., Fang, Y., Fang, X., Huang, X., 2019. A machine learning-based defensive alerting system against reckless driving in vehicular networks. IEEE Trans. Veh. Technol. 68, 12227-12238. 





Zhou, Y., Chalette, M.E., Bhaskar, A., Chung, E., 2018. Optimal vehicle trajectory planning with control constraints and recursive implementation for automated on-ramp merging. IEEE Trans. Intell. Transp. Syst. 20, 3409-3420. 





Zhou, Y., Ahn, S., Wang, M., Hoogendoorn, S., 2019. Stabilizing mixed vehicular platoons with connected automated vehicles: An H-infinity approach. Transp. Res. Part B Methodol. 132, 152-170. https://doi.org/10.1016/j.trb.2019.06.005. 





Zhu, J., Tasic, I., Qu, X., 2021. Improving freeway merging efficiency via flow-level coordination of connected and autonomous vehicles. IEEE Trans. Intell. Transp. Syst. 2024. 





Zhu, J., Easa, S., Gao, K., 2022a. Merging control strategies of connected and autonomous vehicles at freeway on-ramps: a comprehensive review. J. Intell. Connect. Veh. 5, 99-111. 





Zhu, J., Tasic, I., Qu, X., 2022b. Flow-level coordination of connected and autonomous vehicles in multilane freeway ramp merging areas. Multimodal Transp. 1, 100005 https://doi.org/10.1016/j.multra.2022.100005. 





Zhu, J., Gao, K., Li, H., He, Z., Monreal, C.O., 2023. Bi-level ramp merging coordination for dense mixed traffic conditions. Fundamental Research. 

