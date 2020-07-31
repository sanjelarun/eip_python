''' WAP which takee input two strings s and t of bits encoding binary numbers Bs and Bt, respectively
 and returns a new string of bits represeting the number Bs + Bt '''
def binary_string_add(A, B):
    # Making sure that both string have equal length
    diff = abs(len(A) - len(B))
    if len(A) < len(B):
        for i in range(diff):
            A = "0" + A
    else:
        for i in range(diff):
            B = "0" + B
    carry = 0
    s = ""
    i = len(A) - 1
    while i >= 0:
        tmp = int(A[i]) +int(B[i]) + carry
        if tmp == 2:
            s  = "0" + s
            carry = 1
        elif tmp == 3:
            s = "1" + s
            carry = 1
        else:
            s = str(tmp) + s
        i -= 1  
    return  "1" + s if carry == 1 else s

print(binary_string_add('11111', '1'))