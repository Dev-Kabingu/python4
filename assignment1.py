# Assignment 1
class Robot:
    def __init__(self, model, battery_level, sensors):
        # Constructor to initialize the robot with model, battery level, and sensors
        self.model = model
        self.battery_level = battery_level
        self.sensors = sensors  # List of sensors, e.g., ["camera", "ultrasonic"]

    def move(self):
        # Method to simulate robot movement
        if self.battery_level > 0:
            print(f"{self.model} is moving!")
            self.battery_level -= 10  # Moving consumes battery
        else:
            print(f"{self.model} has no battery left to move!")

    def detect_obstacles(self):
        # Method to simulate obstacle detection using sensors
        if "ultrasonic" in self.sensors:
            print(f"{self.model} detects obstacles using ultrasonic sensor.")
        else:
            print(f"{self.model} does not have ultrasonic sensor for obstacle detection.")

    def charge(self):
        # Method to charge the robot
        self.battery_level = 100
        print(f"{self.model} is charging... Battery is now full!")
        


# Create a Robot object
robot1 = Robot("Robot", 50, ["camera", "infrared"])
robot1.move()
robot1.detect_obstacles()
robot1.charge()


# Polymorphism and inheritance (Subclass)
class AutonomousRobot(Robot):
    def __init__(self, model, battery_level, sensors, ai_algorithm):
        # Inheriting from Robot and adding AI algorithm as an additional attribute
        super().__init__(model, battery_level, sensors)
        self.ai_algorithm = ai_algorithm

    def navigate(self):
        # Autonomous decision-making to navigate the environment
        if self.battery_level > 0:
            print(f"{self.model} is navigating using {self.ai_algorithm}.")
            self.battery_level -= 15  # Autonomous navigation consumes more battery
        else:
            print(f"{self.model} needs charging to navigate.")

    def detect_obstacles(self):
        # Overriding detect_obstacles to include AI-based detection
        if "ultrasonic" in self.sensors:
            print(f"{self.model} is detecting obstacles autonomously using ultrasonic sensor.")
        else:
            print(f"{self.model} is relying on other sensors for obstacle detection.")

# Create an AutonomousRobot object
robot2 = AutonomousRobot("AutoBot", 80, ["camera", "ultrasonic"], "Deep Learning")
robot2.move()
robot2.detect_obstacles()
robot2.navigate()
robot2.charge()
