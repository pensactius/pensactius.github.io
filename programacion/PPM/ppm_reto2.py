#!/bin/env python


print('P3')
print('8 8')
print('255')
# fila 1
for x in range(8):
    print('0 255 0', end='  ')
print()

# fila 2 y 3
for i in range(2):
    print('255 255 0  ' + '255 0 0  '*6 + '255 255 0')

# fila 4
print('255 255 0  ' + '70 0 0  '*2 + '255 0 0  '*2 + '70 0 0  '*2 + '255 255 0')

# fila 5 y 6
for i in range(2):
    print('255 255 0  '*3 + '255 0 0  '*2 + '255 255 0  '*3)

# fila 7
print('0 255 0  '*3 + '255 0 0  '*2 + '0 255 0  '*3)

# fila 8
print('0 255 0  '*3 + '70 0 0  '*2 + '0 255 0  '*3)