import random
import time
import math

print()
print("Este juego consiste en realizar una serie de mini-juegos en el menor tiempo posible.\n"
      "Cuando el juego termine tu puntaje final (de acuerdo a los errores y al tiempo \n"
      "que te demoraste) será comparado con los resultados globales.\n")

# Global time
global_time = 0

# Global score
global_score = 0

# Para "Noción del Tiempo"

enunciado_noc_tiemp = ('Pulse una vez enter y cuando crea que hallan pasado exactamente\n'
                       '15 segundos vuelva a pulsar enter: ')

# Para "Operación matemática"
enunciado_op_math = ('A continuación se mostraran 5 operaciones matematicas en pantalla\n'
                     'que tendrá que realizar (una por una). Pulse enter para empezar: ')

# Para "Tiempo de reacción"
enunciado_tiemp_reac = ('Cuando aparezca un mensaje apreta enter lo más rapido posible\n'
                        '(para comenzar pulsa ENTER):')

# Para "Pregunta"
preguntas = ['¿Quién escribió La Odisea?', '¿Cuál es el río más largo del mundo?',
             '¿Cómo se llama la Reina del Reino Unido? (solo primer nombre)',
             '¿Cuándo acabó la II Guerra Mundial(año)?',
             '¿Cómo se denomina el resultado de la multiplicación?']
respuestas = ['homero', 'amazonas', 'isabel', '1945', 'producto']

lista = ['Operación Matemática', 'Tiempo de Reacción', 'Preguntas', 'Noción del Tiempo']
lista_random = []
cycles = len(lista)
for game in range(cycles):
    j = random.choice(lista)
    lista_random.append(j)
    lista.remove(j)


for game in lista_random:

    if game == 'Operación Matemática':
        print()
        input(enunciado_op_math)

        for i in range(5):

            suma = random.randrange(1, 100)
            suma_1 = random.randrange(1, 100)
            mult = random.randrange(1, 10)
            mult_1 = random.randrange(1, 10)

            type_operation = random.choice(['*', '+'])

            if type_operation == '+':
                correct = suma + suma_1
                print(f'{suma} mas {suma_1}')
                time_1 = time.time()
                answer = int(input("= "))

                if correct == answer:
                    print('BIEEEN!!!')
                    time_2 = time.time() - time_1
                    score = round(4000 / time_2)
                    print(f'sumas {score} puntos.')
                    global_score += score
                else:
                    score = -300
                    print(f'Respuesta incorrecta, se quitan {-score} puntos.')
                    global_score += score

            elif type_operation == '*':
                correct = mult * mult_1
                print(f'{mult} por {mult_1}')
                time_1 = time.time()
                answer = int(input("= "))

                if correct == answer:
                    print('BIEEEN!!!')
                    time_2 = time.time() - time_1
                    score = round(4000 / time_2)
                    print(f'sumas {score} puntos.')
                    global_score += score
                else:
                    score = -300
                    print(f'Respuesta incorrecta, se quitan {-score} puntos.')
                    global_score += score

    if game == 'Tiempo de Reacción':
        print()
        input(enunciado_tiemp_reac)
        time.sleep(random.randrange(4, 13))
        print("YA!!!!")
        time_1 = time.time()
        input('')
        time_2 = time.time() - time_1
        score = 10000 / (time_2 * 2)
        print(f'Has conseguído {score} puntos y tu tiempo fue de {time_2} segundos')
        global_score += score

    if game == 'Noción del Tiempo':
        print()
        input(enunciado_noc_tiemp)
        time_1 = time.time()
        input()
        time_2 = time.time() - time_1
        difference = abs(time_2 - 15)  # Valor absoluto de la diferencia entre 15 segundos y el tiempo marcado por la persona
        if difference < 0.3:
            score = 10000
        elif difference > 0.3:
            score = round(10000 / (difference + 0.7))
        print(f'Has sumado {score} puntos con un tiempo de {time_2}')
        global_score += score

    if game == 'Preguntas':
        for i in range(2):
            a = random.choice(preguntas)
            time_1 = time.time()
            answer = input(f'{a}\n')
            answer = answer.lower()
            time_2 = time.time() - time_1
            correct_answer = respuestas[preguntas.index(a)]
            print(time_2)

            if answer == correct_answer:  # Acordarse de considerar tiempo y respuesta correcta o incorrecta en el puntaje
                print('Correcto!!')
            else:
                print('Incorrecto, se restan puntos en el marcador')
print(global_score)
