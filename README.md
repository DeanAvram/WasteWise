# WasteWise

An app that encourages people to recycle

## Image classification

The user will scan a waste with his camera. With the image classification algorithm implemented with ResBet neural network, the waste will classify by its type

## Find recycling facilities

The app is connecting to many APIs and maps to find the closest relevant recycling facility to the user.

## API Specification

## User

### Create new User
```
POST /wastewise/users
```
Request Body:
```json
{
  "name": "<NAME>",
  "email": "<EMAIL>",
  "password": "<PASSWORD>",
  "role": "<Role>"
}
```

Response:
```json
{
  "name": "<NAME>",
  "email": "<EMAIL>",
  "password": "<PASSWORD>",
  "role": "<Role>"
}
```
### Get User
```
GET /wastewise/users?email=<EMAIL>?email=<LOGGED_IN_USER_EMAIL>&password=<LOGGED_IN_USER_PASSWORD>
```

Response:
```json
{
  "name": "<NAME>",
  "email": "<EMAIL>",
  "password": "<PASSWORD>",
  "role": "<Role>"
}
```

### Update User
```
PUT /wastewise/users
```
```json
{
  "email": "<EMAIL>",
  "name": "<NAME>",
  "password": "<PASSWORD>"
}
```

## Object

### Create new Object
```
POST /wastewise/objects?email=<USER_EMAIL>&password=<USER_PASSWORD>
```
Request Body:
```json
{
  "type": "<TYPE>",
  "active": "<ACTIVE>",
  "data": {
    "location": {
      "lng": "<LNG>",
      "lat": "<LAT>"
    }
  }
}
```

Response:
```json
{
  "_id": "<ID>",
  "active": "<ACTIVE>",
  "created_by": "<CREATED_BY>",
  "type": "<TYPE>",
  "data": {
    "location": {
      "lng": "<LNG>",
      "lat": "<LAT>"
    }
  }
}
```

### Get Object
```
GET /wastewise/objects/<OBJECT_ID>?email=<USER_EMAIL>&password=<USER_PASSWORD>
```

Response:
```json
{
  "_id": "<ID>",
  "active": "<ACTIVE>",
  "created_by": "<CREATED_BY>",
  "type": "<TYPE>",
  "data": {
    "location": {
      "lng": "<LNG>",
      "lat": "<LAT>"
    }
  }
}
```

### Update Object
```
PUT /wastewise/objects/<OBJECT_ID>?email=<USER_EMAIL>&password=<USER_PASSWORD>
```

Request Body:
```json
{
  "active": "<ACTIVE>",
  "data": {
    "location": {
      "lng": "<LNG>",
      "lat": "<LAT>"
    }
  }
}
```

## Commands

```
POST /wastewise/commands?email=<USER_EMAIL>&password=<USER_PASSWORD>
```

### Direct

Execute this command to find the closest recycling facility to the user

Returns the closest recycling facilities

Request body:

```json
{
  "type": "DIRECT",
  "data": {
    "bin_type": "<BIN_TYPE>",
    "location": {
      "lng": "<LNG>",
      "lat": "<LAT>"
    }
  }
}
```

Response:

```json
{
  "_id": "<ID>",
  "active": "true",
  "created_by": "<CREATED_BY>",
  "data": {
    "bin_type": "<BIN_TYPE>",
    "name": "<NAME>",
    "location": {
      "lng": "<LNG>",
      "lat": "<LAT>"
    }
  },
  "distance": "<DISTANCE>",
  "type": "PUBLIC_FACILITY"
}
```

### History

Execute this command to find the history of the user's classifications

Returns a list of classifications of a user in a specific period of time

Request body:

```json
{
  "type": "HISTORY",
  "data": {
    "period": "EnumPeriod"
  }
}
```

### Get Places

Execute this command to get all the recycling facilities in a specific radius

Returns a list of recycling facilities in a specific radius

Required body:

```json
{
  "type": "FACILITIES",
  "data": {
    "location": {
      "lng": "<LNG>",
      "lat": "<LAT>"
    },
    "radius": "<RADIUS>"
  }
}
```

### Classify

Execute this command to classify the type of the waste
Returns the type of the waste and add a classification object to the database
The classification object contains the type of the waste, and the time of the classification
Require a binary file in the body of the request

```
POST /wastewise/classify?email=<USER_EMAIL>&password=<USER_PASSWORD>
```

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

## Test

```bash
pytest tests
```

## Mongo

### Start mongo in linux

```bash
sudo systemctl start mongod | sudo systemctl status mongod
```
