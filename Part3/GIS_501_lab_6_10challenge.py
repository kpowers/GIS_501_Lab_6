## Kelsey Powers GIS 501 Lab 6 Exercise 10 Challenge Problem 1
##AddLayer.. Add the parks layer from the Parks data frame in Austin_TX.mxd 
##to the other to data frames in the same map document

import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_6/GIS_501_data_L6/Exercise10/"
mapdoc = arcpy.mapping.MapDocument("D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_6/GIS_501_data_L6/Exercise10/Austin_TX.mxd")
addLayer = arcpy.mapping.ListLayers(mapdoc)[8]
facdf = arcpy.mapping.ListDataFrames(mapdoc, "Facilities")[0]
for df in facdf:
	print "dataframe = " + str(df)
	arcpy.mapping.AddLayer(df, addLayer)
facST = arcpy.mapping.ListDataFrames(mapdoc, "Street Trees")[0]
for df2 in facST:
	print "dataframe = " + str(df2)
	arcpy.mapping.AddLayer(df2, addLayer)
mapdoc.save()
del mapdoc
print "finished"
