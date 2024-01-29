import urllib.request
import json

def obtener_tipos_de_cambio(api_key, base_currency):
    url = f'https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}'

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data['rates']
    except urllib.error.HTTPError as e:
        print(f'Error al obtener tipos de cambio: {e.code}')
        return None

def convertir_moneda(cantidad, tasa_de_cambio):
    return cantidad * tasa_de_cambio

def main():
    
    api_key = 'TU_API_KEY'
    base_currency = input('Ingrese la moneda base (ejemplo: USD): ').upper()
    cantidad = float(input('Ingrese la cantidad a convertir: '))
    currency_to_convert = input('Ingrese la moneda a la que desea convertir (ejemplo: EUR): ').upper()

    tipos_de_cambio = obtener_tipos_de_cambio(api_key, base_currency)

    if tipos_de_cambio:
        if currency_to_convert in tipos_de_cambio:
            tasa_de_cambio = tipos_de_cambio[currency_to_convert]
            resultado = convertir_moneda(cantidad, tasa_de_cambio)
            print(f'{cantidad} {base_currency} equivale a {resultado} {currency_to_convert}')
        else:
            print(f'La moneda "{currency_to_convert}" no está disponible en la API.')
    else:
        print('No se pudo obtener información sobre los tipos de cambio.')

if __name__ == "__main__":
    main()