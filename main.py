from smart_home import *

# Инициализация мест
Outside = OutsideConditions()
WaterConditions1 = WaterConditions(Outside)
Hallway = Room(Outside,"Прихожая",[],[])
Bathroom = WaterRoom(WaterConditions1, "Ванная",[],[])
Kitchen = WaterRoom(WaterConditions1, "Кухня",[],[])
Balcony = Room(Outside,"Балкон",[],[])
Home1 = Home(Outside, [Hallway, Bathroom, Kitchen, Balcony])

# Инициализация и добавление сенсоров
MovementSensor1 = MovementSensor(random.randrange(0, 2))
Hallway.add_sensor(MovementSensor1)

FloodSensor1 = FloodSensor(Bathroom)
Bathroom.add_sensor(FloodSensor1)

MovementSensor2 = MovementSensor(random.randrange(0, 2))
Bathroom.add_sensor(MovementSensor2)

FloodSensor2 = FloodSensor(Kitchen)
Kitchen.add_sensor(FloodSensor2)

HumiditySensor1 = HumiditySensor(Kitchen)
Kitchen.add_sensor(HumiditySensor1)

LightSensor1 = LightSensor(Kitchen)
Kitchen.add_sensor(LightSensor1)

Termometer1 = Termometer(Kitchen)
Kitchen.add_sensor(Termometer1)

Termometer2 = Termometer(Balcony)
Balcony.add_sensor(Termometer2)

# Инициализация и добавление девайсов
Lamp1 = Lamp(Hallway)
Hallway.add_device(Lamp1)

Lamp2 = Lamp(Bathroom)
Bathroom.add_device(Lamp2)

WaterPipeline1 = WaterPipeline(Bathroom)
Bathroom.add_device(WaterPipeline1)

Lamp3 = Lamp(Kitchen)
Kitchen.add_device(Lamp3)

Heater1 = Heater(Kitchen)
Kitchen.add_device(Heater1)

WaterPipeline2 = WaterPipeline(Kitchen)
Kitchen .add_device(WaterPipeline2)

Humidifier1 = Humidifier(Kitchen)
Kitchen.add_device(Humidifier1)

Lamp5 = Lamp(Kitchen)
Kitchen.add_device(Lamp5)

Lamp6 = Lamp(Kitchen)
Kitchen.add_device(Lamp6)

Window1 = Window(Kitchen,Outside)
Kitchen.add_device(Window1)

Curtain1 = Curtain(Kitchen,Outside)
Kitchen.add_device(Curtain1)

Lamp4 = Lamp(Balcony)
Balcony.add_device(Lamp4)

Heater2 = Heater(Balcony)
Balcony.add_device(Heater2)

Window2 = Window(Balcony,Outside)
Balcony.add_device(Window2)

Curtain2 = Curtain(Balcony,Outside)
Balcony.add_device(Curtain2)

# Инициализация контроллера
Controller1 = Controller(Home1)


# Проверка параметров в консли
Outside.print()
Controller1.check_home()