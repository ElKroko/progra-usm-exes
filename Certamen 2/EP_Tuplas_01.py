def punto_en_recta(p, r):
    m = r[0]
    b = r[1]
    x = p[0]
    y = p[1]

    if y == m * x + b:
        return True
    else:
        return False


def son_paralelas(r1, r2):
    m1 = r1[0]
    b1 = r1[1]
    m2 = r2[0]
    b2 = r2[1]
    if m1 == m2 and b1 != b2:
        return True
    else:
        return False


def recta_que_pasa_por(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    return (m, b)


def punto_de_interseccion(r1, r2):
    if son_paralelas(r1, r2):
        return None
    a = m1 = r1[0]
    b = b1 = r1[1]
    c = m2 = r2[0]
    d = b2 = r2[1]

    x = float(b2 - b1) / float(m1 - m2)
    y = m1 * x + b1

    return (x, y)