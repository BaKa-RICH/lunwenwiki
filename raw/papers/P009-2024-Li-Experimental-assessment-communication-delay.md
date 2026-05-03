Full Length Article 

# Experimental assessment of communication delay's impact on connected automated vehicle speed volatility and energy consumption

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/96d3fedcdb85d29e882f9f7157fdbc69d7ef15573c24b4c09a478bb1e981806b.jpg)


Wan Li a , Jackeline Rios-Torres a , Boyu Wang b , Zulqarnain H. Khattak c,* 

a Buildings and Transportation Science Division, Oak Ridge National Laboratory, Oak Ridge, 37831, USA 

b School of Electrical and Information Engineering, Beijing University of Civil Engineering and Architecture, Beijing, 102627, China 

c Civil and Environmental Engineering, Carnegie Mellon University (CMU), Pittsburgh, 15213, USA 

# A R T I C L E I N F O

# Keywords:

Communication delay 

Connected and autonomous vehicles (CAVs) 

Merging control 

Field experimental data 

Vehicle-in-the-loop testing 

# A B S T R A C T

Communication delays within connected and autonomous vehicles (CAVs) pose significant risks. It is imperative to address these issues to ensure the safe and effective operation of CAVs. However, the exploration of communication delays on CAV operations and their energy use remains sparse in the literature. To fill the research gap, this study leverages the facilities at America Center of Mobility (ACM) Smart City Test Center to implement and evaluate a CAV merging control algorithm through vehicle-in-the-loop testing. This study aims at achieving three main objectives: (1) develop and implement a CAV merging control strategy in the experimental test bed through vehicle-in-the-loop testing, (2) propose analytical models to quantify the impacts of communication delay on the variability of CAV speed and energy consumption based on field experiment data, and (3) create a predictive model for energy usage considering various CAV attributes and dynamics, e.g., speed, acceleration, yaw rate, and communication delays. To our knowledge, this is one of the first attempts at evaluating the impacts of communication delays on CAV merging operational control with field data, making critical advancement in the field. The results suggest that communication delay has a more substantial effect on energy consumption under high-speed volatility compared to low-speed volatility. Among all factors examined, acceleration is the dominant characteristic that influences energy usage. It also revealed that even minor improvements in communication delay can yield tangible improvements in energy efficiency. The results provide guidance on CAV field experiments and the influence of communication delays on CAV operation and energy consumption. 

# 1. Introduction

The on-ramp merging areas on freeways are one of the main causes for traffic congestions, energy inefficiency, and traffic accidents. The merging vehicles may interrupt the mainline traffic flows with improper driving behaviors, leading to speed instability, capacity reduction, and high fuel consumption. Connected and autonomous vehicle (CAV) technology with its real-time Vehicle-to-Everything (V2X) communication capability brings potential to transform the conventional merging operation of human drivers (Ali et al., 2021; Gu et al., 2022; Guo et al., 2020; Mohammadian et al., 2023; Zhou et al., 2016). The advanced merging control strategies of CAVs aims to optimize the merging process considering various factors, e.g., commutation between CAVs, road traffic conditions, and vehicle dynamics to improve traffic mobility, safety, and energy efficiency by regulating the individual CAV's trajectories. Numerous studies have been devoted to the development and 

testing of CAV merging control strategies (Di et al., 2023; Larsson et al., 2021; Li et al., 2023; Liu et al., 2023; Tang et al., 2022; Xiao and Cassandras, 2021; Xiong et al., 2022; Zhu et al., 2022). However, most of them have been tested in simulated environments, significantly limiting their ability to gather authentic field implementation data and comprehensively evaluate the robustness of CAV operations and energy usage to communication delays. Furthermore, most of the simulation-based evaluation of CAVs considers perfect communication with no delays (Branzi et al., 2021; Ge et al., 2022; Yan et al., 2020). One significant innovation of this study is to utilize the American Center of Mobility (ACM) test facilities to perform vehicle-in-the-loop testing for the proposed CAV merging control algorithm. The field data serve as a foundation for validating our model and further examining various operational dynamics of the CAV. 

The reliable and low-latency communication system plays an important role in supporting various CAV applications (Olovsson et al., 

2022). Communication delay in CAVs can have significant impacts on safety and efficient operations for both individual CAVs in a mixed traffic environment and the general traffic network (American Center of Mobility, 2024; Mcity, 2023; Khattak et al., 2023). For an individual CAV, a delay in commutation can lead to the CAV receiving outdated messages and making less optimal or incorrect driving decisions, leading to inefficient driving operations or even potential accidents. Communication delays can also impact the energy efficiency as the CAVs may need to slow down or stop timely information is not received. For an overall traffic network, communication delay can also cause information interpretation issues, e.g., it is difficult to exchange and use information between different CAVs, and between CAVs and infrastructure (Khattak et al., 2020, 2022). As a result, communication delay is a critical variable influencing CAV operations. This study is particularly focused on the exploration of the effects of communication delay on CAV driving behaviors and their energy usage patterns using field data. 

Recognizing the critical issue of communication delay, this study aims to conduct an in-depth examination of the overlooked impacts on CAV dynamics and energy efficiency. Using the state-of-the-art facilities at ACM Smart City Test Center, along with its sophisticated digital twin, we have implemented and evaluated a CAV merging control algorithm through vehicle-in-the-loop experiment. Specifically, we developed a Hybrid Long Short-Term Memory (H-LSTM) model to examine and predict energy consumption by capturing complex quantitative relationships among various vehicle characteristics. These features include speed, acceleration, yaw rate, communication delays, speed volatility, and energy consumption. Our model uniquely addresses the temporal dependencies inherent in the CAVs operational data. Unlike traditional models, the H-LSTM framework effectively captures the high correlations between preceding and succeeding data points in time series data, which significantly impact energy consumption. Using the advanced capabilities of LSTM networks, our model not only estimates speed variability and energy consumption with high precision, but also provides a comprehensive understanding of how temporal dependencies influence these aspects. 

This study has several noteworthy contributions. 

 This study successively implemented a CAV merging control strategy in real world settings. The implementation generated valuable field experimental data, offering unique opportunities for subsequent evaluations and analysis. 

 This study introduced a novel approach for estimating and validating communication delays, leveraging field experimental data. This approach represents a significant advancement in accurately assessing real-world communication latency, facilitating improved design and deployment strategies for CAV applications. 

 This study developed a predictive model that not only precisely estimates speed variability and energy consumption but also uniquely captures the temporal dependencies of CAV operational data, which is a critical aspect previously overlooked in the literature. 

# 2. Literature review

Research on merging control for CAVs is an active area of study. The strategy will depend on many factors, e.g., the level of autonomy of the vehicles, the availability of communication, the traffic management systems, level of penetration of CAVs, and the regulations and standards in place. There are various CAV merging control strategies. Zhu et al. (2022) provided a comprehensive review of merging control strategies for merging CAVs at freeway on-ramps, including ram petering, variable speed limits, cooperative merging, platooning, and reservation-based merging. The paper also highlighted the importance of Vehicle-to-Infrastructure (V2I) communication in supporting effective merging. Li et al. (2023) proposed a communication-based soft actor-critic algorithm to enhance the cooperation of merging CAVs in heavy traffic. The algorithm included a local module and a global module. The local module 

aimed to control individual vehicle while global module facilitated communication and cooperation among vehicles. Xiong et al. (2022) proposed a merging control method that considered the uncertainty of human driving when a CAV merged to a lane with human-driven vehicle. The method involved two stages. First, the CAV predicted the trajectories of the surrounding vehicles in the human-driven lane and chooses an optimal gap to merge. Second, the CAV adjusted its speed and position to match the optimal gap to minimize the risk of collision. Di et al. (2023) proposed a predictive control strategy integrating variable speed limits, ramp metering, and lane changing to optimize traffic flow and reduce traffic congestion. The system considered the differences on driving behaviors between cAVs and connected vehicles (CVs) to optimize overall traffic flow. Xiao and Cassandras (2021) developed a decentralized merging control strategy for CAVs that ensures safe merging maneuvers. The proposed strategy utilized a model predictive control (MPC) approach that considered the kinematic constraints of CAVs as well as the minimum distance between CAVs to avoid collision. Tang et al. (2022) developed a hierarchical cooperative merging control model for CAVs that enabled flexible merging positions. The proposed model contained two layers. The upper layer coordinated merging process with a system-level multi-objective optimization algorithm, while the lower layers controlled individual CAV to implement merging command using a model predictive control approach. 

Most literature on CAV merging control, including the studies discussed in this section, used microscopic simulator, e.g., VISSIM or SUMO, to test the performance of the algorithms. However, traffic simulation has its limitations. First, it is simplified models that are based on simplified assumptions about driver behaviors, vehicle dynamics, and road conditions. Simulation models assume perfect communication with no delays. These assumptions cannot reflect the complexity and variability of realworld traffic situations, leading to inaccurate estimations of traffic conditions and incomplete information. Second, simulation has limited flexibility. It is designed to simulate specific scenarios and may not be easily adapted to changes in the traffic environment. Field tests of CAV maneuvers, on the other hand, is a promising step to advance the technology and ensure its integration into the transportation system. It typically involves a range of merging scenarios, including different traffic densities, varied penetration levels of CAVs, and speeds. Most importantly, real-world data, including controlled CAV data (speed, position, acceleration, vehicle dynamic data), traffic environment data (surrounding vehicles), and communication performance data (communication delay), can be collected from the field tests. They provide a valuable opportunity to evaluate the real-world performance of CAVs and collect data on the effectiveness, safety, and user experience. 

Unlike simulation platforms, real-world testbed for CAV operation has many advantages. These test sites provide an environment to evaluate the performance and effectiveness of different control strategies for CAVs. There are several testing facilities around the world that are famous for the research in CAVs. For example, Mcity is a 32-acre testing facility in Michigan, USA that simulates real-world urban and suburban driving scenarios (Mcity, 2023). Its test track includes a variety of road types, e.g., roundabouts, tunnels, and pedestrian crossings, to create a diverse testing environment. Mcity also has a range of sensors and equipment installed to collect data on CAV performance, e.g., cameras, LiDAR, and GPS system. The ACM Smart City Test Center is a testing and product development facility for CAV, also located in Michigan, USA (American Center of Mobility, 2024). The facility includes a range of communication infrastructure to support the testing of CAVS. Singapore Autonomous Vehicle Initiative (SAVI) is a research program aiming at developing fully autonomous vehicle capable of navigating complex urban environments (Quek, 2017). The initiative supports the development and deployment of autonomous vehicles in Singapore, including establishment of regulatory framework and construction of a test facility for CAVs called CENRAN. 

Communication delays significantly influence CAV applications, impacting their driving behavior and traffic flow dynamics. As previously 

discussed, the scarcity of field experiment data limits in-depth studies on the various aspects of communication delays. Khattak et al. (2023) examined the effects of communications delays on the safety and stability of CAV platoons employing real-world data on a five-vehicle platoon. The research employed switching regime models to assess the behavior of the lead vehicle and following vehicles under various scenarios. Findings indicated that cooperative adaptive cruise control (CACC) systems mitigate volatility more effectively than adaptive cruise control (ACC) systems due to enhanced vehicular communication and synchronization although delays were shown to increase volatility and instability, particularly among following vehicles. Fang et al. (2022) delved into the effects of V2I communication delay on CAV on-ramp merging utilizing statistical analysis and real-world data to estimate communication delays. By incorporating these delays into an optimal control model for on-ramp merging, the study assessed the impact on vehicle control laws and overall merging safety. The findings highlighted that V2I communication delays, characterized by a probability density function that varies across scenarios, could degrade the dynamic performance of control processes, potentially leading to increased risks of lateral collisions in merging areas. An and Jung (2018) introduced a cooperative lane change protocol that addresses V2V communication delays during path planning for lane changing behaviors. Vehicles were modeled as oriented bounding boxes (OBBs) to evaluate collision risks. The protocol's effectiveness was tested in a simulated highway environment with integrated longitudinal and lateral control systems, demonstrating its capability to mitigate the impact of communication delays on lane changing. Fang et al. (2022) and An and Jung (2018) developed models for merging and lane changing that took into account the impact of communication delays. These models were tested within a simulation environment to assess their model and performance. However, the comprehensive effects of delays across different scenarios remained underexplored and insufficiently validated. This gap highlights a need for further research to fully understand the implications of communication delays on traffic dynamics and safety measures. In a parallel study, Khattak et al. (2023) examined the influence of communication delays on the stability and safety of vehicle platoons. Despite the insightful findings, this model did not account for the temporal dependencies inherent in the CAV data. This omission suggests a potential area for improvement in modeling approaches, where incorporating temporal dynamics could lead to a more accurate understanding of communication delays' impacts on platoon behavior. 

From the literature, there are many studies focused on CAV merging control strategy development while limited work has been done to evaluate the CAV performance based on field experimental data. To fill the research gap, this study applied different analytical models including H-LSTM to examine the performance of CAVs with field data. Particularly, this study aims to identify the impact of communication delay on 

CAV speed volatility and its energy consumption. 

# 3. Field experiment

This section presents the experimental framework, including the algorithm and test bed utilized for the field experiment on CAV merging control, which is significant in generating real-world data for further analysis and evaluation. We first introduce the CAV merging control algorithm for implementation and testing. Then a detailed description of the ACM test center and its digital twin is provided, which serves as an essential component in vehicle-in-the-loop testing. Lastly, we describe experiment setup, emphasizing the testing scenarios. 

# 3.1. Optimal merging control algorithm

This study applied our previous work of optimal merging control algorithm (Rios-Torres et al., 2021; Rios-Torres and Malikopoulos, 2016) to coordinate the vehicles driving inside the predefined control zone, as shown in Fig. 1. The goal is to minimize the acceleration and fuel consumption of each vehicle in the control zone, e.g., the dynamics of 5 vehicles in control zone in Fig. 1 was optimized and synchronized before merging zone. 

The closed-loop optimal merging controller includes two stages: (1) calculation of the desired arrival time at the merging zone to avoid collision and (2) solving the optimal merging control problem. In Fig. 2, the centralized coordinator will broadcast each vehicle i's desired final position $x _ { f i s }$ speed $\nu _ { f i } ,$ and desired arrival time at the merging zone $t _ { f i }$ to all vehicles within the control zone. These desired values are calculated with Eqs. (3)–(8). Then the controller updates the optimization constants and solve optimal control problem based on the information shared by the centralized coordinator. 

To calculate the arrival time at the merging zone of vehicle $i , t _ { f i } ,$ we need to look at if there is a proceeding vehicle in front of the host vehicle. If there is no proceeding vehicle, the $t _ { f i }$ is computed as 

$$
t _ {f i} = t _ {c i} + L / v _ {f i} \tag {1}
$$

where $t _ { c i }$ is the time at which vehicle i reaches the control zone, $L$ is the length of the control zone, and $\nu _ { f i }$ is the speed the vehicle should follow at the time it reaches the merging zone. 

If there is preceding vehicle, 

$$
t _ {f i} = t _ {f, i - 1} + \rho \tag {2}
$$

where $t _ { f , i - 1 }$ is the time to reach the merging zone for the preceding vehicle vehicle $i - 1$ and $\rho$ is the desired headway that can be defined according to the vehicle type. 

We briefly discuss the optimal merging control problem; more details 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/4a3a7e61bcc5a39ea685d01feb6d28806acf557ee0637fc5d84b29491a102719.jpg)



Fig. 1. Merging control scenario.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/2b1288f78243b3843e3dd76c011b942ccfa85fae06d2fd48749e9c4c6da290d2.jpg)



Fig. 2. Closed-loop optimal merging controller.


of the model and its solution refer to Rios-Torres et al. (2021) and Rios-Torres and Malikopoulos (2016). Each vehicle is modeled by a second order dynamics in Eqs. (3) and (4): 

$$
\dot {x} _ {i} = v _ {i} (t) \tag {3}
$$

$$
\dot {v} _ {i} = u _ {i} (t) \tag {4}
$$

where $x _ { i } , \nu _ { i } ,$ and $u _ { i }$ denote vehicle position, speed, and acceleration rate of vehicle i, respectively. The objective is to minimize the $L _ { 2 }$ norm of acceleration in Eq. (5). According to Rios-torres et al. (2021), fuel consumption exhibits a monotonic relationship with acceleration. Generally, reducing acceleration minimizes transient engine operations, directly benefiting fuel efficiency. This is because internal combustion engines are optimized for steady-state operating conditions. 

$$
\min  \int_ {t _ {0 i}} ^ {t _ {f i}} u _ {i} ^ {2} \mathrm {d} t \tag {5}
$$

where $t _ { 0 i }$ is the current time and $t _ { f i }$ is the arrival time at merging zone. 

The Hamiltonian analysis (Pontryagin, 2018) is applied to find optimal control input $( u _ { i } )$ and states $( x _ { i }$ and vi) for each vehicle using Eqs. (6)–(8): 

$$
u _ {i} ^ {*} = a _ {i} t + b _ {i} \tag {6}
$$

$$
v _ {i} ^ {*} (t) = \frac {1}{2} a _ {i} t ^ {2} + b _ {i} t + c _ {i} \tag {7}
$$

$$
x _ {i} ^ {*} (t) = \frac {1}{3} a _ {i} t ^ {3} + \frac {1}{2} b _ {i} t ^ {2} + c _ {i} t + d _ {i} \tag {8}
$$

# 3.2. ACM test track and vehicle-in-the-loop testing

A CAV was tested on the America Center of Mobility (ACM) test track with the layout of 500-acre site using Drive-by-Wire and Dedicated Short Range Communication (DSRC), as shown in Fig. 3. The track consists of a highway loop with arterials and ramps that replicate real-world infrastructure and provide driving scenarios that involve highway speeds, interactions with other vehicles at interchanges, navigating a highvolume and high-speed intersection, and driving in re-configurable open pavement areas (Buller et al., 2023). The ACM infrastructure can measure and collect information of vehicles to quantify the CAV performance on cooperative driving, merging, and lane changing in realistic scenarios. 

As shown in Fig. 3, we used four different locations at the ACM for CAV merging control testing which were named as Minor Lane A, Major Lane A, Minor Lane B, and Major Lane B. The merge zones are 100 m long and the control zones are $4 0 0 \ \mathrm { m }$ long. 

A digital twin of the ACM test track was developed in traffic simulator VISSIM. It creates a mixed reality test to evaluate complex traffic scenarios without the need of a full fleet of real vehicles. The field experiment can test virtual vehicles on digital twin and real vehicles on the test site. Virtual and real vehicles can communicate through the roadside units. The real vehicle can receive messages from both virtual vehicles and the infrastructure. Simultaneously, real vehicles can broadcast 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/4b4bd758af5fbdd0abc293297b41ede397dd4492904163520da23878da5dd9a0.jpg)



Fig. 3. Field test site at ACM.


information to digital twin, allowing virtual vehicle to interact with real vehicles. With this capability, it becomes possible to test algorithms in traffic that is congested, without incurring the expenses and risks associated with field tests involving real cars. 

Based on the digital twin, this study further developed a platform integrating VISSIM simulation, on-track real CAV test, and Connected Autonomous Electric Vehicle (CAEV) control algorithm in Fig. 4. The optimal merging commands generated from CAV control algorithms were communicated to the real CAV through Basic Safety Messages (BSM) via a Robot Operating System (ROS). The real CAV controlled its speed and acceleration based on the optimal command generated from Section 3.1, but it was constrained by the virtual leading vehicle in simulation. In simulation environments, the virtual CAV (red vehicle in Fig. 4) updated its speed and location based on real vehicles. The system is demonstrated to support closed-loop operation and control of CAVs in real-time and it also incorporates a protocol for centralized traffic management. 

# 3.3. Experiment setup

There are two merging scenarios developed in simulation environment. They are applied based on two most common sources of traffic jams: (1) Slow Merging Traffic: In this scenario, the minor lane traffic is initially much slower than the major lane traffic. We anticipate that this could cause traffic congestion (as vehicles on the major lane slow down) or energy inefficiency (as vehicles on the minor lane must speed up quickly). (2) High Traffic Density: In the scenario, the major lane is congested and merging cars will have to fight their way into the lane. Table 1 shows the details of the scenarios. 

The field experiments were conducted over four days, beginning from May 31, 2022 to June 3, 2022, during which a total of 21 test runs were successfully completed. A real CAV is equipped to receive real-time information and perceive the surrounding traffic which were simulated within VISSIM. The behavior of the controlled CAV is governed by the optimal merging control algorithm proposed in Section 3.1. 


Table 1 Details of merging scenarios in simulation.


<table><tr><td rowspan="2"></td><td colspan="2">Slow merging traffic</td><td colspan="2">High traffic density</td></tr><tr><td>Major lane</td><td>Minor lane</td><td>Major lane</td><td>Minor lane</td></tr><tr><td>Entry speed</td><td>20 m/s</td><td>10, 15 m/s</td><td>20 m/s</td><td>20 m/s</td></tr><tr><td>No. of cars</td><td>6</td><td>6</td><td>10</td><td>4</td></tr><tr><td>Following time</td><td>3 s</td><td>3 s</td><td>1 s</td><td>3 s</td></tr></table>

# 4. Methodology

This section illustrates methods for estimating communication delay, measuring speed volatility, and quantifying impacts of communication delay on speed volatility and energy consumption with field experimental data. 

# 4.1. Communication delays

Based on the literature, the communication delay is characterized as the time interval between the transmission of a message by the central controller and the reception of that identical message by the vehicle (Buller et al., 2023). To quantify communication delay, it is necessary to identify pairs of transmission and reception data points. However, extracting those pairs from field-experiment data is challenging. The time latencies between the central controller and the vehicle are not synchronous. For example, the central controller may operate on a 0.1-s interval while the vehicle updates its stats every 0.5–1.0 s interval. This difference makes it difficult to get accurate communication data. To overcome this challenge, an approximation method has been developed, as shown in Algorithm 1. When pairing the data points in the data set of transmission (from controller to vehicle) and receiving (vehicle to controller) messages, an additional constraint on speed (check speed difference) is required because there might be missing data due to the different time latency. Specifically, two data points, i and $j ,$ are paired when the difference between their corresponding time step, $t _ { i }$ and $t _ { j } ,$ is less than the threshold value $\epsilon _ { t }$ and the difference between their recorded speed, $\nu _ { i }$ and $\nu _ { j } ,$ , is less than the threshold value $\epsilon _ { \nu } .$ . 

Algorithm 1 Estimation method of communication delay while transmission message $i\in I$ and receiving message $j\in J$ do if $0 < t_{i} - t_{j} < = \epsilon_{t}$ and $|v_{i} - v_{j}| < = \epsilon_{v}$ then Pair the transmission message $i$ and the receiving message $j$ Delay $d_{i} = t_{i} - t_{j}$ end if end while 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/c688d55362a5d2c10c616ef6ca983696a4e4e309e3a0834cc05b199cbccfef2a.jpg)



Fig. 4. Framework of field experiment: Illustration on how control algorithm, simulation environment, and on-track field experiment are connected together.


To validate the communication delay, it is essential to conduct a series of empirical tests where real-world communication delay measurements are taken and compared to the estimates provided by Algorithm 1. The parameter $\epsilon _ { \nu }$ and $\epsilon _ { t }$ are crucial as they determine the sensitivity of the estimation. During the validation process, it is necessary to record the timestamps of the transmission and receiving messages and apply the algorithm to compute the estimated delays. For each pairing of messages, the estimated delay should fall within the real-world delay range. Adjusting $\epsilon _ { \nu }$ and $\epsilon _ { t }$ iteratively to fine-tune the algorithm's performance, as shown in Algorithm 2. A smaller value may provide a more precise pairing of messages, but might miss some valid data, leading to a sparser estimation. Conversely, a larger value may include more pairings but could introduce noise, reducing the accuracy of the delay estimation. Ultimately, the algorithm's validation lies in its ability to consistently produce delay estimates that fall within the real-world range of 0.01–0.10 s. The optimal value balances the trade-off between precision and recall of delay estimations, ensuring that the algorithm is accurate and robust. 

(2023) and Buller et al. (2023), the average communication delay should fall within [0.01 s, 0.05 s]. The closest value from our calculations is 0.06 s, corresponding to $\epsilon _ { \nu } = 0 . 1$ and $\epsilon _ { t } = 0 . 1$ . 

Fig. 6 compares the speeds from the outgoing transmission message and incoming receiving message of the real CAV in the test. The two curves appear closely aligned. The slight deviations between the two attributed to the communication delays. Based on field data, the average communication delay is 0.06 s and standard deviation is 0.01 s. 

# 4.2. Speed volatility

Based on field experiment data, we consider several metrics to quantify the speed volatility of the CAV. Speed stability is crucial to smooth traffic flow, reducing bottlenecks and prevent traffic incidents. High speed volatility is always involving a pattern of acceleration and deceleration, which is less energy efficient than maintaining a steady speed. Hence, it is significant to examine the speed volatility for CAV under merging control. Bollinger bands algorithm is one the most widely used method to evaluate speed volatility. According to Lento et al. 

Algorithm 2 Validation method of communication delay 

Require: List of candidate values of $\epsilon _ { v }$ $L _ { \epsilon _ { v } }$ and List of candidate values of 

$$
\epsilon_ {t}, L _ {\epsilon_ {t}}
$$

for $\epsilon _ { v }$ in $L _ { \epsilon _ { v } }$ do 

for $\epsilon _ { t }$ in $L _ { \epsilon _ { t } }$ do 

Implement Algorithm 1 

Record the average communication delay 

end for 

Select the optimal $\epsilon _ { v }$ and $\epsilon _ { t }$ when the corresponding average commutation 

delay is closest to the real-world value. 

Algorithms 1 and 2 were implemented to estimate and validate the communication delay. Specifically, we selected candidate values for $\epsilon _ { \nu }$ in the range [0.1, 0.5] and $\epsilon _ { t }$ in the range [0.1, 0.5]. The average value of communication delay under each combination of $\epsilon _ { \nu }$ and $\epsilon _ { t }$ is shown in Fig. 5. As threshold values for both $\epsilon _ { \nu }$ and $\epsilon _ { t }$ increase, the resulting communication delay also increases. According to the Khattak et al. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/e15d24df5c89a5d688f268e87753ae9f3c5ba479a2da181986830d58e4ee053d.jpg)



Fig. 5. Average communication delay under different values of $\epsilon _ { t }$ and $\epsilon _ { \nu }$


(2007), Bollinger bands involve calculating the moving average of a chosen metric (such as speed or acceleration) and using it as a reference point for assessing volatility relative to the average value over time. The bands are determined by establishing standard deviations above and below the moving average, with wider bands and larger standard deviations indicating higher volatility. The upper and lower bands are determined by setting two standard deviations above and below the moving average value, as shown in Eqs. (9) and (10): 

$$
B B _ {u} = M A + 2 \sqrt {\frac {\left(x _ {i} - M A\right) ^ {2}}{n}} \tag {9}
$$

$$
B B _ {l} = M A - 2 \sqrt {\frac {\left(x _ {i} - M A\right) ^ {2}}{n}} \tag {10}
$$

$$
M A = \sum_ {i = 1} ^ {n} \frac {x _ {i}}{n} \tag {11}
$$

In Eq. (11), $x$ represents either the instantaneous speed or acceleration, while n denotes the total number of observations. Moving average (MA) was calculated for each interval within each time series. Specifically, the moving average was computed for the first interval, e.g., 5 s (1–5 s) of the series, followed by the next 5 s (2–6 s), until the moving average was determined for the entire time series of a given clip. This process was repeated for each time series of each event, enabling the utilization of time series with varying levels of volatility. The resulting moving averages were employed to estimate the upper and lower bands $B B _ { u }$ and BBl) for the Bollinger Bands. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/1bfab465d443f90eb98079c85366322c092eb3ca3b991fe0b047a1f19256094b.jpg)



Fig. 6. Speed profile of incoming and outgoing messages.


# 4.3. Hybrid long short-term memory (H-LSTM) model for energy prediction

To examine the potential quantitative relationships among vehicle features, including communication delays, speed volatility, and energy consumption, this study develops a H-LSTM model for energy consumption prediction. The proposed Hybrid LSTM model incorporates linear and nonlinear parts, as shown in Eq. (12): 

$$
y (k + 1) = \beta_ {s} v (k) + \beta_ {d} d (k) + \beta_ {a} a (k) + \beta_ {y r} y r (k) + f (v (k - h) \dots v (k - 1), \tag {12}
$$

$$
d (k - h) \dots d (k - 1), a (k - h) \dots a (l - 1), y r (k - 1) \dots y r (k - 1))
$$

The H-LSTM model is achieved by minimizing the loss function $J$ in Eq. (13) using gradient approach. The factor of 1/2 is often included for convenience in the differentiation process when applying gradient descent, as it cancels out the coefficient when the derivative is taken. The goal of minimizing the loss function $J$ is to reduce the difference between the predicted and actual values, thereby improving the accuracy of the model. 

$$
\min  J = \frac {1}{2} (\hat {y} (k + 1) - y (k + 1)) ^ {2} \tag {13}
$$

$$
\hat {y} (k + 1) = \beta_ {s} v (k) + \beta_ {d} d (k) + \beta_ {a} a (k) + \beta_ {y r} y r (k) + \hat {f} (v (k - h) \dots v (k - 1), d (k - h) \dots d (k - 1), a (k - h) \dots a (l - 1), y r (k - h) \dots y r (k - 1); \pi) \tag {14}
$$

where $y ( k )$ denotes speed volatility and energy consumption at time step k. The input features include vehicle speed $\nu ( k )$ , communication delay $d ( k )$ , vehicle acceleration $a ( k )$ , and yaw rate $y r ( k )$ at time k. As per expert knowledge, these four variables play a significant role in determining the speed volatility and energy consumption. As a result, this study models these variables using linear function with corresponding parameters: $\beta _ { s } ,$ βd, $\beta _ { a } ,$ and $\beta _ { y r }$ . Since the features at previous time steps from $k - h$ up to $k - 1$ (historical sequence) could also be important, the nonlinear function $f$ is applied to using Long Short-term Memory (LSTM) model. LSTM networks are particularly well-suited for exploring the temporal dependencies of time-series data due to their ability to maintain and update information over extended sequences. This capability is crucial for CAV trajectory data, where the relationships between past, present, and future vehicle states significantly influence overall performance and energy consumption. LSTM effectively captures these dependencies by using specialized gating mechanisms that regulate the flow of information, allowing them to retain relevant historical data while discarding irrelevant details. This makes LSTM networks ideal for modeling the sequential and highly correlated nature of CAV trajectory data, enabling more accurate predictions and deeper insights into the factors affecting vehicle dynamics. If the features mentioned above are not significant, the corresponding neural network weights would be automatically adjusted to zero. This approach allows the model to separately and effectively analyze the complex, linear and nonlinear patterns in the field data, while assessing the impact of various factors simultaneously, thus providing an understanding of their contributions to energy usage. It is noted that the hybrid time series deep learning model has been successfully validated with traffic data before in Subramaniyan et al. (2023). 

where $\beta _ { s } , \beta _ { d } , \beta _ { a } , \beta _ { y r } ,$ and $\pi$ are parameters to be trained. $\pi$ groups all neural network weights and bias. 

LSTM takes $x _ { t }$ as input in Eqs. (15)–(17). In our case, the input $x _ { t }$ is the time series energy consumption and speed volatility $y ( k )$ . The memory cell state $C _ { t }$ is the central component of the LSTM. It holds essential information for predicting speed volatility and energy consumption in the next time step. The memory cell state is regulated by three gates: the forget gate, the update gate, and the output gate, which either remove or incorporate information into it. These gates are defined as $f _ { t s } \ i _ { t } ,$ and $o _ { t }$ respectively. Equations (15)–(17) show the functions to estimate the three gates: 

$$
f _ {t} = \sigma \left(W _ {f} x _ {t} + U _ {f} h _ {t - 1} + b _ {f}\right) \tag {15}
$$

$$
i _ {t} = \sigma \left(W _ {i} x _ {t} + U _ {i} h _ {t - 1} + b _ {i}\right) \tag {16}
$$

$$
o _ {t} = \sigma \left(W _ {o} x _ {t} + U _ {o} h _ {t - 1} + b _ {o}\right) \tag {17}
$$

where $W _ { f } , U _ { f } , b _ { f } , W _ { i } , U _ { i } , b _ { i } , W _ { o } , U _ { o } ,$ $U _ { o } ,$ and $b _ { o }$ are parameters that need to be learned. Parameters Wa, a  f, i, o and $U _ { a } ,$ $a \in f , i ,$ o regulate three gates corresponding to the current input cell state $x _ { t }$ and the previous hidden cell state $h _ { ( t - 1 ) }$ . Specifically, the sigmoid function $\sigma$ is utilized to determine the output values of the gates $f _ { t } , ~ i _ { t } ,$ and $o _ { t }$ which are vectors of values between 0 and 1. These gates serve as variables to dictate which information is allowed to be transmitted from the previous cell state $c _ { ( t - 1 ) }$ to the current cell state $c _ { t } .$ 

To derive the candidate cell input state $\hat { c } _ { t }$ , Eq. (18) is employed. Equation (19) involves the element-wise multiplication of the forget gate 


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/d3768ceb7cc335e8229e1f0082c26620b5b56fd66f44ddf8ed0f281e0a43b60f.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/fb529cb272fde26c11a3dc5ba063250f3c5b1797e059344739c28a45506af155.jpg)



Fig. 7. Comparisons of speed and acceleration between open-loop and closed-loop control algorithms.


$f _ { t }$ with the previous memory cell $c _ { ( t - 1 ) } .$ which determines whether the previous memory cell $c _ { ( t - 1 ) }$ holds pertinent information that should be retained. If the value of $f _ { t }$ at time step t is 0 (or close to 0), it suggests that the corresponding component in $c _ { ( t - 1 ) }$ must be removed by the LSTM. Conversely, if the value is 1, the information will be preserved. Similarly, the input gate $i _ { t }$ is multiplied element-wise by the current candidate cell input state $\tilde { c } _ { t }$ to determine the extent to which the current cell state $c _ { t }$ requires modification. Finally, Eq. (20) illustrates the values from the updated cell state $c _ { t }$ that will be added to the hidden state output $h _ { t }$ . 

$$
c _ {t} = \tanh  \left(W _ {c} x _ {t} + U _ {c} h _ {t - 1} + b _ {c}\right) \tag {18}
$$

$$
c _ {t} = f _ {t} \times c _ {t - 1} + i _ {t} \times c _ {t} \tag {19}
$$

$$
h _ {t} = o _ {t} \operatorname {t a n h} \left(c _ {t}\right) \tag {20}
$$

# 5. Results and discussion

This section shows the numerical analysis of the field experiment data with the proposed approaches. Our investigation begins by assessing the efficiency of the closed-loop optimal merging control algorithm in Eqs. (3)–(8). To validate this algorithm, we explore two distinct scenarios: (1) The scenario where the controlled CAV adheres to the VISSIM internal driver model, which is treated as an open-loop control strategy and baseline scenarios (Zeidler et al., 2019), and (2) the scenario where the CAV is governed by the deployed closed-loop optimal merging control strategy. 

Fig. 7 presents a comparative analysis of two different control strategies applied to CAVs by showing their performance on speed and acceleration. In Fig. 7, the blue bars represent the open-loop control strategy, which follows optimal driving command without adjusting to feedback, while the orange bars represent the closed-loop optimal merging control strategy, which continually adjusts the vehicle's actions based on real-time feedback to achieve an optimal performance. From the speed distribution on the left, it is evident that the closed-loop control tends to favor a narrower speed range centering around $1 0 \ \mathrm { m } / s ,$ , suggesting a more consistent driving speed when compared to the open-loop control, which shows a wider distribution of speeds. Fig. 7b indicates that the closed-loop strategy has a higher concentration of observations at 

lower acceleration values, especially around $0 { - } 1 0 ~ \mathrm { ~ m / s } ^ { 2 }$ , implying smoother acceleration and deceleration behaviors. In contrast, the openloop strategy displays a broader spread of acceleration values, with a significant number of observations at higher accelerations, which may reflect a less efficient or less comfortable driving experience. 

Fig. 8 illustrates the energy consumption when operating under two different control strategies. It is obvious that the closed-loop control strategy has a tighter distribution of energy consumption levels, predominantly clustered at the lower end of the energy scale. This suggests that the closed-loop control generally uses less energy. Moreover, the mean energy consumption per vehicle of the open-loop control is $1 2 . 5 \%$ higher at 0.00036 kWh compared to the closed-loop control, which has a mean of 0.00032 kWh. It further suggests the closed-loop strategy is more energy-efficient. The experiment indicated that the closed-loop control could potentially lead to reduced energy use in real-world applications. 

Then we examine the accuracy and robustness of the proposed H-LSTM model as this is significant to quantify the impacts of various factors on speed volatility and energy usage. Then we use the calibrated 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/cc99038e7224068a0e2d2c79e5bb6b53a6e88d586a5daaedf68a95e60df527aa.jpg)



Fig. 8. Comparisons of energy consumption between open-loop and closed-loop control algorithms.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/b91b3998286464975c50e758ba6b25d36c2c574452ad1d118bd1a2ef7d6e8e4f.jpg)



Fig. 9. High and low speed volatility from $K$ -means clustering.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/ab07be2e7b062459b67a07ea0f9c1d3e245c357a54332325432b618e1904f09a.jpg)



Fig. 10. Architecture of H-LSTM model.


model to explore such impacts. Noted that we combined the datasets from slow merging traffic and high traffic density scenarios for a collective analysis rather than treating them separately. This decision was informed by a comprehensive evaluation of the data, which indicated that there were no statistically significant differences in the results obtained from the two scenarios. 

Equations (9)–(11) are applied to compute the speed volatility. Then K-means clustering is used to group similar data points together. The goal is to partition the data points into two different clusters: high-speed volatility and low-speed volatility, as shown in Fig. 9. It is noted that these scenarios of speed volatility are independent of the ”slow merging traffic” and ”high traffic density” scenarios defined in the simulation. While the former scenarios focus on overall traffic conditions and speed itself, our analysis of speed volatility examines the fluctuations in speed, which are directly influenced by acceleration, the key control variable in the merging control algorithm. The distinction between high-speed and low-speed volatility is crucial because it allows us to recognize how the same factors can have different impacts under varying operating conditions. H-LSTM model was applied on two scenarios separately to quantify the impacts of different features on energy consumption. 

The overall H-LSTM model structure is shown in Fig. 10. Sequential historical data serve as input to an LSTM layer, followed by a fully connected layer. This sequence constructs the nonlinear term as specified in Eq. (9). Additional inputs, including speed, acceleration, yaw rate, and communication delay, are treated as linear factors. There are processed 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/f43beda44d6c0a01bfa37f797a9db4e4521f314c3e6c9dfd7b47e1b75c14b770.jpg)



Fig. 11. Training and validation loss of H-LSTM.


through a linear function to explore their impacts on the energy consumption. 

Fig. 11 shows the parameter optimization within the H-LSTM model, aiming at achieving optimal performance. The convergence of training and validation loss curves is an indicator of the well-tuned H-LSTM model, suggesting the model is learning effectively from the field data 

without over-fitting, as evidenced by the close alignment of the training and validation loss values. This ensures the model generalizes well to new and unseen data, therefore demonstrating the robustness of the parameter selection. 

Table 2 shows a comparative analysis of various linear and nonlinear predictive models, with a focus on their accuracy as measure by the Mean Absolute Percentage Error (MAPE). The proposed H-LSTM model demonstrates superior performance comparing others, achieving the lowest MAPE at $9 . 3 6 \%$ . This is a significant improvement over traditional models like ARIMA and Linear Regression, as well as standard LSTM models with two and three layers. The high accuracy of H-LSTM indicates that it is effective in capturing complex patterns in the CAV field data, which are often missed by simpler linear models and by less sophisticated nonlinear models. The H-LSTM with both linear and nonlinear terms improves its potentials to deliver more reliable and accurate forecasts in practical applications. 

With the well-trained and calibrated H-LSTM model, we further examine the impact of various factors on speed volatility and energy usage. It is noted that linear terms account for most of data variance $( 8 9 \% - 9 4 \% )$ ) so the nonlinear term is neglected for the analysis purpose. Table 3 shows the coefficient for speed volatility estimation and is intended to identify and weigh the dominant features that impact speed volatility in general, which establishes a foundational understanding of the key determinants that affect speed volatility across all scenarios. Hence, we do not differentiate between high-speed and low-speed conditions. Speed carries the most substantial weight at 0.55, indicating its predominant influence on speed volatility compared to acceleration, communication delay, and yaw rate. The coefficient also suggests that an increase of any of these factors is likely to increase the instability of speed and its potential energy consumption. It implies the significance of maintaining steady speeds in optimizing smooth traffic. 

The coefficient of 0.28 in communication delay suggests that even modest delays in information transmission can lead to noticeable increase in speed volatility. It becomes particularly important when considering the real-world implications of such volatility. In the scenarios of merging on high-speed roads, communication delays can disrupt the smooth vehicle operation. The resulting speed volatility may bring more frequent acceleration and deceleration, leading to broader traffic inefficiencies. 

Table 4 shows coefficients of linear terms in H-LSTM model for energy estimation under high- and low-speed volatility. The distinction between high-speed and low-speed volatility is crucial because it allows for a comprehensive analysis that recognizes the differential effects under different operating conditions. As explained before, the linear components account for most of the data variance. Hence, for the purposes of this analysis, the nonlinear term is considered negligible. The coefficients of speed, acceleration, and delay under high-speed volatility are higher 


Table 2 Model comparisons in mean absolute percentage error (MAPE).


<table><tr><td>Model</td><td>MAPE (%)</td></tr><tr><td>ARIMA</td><td>25.69</td></tr><tr><td>Linear regression</td><td>12.36</td></tr><tr><td>Partial least square regression</td><td>11.68</td></tr><tr><td>LSTM - 2 layers</td><td>10.98</td></tr><tr><td>LSTM - 3 layers</td><td>10.55</td></tr><tr><td>H-LSTM</td><td>9.36</td></tr></table>


Table 3 Coefficient for speed volatility estimation.


<table><tr><td>Factor</td><td>Value</td></tr><tr><td>Speed</td><td>0.55</td></tr><tr><td>Acceleration</td><td>0.24</td></tr><tr><td>Delay</td><td>0.28</td></tr><tr><td>Yaw rate</td><td>0.27</td></tr></table>


Table 4 Coefficient for energy estimation.


<table><tr><td>Factor</td><td>High-speed volatility</td><td>Low-speed volatility</td></tr><tr><td>Speed</td><td>0.70</td><td>0.47</td></tr><tr><td>Acceleration</td><td>1.44</td><td>1.16</td></tr><tr><td>Delay</td><td>0.70</td><td>0.63</td></tr><tr><td>Yaw rate</td><td>0.71</td><td>1.11</td></tr></table>

than those under low-speed volatility, implying that an identical increase in these variables results in a large surge in energy consumption when compared to scenarios with lower speed volatility. This suggests that stability in speed plays a critical role in energy efficiency, with unstable speed leading to higher energy demand. In the contrast, the coefficient for yaw rate is higher under low-speed volatility. This indicates that yaw rate, a measure of rate of change in the vehicles' direction, has a more significant impact on energy consumption when speeds are relatively stable. It may be due to the additional energy required to alter the vehicles' trajectory. Noted the coefficient of communication delay is substantial under both scenarios: 0.7 under high-speed volatility and 0.63 under low-speed volatility. The difference suggests that communication delay has a more significant impact on energy consumption when speed volatility is high. This could be attributed to the CAV's control system that CAV may make more aggressive adjustments to speed and direction to overcompensate for delayed information, therefore consuming more energy. Moreover, it also indicates that minor improvements in reducing communication delay could lead to measurable gains in energy efficiency. For example, if communication delay increases by 0.01 s, it could save 0.007 kWh at each time step. This is because the coefficient for delay in the context of high-speed volatility is given as 0.70, which represents the amount of energy (in kWh) conserved or expended for each unit change in the communication delay. According to Eq. (12), if there is a decrease in delay $d ( k )$ by 0.01 s (which translates into $- 0 . 0 1$ in Eq. (12) since it is a reduction), we can calculate the impact on energy consumption by multiplying this change by the coefficient of delay. The findings highlight the necessary of robust communication infrastructures to minimize communication delays and enhance the operational and energy efficiency. 

# 6. Conclusions

This study applied H-LSTM model to quantify the impacts of communication delay on speed volatility and energy consumption with field test data. Specifically, the merging control algorithm was implemented on the real vehicles in ACM test track and virtual vehicles in its digital twin. The optimal merging commands were communicated to the real vehicle to affect its driving behaviors. The real CAV controlled its speed and acceleration based on the optimal command, but it was constrained by the virtual leading vehicle in simulation. The proposed algorithms demonstrated that under high-speed volatility, the impact of delay on energy consumption is more significant than that under lowspeed volatility. Among all features, acceleration is the most significant features affecting the energy consumption comparing to other features. The numerical results also indicate that minor improvements in reducing communication delay could lead to measurable gains in energy efficiency. For example, if communication delay increases by 0.01 s, it could save 0.007 kWh at each time step. 

This study can be extended for a few research directions in the future. We will conduct more controlled analytical experiments for analysis. These controlled experiments would allow us to establish causality rather than mere correlation and are a logical next step for further research. In addition, communication delay may not only affect the energy consumption of real vehicle but could also affect the vehicle platoon on the freeways as well. These impacts are also worthwhile to evaluate. Additionally, different merging control algorithm may have varied performance regarding to the vehicle platoon performance. It would be 

interesting to test and compare different algorithms as well, which can lead to a higher market share of Battery Electric Vehicles (BEVs). 

# Replication and data sharing

Raw data were generated at America Center of Mobility. Derived data supporting the findings of this study may be provided with sponsor restrictions from the corresponding author on reasonable request. Demo data can be found at https://github.com/wanli3301114/Communication Delay.git. 

# CRediT authorship contribution statement

Wan Li: Writing – review & editing, Writing – original draft, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. Jackeline Rios-Torres: Writing – review & editing, Writing – original draft, Funding acquisition, Data curation, Conceptualization. Boyu Wang: Writing – original draft, Formal analysis. Zulqarnain H. Khattak: Writing – review & editing, Writing – original draft, Project administration, Methodology, Investigation, Funding acquisition, Data curation, Conceptualization. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Acknowledgement

This funding for this research was provided by US Department of Energy (DOE) under the project EEMS082:Validation of Connected and Automated Mobility System. The authors are thankful for the support. 

# References



Ali, Y., Zheng, Z., Haque, M.M., 2021. Modelling lane-changing execution behaviour in a connected environment: a grouped random parameters with heterogeneity-in-means approach. Commun. Transp. Res. 1, 100009. 





American Center for Mobility (ACM), 2024. Offerings & services. https://acmwillowrun. org/offerings-services/#technology. 





An, H., Jung, J.-i., 2018. Design of a cooperative lane change protocol for a connected and automated vehicle based on an estimation of the communication delay. Sensors 18, 3499. 





Branzi, V., Meocci, M., Domenichini, L., Calcinai, M., 2021. A combined simulation approach to evaluate overtaking behaviour on two-lane two-way rural roads. J. Adv. Transport. 2021, 1–18. 





Buller, W., Chase, R., Paki, J.E., Dudekula, A.B., Naber, J., Sarkar, R.. Flexiblearchitecture for testing connectedvehiclesinrealistic traffic.https://doi.org/10.4271/2023-01-0218. 





Di, Y., Zhang, W., Ding, H., Zheng, X., Bai, H., 2023. Integrated control for mixed cav and cv traffic flow in expressway merge zones combined with variable speed limit, ramp metering, and lane changing. J. Transport. Eng., Part A: Systems 149, 04022140. 





Fang, Y., Min, H., Wu, X., Wang, W., Zhao, X., Mao, G., 2022. On-ramp merging strategies of connected and automated vehicles considering communication delay. IEEE Trans. Intell. Transport. Syst. 23, 15298–15312. 





Ge, J., Xu, H., Zhang, J., Zhang, Y., Yao, D., Li, L., et al., 2022. Heterogeneous driver modeling and corner scenarios sampling for automated vehicles testing. J. Adv. Transport. 2022, 8655514. 





Gu, Z., Wang, Z., Liu, Z., Saberi, M., 2022. Network traffic instability with automated driving and cooperative merging. Transport. Res. C Emerg. Technol. 138, 103626. 





Guo, J., Cheng, S., Liu, Y., 2020. Merging and diverging impact on mixed traffic of regular and autonomous vehicles. IEEE Trans. Intell. Transport. Syst. 22, 1639–1649. 





Khattak, Z.H., Rios-Torres, J., Fontaine, M.D., 2023. Impact of communications delay on safety and stability of connected and automated vehicle platoons: empirical evidence from experimental data. IEEE Access 11, 128549–128568. 





Khattak, Z.H., Smith, B., Fontaine, M., Ma, J., Khattak, A., 2022. Active lane management and control using connected and automated vehicles in a mixed traffic environment. Transport. Res. C Emerg. Technol. 139, 103648. 





Khattak, Z.H., Smith, B., Park, H., Fontaine, M., 2020. Cooperative lane control application for fully connected and automated vehicles at multilane freeways. Transport. Res. C Emerg. Technol. 111, 294–317. 





Larsson, J., Keskin, M.F., Peng, B., Kulcs-ar, B., Wymeersch, H., 2021. Pro-social control of connected automated vehicles in mixed-autonomy multi-lane highway traffic. Commun. Transp. Res. 1, 100019. 





Lento, C., Gradojevic, N., Wright, C.S., 2007. Investment information content in bollinger bands? Appl. Financ. Econ. Lett. 3, 263–267. 





Li, M., Li, Z., Wang, S., Zheng, S., 2023. Enhancing cooperation of vehicle merging control in heavy traffic using communication-based soft actor-critic algorithm. IEEE Trans. Intell. Transport. Syst. 24, 6491–6506. 





Liu, H., Zhuang, W., Yin, G., Li, Z., Cao, D., 2023. Safety-critical and flexible cooperative on-ramp merging control of connected and automated vehicles in mixed traffic. IEEE Trans. Intell. Transport. Syst. 24, 2920–2934. 





Mcity, 2023. Mcity test facility. https://mcity.umich.edu/what-we-do/mcity-testfacility/. 





Mohammadian, S., Zheng, Z., Haque, M.M., Bhaskar, A., 2023. Continuum modeling of freeway traffic flows: state-of-the-art, challenges and future directions in the era of connected and automated vehicles. Commun. Transp. Res. 3, 100107. 





Olovsson, T., Svensson, T., Wu, J., 2022. Future connected vehicles: communications demands, privacy and cyber-security. Commun. Transp. Res. Commun. Transp. Res. 2, 100056. 





Pontryagin, L.S., 2018. Mathematical Theory of Optimal Processes. London: Routledge. 





Quek, A., 2017. Singapore autonomous vehicle initiative (savi). https://cetran.sg/news/. Rios-Torres, J., Khattak, Z., Han, J., Wang, C., Lim, H., 2021. Assessing the implications of automated merging control in a mixed and heterogeneous traffic environment. In: 2021 IEEE International Intelligent Transportation Systems Conference (ITSC), pp. 1098–1104. 





Rios-Torres, J., Malikopoulos, A.A., 2016. Automated and cooperative vehicle merging at highway on-ramps. IEEE Trans. Intell. Transport. Syst. 18, 780–789. 





Subramaniyan, A.B., Wang, C., Shao, Y., Li, W., Wang, H., Zhang, G., Ma, T., 2023. Hybrid recurrent neural network modeling for traffic delay prediction at signalized intersections along an urban arterial. IEEE Trans. Intell. Transport. Syst. 24, 1384–1394. 





Tang, Z., Zhu, H., Zhang, X., Iryo-Asano, M., Nakamura, H., 2022. A novel hierarchical cooperative merging control model of connected and automated vehicles featuring flexible merging positions in system optimization. Transport. Res. C Emerg. Technol. 138, 103650. 





Xiao, W., Cassandras, C.G., 2021. Decentralized optimal merging control for connected and automated vehicles with safety constraint guarantees. Automatica 123, 109333. 





Xiong, B.-K., Jiang, R., Li, X., 2022. Managing merging from a cav lane to a human-driven vehicle lane considering the uncertainty of human driving. Transport. Res. C Emerg. Technol. 142, 103775. 





Yan, M., Ma, W., Zuo, L., Yang, P., 2020. Distributed model predictive control for platooning of heterogeneous vehicles with multiple constraints and communication delays. J. Adv. Transport. 2020, 1–16. 





Zeidler, V., Buck, H.S., Kautzsch, L., Vortisch, P., Weyland, C.M., 2019. Simulation of autonomous vehicles based on wiedemann's car following model in ptv vissim. In: Proceedings of the 98th Annual Meeting of the Transportation Research Board (TRB), Washington, DC, USA, pp. 13–17. 





Zhou, M., Qu, X., Jin, S., 2016. On the impact of cooperative autonomous vehicles in improving freeway merging: a modified intelligent driver model-based approach. IEEE Trans. Intell. Transport. Syst. 18, 1422–1428. 





Zhu, J., Easa, S., Gao, K., 2022. Merging control strategies of connected and autonomous vehicles at freeway on-ramps: a comprehensive review. J. Intell. Connect. Veh. 5, 99–111. 



![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/d1f2d783d8882588234a31795804c12f0ff63165baab5ae97c84c76ab6945feb.jpg)


Wan Li is a Research Associate Staff Member in the Mobility and Energy Transitions Analysis (META) group at Oak Ridge National Laboratory (ORNL). She earned the Ph.D. degree in civil engineering from the University of Washington in 2019 and the M.S. degree in civil engineering from Louisiana State University in 2014. Her research primarily focuses on traffic system modeling and simulation, urban transportation network operation and control, data-driven spatiotemporal forecasting, and transportation big data analytics. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/3f3391be2b52ac8229947e69f9b90f7201dc3744cd445b83f282f19d78c8241b.jpg)


Jackeline Rios-Torres received the Ph.D. degree in automotive engineering from Clemson University and the B.S. degree in electronic engineering from the Universidad del Valle-Colombia. Her current research is mainly focused on the development of optimal connected and automated vehicles (CAVs) coordination strategies and the analysis of their implications considering different traffic scenarios to increase mobility energy efficiency. Her research interests include analysis, control and optimization of intelligent transportation and mobility systems, advanced driver assistance systems and energy management control for advanced powertrain systems. She received the Ph.D. degree in automotive engineering from Clemson University in 2015 and the B.S. degree in electronic engineering from the Universidad del Valle-Colombia in 2007. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/c4b7eae34cf34a93350655a877d96a55bc489b55db6bab4bbef316b0b51ab3de.jpg)



Zulqarnain H. Khattak is a Research Faculty/systems Scientist at Carnegie Mellon University (CMU). Prior to joining CMU, he was a R&D staff scientist at Oak Ridge National Laboratory. He received the M.S. degree in transportation systems engineering from the University of Pittsburgh in 2016 and the Ph.D. degree in civil (transportation systems) engineering from University of Virginia in 2019. His research interests are at the interface of data analytics and simulation for smart mobility systems. These include the operational, safety, energy, efficiency and cybersecurity assessment of intelligent transportation systems and disruptive connected and automated vehicles. His research leverages the application of optimization, control theory, advanced statistical and machine learning methods. He has authored several articles on cooperative automated mobility. He is an associate member of American Society of Civil Engineers (ASCE) and Institute of Electrical and Electronics Engineers (IEEE).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-28/d0cf8915-13ff-46a9-942f-ceb5f18a2516/32b339e9292e57045a83b0eecc9d679a2ea9001b8f8d3fffaf32f93be3195ae6.jpg)



Boyu Wang is an Assistant Professor at Beijing University of Civil Engineering and Architecture. He received the Ph.D. degree and M.S. degree in Electrical Engineering from Louisiana State University in 2018 and 2015, respectively. His research interests include decentralized optimal control, power system stability analysis, machine learning applications in smart cities and load forecasting.
