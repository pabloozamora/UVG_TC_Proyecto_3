class TuringMachine:
    def __init__(self, transitions, acceptance):
        self.transitions = transitions
        self.acceptance = acceptance
        self.state = 'q0'
        self.position = 0
        self.tape = []

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
    
    '''transitions = [
        {'currentState': 'q0', 'tapeInput': '0', 'writeTape': '0', 'direction': 'R', 'nextState': 'q0'},
        {'currentState': 'q0', 'tapeInput': '1', 'writeTape': '1', 'direction': 'R', 'nextState': 'q1'},
        {'currentState': 'q1', 'tapeInput': '0', 'writeTape': '0', 'direction': 'R', 'nextState': 'q1'},
        {'currentState': 'q1', 'tapeInput': 'B', 'writeTape': 'B', 'direction': 'R', 'nextState': 'q2'}
    ]'''
    
    transitions = [
        {'currentState': 'q0', 'tapeInput': '1', 'writeTape': '1', 'direction': 'R', 'nextState': 'q0'},
        {'currentState': 'q0', 'tapeInput': '-', 'writeTape': '-', 'direction': 'R', 'nextState': 'q1'},
        {'currentState': 'q1', 'tapeInput': '1', 'writeTape': 'X', 'direction': 'L', 'nextState': 'q1'},
        {'currentState': 'q1', 'tapeInput': '-', 'writeTape': '-', 'direction': 'L', 'nextState': 'q2'},
        {'currentState': 'q1', 'tapeInput': 'X', 'writeTape': 'X', 'direction': 'L', 'nextState': 'q1'},
        {'currentState': 'q1', 'tapeInput': 'B', 'writeTape': 'B', 'direction': 'L', 'nextState': 'q4'},
        {'currentState': 'q2', 'tapeInput': '1', 'writeTape': 'X', 'direction': 'R', 'nextState': 'q3'},
        {'currentState': 'q2', 'tapeInput': 'X', 'writeTape': 'X', 'direction': 'L', 'nextState': 'q2'},
        {'currentState': 'q3', 'tapeInput': '1', 'writeTape': 'X', 'direction': 'L', 'nextState': 'q1'},
        {'currentState': 'q3', 'tapeInput': '-', 'writeTape': '-', 'direction': 'R', 'nextState': 'q3'},
        {'currentState': 'q3', 'tapeInput': 'X', 'writeTape': 'X', 'direction': 'R', 'nextState': 'q3'},
        {'currentState': 'q3', 'tapeInput': 'B', 'writeTape': 'B', 'direction': 'L', 'nextState': 'q4'},
        {'currentState': 'q4', 'tapeInput': '1', 'writeTape': '1', 'direction': 'R', 'nextState': 'q4'},
        {'currentState': 'q4', 'tapeInput': '-', 'writeTape': 'B', 'direction': 'L', 'nextState': 'q4'},
        {'currentState': 'q4', 'tapeInput': 'X', 'writeTape': 'B', 'direction': 'L', 'nextState': 'q4'},
        {'currentState': 'q4', 'tapeInput': 'B', 'writeTape': 'B', 'direction': 'R', 'nextState': 'q5'},
    ]

    acceptance = ['q5']

    input_str = str(input('\nIngrese una cadena: '))
    turing_machine = TuringMachine(transitions, acceptance)
    turing_machine.tape = [*input_str, 'B']

    print('\nDerivación:\n')
    result = turing_machine.run()
    print(f'\nEstado final: {turing_machine.state}')
    print(f'Estado final de la cinta: {turing_machine.tape}')
    if result:
        print(f'\nLa cadena {input_str} sí es aceptada por la máquina\n')
    else:
        print(f'\nLa cadena {input_str} no es aceptada por la máquina\n')
