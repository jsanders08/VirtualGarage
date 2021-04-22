class Vehicle:
  def __init__(self,make,model,color,fuelType,options):
    self.make = make
    self.model = model
    self.color = color
    self.fuelType = fuelType
    self.options = options
    def getMake(self):
      return self.make
    def getModel(self):
      return self.model
    def getColor(self):
      return self.color
    def getFuelType(self):
      return self.fuelType
    def getOptions(self):
      return self.options

class Car(Vehicle):
    def __init__(self, make, model, color, fuelType, options, engineSize, numDoors):
      Vehicle.__init__(self,make,model,color,fuelType,options)
      self.engineSize = engineSize
      self.numDoors = numDoors
    def getEngineSize(self):
      return self.engineSize
    def getnumDoors(self):
      return self.numDoors
    def printDetails(self):
      print("Car Make:",self.make)
      print("Car Model:",self.model)
      print("Car Color:", self.color)
      print("Car Fuel Type:", self.fuelType)
      print("Car Options:", self.options)
      print("Car Engine Size:", self.engineSize)
      print("Number of Car Doors:", self.numDoors)
class Pickup(Vehicle):
    def __init__(self,make, model, color, fuelType, options, cabStyle, bedLength):
      Vehicle.__init__(self, make, model, color, fuelType, options)
      self.cabStyle=cabStyle
      self.bedLength=bedLength
    def getCabStyle(self):
      return self.cabStyle
    def getBedLength(self):
      return self.bedLength
    def printDetails(self):
      print("Pickup Make:", self.make)
      print("Pickup model:", self.model)
      print("Pickup Color:", self.color)
      print("Pickup Fuel Type:", self.fuelType)
      print("Pickup Options:", self.options)
      print("Pickup Cab Style:", self.cabStyle)
      print("Pickup Bed Length:", self.bedLength)
garage=[]
while(True):
  option =input("Enter \n1 for Car \n2 for Pickup \n3 for Exit \n")
  if(option==1):
    make=input("Enter Car Make :")
    model=input("Enter Car Model :")
    color=input("Enter Car Color :")
    fuelType=input("Enter Car Fuel type :")
    options=input("Enter Car Option separated by space :")
    enginesize=int(input("Enter Car Engine Size :"))
    numDoors=int(input("Enter Number of Car Doors :"))
    p= Car(make, model, color,fuelType, options, engineSize, numDoors)
    garage.append(p)
  elif(option==2):
    make=input("Enter Pickup Make :")
    model=input("Enter Pickup Model :")
    color=input("Enter Pickup Color :")
    fuelType=input("Enter Pickup Fuel Type: ")
    options=input("Enter Pickup Option separated by space :")
    cabStyle=input("Enter Pickup Cab Style :")
    bedLength=int(input("Enter Pickup Bed Length :"))
    t= Pickup(make, model, color, fuelType, options, cabStyle, bedLength)
    garage.append(t)
  else:
    raise SystemExit
    print("Here is your vehicle details :")
    print("-----------------------")
  for v in garage:
    print(v.printDetails())
