import json
import os

class Engine():
    #__ Constructor __#
    def __init__(self, path):
        self._program_data = None
        self.step = 'start'
        self.step_data = None
        self.step_type = None

        # Estructuras de datos nesesarias para el interprete
        # Tipos de pasos
        self.step_types = [
            "START",            # declara el inicio del programa
            "END",              # declara el final del programa
            "EXECUTE",          # ejecuta un comando de la terminal
            "INPUT",            # pide un dato al usuario
            "OUTPUT",           # muestra un dato al usuario como una variable o texto
            "CONDITONAL",       # ejecuta un condicion
            "OPERATION",        # ejecuta una operacion
            "ASIGNATION",       # asigna un valor a una variable (este paso esta en revision para ser remplazado por OPERATION)
            "LOOP",             # ejecuta un ciclo (sin terminar)
            "DEBUG"             # este le da mensajes al programador del interprete
        ]

        # Variables del interprete durante la ejecucion
        self.interpreter_vars = {
            'defalut_int' : {
                'value' : 0,
                'type' : 'int'
            },
            'easter_egg' : {
                'value' : 'Hola, me alegro que hayas descubierto este mensaje, solo quiero decir que no supe que poner en este texto asi que solo puse esto :D',
                'type' : 'str'
            }
        }

        self._open_file(path)


    #__ Metodos __#
    def _open_file(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            self._program_data = json.load(f)

    def _eval_steps(self):
        # ver el tipo de paso y ejecutarlo
        if self.step_type == 'START':
            print("Start the program")

        elif self.step_type == 'EXECUTE':
            print("Execute a command")

            # algunos comandos de la consola se desactivaran por seguridad
            if(self.step_data['command'] == ''):
                os.system(self.step_data['command'])

        elif self.step_type == 'INPUT':
            user_input = input(self.step_data['message'])

            new_var_reserv = {
                self.step_data['var'] : {
                    'value' : user_input,
                    'type' : self.step_data['type_var']
                }
            }

            self.interpreter_vars.update(new_var_reserv)

        elif self.step_type == 'OUTPUT':
            print(self.step_data['message'])

        elif self.step_type == 'LOOP':
            print("Loop")

        elif self.step_type == 'ASIGNATION':
            print("Asignation")

            new_var_reserv = {
                self.step_data['var'] : {
                    'value' : self.step_data['value'],
                    'type' : self.step_data['type_var']
                }
            }

            self.interpreter_vars.update(new_var_reserv)

        elif self.step_type == 'OPERATION':
            print("operation")

            new_var_reserv = {
                self.step_data['var'] : {
                    'value' : eval(self.step_data['ope']),
                    'type' : self.step_data['type_var']
                }
            }

            self.interpreter_vars.update(new_var_reserv)

        # instrucciones reservadas para la depuracion en desarrollo
        elif self.step_type == 'DEBUG':
            print("Debug")

            if self.step_data['command'] == 'print_all_vars':
                print(self.interpreter_vars)

        else:
            print("Error: Unknown instruction type")

        self.step = self.step_data['next']

    def run(self):
        while self.step != 'end':
            self.step_data = self._program_data[self.step]
            self.step_type = self.step_data['type']

            print('<' + self.step + '>', end=' ')

            self._eval_steps()

# Ejecucion de prueva
if __name__ == '__main__':
    engine = Engine('testing_programs/instructions.json')
    engine.run()

    