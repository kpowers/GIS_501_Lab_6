## Kelsey Powers GIS 501 Lab 6 Challenge problem 2 from Exercise 09

import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_6/GIS_501_data_L6/Exercise09/"

arcpy.CreateFileGDB_Management("D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_6/GIS_501_data_L6/Exercise09/", "new.gdb")
rasterlist=arcpy.ListRasters()
for raster in rasterlist:
	print raster
	arcpy.RasterToGeodatabase_conversion(raster, "new.gdb")
