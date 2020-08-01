# RA26_Ctrl-Alt-Elite_WIMDR

## Project Description
There are quite a lot of unnoticed waste in our country. Our main aim is to bring that waste to notice using drone and vehicular surveillance and even general public’s intervention.   
The drone and vehicular cameras captures videos along with location, date and time and directly send it to our main server. The interested people can also capture the image of waste in their nearby loacality using our app.  
 
Deep learning techniques are used to detect whether the image contains garbage or not and also the animals present around the garbage.
Clusters are defined with each cluster having a radius of around 1km. Using API calls population density and number of water bodies is fetched for all the clusters.
Thus with this we have these four features for every cluster -
* Number of garbage locations
* Water Bodies 
* Population Density
* Number of Animals

Using these four features a garbage index is generated and the clusters are divided into three types each with high, medium or low urgency.
These index are plotted on the map and the ngos are notified about it through our website.
NGOs undertake these areas for cleaning, and once they clean it the governement reviews the cleaned area and updates ratings of NGOs based on their performance. If there are certain areas which none of the NGOs have cleaned for a very long time the government can get it cleaned. 
Thus, with the involvement of the citizens, the NGOs and the governement we aim to make our country more clean.
