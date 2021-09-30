
from automata.fa.dfa import DFA
import ctypes

class myDFA:
    def __init__(self, pos_string, current_state, prev_state):
        pos_string = []
        type(pos_string)
        current_state = []
        type(current_state)
        prev_state = []
        type(prev_state)

def count(start, transition):
    num_strings = 0
    return num_strings

def possible_strings(alphabet, start, length, dfa):
    #print(start)
    buffer = []
    pos_string = ""
    type(buffer)
    if start == length:
        start = 0
        for i in range(0, len(buffer)):
            pos_string += buffer[i]     
        #print((pos_string))
        return pos_string
    else:
        for i in range(start, length):
            #print("this is the read input for the dfa: ", dfa.read_input(str(start)), '\n')
            append =(dfa.read_input(str(start)))
            buffer.append(append)
            #print(buffer[0])
            #print(i)
            possible_strings(alphabet, start+1, length, dfa)


def main():
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
            initial_state= '0',
            final_states={'a', 'b', 'c', 'd'}
        )
    alphabet = "abcd"
    n = 4
    start = 0
    #print(dfa1.read_input('01231'))
    print_this = possible_strings(alphabet, start, n, dfa1)
    print(print_this)
    #for i in range(0,len(print_this)):
        #print(print_this[i])
    #num_strings = pow(2, n)
    #num_loop = 0

    #for x in range(num_strings):
        #for i in range(n):
            #num_loop+= 1
            #count(start, transition)
            # buffer.append(count())
            #print(buffer)
    #if
    #print(num_loop)


if __name__ == '__main__':
    main()
