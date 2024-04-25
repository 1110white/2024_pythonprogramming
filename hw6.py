
for i in range (1, 10):
    for j in range (2, 6):
        a = '\n' if(j == 5) else '\t'
        print(f'{j} x {i} = {j*i:2d}', end = a)
        j += 1
    i += 1

print('\n')

for i in range (1, 10):
    for j in range (6, 10):
        a = '\n' if(j == 9) else '\t'
        print(f'{j} x {i} = {j*i:2d}', end = a)
        j += 1
    i += 1
    

    
