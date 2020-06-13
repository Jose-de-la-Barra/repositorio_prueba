import math


def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d


centros_salud = ['Posta central Stgo', 'Hospital El Carmen', 'Hospital San Juan de Dios',
                 'Clínica Las Condes', 'Clínica Alemana', 'Clínica Indisa']

centros_salud_ubicacion = [[-33.4437, -70.6380], [-33.5081, -70.7743], [-33.4422, -70.6790],
                           [-33.3848, -70.5303], [-33.3924, -70.5730], [-33.4213, -70.6186]]

ubicacion_lat = float(input("Ingrese la latitud de su ubicación anteponiendo un signo de menos: "))
ubicacion_long = float(input("Ingrese la longitud su ubicación anteponiendo un signo de menos: "))

ubicacion = [ubicacion_lat, ubicacion_long]
lat = []
long = []
a = 999

for i in centros_salud_ubicacion:
    lat.append(i[0])
    long.append(i[1])


for j in range(len(centros_salud_ubicacion)):
    distancia = distance((ubicacion_lat, ubicacion_long), tuple(centros_salud_ubicacion[j]))
    print(f'{centros_salud[j]} está a {round(distancia, 3)} kilómetros')  # ocupe round para redondear los números
    print()
    if distancia < a:
        a = distancia
        cercano = centros_salud[j]
print()
print()
print(f'El hospital más cercano es {cercano} y está a {round(a, 3)} kilómetros')




