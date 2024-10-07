def suhu(satuan1, satuan2, nilai):

    if satuan1 == 'c' and satuan2 == 'f':
        return (nilai * 9/5) + 32
    elif satuan1 == 'c' and satuan2 == 'k':
        return (nilai + 273.15)
    elif satuan1 == 'c' and satuan2 == 'r':
        return (nilai * 4/5)