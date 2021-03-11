import osmnx as osmnx
import argparse
import time
import osmnx as ox
import os
import warnings
warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser()
parser.add_argument("country")
parser.add_argument('poi_type')
args = parser.parse_args()

country = args.country
pois = args.poi_type

t0 = time.time()

print('starting ', country)

gdf = ox.pois.pois_from_place(args.country,{'amenity':args.poi_type})

t1=time.time()
if not os.path.exists('output/' + country):
    os.mkdir('output/'+ country)

gdf=gdf[['name','geometry']]
gdf.geometry = [geom.centroid if geom.type in ['Polygon','MultiPolygon','LineString'] else geom for geom in gdf.geometry]

out_pth = 'output/{}_{}.shp'.format(country, pois)
print('output: ' + out_pth)
gdf.to_file(out_pth)

print("retrieved {} POIs in {:,.0f} seconds".format(len(gdf), t1-t0))

