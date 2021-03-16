from importlib import reload
from typing import Optional
from fastapi import FastAPI
import uvicorn # ASGI server
#from data import DataAccess as da=> from ./API.data import DataAcess
from fastapi.encoders import jsonable_encoder
from urllib.parse import urlparse
from cassandra.cluster import Cluster


class DataAccess():

    @classmethod
    def connexion(cls):
    #if __name__ == "__main__":
    #lorsque l'on teste en local , on garde localhost ou l'adresse IP, ici on travaille dans les containers on indique le nom des containers , soit l'adresse IP       
        cls.cluster = Cluster(['cassandra-resto1final','cassandra-resto2final'], port=9042)
        cls.session = cls.cluster.connect('resto')
        #cls.session.execute('USE resto') ce n'est plus nécessaire à partir du moment où l'on indique le nom de ma keyspace dans la session de connexion
    @classmethod
    def deconnexion(cls):
        
        cls.cluster.shutdown()
    
    @classmethod
    def get_info_id(cls,id):
        
        info_resto_id = {}
        liste_info_resto_id = []
        cls.connexion()
        # rows = session.execute('SELECT * FROM restaurant')
        rows = cls.session.execute(f'SELECT id, borough, buildingnum,cuisinetype,phone,street,name,zipcode  FROM restaurant WHERE id={id};')
        for row in rows:
            #print(row.zipcode,row.street,row.phone,row.borough,row.id,row.cuisinetype)
            info_resto_id = {'id':row.id,'borough':row.borough,'buildingnum':row.buildingnum,'cuisinetype':row.cuisinetype,'phone':row.phone,'street':row.street,"name":row.name,'zipcode':row.zipcode}
            liste_info_resto_id.append(info_resto_id)
        #print(info_resto_id)
        #DataAccess().deconnexion()

        return list(liste_info_resto_id)
    
    @classmethod
    def get_info_kitchen(cls,cuisinetype):
        
        info_restaurant = []
        dico ={}
        cuisinetype = str(cuisinetype)
        cls.connexion()
        #rows = session.execute('SELECT * FROM restaurant WHERE cuisinetype="Mexican";')
        rows = cls.session.execute(f"SELECT * FROM restaurant WHERE cuisinetype= '{cuisinetype}';")
        for row in rows:
            #print(row.zipcode,row.street,row.phone,row.borough,row.id,row.cuisinetype)
            dico = {'id':row.id,'nom ':row.name,'rue':row.street,'cuisine':row.cuisinetype}
            info_restaurant.append(dico)
        print(info_restaurant)
            
        #DataAccess().deconnexion()
        return info_restaurant
    
    @classmethod
    def get_info_inspection(cls,idrestaurant):
        
        liste = []
        #dico ={} 
        cls.connexion()
        rows = cls.session.execute(f"SELECT * FROM inspection WHERE idrestaurant= {idrestaurant};")
        for row in rows:
            liste.append(row)
        # row1 = cls.session.execute(f"SELECT name FROM restaurant WHERE id= {idrestaurant};")
        # row1 = list(row1)
        # dico = {idrestaurant:len(liste)}
        result = {f"nombre d'inspection du restaurant ayant l'id n°{idrestaurant}" : len(liste)}
        print(result)
        return result
           

    @classmethod
    def get_ten_resto(cls, grade):
        
        dico ={}
        idrestaurant = []
        liste_grade = []
        #grade = str(grade)
        cls.connexion()
        rows = cls.session.execute(f"SELECT idrestaurant FROM inspection WHERE grade= '{grade}' GROUP BY idrestaurant limit 10;")
        for row in rows:
            #print(row.idrestaurant,row.score,row.violationdescription)
            idrestaurant.append(row.idrestaurant)
        for id in idrestaurant:
                info = cls.session.execute(f"SELECT name  FROM restaurant WHERE id = {id};")
                info = list(info)
                dico = {id:info}
                liste_grade.append(dico)

        #print (info)
        #DataAccess().deconnexion()
        return liste_grade


# a = DataAccess().get_info_id(50006392)
# print(a)
# print('===========================================')
#resto = DataAccess().get_info_kitchen('Thai') 
print('===========================================')
#DataAccess().get_info_inspection(50006392)
# print('===========================================')
#print(resto)
#grade = DataAccess().get_ten_resto('A')
#print(grade)
# from models import Item

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello":"World"}

@app.get("/info_restaurant/{id}")
async def get_info_id(id:int):
    
    data = DataAccess().get_info_id(id)
    #DataAccess().deconnexion()
    return jsonable_encoder(data)

@app.get("/info_restaurant/cuisine/{cuisinetype}")
async def get_info_kitchen(cuisinetype:str):

    data = DataAccess().get_info_kitchen(cuisinetype)
    return jsonable_encoder(data)

   

@app.get("/info_restaurant/inspection/{idrestaurant}")
async def get_info_inspection(idrestaurant:int):
    
    data = DataAccess().get_info_inspection(idrestaurant)
    #da.deconnexion()
    return jsonable_encoder(data)

@app.get("/info_restaurant/grade/{grade}")
async def get_ten_resto(grade:str):
    
    data = DataAccess().get_ten_resto(grade)
    #da.deconnexion()
    return jsonable_encoder(data)

# if __name__ == "__main__":
#     uvicorn.run('api:app', host="127.0.0.1", port=8000,reload=True)

    #  cuisinetype = str(cuisinetype)
    # print(cuisinetype)
    # data = da.recup_info_type_cuisine(cuisinetype)
    # #da.deconnexion()
    # return data