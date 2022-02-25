# Gameboy Palette (fondo, oscuro..claro)
gb_palette = [(255, 252, 173), (15, 56, 15), (48, 98, 48), (139, 172, 15)]

def ppmBegin(size):
    w, h = size
    cabecera = f"""P3
{w} {h}
255"""
    print(cabecera, end='')

    
spr_mario = """
0001110000
0011111110
0111331300
1131133330
1133331130
0033333300
0112112000
1112112110
3310220113
3322222233
0011001100
0111001110
"""
ppmBegin((10, 12))

for pixel in spr_mario:
    if pixel in "01234":
        palette_index = int(pixel)
        r, g, b = gb_palette[int(pixel)]
        print(f'{r} {g} {b}  ', end='')
    if pixel == '\n':
        print()
        