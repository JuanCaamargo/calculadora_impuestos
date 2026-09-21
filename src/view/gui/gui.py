import sys

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

sys.path.append("src")
from model import calculadora_impuestos as calc


IMPUESTOS = {
    "IVA 19%": "iva19",
    "IVA 5%": "iva5",
    "Exento": "exento",
    "Excluido": "excluido",
    "INC 8%": "inc",
    "Licores 25%": "impuesto_licor",
}

COLOR_NORMAL = (1, 1, 1, 1)
COLOR_SELECCIONADO = (0.3, 0.75, 0.35, 1)


class CalculadoraImpuestoApp(App):

    def build(self):
        contenedor = GridLayout(
            cols=2,
            padding=20,
            spacing=10
        )

        contenedor.add_widget(Label(
            text="CALCULADORA DE IMPUESTOS",
            bold=True,
            font_size=22
        ))
        contenedor.add_widget(Label(text=""))

        contenedor.add_widget(Label(text="Precio del producto"))
        self.precio = TextInput(
            hint_text="Ej: 2500000",
            multiline=False
        )
        contenedor.add_widget(self.precio)

        contenedor.add_widget(Label(text="Tipo de impuesto"))

        impuestos = GridLayout(cols=2, spacing=5)
        self.botones_impuesto = {}

        for nombre, clave in IMPUESTOS.items():
            boton = Button(text=nombre)
            boton.bind(
                on_press=lambda _, clave=clave:
                self.seleccionar_impuesto(clave)
            )
            self.botones_impuesto[clave] = boton
            impuestos.add_widget(boton)

        contenedor.add_widget(impuestos)

        contenedor.add_widget(Label(text="Cantidad de bolsas"))
        self.bolsas = TextInput(
            text="0",
            input_filter="int",
            multiline=False
        )
        contenedor.add_widget(self.bolsas)

        calcular = Button(
            text="CALCULAR",
            bold=True
        )
        calcular.bind(on_press=self.calcular_impuesto)
        contenedor.add_widget(calcular)

        self.resultado = Label(
            text="Aquí aparecerá el resultado"
        )
        contenedor.add_widget(self.resultado)

        self.impuesto_seleccionado = None

        return contenedor

    def seleccionar_impuesto(self, clave):
        self.impuesto_seleccionado = clave

        for clave_boton, boton in self.botones_impuesto.items():
            boton.background_color = (
                COLOR_SELECCIONADO
                if clave_boton == clave
                else COLOR_NORMAL
            )

    def calcular_impuesto(self, _):
        try:
            precio = calc.validar_y_convertir_precio(
                self.precio.text
            )
            bolsas = self.validar_bolsas(self.bolsas.text)

            impuesto = {
                self.impuesto_seleccionado: True
            } if self.impuesto_seleccionado else {}

            resultado = calc.calcular_impuestos(
                precio,
                bolsas=bolsas > 0,
                cantidad_bolsas=bolsas,
                **impuesto
            )

            self.mostrar_resultado(resultado)

        except (
            calc.PrecioInvalidoError,
            calc.ImpuestoInvalidoError
        ) as error:
            self.mostrar_error(error)

        except Exception:
            self.mostrar_error(
                ValueError("Ocurrió un error inesperado.")
            )

    @staticmethod
    def validar_bolsas(texto):
        try:
            cantidad = int(texto.strip() or 0)
        except ValueError:
            raise calc.ImpuestoInvalidoError()

        if cantidad < 0:
            raise calc.ImpuestoInvalidoError()

        return cantidad

    def mostrar_resultado(self, resultado):
        self.resultado.text = (
            f"Precio base: ${resultado['precio_base']:,.2f}\n"
            f"Impuesto: {resultado['nombre_impuesto']}\n"
            f"Valor impuesto: ${resultado['valor_impuesto']:,.2f}\n"
            f"Valor bolsas: ${resultado['valor_bolsas']:,.2f}\n"
            f"TOTAL: ${resultado['total']:,.2f}"
        )

    def mostrar_error(self, error):
        mensajes = {
            calc.PrecioInvalidoError:
                "Ingrese un precio numérico mayor que 0.",
            calc.ImpuestoInvalidoError:
                "Seleccione un impuesto y revise la cantidad de bolsas.",
        }

        mensaje = mensajes.get(
            type(error),
            str(error)
        )

        Popup(
            title="Datos inválidos",
            content=Label(text=mensaje),
            size_hint=(0.8, 0.3)
        ).open()


if __name__ == "__main__":
    CalculadoraImpuestoApp().run()