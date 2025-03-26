
def hammingWeight(n):
    c = str(bin(n)).replace("0b","")
    count = 0
    for i in c: 
        if i == '1': 
            count+=1
    return count


def hammingWeight2(n): 
    return bin(n).count('1')

print(hammingWeight2(11))