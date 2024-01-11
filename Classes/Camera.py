from Classes.Physics import RoadVehiclePhysics

class Camera:

	def __init__(self, position, horizontalAngle, verticalAngle, projectionViewer, fieldOfView=250, zoom=250, projectionType='orthographic'):

		self.position = position
		self.horizontalAngle = horizontalAngle
		self.verticalAngle = verticalAngle
		self.fieldOfView = fieldOfView
		self.zoom = zoom
		self.projectionType = projectionType
		self.projectionViewer = projectionViewer

	def LEFT(self):
		
		self.projectionViewer.rotateAboutCamera('Y', 0.05)

	def RIGHT(self):
		
		self.projectionViewer.rotateAboutCamera('Y', -0.05)

	def DOWN(self):
		
		self.projectionViewer.moveCameraVertically(20)

	def UP(self):
		
		self.projectionViewer.moveCameraVertically(-20)

	def W(self):
		
		self.projectionViewer.moveCameraHorizontally('Z', -20)

	def S(self):
		
		self.projectionViewer.moveCameraHorizontally('Z', 20)

	def A(self):
		
		self.projectionViewer.moveCameraHorizontally('X', -20)
	
	def D(self):
		
		self.projectionViewer.moveCameraHorizontally('X', 20)

class CarCamera(Camera):

	def __init__(self, position, horizontalAngle, verticalAngle, projectionViewer, fieldOfView=250, zoom=250, projectionType='orthographic'):

		super().__init__(position, horizontalAngle, verticalAngle, projectionViewer, fieldOfView=250, zoom=250, projectionType='orthographic')

		self.carPhysics = RoadVehiclePhysics()
		self.braking = False

		projectionViewer.backgroundFunctions.append(self.updateCamera)

	def updateCamera(self):

		if self.braking == False:

			self.carPhysics.vehicleUpdate()

			self.projectionViewer.moveCameraHorizontally('Z', -self.carPhysics.vehicleSpeed[2])

		else:

			self.braking = False

	def W(self):

		#Accelerator

		self.carPhysics.accelerate()

		self.projectionViewer.moveCameraHorizontally('Z', -self.carPhysics.vehicleSpeed[2])

	def S(self):

		#Brake

		self.braking = True

		self.carPhysics.brake()

		self.projectionViewer.moveCameraHorizontally('Z', -self.carPhysics.vehicleSpeed[2])


	def LEFT(self):

		steerAmount = self.carPhysics.steerLeft()

		self.projectionViewer.rotateAboutCamera('Y', steerAmount)

	def RIGHT(self):

		steerAmount = self.carPhysics.steerRight()

		self.projectionViewer.rotateAboutCamera('Y', steerAmount)





