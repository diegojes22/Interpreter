# Librerias
import os
import sys
import json

interpreter_vars = { # Aqui es donde se guardan las variables del programa
    'defalut_int' : {
        'value' : 0,
        'type' : 'int'
    }
}

# Funciones
def open_json_file(file_path): # Abrir archivo json que contiene el programa
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Programa principal
if __name__ == '__main__':
    json_program = open_json_file('testing_programs/input.json') # abir programa

    step = 'start'

    # ciclo de ejecucion del algoritmo
    while step != 'end':
        # obtener datos del paso actual
        step_data = json_program[step]
        step_type = step_data['type']

        print('<' + step + '>', end=' ')

        # ver el tipo de paso y ejecutarlo
        if step_type == 'START':
            print("Start the program")

        elif step_type == 'EXECUTE':
            print("Execute a command")

            # algunos comandos de la consola se desactivaran por seguridad
            if(step_data['command'] == ''):
                os.system(step_data['command'])

        elif step_type == 'INPUT':
            user_input = input(step_data['message'])

            new_var_reserv = {
                step_data['var'] : {
                    'value' : user_input,
                    'type' : step_data['type_var']
                }
            }

            interpreter_vars.update(new_var_reserv)

        elif step_type == 'OUTPUT':
            print(step_data['message'], interpreter_vars[step_data['var']])

        elif step_type == 'LOOP':
            print("Loop")

        elif step_type == 'ASIGNATION':
            print("Asignation")

            new_var_reserv = {
                step_data['var'] : {
                    'value' : step_data['value'],
                    'type' : step_data['type_var']
                }
            }

            interpreter_vars.update(new_var_reserv)

        elif step_type == 'OPERATION':
            print("operation")

            new_var_reserv = {
                step_data['var'] : {
                    'value' : eval(step_data['ope']),
                    'type' : step_data['type_var']
                }
            }

            interpreter_vars.update(new_var_reserv)

        # instrucciones reservadas para la depuracion en desarrollo
        elif step_type == 'DEBUG':
            print("Debug")

            if step_data['command'] == 'print_all_vars':
                print(interpreter_vars)

        else:
            print("Error: Unknown instruction type")

        step = step_data['next']
