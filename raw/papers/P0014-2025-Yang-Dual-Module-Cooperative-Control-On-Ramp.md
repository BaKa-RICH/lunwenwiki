# A dual-module cooperative control method for on-ramp area in heterogeneous traffic flow using reinforcement learning

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/a45ca9e9f3dcde30a6de1b901c862e735dcd8e7207daa19e2113471751895ea5.jpg)


Wenzhang Yang a,b,c , $\mathrm { a , b , c _ { \phi } } _ { \phi }$ Changyin Dong d,e , Ziqian Zhang a,b,c , Xu Chen a,b,c , Hao Wang a,b,c,* 

a Jiangsu Key Laboratory of Urban ITS, Southeast University, Nanjing, 211189, China 

b Jiangsu Province Collaborative Innovation Center of Modern Urban Traffic Technologies, Nanjing, 211189, China 

c School of Transportation, Southeast University, Nanjing, 211189, China 

d School of Aeronautics, Northwestern Polytechnical University, Xi’an, 710072, China 

e National Key Laboratory of Aircraft Configuration Design, Xi’an, 710072, China 

# A R T I C L E I N F O

Keywords: 

On-ramp 

Reinforcement learning 

Cooperative control 

Heterogeneous traffic flow 

# A B S T R A C T

In the on-ramp area, vehicle conflicts significantly reduce traffic efficiency and increase collision risks. This study introduces a novel dual-module cooperative control approach designed for on-ramps that accommodate heterogeneous traffic flows, including connected and automated vehicles (CAVs) and human driving vehicles (HDVs). By utilizing reinforcement learning techniques, the approach aims to enhance both traffic efficiency and safety. The approach comprises two key modules: the merging control module and the lane-changing control module. The merging control module facilitates cooperation between mainline and ramp vehicles, while the lane-changing control module assists mainline CAVs in making informed lane-change decisions. Agents within these modules are trained using the proximal policy optimization algorithm, known for its strong convergence properties. After 100 to 200 training episodes, the agents achieve stable peak average rewards. Simulation results demonstrate significant improvements in traffic efficiency and safety with the dual-module control method in onramp areas, especially in scenarios involving CAV-HDV heterogeneous traffic flows. With a CAV penetration rate of just 0.2, average vehicle delay is reduced by $2 6 ~ \%$ . Furthermore, from a safety perspective, when the CAV penetration rate reaches or exceeds 0.3, the time-exposed time-to-collision decreases by approximately $4 5 \ \%$ . Transferability analysis indicates that integrating reinforcement learning agents into the control strategy produces positive results across varying maximum speeds and flow rates. In heterogeneous traffic environments, it is advisable to train agents at high CAV penetration rates. Comparative studies further show that the proposed method significantly enhances traffic efficiency and safety, maintaining robust performance even at lower CAV penetration rates. 

# 1. Introduction

# 1.1. Background and objective

The on-ramp area is a critical component of the highway network, serving as a vital junction where vehicles from the mainline and ramp merge. However, this merging process can lead to continuous traffic conflicts, posing a significant risk of vehicle collisions. As these conflicts tend to propagate upstream along the highway, they can have a detrimental effect on the overall traffic efficiency of the road network (Liu et al., 2018; Rios-Torres and Malikopoulos, 2017a,b). In response, 

researchers have focused their efforts on studying the specific traffic issues related to on-ramp areas, aiming to improve traffic conditions within this zone. This includes enhancing traffic efficiency (Pooladsanj et al., 2023; Shang et al., 2023; Sun et al., 2020; Xue et al., 2023), safety (Sheikh and Peng, 2023; Yang et al., 2023b; Zhu and Tasic, 2021; Zhu et al., 2022), reducing fuel consumption (Yang et al., 2023a), and minimizing pollutant emissions (Mu et al., 2021). 

Currently, the control measures implemented in the on-ramp area primarily aim to restrict the speed of vehicles within the ramp and establish a dedicated acceleration lane alongside the mainline. Once vehicles enter the acceleration lane, they accelerate to a speed higher 

than the low limit and carefully select an appropriate moment to merge into the mainline (Hua et al., 2009; Jia et al., 2005). This approach is adopted because lower speeds on the ramp reduce the risk of merging collisions (Li et al., 2007). While this strategy enhances safety to some extent, it significantly limits the ramp’s capacity, often leading to congestion when a continuous flow of vehicles enters from the ramp entrance. Moreover, in cases of mild congestion, the merging process cannot be guaranteed to be safe due to the inability to regulate impulsive merging behavior of ramp vehicles (Lee et al., 2006). To address this issue, certain on-ramp areas have implemented ramp metering techniques to regulate the entry of ramp vehicles into the mainline during specific time periods (Han et al., 2022; Pooladsanj et al., 2023). Although some advanced ramp metering methods have shown moderate improvements in overall traffic efficiency in recent years, they still prioritize the right-of-way for mainline vehicles at the expense of ramp vehicles. 

The emergence of connected and automated vehicles (CAVs) has brought about a revolution in on-ramp control strategies. CAVs possess the capability to collect real-time data on nearby vehicles, empowering them to make more informed decisions compared to human driving vehicles (HDVs) (Dong et al., 2023; Greguri´c et al., 2022; Nie et al., 2024; Norouzi et al., 2023; Sharma et al., 2021; Chen et al., 2024a,b, 2025). Moreover, when coupled with vehicle-to-everything (V2X) technology, seamless communication can be established among CAVs as well as between CAVs and control centers located in the on-ramp area. This facilitates cooperative control of vehicles on both the ramp and the mainline, without compromising the right of way on the ramp. Cooperative control holds immense potential for enhancing the efficiency and safety of the on-ramp area, and has emerged as a prominent approach in the field of on-ramp control within the CAV environment (Sun et al., 2020; Xue et al., 2023; Yang et al., 2023a&b). 

There are two primary research directions for the cooperative control of CAVs in on-ramp areas. The first direction focuses on optimizing the merging process, which typically involves the ramp and only one adjacent lane in the mainline. By controlling vehicles in both lanes, merging conflicts can be mitigated (Mu et al., 2021; Rios-Torres and Malikopoulos, 2017a; Sun et al., 2020; Xue et al., 2023; Yang et al., 2023a&b). The second direction involves optimizing lane selection in scenarios where there are multiple lanes on the mainline. The objective of cooperative control is to enable CAVs to select more suitable lanes, thereby improving overall traffic efficiency (Ding et al., 2021; Liu et al., 2022a). Some studies also incorporate both strategies mentioned above, resulting in a better overall outcome (Han et al., 2023; Hou et al., 2023; Luo et al., 2022). 

Among the various cooperative control methods, reinforcement learning (RL) stands out due to its exceptional optimization potential, making it one of the most prominent approaches in the field (He et al., 2023; Li et al., 2023, 2024a; Lin et al., 2022). Accordingly, this study proposes a cooperative control method for CAVs in the on-ramp area, utilizing RL algorithms. This method comprises two modules. One focuses on optimizing the merging process, while the other focuses on lane selection. The method is specifically designed for the heterogeneous traffic flow of CAV-HDV, resulting in significant improvements in traffic efficiency and a reduction in collision risk. This research represents an enhancement of the on-ramp cooperative control method in the CAV era, contributing to the development of more efficient and safer intelligent transportation systems. 

# 1.2. Literature review

# 1.2.1. Inclusion and exclusion criteria

In the literature review of this section, only studies that meet the following inclusion criteria were selected: 

● Only English language studies. 

● Studies published in English. 

● Studies published in peer-reviewed journals or conferences. 

Studies focused on cooperative control of the merging process for CAVs. 

Studies addressing cooperative control of the lane-changing process for CAVs. 

Priority is given to studies published within the past five years to ensure the relevance of the research findings. Additionally, earlier studies that are highly cited or of significant importance are also considered for inclusion in the literature review. 

# 1.2.2. Cooperative control of the merging process

In recent years, CAVs have become a focal point within the transportation industry, as highlighted by numerous significant studies (Dong et al., 2018; Gao et al., 2024a&Gao et al., 2024b; Gokasar et al., 2023; Min et al., 2024; Qin et al., 2019). CAVs are characterized by two essential features: “connected” and “automated.” The “connected” aspect allows CAVs to interact with various information sources, while the “automated” feature enables them to perform driving tasks independently without human intervention. 

This unique combination has spurred research into the cooperative control of CAVs, particularly in the context of merging processes within on-ramp areas. A classic approach in this research area involves cooperative control based on virtual platoons, a concept initially proposed by Lu et al. (2004) for on-ramp merging. In this control mode, CAVs from both the mainline and the ramp are organized into a single platoon, granting equal right of way to vehicles from both sources. 

Building on the theory of virtual platoons, Rios-Torres and Maliko poulos (2017a) introduced an optimization framework and analytical solutions for real-time coordination of CAVs at merging zones. Chen et al. (2021) established vehicle virtual platoons based on rotation within the on-ramp environment and developed a multi-predecessor virtual car-following model, along with a unidirectional multi-leader communication topology to manage the longitudinal behavior of each CAV. Xue et al. (2023) further divided CAVs on the mainline and ramp into multiple local virtual platoons, allowing their control method to adapt to varying traffic conditions. Li et al. (2024b) proposed a merging control strategy for connected and automated electric vehicle platooning to enhance time and energy efficiency, clustering vehicles to minimize excessive acceleration and reduce computational demands. Meng et al. (2024) designed a spatially correlated controller with uniform boundedness and robustness for each vehicle in the virtual platoon, enabling real-time analysis of control effects, which contributed to greater stability and reliability of the proposed strategy. 

Many control methods emphasize that strategies should be implemented before vehicles enter the merging area. For instance, Liao et al. (2022) developed a cooperative on-ramp merging system for CAVs that facilitates coordination among merging vehicles prior to their entry into the merging zone. Their findings indicated that early cooperation effectively addresses safety and environmental sustainability issues, even with acceptable communication delays. Tang et al. (2022) explored the non-fixed merging positions of CAVs, optimizing both the merging order and key vehicle states in advance, which significantly improved traffic efficiency. Jing et al. (2022) created a hierarchical, decentralized cooperative coordination framework designed to enhance merging efficiency while reducing fuel consumption. Fang et al. (2022) investigated the effects of communication delays on cooperative control during the merging of CAVs, focusing on centralized early control. In the model of Chen et al. (2024), the optimal number of auxiliary vehicles from the mainline and their specific roles were determined during early cooperation to mitigate interference during on-ramp merging. Zhou et al. (2024) addressed temporary congestion by managing the gaps created by highway mainline vehicles for merging vehicles from ramps, achieving positive outcomes. 

While the studies mentioned above primarily focus on pure CAV environments, some research has begun to address the merging 

challenges posed by heterogeneous traffic flows, anticipating the coexistence of CAVs and HDVs in future traffic scenarios. For example, Sun et al. (2020) proposed a cooperative decision-making mechanism to enhance overall throughput in CAV-HDV environments. Mu et al. (2021) presented a systematic trajectory planning approach for optimizing merging processes in heterogeneous traffic conditions. Liu et al. (2022b) examined the formation of virtual platoons in such environments, while Yang et al. (2023b) introduced a gap selection model for ramp vehicles, enabling the formation of optimal virtual platoons to enhance merging safety. Hou et al. (2023) determined the optimal merging positions for vehicles transitioning from ramps to adjacent mainline lanes, assigning cooperative vehicles to stabilize the merging process, particularly effective at high CAV penetration rates. Liu et al. (2023a) developed a hierarchical cooperative ramp merging control strategy to optimize flexible trajectories with safety guarantees in heterogeneous traffic, addressing the uncertainties posed by human driver behaviors. Li et al. (2024c) analyzed how macro traffic flow conditions impact merging processes in heterogeneous traffic, leading to improved traffic efficiency while significantly reducing accident risks and emissions. 

In recent years, the concept of RL has gained significant traction, leading to a surge in studies focusing on cooperative control of CAVs within on-ramp areas using RL techniques. For instance, Li et al. (2022) successfully integrated RL technology into vehicle merging control, resulting in a tangible reduction in travel time. Lin et al. (2022) explored automated on-ramp merging strategies specifically tailored for a power-split Plug-In Hybrid Electric Vehicle, leveraging deep RL methodologies. Furthermore, Li et al. (2024a) devised an innovative interactive merging strategy based on multi-agent deep RL, facilitating ramp CAVs in gauging the dynamic responses of mainline vehicles. He et al. (2023) and Liu et al. (2022a) also employed RL methods from various perspectives to address the issue of vehicle merging on the ramp. 

# 1.2.3. Cooperative control of the lane-changing process

Cooperative lane-changing control technology has emerged as a significant research focus in the field of intelligent transportation systems in recent years. This technology aims to improve the traffic conditions by facilitating cooperation among vehicles during lane changes. For instance, Yuan et al. (2021) proposed a game theory-based lane-- changing strategy that optimizes autonomous lane-changing decisions among CAVs. Atagoziev et al. (2023) developed an algorithm designed to minimize the time it takes for a single CAV to change lanes. Additionally, the control strategy proposed by Sun et al. (2023) enables vehicles to smoothly merge during lane changes and quickly achieve stable tracking of vehicles in the target lane afterward. 

In heterogeneous traffic environments, the cooperative lanechanging strategy for CAVs is particularly crucial, as vehicles must navigate various complex traffic conditions and dynamic changes. For example, Wang et al. (2022) examined the impact of CAV penetration rates on lane-changing strategies in heterogeneous traffic flows. Similarly, Peng et al. (2022) derived an optimized method for CAV lane changes at different penetration rates, considering the stability of heterogeneous traffic and optimal control strategies. Liu et al. (2023b) focused on using CAVs to mitigate the negative lane-changing behaviors of surrounding HDVs, thereby improving string stability in heterogeneous traffic flow. Shen et al. (2024) explored all possible vehicle configurations around a CAV and proposed a dynamic hierarchical cooperative lane-changing strategy that generates optimal lane-changing trajectories to enhance driving comfort and efficiency. 

Additionally, several studies have addressed lane change issues in specific application scenarios. Li et al. (2022) introduced a cooperative energy-efficient lane change model for truck platooning, which maintains platoon cohesion through cooperative speed adjustments and model predictive control. Wang et al. (2024) developed a new lane change control strategy for hybrid electric vehicles, demonstrating superior performance compared to traditional methods. From a practical perspective, cooperative lane change control technology has been tested 

and implemented in various real-world situations. For example, Chen et al. (2023) and Dong et al. (2023) investigated vehicle lane-changing control in off-ramp areas to enhance safety and efficiency. Jiang et al., 2024 proposed an optimal control strategy that improves the transition of CAVs from ordinary lanes to dedicated lanes, thereby boosting traffic safety and efficiency. Liu et al. (2024) concentrated on the lane-changing process for CAVs moving from dedicated lanes to adjacent lanes, aiming to increase both the success rate and execution time of this maneuver. 

Moreover, substantial research has focused on the lane-changing behavior of mainline vehicles near on-ramps. For instance, Ding et al. (2021) introduced an automated cooperative control approach specifically designed for CAVs in multilane freeway merging zones, incorporating a model for mainline vehicle lane changes that considers on-ramp traffic demands. Similarly, Luo et al. (2022) proposed a strategy for a centralized controller to facilitate the efficient merging of CAVs from a multiple-lane on-ramp. Sharma et al. (2022) developed a multi-class lane change advisory system that significantly enhances traffic efficiency at highway merging sections using cooperative intelligent transportation systems. In a related study, Hou et al. (2023) proposed a hierarchical model for collaborative control on the on-ramp under heterogeneous traffic conditions, which enables the creation of suitable merging opportunities for ramp vehicles through adjustments in the mainline vehicle lanes. Furthermore, Han et al. (2023) introduced a trajectory optimization strategy for CAVs that integrates both lane-changing and merging optimizations. Li et al. (2024d) proposed a lateral velocity control strategy for lane changes in the on-ramp area, offering efficient lateral guidance for CAVs through optimal lateral velocity control parameters. 

# 1.3. Contribution and organization

The main contributions of this research are twofold. First, we introduce an innovative optimization approach specifically tailored for the intricate dynamics of on-ramp merging scenarios. Our method features two cohesive modules designed to tackle the unique challenges posed by multi-lane on-ramps. This approach not only optimizes the merging behavior of vehicles entering from the ramp but also improves the lane-changing dynamics of vehicles on the mainline. Of particular importance is the method’s versatility in environments with both CAVs and HDVs. Remarkably, even with low penetration rates of CAVs, our approach substantially enhances overall traffic efficiency and safety. Second, this study explores the training of distinct RL agents operating in various lanes, providing a nuanced strategy for CAVs. The final control decision for a CAV was derived from a collaboration between the agent’s chosen actions and foundational traffic regulations, ensuring a control strategy that is both robust and reliable. The combination of these elements is infrequently addressed in existing literature, and our results robustly demonstrate the efficacy of the proposed methodology, underscoring the research’s importance in advancing traffic control strategies. 

The remainder of this paper is organized as follows: The on-ramp scenario of this research is described in Section 2. Section 3 proposes the dual-module cooperative control method. The simulation experimental is designed in Section 4. Then Section 5 shows the simulation results and discussions. Finally, the conclusions are introduced in Section 6. 

# 2. On-ramp scenario

As depicted in Fig. 1, the on-ramp scenario investigated in this study comprises one ramp and two mainline lanes. To facilitate clarity in the description, the acceleration lane is considered to be part of the ramp. The two mainline lanes are named as Lane 1 and Lane 2. Lane 1 is located on the inner side of the mainline, while Lane 2 is situated on the outer side. In an intelligent transportation system, the on-ramp area is 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/d9bb2369e76d7624b6372f20c9f057d4478ace3d1c8ac5b05f2c32273a8109fc.jpg)



Fig. 1. The environment of the on-ramp area.


outfitted with roadside perception equipment to enable real-time detection and monitoring of all vehicles within its range. The coverage of the roadside perception equipment should extend a certain distance before and after the merging point of each lane, and cover both the mainline and ramp equally. This equipment transmits real-time information, including vehicle speed and position, to the control center. Leveraging V2X technology (Ji et al., 2023; Jiang et al., 2021), the control center can transmit control commands to CAVs based on this information. However, HDVs, although perceptible, remain under the control of human drivers and thus are uncontrollable. 

The control center transmits control commands to CAVs with the aim of enhancing traffic conditions within the on-ramp area, focusing on two key objectives. Firstly, it seeks to enhance traffic efficiency, minimize delays, and increase throughput. Throughput refers to the number of vehicles exiting the on-ramp area within a specific time frame. As illustrated in Fig. 1, traffic flow from three lanes (Lane 1, Lane 2, ramp) enters the on-ramp area but ultimately exits through the two mainline lanes (Lane 1, Lane 2). This invariably results in traffic conflicts between vehicles from different lanes, with merging conflicts between Lane 2 vehicles and ramp vehicles being the most prevalent (Yang et al., 2023b; Zhu and Tasic, 2021). Furthermore, traffic conflicts arising from Lane 2 may spill over to Lane 1 due to lane-changing activities. Therefore, the second objective of the control center is to mitigate conflicts stemming from vehicle merging and promote safety. The dual-module cooperative control method proposed in this study specifically targets these twin objectives: efficiency and safety. 

# 3. Dual-module cooperative control method

This section aims to present a dual-module cooperative control method. The focus of this method lies in regulating CAVs situated within the on-ramp area. Specifically, the method encompasses two primary modules: merging control (MC) and lane-changing control (LC). The MC module operates by orchestrating cooperative control among Lane 2 vehicles and ramp vehicles. As for the LC module, it serves to aid mainline CAVs in making informed decisions regarding lane changes. Simultaneously, this module governs the conduct of Lane 1 vehicles, facilitating seamless coordination with those in Lane 2 during lane-

changing maneuvers. Both modules utilize RL techniques to achieve their primary objectives of enhancing efficiency and safety. This involves defining specific actions, states, and rewards to guide the learning process. For this particular study, the RL algorithm employed is proximal policy optimization (PPO) algorithms (Schulman et al., 2017). 

# 3.1. Proximal policy optimization algorithm

The PPO algorithm, introduced by OpenAI (Schulman et al., 2017), has gained significant popularity as one of the most prevalent RL algorithms in use today. Its principal aim is to optimize a “surrogate” objective function through stochastic gradient ascent, thereby facilitating ongoing refinement of the strategy as it interacts with the environment and collects data samples. A distinguishing characteristic of the PPO algorithm is its capability to support multiple epochs of minibatch updates, as opposed to the traditional policy gradient method that only allows for one gradient update per data sample. This feature sets PPO apart from its counterparts and contributes to its effectiveness in RL tasks. 

Furthermore, the PPO algorithm shares some characteristics with the trust region policy optimization (TRPO) algorithm (Schulman et al., 2015). In the TRPO algorithm, the objective function is defined as: 

$$
L ^ {C P I} (\theta) = \widehat {\mathbb {E}} _ {t} \left[ \begin{array}{l} \pi_ {\theta} (a _ {t} | s _ {t}) \\ \pi_ {\theta_ {\mathrm {o l d}}} (a _ {t} | s _ {t}) \widehat {A} _ {t} \end{array} \right] = \widehat {\mathbb {E}} _ {t} [ r _ {t} (\theta) \widehat {A} _ {t} ] \tag {1}
$$

where $\pi _ { \theta }$ is the stochastic policy. $\theta _ { \mathrm { o l d } }$ denotes the vector of policy parameters prior to any updates. $r _ { t } ( \theta )$ is the simplified notation for probability ratio. The superscript CPI represents that it is an objective of conservative policy iteration (Kakade and Langford, 2002). As an enhancement to the TRPO algorithm, the primary optimization objective of the PPO algorithm is as follows: 

$$
L ^ {C L I P} (\theta) = \widehat {\mathbb {E}} _ {t} \left[ \min  \left(r _ {t} (\theta) \widehat {A} _ {t}, \operatorname {c l i p} \left(r _ {t} (\theta), 1 - \epsilon , 1 + \epsilon\right) \widehat {A} _ {t}\right) \right] \tag {2}
$$

where $\widehat { A } _ { t }$ is an estimator of the advantage function at timestep t. The expectation $\widehat { \mathbb { E } } _ { t }$ indicates the empirical average over a finite batch of 

samples. ϵ is a the clipped parameter. 

Algorithm 1: PPO (Schulman et al., 2017) 

for iteration $= 1,2,\ldots$ do   
for actor $= 1,2,\dots,N$ do   
Run policy $\pi_{\mathrm{old}}$ in environment for $T$ timesteps   
Compute advantage estimates $\hat{A}_1,\dots \hat{A}_T$ end for Optimize surrogate $L^{CLIP}(\theta)$ , with epochs and batch size $\theta_{\mathrm{old}}\gets \theta$ end for 

Under the optimization objective outlined in Eq. (2), the pseudocode for the PPO algorithm is presented in Algorithm 1. Fig. 2 illustrates the detailed system architecture of the PPO algorithm. The main hyperparameters are highlighted in red, including the discount factor (gamma), the learning rates for the actor (Actor_1r) and critic networks (Critic_1r), the number of updates per training iteration (PPO_epoch), and the capacity of the experience replay buffer (buffer_capacity). The key feature of the PPO algorithm is the clipped surrogate objective. In Eq. (2), the first term represents the optimization objective of the TRPO algorithm. The second term truncates the objective function of TRPO, ensuring that $r _ { t } ( \theta )$ always remains within the range [1-ϵ, $\boldsymbol { 1 + \epsilon } ]$ . By selecting the minimum values between the truncated and non-truncated objective functions, the final objective function serves as a lower bound for the non-truncated objective function. This design simplifies the implementation of the PPO algorithm while preserving the stability and correlation of trust region methods, ultimately leading to improved overall performance. In summary, the PPO algorithm represents a significant advancement in the field of RL, and its versatility makes it an indispensable tool for researchers and practitioners alike. 

# 3.2. Merging control module

It is widely recognized that the primary challenge in the on-ramp area arises from the merging of vehicles from the ramp into Lane 2. While ramp vehicles can only commence merging into the mainline after crossing the merging point and entering the acceleration lane, recent studies have demonstrated that cooperative control of CAVs from the mainline and ramp within a certain distance before the merging point can significantly enhance the efficiency and safety of the merging process (Li et al., 2023; Lin et al., 2022; Yang et al., 2023a&b). In the MC module, a set of control methods for Lane 2 and ramp CAVs in the on-ramp area is developed using RL techniques. 

As depicted in Fig. 3, CAVs function as the agents that continually 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/151dcce70981b1cf0cfe80693725ba6286c2cd7b27f90e137a11a7cc946b6109.jpg)



Fig. 3. The process of reinforcement learning.


adapt through their interactions with the surrounding environment. The current state of each CAV is contingent upon its surroundings, and based on this information, the vehicle responds with corresponding actions. These actions, in tandem with the restrictions for vehicles, have a direct impact on the environment. Subsequently, the environment determines the states and rewards for the next iteration. Note that the alterations in the environment during a learning cycle of a CAV are not solely influenced by the individual vehicle under consideration. They are dependent on all vehicles present within the on-ramp area, encompassing both CAVs and HDVs. When multiple CAVs are present in the on-ramp area, each CAV functions simultaneously as an agent and as part of the environment in which other CAVs interact. The RL settings for actions, states, and rewards are outlined as follows. 

# (1) Action space

In the MC module, the PPO agent generates a continuous and bounded variable as its action output, ensuring that the resulting action falls within the interval of $[ \boldsymbol { a } _ { \mathrm { m i n } } , \ : \boldsymbol { a } _ { \mathrm { m a x } } ]$ . In this context, $a _ { \mathrm { m i n } }$ and $a _ { \mathrm { m a x } }$ represent the maximum deceleration and maximum acceleration of the vehicle under normal conditions, respectively. However, it is crucial to emphasize that the actions produced by the PPO agent do not directly translate to the acceleration executed by the vehicle. The final decision regarding the vehicle’s acceleration must still comply with various constraints. For example, if the vehicle’s speed is 0, it is clearly unreasonable for the output action to be negative. Likewise, if the vehicle is in close proximity to the preceding vehicle, further acceleration would pose a safety risk. Thus, the acceleration of the vehicle is determined by a combination of the action taken by the PPO agent and the restrictions imposed by the vehicle dynamics. The vehicle dynamics restrictions 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/caaf0bd7581275e6d917f3b43a8385d8264122231b99a16fd6becb6232339af4.jpg)



Fig. 2. The detailed system architecture of the PPO algorithm.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/222fced2923b2b74066a40b259c7eaf83a45343d70e26d2cd516c00d94df6171.jpg)



Fig. 4. Sketch map of related vehicles in the state definition.


employed in the study will be introduced in Section 4. 

# (2) State space

When configuring the state space, it is crucial to consider various factors associated with action selection. In the MC module, the vehicle’s acceleration primarily depends on the action generated by the PPO agent. Therefore, it is evident that the state space should encompass pertinent information regarding both the subject vehicle and the preceding vehicle. Additionally, given that one of the control objectives is to resolve merging conflicts among vehicles, it is imperative to include information about vehicles from different lanes within the state space. 

As Fig. 4 shows, considering the equal lengths of the three lanes in the on-ramp area, a virtual vehicle, denoted as i’, can be assumed on Lane 2 for the ramp vehicle i, satisfying $x _ { i } , = x _ { i }$ . Here, $x$ represents the position of the subject vehicle, which corresponds to the distance from the entrance of the on-ramp area. The virtual preceding and rear vehicles of ramp vehicle i correspond to the preceding and rear vehicles of vehicle i’ on Lane 2. Similarly, for any Lane 2 vehicle, a virtual vehicle is assumed on the ramp, and its virtual preceding and rear vehicles are determined accordingly. It is crucial to incorporate the information regarding the virtual preceding and rear vehicles into the agent state, considering the potential conflict they may have with the subject vehicle. 

The state of the PPO agent encompasses relevant information about the subject vehicle, preceding vehicle, virtual preceding vehicle, and virtual rear vehicle, as defined below: 

$$
\boldsymbol {S} = \left\{\nu_ {i}, \nu_ {i - 1}, x _ {i - 1} - x _ {i}, \nu_ {k}, x _ {k} - x _ {i}, \nu_ {k + 1}, x _ {i} - x _ {k + 1} \right\} \tag {3}
$$

where i-1 denotes the preceding vehicle. $k$ and $k { + 1 }$ represent the virtual preceding vehicle and virtual rear vehicle, respectively. $\nu$ is the speed of 

# (3) Reward function

As previously mentioned, the cooperative control method presented in this study focuses on two primary objectives: efficiency and safety. Consequently, the reward function of the PPO agent must encompass these fundamental aspects. Efficiency, for instance, can be accurately characterized by the vehicle’s speed: 

$$
R _ {\mathrm {E}} (t) = \nu_ {i} (t + 1) / \nu_ {\max } \tag {4}
$$

where $R _ { \mathrm { E } }$ represents the efficiency-related reward. t represents the current time, while $_ { t + 1 }$ denotes the next time step. 

In terms of safety objectives, it is important to incorporate safety evaluation indicators not only for the subject vehicle and the preceding vehicle but also for the subject vehicle with its virtual preceding and rear vehicles. This is particularly important as a vehicle approaches the merging point, where the ramp vehicle will merge into the mainline, potentially leading to conflicts with its virtual preceding and rear vehicles. By considering these potential conflicts as negative feedback rewards and integrating them into the agent’s learning process, it becomes possible to mitigate such conflicts during the merging process and enhance overall safety. 

In this study, the time-to-collision (TTC) will be employed as a safety evaluation indicator for vehicles. TTC was defined as to measure “the time required for two vehicles to collide if they continue at their present speeds and on the same path” (Hayward, 1972). For the subject vehicle $i ,$ the following indicators are defined: 

$$
T T C _ {i - 1, i} (t) = \frac {\mathbf {x} _ {i - 1} (t) - \mathbf {x} _ {i} (t) - L}{\nu_ {i} (t) - \nu_ {i - 1} (t)} \tag {5}
$$

$$
T T C _ {k, i} (t) = \frac {\mathbf {x} _ {k} (t) - \mathbf {x} _ {i} (t) - L}{\nu_ {i} (t) - \nu_ {k} (t)} \tag {6}
$$

$$
T T C _ {i, k + 1} (t) = \frac {\boldsymbol {x} _ {i} (t) - \boldsymbol {x} _ {k + 1} (t) - L}{\nu_ {k + 1} (t) - \nu_ {i} (t)} \tag {7}
$$

where $T T C _ { i - 1 }$ , $T T C _ { k , \astrosun }$ , $T T C _ { i , k + 1 }$ represent the TTC values of the subject vehicle with its preceding vehicle, virtual preceding vehicle, and virtual rear vehicle, respectively. 

On this basis, the safety-related reward is delineated as follows: 

$$
R _ {\mathrm {S}} (t) = R _ {\mathrm {S} 1} (t) + R _ {\mathrm {S} 2} (t) + R _ {\mathrm {S} 3} (t) \tag {8}
$$

$$
R _ {S 1} (t) = \left\{ \begin{array}{c} - 1, \text {i f} 0 <   T T C _ {i - 1, i} (t + 1) <   T T C ^ {*} \\ 0, \text {e l s e} \end{array} \right. \tag {9}
$$

$$
R _ {S 2} (t) = \left\{ \begin{array}{c} - x _ {i} (t) / L _ {0}, \text {i f} 0 <   T T C _ {k, i} (t + 1) <   T T C ^ {*} \text {o r} x _ {k} (t + 1) - x _ {i} (t + 1) - L <   S _ {0} \\ 0, \text {e l s e} \end{array} \right. \tag {10}
$$

$$
R _ {S 3} (t) = \left\{ \begin{array}{c} - x _ {i} (t) / L _ {0}, \text {i f} 0 <   T T C _ {i, k + 1} (t + 1) <   T T C ^ {*} \text {o r} x _ {i} (t + 1) - x _ {k + 1} (t + 1) - L <   S _ {0} \\ 0, \text {e l s e} \end{array} \right. \tag {11}
$$

# the subject vehicle.

In cases where the subject vehicle lacks preceding vehicle or virtual preceding and rear vehicles within the on-ramp area, the corresponding longitudinal distance is substituted with $2 ^ { \ast } ( L + S _ { 0 } + t _ { \mathrm { H } } { } ^ { \ast } \nu _ { \mathrm { m a x } } ) .$ . The speed of the preceding or virtual preceding vehicle is replaced with $\nu _ { \mathrm { m a x } } .$ , while the speed of the virtual rear vehicle is set to 0. Here, $\nu _ { \mathrm { m a x } }$ represents the maximum speed of the vehicle. $L$ is the vehicle length. $s _ { 0 }$ is the minimum safety distance. $t _ { \mathrm { H } }$ is the desired gap headway of HDVs. 

where $L _ { 0 }$ represents the length of the on-ramp area prior to the merging point. $T T C ^ { * }$ is the TTC threshold value, it is used to delimit whether the current scene is safe. $R _ { S }$ denotes the safety-related reward, comprising three components: RS1, RS2, RS3. RS1 serves as a negative feedback reward for ensuring preceding vehicle safety, while $R _ { S 2 }$ and $R _ { S 3 }$ respectively represent negative feedback rewards for virtual preceding and rear vehicle safety. In $R _ { S 2 }$ and $R _ { S 3 }$ , a negative feedback reward is provided if the value of TTC is less than the designated $T T C ^ { * }$ , or if the vehicle comes in close proximity to the virtual preceding or rear vehicles 

longitudinally. 

Finally, in the MC module, the reward for PPO agent is the sum of the efficiency-related reward and safety-related reward: 

$$
R (t) = R _ {\mathrm {E}} (t) + R _ {\mathrm {S}} (t) \tag {12}
$$

# 3.3. Lane-changing control module

In the on-ramp area, two distinct lane-changing behaviors need to be considered: the merging of ramp vehicles into Lane 2, and the switching of lanes by mainline vehicles between Lane 1 and 2. The former involves a one-way and semi-forced lane change, where ramp vehicles switch lanes when it is safe to do so before reaching the exit of the on-ramp area. Whereas the latter involves a controllable lane change, where CAVs can improve overall traffic efficiency and safety by changing lanes at the appropriate time. Additionally, transitioning from Lane 2 to Lane 1 can reduce conflicts between Lane 2 vehicles and ramp vehicles during merging. The proposed LC module aims to regulate the latter, which is the lane-changing behavior of the mainline CAVs. 

The lane-changing behavior of CAVs should prioritize enhancing the overall efficiency and safety of the traffic system. From a safety perspective, this study has implemented a restriction on lane-changing from Lane 1 to Lane 2 within the on-ramp area for CAVs. This restriction aims to mitigate potential conflicts between vehicles on Lane 2 and those on the ramp. Furthermore, it is crucial to facilitate timely lane changes for CAVs in Lane 2 towards Lane 1. The decision to initiate a lane change can be based on the average speed of vehicles within the respective lane. It is important to note that when calculating the average speed, both Lane 2 vehicles and ramp vehicles should be considered as one unit since they will eventually exit from Lane 2. The formula for calculating the average speed is as follows: 

$$
\bar {\nu} _ {1} (t) = \sum_ {i = 1} ^ {N _ {\mathrm {L} 1}} \left[ \nu_ {i} (t) \right] / N _ {\mathrm {L} 1} \tag {13}
$$

$$
\bar {\nu} _ {2} (t) = \sum_ {i = 1} ^ {N _ {\mathrm {L} 2} + N _ {\mathrm {R}}} \left[ v _ {i} (t) \right] / \left(N _ {\mathrm {L} 2} + N _ {\mathrm {R}}\right) \tag {14}
$$

$$
R _ {S 3} ^ {\prime} (t) = \left\{ \begin{array}{l} - 0. 2, \text {i f} 0 <   T T C _ {i, k + 1} (t + 1) <   T T C ^ {*} \text {o r} x _ {i} (t + 1) - x _ {k + 1} (t + 1) - L <   S _ {0} \\ 0, \text {e l s e} \end{array} \right. \tag {21}
$$

where $\overline { { \nu } } _ { 1 }$ represents the average speed of Lane 1 vehicles. $\overline { { \nu } } _ { 2 }$ represents the average speed of Lane 2 and ramp vehicles. $N _ { \mathrm { L 1 } } , N _ { \mathrm { L 2 } } , N _ { \mathrm { R } }$ respectively represent the number of vehicles on Lane 1, Lane 2, and ramp. 

The vehicles in different lanes display diverse average speeds, suggesting an uneven distribution of traffic. In cases where $\overline { { \nu } } _ { 1 } > { C _ { \mathrm { U } } } ^ { * } \overline { { \nu } } _ { 2 }$ , it becomes essential for the CAVs in Lane 2 to proactively change lanes towards Lane 1, aiming to maintain balanced traffic efficiency across all lanes. Here, $C _ { \mathrm { { U } } }$ is a coefficient with a value greater than 1. Simultaneously, it is of utmost importance for the CAVs to strictly adhere to the lane-changing conditions throughout this procedure, which will be discussed further in Section 4. 

By governing the conduct of Lane 1 vehicles, seamless coordination can be facilitated with those in Lane 2 during lane-changing maneuvers. As such, a control method is devised for the Lane 1 CAVs within the LC module, leveraging RL. The RL settings for actions, states, and rewards are outlined as follows. 

(1) Action space 

In the LC module, the action performed by the PPO agent is identical to those executed in the MC module. The action is a continuous and bounded variable, situated within the interval $[ \boldsymbol { a } _ { \mathrm { m i n } } , \boldsymbol { a } _ { \mathrm { m a x } } ]$ . 

(2) State space 

In the LC module, the state definition of the PPO agent is as follows: 

$$
\boldsymbol {S} ^ {\prime} = \left\{\nu_ {i}, \nu_ {i - 1}, x _ {i - 1} - x _ {i}, \nu_ {k}, x _ {k} - x _ {i}, \nu_ {k + 1}, x _ {i} - x _ {k + 1}, U \right\} \tag {15}
$$

The first seven parameters are consistent with those found in the MC module and pertain to various aspects of the subject vehicle, preceding vehicle, virtual preceding vehicle, and virtual rear vehicle. If the relevant vehicle is absent, the corresponding parameter values remain consistent with those outlined in Section 3.2. In addition, the supple mentary parameter, U, is assigned a value of 1 when $\overline { { \nu } } _ { 1 } > C _ { \mathrm { U } } { } ^ { * } \overline { { \nu } } _ { 2 }$ or a value of 2 otherwise. 

(3) Reward function 

In the LC module, the reward settings are as follows: 

$$
R ^ {\prime} (t) = R _ {\mathrm {E}} ^ {\prime} (t) + R _ {\mathrm {S}} ^ {\prime} (t) \tag {16}
$$

$$
R _ {\mathrm {E}} ^ {\prime} (t) = \nu_ {i} (t + 1) / \nu_ {\max } \tag {17}
$$

$$
R _ {\mathrm {s}} ^ {\prime} (t) = \left\{ \begin{array}{l} R _ {\mathrm {s} 1} ^ {\prime} (t) + R _ {\mathrm {s} 2} ^ {\prime} (t) + R _ {\mathrm {s} 3} ^ {\prime} (t), \text {i f} U = 1 \\ R _ {\mathrm {s} 1} ^ {\prime} (t), \text {e l s e} \end{array} \right. \tag {18}
$$

$$
R _ {\mathrm {S} 1} ^ {\prime} (t) = \left\{ \begin{array}{c} - 1, \text {i f} 0 <   T T C _ {i - 1, i} (t + 1) <   T T C ^ {*} \\ 0, \text {e l s e} \end{array} \right. \tag {19}
$$

$$
R _ {S 2} ^ {\prime} (t) = \left\{ \begin{array}{c} - 0. 2, \text {i f} 0 <   T T C _ {k, i} (t + 1) <   T T C ^ {*} \text {o r} x _ {k} (t + 1) - x _ {i} (t + 1) - L <   S _ {0} \\ 0, \text {e l s e} \end{array} \right. \tag {20}
$$

The differentiation between LC module rewards and MC module rewards resides in the setup of safety-related rewards. In the LC module, the reward is directly associated with the parameter U. When the value of $U$ deviates from 1, the safety-related rewards no longer take into account the negative feedback rewards for virtual preceding and rear vehicle safety. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/c8fe964e72bd1c24b0b4bca04a1c78d48e0915522b86a10d5e821511d79b1705.jpg)



Fig. 5. Car-following behavior of vehicles.


# 4. Simulation experimental design

# 4.1. Modeling human driving vehicles

In a heterogeneous traffic environment, the dual-module cooperative control method is utilized to regulate CAVs. However, to establish a comprehensive simulation experimental framework, it is essential to employ suitable models that accurately depict the driving characteristics of HDVs. This section presents the car-following and lane-changing models utilized in simulation experiments for HDVs. It is important to note that while these models serve as valuable tools for simulation purposes, the proposed control methods are not reliant on them. As the field of traffic flow theory continues to advance, new models may emerge, but this will not hinder the practical application of the proposed control method. 

# 4.1.1. Car-following model

The car-following model describes the interaction between adjacent vehicles within a platoon. As illustrated in Fig. 5, when vehicle ‘i’ follows vehicle ‘i-1′, its driving behavior is influenced by both vehicle ‘i-1′ and its own characteristics. This relationship can be represented using various models. 

The car-following behavior of HDVs can be accurately described by the intelligent driver model (IDM), which was originally proposed by Treiber et al. (2000). The IDM considers the acceleration of the subject vehicle to be influenced by a combination of driving force towards the maximum speed and drag force exerted by the preceding vehicle. Specifically, when analyzing a subject vehicle denoted by a sequence number ‘i’ and a preceding vehicle denoted by a sequence number ‘i-1′, the IDM equation can be expressed as follows: 

$$
\dot {v} _ {i} (t) = a _ {\max } \left[ 1 - \left(\frac {v _ {i} (t)}{v _ {\max }}\right) ^ {4} - \left(\frac {s _ {i} ^ {*} (t)}{s _ {i} (t) - L}\right) ^ {2} \right] \tag {22}
$$

$$
s _ {i} ^ {*} (t) = S _ {0} + t _ {\mathrm {H}} v _ {i} (t) + \frac {\left(v _ {i} (t) - v _ {i - 1} (t)\right) v _ {i} (t)}{2 \sqrt {- a _ {\max} a _ {\min}}} \tag {23}
$$

where $\dot { \nu }$ means the acceleration of the subject vehicle. s means the spacing of the subject vehicle and the preceding vehicle, $s _ { i } ( t ) = x _ { i - 1 } ( t ) .$ - $x _ { i } ( t )$ . 

# 4.1.2. Lane-changing model

When HDVs are traveling on the mainline, drivers often encounter situations where they are dissatisfied with the speed of their current lane and consider changing lanes. This cognitive discontentment regarding driving speed can be mathematically represented, as elucidated by Chen and Wang (2019): 

$$
c _ {i} (t) = \left(v _ {\mathrm {d}} - v _ {i} (t)\right) / v _ {\mathrm {d}} \Delta t \tag {24}
$$

$$
C _ {i} (t) = \sum_ {k = 1} ^ {t} c _ {i} (k) \tag {25}
$$

where $C$ is the cumulative dissatisfaction of the driver. $\nu _ { \mathrm { d } }$ represents the desired speed. Δt denotes the time step. 

Once drivers’ cumulative dissatisfaction with their current lane surpasses the threshold value $( C ^ { * } )$ , they may opt for a lane change. Generally, drivers choose to switch lanes when it enables their vehicle to achieve a higher speed, resulting in two scenarios for lane changes: (1) when the preceding vehicle on the target lane is moving faster than the one on the current lane, and (2) when the preceding vehicle on the target lane is particularly far away. 

Rule 1 illustrates the probability of lane-changing for HDVs when the drivers’ cumulative dissatisfaction with their current lane surpasses $C ^ { * }$ . Here, i-1 denotes the preceding vehicle on the current lane and $k$ denotes the preceding vehicle on the target lane. $\nu ^ { * }$ serves as the speed difference 

threshold for lane-changing, where a certain possibility of changing lanes exists when the speed difference between i-1 and $k$ is less than $\nu ^ { * }$ . If the speed difference between i-1 and $k$ is greater than or equal to $\nu ^ { * }$ , the subject vehicle will opt for lane changing. $L _ { 2 }$ represents the position difference threshold for lane-changing, whereby the subject vehicle will also choose to change lanes if the position difference between i-1 and $k$ exceeds the threshold. Nonetheless, it is crucial for a vehicle to meet the lane-changing conditions, which will be further discussed in Section 4.2, in order to successfully change lanes. 


Rule 1: Probability of lane-changing selection for HDVs


<table><tr><td>if C_i(t) &gt; C*</td></tr><tr><td>if v_k(t) - v_{i-1}(t) ≤ 0</td></tr><tr><td>p = 0</td></tr><tr><td>elif 0 &lt; v_k(t) - v_{i-1}(t) &lt; v*</td></tr><tr><td>p = (v_k(t) - v_{i-1}(t))/v*</td></tr><tr><td>else</td></tr><tr><td>p = 1</td></tr><tr><td>end</td></tr><tr><td>if x_k(t) - x_{i-1}(t) &gt; L_2</td></tr><tr><td>p = 1</td></tr><tr><td>end</td></tr><tr><td>end</td></tr><tr><td>return p</td></tr></table>

# 4.2. Restrictions for vehicles in simulation

# 4.2.1. Restriction of acceleration

As widely acknowledged, the acceleration of a vehicle has a direct impact on its velocity, thereby determining its position. In the simulation, once the acceleration is determined at any given moment, the speed and position of the subject vehicle are promptly adjusted using the following equation: 

$$
v _ {i} (t) = v _ {i} (t - 1) + \dot {v} _ {i} (t - 1) \Delta t \tag {26}
$$

$$
x _ {i} (t) = x _ {i} (t - 1) + \frac {\nu_ {i} (t - 1) + \nu_ {i} (t)}{2} \Delta t \tag {27}
$$

where t-1denotes the previous time step. 

Next, after obtaining the current speed and position, control methods or other models are utilized to determine the vehicle’s acceleration at the present moment. It is crucial to ensure that the vehicle’s speed does not exceed the maximum limit or drop below zero. Furthermore, the acceleration must not surpass the maximum threshold or fall below the maximum deceleration. Therefore, the initially obtained acceleration is subject to the following constraints: 

$$
\dot {v} _ {i} (t) = \min  \left\{a _ {\max }, \dot {v} _ {i} (t), \frac {v _ {\max } - v _ {i} (t)}{\Delta t} \right\} \tag {28}
$$

$$
\dot {v} _ {i} (t) = \max  \left\{a _ {\min }, \dot {v} _ {i} (t), \frac {- v _ {i} (t)}{\Delta t} \right\} \tag {29}
$$

Moreover, when the spacing between the subject vehicle and the preceding vehicle is too close, the vehicle will initiate braking with varying intensity. As explained by Kidd et al. (2023), vehicle braking can 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/9cdf22639bf2540b2a4c9e941adf405a90a9b818dda5928bc0f0abdfb87ad94a.jpg)



Fig. 6. Lane-changing behavior of vehicles.


be classified into two distinct types: forward collision warning and emergency braking. In the former situation, the vehicle will apply the standard maximum deceleration, whereas in the latter scenario, the vehicle will undergo significant deceleration, surpassing the maximum deceleration in conventional scenarios. In their studies, the braking patterns of vehicles are influenced by the TTC indicator, as illustrated in the equation provided below: 

$$
\dot {v} _ {i} (t) = \left\{ \begin{array}{l} a _ {\min }, \text {i f} T T C _ {1} ^ {*} \leq T T C _ {i - 1, i} (t) <   T T C ^ {*} \\ a _ {\mathrm {e m e r}}, \text {i f} T T C _ {i - 1, i} (t) <   T T C _ {1} ^ {*} \\ \dot {v} _ {i} (t), \text {e l s e} \end{array} \right. \tag {30}
$$

where $T T C _ { 1 } { ^ * }$ represents the threshold value used to determine the need for emergency braking, and is set to a value lower than $T T C ^ { * }$ . $a _ { \mathrm { e m e r } }$ is the emergency braking deceleration. 

# 4.2.2. Lane-changing conditions

When it comes to changing lanes, whether it involves the merging of ramp vehicles into Lane 2 or the switching of lanes by mainline vehicles between Lane 1 and 2, it is crucial to adhere to specific conditions. In this study, the TTC serves as an indicator to assess lane change safety. As Fig. 6 shows, for a given vehicle, labeled as “i", intending to switch lanes, the TTC between it with the preceding (labeled as “k") and rear (labeled as $^ { \mathrm { * } } k { + } 1 ^ { \prime \prime } )$ vehicles on the target lane is calculated using Eqs. (6) and (7). Generally, before vehicle i can proceed with the lane change, the following conditions must be satisfied: 


Table 1 Parameter values in the simulation.


<table><tr><td>Parameter</td><td>Value</td><td>Unit</td><td>Parameter</td><td>Value</td><td>Unit</td></tr><tr><td>Δt</td><td>0.1</td><td>s</td><td>L0</td><td>200</td><td>m</td></tr><tr><td>tH</td><td>1.6</td><td>s</td><td>L1</td><td>200</td><td>m</td></tr><tr><td>tA</td><td>1.1</td><td>s</td><td>L2</td><td>40</td><td>m</td></tr><tr><td>tC</td><td>0.6</td><td>s</td><td>a max</td><td>3</td><td>m/s2</td></tr><tr><td>νd</td><td>25</td><td>m/s</td><td>a min</td><td>-3</td><td>m/s2</td></tr><tr><td>νmax</td><td>25</td><td>m/s</td><td>a emer</td><td>-8</td><td>m/s2</td></tr><tr><td>L</td><td>5</td><td>m</td><td>kp</td><td>0.45</td><td>s-1</td></tr><tr><td>S0</td><td>2</td><td>m</td><td>kd</td><td>0.25</td><td>-</td></tr><tr><td>S1</td><td>5</td><td>m</td><td>k1</td><td>0.23</td><td>s-1</td></tr><tr><td>TTC*</td><td>2</td><td>s</td><td>k2</td><td>0.07</td><td>s-2</td></tr><tr><td>TTC1*</td><td>1</td><td>s</td><td>CU</td><td>1.05</td><td></td></tr><tr><td>ν*</td><td>3</td><td>m/s</td><td>C*</td><td>2</td><td>s</td></tr></table>

$$
\boldsymbol {x} _ {k} (t) - \boldsymbol {x} _ {i} (t) > L + S _ {1}
$$

$$
x _ {i} (t) - x _ {k + 1} (t) > L + S _ {1}
$$

$$
T T C _ {k, i} (t) \geq T T C ^ {*} \text {o r} T T C _ {k, i} (t) \leq 0
$$

$$
T T C _ {i, k + 1} (t) \geq T T C ^ {*} \text {o r} T T C _ {i, k + 1} (t) \leq 0
$$

where $s _ { 1 }$ is the minimum distance for lane change. 

# 4.3. Simulation architecture

The simulation flowchart for this study is illustrated in Fig. 7. During the simulation, vehicles enter the on-ramp area randomly, with a 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/20c23679531de8346c6481bc5c20336b18340d6e8820bcbe2bebed36da79cc24.jpg)



Fig. 7. The simulation flowchart.


predetermined flow rate and the penetration rate of CAVs. Within the on-ramp area, different vehicle types exhibit distinct longitudinal acceleration updates and lane-changing behaviors. As agents, CAVs undergo sequential learning at each simulation step or evaluate the effectiveness of agent learning during the testing phase. Throughout the simulation process, all relevant evaluation indicators are recorded. Finally, the average indicators for all exiting vehicles are computed upon completion of the simulation. The RL of agents in the simulation experiments is implemented using the torch library in Python. Table 1 presents the settings for the main simulation parameters. 

Additionally, there are several rules that need be noted with regards to the simulation settings: (1) Given the critical role of decision-making in strategy formulation (Akram and Ahmad, 2023; Akram et al., 2024; Jiang et al., 2024; Liu et al., 2025; Jiang et al., 2025), this study focuses on the decision-making process for vehicle lane-changing rather than the actual execution of the lane changes. Consequently, once the lane-changing conditions are satisfied, the execution of lane-changing in the simulation can be considered completed at a specific time step. (2) It is crucial to emphasize that there are restrictions on vehicles changing lanes within 10 s of completing a lane change. This implies that vehicles entering from the ramp cannot immediately transition to Lane 1 on the mainline right after merging. (3) Furthermore, vehicles are prohibited from changing lanes within $2 0 ~ \mathrm { { m } }$ of the on-ramp area entrance. This restriction is implemented to prevent any disruption to vehicles entering from the entrance. (4) HDVs are expected to abide by the first-in-first-out rule while driving within the acceleration lane and the corresponding section of Lane 2. 

# 4.4. Settings of comparison group

In this study, a comparison group has been established to evaluate the proposed control method. In the comparison group, HDVs follow the same driving rules as the dual-module control group, which are detailed in Section 4.1. However, instead of utilizing the dual-module cooperative control method, the comparison group employs a traditional control strategy for CAVs. Specifically, the lane-changing behavior of CAVs in the comparison group aligns with that of HDVs, as described in Section 4.1. Furthermore, the longitudinal acceleration of CAVs is regulated using PATH cooperative adaptive cruise control (CACC) and adaptive cruise control (ACC) models (Milan´es and Shladover, 2014). 

When the preceding vehicle of the subject CAV is also a CAV, a modified model of PATH CACC can be employed to update the acceleration of the CAV at each time step (Wang et al., 2019; Yang et al., 2023a&b): 

$$
\dot {v} _ {i} (t) = \frac {k _ {\mathrm {p}} \left(s _ {i} (t) - t _ {\mathrm {C}} v _ {i} (t) - L - S _ {0}\right) - k _ {\mathrm {d}} \left(v _ {i} (t) - v _ {i - 1} (t)\right)}{\Delta t + k _ {\mathrm {d}} t _ {\mathrm {C}}} \tag {32}
$$

where $k _ { \mathrm { p } }$ and $k _ { \mathrm { d } }$ are the gains trying to adjust the spacing error with respect to the preceding vehicle. $t _ { \mathrm { C } }$ is the desired gap headway of CACC vehicle. 

When the preceding vehicle of the subject CAV is an HDV, the PATH ACC model is utilized to update its acceleration ( HMilan´es and Shladover, 2014): 

$$
\dot {v} _ {i} (t) = k _ {1} \left(s _ {i} (t) - t _ {\mathrm {A}} v _ {i} (t) - L - S _ {0}\right) - k _ {2} \left(v _ {i} (t) - v _ {i - 1} (t)\right) \tag {33}
$$

where $k _ { 1 }$ and $k _ { 2 }$ are the gains on positioning and speed errors respectively. $t _ { \mathrm { A } }$ is the desired gap headway of ACC vehicle. 

# 4.5. Evaluation indicators

In this study, two parameters are chosen as evaluation indicators to assess the efficacy of the dual-module cooperative control method. These indicators encompass an efficiency-related indicator known as delay, as well as a safety-related indicator referred to as time exposed TTC (TET). The definitions and calculation methods for each parameter 

are provided below. 

# (1) Delay

The equation below is utilized to determine the mean delay of vehicles exiting the on-ramp area during each simulation round: 

$$
\bar {d} = \frac {1}{N _ {\mathrm {E}}} \sum_ {i = 1} ^ {N _ {\mathrm {E}}} \left(\frac {L _ {0} + L _ {1}}{\nu_ {\mathrm {d}}} - \left(T _ {i} ^ {\prime} - T _ {i}\right)\right) \tag {34}
$$

where $N _ { \mathrm { E } }$ is the number of vehicles to exit the on-ramp area in a round. T′ is the time of the subject vehicle to exit the on-ramp area. T is the expected time of the subject vehicle to enter the on-ramp area. 

# (2) TET

The TET concept is derived from the TTC (Minderhoud and Bovy, 2001). TET quantifies the period during which a vehicle remains in an unsafe condition: 

$$
T E T _ {i - 1, i} (t) = \delta_ {t} \times \Delta t, \delta_ {t} = \left\{ \begin{array}{l} 1, \text {i f} 0 <   T T C _ {i - 1, i} (t) <   T T C ^ {*} \\ 0, \text {e l s e} \end{array} \right. \tag {35}
$$

When TET is used to evaluate the safety of merging, it measures the collision risk that a ramp vehicle bears until the merging conditions have been satisfied. This risk arises from both virtual preceding and rear vehicles on Lane 2 of the mainline (Yang et al., 2023b). The calculation method for TET is detailed as follows: 

$$
T E T _ {i} = \sum_ {t = 1} ^ {\text {T i m e}} \max  \left(T E T _ {k, i} (t), T E T _ {i, k + 1} (t)\right) \tag {36}
$$

where Time means the total duration that the subject vehicle spends within the on-ramp area. The average TET value for all ramp vehicles exiting the on-ramp area can be calculated using the following formula: 

$$
\overline {{T E T}} = \frac {1}{N _ {\mathrm {R E}}} \sum_ {i = 1} ^ {N _ {\mathrm {R E}}} T E T _ {i} \tag {37}
$$

where $N _ { \mathrm { R E } }$ is the number of ramp vehicles to exit the on-ramp area. 

# 5. Results and discussions

# 5.1. The learning process of agents

When conducting RL training, two agents were constructed for the MC and LC modules, respectively. These agents were defined based on the actions, states, and rewards specified in Section 3, and trained concurrently. Both agents shared the same hyperparameter settings, with their values during training presented in Table 2. Moreover, the deep neural networks utilized an 8-neuron hidden layer. 

Each training task consisted of 400 simulation rounds, with each round lasting 180 s and a simulation time step size of 0.1 s. All CAVs within the on-ramp area were trained at each time step. The traffic flow rate of Lane 1 was set to 1500 veh/h, while the flow rate of both the ramp and Lane 2 is set to 1000 veh/h. Fig. 8 displays the average reward 


Table 2 Values of the hyperparameters.


<table><tr><td>Hyperparameter</td><td>Description</td><td>Value</td></tr><tr><td>ε</td><td>Clipped parameter</td><td>0.2</td></tr><tr><td>gamma</td><td>Discount factor</td><td>0.99</td></tr><tr><td>actor_lr</td><td>Learning rate for the actor network</td><td>10-4</td></tr><tr><td>critic_lr</td><td>Learning rate for the critic network</td><td>10-4</td></tr><tr><td>PPO_epoch</td><td>Number of updates for PPO agent per training iteration</td><td>5</td></tr><tr><td>buffer_capacity</td><td>Capacity of the experience replay buffer</td><td>3000</td></tr><tr><td>batch_size</td><td>-</td><td>256</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/3527ae1e7f45586700a4d88f2eafb2c118e89a4b07c632e9efdd2f106be7cea9.jpg)



(a)pc=0.1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/e545831922d2bddb06f2536ef792643a73459e34c904744c7b3decbc32c5e89b.jpg)



(c)pc=0.3


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/ce62b6d8cf1306564992124fc62f420b73cfde9bd2b5e2d7f98f5fbf9c29b56e.jpg)



(e)pc=0.5


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/d34a5fa008ca5dcda054d6c442a293028edcdde70c42d6605cb32a13aff929bc.jpg)



(g)pc=0.7


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/a0b1ca0c0447240f50d8b311031fafbbd06f097958ef2b8f385900eec8c859fb.jpg)



(i) pc=0.9


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/ebe7f83d88ae6b9014ec6b1deaf4526a2a73bca1f4f8e8f1b90e233604363681.jpg)



(b)pc=0.2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/186038970c30a2545d192e66cf31580098b21a451ef32fda0367dd18a023c886.jpg)



(d)pc=0.4


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/03cc28eaf856a7f9112bbd352d29f39088396ec607b4eca0fe81fecbe8b0caef.jpg)



(f)pc=0.6


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/b7a6b6494320273a6702dfe86f06da92c96a56b238f2529d9aa7a1a4a0cb7f2d.jpg)



(h)pc=0.8


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/f69eda4a424119d6d6a8b91c1edd8aec4b59596d58f30e6dedd01e415db41189.jpg)



() pc=1.0



Fig. 8. The average reward of each round under different penetration rates of CAVs. $( p _ { \mathrm { { C } } }$ means the penetration rates of CAVs).


of each round under different penetration rates of CAVs. The raw result represents the average value of all rewards in each round, while the smooth result is a smoothed version of the raw result. For example, in the MC module, the calculation method for them is as follows: 

$$
\bar {R} _ {k} = \left(\sum_ {l = 1} ^ {T T i m e _ {k}} R _ {k, l}\right) / T T i m e _ {k}, k = 1, 2 \dots , 4 0 0 \tag {38}
$$

$$
\overline {{R ^ {\prime}}} _ {k} = \left(\sum_ {j = k} ^ {k + 1 9} \sum_ {l = 1} ^ {T T i m e _ {j}} R _ {j, l}\right) / \sum_ {j = k} ^ {k + 1 9} T T i m e _ {j}, k = 1, 2 \dots , 3 8 1 \tag {39}
$$

where $\overline { { R } }$ represents the raw result of the average reward in each round. ${ \overline { { R } } } ^ { \prime }$ denotes the smooth result of the average reward. TTime is the total number of trainings per round. 

As depicted in Fig. 8, both the agents of the MC module and LC module demonstrate convergence across various penetration rates of CAVs. Generally, after training for 100 to 200 episodes, the average reward stabilizes at a maximum level. This suggests that the PPO algorithm exhibits strong convergence properties in this study. Furthermore, a higher penetration rate of CAVs leads to more favorable training outcomes, as evidenced by higher average rewards during convergence and reduced fluctuations. It is important to note that the sequence of vehicle inputs varies in each round. Occasionally, dense vehicle inputs within a short period may result in congestion and consequently lower rewards for training in that specific round. Consequently, the raw results may exhibit significant fluctuations. However, these fluctuations are effectively mitigated through the application of reward result smoothing, indicating successful training of the agents. 

# 5.2. Typical simulation results

This section presents the testing and evaluation of the trained agents introduced in Section 5.1. The testing phase consisted of two groups, including the dual-module control group and the comparison group. Each testing task comprised 100 simulation rounds, each lasting 180 s, with a simulation time step size of 0.1 s. As in the training phase, the traffic flow rate for Lane 1 was set at 1500 veh/h, while the ramp and Lane 2 had a flow rate of 1000 veh/h. 

The results of the relevant evaluation indicators are illustrated in Fig. 9. It is clear that the dual-module control method leads to significantly decreased values of evaluation indicators. Upon examining the evaluation indicator results for each group across various CAV penetration rates, it is evident that at low penetration rates (0.1–0.2), there is a high average delay for vehicles, highlighting a negative impact on traffic efficiency. As the penetration rate increases, the delay decreases, stabilizing at an average of 3–4 s. Furthermore, for both groups, the TET exhibits a consistent decrease with the increase in penetration rate, suggesting that CAVs have the potential to enhance traffic safety in the on-ramp area. 

Table 3 illustrates a comparative analysis of evaluation indicators between the dual-module control group and the comparison group. The findings clearly demonstrate the efficacy of the dual-module cooperative control approach in reducing average vehicle delays. Even at a modest CAV penetration rate of 0.2, there is a remarkable $2 6 ~ \%$ reduction in average vehicle delay. However, as the penetration rate increases (0.9–1), the delay in the comparison group nears its threshold, making further reductions challenging. Regarding safety evaluation, the control method introduced in this study significantly diminishes the average TET value. When the CAV penetration rate exceeds or equals 0.3, the rate of TET reduction reaches approximately $4 5 \ \%$ . Hence, the simulation results strongly indicate that the proposed dual-module cooperative control method effectively enhances both vehicle efficiency and safety within the on-ramp area. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/5a22bdae662c71c7ac492d230ca814ac91768c1a9a0d44e64412db7107e7ace8.jpg)



(a)Delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/cafff7ab36be08a60650d1af464408e261282594230ea3048bc8a247f73efc36.jpg)



(b)TET



Fig. 9. The average results of typical simulation.



Table 3 The decrease rate of evaluation indicators in the dual-module control group compared to the comparison group.


<table><tr><td rowspan="2">Evaluation indicator</td><td colspan="10">Penetration rate of CAVs</td></tr><tr><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td><td>1</td></tr><tr><td>Average delay</td><td>0.17</td><td>0.26</td><td>0.29</td><td>0.28</td><td>0.24</td><td>0.18</td><td>0.13</td><td>0.11</td><td>0.03</td><td>0</td></tr><tr><td>Average TET</td><td>0.17</td><td>0.30</td><td>0.44</td><td>0.45</td><td>0.45</td><td>0.43</td><td>0.44</td><td>0.45</td><td>0.46</td><td>0.49</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/5c9948af08410aded77208a649128cd897c00c3b62dba3a059125e243708ff98.jpg)



Fig. 10. The average delay for vehicles from different lanes.


# 5.3. Classification discussion

# 5.3.1. Discussion for vehicles from different lanes

In this section, 100 rounds of simulation were conducted using the same settings as outlined in Section 5.2. The penetration rate of CAVs in the simulation was also set between 0.1 and 1. The average delay was derived for vehicles from different lanes, as depicted in Fig. 10. It is important to note that a vehicle’s lane affiliation is determined by the lane it enters the on-ramp area from. 

The dual-module control group is found to outperform the comparison group across all lanes, indicating the effectiveness of the proposed control method in optimizing vehicle performance within each lane. Specifically, the average reduction in delay for vehicles in Lane 1 is 16.9 $\%$ , while for Lane 2, it is $2 4 . 9 ~ \%$ , and for ramp vehicles, it is $1 1 . 5 ~ \%$ . Notably, the most significant reduction in delay occurs for vehicles in 

Lane 2, which can be attributed to the effectiveness of the LC and MC modules. The LC module aids mainline CAVs in making informed lanechange decisions, allowing vehicles in Lane 2 ample opportunities to autonomously select their lanes before they need to compete with ramp vehicles for the right of way. This approach has enhanced the traffic efficiency of Lane 2 vehicles. Simultaneously, the MC module takes into account traffic efficiency improvements when coordinating the control of both Lane 2 and ramp vehicles. 

Furthermore, Due to the higher flow rate setting in Lane 1, delays experienced by Lane 1 vehicles are more significant than those of Lane 2 and ramp vehicles. When the penetration rate of CAVs is high, the delays of Lane 1 vehicles in the dual-module control group do not continue to decrease, primarily because of the lane-changing restrictions imposed on CAVs. In the dual-module control group, mainline CAVs are configured to avoid conflicts with ramp vehicles by refraining from changing lanes from Lane 1 to Lane 2. 

# 5.3.2. Discussion for vehicles with different types

In this section, one hundred rounds of simulation were conducted using the same settings as detailed in Section 5.2. The results are presented separately for CAVs and HDVs to assess the proposed control method’s impact on traffic efficiency and safety for different vehicle types. 

Fig. 11 shows the evaluating indicators for vehicles with different types. In terms of average delay, as depicted in Fig. 11(a), it becomes evident that the proposed control method enhances not only the traffic efficiency of CAVs but also significantly improves the traffic efficiency of HDVs. Moreover, it can be observed that the delays of HDVs are slightly greater than those of CAVs. Specifically, CAVs experience an average delay reduction of $2 2 . 7 ~ \%$ , while HDVs see a reduction of $1 5 . 9 ~ \%$ . The proposed dual-module cooperative control method boosts the traffic efficiency of CAVs, which, in turn, positively affects the efficiency of 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/a16b45947b96d8e27ef0490c8314b06bca9629e9618c7b024071baecbae5b00c.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/5bdb2b051fa355ee46413a9c77f0429cc1c5da966a4499d9ac94813693050a65.jpg)



(b)



Fig. 11. The evaluating indicators for vehicles with different types. (a) Average delay, (b) average TET.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/bde5278faa5ca068ac4c1e346445b605b93095322034201cd1b37c2695eff2b1.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/59840387f09228e3ef1797d62dc34b46536b3d2149e5fd18849f7401de2734df.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/7ec4fdb58a4122356a1f188f3086638f3c065f51bff99095cdf0138d11c29ca6.jpg)



（c）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/c39388e9f2ad141608b70b7209fff500eaf979304456ef9b81c0f190dffe396a.jpg)



(d）



Fig. 12. The trajectories of vehicles in a simulation round. (a) and (c) are the results of dual-module control group. (b) and (d) are the results of comparison group.


# HDVs within the transportation system.

Regarding average TET, Fig. 11(b) shows that the difference in TET values between CAVs and HDVs is minimal, with an average decline rate of approximately $4 1 \ \%$ . This suggests that the safety improvements achieved by CAVs extend throughout the entire system, rather than being confined to CAVs alone. 

# 5.4. Vehicle trajectory analysis

This section showcases the recorded vehicle trajectory captured during a simulation round, as depicted in Fig. 12. The simulation settings align with those described in Section 5.2. Within the figure, alterations in line color, or the presence or absence of lines, all denote lane changes made by the vehicles. For instance, in Fig. 12(a) and (b), the transition from a blue to red line signifies the successful merging of the subject ramp vehicle into Lane 2. 

The vehicle trajectories effectively illustrate the underlying reasons behind the notable improvements in efficiency and safety brought about by the proposed cooperative control method. Upon analyzing Fig. 12(b), it becomes evident that within the 40–60 s of the simulation, there is a high influx of vehicles entering Lane 2 and the ramp. This results in conflicts between vehicles from Lane 2 and the ramp during the merging process, leading to congestion. This congestion persists and spreads upstream until approximately 100 s before it subsides. Furthermore, Fig. 12(d) highlights that this conflict spills over into Lane 1 as well. However, as depicted in Fig. 12(a), under the dual-module cooperative control, such congestion does not occur. This can be attributed to two factors. Firstly, prior to reaching the merging point, vehicles on Lane 2 and the ramp engage in cooperative control to ensure a safe distance between them, leading to fewer merging conflicts and enabling ramp vehicles to merge into the mainline earlier. Secondly, some CAVs on Lane 2 anticipate potential conflicts with ramp vehicles and proactively 

switch to Lane 1, effectively mitigating potential congestion. These factors significantly enhance traffic efficiency and safety, as confirmed by the comprehensive evaluation indicators. In this simulation round, the dual-module control group experiences an average delay of $2 . 3 8 \ s _ { \mathrm { { \scriptsize ~ { ~ \alpha ~ } } } }$ , with a TET of 0.41 s. Conversely, the comparison group encounters an average delay of up to 3.71 s, with a TET of 1.63 s. 

# 5.5. Transferability analysis of reinforcement learning

In this section, modifications are made to specific settings within the training environment for RL agents to establish different testing environments. Subsequently, simulations are conducted across diverse testing scenarios. This process evaluates the transferability of RL within traffic environments. Adjustments are implemented on several parameters, including the penetration rate of CAVs, the maximum speed of vehicles, and the traffic flow rate, to facilitate this evaluation. 

# 5.5.1. The penetration rate of CAVs

Considering the evolving landscape of CAVs, it’s projected that roads will witness a diverse mix of traffic for a considerable time ahead. The penetration rate of CAVs emerges as a pivotal factor influencing this heterogeneous traffic scenario. This section delves into the transferability of agents, initially trained as per Section 5.1, across varying penetration rates relative to their original training conditions. To this end, five distinct groups were established for simulation studies, comprising a comparison group alongside four dual-module control groups. Specifically, in dual-module control group 1.1, akin to earlier sections, the evaluation at each penetration rate was performed using agents tailored to that specific penetration rate. Meanwhile, dualmodule control group 1.2 engaged in all tests with agents trained at penetration rates of 0.3. Similarly, dual-module control groups 1.3 and 1.4 utilized agents trained at penetration rates of 0.5 and 0.7, respectively. 

The simulation’s additional parameters were aligned with those detailed in Section 5.2. Across the board, 100 rounds of simulations were executed, with the performance indicators for all groups illustrated in Fig. 13. The analysis reveals that, in terms of TET, each dual-module control group outperformed the comparison group. However, when examining delays, groups 1.1, 1.3, and 1.4 demonstrate superior optimization effects. Among these, groups 1.1 and 1.4 stand out as the most effective. Conversely, group 1.2 exhibited subpar control effect when faced with high penetration rates. This observation underscores that the 

agents trained in high penetration rate settings also excel in low penetration rate scenarios, whereas those trained under low penetration rate conditions struggle to achieve comparable optimization in the high penetration rate environments. Consequently, for heterogeneous traffic flows, prioritizing the training of agents at higher penetration rates is advisable for optimal performance. 

# 5.5.2. The maximum speed

This section delves into the influence of varying maximum speeds on the efficacy of agent testing. To investigate this, the agents underwent training within environments designated with maximum speeds ranging from 22 to $2 7 ~ \mathrm { { m } } / s$ . Within these training settings, the penetration rate for CAVs was set at 0.5, with all other parameters aligning with those outlined in Section 5.1. Four distinct groups were established for simulation testing. In the context of dual-module control, group 2.1 engaged in simulations at each specified maximum speed using agents trained in those exact speeds. Meanwhile, groups 2.2 and 2.3 engaged in all tests using agents trained at maximum speed of $2 3 \mathrm { m } / s$ and $2 5 \mathrm { m } / s$ , respectively. 

Following a series of tests containing 100 simulation rounds, the outcomes for each evaluative indicators were compiled, as presented in Fig. 14. The analysis reveals that, relative to the baseline comparison group, each dual-module control group demonstrated notable optimization benefits. This suggests that the agents are capable of maintaining effective control even amidst variations in maximum speed settings. Moreover, a comparative review of the performance indicators across different groups under varied maximum speed conditions indicates that while an increase in maximum speed tends to reduce vehicle transit times, it does not markedly affect vehicle delay times. 

# 5.5.3. The total flow rate

This section evaluates the optimization performance of the agents trained in Section 5.1, across varying traffic flow rate conditions. During the simulations, the total traffic flow rate was set to range between 2450 and 4200 vehicles per hour. The distribution of the flow rate across the lanes was configured as follows: Lane 1 to Lane 2 to the ramp at a ratio of 1.5:1:1. A comprehensive series of 100 simulation tests were conducted, maintaining consistency with the parameters outlined in Section 5.2 for all other simulation settings. The average outcomes of various evaluation indicators are depicted in Fig. 15. It is observed that an increase in the flow rate leads to a corresponding rise in both the average delay and the TET of vehicles. More critically, the findings reveal that, irrespective 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/a1d7aacb424d12d863db308a14ca5be1301f1c079437d8c96eb4aee6c4acd11f.jpg)



(a) Average delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/4119c60703738cade0b07e1ef3153f345420520118accc4cd38ebd2d86b24e2f.jpg)



(b) Average TET



Fig. 13. The simulation results of the evaluation indicators in dual-module control group 1.1–1.4 compared to the comparison group.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/c72f554f36ce95260b6212a6d461e2433ee010443320d6403ad0fd6b3ae717bd.jpg)



(a) Average delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/a3db1f58bcfc58f578e562beea8db81bb991864af6b12fca96440dd9e11ab43f.jpg)



(b) Average TET



Fig. 14. The simulation results of the evaluation indicators in dual-module control group 2.1–2.3 compared to the comparison group.


of the flow rate, the control strategy proposed in this paper significantly reduces both the average delay and TET for vehicles in the on-ramp area. This underscores the robust transferability of RL techniques in adapting to changes in traffic flow rates. 

# 5.5.4. The flow rate ratio

This section evaluates the optimization performance of the agents trained in Section 5.1 under varying traffic flow rate ratios. The flow rate ratio is defined as the proportion of the mainline’s flow rate to that of the ramp, with the mainline flow rate being the total of the flow rates from Lane 1 and Lane 2. During the simulations, the overall flow rate was held constant at 3500 vehicles per hour, with equal flow rates for Lane 1 and Lane 2. A comprehensive series of 100 simulation tests was conducted, following the parameters outlined in Section 5.2 for all other simulation settings. 

The average results for various evaluation indicators are shown in Fig. 16. It is clear that, across different flow rate ratios, the delay and TET values for the dual-module control group are lower than those of the comparison group. This indicates that the dual-module cooperative control method remains effective even as traffic conditions change. Moreover, at lower penetration rates of CAVs, when the flow rate ratio is low, both delay and TET for vehicles tend to increase. This is attributed to the fact that a relatively low flow rate ratio results in a higher ramp flow rate, leading to more vehicle merging conflicts. 

# 5.5.5. The length of the control area

This section examines the performance of the dual-module cooperative control method as the length of the control area varies. In the simulation, we adjusted the length of the control area by changing the length of the on-ramp area prior to the merging point $\left( L _ { 0 } \right)$ . The flow rate for Lane 1 was set at 1500 veh/h, while the flow rates for Lane 2 and the ramp were both set at 1000 veh/h. A comprehensive series of 100 simulation tests was conducted, adhering to the parameters outlined in Section 5.2 for all other settings. 

The average results for various evaluation indicators are presented in Fig. 17. It is evident that, in all cases, the delay and TET values for the dual-module control group are lower than those of the comparison group. This suggests that the effectiveness of the dual-module cooperative control method remains consistent despite changes in $L _ { 0 }$ . Furthermore, there is no significant correlation between $L _ { 0 }$ with TET and delay values, indicating that a superior control effect can be achieved without extending the length of the control area. 

# 5.6. Comparative study

This section conducts a comparative study between the method proposed in this research and the existing method identified in the study by Yang et al. (2023b). The existing method employs gap selection control for vehicles in heterogeneous traffic flow. Consequently, the simulation results derived from this method are referred to as the “gap selection control group." 

The simulation environment of this section aligns with the settings outlined in Section 5.2. In this environment, 100 simulation rounds were conducted for three groups: the comparison group, the dual-module control group, and the gap selection control group, across CAV penetration rates ranging from 0.1 to 1. The simulation results are illustrated in Fig. 18. 

Regarding average delay, Fig. 18 (a) and (b) reveal that the dualmodule control group significantly reduces vehicle delay compared to the comparison group. In contrast, the gap selection control group shows limited effectiveness in this regard. This disparity arises because the method proposed in this study comprehensively addresses both the efficiency and safety conditions of traffic flow, whereas the gap selection control group does not prioritize efficiency improvements. 

The safety aspects of the merging process are presented in Fig. 18(c) and (d). It is evident that at low CAV penetration rates $_ { ( < 0 . 6 ) }$ , the average TET for the dual-module control group is lower than that of the gap selection control group. However, at higher penetration rates, the gap selection control group outperforms the dual-module control group in reducing average TET. 

Overall, the method proposed in this study demonstrates significant advantages in enhancing traffic efficiency compared to the approach by Yang et al. (2023b). Additionally, in terms of safety during the merging process, this method shows superior performance at low CAV penetration rates $_ { ( < 0 . 6 ) }$ . Therefore, the dual-module cooperative control method proposed in this study is highly competitive, particularly in scenarios with low CAV penetration rates. 

# 6. Conclusions, limitations and future works

# 6.1. Conclusions

In this paper, a cooperative control method utilizing RL is proposed for vehicles in the on-ramp area. Initially, an on-ramp scenario featuring multiple lanes is introduced, outlining the control objective of 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/0d45dc53abec98b33238842b42249fabf4c26903d0fe68860f9cf55f397418dc.jpg)



(a) Delay of dual-module control group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/5b7fb5bd3e9e6fa614a7120fb955446005669547debd215dae7b8a4d8109db65.jpg)



(b) Delay of comparison group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/572442e6c27175791c77c7a61b846c038ab8f86e0dba4f13b36213c987e559ec.jpg)



(c) TET of dual-module control group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/b1e890f8ac773c0dcd0e4a2c81c37feaefad9fdc86c1363278f29f5dbdbf22d7.jpg)



(d) TET of comparison group



Fig. 15. The average results of various evaluation indicators in simulation with different flow rates.


enhancing traffic efficiency and safety in a CAV-HDV heterogeneous traffic flow environment. Subsequently, a dual-module cooperative control approach is presented, comprising the MC module and the LC module. The MC module orchestrate cooperative control among Lane 2 vehicles and ramp vehicles. While the LC module assists mainline CAVs in making informed lane change decisions. Additionally, it governs the behavior of Lane 1 vehicles to ensure seamless coordination during lanechanging maneuvers with those in Lane 2. To achieve the objectives of enhancing efficiency and safety, suitable actions, states, and rewards are defined for the agents of both modules, with the PPO RL algorithm employed for training purposes. Ultimately, the control decisions for CAVs emerge from a synergy between the agent’s selected actions and foundational traffic regulations, resulting in a control strategy that is not only innovative but also highly reliable and adaptable to real-world scenarios. 

A simulation experimental framework was developed, along with the establishment of a comparison group to assess the optimization impact of the control method. During the simulation, vehicles enter the on-ramp area randomly and adhere to the specific flow rate and penetration rates of CAVs. PPO agents were trained within this framework. The training results indicate that the algorithm exhibits strong convergence properties, with the agents’ average rewards stabilizing at their maximum level after 100 to 200 training episodes. 

The simulation results demonstrate that the dual-module control method significantly enhances traffic efficiency and safety in the onramp area. This control strategy is particularly well-suited for CAV-HDV heterogeneous traffic flow scenarios and can also yield positive results at lower CAV penetration rates. Even at a modest CAV penetration rate of 0.2, there is a notable $2 6 ~ \%$ reduction in average vehicle delay. Furthermore, in terms of safety, when the CAV penetration rate 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/704cd933adb383a7361d58f626e389468ee327fc6aff6ffd6c553afc810c97be.jpg)



(a) Delay of dual-module control group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/fcc4a83ceb67cbd4b03c88ecdf2f0282bf15bd039979b328028b54446a844bb4.jpg)



(b) Delay of comparison group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/ddae2e21cf77c8b2df5e529c8b6af3d832f5d737a1f0b3c251a359362351e246.jpg)



(c) TET of dual-module control group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/57a3084ed2a872db33db7d26f4c832efdeeaf707fda10dd386dcd1c98316c104.jpg)



(d) TET of comparison group



Fig. 16. The average results of various evaluation indicators in simulation with different flow rate ratios.


exceeds or equals 0.3, the reduction rate of TET reaches approximately $4 5 \ \%$ . 

The dual-module control method improves the performance of vehicles in each lane, benefiting not only CAVs but also enhancing the efficiency and safety of HDVs. Transferability analysis indicates that employing RL agents in the control strategy yields positive effects across different maximum speeds and flow rates. In heterogeneous traffic environments, agent training is recommended at high CAV penetration rates. The comparative study further demonstrate that the proposed method significantly enhances traffic efficiency and safety, showcasing excellent performance even at lower CAV penetration rates. 

# 6.2. Limitations

While this study offers valuable insights, it also acknowledges certain 

limitations. Specifically, the current practical implementation of cooperative control methods for CAVs faces challenges across multiple dimensions, including technical, infrastructure, legal, and social acceptance levels. 

Technical level: Real-time communication among CAVs encounters significant hurdles, primarily dependent on advancements in mobile communication technology. Furthermore, network security threats, including data privacy concerns, pose critical challenges for CAVs. Ensuring the security and reliability of vehicle systems is essential, necessitating the establishment of multi-tiered network security measures. Additionally, the intelligent perception technology of CAVs requires enhancement; improving accuracy and precision in environmental perception necessitates integrating various sensors—such as LiDAR, cameras—alongside data fusion techniques. 

Infrastructure level: Existing roadways and transportation 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/159494b66d2814c80fe47c19ca3758a732868e467eba85fdfac67a0c040975bb.jpg)



(a) Delay of dual-module control group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/8758df5a03d14bb9a385edf807b1deb00c819827488ba7fdf5d1b7df16c6714a.jpg)



(b) Delay of comparison group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/a0f8b370d8d11427e4ab7d8402bf4300f83c12c5d7afea24d71e3f25563a8a16.jpg)



(c) TET of dual-module control group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/506dca46ef57efc1db6b93cea22eccdfc9decaf5fa30749eeb11180e668cec20.jpg)



(d) TET of comparison group



Fig. 17. The average results of various evaluation indicators in simulation with different lengths of the control area.


infrastructure often fail to meet the specific needs of CAVs, lacking the capacity for cooperative interactions among vehicles, between vehicles and roadways, and with cloud services. This situation underscores the urgent need for increased investment in intelligent transportation infrastructure to elevate the overall intelligence of the transportation network. Moreover, the absence of effective data-sharing platforms has resulted in significant information silos among various transportation stakeholders. Therefore, developing a unified data-sharing platform is essential to facilitate information exchange among these participants. 

Legal level: Current laws and regulations frequently fall short in adequately addressing the unique characteristics of CAVs. The disparities in technical standards and regulations across different regions and countries pose challenges for collaborative control on a cross-regional basis. To address this issue, it is imperative for governments to collaborate with industry stakeholders to establish regulations and standards 

that align with practical needs while ensuring timely updates. Additionally, active participation in the development of international standards is necessary to foster technical exchange and cooperation among nations, thereby promoting standardization. 

Social acceptance level: Public skepticism regarding the safety and privacy of intelligent connected vehicles persists among some community members. To mitigate these concerns, it is vital to promote the advantages, safety features, and underlying technical principles of CAVs through various channels, thereby enhancing public awareness and acceptance. Furthermore, the evolution of intelligent networking technology may disrupt traditional transportation professions, potentially eliciting social responses. Consequently, it is crucial for society to provide training and support for the transformation of affected professions, aiding them in adapting to the new work environment. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/46f74fa4dc548a97e4af528430c412ff4ab3f9e506b964d74cd364a2f7ead9b1.jpg)



(a) Average delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/521b8e46788fecd76e4e2104e53a3b8775d7426fd29e7cb75e90267ee56ca240.jpg)



(b) Decrease rate of average delay


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/90b3cd9dcd9d509981ec97eb291b1fd9e6a7cc4f011f3277204f7b02a1d0cfd8.jpg)



(c) Average TET


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-29/638e591c-10a5-4b4d-9f7f-09b6935828fd/c7662173c271b920bd7a4379df1e47b703f35ec737a13338b945cab84ff19560.jpg)



(d) Decrease rate of average TET



Fig. 18. The simulation results of the dual-module control group compared to the existing method.


# 6.3. Future works

Future research will focus on the following key directions to further deepen and expand the current achievements in this area: 

(1) This study proposes a cooperative control method for CAVs based on reinforcement learning. However, the current research does not address higher-level vehicle right-of-way allocation, which is crucial for optimizing traffic flow in complex environments. Effective allocation of road rights remains a key issue that needs urgent attention. Moreover, the introduction of dedicated CAV lanes may influence vehicle behavior, potentially impacting onramp environments. Therefore, future research will delve deeper into these aspects to enhance the depth and applicability of cooperative control methods. 

(2) As discussed in Section 6.2, there are significant challenges in conducting real-world experiments for CAVs. Due to these 

challenges, this study has primarily relied on simulation methods to verify and evaluate the proposed control method. While simulations are valuable, they may not fully capture the complexities of real-world traffic scenarios. In future work, we plan to gradually transition to practical experiments. Initially, these could involve virtual reality technology and driving simulators, offering a safe testing environment while allowing for controlled observation of vehicle behavior in CAV-HDV heterogeneous traffic flow. As the research progresses, we aim to conduct on-site vehicle control experiments in specific, enclosed settings under safe conditions, in order to more comprehensively assess the applicability and effectiveness of our cooperative control method in real-world contexts. These efforts will contribute to building a stronger empirical foundation and provide theoretical support for advancing the research on CAV cooperative control. 

# CRediT authorship contribution statement

Wenzhang Yang: Writing – review & editing, Writing – original draft, Software, Methodology, Formal analysis, Conceptualization. Changyin Dong: Writing – review & editing, Supervision, Methodology, Funding acquisition. Ziqian Zhang: Writing – review & editing, Formal analysis. Xu Chen: Writing – review & editing, Formal analysis, Conceptualization. Hao Wang: Writing – review & editing, Supervision, Methodology, Funding acquisition, Conceptualization. 

# Notations


The following symbols are used in this paper:


<table><tr><td>A</td><td>= action of reinforcement learning</td></tr><tr><td>a max</td><td>= maximum acceleration of vehicles</td></tr><tr><td>a min</td><td>= maximum deceleration of vehicles</td></tr><tr><td>A t</td><td>= estimator of the advantage function at timestep t</td></tr><tr><td>C</td><td>= cumulative dissatisfaction of the driver</td></tr><tr><td>C*</td><td>= threshold value of C</td></tr><tr><td>C U</td><td>= a coefficient with a value greater than 1</td></tr><tr><td>d</td><td>= average delay</td></tr><tr><td>Δt</td><td>= time step</td></tr><tr><td>ε</td><td>= a hyperparameter</td></tr><tr><td>i</td><td>= subject vehicle, while i-1 represents preceding vehicle</td></tr><tr><td>i&#x27;</td><td>= virtual vehicle</td></tr><tr><td>k</td><td>= virtual preceding vehicle, while k+1 represents virtual rear vehicle</td></tr><tr><td>k1</td><td>= parameter in PATH ACC model</td></tr><tr><td>k2</td><td>= parameter in PATH ACC model</td></tr><tr><td>kd</td><td>= parameter in PATH CACC model</td></tr><tr><td>kp</td><td>= parameter in PATH CACC model</td></tr><tr><td>L</td><td>= vehicle length</td></tr><tr><td>L0</td><td>= length of the on-ramp area prior to the merging point</td></tr><tr><td>L1</td><td>= length of the acceleration lane</td></tr><tr><td>L2</td><td>= position difference threshold for lane-changing</td></tr><tr><td>NE</td><td>= number of vehicles to exit the on-ramp area in a round</td></tr><tr><td>NL1</td><td>= number of vehicles on Lane 1</td></tr><tr><td>NL2</td><td>= number of vehicles on Lane 2</td></tr><tr><td>NR</td><td>= number of vehicles on ramp</td></tr><tr><td>NRE</td><td>= number of ramp vehicles to exit the on-ramp area</td></tr><tr><td>πθ</td><td>= stochastic policy</td></tr><tr><td>pC</td><td>= penetration rate of CAVs</td></tr><tr><td>R</td><td>= reward of reinforcement learning</td></tr><tr><td>R</td><td>= raw result of the average reward in each round</td></tr><tr><td>R&#x27;</td><td>= smooth result of the average reward</td></tr><tr><td>RE</td><td>= efficiency-related reward</td></tr><tr><td>RS</td><td>= safety-related reward</td></tr><tr><td>r1(θ)</td><td>= simplified notation for probability ratio</td></tr><tr><td>s</td><td>= spacing headway of the subject vehicle</td></tr><tr><td>S</td><td>= state of reinforcement learning</td></tr><tr><td>S0</td><td>= minimum safety distance</td></tr><tr><td>S1</td><td>= minimum distance for lane change</td></tr><tr><td>t</td><td>= current time</td></tr><tr><td>T</td><td>= expected time of the subject vehicle to enter the on-ramp area</td></tr><tr><td>T&#x27;</td><td>= time of the subject vehicle to exit the on-ramp area</td></tr><tr><td>tA</td><td>= desired gap headway of ACC vehicle</td></tr><tr><td>tC</td><td>= desired gap headway of CACC vehicle</td></tr><tr><td>TET</td><td>= time exposed TTC</td></tr><tr><td>tH</td><td>= desired gap headway of HDVs</td></tr><tr><td>θold</td><td>= vector of policy parameters prior to any updates</td></tr><tr><td>Time</td><td>= total duration that the subject vehicle spends within the on-ramp area</td></tr><tr><td>TTC</td><td>= time-to-collision</td></tr><tr><td>TTC*</td><td>= TTC threshold value</td></tr><tr><td>TTC1*</td><td>= threshold value used to determine the need for emergency braking</td></tr><tr><td>TTime</td><td>= total number of trainings per round</td></tr><tr><td>U</td><td>= a parameter in the state of LC module</td></tr><tr><td>v</td><td>= speed of the subject vehicle</td></tr><tr><td>dot</td><td>= acceleration of the subject vehicle</td></tr><tr><td>v1</td><td>= average speed of Lane 1 vehicles</td></tr><tr><td>v2</td><td>= average speed of Lane 2 and ramp vehicles</td></tr><tr><td>vd</td><td>= desired speed</td></tr><tr><td>vmax</td><td>= maximum speed of vehicles</td></tr><tr><td>x</td><td>= position of the subject vehicle</td></tr></table>

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Acknowledgements

This work was sponsored by the National Key Research and Development Program of China (No. 2022ZD0115600), the National Natural Science Foundation of China (No.52072067, 52302405), the Natural Science Foundation of Jiangsu Province (No. BK20210249), the SEU Innovation Capability Enhancement Plan for Doctoral Students (CXJH_SEU 24178), the Postgraduate Research & Practice Innovation Program of Jiangsu Province (KYCX24_0451), and Postdoctoral Fellowship Program of CPSF (No. GZC20230431). 

# Data availability

Data will be made available on request. 

# References



Akram, Z., Ahmad, U., 2023. A multi-criteria group decision-making method based on fuzzy rough number for optimal water supply strategy. Soft Comput. https://doi. org/10.1007/s00500-023-08942-y. 





Akram, Z., Ahmad, U., Alcantud, J.C.R., 2024. Multi-criteria decision-making for the selection of best airport ground access mode with a new fuzzy rough-entropy based method. Eng. Appl. Artif. Intell. 135, 108843. 





Atagoziev, M., Schmidt, E.G., Schmidt, K.W., 2023. Lane change scheduling for connected and autonomous vehicles. Transport. Res. C Emerg. Technol. 147, 103985. 





Chen, X., Dong, C., Yang, W., Hou, Y., Wang, H., 2024b. Platoon control and external human-machine interfaces: innovations in pedestrian-autonomous vehicle interactions. Transportmetr. A: Transp. Sci. 20, 1–32. 





Chen, X., Li, X., Hou, Y., Yang, W., Dong, C., Wang, H., 2025. Effect of eHMI-equipped automated vehicles on pedestrian crossing behavior and safety: A focus on blind spot scenarios. Accid. Anal. Prevent. 212, 107915. 





Chen, X., Li, S., Yang, W., Chen, Y., Wang, H., 2024a. Enhanced microsimulation framework for right-turning vehicle-pedestrian interactions at signalized intersection. Simulat. Model. Pract. Theory 134, 102930. 





Chen, H., Wang, J., 2019. A decision-making method for lane changes of automated vehicles on freeways based on driver’s dissatisfaction. China J. Highw. Transp. 32 (12), 1–9&45. 





Chen, T., Wang, M., Gong, S., Zhou, Y., Ran, B., 2021. Connected and automated vehicle distributed control for on-ramp merging scenario: a virtual rotation approach. Transport. Res. C Emerg. Technol. 133, 103451. 





Chen, X., Wu, Z., Liang, Y., 2023. Modeling mixed traffic flow with connected autonomous vehicles and human-Driven vehicles in off-ramp diverging areas. Sustainability 15 (7), 5651. 





Chen, J., Zhou, Y., Chung, E., 2024. An integrated approach to optimal merging sequence generation and trajectory planning of connected automated vehicles for freeway onramp merging sections. IEEE Trans. Intell. Transport. Syst. 25 (2), 1897–1912. 





Ding, H., Di, Y., Zheng, X., Bai, H., Zhang, W., 2021. Automated cooperative control of multilane freeway merging areas in connected and autonomous vehicle environments. Transportmetrica B: Trans. Dynam. 9 (1), 437–455. 





Dong, C., Wang, H., Wang, W., Li, Y., Hua, X., 2018. Hybrid traffic flow model for intelligent vehicles exiting to off-ramp. Acta Phys. Sin. 67 (14), 144501. 





Dong, C., Li, Y., Wang, H., Tu, R., Chen, Y., Ni, D., Liu, Y., 2023. Lane-changing trajectory control strategy on fuel consumption in an iterative learning framework. Expert Syst. Appl. 228, 120251. 





Fang, Y., Min, H., Wu, X., Wang, W., Zhao, X., Mao, G., 2022. On-Ramp merging strategies of connected and automated vehicles considering communication delay. IEEE Trans. Intell. Transport. Syst. 23 (9), 15298–15312. 





Gao, H., Jia, H., Huang, Q., Wu, R., Tian, J., Wang, G., Liu, C., 2024a. A hybrid deep learning model for urban expressway lane-level mixed traffic flow prediction. Eng. Appl. Artif. Intell. 133 (Part B), 108242. 





Gao, Z., Yu, T., Gao, F., Zhao, R., Sun, T., 2024b. Human-like mechanism deep learning model for longitudinal motion control of autonomous vehicles. Eng. Appl. Artif. Intell. 133 (Part A), 108060. 





Gokasar, I., Simic, V., Deveci, M., Senapati, T., 2023. Alternative prioritization of freeway incident management using autonomous vehicles in mixed traffic using a type-2 neutrosophic number based decision support system. Eng. Appl. Artif. Intell. 123 (Part A), 106183. 





Greguri´c, M., Kuˇsi´c, K., Ivanjko, E., 2022. Impact of deep reinforcement learning on variable speed limit strategies in connected vehicles environments. Eng. Appl. Artif. Intell. 112, 104850. 





Han, Y., Wang, M., Li, L., Roncoli, C., Gao, J., Liu, P., 2022. A physics-informed reinforcement learning-based strategy for local and coordinated ramp metering. Transport. Res. C Emerg. Technol. 137, 103584. 





Han, L., Zhang, L., Guo, W., 2023. Multilane freeway merging control via trajectory optimization in a mixed traffic environment. IET Intell. Transp. Syst. 17, 1891–1907. 





Hayward, J.C., 1972. Near-miss determination through use of a scale of danger. Highw. Res. Rec. 384, 24–385. 





He, X., Lou, B., Yang, H., Lv, C., 2023. Robust decision making for autonomous vehicles at highway on-ramps: a constrained adversarial reinforcement learning approach. IEEE Trans. Intell. Transport. Syst. 24 (4), 4103–4113. 





Hou, K., Zheng, F., Liu, X., Guo, G., 2023. Cooperative on-Ramp merging control model for mixed traffic on multi-lane freeways. IEEE Trans. Intell. Transport. Syst. 24 (10), 10774–10790. 





Hua, W., Zhou, F.Y., Chen, J.H., 2009. The effects of offsetting and wedging cell lattices in the on-ramp system. Int. J. Mod. Phys. C 20 (7), 1039–1047. 





Ji, K., Li, N., Orsag, M., Han, K., 2023. Hierarchical and game-theoretic decision-making for connected and automated vehicles in overtaking scenarios. Transport. Res. C Emerg. Technol. 150, 104109. 





Jia, B., Jiang, R., Wu, Q.S., 2005. The effects of accelerating lane in the on-ramp system. Phys. Stat. Mech. Appl. 345 (1–2), 218–226. 





Jiang, Y., Man, Z., Wang, Y., Yao, Z., 2024. Cooperative lane-changing for connected autonomous vehicles merging into dedicated lanes in mixed traffic flow. Expert Syst. Appl. 252 (Part A), 124163. 





Jiang, L., Moln´ar, T.G., Orosz, G., 2021. On the deployment of V2X roadside units for traffic prediction. Transport. Res. C Emerg. Technol. 129, 103238. 





Jiang, S., Sun, Y., Wong, W., Xu, Y., Zhao, X., 2024. Real-time urban traffic monitoring using transit buses as probes. Transport. Res. Rec. 1–18. 





Jiang, S., Zhang, X., Liang, Y., Wong, W., Park, S., Zhao, X, 2025. Examining the shortterm causal impact of evacuation orders on traffic speed: evidence from Hurricane Ian. Available at SSRN 5118520. 





Jing, S., Hui, F., Zhao, X., Rios-Torres, J., Khattak, A.J., 2022. Integrated longitudinal and lateral hierarchical control of cooperative merging of connected and automated vehicles at on-ramps. IEEE Trans. Intell. Transport. Syst. 23 (12), 24248–24262. 





Kakade, S., Langford, J., 2002. Approximately optimal approximate reinforcement learning. Intern. Confer. Mach. Learning 2, 267–274. 





Kidd, D.G., Perez-Rapela, D., Jermakian, J.S., 2023. Characteristics of automatic emergency braking responses in passenger vehicles evaluated in the IIHS front crash prevention program. Accid. Anal. Prev. 190, 107150. 





Lee, C., Hellinga, B., Ozbay, K., 2006. Quantifying effects of ramp metering on freeway safety. Accid. Anal. Prev. 38 (2), 279–288. 





Li, F., Zhang, X.Y., Gao, Z.Y., 2007. The effect of restricted velocity in the two-lane onramp system. Phys. Stat. Mech. Appl. 374 (2), 827–834. 





Li, M., Li, Z., Zhou, Y., Wu, J., 2022. A cooperative energy efficient truck platoon lanechanging model preventing platoon decoupling in a mixed traffic environment. J. Intelligent Transp. Syst. 28 (2), 174–188. 





Li, M., Li, Z., Wang, S., Zheng, S., 2023. Enhancing cooperation of vehicle merging control in heavy traffic using communication-based soft actor-critic algorithm. IEEE Trans. Intell. Transport. Syst. 24 (6), 6491–6506. 





Li, L., Zhao, W., Wang, C., Fotouhi, A., Liu, X., 2024a. Nash double Q-based multi-agent deep reinforcement learning for interactive merging strategy in mixed traffic. Expert Syst. Appl. 237 (Part B), 121458. 





Li, W., Ding, H., Xu, N., Song, Z., Zhang, J., 2024b. A time and energy efficient merging control for platoon formation of connected and automated electric vehicles at onramps. Nonlinear Dyn. 112, 3619–3642. 





Li, L., Qian, C., Gan, J., Zhang, D., Qu, X., Xiao, F., Ran, B., 2024c. DCoMA: a dynamic coordinative merging assistant strategy for on-ramp vehicles with mixed traffic conditions. Transport. Res. C Emerg. Technol. 165, 104700. 





Li, Y., Zhang, Y., Ma, Y., 2024d. A merging strategy framework for connected and automated vehicles in multi-lane mixed traffic scenarios. IEEE Access 12, 92753–92763. 





Liao, X., Wang, Z., Zhao, X., Han, K., Tiwari, P., Barth, M.J., Wu, G., 2022. Cooperative ramp merging design and field implementation: a digital twin approach based on vehicle-to-cloud communication. IEEE Trans. Intell. Transport. Syst. 23 (5), 4490–4500. 





Lin, Y., McPhee, J., Azad, N.L., 2022. Co-optimization of on-ramp merging and plug-in hybrid electric vehicle power split using deep reinforcement learning. IEEE Trans. Veh. Technol. 71 (7), 6958–6968. 





Liu, H., Kan, X., Shladover, S.E., Lu, X.Y., Ferlis, R.E., 2018. Modeling impacts of Cooperative Adaptive Cruise Control on mixed traffic flow in multi-lane freeway facilities. Transport. Res. C Emerg. Technol. 95, 261–279. 





Liu, L., Zhang, X., Jiang, S., Zhao, X., 2025. Hurricane evacuation analysis with largescale mobile device location data during hurricane Ian. Transport. Res. D: Transp. Environ. 139, 104559. 





Liu, J., Zhao, W., Xu, C., 2022a. An efficient on-ramp merging strategy for connected and automated vehicles in multi-lane traffic. IEEE Trans. Intell. Transport. Syst. 23 (6), 5056–5067. 





Liu, Z., Sun, D., Zhao, M., Huang, S., Wu, X., 2022b. A freeway on-ramps BLVD-based virtual platoon control for mixed traffic: a cyber-physical perspective. 2022 IEEE 25th International Conference on Intelligent Transportation Systems (ITSC), pp. 1516–1521. 





Liu, H., Zhuang, W., Yin, G., Li, Z., Cao, D., 2023a. Safety-critical and flexible cooperative on-ramp merging control of connected and automated vehicles in mixed traffic. IEEE Trans. Intell. Transport. Syst. 24 (3), 2920–2934. 





Liu, Y., Zhou, A., Wang, Y., Peeta, S., 2023b. Proactive longitudinal control to preclude disruptive lane changes of human-driven vehicles in mixed-flow traffic. Control Eng. Pract. 136, 105522. 





Liu, C., Liu, Z., Xu, Z., Li, X., 2024. A multistep cooperative lane change strategy for connected and autonomous vehicle platoons departing from dedicated lanes. Transport. Res. C Emerg. Technol. 165, 104720. 





Lu, X.Y., Tan, H.S., Shladover, S.E., Hedrick, J.K., 2004. Automated vehicle merging maneuver implemen-tation for AHS. Veh. Syst. Dyn. 41 (2), 85–107. 





Luo, X., Li, X., Shaon, M.R.R., Zhang, Y., 2022. Multi-lane-merging strategy for connected automated vehicles on freeway ramps. Transportmetrica B: Trans. Dynam. 11 (1), 127–145. 





Meng, T., Huang, J., Hu, Z., Yang, Z., Chen, Y., Yang, D., Zhong, Z., 2024. Spatialdependent robust control strategy for on-ramp merging. IEEE Trans. Veh. Technol. 73 (3), 3191–3205. 





Milan´es, V., Shladover, S.E., 2014. Modeling cooperative and autonomous adaptive cruise control dynamic responses using experimental data. Transport. Res. C Emerg. Technol. 48, 285–300. 





Min, H., Lei, X., Wu, X., Fang, Y., Chen, S., Wang, W., Zhao, X., 2024. Toward interpretable anomaly detection for autonomous vehicles with denoising variational transformer. Eng. Appl. Artif. Intell. 129, 107601. 





Minderhoud, M.M., Bovy, P.H., 2001. Extended time-to-collision measures for road traffic safety assessment. Accid. Anal. Prev. 33 (1), 89–97. 





Mu, C., Du, L., Zhao, X., 2021. Event triggered rolling horizon based systematical trajectory planning for merging platoons at mainline-ramp intersection. Transport. Res. C Emerg. Technol. 125, 103006. 





Nie, Q., Ou, J., Zhang, H., Lu, J., Li, S., Shi, H., 2024. A robust integrated multi-strategy bus control system via deep reinforcement learning. Eng. Appl. Artif. Intell. 133 (Part A), 107986. 





Norouzi, A., Heidarifar, H., Borhan, H., Shahbakhti, M., Koch, C.R., 2023. Integrating machine learning and model predictive control for automotive applications: a review and future directions. Eng. Appl. Artif. Intell. 120, 105878. 





Peng, J., Wei, S., Chai, L., 2022. Strategy of lane-changing coupling process for connected and automated vehicles in mixed traffic environment. Transportmetrica B: Trans. Dynam. 11 (1), 979–995. 





Pooladsanj, M., Savla, K., Ioannou, P.A., 2023. Ramp metering to maximize freeway throughput under vehicle safety constraints. Transport. Res. C Emerg. Technol. 154, 104267. 





Qin, Y., Wang, H., Ran, B., 2019. Impacts of cooperative adaptive cruise control platoons on emissions under traffic oscillation. J. Intelligent Transp. Syst. 25 (4), 376–383. 





Rios-Torres, J., Malikopoulos, A.A., 2017a. Automated and cooperative vehicle merging at highway on-ramps. IEEE Trans. Intell. Transport. Syst. 18 (4), 780–789. 





Rios-Torres, J., Malikopoulos, A.A., 2017b. A survey on the coordination of connected and automated vehicles at intersections and merging at highway on-ramps. IEEE Trans. Intell. Transport. Syst. 18 (5), 1066–1077. 





Schulman, J., Levine, S., Moritz, P., Jordan, M.I., Abbeel, P., 2015. Trust region policy optimization. arXiv Prepr. arXiv:1502.05477. 





Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O., 2017. Proximal policy optimization algorithms. arXiv Prepr. arXiv1707.06347. 





Shang, M., Wang, S., Stern, R.E., 2023. Extending ramp metering control to mixed autonomy traffic flow with varying degrees of automation. Transport. Res. C Emerg. Technol. 151, 104119. 





Sharma, O., Sahoo, N.C., Puhan, N.B., 2021. Recent advances in motion and behavior planning techniques for software architecture of autonomous vehicles: a state-of-theart survey. Eng. Appl. Artif. Intell. 101, 104211. 





Sharma, S., Papamichail, I., Nadi, A., van Lint, H., Tavasszy, L., 2022. A multi-class lanechanging advisory system for freeway merging sections using cooperative ITS. IEEE Trans. Intell. Transport. Syst. 23 (9), 15121–15132. 





Sheikh, M.S., Peng, Y., 2023. A collision avoidance model for on-ramp merging of autonomous vehicles. KSCE J. Civ. Eng. 27 (3), 1323–1339. 





Shen, S., Liu, X., Li, Z., Zhang, H., Ke, J., Chen, Z., 2024. A dynamic hierarchical cooperative lane change strategy for off-ramp connected and autonomous vehicles in mixed traffic environment. Phys. Stat. Mech. Appl. 650, 129976. 





Sun, Z., Huang, T., Zhang, P., 2020. Cooperative decision-making for mixed traffic: a ramp merging example. Transport. Res. C Emerg. Technol. 120, 102764. 





Sun, K., Zhao, X., Gong, S., Wu, X., 2023. A cooperative lane change control strategy for connected and automated vehicles by considering preceding vehicle switching. Appl. Sci. 13 (4), 2193. 





Tang, Z., Zhu, H., Zhang, X., Iryo-Asano, M., Nakamura, H., 2022. A novel hierarchical cooperative merging control model of connected and automated vehicles featuring flexible merging positions in system optimization. Transport. Res. C Emerg. Technol. 138, 103650. 





Treiber, M., Hennecke, A., Helbing, D., 2000. Congested traffic states in empirical observations and microscopic simulations. Phys. Rev. E: Stat. Phys., Plasmas, Fluids, Relat. Interdiscip. Top. 62 (2 Pt A), 1805–1824. 





Wang, H., Qin, Y., Wang, W., Chen, J., 2019. Stability of CACC-manual heterogeneous vehicular flow with partial CACC performance degrading. Transportmetrica B: Trans. Dynam. 7 (1), 788–813. 





Wang, Y., Wang, L., Guo, J., Papamichail, I., Papageorgiou, M., Wang, F., Bertini, R., Hua, W., Yang, Q., 2022. Ego-efficient lane changes of connected and automated vehicles with impacts on traffic flow. Transport. Res. C Emerg. Technol. 138, 103478. 





Wang, R., Shen, L., Zhou, Y., Ding, R., Ye, Q., 2024. Lane-changing control for hybrid electric vehicles with dedicated hybrid transmission based on robust model predictive control. Proc. Inst. Mech. Eng. - Part D J. Automob. Eng. 238 (10–11), 3140–3159. 





Xue, Y., Zhang, X., Cui, Z., Yu, B., Gao, K., 2023. A platoon-based cooperative optimal control for connected autonomous vehicles at highway on-ramps under heavy traffic. Transport. Res. C Emerg. Technol. 150, 104083. 





Yang, W., Dong, C., Wang, H., 2023a. A cooperative merging speed control strategy of CAVs based on virtual platoon in on-ramp merging system. Transportmetrica B: Trans. Dynam. 11 (1), 1432–1454. 





Yang, W., Dong, C., Chen, X., Chen, Y., Wang, H., 2023b. A cooperative control method for safer on-ramp merging process in heterogeneous traffic flow. Accid. Anal. Prev. 193, 107324. 





Yuan, Z., Ding, W., Ran, B., Qu, X., Zhang, Y., 2021. Coordinated decisions of discretionary lane change between connected and automated vehicles on freeways: a game theory-based lane change strategy. IET Intell. Transp. Syst. 14 (13), 1864–1870. 





Zhou, Y., Chen, J., Chung, E., Ozbay, K., 2024. CAV-enabled active resolving of temporary mainline congestion caused by gap creation for on-ramp merging vehicles. IEEE Trans. Intell. Transport. Syst. 25 (7), 6873–6888. 





Zhu, J., Tasic, I., 2021. Safety analysis of freeway on-ramp merging with the presence of autonomous vehicles. Accid. Anal. Prev. 152, 105966. 





Zhu, J., Ma, Y., Lou, Y., 2022. Multi-vehicle interaction safety of connected automated vehicles in merging area: a real-time risk assessment approach. Accid. Anal. Prev. 166, 106546. 

