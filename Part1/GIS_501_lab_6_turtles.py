##GIS 501 - Lab 6 problem 1 Create a turtle
##You are going to write a script that asks the user to input a number and then draws a shape with that number of sides!
import arcpy, turtle, fileinput, string
				#allows us to use the turtles library	
#wn = turtle.Screen()                            #creates a graphics window
turtle.speed                                    #gives turtle max speed
#wn.bgcolor('lightblue')		                #background color to light blue
alex = turtle.Turtle() 			        #create a turtle named alex
alex.color('darkgreen')

arcpy.env.overwriteOutput = True #be able to overwrite data
filelocation = "E:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_6/"  #WHERE YOU WANT YOUR NEW FILE
fc = "turtle_poly.shp"		##place to put turtle feature class
spatialref = "E:\GIS_501_AU_2014_Directory\GIS501_Labs\GIS501_Lab_6\GIS_501_data_L6\Exercise10/WGS_1984.prj"
arcpy.management.CreateFeatureclass(filelocation, fc, "POLYGON", "", "", "", spatialref)
arcpy.management.AddField(fc, "X", "FLOAT")
arcpy.management.AddField(fc, "Y", "FLOAT")

##Create a  search cursor to  iterate through each row of the input feature class.
##Create an insert cursor to insert rows into the output feature class.
cursIns = arcpy.da.InsertCursor(fc, ["SHAPE@"])

##create an empty array  and point object needed to create features
point = arcpy.Point()
array = arcpy.Array()		

print ("This program draws shapes based on the numbers you enter in a uniform pattern.")
num_sides = int(input("Enter the number of sides for an equilateral polygon the turtle will draw: "))

#divide the inside angle by number of sides input by user to determine angle that the turtle turns.
angle = int(360/num_sides)

for num_sides in range (num_sides):
    alex.forward(50)                            #length of each line segment
    alex.left(angle)
    point.X, point.Y=alex.position()
    array.add(point)
polygon = arcpy.Polygon(array)
cursIns.insertRow([polygon])
    #cursIns.insertRow()
    #for row in cursIns:

#cursIns.insertRow([arcpy.Polygon(array)])
del cursIns

turtle.mainloop()                               #keeps turtle draw window from freezing
    
    




