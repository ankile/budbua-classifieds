# Budbua
Budbua AS er norges eldste og største auksjonsselskap og ble stiftet i 1869. De har nå bestemt seg for å gå digitalt og ønsker norges beste auksjonsapplikasjon. Dette er web-appen som bidrar til å nå dette målet. 

Du finner webappen live på <https://budbua.no>


## Status
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![pipeline status](https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-7/badges/master/pipeline.svg)](https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-7/commits/master)
[![coverage report](https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-7/badges/master/coverage.svg)](https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-7/commits/master)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)


## Oppsummering
Web-løsningen er arkitekturmessig delt opp i to deler. Backend for å håndtere databasekall og intern logikk, i kombinasjon med frontend for å håndtere GUI og interaksjon med endebruker. Frontend kommuniserer med backend via HTTP-kall og autentiseres med [JWT-tokens](https://jwt.io/introduction/). 

Kommunikasjonsstrukturen mellom backend og frontend er definert på [wikien](https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-7/wikis/Communication/auctions). All ny nødvendige strukturer blir oppdatert der. 
### Backend
[Installasjon](#installasjon)

Det blir brukt [REST arkitektur](https://en.wikipedia.org/wiki/Representational_state_transfer) for backend. For å oppnå dette bruker vi python-rammeverket [Django](https://www.djangoproject.com/). 

Backend blir deployet automatisk til [Heroku](https://www.heroku.com/) om alle testene blir passert.


### Frontend
[Installasjon](#installasjon)



Det blir brukt javascript-rammeverket [Vue](https://vuejs.org/) som kjører på toppen av [Node.js](https://nodejs.org/en/). Til stylingen brukes [Semantic UI](https://semantic-ui-vue.github.io/#/) med en kombinasjon av eget design. 

Frontend blir deployet automatisk til [Netlify](https://www.netlify.com/) om alle tester blir passert. 


## Bilder
Legg inn litt enkle bilder her


## Installasjon

Start med å klone git-repoet med kommandoen 

SSH: `git clone git@gitlab.stud.idi.ntnu.no:programvareutvikling-v19/gruppe-7.git`

HTTPS: `git clone https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-7.git`

### Frontend

Last ned og installer [Node.js](https://nodejs.org/en/)

Åpne så et terminalvindu i mappen "frontend" og eksekvere kommandoen `npm install`. Da vil alle nødvendige avhengigheter installert.

Du kjører frontend-delen av webappen med å eksekvere kommandoen `npm run serve`



### Backend

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


## Bruk

For å kjøre prosjektet lokalt må du åpne et terminalvindu i mappen frontend og et terminalvindu i mappen backend. 

I terminalvinduet i backend-mappen eksekverer du kommandoen `python manage.py runserver`

I terminalvinduet i frontend-mappen eksekverer du kommandoen `npm run serve`

Du kan da aksessere webappen ved å gå inn i nettleseren din og skrive adressen <http://localhost:8080/>


## Testing

Testingen blir gjort i backend-delen av appen. Testingen skal sørge for at vi ikke ødelegger allerede fungerende funksjoner når vi implementerer nye. 

Testfilene bruker denne strukturen: `backend/{appnavn}/test_{hvasomtestes}.py`

For å kjøre testene åpner du et terminalvindu backend-mappen og eksekverer kommandoen `python manage.py test`. Da vil alle testene bli kjørt og en feilmelding vil oppstå om noen feiler. 

Ønsker du mer informasjon på hva som blir testet kan du skrive `python manage.py test --verbosity=2`

## Kreditt

Takk til alle i Pusju Consulting som har tatt del i utviklingen.
```javascript
frontend = ["Ivar Nordvik Myrstad", "Tor Tryggestad Berre"]
backend = ["Nicolai Brummenæs", "Lars Lien Ankile", "Magnus Schack von Fyren Kieler Kvam"]
testing = ["Kent Are Torvik"]
```

## Lisens

MIT License

Copyright (c) 2019 dagsfylla

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.