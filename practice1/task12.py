# #Как известно, поверхность планеты Земля искривлена, и расстояние между точками, характеризующимися одинаковыми градусами по долготе, может быть разным в зависимости от широты. Таким образом, для вычисления расстояния между двумя точками на Земле одной лишь теоремой Пифагора не обойтись.
# Допустим, (t1 , g1) и (t2 , g2) – координаты широты и долготы двух точек на поверхности Земли. Тогда расстояние в километрах между ними с учетом искривленности планеты можно найти по следующей формуле:
# distance = 6371,01*arccos(sin(t1)*sin(t2) + cos(t1)*cos(t2)*cos(g1 - g2)).
import math

t1_degrees, g1_degrees = [
    int(i)
    for i in input("Введите координаты точки а в градусах через пробел:\n").split()
    ]
t2_degrees, g2_degrees = [
    int(i)
    for i in input("Введите координаты точки b в градусах через пробел:\n").split()
    ]
t1_radians = math.radians(t1_degrees)
g1_radians = math.radians(g1_degrees)
t2_radians = math.radians(t2_degrees)
g2_radians = math.radians(g2_degrees)

distance =6371.01*math.acos(math.sin(t1_radians)*math.sin(t2_radians) + math.cos(t1_radians)*math.cos(t2_radians)*math.cos(g1_radians-g2_radians))
print(f"расстояние от a до b равно {distance} км")