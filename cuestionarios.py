def test(mat):
    fils = len(mat)
    cols = len(mat[0])
    for k in range(cols):
        ac = 0
        for g in range(fils):
            ac += mat[k][g]
        p = ac / fils
        print('Indice:', k, '- Promedio:', p)