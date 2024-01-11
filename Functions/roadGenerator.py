
from Classes.Wireframe import Wireframe
from Classes.Face import Face
import numpy as np

def roadGenerator():
		
	roadWireframe = Wireframe()

	nodes, faces = straightRoad()

	roadWireframe.addNodes(nodes)
	roadWireframe.addFaces(faces)

	return roadWireframe

def straightRoad():
	
	nodes = np.array(
					[[0,0,0],
					[1500, 0,0],
					[1500, 0, 10000],
					[0, 0, 10000]]
					)

	faces = [
				Face([0,2,1], [0,1,0], [177,177,177]),
			 	Face([3,2,0], [0,1,0], [177,177,177]),
			]

	return nodes, faces

def turn():
	pass

def tJunction():
	pass
