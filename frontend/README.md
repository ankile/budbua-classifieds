[![Netlify Status](https://api.netlify.com/api/v1/badges/1dd9b4bd-f2e7-4653-b032-f416480f5f6b/deploy-status)](https://app.netlify.com/sites/gallant-swirles-109ebc/deploys)

# frontend

### Project setup
```
npm install
```

#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Run your tests
```
npm run test
```

#### Lints and fixes files
```
npm run lint
```

#### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


# Prosjektstruktur 

## Mapper

### Views
I denne mappen finnes filer knyttet til et hvert view på siden. Eksempelvis vil alle komponenter som brukes i ```/auth (login og registrering)```, lagres i mappen ```auth```. 
Internt i denne mappen vil hver feature ha sin egen fil, samt en felles wrapperfil som knytter viewet sammen.

