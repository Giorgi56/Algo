def trifus(lst):
    """Tri fusion avec des listes dans la fonction auxiliaire fus"""
    def fus(lst1, lst2):
        """Fusion récursive de deux listes lst1 et lst2 triées"""
        m, n = len(lst1), len(lst2)
        match (m, n):
            case (0, _):
                return lst2
            case (_, 0):
                return lst1
            case _:
                # On construit récursivement la liste à renvoyer en premant comme premier élément
                # le min entre le premier de lst1 et le premier de lst2 parce que lst1 et lst2 sont triées!
                if lst1[0] < lst2[0]:
                    return [lst1[0]] + fus(lst1[1:], lst2)
                else:
                    return [lst2[0]] + fus(lst1, lst2[1:])
    def aux(p, q):
        """
        Fonction auxiliaire récursive qui sépare les listes et 
        fusionne les sous-listes séparées elles-mêmes aussi
        """
        a = lst[p:q]
        n = len(a)
        match n:
            case 1:
                return a
            case 2:
                [k, r] = a
                return [min(k, r), max(k, r)]
            case _:
                m = (p + q) // 2
                # print(lst[p:m])
                # print(lst[m:q])
                return fus(aux(p, m), aux(m, q))
    return aux(0, len(lst))

print(trifus([5, 7, -1, 6, 10]))
print(trifus([15, -7, 1, 68, -109]))

def trifus2(lst):
    """Tri fusion avec des indices au lieu des listes dans la fonction auxiliaire fus"""
    def fus(lst1, lst2):
        (a, b), (c, d) = lst1, lst2
        m, n = b - a, d - c
        match (m, n):
            case (0, _):
                return lst[c:d]
            case (_, 0):
                return lst[a:b]
            case _:
                if lst[a] < lst[c]:
                    return [lst[a]] + fus((a + 1, b), lst2)
                else:
                    return [lst[c]] + fus(lst1, (c + 1, d))
    def aux(p, q):
        a = lst[p:q]
        n = len(a)
        match n:
            case 1:
                return a
            case 2:
                [k, r] = a
                return [min(k, r), max(k, r)]
            case _:
                m = (p + q) // 2
                # print(lst[p:m])
                # print(lst[m:q])
                return fus(aux(p, m), aux(m, q))
    return aux(0, len(lst))

print(trifus([5, 7, -1, 6, 10]))
print(trifus([15, -7, 1, 68, -109]))
