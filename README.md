# currency-explorer-api

## About the project
Currency explorer is an api for providing a comprehensive overview of dollars and euros exchanges across the Dominican
Republic. 

It comprises in a public api endpoint for unauthenticated requests that is powered by a cron job that regularly 
scrapes the daily fluctuations of values vs the Dominican Peso.

## Getting started
* Install node dependencies: ```npm i```
* Install python dependencies: ```pip install -r requirements.txt```

### Local development
A local web server can be started with ```npm start```.

### Tests
For running tests simply use ```python -m unittest```.

## Deployment
Copy the sample `.env` file and fill it with the aws credentials: ```cp .env-sample .env```
