from direct.showbase.ShowBase import ShowBase
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses

class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()

        fullCycle = 60
        #t = 0
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)

            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseballSeams(self.Planet3, nickName, j, fullCycle, 2)
            #self.DrawCircleXY(self.Planet6, nickName, t)
           # t = t + 2
            defensePaths.CircleXY(self)
            defensePaths.CircleXZ(self)
            defensePaths.CircleYZ(self)

    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/Drones/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/Drones/DroneDefender/octotoad1_auv.png", position, 10)

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/Drones/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/Drones/DroneDefender/octotoad1_auv.png", position, 5)

    #def DrawCircleXY(self, centralObject, droneName, step, radius = 1):
        #unitVec = defensePaths.CircleXY(step)
        #unitVec.normalize()
        #position = unitVec * radius + centralObject.modelNode.getPos()
       # print(position)
        #spaceJamClasses.Drone(self.loader, "./Assets/Drones/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/Drones/DroneDefender/octotoad1_auv.png", position, 5)

    def SetupScene(self):
            #Universe
        #self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")                                       #Load universe model
        #self.Universe.reparentTo(self.render)                                                                       
        #self.Universe.setScale(15000)                                                                               #Scales up universe

        #texUni = self.loader.loadTexture("./Assets/Universe/starfield-in-blue.jpg")                                 #Set texture of Universe
        #self.Universe.setTexture(texUni, 1)

        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', "./Assets/Universe/starfield-in-blue.jpg", (0, 0, 0), 15000)

            #Spaceship
        #self.Ship = self.loader.loadModel("./Assets/Spaceships/Destroyer/OhMy.egg")
        #self.Ship.reparentTo(self.render)
        #self.Ship.setPos(100, 1000, 100)
        
        self.Ship = spaceJamClasses.Spaceship(self.loader,"./Assets/Spaceships/Destroyer/OhMy.egg", self.render, 'Ship', (100, 1000, 100), 0.5)

            #Planets
        #self.Planet1 = self.loader.loadModel("./Assets/Planets/redPlanet.x")                                        #Load planet
        #self.Planet1.reparentTo(self.render)
        #self.Planet1.setPos(150, 5000, 67)                                                                          #Place planets in different spots
        #self.Planet1.setScale(350)                                                                                  #Scales up planet

        #texPlan1 = self.loader.loadTexture("./Assets/Planets/Planet1.jpg")                                          #Set texture of Planet
        #self.Planet1.setTexture(texPlan1, 1)

        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/redPlanet.x", self.render, 'Planet1', "./Assets/Planets/Planet1.jpg", (150, 5000, 67), 350)

        #self.Planet2 = self.loader.loadModel("./Assets/Planets/redPlanet.x")
        #self.Planet2.reparentTo(self.render)
        #self.Planet2.setPos(5000, 1000, 183)
        #self.Planet2.setScale(600)

        #texPlan2 = self.loader.loadTexture("./Assets/Planets/Planet2.jpg")
        #self.Planet2.setTexture(texPlan2, 1)

        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/redPlanet.x", self.render, 'Planet2', "./Assets/Planets/Planet2.jpg", (5000, 1000, 183), 600)

        #self.Planet3 = self.loader.loadModel("./Assets/Planets/redPlanet.x")
        #self.Planet3.reparentTo(self.render)
        #self.Planet3.setPos(500, 9060, 23)
        #self.Planet3.setScale(200)

        #texPlan3 = self.loader.loadTexture("./Assets/Planets/Planet3.png")
        #self.Planet3.setTexture(texPlan3, 1)

        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/redPlanet.x", self.render, 'Planet3', "./Assets/Planets/Planet3.png", (500, 9060, 23), 200)

        #self.Planet4 = self.loader.loadModel("./Assets/Planets/redPlanet.x")
        #self.Planet4.reparentTo(self.render)
        #self.Planet4.setPos(1000, 1833, 1000)
        #self.Planet4.setScale(350)

        #texPlan4 = self.loader.loadTexture("./Assets/Planets/Planet4.png")
        #self.Planet4.setTexture(texPlan4, 1)

        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/redPlanet.x", self.render, 'Planet4', "./Assets/Planets/Planet4.png", (1000, 1833, 1000), 350)

        #self.Planet5 = self.loader.loadModel("./Assets/Planets/redPlanet.x")
        #self.Planet5.reparentTo(self.render)
        #self.Planet5.setPos(183, 500, 1500)
        #self.Planet5.setScale(300)

        #texPlan5 = self.loader.loadTexture("./Assets/Planets/Planet5.png")
        #self.Planet5.setTexture(texPlan5, 1)

        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/redPlanet.x", self.render, 'Planet5', "./Assets/Planets/Planet5.png", (183, 500, 1500), 300)

        #self.Planet6 = self.loader.loadModel("./Assets/Planets/redPlanet.x")
        #self.Planet6.reparentTo(self.render)
        #self.Planet6.setPos(20, 20, 23)
        #self.Planet6.setScale(400)

        #texPlan6 = self.loader.loadTexture("./Assets/Planets/Planet6.png")
        #self.Planet6.setTexture(texPlan6, 1)

        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/redPlanet.x", self.render, 'Planet6', "./Assets/Planets/Planet6.png", (2000, 2000, 2300), 400)

            #Space Station
        #self.Station = self.loader.loadModel("./Assets/Space Station/SpaceStation1B/spaceStation.egg")
        #self.Station.reparentTo(self.render)
        #self.Station.setPos(-1000, -1000, -1000)
        #self.Station.setScale(40)

        self.Station = spaceJamClasses.SpaceStation(self.loader, "./Assets/SpaceStation/SpaceStation1B/spaceStation.egg", self.render, 'Station', (-1000, -1000, -1000), 40)
        
        


        

        
app = SpaceJam()
app.run()