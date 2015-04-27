import numpy as np
import pandas as pd
import h5py
import os

"""
process hdf5 file into format consumable by spotfire
reads frmo source_data/converted
outputs to processed_data
"""

dates = ['2014026', '2015001', '2015016']
#dates = []

for d in dates:
	print d
	fn = os.path.join("source_data", "converted", "VHP.G16.C07.NP.P%s.ND.h5" % (d))
	fo = os.path.join("processed_data", "VHP.G16.C07.NP.P%s.ND.csv" % (d))

	# import ndvi hdf5 dataset
	f = h5py.File('test.h5','r') 
	ndvi =  f['NDVI']

	# create dataframe from dataset
	bank = []
	for ind, r in enumerate(ndvi):
		bank.append(r)
	df = pd.DataFrame(data=bank)

	# reverse row order
	df = df.iloc[::-1]

	# replace index with latitude values
	lat = (f.attrs.__getitem__('geospatial_lat_min_GLOSDS'), f.attrs.__getitem__('geospatial_lat_max_GLOSDS'))
	ran = lat[1] - lat[0]
	inc = ran / ndvi.shape[0]
	lat_ind = [round((lat[0] + ind * inc), 5) for ind in range(ndvi.shape[0])]
	lat_ind.reverse()
	df.index = lat_ind

	# replace column names with longitude values
	lon = (f.attrs.__getitem__('geospatial_lon_min_GLOSDS'), f.attrs.__getitem__('geospatial_lon_max_GLOSDS'))
	ran = lon[1] - lon[0]
	inc = ran / ndvi.shape[1]
	lon_ind = [round((lon[0] + ind * inc), 5) for ind in range(ndvi.shape[1])]
	df.columns = lon_ind

	# stack for spotfire
	df = df.stack().reset_index()
	df.columns = ['lat', 'lng', 'val']

	df.to_csv(fo)

print "done"