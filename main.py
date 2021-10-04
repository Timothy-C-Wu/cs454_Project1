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
    buffer = []
    type(buffer)
    valid_count = 0
    isa = isb = isc = isd = False
    for i in range(len(los)):
        #print(len(los[i]))
        if len(los[i]) > 6:
            begin = 0
            end = 6
            #print("not here")
            while end <= len(los[i]):
                if 'a' not in los[i] and 'b' not in los[i] and 'c' not in los[i] and 'd' not in los[i] in los[i]:
                    continue
                    begin += 1
                    end += 1
                else:
                    valid_count+=1
                    begin+=1
                    end+=1
                #print(end)
        else:
            if 'a' in los[i] and 'b' in los[i] and 'c' in los[i] and 'd' in los[i]:
                valid_count+= 1
                #print(los[i])
    return valid_count


def possible_strings(alphabet, length, dfa, strings):
    inc = 0
    pos_string = ""
    '''if start < length:
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

    #print(inc)
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
    n = 12
    strings = []
    type(strings)
    los = possible_strings(alphabet, n, dfa1, strings)
    is_valid = count(los)
    print(is_valid)


if __name__ == '__main__':
    main()