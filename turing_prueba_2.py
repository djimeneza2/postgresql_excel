def isValid(s:str)->bool:

    result = None 

    valid_strings = ["(",")","[","]","{","}"]

    input_string=s.strip().split()

    if len(input_string)%2 != 0:
        result = 0
    else:
        j=0
        for i in input_string:
            if i in valid_strings:
                if i=="(":
                    m=1
                elif i="[":
                    m=2
                elif i="{":
                    m=3
        else:
            result=0
            break

    return result

if __name__ == "__main__":
    line=input()
    if isValid(line):
        print("valid")
    else:
        print("invalid")