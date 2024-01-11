
class VehiclePhysics:

	def __init__(self):

		self.vehicleSpeed = [0,0,0]
		self.vehicleAcceleration = [0,0,0]

	def vehicleUpdate():
		
		pass

class RoadVehiclePhysics(VehiclePhysics):

	def __init__(self):
		
		super().__init__()

		self.vehicleDeccelerationRate = 0.05

	def vehicleUpdate(self):

		if self.vehicleSpeed[2] > 0:

			self.vehicleSpeed[2] -= self.vehicleDeccelerationRate

	def accelerate(self):

		if self.vehicleSpeed[2] < 30:

			self.vehicleSpeed[2] += 0.8

	def brake(self):

		if self.vehicleSpeed[2] > 0:

			self.vehicleSpeed[2] -= 4*(1/self.vehicleSpeed[2])

		else:

			self.vehicleSpeed[2] = 0

	def steerLeft(self):

		return self.vehicleSpeed[2] * 0.001

	def steerRight(self):

		return -self.vehicleSpeed[2] * 0.001

