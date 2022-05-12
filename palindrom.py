'''
kata = 'isi'
arr = []
isTrue = "True"
for i in range(len(kata)):
    if kata[i] != kata[-1-i]:
        isTrue = "False"
        break
print(isTrue)
'''

def setIsTrue(val):
    return val

def cekKata(kata):
    isTrue = "True"
    for i in range(len(kata)):
        if kata[i] != kata[-1-i]:
            isTrue = setIsTrue("False")
            break
    return isTrue

print(cekKata('basi'))

'''
arr2 = arr[::-1]
kata2 = ('').join(arr2)

if kata == kata2:
    print("True")
else:
    print("False")
'''
