
from automata.fa.dfa import DFA
import ctypes
def count(start, transition):
    dfa1 = DFA(
        states={'0', 'a', 'b', 'c', 'd'},
        input_symbols={'0', '1', '2', '3'},
        transitions={
            '0': {'0': 'a', '1': 'b', '2': 'c', '3': 'd'},
            'a': {'0': 'a', '1': 'b', '2': 'c', '3': 'd'},
            'b': {'0': 'a', '1': 'b', '2': 'c', '3': 'd'},
            'c': {'0': 'a', '1': 'b', '2': 'c', '3': 'd'},
            'd': {'0': 'a', '1': 'b', '2': 'c', '3': 'd'}
        },
        initial_state= start,
        final_states={'a', 'b', 'c', 'd'}
    )

    final_state = DFA.read_input(dfa1, transition)
    return final_state



def main():
    n = 6
    num_loop = 0
    buffer = []
    type(buffer)
    for x in range(n):
        for i in range(3):
            for t in range(3):
                num_loop+= 1
                #count(i, t)
                #buffer.append(count())
                #print(buffer)
    #if
    print(num_loop)


if __name__ == '__main__':
    main()
