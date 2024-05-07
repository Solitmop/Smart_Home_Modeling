from datetime import datetime
import random

# Нормальные значения
NormalTemperature = 25  #°C
NormalHumidity    = 40  #%
NormalLight       = 150 #люкс

# Функции случайных значений
def random_temperature():
    return random.randint(-30, 35)
def random_humidity():
    return random.randrange(0, 100)
def random_light():
    return random.randrange(0, 150)
def random_time():
    return datetime.strptime(str(random.randrange(0, 24))+':'+str(random.randrange(0, 60))+':'
                                                             +str(random.randrange(0, 60)), "%H:%M:%S")
# Условия
class GeneralConditions:
    def __init__(self, temperature=random_temperature(), humidity=random_humidity(), light=random_light()):
        self.temperature = temperature
        self.humidity = humidity
        self.light = light
    def get_temperature(self):
        return self.temperature
    def get_humidity(self):
        return self.humidity
    def get_light(self):
        return self.light
    def set_temperature(self, temperature=random_temperature()):
        self.temperature = temperature
    def set_humidity(self, humidity=random_humidity()):
        self.humidity = humidity
    def set_light(self, light=random_light()):
        self.light = light
class WaterConditions(GeneralConditions):
    def __init__(self, temperature=random_temperature(), humidity=random_humidity(), light=random_light(), flood=random.randrange(0, 2), water_flow=True):
        self.flood = flood
        self.water_flow = water_flow
        super().__init__(temperature, humidity, light)
    def __init__(self, Conditions:GeneralConditions, flood=random.randrange(0, 2), water_flow=True):
        self.flood = flood
        self.water_flow = water_flow
        super().__init__(Conditions.get_temperature(),Conditions.get_humidity(),Conditions.get_light())
    def get_flood(self):
        return self.flood
    def get_water_flow(self):
        return self.water_flow
    def set_flood(self, flood):
        self.flood = flood
    def set_water_flow(self, water_flow):
        self.water_flow = water_flow
class OutsideConditions(GeneralConditions):
    def __init__(self, Conditions:GeneralConditions, time=random_time()):
        super().__init__(Conditions.get_temperature(),Conditions.get_humidity(),Conditions.get_light())
        self.time = time
    def __init__(self, temperature=random_temperature(), humidity=random_humidity(), light=random_light(), time=random_time()):
        super().__init__(temperature, humidity, light)
        self.time = time
    def get_time(self):
        return self.time
    def set_time(self, time):
        self.time = time
    def print(self):
        print("Внешние условия:")
        print("Время: ",self.time.strftime("%H:%M"))
        print("Температура: ",self.temperature)
        print("Влажность: ",self.humidity)
        print("Свет: ",self.light)
    
# Места
class Room(GeneralConditions):
    def __init__(self,Conditions,name,sensors:list,devices:list):
        self.name = name
        self.sensors = sensors
        self.devices = devices
        self.set_humidity(Conditions.get_humidity())
        self.set_temperature(Conditions.get_temperature())
        self.set_light(Conditions.get_light())
    def add_sensor(self, sensor):
        self.sensors.append(sensor)
    def add_device(self, device):
        self.devices.append(device)
    def get_name(self):
        return self.name
class WaterRoom(Room, WaterConditions):
    def __init__(self,Conditions,name,sensors:list,devices:list):
        self.name = name
        self.sensors = sensors
        self.devices = devices
        self.set_flood(Conditions.get_flood())
        self.set_water_flow(Conditions.get_water_flow())
        self.set_humidity(Conditions.get_humidity())
        self.set_temperature(Conditions.get_temperature())
        self.set_light(Conditions.get_light())
class Home:
    def __init__(self,outside:OutsideConditions,rooms=[]):
        self.rooms = rooms
        self.outside = outside
    def add_room(self, room):
        self.rooms.append(room)
# Датчики
class Sensor:
    def __init__(self,Conditions:GeneralConditions):
        self.Conditions = Conditions
    def set_conditions(self, Conditions):
        self.Conditions = Conditions
    def get_conditions(self):
        return self.Conditions
class Clock(Sensor):
    def __init__(self,conditions:GeneralConditions):
        super().__init__(conditions)
        self.time = self.Conditions.get_time()
    def get_real_time(self):
        return datetime.datetime.now().time()
    def get_time(self):
        return self.time
    def set_conditions_time(self):
        self.time = self.Conditions.get_time()
    def set_time(self, time):
        self.time = time
class Termometer(Sensor):
    def __init__(self,Conditions:GeneralConditions):
        super().__init__(Conditions)
    def get_temperature(self):
        return self.Conditions.get_temperature()
class HumiditySensor(Sensor):
    def __init__(self,Conditions:GeneralConditions):
        super().__init__(Conditions)
    def get_humidity(self):
        return self.Conditions.get_humidity()
class LightSensor(Sensor):
    def __init__(self,Conditions:GeneralConditions):
        super().__init__(Conditions)
    def get_light(self):
        return self.Conditions.get_light()
class MovementSensor(Sensor):
    def __init__(self, movement=False):
        self.movement = movement
    def get_movement(self):
        return self.movement
    def set_movement(self, movement):
        self.movement = movement
class FloodSensor(Sensor):
    def __init__(self,Conditions:WaterConditions):
        super().__init__(Conditions)
    def get_state(self):
        return self.Conditions.get_flood()
# Управляемые элементы
class Device:
    def __init__(self, Conditions:GeneralConditions, state=False):
        self.state = state
        self.Conditions = Conditions
    def get_state(self):
        return self.state
    def set_conditions(self, Conditions):
        self.Conditions = Conditions
    def get_conditions(self):
        return self.Conditions

class Lamp(Device):
    def __init__(self, Conditions:GeneralConditions, state=False):
        super().__init__(Conditions,state)
    def on(self):
        self.state = True
        self.Conditions.set_light(NormalLight)
    def off(self):
        self.state = False
        self.Conditions.set_light(0)
class Heater(Device):
    def __init__(self,Conditions:GeneralConditions, state=False):
        super().__init__(Conditions,state)
    def on(self):
        self.state = True
        self.Conditions.set_temperature(self.Conditions.get_temperature() + 1)
        self.Conditions.set_humidity(self.Conditions.get_humidity() - 1)
    def off(self):
        self.state = False
class Humidifier(Device):
    def __init__(self, Conditions:GeneralConditions, state=False):
        super().__init__(Conditions,state)
    def on(self):
        self.state = True
        self.Conditions.set_humidity(self.Conditions.get_humidity() + 1)
    def off(self):
        self.state = False
class Window(Device):
    def __init__(self, InsideConditions:GeneralConditions, OutsideConditions:GeneralConditions, state=False): #False - закрыт, True - открыт
        super().__init__(InsideConditions,state)
        self.OutsideConditions = OutsideConditions
    def open(self):
        self.state = True
        self.Conditions.set_temperature(self.Conditions.get_temperature() - 1)
    def close(self):
        self.state = False
class Curtain(Device):
    def __init__(self, InsideConditions:GeneralConditions, OutsideConditions:GeneralConditions, state=False): #False - закрыт, True - открыт
        super().__init__(InsideConditions,state)
        self.OutsideConditions = OutsideConditions
    def open(self):
        self.state = True
        self.Conditions.set_light(self.OutsideConditions.get_light())
    def close(self):
        self.state = False
        self.Conditions.set_light(0)
class WaterPipeline(Device):
    def __init__(self, Conditions:WaterConditions, state=True): #False - закрыт, True - открыт
        super().__init__(Conditions,state)
    def on(self):
        self.state = True
        self.Conditions.set_water_flow(True)
    def off(self):
        self.state = False
        self.Conditions.set_water_flow(False)
        self.Conditions.set_flood(False)
# Прямое управление
class Phone:
    def __init__(self):
        pass
    def set_temperature(self, temperature):
        global NormalTemperature
        NormalTemperature = temperature
    def set_humidity(self, humidity):
        global NormalHumidity
        NormalHumidity = humidity
    def set_light(self, light):
        global NormalLight 
        NormalLight = light
class Controller:
    def __init__(self,Home:Home):
        self.Home = Home
    def check_home(self):
        for room in self.Home.rooms:
            print('Проверка комнаты', room.get_name())
            self.check_room(room)
    def check_room(self, room:Room):
        if type(room) is WaterRoom:
            for sensor in room.sensors:
                if type(sensor) is FloodSensor:
                    self.check_flood(sensor,room)
                    print('В', room.get_name(), 'нет потопа')
        for sensor in room.sensors:
            if type(sensor) is Termometer:
                self.check_temperature(sensor,room)
                print('Температура в норме')
            elif type(sensor) is HumiditySensor:
                self.check_humidity(sensor,room)
                print('Влажность в норме')
            elif type(sensor) is LightSensor:
                self.check_light(sensor,room)
                print('Свет в норме')
            elif type(sensor) is MovementSensor:
                self.check_movement(sensor,room)
    def check_flood(self,sensor,room):
        if sensor.get_state():
            print('Потоп в', room.get_name())
            for device in room.devices:
                if type(device) is WaterPipeline:
                    device.off()
                    print("Выключено водоснабжение")
    def check_temperature(self,sensor,room):
        if sensor.get_temperature() > NormalTemperature:
            print('Температура выше нормы')
            for device in room.devices:
                if type(device) is Heater:
                    device.off()
                elif type(device) is Window:
                    delta_temperature = sensor.get_temperature()
                    while sensor.get_temperature() > NormalTemperature:
                        device.open()
                    delta_temperature = sensor.get_temperature() - delta_temperature
                    print("Температура изменилась на", delta_temperature, "градусов")
        elif sensor.get_temperature() < NormalTemperature:
            print('Температура ниже нормы')
            for device in room.devices:
                if type(device) is Heater:
                    delta_temperature = sensor.get_temperature()
                    while sensor.get_temperature() < NormalTemperature:
                        device.on()
                    delta_temperature = sensor.get_temperature() - delta_temperature
                    print("Температура изменилась на", delta_temperature, "градусов")
                elif type(device) is Window:
                    device.close()
    def check_humidity(self,sensor,room):
        if sensor.get_humidity() > NormalHumidity:
            print('Влажность выше нормы')
            for device in room.devices:
                if type(device) is Humidifier:
                    device.off()
                elif type(device) is Heater:
                    delta_humidity = sensor.get_humidity()
                    while sensor.get_humidity() > NormalHumidity:
                        device.on()
                    delta_humidity = sensor.get_humidity() - delta_humidity
                    print("Влажность изменилась на", delta_humidity, "%")
            for sensor2 in room.sensors:
                if type(sensor2) is Termometer:
                    self.check_temperature(sensor2,room)
        elif sensor.get_humidity() < NormalHumidity:
            print('Влажность ниже нормы')
            for device in room.devices:
                if type(device) is Humidifier:
                    delta_humidity = sensor.get_humidity()
                    while sensor.get_humidity() < NormalHumidity:
                        device.on()
                    delta_humidity = sensor.get_humidity() - delta_humidity
                    print("Влажность изменилась на", delta_humidity, "%")
                elif type(device) is Heater:
                    device.off()
    def check_light(self,sensor,room):
        if sensor.get_light() > NormalLight:
            print('Свет выше нормы')
            for device in room.devices:
                if type(device) is Lamp:
                    device.off()
                elif type(device) is Curtain:
                    device.open()
                    print("Открыты шторы")
        elif sensor.get_light() < NormalLight:
            print('Свет ниже нормы')
            for device in room.devices:
                if type(device) is Lamp:
                    device.on()
                    print("Выключено освещение")
                elif type(device) is Curtain:
                    device.close()
    def check_movement(self,sensor,room):
        if sensor.get_movement():
            print('Замечено движение в', room.get_name())
            for device in room.devices:
                if type(device) is Lamp:
                    device.on()
                    print("Включено освещение")
                    break
        else:
            for device in room.devices:
                if type(device) is Lamp:
                    device.off()
