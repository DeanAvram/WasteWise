import pandas as pd
import os
import json
from src.data.object import Object
from pyproj import Proj, transform

is_loaded = False


class LoadFromExcel:
    def __init__(self, db):
        self.db = db
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, 'recycle_facilities.xlsx')
        self._df = pd.read_excel(file_path)
        self.itm_proj = Proj(init='epsg:2039')  # Israeli Transverse Mercator (ITM) projection
        self.wgs_proj = Proj(init='epsg:4326')  # World Geodetic System (WGS) projection

    def _create_place(self, row):
        itm_x = row['x']
        itm_y = row['y']

        wgs_lng, wgs_lat = transform(self.itm_proj, self.wgs_proj, itm_x, itm_y)
        #transformer = Transformer.from_crs("ESPG:2039", "ESPG:4326")
        #wgs_lng, wgs_lat = transformer.transform(itm_x, itm_y)

        # Create a new object
        obj = Object("place", "admin")
        obj.data = {
            "name": row['shem_rechov'] + ' ' + str(row['ms_bait']),
            "location": {
                "coordinates": [wgs_lng, wgs_lat]
            }
        }
        # Insert the object into the database
        self.db.objects.insert_one(json.loads(obj.toJSON()))

    def load_places(self):
        global is_loaded
        if is_loaded:
            return
        self._df.apply(self._create_place, axis=1)
        is_loaded = True
