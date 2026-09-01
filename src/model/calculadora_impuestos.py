TARIFA_IVA_GENERAL = 0.19
TARIFA_IVA_REDUCIDO = 0.05
TARIFA_INC = 0.08
TARIFA_LICOR = 0.25

VALOR_BOLSA = 73

PRECIO_MINIMO = 1
PRECIO_MAXIMO = 1_000_000_000


class PrecioInvalidoError(Exception):
    "Excepción que se dispara cuando el precio ingresado no es válido"

    def __init__(self):
        super().__init__("El precio ingresado no es válido")


class ImpuestoInvalidoError(Exception):
    "Excepción que se dispara cuando la selección del impuesto no es válida"

    def __init__(self):
        super().__init__("La selección de impuestos no es válida")


def validar_y_convertir_precio(texto):
    """
    Valida el precio ingresado y lo convierte a un valor numérico.
    """
    if texto is None or texto.strip() == "":
        raise PrecioInvalidoError()

    texto_limpio = texto.strip().replace(",", "")

    try:
        precio = float(texto_limpio)
    except ValueError:
        raise PrecioInvalidoError()

    if precio <= 0:
        raise PrecioInvalidoError()

    if precio < PRECIO_MINIMO or precio > PRECIO_MAXIMO:
        raise PrecioInvalidoError()

    return precio


def calcular_impuestos(
    precio,
    iva19=False,
    iva5=False,
    exento=False,
    excluido=False,
    inc=False,
    impuesto_licor=False,
    bolsas=False,
    cantidad_bolsas=0
):
    if iva19 and iva5:
        raise ImpuestoInvalidoError()

    cantidad_seleccionados = 0

    for opcion in (
        iva19,
        iva5,
        exento,
        excluido,
        inc,
        impuesto_licor
    ):
        if opcion:
            cantidad_seleccionados += 1

    if cantidad_seleccionados == 0:
        raise ImpuestoInvalidoError()

    if cantidad_seleccionados > 1:
        raise ImpuestoInvalidoError()

    if iva19:
        nombre_impuesto = "IVA 19%"
        valor_impuesto = precio * TARIFA_IVA_GENERAL

    elif iva5:
        nombre_impuesto = "IVA 5%"
        valor_impuesto = precio * TARIFA_IVA_REDUCIDO

    elif inc:
        nombre_impuesto = "Impuesto Nacional al Consumo"
        valor_impuesto = precio * TARIFA_INC

    elif impuesto_licor:
        nombre_impuesto = "Impuesto a licores"
        valor_impuesto = precio * TARIFA_LICOR

    elif exento:
        nombre_impuesto = "Exento"
        valor_impuesto = 0.0

    else:
        nombre_impuesto = "Excluido"
        valor_impuesto = 0.0

    valor_bolsas = 0.0

    if bolsas:
        if cantidad_bolsas <= 0:
            raise ImpuestoInvalidoError()

        valor_bolsas = cantidad_bolsas * VALOR_BOLSA

    total = precio + valor_impuesto + valor_bolsas

    resultado = {
        "precio_base": precio,
        "nombre_impuesto": nombre_impuesto,
        "valor_impuesto": valor_impuesto,
        "valor_bolsas": valor_bolsas,
        "total": total
    }

    return resultado