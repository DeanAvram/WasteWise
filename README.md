# WasteWise

An app that encourages people to recycle

## Image classification

The user will scan a waste with his camera. With the image classification algorithm implemented with ResBet neural network, the waste will classify by its type

## Find recycling facilities

The app is connecting to many APIs and maps to find the closest relevant recycling facility to the user.

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

## Mongo

### Srart mongo in linux

```bash
sudo systemctl start mongod
sudo systemctl status mongod
```
