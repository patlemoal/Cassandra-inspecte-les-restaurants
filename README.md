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

Les containers sont mis en place grâce au fichier ![docker-compose.yaml](docker-compose.yaml) qui est lié au !(Dockerfile) via l'instruction build
Les principales instructions sont dans le fichier ![principalescommandes.txt](principalescommandes.txt) 

## Le fichier api.py 

Nous avons créé une API pour accéder :

    aux infos d'un restaurant à partir de son id,
    à la liste des noms de restaurants à partir du type de cuisine,
    au nombre d'inspection d'un restaurant à partir de son id restaurant,
    les noms des 10 premiers restaurants d'un grade donné.

## Mise en place de la base de données

Dans le répertoire resources, nous avons crée un fichier ![init.cql](init.cql) qui donne les principales instructions pour la création de la keyspace et des différentes tables. Il est relié au ![docker-compose.yaml](docker-compose.yaml)  
le fichier ![principalescommandes.txt](principalescommandes.txt) résume les différentes actions à accomplir pour mettre en place la base de données dans le contenair via l'invite de commande.




