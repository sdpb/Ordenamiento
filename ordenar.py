import sys

sys.setrecursionlimit(15000)


# ===[BUBBLE SORT]===============================================

def bubble_sort(datos, campo, ascendente):
    for nCiclo in range(len(datos) - 1, 0, -1):
        for i in range(nCiclo):
            if campo == "nombre" and ascendente:
                if datos[i].nombre > datos[i + 1].nombre:
                    temp = datos[i]
                    datos[i] = datos[i + 1]
                    datos[i + 1] = temp
            else:
                if datos[i].nombre < datos[i + 1].nombre:
                    temp = datos[i]
                    datos[i] = datos[i + 1]
                    datos[i + 1] = temp

            if campo == "edad" and ascendente:
                if int(datos[i].edad) > int(datos[i + 1].edad):
                    temp = datos[i]
                    datos[i] = datos[i + 1]
                    datos[i + 1] = temp
            else:
                if int(datos[i].edad) < int(datos[i + 1].edad):
                    temp = datos[i]
                    datos[i] = datos[i + 1]
                    datos[i + 1] = temp
    return datos


# ===[MERGE SORT]===============================================

def merge_sort(datos, campo, asc):
    if len(datos) <= 1:
        return datos

    mitad = len(datos) // 2

    return merge(merge_sort(datos[:mitad], campo, asc),
                 merge_sort(datos[mitad:], campo, asc),
                 campo, asc)


def merge(datosIzq, datosDer, campo, asc):
    pos1 = pos2 = 0
    datosOut = []

    while pos1 < len(datosIzq) and pos2 < len(datosDer):
        if campo == "nombre":
            if asc:
                if datosIzq[pos1].nombre < datosDer[pos2].nombre:
                    datosOut.append(datosIzq[pos1])
                    pos1 += 1
                else:
                    datosOut.append(datosDer[pos2])
                    pos2 += 1
            else:
                if datosIzq[pos1].nombre > datosDer[pos2].nombre:
                    datosOut.append(datosIzq[pos1])
                    pos1 += 1
                else:
                    datosOut.append(datosDer[pos2])
                    pos2 += 1

        if campo == "edad":
            if asc:
                if int(datosIzq[pos1].edad) < int(datosDer[pos2].edad):
                    datosOut.append(datosIzq[pos1])
                    pos1 += 1
                else:
                    datosOut.append(datosDer[pos2])
                    pos2 += 1
            else:
                if int(datosIzq[pos1].edad) > int(datosDer[pos2].edad):
                    datosOut.append(datosIzq[pos1])
                    pos1 += 1
                else:
                    datosOut.append(datosDer[pos2])
                    pos2 += 1

    datosOut += datosIzq[pos1:] + datosDer[pos2:]
    return datosOut


def partition(array, start, end):
    pivot = array[start].edad
    low = start + 1
    high = end

    while True:
        while low <= high and array[high].edad >= pivot:
            high = high - 1
        while low <= high and array[low].edad <= pivot:
            low = low + 1
        if low <= high:
            array[low].edad, array[high].edad = array[high].edad, array[low].edad
        else:
            break
    array[start].edad, array[high].edad = array[high].edad, array[start].edad
    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)

    return array


def quick_sort_2(data, criteria, ascendant):
    if len(data) <= 1:
        return data
    pivot_C = data[len(data) // 2]
    if criteria == "edad":
        dataLeft = [_ for _ in data if _.edad < pivot_C.edad]
        dataMiddle = [_ for _ in data if _.edad == pivot_C.edad]
        dataRight = [_ for _ in data if _.edad > pivot_C.edad]

    elif criteria == "nombre":
        dataLeft = [_ for _ in data if _.nombre < pivot_C.nombre]
        dataMiddle = [_ for _ in data if _.nombre == pivot_C.nombre]
        dataRight = [_ for _ in data if _.nombre > pivot_C.nombre]
    else:
        return []
    return quick_sort_2(dataLeft, criteria, ascendant) + dataMiddle + quick_sort_2(dataRight, criteria, ascendant)
