# Advancements in Weed Mapping: A Systematic Review

Mohammad Jahanbakht $^{123*}$ , Alex Olsen $^{4}$ , Ross Marchant $^{4}$ , Emilie Fillols $^{5}$ , and Mostafa Rahimi Azghadi $^{123*}$

$^{1}$  College of Science and Engineering, James Cook University, Douglas, QLD 4814, Australia $^{2}$  ARC Training Centre in Plant Biosecurity, James Cook University, Australia $^{3}$  Agriculture Technology and Adoption Centre, James Cook University, Australia $^{4}$  Infarm Pty Ltd, Goondiwindi, QLD 4390, Australia $^{5}$  Sugar Research Australia, Brisbane 4000, QLD, Australia

$^{6}$ Corresponding Authors: Mohammad Jahanbakht (mohammad.jahanbakht@jcsu.edu.au) and Mostafa Rahimi Azghadi (mostafa.rahimiazghadi@jcu.edu.au)

Abstract - Weed mapping plays a critical role in precision management by providing accurate and timely data on weed distribution, enabling targeted control and reduced herbicide use. This minimizes environmental impacts, supports sustainable land management, and improves outcomes across agricultural and natural environments. Recent advances in weed mapping leverage ground- vehicle Red Green Blue (RGB) cameras, satellite and drone- based remote sensing combined with sensors such as spectral, Near Infra- Red (NIR), and thermal cameras. The resulting data are processed using advanced techniques including big data analytics and machine learning, significantly improving the spatial and temporal resolution of weed maps and enabling site- specific management decisions. Despite a growing body of research in this domain, there is a lack of comprehensive literature reviews specifically focused on weed mapping. In particular, the absence of a structured analysis spanning the entire mapping pipeline, from data acquisition to processing techniques and mapping tools, limits progress in the field. This review addresses these gaps by systematically examining state- of- the- art methods in data acquisition (sensor and platform technologies), data processing (including annotation and modelling), and mapping techniques (such as spatiotemporal analysis and decision support tools). Following PRISMA guidelines, we critically evaluate and synthesize key findings from the literature to provide a holistic understanding of the weed mapping landscape. This review serves as a foundational reference to guide future research and support the development of efficient, scalable, and sustainable weed management systems.

Keywords: Weed mapping, remote sensing, machine learning, deep learning, drone, satellite

# I. Introduction

Invasive weeds present a major threat to both agricultural productivity and environmental sustainability globally. Their spread leads to considerable economic losses by competing with the crop and reducing crop yields, disrupting harvesting, and promoting insect pests and diseases [1, 2]. As the agricultural sector contends with these impacts, effective weed management strategies are crucial to support sustainable food production and protect natural ecosystems.

One such strategy involves integrated precision approaches, leveraging technological advancements to enhance weed mapping and control. In this regard, precision agriculture represents a paradigm shift from traditional farming systems, utilizing data- driven methodologies to optimize resource utilization and improve productivity [3]. It integrates modern electronic sensors, including those for monitoring environmental parameters, navigation, visual and spectral imaging, and mapping, with advanced processing techniques such as machine learning algorithms to assess conditions across the field. This enables informed, site- specific decision- making tailored to both farm and environmental conditions [4].

Recent advancements in electronic sensors, including those employed in remote sensing technologies have revolutionized agricultural and environmental monitoring, offering enhanced capabilities for weed mapping. Remote sensing platforms, including satellites [5] and Unmanned Aerial Vehicles (UAVs) [6], provide large- scale spatial and sometimes temporal data that enable precise weed detection and management. In addition, ground- based machinery can be used to collect weed data at high spatial and temporal resolution [7].

Once weed data is collected, it must be processed and analyzed for weed detection and classification. This is typically achieved using machine learning models capable of handling complex spectral and spatial data, allowing for the reliable identification of weed species even in diverse and heterogeneous agricultural landscapes [8]. The integration of advanced remote sensing technologies, such as hyperspectral and multispectral imaging, further enhances these models by providing rich spectral information that helps

![](https://cdn-mineru.openxlab.org.cn/extract/2d553dfd-344a-49ff-b6e5-3dbb91d7b1db/741d32232f735be528849c65b6760dca42f011161811fa4177bc765089f32e43.jpg)  
Figure 1: This paper covers the full weed mapping pipeline as illustrated here, from data acquisition to advanced data processing, to visualization dashboards and spatiotemporal models that support informed farm management.

distinguish plant species based on their unique spectral signatures [9].

After invasive weed detection with advanced machine learning and analytical models, analyzing the spatiotemporal patterns of weed spread is crucial for understanding their ecological impact and predicting future invasions. This step enables more effective, data- driven management strategies by identifying high- risk areas and optimal intervention times. Recent advancements in spatiotemporal weed pattern analysis have significantly enhanced our understanding of weed dynamics across agricultural landscapes. Innovative technologies, such as timeseries forecasting and photogrammetry, now enable the creation of detailed multi- dimensional models of weed populations, capturing variations in plant height, volume, and canopy structure over time [10]. These models facilitate the generation of high- resolution spatiotemporal maps, allowing for precise monitoring of weed distribution and growth patterns.

To explore these novel advancements in weed mapping technologies, we will systematically review the latest developments in the area, highlighting their potential to enhance efficiency and sustainability. By examining current research, technological innovations, and practical applications, we aim to provide insights into how precision management can be harnessed to improve weed control strategies. This study's primary contributions include:

Filling a significant gap in the literature by developing a comprehensive systematic review focused solely on weed mapping serving as a central reference point for future studies and applications.

- Providing a detailed and structured synthesis of modern data acquisition tools and technologies used in weed mapping, offering clarity on their applicability and limitations.- Reviewing and synthesizing current data processing methodologies, including big data handling, annotation strategies, machine learning, deep learning, and edge computing, by highlighting their strengths, challenges, and practical implications.- Exploring commonly used weed mapping tools, spatial and temporal pattern modelling approaches, and their integration into decision support systems, providing valuable insights for operational deployment.- Delivering cross-sectoral actionable insights for agricultural technology developers, policymakers, and farm managers aiming to implement data-driven and environmentally sustainable weed control strategies.- Identifying key research and development opportunities, encouraging interdisciplinary innovation in weed mapping technologies and offering a future-oriented roadmap.

The rest of the paper is structured as follows. Section II presents our Preferred Reporting Items for Systematic Reviews and Meta- Analyses (PRISMA)- based systematic review methodology, outlining the literature selection, screening, and analysis process. The overall

![](https://cdn-mineru.openxlab.org.cn/extract/2d553dfd-344a-49ff-b6e5-3dbb91d7b1db/2a2b08064e775084e6fe42b117ce9e7ae6922bbe84cf0b78c7cd5fff91129160.jpg)  
Figure 2: The literature selection flowchart through consecutive inclusion/exclusion steps that follows the PRISMA guidelines.

flow of technical discussions is summarized in Figure 1, covering acquisition, processing, and mapping. Section III discusses data acquisition tools used in weed mapping, including a review of imaging sensors, agricultural machinery, and remote sensing platforms such as drones and satellites. Section IV explores weed data processing techniques and technologies, covering key aspects such as big data handling, data annotation, deep learning models, and edge computing solutions. Section V focuses on weed mapping technologies, discussing spatiotemporal weed patterns, the impact of farm management practices, and commonly used mapping tools and decision- support systems. Finally, Section VI outlines future research directions and technological innovations needed to advance the field of precision weed management.

# II. Survey Methodology

This systematic review was conducted following the PRISMA guidelines, ensuring a transparent, methodical, and replicable approach to synthesizing the literature on weed mapping in agriculture. The use of PRISMA enhances the scientific quality of the study by reducing bias through comprehensive and structured literature searches, while providing a clear account of the procedures undertaken throughout the review process. The methodology was carried out in three main phases: identification, screening, and eligibility, as illustrated in Figure 2.

In the identification phase, we performed an initial search using the keywords "weed mapping" and "agriculture" across two major academic databases: Elsevier and IEEE Xplore. This search was conducted in April 2025 and limited to publications released after the year 2000. A total of 238 articles (including 222 papers from Elsevier and 16 papers from IEEE Xplore) were retrieved and archived locally for further analysis.

The screening phase involved reviewing the titles and abstracts of all 238 identified records. To proceed to the next stage, studies were required to meet two criteria: (a) the research addressed weed control topics, and (b) the application context was within precision weed management. After applying these filters, 207 articles were retained.

In the final eligibility phase, the remaining 207 articles were subjected to a more in- depth evaluation. We examined section and subsection titles and partially skimmed the main text of each article to ensure relevance. Studies were excluded if they (a) did not pertain to modern agricultural methods in weed management, or (b) failed to address at least one of our three core focus areas: data acquisition, data processing, and weed mapping. It is worth noting that some of the studies were included in more than one focus area. Ultimately, 151 publications met the eligibility criteria and were included in this review.

These 151 studies comprise 135 journal articles, 8 government, web, book, or thesis reports, and 8 conference papers. Their publication years span from 2003 to 2025. A detailed breakdown of these studies based on publication type, publication year, and conceptual focus is presented in Figure 3.

# III. Data Acquisition

Traditional methods for monitoring incursions of invasive weeds are often labor- intensive, time- consuming, expensive, and rarely fully effective [2]. Advancements depend on the development of efficient and scalable data acquisition and processing technologies. Innovative tools, including cameras and sensor- based systems, must be capable of addressing the dynamic characteristics of weeds and the vast scale of agricultural landscapes to enable effective detection and tracking of infestations. This section will explore modern approaches to data acquisition in weed surveillance.

# Data Capture Modalities

The integration of advanced imaging technologies in agriculture has significantly enhanced weed mapping and crop monitoring. These technologies leverage different parts of the electromagnetic spectrum in Figure

4a to capture vital information about crops, soil, and surrounding vegetation. The following subsections discuss various imaging modalities and their applications in agricultural practices, particularly in weed management.

# X-ray

X- ray technology is widely utilized in agriculture for detecting contaminants in food packaging and assessing the quality of agricultural products. X- rays reveal spatial information and acquire three- dimensional data, making them effective for detecting density variations in varied materials. Most agricultural applications employ soft X- rays, which have been extensively used for studying crops, soil, grains, tree nuts, and fruits [11]. Soft X- ray technology with low energy and longer wavelength (compared to hard X- rays) allows for detailed visualization of internal structures in thin- film materials, making it a valuable tool for quality assessment in agricultural products.

In weed management, soft X- ray imaging plays a crucial role in seed inspection, commonly known as seed radiography [12]. This technique helps identify and remove weed seeds from agricultural good seed batches by analyzing their internal structures before planting. By sorting out undesirable weed seeds, farmers can reduce the risk of weed infestations, leading to improved crop productivity and quality.

# Visible RGB

RGB imaging relies on visible light to capture high- resolution images of crops and weeds. The quality of image acquisition is dependent on two primary components: illumination sources and camera systems. The choice of illumination significantly influences the ability to extract texture, shape, and color features of agricultural objects.

In a study by Raja et al. [13], multiple illumination techniques are successfully utilized to enhance the accuracy of weed classification in controlled- light imaging chambers. These chambers were designed to

![](https://cdn-mineru.openxlab.org.cn/extract/2d553dfd-344a-49ff-b6e5-3dbb91d7b1db/443349f7ec4b3b055a0cfc502a07c31b7ba34f96660549e947a4ca0d1e0e07a1.jpg)  
Figure 3: Distribution of the surveyed articles over (a) publication venues, i.e., journal names, conferences, official reports, websites, etc., (b) publication years, and (c) conceptual topics of this review, i.e., data acquisition, data processing, and weed mapping.

![](https://cdn-mineru.openxlab.org.cn/extract/2d553dfd-344a-49ff-b6e5-3dbb91d7b1db/eaf21ae3f335fc9114c94d795e3f0c5e622226573b953833298c38bdf5db0ab6.jpg)  
Figure 4: (a) Frequency spectrum and bandwidths in agricultural applications and (b) Conceptualization of RGB, multispectral, and hyperspectral imaging techniques.

minimize interference from natural light and to capture high- resolution images under uniform illumination, white balance calibration, and controlled exposure time, ensuring clear visualization of crops and weeds. This integration of illumination techniques has significantly enhanced the reliability of the classification algorithm, achieving a lettuce crop detection accuracy of  $99.75\%$  and correctly identifying  $98.11\%$  of sprayable weeds.

In another work addressing the illumination problem, FieldNet was proposed as a real- time deep learning framework for shadow removal in outdoor environments. By eliminating shadows without needing shadow masks at inference, FieldNet improves image consistency under varying lighting, enhancing weed detection accuracy in field robotics [14].

Cameras, the other major component of RGB imaging, include monocular and binocular configurations. Monocular cameras provide cost- effective 2D imaging, while binocular stereo vision (stereoscopic) systems generate 3D visual representations by capturing depth information. The former is the most common scenario, while the latter is particularly useful for measuring object dimensions and detecting plant structures, making it a valuable tool for weed identification applications.

Binocular cameras are successfully utilized in [15] for weed detection in rice fields, significantly improving classification accuracy compared to conventional single- source cameras. By capturing stereoscopic video data and incorporating 3D depth perception under controlled light conditions, the study leveraged a computer vision system that achieved  $96.95\%$  weed classification accuracy. This helps distinguish between similar- looking plants more effectively than single- camera systems.

# Spectral

Spectral remote sensors have transformed the way we collect and analyze data on various weed species across different environments. These advanced sensors capture detailed spectral reflectance information from target plants, supporting agricultural applications such as weed identification, crop yield estimation, and disease monitoring. Spectral imaging includes multispectral and hyperspectral techniques [16]. Figure 4b compares these techniques with each other and with the RGB imaging method.

Hyperspectral imaging captures hundreds of narrow spectral bands, providing extensive spectral information for each pixel in an image. This capability is highly beneficial for material identification, agriculture, mineralogy, and medical imaging. In agriculture, hyperspectral imaging is used to classify weeds, detect disease and pest, monitor plant health, and plant stressors [16]. However, hyperspectral imaging systems are costly and require complex data modeling and processing. The high spectral resolution can also limit real- time applications due to computational challenges. Despite these drawbacks, hyperspectral imaging remains an essential tool for precise weed mapping and vegetation monitoring.

On the other hand, multispectral imaging captures a limited number of broader spectral bands, making it a more computationally efficient alternative to hyperspectral imaging. It is commonly used in remote sensing applications and environmental monitoring. Compared to hyperspectral imaging, multispectral imaging offers a balance between computational efficiency and spectral information, making it a widely used approach for weed detection and agricultural mapping [9].

Table 1 presents various weed species commonly found in agricultural fields, detailing their names, associated crop environments, and the type of vision technology used for their detection. The listed weeds span multiple crops, including sugarcane, wheat, maize, soybean, and barley, highlighting their widespread impact on global agriculture. This highlights the effective use of RGB and spectral imaging sensors in advanced weed detection studies in literature.

Table 1: RGB and spectral imaging technologies reported in the latest weed control applications.  

<table><tr><td rowspan="4">RGB</td><td>Weed</td><td>Amaranthus blitoides</td><td>Amaranthus tuberculatus</td><td>Chromolaena odorata</td><td>Cirsium arvense</td></tr><tr><td>Crop</td><td>Maize [17]</td><td>Black bean, canola, corn, flax, soybean, and sugar beets [18]</td><td>Crop of tropical climate regions [19]</td><td>Wheat [20] and barley [21]</td></tr><tr><td>Weed</td><td>Cynodon dactylon</td><td>Ambrosia artemisiifolia</td><td>Sorghum halepense</td><td>Tussilago farfara</td></tr><tr><td>Crop</td><td>Vine [22]</td><td>Black bean, canola, corn, flax, soybean, and sugar beets [18]</td><td>Maize [17]</td><td>Barley [21]</td></tr><tr><td rowspan="8">Spectral</td><td>Weed</td><td>Ageratum conyzoides</td><td>Avena sterilis</td><td>Amaranthus palmeri</td><td>Bassia scoparia</td></tr><tr><td>Crop</td><td>Sugarcane [23]</td><td>Wheat [24]</td><td>Corn, soybeans, and cotton [25]</td><td>Barley, corn, dry pea, garbanzo, lentils, pinto bean, safflower, and sugar beet [26]</td></tr><tr><td>Weed</td><td>Chenopodium album</td><td>Cirsium arvense</td><td>Commelina bengalensis</td><td>Conyza canadensis</td></tr><tr><td>Crop</td><td>Maize [27]</td><td>Maize and sugar beet [27]</td><td>Sugarcane [23]</td><td>Barley, corn, dry pea, garbanzo, lentils, pinto bean, safflower, and sugar beet [26]</td></tr><tr><td>Weed</td><td>Crotalaria juncea</td><td>Fallopia convolvulus</td><td>Ipomoea hederifolia and Ipomoea purpurea</td><td>Lolium multiflorum and Lolium rigidum</td></tr><tr><td>Crop</td><td>Sugarcane [23]</td><td>Sugar beet [27]</td><td>Sugarcane [23]</td><td>Sugar beet [27] and wheat [24]</td></tr><tr><td>Weed</td><td>Megathyrsus maximus</td><td>Phalaris brachystachys</td><td>Sorghum halepense</td><td>Urochloa brizantha</td></tr><tr><td>Crop</td><td>Sugarcane [23]</td><td>Wheat [24]</td><td>Maize [28]</td><td>Sugarcane [23]</td></tr></table>

# NIR and Thermal

Both Near- Infrared (NIR) and thermal cameras use infrared radiation but differ in their detected wavelength ranges. NIR imaging detects reflected light in the  $700-$ $2500\mathrm{nm}$  range, while thermal imaging captures emitted heat in the  $3\mathrm{- }14\mu \mathrm{m}$  range. These technologies offer critical insights into plant health, transpiration rates, and water potential.

In weed control applications, NIR and thermal cameras can be used in temperature- based differentiation [29].

Weeds often exhibit different thermal properties compared to crops due to variations in water content, leaf structure, and metabolic activity. For example, weeds, competing with crops for resources like water, may have different water content levels, influencing their thermal behavior [30]. Furthermore, leaf structures of crops and weeds, including area and thickness, as well as their metabolic activities (reflected in processes like photosynthesis and respiration) contribute to a plant's energy balance and thus its thermal properties [31].

# Terahertz

Terahertz (THz) imaging is an emerging technology used for detecting small unwanted objects in agricultural environments, such as pests, worms, or foreign bodies in crop yields. This technique employs orthogonally polarized terahertz waves to enhance detection accuracy in various agricultural settings, including conveyor belts and land surveying vehicles.

As THz waves interact differently with plant tissues (based on their water content, chemical composition, and cellular structure) a precise differentiation can be detected between weed species and crops, even in dense vegetation. This differentiation can help identify weeds at early growth stages, even before visible differences appear. THz imaging can also be combined with machine learning algorithms to improve weed classification accuracy, helping farmers and researchers develop targeted weed control strategies [32].

# Data Capture Equipment

# Agri-tech Machinery

The application of imaging technologies (discussed in the previous subsection) can benefit from Agri- tech machinery that enables improved spatial resolution, greater coverage, and enhanced temporal flexibility. Among the most appealing approaches are All- Terrain Vehicles (ATVs) and autonomous robotic systems, which provide flexible and responsive solutions to farming operations. These intelligent machines, equipped with state- of- the- art navigation systems, sensors, and AI- driven automation, enable efficient and precise location- specific agricultural tasks, even in challenging terrains [1].

ATVs and agricultural robots enhance productivity by facilitating various farming operations, ranging from sowing and field monitoring to weed control, and harvesting. By leveraging machine learning and vision systems, these autonomous machines optimize resource use while reducing crop damage and soil compaction. Especially in field monitoring and health assessment applications, ATVs and robotic systems can process real- time data collected from sensors and imaging systems to evaluate key indicators such as leaf color, biomass, and disease symptoms [3].

In advanced weed control systems, these machineries employ sophisticated image recognition and classification models to differentiate between crops and weeds [33]. By leveraging real- time sensor data, they execute precise and automated physical weed removal or targeted herbicide applications, reducing the reliance on broad- spectrum chemical treatments. This approach enhances crop health, minimizes agrochemical overspray, and lowers environmental risks associated with traditional weed management strategies [34]. The collection of studies in Table 2 explores various machine vision and AI- based techniques for precision agriculture, focusing on weed and pest detection, automated spraying, and robotic weeding. Commercial solutions (e.g., Trimble's Bilberry, John Deere's See & Spray, and GreenEye) are excluded, as the table focuses exclusively on research- based literature. Besides, some of the listed machines, for example [35], have not been directly used for weed data collection, detection, and management, they provide examples of other machinery and sensors applicable to weed data collection.

# Remote Sensing

Remote sensing involves collecting physical information about an object without direct contact [36]. This plays a crucial role in precision agriculture by enabling crops and farmlands monitoring from varying distances. Technologies such as UAVs and satellites provide superior support for agricultural applications, assisting in crop scouting, yield estimation, precise agrochemical application, and weed control.

A major challenge in remote sensing for precision agriculture lies in spatial, temporal, spectral, and radiometric image resolutions. Spatial resolution determines image detail based on pixel density, with Ground Sampling Distance (GSD) serving as a key metric. Temporal resolution reflects how frequently a location is imaged, while spectral resolution influences the ability to differentiate objects based on narrow frequency bandwidths. Radiometric resolution defines a sensor's capacity to capture subtle energy variations, affecting the precision of plant identification [37].

High resolutions across these categories are critical for distinguishing crops and weeds, particularly in diverse agricultural landscapes. UAVs have emerged as a dominant technology in precision agriculture due to their ability to capture high- resolution images with RGB, multispectral, and hyperspectral sensors, perform low- altitude maneuvers, access difficult terrain, and operate at a lower cost while being less affected by weather conditions compared to satellites. However, UAVs face limitations, including restricted area coverage, payload constraints, regulatory challenges, and the need for skilled operators [37]. Both the drone and satellite applications in weed mapping are studied in more detail here.

Table 2: The application type and operation method of researchbased smart Agri-tech machinery and robots that have been or can be used in industrial weed management systems.  

<table><tr><td>Appl.</td><td>Description</td></tr><tr><td>Robot [35] (for greenhouses)</td><td>·Detecting thrips in strawberry greenhouses
·Traditional machine learning (i.e., SVM)
·Utilizing region and color indices to classify pests, with different kernel functions applied for improved accuracy.</td></tr><tr><td>Robot [38] (general purpose)</td><td>·Air-blast spraying of citrus orchards
·Low-cost smart sensing system using LiDAR
·Deep learning (i.e., YOLOv3 with Resnet50 backbone)
·Classifying trees, estimating tree heights, counting fruits, and enabling precise nozzle control for targeted spraying</td></tr><tr><td>ATV [39] (for row farming)</td><td>·Mechanical weeding machine for precise weed removal in cultivation aisles
·A modular weeder with an inverted pyramid-shaped tool efficiently shovels weed out without use of herbicide
·Deep learning (i.e., convolutional neural network)
·Accurately identifying/detecting weeds</td></tr><tr><td>ATV [40] (for non-row farming)</td><td>·A weeding robot in corn fields
·Equipped with a quadratic traversal algorithm for guiding around the identified corn plants
·Deep learning (i.e., Faster R-CNN)
·real-time image processing on edge and shortest 3D path calculation, based on plant contours and depth cameras.</td></tr><tr><td>Robot [41] (general purpose)</td><td>·Weed detection in corn fields
·Traditional machine learning (i.e., green features and Otsu)
·Identifying/segmenting and positioning corn, weeds, and land profile to improve weed removal efficiency</td></tr></table>

<table><tr><td>Appl.</td><td>Description</td></tr><tr><td>ATV [42] (for orchard spraying)</td><td>Precise and automatic spraying system for peach orchards
·Detects the leaf wall area and plans spraying paths based on region of interest (except in areas with row gaps)
·Traditional machine learning (i.e., depth features and Otsu)
·Using color-depth vision</td></tr><tr><td>ATV [43] (for orchard spraying)</td><td>·Intelligent spraying system for pear orchards
·Deep learning (i.e., SegNet)
·Semantic segmentation of fruit trees
·Integrating depth data from an RGB-D camera to avoid detecting background trees and controls nozzles based on tree coverage in image zones</td></tr><tr><td>ATV [44] (for hydroponic farms)</td><td>·Weed detection in sugar-beet
·Integrating ecological considerations into precision weeding robots
·Rolling-view observation model to improve weeding performance and oversee diverse weed distributions
·Deep learning (i.e., Mask-RCNN)</td></tr><tr><td>ATV [45] (for non-row farming)</td><td>·Weed detection in celery houses
·Real-time robotic weed control in dense vegetable fields by treating celery plants with Rhodamine B to create machine-readable fluorescent signals
·Traditional machine learning (i.e., segmentation by color features)
·Custom illumination system (spectral fluorescence imaging) for precise differentiation of crops from weeds and accurate stem localization</td></tr><tr><td>ATV [46] (for row farming)</td><td>·Effective weed detection and control in strawberries
·Autonomous laser weeding robot with minimal seedling damage
·Deep learning (i.e., YOLOv8)
·Detects strawberry seedlings, weeds, drip irrigation pipes, and weed growth points in real-time.</td></tr></table>

Table 3: Common satellites in large-scale agricultural applications that have been or can be applied in weed mapping. Click the blue hyperlinks to access the satellite webpage.  

<table><tr><td>Satellite</td><td>Resolution</td><td>Applications</td></tr><tr><td>EnMap</td><td>Spatial: 30 m</td><td>HS (420-2450 nm)</td></tr><tr><td>DLR (Germany)</td><td>Swath: 30 km</td><td>Crop mapping [45]</td></tr><tr><td>Since 2022</td><td>Temporal: 27 days</td><td>Plant health [46]</td></tr><tr><td>EO-1 (Hyperion)</td><td>Spatial: 30 m</td><td>HS (357-2576 nm)</td></tr><tr><td>NASA (USA)</td><td>Swath: 7.7 km</td><td>Crop mapping [47, 48]</td></tr><tr><td>Since 2000</td><td>Temporal: 16 days</td><td>Plant health [49]</td></tr><tr><td>Ikonos</td><td>Spatial: 1 m</td><td>MS (4 bands)</td></tr><tr><td>ESA (Europe)</td><td>Swath: 11.3 km</td><td>Crop mapping [50]</td></tr><tr><td>Since 1999</td><td>Temporal: 3 days</td><td></td></tr><tr><td>KOMPSAT-3</td><td>Spatial: 2 m</td><td>MS (2 bands)</td></tr><tr><td>SI (Korea)</td><td>Swath: 15 km</td><td>Land cover [51]</td></tr><tr><td>Since 2012</td><td>Temporal: 1.4 days</td><td></td></tr><tr><td>Landsat 8/9</td><td>Spatial: 30 m</td><td>MS (11 bands)</td></tr><tr><td>NASA (USA)</td><td>Swath: 185 km</td><td>Crop mapping [47]</td></tr><tr><td>Since 2013</td><td>Temporal: 16 days</td><td>Weed mapping [52]</td></tr><tr><td>PlanetScope</td><td>Spatial: 3 m</td><td>MS (4 bands)</td></tr><tr><td>ESA (Europe)</td><td>Swath: 25 km</td><td>Crop mapping [53]</td></tr><tr><td>Since 2016</td><td>Temporal: 1 day</td><td>Weed mapping [54]</td></tr><tr><td>Péliades</td><td>Spatial: 0.5 m</td><td>MS (6 bands)</td></tr><tr><td>CNES (France)</td><td>Swath: 20 km</td><td>Crop mapping [55]</td></tr><tr><td>Since 2011</td><td>Temporal: 1 day</td><td></td></tr><tr><td>Prisma</td><td>Spatial: 30 m</td><td>HS (400-2500 nm)</td></tr><tr><td>ASI (Italy)</td><td>Swath: 30 km</td><td>Land cover [56]</td></tr><tr><td>Since 2019</td><td>Temporal: ~29 days</td><td>Crop mapping [57]</td></tr><tr><td>Proba 1</td><td>Spatial: 17 m</td><td>HS (400-1300 nm)</td></tr><tr><td>ESA (Europe)</td><td>Swath: 15 km</td><td>Plant health [49]</td></tr><tr><td>Since 2001</td><td>Temporal: 7 days</td><td></td></tr><tr><td>Sentinel 1</td><td>Spatial: 10 m</td><td>Radar (C-band)</td></tr><tr><td>ESA (Europe)</td><td>Swath: 250 km</td><td>Crop mapping [58]</td></tr><tr><td>Since 2014</td><td>Temporal: 6-12 days</td><td>Land cover [59]</td></tr><tr><td>Sentinel 2 A/B</td><td>Spatial: 10 m</td><td>MS (13 bands)</td></tr><tr><td>ESA (Europe)</td><td>Swath: 290 km</td><td>Land cover [59, 60]</td></tr><tr><td>Since 2015</td><td>Temporal: 5 days</td><td>Weed mapping [61]</td></tr><tr><td>SPOT 6/7</td><td>Spatial: 6 m</td><td>MS (5 bands)</td></tr><tr><td>ESA (Europe)</td><td>Swath: 60 km</td><td>Crop mapping [62]</td></tr><tr><td>Since 2012</td><td>Temporal: 13 days</td><td>Land cover [63]</td></tr><tr><td>WorldView-3</td><td>Spatial: 0.31 m</td><td>MS (16 bands)</td></tr><tr><td>ESA (Europe)</td><td>Swath: 13.1 km</td><td>Crop mapping [64]</td></tr><tr><td>Since 2014</td><td>Temporal: ≤1 day</td><td></td></tr></table>

MS: Multispectral, HS: Hyperspectral

Satellites: Before the emergence of drones, satellites were the primary platform for agricultural remote sensing due to their widespread availability and costeffectiveness. Satellite- based remote sensing has played a crucial role in monitoring large- scale agricultural landscapes, providing valuable insights into crop health, soil conditions, and environmental factors. Satellites are equipped with a variety of sensors, including optical, multispectral, hyperspectral, radar, and thermal imaging technologies, making them versatile tools for precision agriculture [45].

One of the key advantages of satellite remote sensing is its ability to cover vast or inaccessible areas where traditional field- based data collection methods would be impractical. Several commercial and freely available satellites are equipped with image sensors. However, high- resolution commercial satellite images can be expensive, limiting access for smallholder farmers. A selection of available free and commercial satellites is summarized in Table 3.

Despite their advantages, satellites have inherent limitations. Cloud cover can obstruct their view, while atmospheric effects like scattering and absorption may distort the accuracy of the images they capture. As a result, cloud detection models and atmospheric correction techniques are required to adjust satellite radiation measurements and accurately interpret surface reflectance. Additionally, reflections from the surface or lower atmosphere may alter the true reflectance properties of agricultural materials, requiring further calibration [5].

Another challenge with widely used satellite systems, such as Landsat and Sentinel- 2, is their relatively low spatial resolution (typically 10- 30 meters), which restricts their ability to capture fine- scale agricultural variations. To address this, high- resolution commercial satellites, such as WorldView- 3 and Ikonos, have gained popularity in recent years [50]. These satellites offer spatial resolutions as high as 1- 3 meters, enabling detailed agricultural monitoring that medium- resolution satellites cannot achieve.

Beyond spatial resolution, commercial satellites often provide additional spectral bands and flexible revisit times. For instance, WorldView- 3 includes shortwave infrared and red- edge bands, which improve the detection of crop residues and vegetation characteristics. Additionally, many commercial satellite services allow on- demand tasks, offering higher- frequency data acquisition for specific agricultural regions compared to freely available satellites with fixed revisit schedules [45].

As an example of high- resolution commercial satellite application, a noteworthy study has been conducted by Shendryk et al. [65], which focuses on mapping the spread of Andropogon gayanus (gamba grass). Gamba

grass is an invasive pasture grass that is rapidly spreading through the tropical savannas of northern Australia, increasing fire intensity, and causing ecological damage. To effectively monitor and manage its spread, the researchers developed a machine learning model to ingest high- resolution WorldView- 3 satellite imagery. The results demonstrated that under optimal conditions, gamba grass can be mapped from satellite imagery with an accuracy of up to  $91\%$ . Additionally, spectral indices derived from the imagery significantly improved detection accuracy compared to using raw spectral bands alone.

Drones: While satellites remain indispensable for large- scale and long- term agricultural monitoring, drones have revolutionized precision agriculture by offering ultra- high- resolution imagery with greater flexibility. Advances in sensory and imaging technologies, along with improvements in data processing techniques, continue to enhance the role of drone remote sensing in modern precision farming.

Drones, also known as Unmanned Aerial/Aircraft Systems (UAS), offer a cost- effective way to collect aerial data. Although they generate large volumes of data that demand substantial storage and processing, drones can enable farmers to increase productivity and make informed decisions through real- time aerial observation, early disease detection, targeted interventions, and improved agricultural sustainability. A list of drones that have been or can be used in weed mapping is presented in Table 4. Specifically, their capability to flexibly cover large areas and generate high- resolution images aids in identifying and managing weed patches [66].

Site- specific weed management using drones is gaining popularity [67, 68]. This approach involves precisely targeting weed control methods to individual weeds or weed patches, accounting for spatial variability and temporal dynamics rather than uniformly treating the entire field. Since weeds typically grow in clusters rather than being evenly distributed, site- specific management presents a significant opportunity for reducing herbicide use while maintaining effective weed control [69].

The study in [67] explores a site- specific weed control approach in corn fields using a UAV to map weed distribution, generate a prescription map, and selectively spray using a commercial sprayer. A Crop Row Identification algorithm was developed to detect and remove corn rows from drone imagery, classifying remaining vegetation as weeds. A grid- based prescription map guided herbicide application, ensuring only grids with detected weeds were sprayed. This method reduced herbicide application by  $26.2\%$  compared to conventional practices, demonstrating the potential for reducing chemical use in corn production while maintaining effective weed control.

Table 4: The most common drone products in field monitoring that have been or can be applied in weed mapping.  

<table><tr><td>Drone Type</td><td>Sensor</td><td>Applications</td></tr><tr><td>Batmap, Nuvem
Fixed wing</td><td>RGB</td><td>Plant detection [70]</td></tr><tr><td rowspan="2">DJI, Matrice 100/300/600
Quadcopter</td><td>RGB</td><td>Yield estimation [71] field mapping for spraying [72], and plant growth analyses [73]</td></tr><tr><td>Multi-spectral</td><td>Pest infestation mapping [74], disease detection [75], and data fusion in agriculture [76]</td></tr><tr><td>DJI, Mavic 2/3/Air/Pro
Quadcopter</td><td>RGB</td><td>Plant growth analyses [73], plant detection [77, 78], pest detection [79], and weed detection [19]</td></tr><tr><td rowspan="2">DJI, Phantom 3/4
Quadcopter</td><td>RGB</td><td>Weed detection [80, 81], crop detection [78, 82], and field mapping [83]</td></tr><tr><td>Multi-spectral</td><td>Disease classification [84, 85] and plant health monitoring [86]</td></tr><tr><td>DJI, s1000
Octocopter</td><td>Multi-spectral</td><td>Plant detection [87] and plant health monitoring [88]</td></tr><tr><td>PFT, Firefly 6
Fixed wing</td><td>RGB</td><td>Field mapping [89]</td></tr><tr><td>Horus, Aeronaves
Fixed wing</td><td>RGB</td><td>Weed segmentation [90]</td></tr><tr><td>Microdrones, md4
Quadcopter</td><td>RGB</td><td>Annotated weed imagery dataset [91] and weed segmentation [92]</td></tr><tr><td>Parrot, Anafi
Quadcopter</td><td>RGB</td><td>Disease detection [75]</td></tr><tr><td>Parrot, Bluegrass
Quadcopter</td><td>Multi-spectral</td><td>Plant health monitoring [93] and field mapping [94]</td></tr><tr><td>Quantum systems, F90+
Fixed wing</td><td>Thermal</td><td>Disease classification [84]</td></tr><tr><td>SenseFly, Ebee
Fixed wing</td><td>RGB</td><td>NDVI greenness estimation [95]</td></tr></table>

To address the gap in sensor performance evaluation, Betitame et al. [96] compared the performance of UAV- mounted RGB and multispectral sensors in distinguishing crops, broadleaf weeds, and grasses in soybean fields. Using traditional classification algorithms and object- based image analysis in ArcGIS

Pro, results showed that the RGB sensor achieved  $93.8\%$  accuracy, while the multispectral sensor had a similar accuracy of  $93.4\%$ . The RGB sensor performed better at minimizing misclassifications and was particularly effective in detecting grass, while the multispectral sensor excelled in estimating total crop area due to its broader spectral range. Both sensors effectively classified background regions. Given the comparable performance, the less expensive RGB sensor may be more suitable for cost- effective precision agriculture applications.

Echallium elaterium (a.k.a., squirting cucumber) is a difficult- to- control weed in non- village olive groves, infesting inter- row cover crops. Given its patchy distribution, site- specific control strategies can be effective. The study conducted in [68] developed a UAV- based methodology to detect and map  $E$  elaterium infestations using RGB imagery. Conducted in two super- intensive olive orchards, UAV flights captured images in May (with multiple weed species) and September (when  $E$  elaterium was the sole weed). Classification using random forest models and an unsupervised algorithm achieved an overall accuracy of over 0.85, compared to the accuracy of human experts for  $E$  elaterium of over 0.74.

The study in [97] focused on developing a computer vision- based system for distinguishing potato plants from weeds in complex, high- ocelusion environments during the post- emergence stage. A dataset of 1,950 RGB images from potato farms was collected, annotated at the pixel level, and made publicly available. Deep learning models, i.e., Mask RCNN and YOLOv8, were trained for weed detection, with YOLOv8 achieving a mean average precision of  $83.4\%$  and Mask RCNN reaching  $79\%$ . While YOLOv8 slightly outperformed Mask RCNN in overall mAP, Mask RCNN achieved higher precision, recall, and F1- score for the weed class, making it more effective for weed identification.

In [98], volunteer cotton weed plants growing amidst inter- seasonal and rotated crops, such as corn, become susceptible hosts for boll weevil pests upon reaching the pin- head square stage (5- 6 leaf stage). Effective detection, localization, and targeted eradication or treatment of these weed plants are essential. This paper explored the application of machine/deep learning, specifically the YOLOv3 algorithm, to detect those weeds in corn fields using RGB images acquired by a UAV.

The importance of spatially explicit weed information for controlling infestations and minimizing corn yield losses is highlighted in [99]. UAV- based remote sensing offers an efficient approach to weed mapping, though thermal measurements (such as canopy temperature) have been underutilized. By integrating spectral, textural, structural, and canopy data, researchers identified optimal combinations for improved weed detection using machine learning algorithms. Results showed that incorporating canopy temperature and fusing textural, structural, and thermal features enhanced weed- mapping accuracy.

The research in [100] demonstrates how low- cost UAV platforms can effectively map giant smutgrass infestations in Florida bahiagrass pastures, enabling site- specific weed management and reducing herbicide use. RGB ortho- mosaics collected on two sampling dates (May and August) and at four different altitudes (50, 75, 100, and  $120\mathrm{m}$ ) were analyzed using spectral, texture, and combined approaches with both supervised and unsupervised classification methods. The best mapping results were achieved by integrating spectral and texture analyses with a supervised algorithm, yielding a correlation of 0.91 with ground truth data, although higher altitudes slightly reduced detection accuracy.

Table 5: The most common drone sprayers that have been or can be used in weed management.  

<table><tr><td>Drone application</td><td>Sprayer</td><td>Drone image</td></tr><tr><td>DJI, Agras T30</td><td>30 L tank</td><td rowspan="3">↓</td></tr><tr><td>Hexacopter</td><td>16 nozzles</td></tr><tr><td>Orchard farm [101]</td><td>8 L/min</td></tr><tr><td>DJI, Agras T40</td><td>70 L tank</td><td rowspan="3">↓</td></tr><tr><td>Quadcopter</td><td>4 nozzles</td></tr><tr><td>Sugarcane fields [102]</td><td>12 L/min</td></tr><tr><td>Freeman, 2000 series</td><td>60 L tank</td><td rowspan="3">↓</td></tr><tr><td>Fixed wing</td><td>9 nozzles</td></tr><tr><td>Open-field farms [103]</td><td>4.4 L/min</td></tr><tr><td>XAG, P-series</td><td>15 L tank</td><td rowspan="3">↓</td></tr><tr><td>Quadcopter</td><td>4 nozzles</td></tr><tr><td>Cotton farms [104]</td><td>30 L/min</td></tr><tr><td>XAG, V-series</td><td>16 L tank</td><td rowspan="3">↓</td></tr><tr><td>Bicopter</td><td>2 nozzles</td></tr><tr><td>Open-field farms [105]</td><td>10 L/min</td></tr><tr><td>Yamaha, Rmax</td><td>16 L tank</td><td rowspan="3">↓</td></tr><tr><td>Helicopter</td><td>3 nozzles</td></tr><tr><td>Pineapple farms [106]</td><td>8 L/min</td></tr></table>

In addition to data collection, drones can be used for precision spraying. Table 5 provides a selection list of drones for weed spraying. The table highlights various drone models tailored for agricultural spraying, each designed to optimize efficiency based on specific farming needs. Multi- copter models (e.g., DJI, XAG,

and Yamaha), suitable for smaller fields, feature different tank capacities and nozzle configurations to accommodate varying crop densities and in- flight maneuverability. Fixed- wing drones on the other hand (e.g., Freeman), are more suitable for open- field farms.

# IV. Data Processing

# Data

Building on the data collection technologies and methods outlined in the previous section, large volumes of data can be gathered, requiring intelligent processing algorithms with advanced capabilities. These algorithms can be applied in a variety of management applications including monitoring vegetation health, identifying crop stress, detecting weeds and insect infestations, and enabling precise application of treatments such as herbicides, pesticides, or fungicides [107]. To effectively develop processing algorithms for these applications, large and diverse datasets, capturing variability across different domains and collected using the collection technologies discussed, are essential. This, in turn, gives rise to the big data challenge in agriculture.

# Big Data

Big data refers to extremely large and/or diverse data types that are difficult to manage using traditional data processing tools. Agricultural data is especially getting big, due to the increasing use of technology like Internet of Things (IoT), drones, and satellites [108, 109]. Effectively handling heterogeneous agricultural data, such as environmental (temperature, humidity, rainfall), soil data (pH, moisture, nutrient levels), crop data (yield, health, growth stages, weed, pest, disease), and market data (prices, demand, supply), necessitates sophisticated data warehouses capable of storing, cleaning, standardizing, and integrating/fusing information from disparate sources [110]. Data storage and processing require scalable and cost- effective infrastructure, often leveraging cloud computing platforms. Hadoop [link] and other big data tools offer a promising solution to handle massive volumes of data generated in agriculture.

Cleaning data to remove noise and outliers, along with standardizing formats and protocols, is crucial for ensuring interoperability across diverse data sources. These processes enhance data quality and consistency, facilitating the aggregation and analysis of datasets from varied origins. As highlighted by Yu et al. [111], implementing reproducible data harmonization protocols (constructed from parameterizable primitive operations) enables transparent and scalable integration of heterogeneous weed mapping data. Such harmonized datasets support more effective comparisons, seasonal trend analyses, and accurate model training across different ecosystems/environments, aligning with the

FAIR (Findable, Accessible, Interoperable, and Reusable) principles of data stewardship.

# Data Fusion

Once cleaned and standardized, the data can be more easily fused to develop integrated systems that support precision agriculture, where timely and accurate information is critical. Data fusion techniques integrate information from multiple sources, including satellites, drones, sensor networks, and weather stations. By combining these diverse datasets, a more comprehensive understanding of field conditions is obtained, identifying key farming patterns, predicting risks, and enhancing the accuracy and reliability of agricultural decision- making [3].

Data fusion can be utilized for both imagery and non- imagery data types [112]. When it comes to imagery, various fusion methods are employed to integrate data from multiple sources, aiming to generate high- resolution images with enhanced spatial and spectral quality. A summary of the most used methods, their operational procedures, as well as their respective application in agricultural data handling, which have been or can be applied to weeds, is provided in Table 6. The table covers seven widely used methods: Brovey Transform, Intensity Hue Saturation (IHS), Principal Component Analysis (PCA), Wavelet Transform, Ehlers Fusion, and Gram- Schmidt (GS) Transform. These techniques aim to enhance spatial resolution while preserving spectral integrity by combining high- resolution panchromatic images with lower- resolution multispectral or hyperspectral images. Each method employs a distinct mathematical approach, ranging from spectral normalization and orthogonal transformations to frequency and component- based processing, to achieve effective fusion tailored to agricultural image analysis and precision weed detection.

In the context of agricultural monitoring, non- imagery data fusion incorporates a wide range of sources such as weather data, soil composition, water quality, pest and disease reports, historical yields, market prices, labor availability, etc. Multi- source integration of both imagery and non- imagery data enables a more holistic understanding of crop conditions, and environmental factors [99]. Weed detection particularly benefits from the utilization of fused data, offering effective differentiation between weeds and crops. For instance, Xu et al. [99] explored the use of data fusion for weed management by combining multiple types of spectral, textural, structural, and thermal measurements to improve weed mapping accuracy in corn fields. While thermal data (e.g., canopy temperature) had been underutilized, the research demonstrated that integrating it with other features significantly enhanced weed detection, boosting overall accuracy. The best performance was achieved by fusing textural, structural, and thermal features, with an machine learning model.

Table 6: Multi-source image data fusion techniques that have been or can be used in weed detection applications.  

<table><tr><td>Name</td><td>Application</td><td>Fusion process</td></tr><tr><td>Browley Transform (BT) [113]</td><td>Mergers high-res panchromatic and low-res multispectral images.
Enhances spatial detail while preserving spectral information.
Achieved by normalizing spectral bands and multiplying them with the panchromatic image.</td><td>Each band (Bi) of the multispectral image S is transformed using a high-resolution PAN image as Bi/ΣBn×PAN
The final fused image is reconstructed by combining these transformed bands SBT = {B1,B2,...}</td></tr><tr><td>Ehlers Fusion [114]</td><td>Implements a frequency-based fusion technique to RGB or multispectral images within the IHS color space.
Aims to preserve both spectral integrity and spatial resolution in hyperspectral and multispectral data.
Reduces spectral distortion compared to traditional fusion methods such as Brovey or standard IHS transformations.</td><td>Apply Fast Fourier Transform (F) to both the intensity and the high-resolution panchromatic images
Fi= F(I)
FPAN= F(PAN)
High-frequency components from the panchromatic image are selectively added to the intensity component (by adaptive filtering) to form Fi. Finally, apply Inverse FFT to return intensity back to the original space
I&#x27; = F-1(Fi)
SEhler = (I&#x27;,H,S)</td></tr><tr><td>Gram-Schmidt (GS) [115]</td><td>Enhances the spatial resolution of multispectral images using advanced image fusion techniques.
Maintains spectral integrity during the fusion process to ensure accurate color representation.
Uses these techniques in remote sensing and satellite image processing applications.</td><td>Each multispectral band (Bi) is transformed into an orthogonal basis using the GS process, which ensures that each new component (Bi) is uncorrelated with the previous ones. The first transformed component (Bi) is replaced with a high-resolution panchromatic image. The fused image is then reconstructed by the inverse GS transform SGS= GS-1(PAN,B2,...)</td></tr><tr><td>IHS [116]</td><td>Enhances the spatial resolution of RGB images to improve visual detail.
Preserves the natural color of the images during the enhancement process.
Acknowledges the potential for spectral distortion as a limitation of the method.</td><td>The process includes (1) converting RGB to IHS, (2) replacing the Intensity component, I, with a high-resolution panchromatic image, and (3) converting the new HIS image back to RGB.</td></tr></table>

<table><tr><td>Name</td><td>Application</td><td>Fusion process</td></tr><tr><td>Principal Component Analysis (PCA) [99]</td><td>Converts correlated multispectral image bands into a smaller set of uncorrelated components using PCA.
·Reduces data dimensionality by extracting principal components that capture the most significant variance.
·Utilizes the first principal component to carry and enhance spatial details of the image.
·Preserves spectral information while improving spatial resolution through component substitution.</td><td>For an input multispectral image S with the matrix of eigenvectors V, the PCA is PCA = VTS
We then replace the first PCA component with a high-resolution panchromatic image to form PCA&#x27;. Finally, we transform back the PCA&#x27; into the original spectral space.</td></tr><tr><td>Wavelet Transform [117]</td><td>Combines high-resolution panchromatic images with low-resolution multispectral images using a powerful fusion technique.
·Avoid simple arithmetic fusion methods that may compromise image quality.
·Preserves both spatial and spectral details effectively through wavelet-based fusion.</td><td>Both the panchromatic and multispectral images are decomposed into low-frequency (approx.) and high-frequency (detail) wavelet components.
The low-freq. of the panchromatic image will be added to the high-freq. multispectral coefficients.
The fused image will then be reconstructed by an inverse transformation.</td></tr></table>

Another noteworthy work is conducted by Xia et al. [118], where they introduced a novel approach to weed resistance management by developing a comprehensive resistance score and using multimodal data sources, i.e., spectral, structural, and textural, to map herbicide- resistant weeds. By employing deep learning and various fusion strategies, especially late deep fusion models, the researchers enhanced resistance assessment accuracy. The hyperspectral data proved most informative individually, but combining all modalities coupled with deep learning, significantly improved regression performance across different weed densities.

# Citizen Science

Citizen science in agriculture involves the active participation of non- specialists, such as farmers, in scientific research processes. This approach leverages the collective power of individuals to gather data, conduct experiments, and contribute to agricultural innovation. By engaging citizens, researchers can access vast amounts of localized data that would otherwise be difficult or expensive to collect. In agriculture, citizen science has been particularly valuable for on- farm testing of crop varieties, monitoring environmental conditions, and assessing pest and weed infestations.

Table 7: Publicly available annotated weed image datasets.  

<table><tr><td>Dataset name, publication year</td><td>Modality</td><td>Image Count</td><td>Annotation method</td></tr><tr><td colspan="4">Gathered by handheld devices</td></tr><tr><td>Carrot-weed, 2018</td><td>RGB camera</td><td>39</td><td>Segm. [link]</td></tr><tr><td>Leaf counting, 2018</td><td>RGB camera</td><td>9,372</td><td>Count [link]</td></tr><tr><td>Early-crop-weed, 2019</td><td>RGB camera</td><td>508</td><td>Class. [link]</td></tr><tr><td>DeepWeeds, 2019</td><td>RGB camera</td><td>17,509</td><td>Class. [link]</td></tr><tr><td colspan="4">Gathered by vehicles and robots</td></tr><tr><td>Crop/weed field image dataset, 2015</td><td>MS sensor</td><td>1,500</td><td>Segm. [link]</td></tr><tr><td>Sugar beets, 2016</td><td>NIR and RGB camera</td><td>25,429</td><td>Segm. [link]</td></tr><tr><td>Crop vs weed discrimination, 2019</td><td>NIR and RGB camera</td><td>40</td><td>Segm. [link]</td></tr><tr><td>Ladybird cobbitty brassica, 2019</td><td>Thermal, HS, RGB, weather, and soil data</td><td>2,245</td><td>Class. [link]</td></tr><tr><td>Open plant phenotyping of weeds, 2020</td><td>RGB camera</td><td>7,590</td><td>Det. [link]</td></tr><tr><td>The Rosario dataset, 2022</td><td>Stereo images and GPS positional data</td><td>15 per second</td><td>Det. [link]</td></tr><tr><td>Phenotyping in Weed Identification, 2024</td><td>RGB camera</td><td>28,000</td><td>Class. [link]</td></tr><tr><td>Weed-crop, 2025</td><td>RGB camera</td><td>3,020</td><td>Class. [link]</td></tr><tr><td colspan="4">Gathered by drones</td></tr><tr><td>Grass and broadleaf weeds, 2017</td><td>RGB camera</td><td>400</td><td>Segm. [link]</td></tr><tr><td>WeedNet, 2018</td><td>NIR sensor</td><td>465</td><td>Segm. [link]</td></tr><tr><td>Columbia invasive species, 2018</td><td>RGB images and GPS positional data</td><td>N/A</td><td>Det. [link]</td></tr><tr><td>Cynodon dactylon in vineyard, 2019</td><td>Photomosaic of RGB images</td><td>N/A</td><td>Segm. [link]</td></tr><tr><td>Weed detection projects, 2022</td><td>RGB camera</td><td>4,201</td><td>Det. [link]</td></tr><tr><td>SeSame, weed aerial dataset, 2023</td><td>RGB and NDVI camera</td><td>1,920</td><td>Det. [link]</td></tr><tr><td>Tobacco Dataset for crop/weed classification, 2023</td><td>RGB camera</td><td>1,600</td><td>Segm. [link]</td></tr><tr><td>Sandplain lupin weeds, 2023</td><td>Photomosaic of RGB images</td><td>578</td><td>Det. [link]</td></tr><tr><td>Broad-leaved pepper weed, 2024</td><td>MS sensor</td><td>26,763</td><td>Segm. [link]</td></tr></table>

<table><tr><td>Dataset name, publication year</td><td>Modality</td><td>Image Count</td><td>Annotation method</td></tr><tr><td>DroneWeed, 2024</td><td>RGB camera</td><td>31,002</td><td>Det. [link]</td></tr><tr><td colspan="4">Gathered from various sources</td></tr><tr><td>CottonWeedID15, 2023</td><td>RGB camera</td><td>584</td><td>Segm. [link]</td></tr><tr><td colspan="4">Segm: Segmentation, Det: Detection, Class: Classification
NIR: Near-infrared, MS: Multispectral, HS: Hyperspectral, N/A: Not Available</td></tr></table>

For instance, initiatives such as ClimMob [119] have created software to simplify experimental design and data collection, allowing farmers to engage in largescale trials that support agricultural practices like onfarm testing and experimental citizen science. The proliferation of smartphone technology has further enhanced this approach, allowing farmers to easily document and share observations, such as weed presence and crop health, in real- time [120].

Weed mapping is a critical application of citizen science in agriculture, as it provides spatial and temporal insights into weed distribution and density. Traditional weed mapping methods are labor- intensive and often limited in scope. However, citizen science can scale up data collection by involving farmers and the public in recording weed species and their locations across large areas. In this regard, geostatistical techniques combined with GPS- enabled devices [121] can been used to map weed populations in non- tillage systems.

The potential of citizen science for weed mapping extends beyond data collection to fostering collaboration between farmers, researchers, and policymakers. By involving farmers in the research process, citizen science projects can generate locally relevant solutions that are more likely to be adopted. Moreover, the data collected can inform sustainable weed management strategies, such as ecological redesign of cropping systems and the use of microbial nitrogen immobilization to suppress weed growth [122].

# Data Annotation

A fundamental objective shared across computer visionbased precision agriculture tasks is the accurate detection of specific objects of interest, e.g., weeds, crops, or fruits, while distinguishing them from the surrounding environment. Achieving this not only depends on well- designed model architecture and reliable hardware implementations but also requires robust supervised or semi- supervised data. This typically involves training machine learning models on carefully annotated images to enable accurate and consistent identification [123].

Image annotation is the process of labeling sufficiently large image sets with meaningful semantic information, which is crucial for training AI models. Creating large

scale annotated datasets is a challenging and resourceintensive task. It involves significant effort and cost for image collection, categorization, and annotation, as well as, in some cases, physicochemical analysis of crops [123]. One practical solution to these challenges is data sharing, which holds exciting potential for accelerating scientific advancements. Publicly available datasets not only reduce the time and cost associated with dataset preparation but also facilitate the benchmarking of image analysis and machine learning algorithms across different research groups.

The computer vision community has benefited from the availability of public annotated image datasets, which have driven major advances in object detection, segmentation, and the development of innovative model architectures. While there are several plant- specific image datasets available, many are not directly applicable to weed mapping. A collection of relevant annotated weed datasets is summarized in Table 7. This table presents a diverse collection of agricultural image datasets focused on weed monitoring, categorized by the method of data acquisition, i.e., handheld devices, ground vehicles/robots, drones, and mixed sources. These datasets span from 2015 to 2025 and cover a range of modalities, including RGB, NIR, spectral, and thermal imaging. Vehicle- and robot- acquired datasets are generally larger and more multimodal. Although some of these datasets additionally include GPS coordinates for weed localization, such geospatial metadata is not strictly necessary for designing and training accurate machine learning models.

Although several open- source weed datasets exist, there remains a significant gap in the availability of comprehensive, high- quality foundational datasets tailored to specific crops. While foundational AI models have achieved remarkable success in other domains, replicating this progress in agriculture requires large, diverse, and crop- specific datasets [124], for example, datasets focused on broadleaf weeds. The recent development of WeedNet [125] demonstrates promising progress towards global- scale weed species identification using a foundational model approach. However, despite its achievements, WeedNet also highlights the ongoing need for targeted, regionally adapted datasets and models that capture the nuances of specific cropping systems and agroecological contexts.

If ready- to- use datasets are not available for a new application, then new image datasets must be gathered, and image annotation tools need to be employed. Traditional annotation methods are usually manual, which make them time- consuming and labor- intensive, hence, impractical for large- scale agricultural datasets. Modern image annotation tools and techniques, on the other hand, enable significant advancements in precision applications by facilitating dataset creation. These tools can automate or semi- automate the annotation process, improving efficiency and accuracy. They often incorporate interactive elements, allowing users to refine annotations and correct errors, thereby enhancing the quality of the training data [126].

Semi- supervised learning techniques leverage both labeled and unlabeled data to improve active annotation learning model's performance, particularly when labeled data is scarce [127]. Transfer learning approaches utilize pre- trained models on large, general- purpose datasets and fine- tune them for specific agricultural tasks, accelerating the training process and improving accuracy. Furthermore, novel techniques like propagating labels from semantic neighborhoods can address issues such as class imbalance and incomplete labeling, common problems in agricultural datasets [128]. These techniques are combined with modern AI- assisted annotation tools, such as the Computer Vision Annotation Tool (CVAT) [link], Roboflow Annotate [link], and MakeSense [link], to provide efficient and accurate annotations for agricultural applications.

In contrast to all these closed vocabulary techniques, open- vocabulary semantic segmentation, enhanced by Large Language Models (LLMs), represents a significant advancement in few- shot segmentation of weeds/crops [129]. Close- vocabulary weed annotation techniques rely on a limited set of object classes, constraining their ability to identify new or unseen weed species.

Open- vocabulary approaches, however, leverage the semantic knowledge embedded in LLMs to recognize a broader range of plant species without requiring

![](https://cdn-mineru.openxlab.org.cn/extract/2d553dfd-344a-49ff-b6e5-3dbb91d7b1db/0c3de9792a2d5375f7c2d571b6a9bb38b907188781a2e02c2ab891a71839caef.jpg)  
Figure 5: Conceptual comparison between the most common machine learning approaches in data processing.

extensive retraining. This is achieved by aligning visual features with rich semantic features learned from vast amounts of text and image data [129]. For example, models like CLIP [link], which are pre- trained on largescale vision- language datasets, can be adapted to segment images based on textual descriptions of weed characteristics, even if those specific species were not present in the original training data [130]. This capability is crucial in agricultural settings where weed populations are diverse and constantly evolving. The integration of LLMs allows for more flexible and adaptable weed mapping systems that can respond to new challenges and changing environmental conditions.

Furthermore, Few- shot segmentation, a technique designed to perform image segmentation with minimal training examples, is particularly useful in weed mapping due to the excessive cost and effort associated with acquiring labeled data. By combining LLMs with few- shot learning techniques [130], researchers can develop robust weed mapping systems that require only a handful of annotated images to accurately segment different weed species.

# Machine/Deep Learning

Machine Learning (ML) and Deep Learning (DL) are foundational to the advancement of modern weed mapping technologies in agriculture. These computational methods have significantly outperformed traditional approaches in terms of detection accuracy, cost efficiency, and implementation adaptability. By leveraging intelligent algorithms, ML and DL facilitate various tasks such as weed identification, spatial mapping, resource optimization, and automated treatment strategies [131].

This section explores the major applications of ML in weed mapping, organized into four key areas: classification, detection, segmentation, and LLMs. These key application areas are illustrated in Figure 5. Classification models can identify the presence or absence of weeds in an image [132], but lack precise spatial information. Object detection models locate weeds by drawing bounding boxes around them, providing spatial coordinates but limited pixel- level detail [80]. Semantic and instance segmentation models classify each pixel in an image as either weed or crop, generating detailed weed maps and facilitating precise herbicide application [132]. While the application of LLMs in weed mapping is nascent, their potential lies in integrating contextual information with image data to answer end- users' queries. This can be particularly important in analyzing farmer's field notes and improving weed prediction and management [130].

# Classification

As stated before, weed classification involves categorizing different plant species, particularly distinguishing between weeds and crops, from images or sensor- derived data. This is essential for speciesspecific control and effective weed management strategies. Traditional Machine Learning: Algorithms like K- Nearest Neighbors (KNN), Random Forest, and Decision Trees remain effective for smaller datasets or environments with limited computational capabilities. These methods require manual feature extraction, such as color, shape, and texture descriptors, and are still viable for initial feasibility studies or resource- limited settings [41].

Modern DL architectures such as ResNet, EfficientNet, and Vision Transformers (ViTs) have demonstrated exceptional accuracy in plant classification tasks. These models automatically learn complex visual features and patterns from large agricultural image datasets, offering improved performance over handcrafted feature methods. Lightweight Convolutional Neural Networks (CNNs) are also widely used [133], especially for scenarios with complex backgrounds or constrained hardware resources [8].

# Detection

Weed detection focuses on locating the presence and position of weeds within an image or field. A variety of architectures are employed, with You Only Look Once (YOLO) variants, including YOLOv3 to YOLOv10, being particularly popular due to their speed and efficiency in real- time applications. For instance, when detecting volunteer cotton weed plants in corn fields, YOLOv3 achieved an average detection accuracy exceeding  $80\%$  with an F1- score of  $78.5\%$  [98].A study in 2025 compared YOLOv5 and YOLOv8 for weed detection in cotton farming, highlighting their effectiveness in identifying weeds that compete with cotton crops [134]. Furthermore, research explores modifications and enhancements to the YOLO architecture, such as the PMDNet model built upon YOLOv5, designed for efficient weed detection in wheat fields [135].

Beyond the YOLO family, other deep learning architectures are also being explored for weed detection. Region- based Convolutional Neural Networks (RCNNs) have been applied to detect and classify weeds in potato field, demonstrating the potential of these models in specific agricultural contexts [97]. ViTs are also being considered as effective DL architectures, where these attention- based models are implemented as intelligent weed control system in natural corn fields [136].

# Segmentation

Weed segmentation involves partitioning an image into distinct regions/pixels corresponding to crops and weeds. This provides a more detailed understanding of weed distribution and density compared to detection alone, allowing for precise herbicide application, reducing overall chemical usage, minimizing

environmental impact, and increasing/estimating yield [137]. Segmentation models are widely integrated into weed management robots and UAVs for automated weed detection and targeted herbicide application [72].

Recent research has focused on developing and improving segmentation models to address the specific challenges of weed detection, such as the similarity in spectral features between crops and weeds, variations in weed growth stages, and complex field environments. CNNs, particularly EfficientNet- based models and encoder- decoder architectures like U- Net, DeepLabV3, and PSPNet, are widely used for this advanced computer vision purpose [138].

Farmers usually plant a specific type of crop in their farms. Some studies use this opportunity and focus on segmenting the crop(s), and then classifying the remaining green objects as weeds to reduce model complexity [139]. Researchers are also exploring attention mechanisms and feature fusion techniques to improve segmentation accuracy and robustness in challenging field conditions [140].

Data augmentation techniques to increase the size and diversity of training datasets [141], synthetic data generation (i.e., creating realistic training samples) by pasting segmented plant patches onto soil backgrounds to address the scarcity of labeled data [142], and transfer- learning approaches to leverage knowledge from existing datasets and improve model performance in new environments or with different crop types [143] are among the other weed segmentation improvement solutions.

# Large Language Models

LLMs are increasingly being explored for their potential to revolutionize various aspects of the agricultural sector, including weed management. They offer a promising avenue for automating and enhancing annotation delays, especially without human expert involvement, leading to more efficient and targeted weed control strategies [144]. These models can integrate image features from DL models with textual contexts from natural language processing models to offer a unified query- able neural network.

LLMs are also being used to enhance named entity recognition for agricultural commodity monitoring, which indirectly impacts weed management [145]. Indirect weed detection has previously described as detecting crops first and then naming other green objects as weeds. Similarly, by pretraining transformer- based language models with food- related textual data, semantic matching between food descriptions and crop images can be established, offering insights into potential weed objects [146]. This approach can be expanded to identify and classify weeds based on textual descriptions and associated data.

The combination of Reinforcement Learning (RL) and LLMs represents a novel approach with transformative potential in the agricultural sector, offering adaptive strategies. In research conducted by Chen et al. [147], the study emphasizes the importance of efficient and sustainable crop production management, aiming to minimize environmental impacts through RL- LLM integration. Traditional methods struggle to adapt to the evolving dynamics influenced by climate change, soil variability, and market conditions, whereas RL- LLM integration has enhanced crop management decision support systems by optimizing decision- making through data- driven approaches. Despite considerable progress, challenges related to real- world deployment complexities remain.

# Edge Processing

Edge processing, defined as the deployment of ML and DL models on local devices rather than relying on cloud- based computing, holds significant promise in agricultural applications such as weed mapping. Traditional approaches often require extensive computational resources and suffer from latency issues when processing substantial amounts of data from remote locations. By contrast, edge processing allows for real- time analysis directly at the source, which is crucial for off- grid, time- sensitive, and/or continuous detection tasks in field vehicles/robots [148]. This capability is especially advantageous in environments where real- time monitoring and immediate response are necessary.

In weed mapping, edge processing offers several advantages. Firstly, it enables rapid identification and classification of weeds directly from captured images or sensor data. By deploying detection models locally on edge devices like vehicle- mounted cameras or drones, farmers can quickly assess the extent of weed infestations without relying on external networks, thus reducing dependency on internet connectivity and cloud services [149]. Additionally, real- time monitoring enabled by edge devices ensures that weed management strategies can be adjusted in- time based on evolving field conditions.

Edge processing has certain limitations, such as lower throughput, limited memory that restricts model complexity, and constrained energy availability. Nonetheless, it plays a crucial role in enabling faster and more precise weed control strategies. Once weeds are identified on edge, immediate management action can be taken. This approach not only enhances operational efficiency but also supports sustainable farming practices by reducing chemical usage and preserving soil health [149].

# V. Weed Mapping

# Spatiotemporal Patterns

Understanding the spatial and temporal distribution of weed species within agricultural and environmental systems presents a complex challenge due to the inherent heterogeneity of agroecosystems. Variability in weed distribution arises from both regional and local factors. At the regional scale, differences in climate, field management histories, landscape structure, and soil composition contribute to weed diversity. Locally, factors such as farmer expertise, cultural practices, soil characteristics, topography, and microclimatic conditions significantly affect weed emergence and distribution. Temporal dynamics of weed distribution are also essential for optimizing long- term management strategies. Weed patches keep changing spatially over time, including the annual changes in patch boundaries, and instabilities in their distributions [150].

Weed communities are shaped by the ecological requirements of species, such as growth form, phenological development, and sunlight requests. These traits, coupled with agricultural management practices, lead to noticeable spatial clustering of weeds within fields [151]. Numerous studies have documented that many weed species exhibit aggregated spatial distributions, which means they form patches rather than spreading uniformly [152]. Despite this, herbicides are often broadcast across fields, leading to overuse and environmental harm. Based on a study by Blank et al. [150],  $86\%$  of weed species exhibited patchy distributions. Aggregated patterns were dominant in key weed genera such as Avena. In contrast, some other genres like Chenopodium were found to be randomly distributed.

Seeds' weight, morphology, aerodynamic, and parent's height are other factors that influence the spatial distribution of weeds. Vegetative reproduction, as well as granivores further reinforce aggregation. Overall, most weed seeds fall near the parent plant, especially those without wind or water- assisted dispersal mechanisms, e.g., Ecballium elaterrum, which further emphasizes the benefit of weed mapping before any weed control application [153]. Conversely, winddispersed seeds, e.g., Taraxactum officinale, may produce more randomized distributions.

Temporal weed mapping is as important as its spatial patterns. However,  $63\%$  of studies spanned only one to two years, making them insufficient for assessing longterm temporal weed trends. Only  $6\%$  extended beyond five years. Species with wind- dispersed seeds or low population density tend to show less temporal stability. Understanding temporal trends in time- based weed mapping allows for strategic pre- emergence and postemergence herbicide applications based on historical data. For persistent weed patches, farmers can timely localize their pre- emergent herbicides, thus optimizing product efficiency. The exact timing of post- emergence treatments also depends on the weed emergence pattern to avoid inefficiencies and off- target effects [150].

# Farm Management Effects

Farm management practices significantly influence weed distribution by altering soil conditions, crop rotation patterns, and disturbance regimes. In this regard, cropping systems (i.e., crop type and its associated management practices) heavily influence the weed population and distribution dynamics. Crop canopy architecture, growth vigor, and competitive traits affect weed suppression [154]. For example, maize creates dense shade that limits weed growth, while onion with slow growth and weak canopy cover is a poor competitor. Mechanical cropping operations, like harvesting, also affect seed dispersal and subsequent weed distribution. For example, combine harvesters can spread seeds along the direction of travel, contributing to elongated weed patches [155].

Blank et al. [150] report that  $97\%$  of weed mapping studies focused on broadacre crops, with only  $1.5\%$  each in orchards and vineyards. Corn and wheat were the most frequently studied crops, comprising  $27\%$  and  $23\%$  of studies, respectively. Aggregated weed patterns were most common across major cereals, including maize, wheat, soybean, and barley. Crop competition traits, i.e., early canopy closure, tillering, and root expansion, affect the composition of weed communities. For example, dense crops may favor climbing species like convolvulus, while open- canopy crops benefit rosette- forming weeds. As a result, the need for frequent weed mapping is greater for variable farming practices, as well as species with unstable distributions. For example,

In rotating crops, the variability in field conditions leads to shifts in weed patch dynamics over time. In orchards, where UAVs cannot look under the treetops, understanding patch stability may be even more critical for effective weed management.

Another important farm management practice is the use of herbicides, including their types, dosages, and methods of application. Mapping herbicide usage and herbicide- resistant weeds is just as important as mapping the weeds themselves. Herbicides account for a huge portion of global weed control strategies, but the overuse of specific modes of action has led to widespread herbicide resistance in many weed species. Monitoring and mapping the occurrence of herbicide- resistant weeds are essential for timely detection and effective resistance management.

Table 8: Comparing the software tools commonly used in agricultural science and weed mapping.  

<table><tr><td>Tool</td><td>Description</td><td>Cost</td><td>Features</td><td>Use Cases</td></tr><tr><td>Agisoft Metashape</td><td>Photogrammetry software for 3D point clouds, orthophotos, and terrain models</td><td>Moderate</td><td>3D modeling, DSMs, vegetation structure analysis</td><td>UAV terrain modeling, weed/disease distribution [74]</td></tr><tr><td>ArcGIS Pro</td><td>Industry-standard GIS platform for advanced 2D/3D mapping and spatial analysis</td><td>Expensive</td><td>Advanced 2D/3D, spatial analysis, mobile/GPS integration</td><td>High-end research, enterprise-level Ag data, weed Treatment [156]</td></tr><tr><td>DroneDeploy</td><td>Cloud-based drone mapping platform with AI analysis and Ag modules</td><td>Moderate</td><td>NDVI, plant health, automatic report generation</td><td>Commercial Ag, UAV-based weed maps [81]</td></tr><tr><td>ENVI</td><td>Remote sensing software to process hyperspectral and multispectral images</td><td>Expensive</td><td>Spectral analysis, NDVI, land cover classification</td><td>High-end research, spectral weed detection [6]</td></tr><tr><td>ERDAS Imagine</td><td>Professional image processing tool for raster and satellite data analysis</td><td>Expensive</td><td>Raster modeling, remote sensing, 3D terrain analysis</td><td>Soil/vegetation analysis, GIS labs, weed segmentation [157]</td></tr><tr><td>Field Maps / Survey123</td><td>Mobile GIS apps for collecting georeferenced field data</td><td>Free to moderate</td><td>Offline mapping with GPS, data collection forms</td><td>Ground-truthing, weed survey/management [158]</td></tr><tr><td>Google Earth Engine</td><td>Cloud-based large satellite data analysis using code</td><td>Free for research</td><td>Massive data library, time series analysis</td><td>Remote sensing, regional weed/crop monitoring [83]</td></tr><tr><td>Pix4D</td><td>Drone image processing software for creating maps and 3D models</td><td>Moderate to High</td><td>Orthomosaics, NDVI, 3D modeling, photogrammetry</td><td>Field scouting, UAV-based weed maps [81]</td></tr><tr><td>QGIS</td><td>Open-source software for spatial analysis and mapping</td><td>Free</td><td>Plugin support, raster and vector analysis, basic 3D</td><td>Academic research, weed and disease mapping [74]</td></tr><tr><td>SST Summit / SMS Advanced</td><td>Precision ag software for analyzing field data, generating zones, and prescriptions</td><td>Moderate to High</td><td>Yield maps, variable rate, field analysis tools</td><td>Precision farming, crop and weed management [159]</td></tr><tr><td>Trimble Ag / Farm Works</td><td>Integrated farm management software with GPS and variable rate technology</td><td>High</td><td>GPS, soil/plant data, input prescriptions</td><td>Farm decision support, weed detection [160]</td></tr></table>

Tools such as geo- referenced databases and interactive web- based platforms enable researchers, advisors, and policymakers to visualize the spread of resistant populations, facilitating more targeted and sustainable weed control strategies [161]. For example, Weedscout 2.0 has been developed to track herbicide- resistant Alopecurus species across parts of Europe, while the iMAR system in Italy allows for continuous updates and visualization of resistance data in Echinochloa species [162].

Global efforts to maintain an accurate database of herbicide- resistant weed cases are led by the International Herbicide- Resistant Weed Database [link], offering detailed maps based on herbicide mode of action. Tools like this are not only useful for farmers and researchers but also for policymakers designing integrated weed management frameworks, ensuring that herbicide application remains effective and sustainable.

As can be seen, enhancing farm management, particularly in weed control, requires software- based spatiotemporal data visualization on weed distribution, soil conditions, and crop health. Satellite, drone, and field observation data can be visualized by GIS maps and tools, providing a strong decision- support basis in agriculture. These tools will be studied in detail in the next section.

# Common Maps and Tools

2D and 3D thematic maps are essential tools in weed mapping applications, for visualizing spatial data, analyzing field conditions, and supporting precision management. A breakdown of the most common types of 2D maps used in this context include: Choropleth Maps to display variations of a variable (e.g., weed density or zoned statistics) using color gradients; Dot Density Maps to represent frequency of features (e.g., weed populations or distribution patterns) with dots; Isoline/Contour Maps to connect points of equal value (e.g., farm/land topography or soil parameters levels) by lines; Raster Maps of grid cells (e.g., weed vigor or vegetation indices) where each cell holds a value; Symbol Maps with proportional symbols and their sizes (e.g., weed biomass or herbicide intensity) according to data magnitude; and Heat Maps to represent data density or intensity (e.g., weed infestation zones or hotspots) with color gradients.

Similarly, the most common 3D Maps in weed mapping applications include: Digital Elevation Models to visualize elevation and topography (in weed intensity studies, water flow calculations, irrigation planning, and soil conservation acts); Point Cloud Maps from Light Detection and Ranging (LiDAR) or UAVs to visualize field surfaces (in weed structure analyzes, weed biomass

estimation, and canopy analysis); 3D Vegetation Index Maps to combine remote sensing data with height models to give a volumetric perspective (in weed- crop competition assessment and plant health monitoring); and 3D Time Series Maps to show changes over time with height and intensity layers (in weed or crop growth evaluation and temporal weed dynamics/development).

A comparison between the key software packages in agricultural science and weed mapping is presented in Table 8. This table summarizes the most common tools based on their cost, ease of use, key features, and application scenarios. This comparison is helpful in choosing the right tool depending on project's needs, whether it is academic research, commercial farm management, or field surveying.

# VI. Future Directions

VI. Future DirectionsAlthough modern technologies for weed mapping have advanced significantly, many barriers are left unaddressed, preventing these advancements from being used in real-world applications. Key challenges include the lack of practical and cohesive data and outdated hard and soft technologies. This underscores the need for balanced and unbiased data collection, and modern deep learning analysis, and more intuitive weed mapping techniques to meet diverse agricultural demands. This section explores some of these major challenges in depth, highlighting key opportunities for advancing data-driven solutions to support the evolving needs of precision weed management.

# Data Acquisition

# Environmental Diversity

Comprehensive annotated datasets that encompass various weed growth stages and environmental conditions will enhance ML model robustness and generalizability across diverse agricultural settings. Future studies should incorporate multi- regional trials that consider environmental variables such as climate, vegetation types, and seasonal shifts [91]. Trials and data collection conducted across different regions and at varied times of day will increase the robustness and transferability of weed detection models. Besides, there is a pressing need for long- term and multi- season data collection to better understand temporal weed distribution and to evaluate management strategies over time.

# Early-stage Data

Accurate detection of weeds and plant diseases in their early development stages is still limited. New research should develop technologies capable of collecting data and identifying weeds before outbreak being visible, potentially using machine learning- enhanced remote sensing methods [105]. This also counts for sparse weed densities, especially at lower thresholds, to prevent misclassification and enhance weed resistance evaluation accuracy. Accurate detection of weeds in their early development stage would also translate into more effective weed control as younger weeds are easier to control with herbicides at lower rates.

# Remote Sensing Constraints

UAVs often lack the space and frequency resolution sensors necessary for precise weed identification. Future advancements are expected to focus on wideband or multi- band, as well as high- resolution hyperspectral and multispectral sensors to enhance the precision of weed identification [96]. Compared to RGB cameras, spectral sensors provide richer information, enabling more accurate discrimination of plant species.

In addition to sensor integration, optimizing the power consumption of UAV embedded systems is crucial for developing low- cost, long- endurance drones suitable for high- range agricultural applications. Sensors and onboard processing units can be energy- intensive, limiting flight times and operational efficiency. By optimizing both hardware and software components for energy efficiency, future UAVs can achieve longer flight durations, covering larger areas.

# Internet of Agricultural Things

Internet of Agricultural ThingsAdvancing the use of IoT networks, including Bluetooth Low Energy, Radio- Frequency Identification (RFID), and IP- based sensors will allow better data collection, tracking, and monitoring of weeds and associated biosecurity threats across the agricultural supply chain. Towards this end, solving interoperability issues between devices, platforms, and datasets is critical [4]. Open- source standards and platform- agnostic data formats will facilitate smoother integration and decision- making across the agricultural ecosystem.

# Citizen Science

Citizen ScienceAn emerging and highly scalable approach to addressing the challenges of weed control data collection is the integration of citizen science with smartphone- based imaging. With over five billion unique mobile subscribers worldwide, engaging local communities in image data collection offers a cost- effective and logistically feasible alternative to conventional methods [120]. However, image quality and consistency remain critical challenges.

# Data Processing

# Data Fusion Techniques

Data ProcessingData Fusion TechniquesEspecially in the realm of spectral imaging, the future of weed detection is centered around the fusion of multispectral and hyperspectral data with deep learning methodologies. The utilization of vegetation indices, such as Normalized Difference Vegetation Index (NDVI) and Green NDVI (GNDVI), derived from spectral bands, provides valuable information on plant

health and stress levels, aiding in the discrimination between crops and weeds. In the meantime, the fusion of multi- source data (e.g., UAV, satellite, IoT) offers promise for high- resolution, real- time weed mapping [9]. Future research should prioritize data fusion models that leverage deep learning to integrate multi- source spatiotemporal data seamlessly.

# Image Annotation & Segmentation

Image Annotation & SegmentationRobust annotation tools that can manage occlusions, lighting variations, crop diversity, and the complex morphology of weeds are necessary. Advancements in automated annotation methods, such as semi- supervised learning frameworks utilizing adversarial strategies, have shown promise in reducing the manual effort required for pixel- level annotations [163]. Additionally, the integration of multi- sensor segmentation techniques, combining data from RGB, multispectral, and hyperspectral sensors, can enhance the accuracy of weed identification by leveraging the strengths of each modality. AI- assisted annotation platforms, like those employing superpixel algorithms, offer interactive and efficient means to annotate complex plant structures, thereby accelerating the creation of high- quality annotated datasets.

# Generative AI

Generative AIGenerative AI offers a solution to the challenge of data scarcity in weed mapping by enabling the creation of synthetic datasets that mimic real- world conditions. Techniques such as diffusion models and generative adversarial networks can generate high- fidelity images of various weed species under different environmental conditions, enhancing the robustness of detection models. These synthetic datasets can be used to train deep learning models, improving their performance in real- world scenarios where annotated data is limited. Additionally, combining synthetic data with real- world data through domain adaptation techniques can further enhance model generalization [141]. Nonetheless, challenges remain in ensuring the realism of synthetic data and its alignment with actual field conditions, necessitating ongoing research to refine these methods.

# Advanced Models on the Edge

Advanced Models on the EdgeThe deployment of efficient and lightweight models, such as YOLO and Region- Fusion Detection Transformer (RF- DETR), on edge devices like drones and autonomous ground vehicles is anticipated to facilitate on- the- fly weed identification and mapping. This real- time capability is crucial for implementing precision agriculture practices, enabling timely and targeted weed management interventions [148]. The incorporation of ensemble learning techniques is also expected to improve detection accuracy by combining predictions from multiple models, thereby mitigating the limitations of individual models in complex field scenarios [138]. Furthermore, the integration of temporal data through time- series analysis is expected to capture the phenological changes of vegetation, enhancing the detection of weed emergence patterns over time.

# Vision Language Models

Vision Language ModelsThe integration of VLMs into weed mapping presents promising avenues for enhancing annotation efficiency and detection accuracy. VLMs can assist in automating the weed annotation process by interpreting complex weed imagery, thereby reducing the reliance on manual labelling. This capability is particularly beneficial in scenarios involving occlusions and diverse crop types. Moreover, VLMs can be fine- tuned to understand the nuances of different weed species, enabling more precise identification and classification [147]. However, to ensure reliability and affordability, further research is needed to optimize these models for agricultural applications, considering factors such as computational resources and the need for explainable AI to gain trust among end- users.

# Mapping and Interpretation

# Spatiotemporal Distribution Modelling

Mapping and InterpretationSpatiotemporal Distribution ModellingFuture works need to expand spatial pattern analysis across diverse geographies and multi- year timelines. Current models often lack the capacity to capture the dynamic nature of weed populations over space- time, limiting their effectiveness in long- term management strategies. This modelling is essential for understanding the persistence and evolution of weed populations in varying agricultural landscapes [150]. Moreover, future research should focus on improving seed dispersal modelling, including natural [153] and equipment- driven [155] mechanisms for better understanding/interpreting spatial distribution of weeds. Additionally, the effect of other factors such as soil type, moisture levels, and topography, on weed distribution, establishment, and proliferation need to be studied [152]. Integrating these variables into spatiotemporal models can provide a more comprehensive understanding of weed dynamics, leading to more effective and site- specific management strategies.

# Real-Time Decision Support

Real- Time Decision SupportFuture advancements in real- time decision support systems for weed control can integrate advanced detection techniques and weed density and distribution models to facilitate site- specific management strategies. By leveraging technologies such as UAVs, IoT, and ML models, these systems can provide farmers with timely, actionable insights tailored to their specific field conditions [105]. These decision support systems should incorporate user- friendly interfaces to ensure that farmers, regardless of their technical expertise, can interpret and act upon the data effectively. Moreover, the integration of predictive analytics allows for

proactive weed management, optimizing resource allocation and minimizing environmental impact.

# Global Biosecurity Governance

Weed mapping as a biosecurity measure requires a multilateral governance approach. Establishing international conventions [2] and promoting open- data ecosystems [120] will foster collaboration and accelerate response to invasive threats. Future research should focus on making global weed mapping information affordable and accessible to small- scale farmers. This includes the development of user- friendly and mobile platforms, along with farmer- centric training programs.

# VII. Conclusion

This review systematically explored the landscape of weed mapping by analyzing the latest advancements in data acquisition, processing, and mapping techniques. We identified the major sensing platforms, ranging from handheld and vehicle- mounted devices to UAVs and satellites, and evaluated their integration with RGB, spectral, NIR, thermal, and terahertz imaging technologies. In the data processing domain, we reviewed deep learning- based approaches for data annotation, weed classification, detection, and segmentation, as well as the emerging use of edge computing and large language models for real- time, infield processing. By focusing on spatial and temporal weed dynamics, as well as the influence of farm management practices, this review also shed light on the essential role of GIS- based mapping tools in supporting informed and targeted weed control decisions.

Importantly, this work fills a critical gap in the literature by being the first systematic review dedicated solely to weed mapping, following the PRISMA methodology to ensure methodological strength and transparency. The findings serve as a comprehensive knowledge base for scientists, Agri- tech developers, and decision- makers, helping them understand current capabilities, limitations, and opportunities for innovation. The insights presented herein not only guide future research in the design of smarter, data- driven weed management systems, but also support the broader goal of sustainable agriculture through reduced chemical usage and enhanced crop and environment health. As such, this review is positioned to influence both scientific inquiry and practical implementation in the evolving landscape of precision weed management.

# Acknowledgements

This research is supported by the Australian Research Council Industrial Transformation Research Program (ITRP) through the Training Centre in Plant Biosecurity (IC230100027).

# References

1. Thakur, A., S. Venu, and M. Gurusamy, An extensive review on agricultural robots with a focus on their perception systems. Computers and Electronics in Agriculture, 2023. 212: p. 108146.  
2. Hulme, P.E., Importance of greater interdisciplinarity and geographic scope when tackling the driving forces behind biological invasions. Conservation Biology, 2022. 36(2): p. 13817.  
3. Padhiary, M., et al., Enhancing precision agriculture: A comprehensive review of machine learning and AI vision applications in all-terrain vehicle for farm automation. Smart Agricultural Technology, 2024. 8: p. 100483.  
4. Dhanasekar, S., A comprehensive review on current issues and advancements of Internet of Things in precision agriculture. Computer Science Review, 2025. 55: p. 100694.  
5. Waters, E.K., C.C.-M. Chen, and M. Rahimi Azghadi, Sugarcane health monitoring with satellite spectroscopy and machine learning: A review. Computers and Electronics in Agriculture, 2025. 229: p. 109686.  
6. Sarvestani, G.S., et al., Early Season Dominant Weed Mapping in Maize Field Using Unmanned Aerial Vehicle (UAV) Imagery: Towards Developing Prescription Map. Smart Agricultural Technology, 2025: p. 100956.  
7. Rahimi Azghadi, M., et al., Precision robotic spot-spraying: Reducing herbicide use and enhancing environmental outcomes in sugarcane. Computers and Electronics in Agriculture, 2025. 235: p. 110365.  
8. Panacho Ferreira, B., et al., Evaluating Deep Learning Models for Effective Weed Classification in Agricultural Images. Revista de Informática Teórica e Aplicada, 2025. 32(1): p. 265.  
9. Mensah, B., et al., Advances in weed identification using hyperspectral imaging: A comprehensive review of platform sensors and deep learning techniques. Journal of Agriculture and Food Research, 2024. 18: p. 101388.  
10. Dobbs, A.M., et al., New directions in weed management and research using 3D imaging. Weed Science, 2022. 70(6): p. 641.  
11. Zhang, H., et al., Laser and optical radiation weed control: a critical review. Precision Agriculture, 2024. 25(4): p. 2033.  
12. Elias, S., Seed quality testing, in Handbook of seed science and technology. 2024, CRC Press. p. 561.  
13. Raja, R., et al., Real-time weed-crop classification and localisation technique for robotic weed control in lettuce. Biosystems Engineering, 2020. 192: p. 257.  
14. Saleh, A., et al., FieldNet: Efficient real-time shadow removal for enhanced vision in field robotics. Expert Systems with Applications, 2025. 279: p. 127442.  
15. Dadashzadeh, M., et al., A stereoscopic video computer vision system for weed discrimination in rice field under both natural and controlled light conditions by machine learning. Measurement, 2024. 237: p. 115072.  
16. Ram, B.G., et al., A systematic review of hyperspectral imaging in precision agriculture: Analysis of its current

state and future prospects. Computers and Electronics in Agriculture, 2024. 222: p. 109037.

17. Pena, J.M., et al., Weed Mapping in Early-Season Maize Fields Using Object-Based Analysis of Unmanned Aerial Vehicle (UAV) Images. Public Library of Science, 2013. 8(10): p. 77151.

18. G C, S., et al., Weed and crop species classification using computer vision and deep learning technologies in greenhouse conditions. Journal of Agriculture and Food Research, 2022. 9: p. 100325.

19. Mawardi, Z., D. Gautam, and T.G. Whiteside, Utilization of Remote Sensing Dataset and a Deep Learning Object Detection Model to Map Siam Weed Infestations. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2024. 17: p. 18939.

20. Rasmussen, J., et al., Pre-harvest weed mapping of Cirrium arvense in wheat and barley with off-the-shelf UAVs. Precision Agriculture, 2019. 20(5): p. 983.

21. Rasmussen, J., et al., Potential uses of small unmanned aircraft systems (UAS) in weed research. Weed Research, 2013. 53(4): p. 242.

22. de Castro, A.I., et al., Mapping Cynodon dactylon in vineyards using UAV images for site-specific weed control. Advances in Animal Biosciences, 2017. 8(2): p. 267.

23. Souza, M.F.d., et al., Spectral differentiation of sugarcane from weeds. Biosystems Engineering, 2020. 190: p. 41.

24. LOPEZ-GRANADOS, F., et al., Multispectral classification of grass weeds and wheat (Triticum durum) using linear and nonparametric functional discriminant analysis and neural networks. Weed Research, 2008. 48(1): p. 28.

25. Reddy, K.N., et al., Glyphosate-resistant and glyphosate-susceptible Palmer amaranth (Amaranthus palmeri S. Wats.): hyperspectral reflectance properties of plants and potential for classification. Pest Management Science, 2014. 70(12): p. 1910.

26. Scherrer, B., et al., Hyperspectral imaging and neural networks to classify herbicide-resistant weeds. Journal of Applied Remote Sensing, 2019. 13(4): p. 044516.

27. Louargant, M., et al. Unsupervised Classification Algorithm for Early Weed Detection in Row-Crops by Combining Spatial and Spectral Information. Remote Sensing, 2018. 10.

28. Lopez-Granados, F., et al., Object-based early monitoring of a grass weed in a grass crop using high resolution UAV imagery. Agronomy for Sustainable Development, 2016. 36(4): p. 67.

29. Rahkonen, J. and H. Jokela, Infrared Radiometry for Measuring Plant Leaf Temperature during Thermal Weed Control Treatment. Biosystems Engineering, 2003. 86(3): p. 257.

30. Abdelaal, K., et al., Physiological and Biochemical Changes in Vegetable and Field Crops under Drought, Salinity and Weeds Stresses: Control Strategies and Management. Agriculture, 2022. 12(12): p. 2084.

31. Haworth, M., et al., Impaired photosynthesis and increased leaf construction costs may induce floral

32. Shen, Y., et al., Detection of impurities in wheat using terahertz spectral imaging and convolutional neural networks. Computers and Electronics in Agriculture, 2021. 181: p. 105931.  
33. Ahmadi, A., et al., BonnBot-I Plus: A Bio-Diversity Aware Precise Weed Management Robotic Platform. IEEE Robotics and Automation Letters, 2024. 9(7): p. 6560.  
34. Zhao, P., et al., Design and Testing of an autonomous laser weeding robot for strawberry fields based on DIN-LW-YOLO. Computers and Electronics in Agriculture, 2025. 229: p. 109088.  
35. Ebrahimi, M.A., et al., Vision-based pest detection based on SVM classification method. Computers and Electronics in Agriculture, 2017. 137: p. 52.  
36. Bouguettaya, A., et al., Deep learning techniques to classify agricultural crops through UAV imagery: a review. Neural Computing and Applications, 2022. 34(12): p. 9511.  
37. Istiak, M.A., et al., Adoption of Unmanned Aerial Vehicle (UAV) imagery in agricultural management: A systematic literature review. Ecological Informatics, 2023. 78: p. 102305.  
38. Partel, V., L. Costa, and Y. Ampatzidis, Smart tree crop sprayer utilizing sensor fusion and artificial intelligence. Computers and Electronics in Agriculture, 2021. 191.  
39. Chang, C.-L., B.-X. Xie, and S.-C. Chung, Mechanical Control with a Deep Learning Method for Precise Weeding on a Farm. Agriculture, 2021. 11: p. 1049.  
40. Zhang, L., et al., A quadratic traversal algorithm of shortest weeding path planning for agricultural mobile robots in cornfield. Journal of Robotics, 2021. 2021(1): p. 6633139.  
41. Xu, B., L. Chai, and C. Zhang, Research and application on corn crop identification and positioning method based on Machine vision. Information Processing in Agriculture, 2023. 10(1): p. 106.  
42. Gao, G., K. Xiao, and Y. Jia, A spraying path planning algorithm based on colour-depth fusion segmentation in peach orchards. Computers and Electronics in Agriculture, 2020. 173: p. 105412.  
43. Kim, J., et al. An Intelligent Spraying System with Deep Learning-based Semantic Segmentation of Fruit Trees in Orchards. in International Conference on Robotics and Automation (ICRA). 2021. IEEE.  
44. Raja, R., et al., Real-time precision crop identification in high weed-density environments for robotic weed control using spectral fluorescence imaging in celery. Computers and Electronics in Agriculture, 2025. 231.  
45. Yang, L., et al., Applications of remote sensing for crop residue cover mapping. Smart Agricultural Technology, 2025. 11: p. 100880.  
46. Alam, M.M.T., et al., Optimizing Empirical and Hybrid Modeling for Advanced Canopy Chlorophyll and Nitrogen Retrieval Technique Using EnMAP Data. Environmental Challenges, 2025. 18: p. 101114.

47. Dahiya, N., et al., Chapter 13 - Crop land assessment with deep neural network using hyperspectral satellite dataset, in Hyperautomation in Precision Agriculture, S. Singh, et al., Editors. 2025, Academic Press. p. 159.

48. Galloza, M.S., M.M. Crawford, and G.C. Heathman, Crop Residue Modeling and Mapping Using Landsat, ALI, Hyperion and Airborne Remote Sensing Data. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2013. 6(2): p. 446.

49. Bukhamsin, A., et al., Early and high-throughput plant diagnostics: strategies for disease detection. Trends in Plant Science, 2025. 30(3): p. 324.

50. Arrechea-Castillo, D.A. and Y.T. Solano-Correa, Chapter 14 - Deep learning in multi-sensor agriculture and crop management, in Deep Learning for Multi-Sensor Earth Observation, S. Saha, Editor. 2025, Elsevier. p. 335.

51. Trivedi, S., et al., Chapter 15 - Assessment of agroforestry land use systems for sustainable agriculture development: geospatial perspective using AI, in Sustainable Development Perspectives in Earth Observation, M.D. Behera, et al., Editors. 2025, Elsevier. p. 249.

52. Matongera, T.N., et al., Detection and mapping the spatial distribution of bracken fern weeds using the Landsat 8 OLI new generation sensor. International Journal of Applied Earth Observation and Geoinformation, 2017. 57: p. 93.

53. Mor-Mussery, A., et al., Quantifying the dynamic of cereals and broadleaf plants in semi-arid grasslands using a high-spatial-resolution satellite imaging. Agriculture, Ecosystems & Environment, 2025. 377: p. 109233.

54. Rahali, L., et al., CubeSat installations: New era for precision agriculture? Computers and Electronics in Agriculture, 2025. 230: p. 109764.

55. Sari, I.L., et al., Tree counting of tropical tree plantations using the maximum probability spectral features of high-resolution satellite images and drones. Geomatica, 2025. 77(1): p. 100045.

56. Vaglio Laurin, G., et al., Monitoring habitat diversity with PRISMA hyperspectral and lidar-derived data in Natura 2000 sites: Case study from a Mediterranean forest. Ecological Indicators, 2025. 172: p. 113254.

57. Pepe, M., et al., Mapping spatial distribution of crop residues using PRISMA satellite imaging spectroscopy. European Journal of Remote Sensing, 2023. 56(1): p. 2122872.

58. Palakuru, M., et al., Investigation of Rice Crop Phenology Using C Band SENTINEL-1 SAR Data: A Case Study in Chittoor, Andhra Pradesh. Heliyon, 2025: p. 42900.

59. Xiao, T., et al., Identification of soybean planting areas using Sentinel-1/2 remote sensing data: A combined approach of reduced redundancy feature optimization and ensemble learning. European Journal of Agronomy, 2025. 164: p. 127480.

60. Karimi, N., et al., An advanced high resolution land use/land cover dataset for Iran (ILULC-2022) by focusing on agricultural areas based on remote sensing

data. Computers and Electronics in Agriculture, 2025. 228: p. 109677. 61. Rasmussen, J., S. Azim, and J. Nielsen, Pre- harvest weed mapping of Cirsium arvense L. based on free satellite imagery - The importance of weed aggregation and image resolution. European Journal of Agronomy, 2021. 130: p. 126373. 62. Rouault, P., et al., High- resolution satellite imagery to assess orchard characteristics impacting water use. Agricultural Water Management, 2024. 295: p. 108763. 63. Liu, J., et al., Plant diversity on islands in the Anthropocene: Integrating the effects of the theory of island biogeography and human activities. Basic and Applied Ecology, 2023. 72: p. 45. 64. Quemada, M., et al., Improved crop residue cover estimates obtained by coupling spectral indices for residue and moisture. Remote Sensing of Environment, 2018. 206: p. 33. 65. Shendryk, Y., et al., Leveraging High- Resolution Satellite Imagery and Gradient Boosting for Invasive Weed Mapping. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2020. 13: p. 4443. 66. Anam, I., et al., A systematic review of UAV and AI integration for targeted disease detection, weed management, and pest control in precision agriculture. Smart Agricultural Technology, 2024. 9: p. 100647. 67. Sapkota, R., et al., Towards reducing chemical usage for weed control in agriculture using UAS imagery analysis and computer vision techniques. Scientific Reports, 2023. 13(1). 68. Torres- Sanchez, J., et al., Detection of Ecballium elaterium in hedgerow olive orchards using a low- cost uncrewed aerial vehicle and open- source algorithms. Pest Management Science, 2023. 79(2): p. 645. 69. Canicatti, M. and M. Vallone, Drones in vegetable crops: A systematic literature review. Smart Agricultural Technology, 2024. 7: p. 100396. 70. Rosa, L.E.C.L., et al. FCRN- Based Multi- Task Learning for Automatic Citrus Tree Detection From UAV Images. in Latin American GRSS & ISPRS Remote Sensing Conference (LAGIRS). 2020. IEEE. 71. Qu, H., et al., A fast and efficient approach to estimate wild blueberry yield using machine learning with drone photography: Flight altitude, sampling method and model effects. Computers and Electronics in Agriculture, 2024. 216: p. 108543. 72. Rayamajhi, A., H. Jahanifar, and M.S. Mahmud, Measuring ornamental tree canopy attributes for precision spraying using drone technology and self- supervised segmentation. Computers and Electronics in Agriculture, 2024. 225: p. 109359. 73. Shen, L., et al., GSP- AI: An AI- Powered Platform for Identifying Key Growth Stages and the Vegetative- to- Reproductive Transition in Wheat Using Trilateral Drone Imagery and Meteorological Data. Plant Phenomics, 2024. 6: p. 255. 74. Amarasingam, N., et al., Mapping of insect pest infestation for precision agriculture: A UAV- based multispectral imaging and deep learning techniques.

International Journal of Applied Earth Observation and Geoinformation, 2025. 137: p. 104413.

75. Su, J., et al., Aerial Visual Perception in Smart Farming: Field Study of Wheat Yellow Rust Monitoring. IEEE Transactions on Industrial Informatics, 2021. 17(3): p. 2242.  
76. Barrile, V., et al. Experimenting Agriculture 4.0 with Sensors: A Data Fusion Approach between Remote Sensing, UAVs and Self-Driving Tractors. Sensors, 2022. 22.  
77. Akdogan, C., T. Ozer, and Y. Oguz, PP-YOLO: Deep learning based detection model to detect apple and cherry trees in orchard based on Histogram and Wavelet preprocessing techniques. Computers and Electronics in Agriculture, 2025. 232: p. 110052.  
78. Hajjaji, Y., et al., Enhancing palm precision agriculture: An approach based on deep learning and UAVs for efficient palm tree detection. Ecological Informatics, 2025. 85: p. 102952.  
79. Ichim, L., R. Ciciu, and D. Popescu. Using Drones and Deep Neural Networks to Detect Halyomorpha Halys in Ecological Orchards. in International Geoscience and Remote Sensing Symposium. 2022. IEEE.  
80. Rai, N. and X. Sun, WeedVision: A single-stage deep learning architecture to perform weed detection and segmentation using drone-acquired images. Computers and Electronics in Agriculture, 2024. 219: p. 108792.  
81. Singh, V., D. Singh, and H. Kumar, Efficient Application of Deep Neural Networks for Identifying Small and Multiple Weed Patches Using Drone Images. IEEE Access, 2024. 12: p. 71982.  
82. Rehman, M.U., et al., Advanced drone-based weed detection using feature-enriched deep learning approach. Knowledge-Based Systems, 2024. 305: p. 112655.  
83. Hu, T., et al., High-resolution mapping of grassland canopy cover in China through the integration of extensive drone imagery and satellite data. ISPRS Journal of Photogrammetry and Remote Sensing, 2024. 218: p. 69.  
84. Wijayanto, A.K., et al., Textural features for BLB disease damage assessment in peppy fields using drone data and machine learning: Enhancing disease detection accuracy. Smart Agricultural Technology, 2024. 8: p. 100498.  
85. Narmilan, A., et al., Detection of White Leaf Disease in Sugarcane Using Machine Learning Techniques over UAV Multispectral Images. Drones, 2022. 6(9): p. 230.  
86. Ecke, S., et al., Towards operational UAV-based forest health monitoring: Species identification and crown condition assessment by means of deep learning. Computers and Electronics in Agriculture, 2024. 219: p. 108785.  
87. Donmez, C., et al., Computer vision-based citrus tree detection in a cultivated environment using UAV imagery. Computers and Electronics in Agriculture, 2021. 187: p. 106273.  
88. Sun, Q., et al., Monitoring maize canopy chlorophyll density under lodging stress based on UAV

hyperspectral imagery. Computers and Electronics in Agriculture, 2022. 193: p. 106671. 89. Song, B. and K. Park Detection of Aquatic Plants Using Multispectral UAV Imagery and Vegetation Index. Remote Sensing, 2020. 12. 90. Hashemi- Beni, L., et al., Deep Convolutional Neural Networks for Weeds and Crops Discrimination From UAS Imagery. Frontiers in Remote Sensing, 2022. 3. 91. Mesias- Ruiz, G.A., et al., Drone imagery dataset for early- season weed classification in maize and tomato crops. Data in Brief, 2025. 58: p. 111203. 92. Jimenez- Brenes, F.M., et al., Automatic UAV- based detection of Cymodon dactylon for site- specific vineyard management. PloS one, 2019. 14(6): p. 218132. 93. Qi, H., et al., Monitoring of peanut leaves chlorophyll content based on drone- based multispectral image feature extraction. Computers and Electronics in Agriculture, 2021. 187: p. 106292. 94. Meesaragandla, S., et al., Herbicide spraying and weed identification using drone technology in modern farms: A comprehensive review. Results in Engineering, 2024. 21: p. 101870. 95. Diykh, M., et al., Empirical curvelet transform based deep DenseNet model to predict NDVI using RGB drone imagery data. Computers and Electronics in Agriculture, 2024. 221: p. 108964. 96. Betitame, K., et al., A practical guide to UAV- based weed identification in soybean: Comparing RGB and multispectral sensor performance. Journal of Agriculture and Food Research, 2025. 20: p. 101784. 97. Goyal, R., A. Nath, and U. Niranjan, Weed detection using deep learning in complex and highly occluded potato field environment. Crop Protection, 2025. 187: p. 106948. 98. Kumar Yadav, P., et al., Detecting volunteer cotton plants in a corn field with deep learning on UAV remote- sensing imagery. Computers and Electronics in Agriculture, 2023. 204: p. 107551. 99. Xu, B., et al., Improved weed mapping in corn fields by combining UAV- based spectral, textural, structural, and thermal measurements. Pest Management Science, 2023. 79(7): p. 2591. 100. Rozenberg, G., et al., Using a low- cost unmanned aerial vehicle for mapping giant smutgrass in bahiagrass pastures. Precision Agriculture, 2023. 24(3): p. 971. 101. Dubuis, P.- H., et al., Environmental, bystander and resident exposure from orchard applications using an agricultural unmanned aerial spraying system. Science of The Total Environment, 2023. 881: p. 163371. 102. Milindi, P.S., E.E. Nsenuka, and S.S. Chopra, Driving sustainability in the sugarcane industry: Life Cycle Assessment of conventional and emerging spraying technologies in Tanzania. Science of The Total Environment, 2024. 955: p. 176963. 103. Ahmad, F., et al., Effect of operational parameters of UAV sprayer on spray deposition pattern in target and off- target zones during outer field weed control application. Computers and Electronics in Agriculture, 2020. 172: p. 105350.

104. Chen, P., et al., Droplet distributions in cotton harvest aid applications vary with the interactions among the unmanned aerial vehicle spraying parameters. Industrial Crops and Products, 2021. 163: p. 113324.  
105. Ehrampoosh, A., et al., Intelligent weed management using aerial image processing and precision herbicide spraying: An overview. Crop Protection, 2025: p. 107206.  
106. Wang, J., et al., Meteorological and flight altitude effects on deposition, penetration, and drift in pineapple aerial spraying. Asia-Pacific Journal of Chemical Engineering, 2020. 15(1): p. 2382.  
107. Tait, L.W., et al., Towards remote surveillance of marine pests: A comparison between remote operated vehicles and diver surveys. Frontiers in Marine Science, 2023. 10: p. 1102506.  
108. Nevzorov, A.S., O.N. Beketova, and A.M. Ivanov, The role and place of big data in official agricultural statistics. Accounting in Agriculture, 2025. 8(1).  
109. Ahmed, N. and N. Shakoor, Advancing agriculture through IoT, Big Data, and AI: A review of smart technologies enabling sustainability. Smart Agricultural Technology, 2025. 10: p. 100848.  
110. Ngo, V.M., N.-A. Le-Khac, and M.T. Kechadi. Designing and Implementing Data Warehouse for Agricultural Big Data. in Big Data. 2019. Springer.  
111. Yu, J.K., et al., A General-Purpose Data Harmonization Framework: Supporting Reproducible and Scalable Data Integration in the RADx Data Hub. arXiv, 2025.  
112. Allu, A.R. and S. Mesapam, Impact of remote sensing data fusion on agriculture applications: A review. European Journal of Agronomy, 2025. 164: p. 127478.  
113. Papadopoulos, A. and D. Chachalis, Weed mapping in cotton using proximal and remote sensing under GIS environment, A. Peruzzieditor, Editor. 2012, University of Pisa. p. 293.  
114. Luo, L., et al., VHR GeoEye-1 imagery reveals an ancient water landscape at the Longcheng site, northern Chaohu Lake Basin (China). International Journal of Digital Earth, 2017. 10(2): p. 139.  
115. Reza Ghafarian Malamiri, H., et al., A study on the use of UAV images to improve the separation accuracy of agricultural land areas. Computers and Electronics in Agriculture, 2021. 184: p. 106079.  
116. Xu, K., et al., WeedsNet: a dual attention network with RGB-D image for weed detection in natural wheat field. Precision Agriculture, 2024. 25(1): p. 460.  
117. Alkanov, A., A. Nugmanova, and M. Sutala, Research on crop classification methods based on machine learning using wavelet transformations. Eurasian Journal of Applied Biotechnology, 2023(2).  
118. Xia, F., et al., Weed resistance assessment through airborne multimodal data fusion and deep learning: A novel approach towards sustainable agriculture. International Journal of Applied Earth Observation and Geoinformation, 2023. 120: p. 103352.  
119. Quiros, C., et al., ClimMob: Software to support experimental citizen science in agriculture. Computers and Electronics in Agriculture, 2024. 217: p. 108539.

120. Dehnen-Schmutz, K., et al., Exploring the role of smartphone technology for citizen science in agriculture. Agronomy for Sustainable Development, 2017. 36(2): p. 25.  
121. Rocha, F., et al., Weed mapping using techniques of precision agriculture. Planta daninha, 2015. 33(1): p. 157.  
122. MacLaren, C., et al., An ecological future for weed science to sustain crop production and the environment. A review. Agronomy for Sustainable Development, 2020. 40(4): p. 24.  
123. Lu, Y. and S. Young, A survey of public datasets for computer vision tasks in precision agriculture. Computers and Electronics in Agriculture, 2020. 178: p. 105760.  
124. Li, J., et al., Large language models and foundation models in smart agriculture: Basics, opportunities, and challenges. arXiv, 2024.  
125. Shen, Y., et al., WeedNet: A Foundation Model-Based Global-to-Local AI Approach for Real-Time Weed Species Identification and Classification. arXiv, 2025.  
126. Adnan, M.M., et al., A Review of Methods for The Image Automatic Annotation. Journal of Physics: Conference Series, 2021. 1892(1): p. 012002.  
127. Chen, S. and Z. Zhang, A Semi-Automatic Magnetic Resonance Imaging Annotation Algorithm Based on Semi-Weakly Supervised Learning. Sensors, 2024. 24(12): p. 3893.  
128. Salar, A. and A. Ahmadi, Improving loss function for deep convolutional neural network applied in automatic image annotation. The Visual Computer, 2024. 40(3): p. 1617.  
129. Tang, H., et al., LMSeg: Unleashing the Power of Large-Scale Models for Open-Vocabulary Semantic Segmentation. arXiv, 2024.  
130. Karimi, A. and C. Poullis, DSV-LFS: Unifying LLM-Driven Semantic Cues with Visual Features for Robust Few-Shot Segmentation. arXiv, 2025.  
131. Adhinata, F.D., Wahyono, and R. Sumiharto, A comprehensive survey on weed and crop classification using machine learning and deep learning. Artificial Intelligence in Agriculture, 2024. 13: p. 45.  
132. Sonawane, S. and N.N. Patil, Crop-Weed Segmentation and Classification Using YOLOv8 Approach for Smart Farming. Journal of Studies in Science and Engineering, 2024. 4(2): p. 136.  
133. Calvert, B., et al., Robotic Spot Spraying of Harrisia Cactus (Harrisia martinii) in Grazing Pastures of the Australian Rangelands. Plants, 2021. 10(10): p. 2054.  
134. Kanade, A.K., et al., Weed detection in cotton farming by YOLOv5 and YOLOv8 object detectors. European Journal of Agronomy, 2025. 168: p. 127617.  
135. Qi, Z. and J. Wang, PMDNet: An Improved Object Detection Model for Wheat Field Weed. Agronomy, 2025. 15(1): p. 55.  
136. Garibaldi-Márquez, F., et al., Enhancing site-specific weed detection using deep learning transformer architectures. Crop Protection, 2025. 190: p. 107075.

137. Garibaldi-Márquez, F., G. Flores, and L.M. Valentin-Coronado, Leveraging deep semantic segmentation for assisted weed detection. Journal of Agricultural Engineering, 2025.

138. Ganapathy, S. and S. Srinivasan, Crop weed separation through image-level segmentation: an ensemble of modified U-Net and encoder-decoder. Neural Computing and Applications, 2025.

139. Kong, X., et al., Lightweight cabbage segmentation network and improved weed detection method. Computers and Electronics in Agriculture, 2024. 226: p. 109403.

140. Li, Y., et al., An improved U-net and attention mechanism-based model for sugar beet and weed segmentation. Frontiers in Plant Science, 2025. 15.

141. Li, T., et al., A Patch-Level Data Synthesis Pipeline Enhances Species-Level Crop and Weed Segmentation in Natural Agricultural Scenes. Agriculture, 2025. 15(2): p. 138.

142. Sreeja, K., et al., Implementing Innovative Weed Detection Techniques for Environmental Sustainability. J. Environ. Nanotechnol, 2024. 13(4): p. 287.

143. Chen, H., et al., PIS-Net: Efficient weakly supervised instance segmentation network based on annotated points for rice field weed identification. Smart Agricultural Technology, 2024. 9: p. 100557.

144. Banerjee, S., S. Das, and A.C. Mondal, A Study of the Application Domain of a Large Language Models in the Agricultural Sector. International Journal of Innovative Research in Computer Science and Technology, 2024. 12(5).

145. Lam, H.Y.I., X.E. Ong, and M. Mutwil, Large language models in plant biology. Trends in Plant Science, 2024. 29(10): p. 1145.

146. Marinoudi, V., et al., Large language models impact on agricultural workforce dynamics: Opportunity or risk? Smart Agricultural Technology, 2024. 9: p. 100677.

147. Chen, D. and Y. Huang, Integrating reinforcement learning and large language models for crop production process management optimization and control through a new knowledge-based deep learning paradigm. Computers and Electronics in Agriculture, 2025. 232: p. 110028.

148. Jahanbakht, M., et al., Distributed Deep Learning and Energy-Efficient Real-Time Image Processing at the Edge for Fish Segmentation in Underwater Videos. IEEE Access, 2022. 10: p. 117796.

149. Qureshi, M.F., et al., Real-Time Weed Segmentation in Tobacco Crops Utilizing Deep Learning on a Jetson Nano. in International Conference on Engineering & Computing Technologies (ICECT). 2024. IEEE.

150. Blank, L., G. Rozenberg, and R. Gafni, Spatial and temporal aspects of weeds distribution within agricultural fields - A review. Crop Protection, 2023. 172: p. 106300.

151. Chen, G., et al., Diversity and Life History Traits of Native Weed Communities in Agricultural Areas: A Case Study in Eastern China. Biology, 2024. 13(9): p. 704.

152. Schatke, M., et al., Estimation of weed distribution for site-specific weed management—can Gaussian copula reduce the smoothing effect? Precision Agriculture, 2025. 26(2): p. 37.

153. Xue, K., Modeling Analysis of Factors Influencing Wind-Borne Seed Dispersal: A Case Study on Dandelion. American Journal of Plant Sciences, 2024. 15(4): p. 252.

154. Boinot, S., A. Alignier, and J. Storkey, Landscape perspectives for agroecological weed management. A review. Agronomy for Sustainable Development, 2024. 44(1): p. 7.

155. Jones, E. and P. Rozeboom. Evidence That Combines Can Transport Weed Seeds. 2023; Available from: https://extension.sdstate.edu/evidence-combines-cantransport-weed-seeds.

156. ISDA. Aquatic Noxious Weed Treatment Plans. 2024; Available from: https://gisidaho.hub.arcgis.com/apps/idaho::aquatic-noxiousweed-2024-treatment-plans-mapping-app/explore.

157. Villa, J., Mapping Arundo donax (Arundo cane) with multispectral imagery before, during, and after herbicide treatment along the Rio Grande in Webb County, Texas, 2020-21. 2024, US Geological Survey.

158. Randall, J., et al., From Meadow to Map: Integrating Field Surveys and Interactive Visualizations for Invasive Species Management in a National Park. ISPRS International Journal of Geo-Information, 2022. 11(10): p. 525.

159. Bueno, J., et al., Influence of Field, Crop and Climate Variables on Corn Silage Yield Maps. 2024. AgEng.

160. Chandra Swain, K., et al., Detecting Weed and Barespot in Wild Blueberry Using Ultrasonic Sensor Technology, in Reno, Nevada. 2009, ASABE.

161. Simoes Araujo, A.L., et al., Integrated weed management: insights from a weed resistance survey and non-chemical weed seed control in the Central Great Plains. 2023, Colorado State University.

162. Krahmer, H., et al., Weed surveys and weed mapping in Europe: State of the art and future tasks. Crop Protection, 2020. 129: p. 105010.

163. Saleh, A., et al., Semi-supervised weed detection for rapid deployment and enhanced efficiency. Computers and Electronics in Agriculture, 2025. 236: p. 110410.