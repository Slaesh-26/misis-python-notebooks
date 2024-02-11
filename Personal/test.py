def get_values_list(filename : str):
    file = open(filename, 'r', encoding = "utf-8")
    values_raw = file.read().split(',')
    values_cast = [float(x) for x in values_raw]
    file.close()
    return values_cast

print(get_values_list("input.csv"))
