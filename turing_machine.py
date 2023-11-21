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
                self.state = transition['nextState']
                if transition['direction'] == 'R': self.position += 1
                else: self.position -= 1
                if self.run():
                    return True
        if self.state in self.acceptance:
            return True
        return False

if __name__ == "__main__":
    transitions = [
        {'currentState': 'q0', 'tapeInput': '0', 'writeTape': '0', 'direction': 'R', 'nextState': 'q0'},
        {'currentState': 'q0', 'tapeInput': '1', 'writeTape': '1', 'direction': 'R', 'nextState': 'q1'},
        {'currentState': 'q1', 'tapeInput': '0', 'writeTape': '0', 'direction': 'R', 'nextState': 'q1'},
        {'currentState': 'q1', 'tapeInput': 'B', 'writeTape': 'B', 'direction': 'R', 'nextState': 'q2'}
    ]

    acceptance = ['q2']

    input_str = str(input('Ingrese una cadena: '))
    turing_machine = TuringMachine(transitions, acceptance)
    turing_machine.tape = [*input_str, 'B']

    result = turing_machine.run()
    if result:
        print(f'La cadena {input_str} sí es aceptada por la máquina')
    else:
        print(f'La cadena {input_str} no es aceptada por la máquina')
