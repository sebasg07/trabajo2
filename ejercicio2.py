def convertir_longitud(valor, unidad_origen, unidad_destino):
    conversiones = {
        ("metros", "kilometros"): valor / 1000,
        ("metros", "centimetros"): valor * 100,
        ("metros", "millas"): valor * 0.000621371,
        ("kilometros", "metros"): valor * 1000,
        ("kilometros", "millas"): valor * 0.621371,
        ("kilometros", "centimetros"): valor * 100000,
        ("millas", "metros"): valor / 0.000621371,
        ("millas", "kilometros"): valor / 0.621371,
        ("millas", "centimetros"): valor / 0.0000062137
    }
    return conversiones.get((unidad_origen, unidad_destino), "No se puede realizar la conversión.")

def convertir_masa(valor, unidad_origen, unidad_destino):
    conversiones = {
        ("kilogramos", "gramos"): valor * 1000,
        ("kilogramos", "libras"): valor * 2.20462,
        ("gramos", "kilogramos"): valor / 1000,
        ("gramos", "libras"): valor * 0.00220462,
        ("libras", "kilogramos"): valor / 2.20462,
        ("libras", "gramos"): valor / 0.00220462
    }
    return conversiones.get((unidad_origen, unidad_destino), "No se puede realizar la conversión.")

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == unidad_destino:
        return valor

    if unidad_origen == "celsius":
        if unidad_destino == "fahrenheit":
            return (valor * 9/5) + 32
        elif unidad_destino == "kelvin":
            return valor + 273.15
    elif unidad_origen == "fahrenheit":
        if unidad_destino == "celsius":
            return (valor - 32) * 5/9
        elif unidad_destino == "kelvin":
            return (valor + 459.67) * 5/9
    elif unidad_origen == "kelvin":
        if unidad_destino == "celsius":
            return valor - 273.15
        elif unidad_destino == "fahrenheit":
            return (valor * 9/5) - 459.67

    return "No se puede realizar la conversión."

def main():
    print("Bienvenido al convertidor de unidades!")
    
    valor_original = float(input("Ingrese el valor a convertir: "))
    unidad_origen = input("Ingrese la unidad de origen: ").lower()
    unidad_destino = input("Ingrese la unidad de destino: ").lower()

    if unidad_origen in ("metros", "kilometros", "centimetros", "millas"):
        resultado = convertir_longitud(valor_original, unidad_origen, unidad_destino)
    elif unidad_origen in ("kilogramos", "gramos", "libras"):
        resultado = convertir_masa(valor_original, unidad_origen, unidad_destino)
    elif unidad_origen in ("celsius", "fahrenheit", "kelvin"):
        resultado = convertir_temperatura(valor_original, unidad_origen, unidad_destino)
    else:
        resultado = "Unidad no reconocida."

    print(f"{valor_original} {unidad_origen} son {resultado} {unidad_destino}")

if __name__ == "__main__":
    main()
