# B2C6_Backend
Studenten repository voor Backend voor het vak B2C6 DevOps. De backend wordt gemaakt in Python. Elke klas heeft 1 repository voor Backend.

# Instalation guide
## Python
- Python
- Pip

## Python Library's
Je hebt verschillende libarry's nodig om dit te kunnen draaien. Hieronder staat Py echter kan dit ook python of python3 zijn afhankelijk van de Python 3 versie die geinstaleerd is.
Er is een enviorment aangemaakt, het kan zijn dat deze envoirment alles al bezit waardoor de library's niet opnieuw geinstaleerd moeten worden.

```
py pip install django
py pip install mysqlclient
py pip install djangorestframework
py pip install django-cors-headers
```

## MySQL
Er is hiergewerkt met MariaDB en niet met MySQL echter Django maakt hier geen onderscheid tussen dus tijdens bouwen van database zou dit geen probleem moeten zijn. Indien dit toch het geval is. Contacteer Noah Lenkens.

## XAMPP
Zorg ervoor dat wanneer je jou database opstart er ook een MySQL server draait.
Indien je dit op een windows desktop omgeving doet is [XAMPP](https://www.apachefriends.org/) een goede en gratis optie.

## Database Install
Open je Database GUI. Open hier een SQL editor voer de volgende regels in.
```sql
CREATE DATABASE MVPDatabase CHARACTER SET UTF8;
CREATE USER DatabaseUser@localhost IDENTIFIED BY 'MariaDBPassDB';
GRANT ALL PRIVILEGES ON MVPDatabase.* TO Databaseuser@localhost;
FLUSH PRIVILEGES;
```
*(Tijdens deployement moet localhost veranderd worden naar het IP waar de server op draait)*


## Migration
Als al deze stappen gedaan zijn zul je een migration moeten doen vanuit je backend naar de database, Dit om op die manier al je tabellen aan te maken.
Open eerst een Enviorment (dit staat aangegeven in "Starting the backend server -> Enviorment")
zodra dat gedaan is volg je de volgende stappen.
```
cd MVP-Backend
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
```

# Starting the backend server
Om de server moeten er een aantal stappen plaatsvinden. Eerst open je een enviorment waarna je dan de server doet opstarten.(Indezelfde cmd)

## Enviorment
Hier openen we een enviorment. Hierna niet de CMD afsluiten deze ga je nog nodig hebben.
```
open CMD
cd (FOLDER PATH VAN REPOSITORY)
enviorment\Scripts\activate.bat
```
Als je dit gedaan hebt zie aan het begin van je CMD line "(enviorment)" staan.

## Start Server
Als je een enviorment hebt geopend doe je de volgende stappen.
```
cd MVP-Backend
py manage.py runserver (IP, indien geen IP nodig is leeg laten dan word localhost:8000 gebruikt)
```
Als dit draaid zal de CMD aangeven dat de server is opgestart en op welke IP en Poort
