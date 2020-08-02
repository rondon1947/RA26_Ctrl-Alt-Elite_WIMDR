# Why me migrated from Sqlite3 to PostgreSQL
As mentioned in our solution we are finding Nearest Uncleaned Areas to all NGOs as these queries would be real time we require something efficient so we thought of using some Spatial Database   
    
A spatial database is a database that is optimized for storing and querying data that represents objects defined in a geometric space. Most spatial databases allow the representation of simple geometric objects such as points, lines and polygons. Some spatial databases handle more complex structures such as 3D objects, topological coverages, linear networks, and TINs. While typical databases have developed to manage various numeric and character types of data, such databases require additional functionality to process spatial data types efficiently, and developers have often added geometry or feature data types.    
     
      
Spatial Databases Store data in form of R-tree unlike regular databases which store data in B-Tree ,due to this reason they provide very fast location queries   
**PostGIS** provides spatial objects for the PostgreSQL database, allowing storage and query of information about location and mapping. beside that PostgreSQL has many advantages over Sqlite3 database for such a large project
     
 You can find code using PostgreSQL database in different branch
