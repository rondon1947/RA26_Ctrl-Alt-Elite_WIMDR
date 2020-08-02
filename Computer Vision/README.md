# Machine Learning Model





## Features used to give an urgency index to the waste.
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
#### Data augmentation - 
Considering the effect of day light we have augmented our images based on lighting effects. (Such as brightness, contrast, saturaion, hue etc.) 

After collecting the dataset we constructed bounding boxes around them and labelled them manually using this tool - https://github.com/tzutalin/labelImg

<img width="960" alt="Untitled" src="https://user-images.githubusercontent.com/43816262/89100355-049c2d80-d414-11ea-99a1-1fb0ac651d34.png">

Then we used transfer learning to train our model on ssd_mobilenet_version1. We have also quantized our model to make it light weigth so that the processing time of images is reduced. For image detection its 10fps on cpu and 20fps on gpu.

![download (1)](https://user-images.githubusercontent.com/43816262/89100450-ae7bba00-d414-11ea-9baa-cae95d1bb513.png)
![download (2)](https://user-images.githubusercontent.com/43816262/89100451-b0de1400-d414-11ea-9434-d979a6d269cc.png)

![download (3)](https://user-images.githubusercontent.com/43816262/89100454-b20f4100-d414-11ea-96ff-016dc8f28525.png)
![download](https://user-images.githubusercontent.com/43816262/89100456-b3406e00-d414-11ea-9b29-558e563276b1.png)

## Animal Detection

We have used pretrained YOLO model for detecting animals

<img width="331" alt="cow" src="https://user-images.githubusercontent.com/43816262/89100618-1c74b100-d416-11ea-9308-e8edcf780383.png">
<img width="331" alt="dog" src="https://user-images.githubusercontent.com/43816262/89100621-21396500-d416-11ea-9082-f1dccd11e7ed.png">

## Water Body
 We are using google maps API to get the water bodies within a given radius.
 
 ## Population
 For now we are using reverse geocoding to get the city/town from a latitude and longitude and again an API call for finding the polulation density of that area. If the governement gives us the latest census data of India we can use that to get better results.
 
 ## Generating Index
 All the abouve values are integers so we are normalizing them in the range 0 to 1 and assigning weights to each feature and finding the index oin the end wich lies in the range 0 to 10.

