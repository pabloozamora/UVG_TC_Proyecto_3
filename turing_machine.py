import json

class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, initial_state, acceptance, transitions, tape):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.state = initial_state
        self.acceptance = acceptance
        self.transitions = transitions
        self.position = 0
        self.tape = tape

    def run(self):
        for transition in self.transitions:
            if self.state == transition['currentState'] and self.tape[self.position] == transition['tapeInput']:
                self.tape[self.position] = transition['writeTape']
                derivation = ''
                for index, element in enumerate(self.tape):
                    if index == self.position:
                        derivation += '\033[94m' + element + '\033[0m'
                    else:
                        derivation += element
                print(derivation)
                self.state = transition['nextState']
                if transition['direction'] == 'R': self.position += 1
                else: self.position -= 1
                if self.run():
                    return True
        if self.state in self.acceptance:
            return True
        return False

if __name__ == "__main__":
    
    # Obtener componentes para la máquina
    
    with open('substraction.json') as json_file:
        data = json.load(json_file)
        states = data["states"]
        input_alphabet = data["inputAlphabet"]
        tape_alphabet = data["tapeAlphabet"]
        initial_state = data["initialState"]
        acceptance = data["acceptance"]
        transitions = data["transitions"]

    # Obtener input
    
    w = str(input('\nIngrese una cadena: '))
    turing_machine = TuringMachine(states, input_alphabet, tape_alphabet, initial_state, acceptance, transitions, [*w, 'B'])
    
    # Verificar cadena

    print('\nDerivación:\n')
    result = turing_machine.run()
    print(f'\nEstado final: {turing_machine.state}')
    print(f'Cadena en la cinta: {turing_machine.tape}')
    if result:
        print(f'\nLa cadena {w} sí es aceptada por la máquina\n')
    else:
        print(f'\nLa cadena {w} no es aceptada por la máquina\n')
