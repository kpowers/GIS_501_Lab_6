## Kelsey Powers GIS 501 Lab 6 Challenge problem 1 from Exercise 09
# moderate slope: 5-20 deg
#Southerly aspect: 150-270 deg
#Forested: land cover types of 41, 42, 43

import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.env.overwriteOutput = True
env.workspace = "D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_6/GIS_501_data_L6/Exercise09/"
elevraster = arcpy.Raster("elevation")
#define input raster

if arcpy.CheckExtension("spatial") == "Available":
	arcpy.CheckOutExtension("spatial")
	slope = arcpy.sa.Slope(elevraster)
	elevraster.save("slope")
else:
	print "Spatial Analyst license is not available."

##Find Moderate Slopes!
lowslopedeg = slope > 5
upslopedeg = slope < 20

modslope = lowslopedeg & upslopedeg
modslope.save("moderateslope")

##Find southerly aspect slopes
aspslope = Aspect(slope)
SouthLow = aspslope > 150
SouthHigh = aspslope< 270
Southerlyslope = SouthLow & SouthHigh

Southerlyslope.save("SoutherlySlope.tif")

##Find Forested Land. Types: 41, 42,43
inraster = arcpy.Raster("landcover.tif")
myRemapVal = RemapValue([[41, 1],[42,2],[43,3]])
outreclass = Reclassify(inraster, "VALUE", myRemapVal, "NODATA")
outreclass.save("lc_recl.tif")

final = Southerlyslope & outreclass & modslope
final.save("final.tif")
arcpy.CheckInExtension("spatial.tif")