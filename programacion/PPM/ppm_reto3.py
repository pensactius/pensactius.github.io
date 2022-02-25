marciano = """
.X....X.
..XXXX..
.X.XX.X.
.XXXXXX.
.X....X.
.XXXXXX.
..X..X..
.X....X.
"""

print('P3')
print('8 8')
print('255')

l = marciano.split()
for row in l:
    row_data = ['0 0 0  ' if c=='.' else '200 200 200  ' for c in row]
    print(''.join(row_data))