def DFA(transitions,initial,accepting,string):
    state = initial
    try:
        for c in string:
            state = transitions[state][c]
        return state in accepting
    except KeyError:
        print("Cadena no aceptada")

def main():
    table = {
        1 : {'r': [2,5], 'b': 6},
        2 : {'r': [5,7], 'b': [1,3,6]},
        3 : {'r': [2,7,7], 'b': [6,8]},
        4 : {'r': 7, 'b': [3,8]},
        5 : {'r': [2,10], 'b': [1,6,9]},
        6 : {'r': [2,5,7,10], 'b': [1,3,9,11]},
        7 : {'r': [2,4,10,12], 'b': [3,6,8,11]},
        8 : {'r': [4,7,12], 'b': [3,1]},
        9 : {'r': [5,10,13], 'b': [14,6]},
        10 : {'r': [5,7,13,15], 'b': [6,9,11,14]},
        11 : {'r': [7,10,12,15], 'b': [6,8,14,16]},
        12 : {'r': [7,15], 'b': [8,11,16]},
        13 : {'r': 10, 'b': [9,14]},
        14 : {'r': [10,13,15], 'b': [9,11]},
        15 : {'r': [10,12], 'b': [11,14,16]},
        16 : {'r': [12,15], 'b': 11}
    }
    
    instructions = input("Introduce las lineas de comando: ")
    DFA(table,1,{16},instructions)
    
if __name__ == "__main__":
    while True:
        main()