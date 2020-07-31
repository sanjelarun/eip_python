''' WAP which takee input two strings s and t of bits encoding binary numbers Bs and Bt, respectively
 and returns a new string of bits represeting the number Bs + Bt '''


def cache_table(a, b, c):
    if a == '0' and b == '0' and c == '0':
        return '0', '0'
    elif a == '0' and b == '0' and c == '1':
        return '1', '0'
    elif a == '0' and b == '1' and c == '0':
        return '1', '0'
    elif a == '0' and b == '1' and c == '1':
        return '0', '1'
    elif a == '1' and b == '0' and c == '0':
        return '1', '0'
    elif a == '1' and b == '1' and c == '0':
        return '0', '1'
    elif a == '1' and b == '0' and c == '1':
        return '0', '1'
    else:
        return '1', '1'


def binary_string_add(A, B):
    # Making sure that both string have equal length
    diff = abs(len(A) - len(B))
    if len(A) < len(B):
        for i in range(diff):
            A = "0" + A
    else:
        for i in range(diff):
            B = "0" + B
    c = '0'
    s = ""
    i = len(A) - 1
    while i >= 0:
        tmp, c = cache_table(A[i], B[i], c)
        s = tmp + s
        i -= 1
    if c == '1': s = '1' + s
    return s


print(binary_string_add('111', '11'))
