from automata.fa.dfa import DFA
from itertools import permutations, product
import ctypes


class myDFA:
    def __init__(self, pos_string, current_state, prev_state):
        pos_string = []
        type(pos_string)
        current_state = []
        type(current_state)
        prev_state = []
        type(prev_state)


def count(los):
    for i in range(len(los)):
        
    return count()


def possible_strings(alphabet, length, dfa, strings):
    inc = 0

    pos_string = ""
    '''
    if start < length:
        # for j in range(length):
        j = 0
        for j in range(length):
            if start < 4:
                pos_string += dfa.read_input(str(start))
                start += 1
                if start >= 4:
                    num = 0
                    while num < 4 and len(pos_string) < length:
                        pos_string += dfa.read_input(str(num))
                        num += 1
        perm = list(permutations(pos_string))
        print(perm)
        print(len(perm))'''
    for i in range(len(alphabet)):
        pos_string += dfa.read_input(str(i))
    for _set in product(list(pos_string), repeat=length):
        inc+=1
        strings.append((''.join(_set)))

    print(inc)
    return strings


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
        initial_state='0',
        final_states={'a', 'b', 'c', 'd'}
    )
    #dfa_check= myDFA()
    alphabet = "abcd"
    n = 6
    strings = []
    type(strings)
    los = possible_strings(alphabet, n, dfa1, strings)
    #print(print_this)
    #for i in range(0,len(los)):
    #    print(los[i])
    #print(len(los))
    # num_strings = pow(2, n)
    # num_loop = 0

    # for x in range(num_strings):
    # for i in range(n):
    # num_loop+= 1
    count(los)
    # buffer.append(count())
    # print(buffer)
    # if
    # print(num_loop)


if __name__ == '__main__':
    main()
