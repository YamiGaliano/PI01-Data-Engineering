from fastapi import FastAPI
import pandas as pd
from pandasql import sqldf
from fastapi.responses import PlainTextResponse
from fastapi import HTTPException
import os

os.environ["OPENBLAS_L2SIZE"] = "512k"


app = FastAPI(title= "API - Plataformas",
    description= "Amazon, Disney, Hulu y Netflix")

# Cargamos la base de datos
global Platforms
Platforms = pd.read_csv('Datasets/All_Platforms.csv')


# Cargamos inicio de API
@app.get('/',response_class=PlainTextResponse)
async def index():
    return 'Lab01 - SoyHenry - Yamila Galiano'

# Cargamos información sobre la API
@app.get('/about',response_class=PlainTextResponse)
async def about():
    return 'API creada con FastAPI y Deta'


#1. get_word_count - cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get('/get_word_count/{plataforma},{keyword}',response_class=PlainTextResponse)
async def get_word_count(plataforma:str, keyword:str):
    if plataforma in Platforms.Platform.unique(): #Validación de plataforma
        query = f"SELECT Platform, count(title) as Cantidad FROM Platforms WHERE title LIKE '%" + keyword + "%' AND Platform LIKE '%" + plataforma + "%'group by Platform"
        df_word = sqldf(query)
        resp = df_word.to_json(orient="index")
    else:
        raise HTTPException(status_code=404, detail='La plataforma ingresada es incorrecta, recuerde que solo puede ingresar: amazon, netflix, hulu o disney.')
    return resp


#2. get_score_count - cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get('/get_score_count/{plataforma},{score},{year}',response_class=PlainTextResponse)
async def get_score_count(plataforma:str, score:int, year:int):
    #creamos un df más pequeño de movies 
    movies = Platforms[Platforms['type']== 'movie']
    score = str(score)
    año = str(year)
    if plataforma in Platforms.Platform.unique(): #Validación de plataforma
        query = f"SELECT Platform, count(title) as cantidad, release_year as anio FROM movies WHERE Platform LIKE '%" + plataforma + "%' AND score > " + score + " AND release_year = "+ año + " group by Platform"
        df_score = sqldf(query)
        resp = df_score.to_json(orient = 'index')
    else:
        raise HTTPException(status_code=404, detail='La plataforma ingresada es incorrecta, recuerde que solo puede ingresar: amazon, netflix, hulu o disney.')
    return resp
    

#3. get_second_score - la segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
@app.get('/get_second_score/{plataforma}',response_class=PlainTextResponse)
async def get_second_score(plataforma:str):
    if plataforma in Platforms.Platform.unique(): #Validación de plataforma
        query = f"SELECT title, score FROM Platforms WHERE type = 'movie' AND Platform LIKE '%" + plataforma + "%' ORDER BY score DESC, title ASC LIMIT 1,1;"
        df_second = sqldf(query)
        resp = df_second.to_json(orient = 'index')
    else:
        raise HTTPException(status_code=404, detail='La plataforma ingresada es incorrecta, recuerde que solo puede ingresar: amazon, netflix, hulu o disney.')
    return resp



#4. get_longest - película que más duró según año, plataforma y tipo de duración
@app.get('/get_longest/{plataforma},{type_duration},{year}',response_class=PlainTextResponse)
async def get_longest(plataforma:str,type_duration:str,year:int):
    if plataforma in Platforms.Platform.unique(): #Validación de plataforma
        año = str(year)
        query = f"SELECT title, duration_int as duration, duration_type FROM Platforms WHERE Platform LIKE '%" + plataforma + "%' AND release_year = " + año + " AND duration_type LIKE '%" + type_duration +  "%' ORDER BY duration_int DESC LIMIT 1;"
        df_longest = sqldf(query)
        resp = df_longest.to_json(orient = 'index')
    else:
        raise HTTPException(status_code=404, detail='La plataforma ingresada es incorrecta, recuerde que solo puede ingresar: amazon, netflix, hulu o disney.')
    return resp


#5. get_rating_count - cantidad de series y películas por rating
@app.get('/get_rating_count/{rating}',response_class=PlainTextResponse)
async def get_rating_count(rating:str):
    query = f"SELECT rating, count(*) as cantidad FROM Platforms WHERE rating LIKE '%" + rating + "%' GROUP BY rating"
    df_rating = sqldf(query)
    resp = df_rating.to_json(orient = 'index')
    return resp

