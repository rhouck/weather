import os

"""
converts hdf4 file to hdf5 format
reads from source_data
outputs to source_data/converted
"""

#dates = ['2014026', '2015001', '2015016']
dates = []

for d in dates:
	print d
	fn = os.path.join("source_data", "VHP.G16.C07.NP.P%s.ND.hdf" % (d))
	fo = os.path.join("source_data", "converted", "VHP.G16.C07.NP.P%s.ND.h5" % (d))
	os.system("./h4h5tools/bin/h4toh5 %s %s" % (fn, fo))

print "done"