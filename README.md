# <h1> **PROYECTO INDIVIDUAL Nº1** </h1>


<br>

¡Hola! Soy *Yamila Galiano* y este es mi primer proyecto del bootcamp de Data Science en SoyHenry, enfocado en Data Engineer.

<hr>  

### Objetivo
Realizar una ingesta de datos desde diversas fuentes, aplicar transformaciones solicitadas y disponibilizar los datos limpios para su consulta a través de una API deployada en Deta.
##
[Consigna completa del LAB - Cohorte 6](https://github.com/HX-FNegrete/PI01-Data-Engineering/blob/main/README.md)


### Contexto
Como parte del equipo de data de una empresa, el área de análisis de datos solicita al área de Data Engineering ciertos requerimientos para el óptimo desarrollo de sus actividades. A partir de 4 datasets de las plataformas Amazon, Disney, Hulu y Netflix se deberá elaborar *transformaciones* requeridas y disponibilizar los datos mediante la *elaboración y ejecución de una API*.

### Tecnologías utilizadas
* [Python](https://docs.python.org/3/)
* [Pandas](https://pandas.pydata.org/)
* [pandasql](https://pypi.org/project/pandasql3/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Deta](https://web.deta.sh/home)


<hr>

## Propuesta de trabajo:

1. Transformaciones.
    * Analizar los datos.
    * Transformaciones solicitadas.
    * Unificar los data sets en uno. 
2. Desarrollo API: Para disponibilizar los datos la empresa usa el framework FastAPI. 
3. Deployment: Utilizamos Deta.

Estos pasos se encuentran detallados en el siguiente video: 
https://www.loom.com/share/bda00889797b4b5e88aa20b0039626c4

<br/>

 <br>

### Archivos del repositorio
- [**Datasets**:](./Datasets/) En esta carpeta se encuentran los archivos .csv utilizados para realizar el proyecto y también el archivo que se creó con los resultados de las transformaciones.  
- [**Limpieza.ipynb**:](Limpieza.ipynb) Aquí están los archivos utilizados para realizar el analisis y transformación.
- [**.deta**:](./.deta) Configuración de archivo deta.
- [**main.py**:](main.py) Script para instanciar la API, con las funciones de consultas.

### Consultas que se pueden realizar en la API:

*Link de la API: https://q8ifew.deta.dev/*

- Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma. 
/get_word_count/plataforma,keyword

- Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. 
/get_score_count/plataforma,score,year

- La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
/get_second_score/plataforma

- Película o serie que más duró según año, plataforma y tipo de duración. En duration_type puede consultar con el parámetro 'min' en casos de peliculas o 'season' en casos de series. /get_longest/plataforma,duration_type,year

- Cantidad de series y películas por rating. /get_rating_count/rating

<br/>

## Conclusión
En este proyecto su pudo integrar los conocimientos obtenidos en el bootcamp respecto a Python y aprender nuevas tecnnologías para utilizar como FastApi y Deta. Como Deta tiene poca documentación respecto a errores y consultas, fue un desafío realizarlo y un gran aprendizaje. 

Contacto:  <a href="https://www.linkedin.com/in/yamila-galiano-ba7083121"><img alt="Linkedin" src="https://img.shields.io/badge/Linkedin-0077B5?style=flat&logo=linkedin&logoColor=white"></a>  

Saludos!
