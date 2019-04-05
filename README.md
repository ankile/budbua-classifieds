# Budbua
Budbua AS er norges eldste og største auksjonsselskap og ble stiftet i 1869. De har nå bestemt seg for å gå digitalt og ønsker norges beste auksjonsapplikasjon. Dette er web-appen som oppfuller dette ønsket. 


## Oppsummering
Web-løsningen er arkitekturmessig delt opp i to deler. Backend for å håndtere databasekall og intern logikk og frontend for å håndtere GUI og interaksjon med endebruker. 
### Backend
[Installasjon](#installasjon)

### Frontend
[Installasjon](#installasjon)


## Build status 
Legg inn badges her for pipeline, netlify, heroku, test-coverage


## Bilder
Legg inn litt enkle bilder her


## Installasjon

### frontend

For å kjøre frontend må du installere npm (node package manager)

- pull den nyeste koden fra gitlab

- kjør kommandoen npm install

- kjør npm start


### backend

For å kjøre backend må du nok:

- pulle den nye koden fra gitlab
- gå inn i backend-mappen `cd backend`
- gå inn i dit virtual environment `source <hva enn ditt env heter>/bin/activate`
- kjør `pip install -r requirements.txt`
- kjør `python manage.py migrate`
- kjør `python manage.py runserver`


## Bruk
Skriv inn om bruk her