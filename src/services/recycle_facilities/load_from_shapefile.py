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
        # bin_type = self._determine_bin_type(row['tsug'])
        bin_type = row['tsug']
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

    @staticmethod
    def _determine_bin_type(bin_type_column):
        print(bin_type_column)
        bin_type_arr = bin_type_column.split(' ')
        if bin_type_arr[-1] == 'מונף':
            return bin_type_arr[-2]
        return bin_type_arr[-1]
