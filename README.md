# Project Visudh
> Tacking India'a Waste Problem


![http://ctrlaltelite.cf/home/](https://img.shields.io/website?down_color=%23ff0000&down_message=offline&style=flat-square&up_color=%2300ff0f&up_message=online&url=http%3A%2F%2Fctrlaltelite.cf%2Fhome%2F)    
![](ReadmeAssets/1.png)

## Project Description

There are quite a lot of unnoticed waste in our country. Our main aim is to bring that waste to notice using drone and vehicular surveillance and even general public’s intervention.
The drone and vehicular cameras captures videos along with location, date and time and directly send it to our main server. The interested people can also capture the image of waste in their nearby loacality using our app.

Deep learning techniques are used to detect whether the image contains garbage or not and also the animals present around the garbage. Clusters are defined with each cluster having a radius of around 1km. Using API calls population density and number of water bodies is fetched for all the clusters. Thus with this we have these four features for every cluster -

* Number of garbage locations
* Water Bodies
* Population Density
* Number of Animals

Using these four features a garbage index is generated and the clusters are divided into three types each with high, medium or low urgency. These index are plotted on the map and the ngos are notified about it through our website. NGOs undertake these areas for cleaning, and once they clean it the governement reviews the cleaned area and updates ratings of NGOs based on their performance. If there are certain areas which none of the NGOs have cleaned for a very long time the government can get it cleaned. Thus, with the involvement of the citizens, the NGOs and the governement we aim to make our country more clean.


## 📸ScreenShots

| 1 | 2|
|------|-------|
|<img src="ReadmeAssets/3.jpeg" width="400"/>|<img src="ReadmeAssets/4.jpeg" width="400"/>|


| 3 | 4|
|------|-------|
|<img src="ReadmeAssets/5.jpeg" width="400"/>|<img src="ReadmeAssets/6.jpeg" width="400"/>|

| 5 | 6 |
|------|-------|
|<img src="ReadmeAssets/7.jpeg" width="400"/>|<img src="ReadmeAssets/8.jpeg" width="400"/>|

> The App Allows users to click a pic on uncleaned area nearby and send it to server the server checks for Garbage in Image and if found  
User get a +1 Contribution Point 
The App Also Allows user to view Nearby NGO Registered as well as non registered and also contact us in case of any problem he/she is facing

Add Website ScreenShots here

## Implementation
![](ReadmeAssets/ProductDesign.jpeg)
This is how the database schema looks like for now   
For Now We have same User Model for Users,NGOs and Government with
different permission for everyone by seperating them with different group   
But We are ready to seperate it in future if the demand arrives  

ML Model Implementation


### So How Everything Works
So everything starts when we get Images at server either from Drones or Users using our app 
Our ML Model checks for garbage in Image and if garbage is found it saves image in Database
We run a script daily on our database to group images in similar area and if image belongs to some area which is already active it is assigned to that area   
Whenever a new garbage image is added to an area its garbage index is recalculated and saved

All NGOs can see these area in order of their garbage Index any NGO can take an area under review , After an NGO take an area under review it gets a responsibilty to clean that area as fast as possible to Increase its Work Done so that Government could increase its rating

Here is when Goverement role comes into play , Government could see all those areas whose request for cleaning is given atleast 15 days ago and are still uncleaned and if taken under review by some NGO and not cleaned in 15 days government can also see name of NGO 
whose under review a particular area is  

Governement can increase or decrease rating of any NGO based on their work done or activeness , government can also permanently delete or ban NGO in case of false remark by NGO of work completion

Anyone can see NGOs profile to see their previous works in cleaning India and rating assigned to them by government

## Future Scope


## Deployment

Our server is deployed with amazon EC2 


You are free to check it out
[Link]()

Also have a look at our app
[Link]()

## Build With

* Python
* Keras
* TensorFlow
* OpenCV
* Flutter
* Django
* Google Maps API
* HTML5
* SCSS(CSS) 
* JavaScript(jQuery)


## Authors

[Aryan Khandelwal]()   
[Abhilasha Sinha]()  
[Amit Dutta]()  
[Rohan Nishant]()    
[Rashi Gupta]()    
[Shrey Rai]()  




