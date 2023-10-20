# WasteWise

An app that encourages people to recycle

## Image classification

The user will scan a waste with his camera. With the image classification algorithm implemented with ResBet neural network, the waste will classify by its type

## Find recycling facilities

The app is connecting to many APIs and maps to find the closest relevant recycling facility to the user.


## Commands

### Direct

Execute this command to find the closest recycling facility to the user

Returns the closest recycling facilities

Required body:
    
```json
{
    "type": "DIRECT",
    "data": {
        "location": {
            "lng": "<LNG>",
            "lat": "<LAT>"
        }
    }
}
```

### History

Execute this command to find the history of the user's predictions

Returns a list of predictions of a user in a specific period of time

The user's email is extracted from the query parameter

Required body:
    
```json
{
    "type": "HISTORY",
    "data": {
        "period": "EnumPeriod"
    }
}
```

### Add Place

Execute this command to add a new recycling facility to the database

Returns the new recycling facility and add it to the database

Required body:
```json
{
  "type": "ADD_PLACE",
  "data": {
    "name": "<NAME>",
    "location": {
      "lng": "<LNG>",
      "lat": "<LAT>"
    }
  }
}
```

### Get Places

Execute this command to get all the recycling facilities in a specific radius

Returns a list of recycling facilities in a specific radius

Required body:
```json
{
  "type": "PLACES",
  "data": {
    "location": {
      "lng": "<LNG>",
      "lat": "<LAT>"
    },
    "radius": "<RADIUS>"
  }
}
```

### Predict
Execute this command to predict the type of the waste
Returns the type of the waste and add a prediction object to the database
The prediction object contains the type of the waste,  and the time of the prediction
Require a file in the body of the request

## Venv

### create a venv

```powershell
python -m venv venv
```

### activate venv

#### powershell

```powershell
.\venv\Scripts\Activate.ps1
```

#### bash

```bash
source venv/bin/activate 
```

## Build

```bash
pip install -r requirements.txt
```

## Run

### Terminal

```bash
export FLASK_APP=src 
flask run
```

## Mongo

### Start mongo in linux

```bash
sudo systemctl start mongod | sudo systemctl status mongod
```
