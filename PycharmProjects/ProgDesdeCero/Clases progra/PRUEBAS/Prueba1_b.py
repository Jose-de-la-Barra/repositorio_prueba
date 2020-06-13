edad = int(input("Ingrese su edad: "))
factor_genero = input("Ingrese su género (H O M): ")

hipertension = input("Hipertensión? (S para Sí, N para No): ")
diabetes = input("Diabetes? (S para Sí, N para No): ​")
cardiaca = input("Enfermedad cardíaca? (S para Sí, N para No): ")
respiratoria = input("Enfermedad respiratoria crónica? (S para Sí, N para No): ")
cancer = input("Cáncer (cualquier tipo)? (S para Sí, N para No): ​")


if edad < 20:
    factor_edad = 0
elif edad < 30:
    factor_edad = -1.458102
elif edad < 40:
    factor_edad = -1.196494
elif edad < 50:
    factor_edad = -0.9109254
elif edad < 60:
    factor_edad = 1.888158
elif edad < 70:
    factor_edad = 2.93897
elif edad < 80:
    factor_edad = 3.774616
else:
    factor_edad = 4.456995

if factor_genero.lower == "m":
    factor_genero = 0
elif factor_genero.lower == "h":
    factor_genero = 0.6176118
else:
    factor_genero = 0

if hipertension.lower() == "s":
    comorbilidad1 = 2.003496
else:
    comorbilidad1 = 0
if diabetes.lower() == "s":
    comorbilidad2 = 2.21035
else:
    comorbilidad2 = 0
if cardiaca.lower() == "s":
    comorbilidad3 = 2.550317
else:
    comorbilidad3 = 0
if respiratoria.lower() == "s":
    comorbilidad4 = 2.036501
else:
    comorbilidad4 = 0
if cancer.lower() == "s":
    comorbilidad5 = 1.925291
else:
    comorbilidad5 = 0


comorbilidad = comorbilidad1 + comorbilidad2 + comorbilidad3 + comorbilidad4 + comorbilidad5

constante = -7.547078
e = 2.71828
riesgo = constante + factor_edad + factor_genero + comorbilidad
probabilidad_muerte = (e ** riesgo)/(1 + (e ** riesgo))

print(f"La probabilidad que mueras de COVID-19, si te contagias, es de {probabilidad_muerte}%")
