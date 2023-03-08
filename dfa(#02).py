# construct a DFA using conditional programming 

# if 0 at q0 , then go to q1 else go to dead end (naming the state q2 here)
# if 0 at q1 then loop at q1 else go to final state q3 and loop for 0,1
# E = {0,1}

def q0(char):
    if (char == '0'):
        dfa = 1
    elif (char == '1'):
        dfa = 2
    else:
        dfa = -1
    return dfa

def q1(char):
    if (char == '0'):
        dfa = 1
    elif (char == '1'):
        dfa = 3
    else:
        dfa = -1
    return dfa

def q2(char):
    if (char == '0' or char == '1'):
        dfa = 2
    else:
        dfa = -1
    return dfa

def q3(char):
    if (char == '0' or char == '1'):
        dfa = 3
    else:
        dfa = -1
    return dfa

def isValid(str):
    str_len = len(str)
    dfa = 0 # starting value
    for x in range(str_len):
        if (dfa == 0):
            dfa = q0(str[x])
        
        elif (dfa == 2):
            dfa = q2(str[x])
        
        elif (dfa == 1):
            dfa = q1(str[x])
        
        elif (dfa == 3):
            dfa = q3(str[x])
        
    if (dfa == 3):
        return 1
    else:
        return 0
    
# main/driver code

string = "01"

if (isValid(string)):
    print("Valid string for the given formal language")
else:
    print("String not valid.")