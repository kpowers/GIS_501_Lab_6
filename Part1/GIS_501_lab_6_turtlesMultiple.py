##GIS 501 - Lab 6 problem 1 Create a turtle
##You are going to write a script that asks the user to input a number and then draws a shape with that number of sides!
import arcpy, turtle, fileinput, string
				#allows us to use the turtles library	
wn = turtle.Screen()                            #creates a graphics window
turtle.speed                                    #gives turtle max speed
wn.bgcolor('lightblue')		                #background color to light blue
alex = turtle.Turtle() 			        #create a turtle named alex
alex.color('darkgreen')

##Setup Turtle Bob.
bob = turtle.Turtle()
bob.color ('blue')
#set turtle bob's start location 100 pixels to the right
bob.penup()
bob.setx(100)
bob.pendown()

arcpy.env.overwriteOutput = True #be able to overwrite data
filelocation = "D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_6/"  #WHERE YOU WANT YOUR NEW FILE
fc = "turtle_poly.shp"		##place to put turtle feature class
spatialref = "D:\GIS_501_AU_2014_Directory\GIS501_Labs\GIS501_Lab_6\GIS_501_data_L6\Exercise10/WGS_1984.prj"
arcpy.management.CreateFeatureclass(filelocation, fc, "POLYGON", "", "", "", spatialref)

##Create a  search cursor to  iterate through each row of the input feature class.
##Create an insert cursor to insert rows into the output feature class.
cursIns = arcpy.da.InsertCursor(fc, ["SHAPE@"])
cursSrch =  arcpy.da.SearchCursor(fc, ["SHAPE@"])

##create an empty array  and point object needed to create features
point = arcpy.Point()
array = arcpy.Array()
pointB = arcpy.Point()
arrayB = arcpy.Array()		

print ("This program draws shapes based on the numbers you enter in a uniform pattern.")
num_sides = int(input("Enter the number of sides for an equilateral polygon the turtle will draw. First Turtle:  "))
num_sidesbob = int(input("Second Turtle:  "))

#divide the inside angle by number of sides input by user to determine angle that the turtle turns.
angle = int(360/num_sides)
anglebob = int(360/num_sidesbob)

for num_sides in range (num_sides):
    alex.forward(50)                            #length of each line segment
    alex.left(angle)
    point.X, point.Y=alex.position()
    array.add(point)

for num_sidesbob in range(num_sidesbob):
	bob.forward(50)
	bob.left(anglebob)
	point.X, point.Y = bob.position()
	arrayB.add(point)
	
#make an array of arrays to create multipart poygon
multiarray = arcpy.Array([array, arrayB])
#create polygon from array
polygon = arcpy.Polygon(multiarray)
#insert polygon into feature class
cursIns.insertRow([polygon])


del cursIns
del cursSrch

turtle.mainloop()                               #keeps turtle draw window from freezing
    
    




