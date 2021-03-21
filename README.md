# Cassandra inspecte les restaurants

``` 
objectif : Utiliser un Cluster Cassandra, monté sur Docker, pour stocker les données des inspections de restaurant. Faire une API en Python pour rendre ces données accessibles. 
```

Notre jeu de données se compose de deux fichiers csv :
  - ![restaurants.csv](restaurants.csv)
  - ![restaurants_inspections.csv](restaurants_inspections.csv)
  
## Mise en place de 3 containers :

Emplacement du logiciel
https://www.docker.com/products/docker-desktop

![image](docker.PNG)

Les containers sont mis en place grâce au fichier ![docker-compose.yaml](docker-compose.yaml) qui est lié au ![Dockerfile](Dockerfile) via l'instruction build
Les principales instructions sont dans le fichier ![principalescommandes.txt](principalescommandes.txt) 


## Mise en place de la base de données

Dans le répertoire resources, nous avons crée un fichier ![init.cql](init.cql) qui donne les principales instructions pour la création de la keyspace et des différentes tables de manière automatique. En une instruction notre keyspace et nos tables sont construites.
``
#copier les tables 
cqlsh> source '/resources/init.cql';
``

Le fichier ![principalescommandes.txt](principalescommandes.txt) résume les différentes actions à accomplir pour mettre en place la base de données dans le contenair via l'invite de commande.

## Le fichier api.py 

Nous avons créé une API pour accéder :

    aux infos d'un restaurant à partir de son id,
    à la liste des noms de restaurants à partir du type de cuisine,
    au nombre d'inspection d'un restaurant à partir de son id restaurant,
    les noms des 10 premiers restaurants d'un grade donné.


![image](visuglobaleFastAPI.PNG)


![image](info_cuisine.PNG)

![image](visuglobaleFastAPI.PNG)
