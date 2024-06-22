# WasteWise

An app that encourages people to recycle

## Image classification

The user will scan a waste with his camera. With the image classification algorithm implemented with ResBet neural network, the waste will classify by its type

## Find recycling facilities

The app is connecting to many APIs and maps to find the closest relevant recycling facility to the user.

## API Specification

## Users API

| Description        | HTTP Method | URL                                                                                | Input         | Output        |
|--------------------|-------------|------------------------------------------------------------------------------------|---------------|---------------|
| Create a new user  | POST        | /wastewise/users                                                                   | [User](#User) | [User](#User) |
| Get a user (Login) | GET         | /wastewise/users/{user_email}?email={logged_in_user}&password={logged_in_password} |               | [User](#User) |
| Update a user      | PATCH       | /wastewise/users/{user_email}?email={email}&password={password}                    | [User](#User) |               |


### User
```json
{
  "name": "Moshe",
  "email": "moshe@mail.com",
  "password": "Abcd1234!",
  "role": "User"
}
```

## Objects API


| Description         | HTTP Method | URL                                                              | Input                     | Output            |
|---------------------|-------------|------------------------------------------------------------------|---------------------------|-------------------|
| Create a new object | POST        | /wastewise/objects?email={email]&password={password}             | [New object](#New-Object) | [Object](#Object) |
| Get an object       | GET         | /wastewise/objects/{object_id}?email={email}&password={password} |                           | [Object](#Object) |
| Update an object    | PATCH       | /wastewise/objects/{object_id}?email={email}&password={password} | [New object](#New-Object) |                   |


### New Object
```json
{
  "type": "PUBLIC_FACILITY",
  "active": true,
  "data": {
    "name": "מגדל שרשן 18",
    "bin_type": "glass",
    "location": {
      "coordinates": [0.0, 0.0]
    }
  }
}
```

### Object
```json
{
  "_id": "5b25e395-12d6-11ef-8521-0c7a15236f90",
  "active": true,
  "created_by": "bins_admin@mail.com",
  "type": "PUBLIC_FACILITY",
  "data": {
    "name": "מגדל שרשן 18",
    "bin_type": "glass",
    "location": {
      "coordinates": [0.0, 0.0]
    }
  }
}
```

### Object Types
- PUBLIC_FACILITY
- PRIVATE_FACILITY
- CLASSIFICATION
- IMAGE



## Commands API

| Description          | HTTP Method | URL                                                   | Input              | Output             |
|----------------------|-------------|-------------------------------------------------------|--------------------|--------------------|
| Create a new command | POST        | /wastewise/commands?email={email]&password={password} | Any Command object | Any Command Object |


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

Response:

```json
[{
  "_id": "5b25e395-12d6-11ef-8521-0c7a15236f90",
  "active": true,
  "created_by": "bins_admin@mail.com",
  "data": {
    "name": "מגדל שרשן 18",
    "bin_type": "glass",
    "location": {
      "coordinates": [0.0, 0.0]
    }
  },
  "distance": 180,
  "type": "PUBLIC_FACILITY"
}]
```


### Get Private Facilities

Execute this command to get all the private recycling facilities of a specific user

Returns a list of recycling facilities in a specific radius

Required body:

```json
{
  "type": "PRIVATE_FACILITIES",
  "data": {
    "bin_type": "<BIN_TYPE>"
  }
}
```

Response:

```json
[{
        "_id": "9fc0bf3b-2753-11ef-9bd9-0c7a15236f94",
        "active": true,
        "created_by": "user@gmail.com",
        "data": {
            "bin_type": "glass",
            "location": {
                "coordinates": [
                    34.80354728937988,
                    32.07512400933965
                ]
            },
            "name": "Katzenelson St 18, Giv'atayim, Israel",
            "private_name": "Work"
        },
        "type": "PRIVATE_FACILITY"
}]
```

### Classify API

| Description      | HTTP Method | URL                                                   | Input | Output                            |
|------------------|-------------|-------------------------------------------------------|-------|-----------------------------------|
| Classify a waste | POST        | /wastewise/classify?email={email]&password={password} | Image | [Classification](#Classification) |


Execute this api to classify the type of the waste
Returns the type of the waste and add a classification object to the database
The classification object contains the type of the waste, and the time of the classification
Require a binary file in the body of the request

### Classification

```json
{
  "classification": "<CLASSIFICATION>"
}
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

## Docker

