# Machine Learning Model





## Parameters of giving an urgency index to the waste.
We have defined clusters of area around 100 m^2, the urgency index to each cluster is given based on following features.
1. Amount of garbage - The number of garbage sites in the cluster. 
2. Animals - There are are many cases in India of animal dying due to consuming hazardous waste and also they are a major cause of garbage littering.
3. Water bodies - These garbage dumps can get into water and lead to water pollution thus we are also taking into consideratios if there are watef bodies present near the  garbage.
4. Population density - If we compare two scenraios one in which the garbage lies in the outskirts and one in which the garbage lies in commercial area it is more urgent  to clean the commercial areas first.

## Garbage Detection
#### Data Set 
There are two sources of our dataset.
1. Open source garbage in image dataset 
2. Dataset collected by us from our nearby areas.
Augmentation - One of the major aspects while capturing a video or an image is the lighting effect depending on the weather (if its sunny or cloudy) drones might capture images with varied brightness. So bightness of the image is the main thing tthat we have considered while augmentation.

After collecting the dataset we constructed bounding boxes around them and labelled them manually using this tool.

Then we used transfer learning to train our model on ssd_mobilenet_version1. We have also quantized our model to make it light weigth so that the processing time of images is reduced.
