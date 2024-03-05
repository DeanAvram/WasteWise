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
        obj = Object("recycle_facility", "admin")
        # bin_type = self._determine_bin_type(row['tsug'])
        bin_type = row['tsug']
        if ('זכוכית' in bin_type):
            bin_type = 'glass'
        elif ('קרטון' in bin_type):
            bin_type = 'cardboard'
        elif ('אריזות' in bin_type):
            bin_type = 'package'
        elif ('טקסטיל' in bin_type):
            bin_type = 'textile'
        elif ('נייר' in bin_type):
            bin_type = 'paper'
        elif ('אלקטרונית' in bin_type):
            bin_type = 'electronic'
        else:
            return
        obj.data = {
            "name": row['shemrechov'] + ' ' + str(int(row['msbait'])),
            "bin_type": bin_type,
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
        # print(gdf['shemrechov'])
        gdf.apply(self._create_place, axis=1)
