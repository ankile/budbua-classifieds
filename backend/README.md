# Frontend

Det blir brukt [REST arkitektur](https://en.wikipedia.org/wiki/Representational_state_transfer) for backend. For å oppnå dette bruker vi python-rammeverket [Django](https://www.djangoproject.com/). 

Backend blir deployet automatisk til [Heroku](https://www.heroku.com/) om alle testene blir passert.

## Installasjon og bruk

Last ned og installer [Python 3.x](https://www.python.org/downloads/)

Åpne så et terminalvindu i mappen "backend" og eksekvere kommandoene:
```bash 
pip3 install virtualenv
virtualenv -p python3 testenv
source testenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Du kjører backend-delen av webappen med å eksekvere kommandoen `python manage.py runserver` fra backend-mappen

## Testing

Testingen blir gjort i backend-delen av appen. Testingen skal sørge for at vi ikke ødelegger allerede fungerende funksjoner når vi implementerer nye. 

Testfilene bruker denne strukturen: `backend/{appnavn}/test_{hvasomtestes}.py`

For å kjøre testene åpner du et terminalvindu backend-mappen og eksekverer kommandoen `python manage.py test`. Da vil alle testene bli kjørt og en feilmelding vil oppstå om noen feiler. 

Ønsker du mer informasjon på hva som blir testet kan du skrive `python manage.py test --verbosity=2`

