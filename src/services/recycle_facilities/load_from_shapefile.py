import json
import fiona
import geopandas as gpd
from src.data.object import Object


class LoadFromShapefile:
    def __init__(self, db):
        self.db = db

    def _create_place(self, row):
        itm_x = row['geometry'].x
        itm_y = row['geometry'].y
        obj = Object("place", "admin")
        obj.data = {
            "name": row['shemrechov'] + ' ' + str(row['msbait']),
            "location": {
                "coordinates": [itm_x, itm_y]
            }
        }
        # Insert the object into the database
        self.db.objects.insert_one(json.loads(obj.toJSON()))

    def load(self):
        # Read the Shapefile
        with fiona.Env():
            gdf = gpd.read_file('RecycleBins/Recycle Bins.shp')
        gdf.apply(self._create_place, axis=1)
