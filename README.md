## Integrantes

* **Juan Pablo Gaviria Franco**
* **Juan Esteban Correa Guzman**

## Descripción del proyecto

La aplicación permite ingresar el precio de un producto, seleccionar la categoría de impuesto correspondiente y calcular el valor del impuesto y el total a pagar.

El sistema también permite agregar el impuesto correspondiente a las bolsas plásticas cuando la compra las incluye.



## Arquitectura del Proyecto
```
calculadora_impuestos/
├── src/
│   ├── model/
│   │   ├── __init__.py
│   │   └── calculadora_impuestos.py     # Lógica de negocio (cálculos y validaciones)
│   └── view/
│       └── console/
│           ├── __init__.py
│           └── consola_calculadora.py   # Interfaz de consola (interacción con el usuario)
├── tests/
│   ├── __init__.py
│   └── test_calculadora.py              # Pruebas unitarias del model
└── doc/
    ├── Casos de prueba calculadora impuestos.xlsx
    └── Entrevista.mp4

```

## Funcionalidades

La aplicación permite trabajar con las siguientes categorías:

* **IVA 19%**
* **IVA 5%**
* **Exento**
* **Excluido**
* **Impuesto Nacional al Consumo (INC)**
* **Impuesto a licores**
* **Impuesto de bolsas plásticas**

## Entradas

1. **Precio del producto**

   * Debe ser un valor numérico.
   * Debe ser mayor que cero.
   * El sistema maneja un límite máximo de precio establecido en el código.

2. **Categoría del impuesto**

   * IVA 19%
   * IVA 5%
   * Exento
   * Excluido
   * Impuesto Nacional al Consumo
   * Impuesto a licores

3. **Bolsas plásticas**

   * El usuario indica si la compra incluye bolsas.
   * Si incluye bolsas, debe ingresar la cantidad.

## Proceso

El funcionamiento general de la aplicación es:

1. El usuario inicia la aplicación.
2. Selecciona la opción para calcular los impuestos.
3. Ingresa el precio del producto.
4. Selecciona la categoría de impuesto.
5. Indica si la compra incluye bolsas plásticas.
6. Si corresponde, ingresa la cantidad de bolsas.
7. El sistema valida los datos ingresados.
8. Se calcula el impuesto correspondiente.
9. Se calcula el impuesto de las bolsas, cuando aplica.
10. Se suman el precio base y los impuestos.
11. El sistema muestra el detalle y el total a pagar.

## Salidas

La aplicación muestra:

* Precio base del producto.
* Nombre del impuesto aplicado.
* Valor del impuesto.
* Valor del impuesto de bolsas plásticas, cuando corresponde.
* **Total a pagar.**

Ejemplo:

```text
========================================
       DETALLE DE LA COMPRA
========================================
Precio base:       $50000.00
IVA 19%:            $9500.00
----------------------------------------
TOTAL A PAGAR:     $59500.00
========================================
```

## Validaciones y manejo de errores

El sistema valida diferentes situaciones para evitar cálculos incorrectos.

Entre ellas:

* Precio vacío.
* Precio con letras o caracteres no numéricos.
* Precio negativo.
* Precio igual a cero.
* Precio superior al límite establecido.
* No seleccionar una categoría de impuesto.
* Seleccionar simultáneamente IVA 5% e IVA 19%.
* Ingresar una cantidad inválida de bolsas.




## Pruebas unitarias

Las pruebas unitarias del proyecto se encuentran en la carpeta `tests/`, específicamente en el archivo:

```text
tests/
├── __init__.py
└── test_calculadora.py
```

El archivo `test_calculadora.py` contiene 10 casos de prueba para verificar el correcto funcionamiento de la calculadora de impuestos.

### Distribución de las pruebas

| Código | Tipo de prueba | Descripción                                           |
| ------ | -------------- | ----------------------------------------------------- |
| CP-01  | Normal         | Cálculo de IVA del 19%                                |
| CP-02  | Normal         | Cálculo del Impuesto Nacional al Consumo (INC) del 8% |
| CP-03  | Normal         | IVA del 19% incluyendo bolsas plásticas               |
| CP-04  | Excepcional    | Cálculo con un precio muy alto                        |
| CP-05  | Excepcional    | Compra sin seleccionar ningún impuesto                |
| CP-06  | Excepcional    | Producto excluido con bolsas plásticas                |
| CP-07  | Error          | Ingreso de un precio negativo                         |
| CP-08  | Error          | Ingreso de letras en el precio                        |
| CP-09  | Error          | Ingreso de un precio vacío                            |
| CP-10  | Error          | Selección simultánea de IVA del 19% e IVA del 5%      |

### ¿Cómo ejecutar las pruebas?

Para ejecutar las pruebas unitarias, primero se debe abrir una terminal ubicada en la carpeta raíz del proyecto:

```text
calculadora_impuestos/
```

Luego se ejecuta el siguiente comando:

```bash
python tests/test_calculadora.py
```

El programa ejecutará automáticamente los 10 casos de prueba y mostrará en consola el resultado de cada uno.

### Resultado esperado

Cuando todas las pruebas funcionan correctamente, se mostrará un resultado similar al siguiente:

```text
============================================================
       PRUEBAS DE LA CALCULADORA DE IMPUESTOS
============================================================

RESULTADO DE CADA CASO
------------------------------------------------------------
CP-01    - IVA 19%                        [PASÓ]
CP-02    - INC 8%                        [PASÓ]
CP-03    - IVA 19% + bolsas             [PASÓ]
CP-04    - Precio muy alto               [PASÓ]
CP-05    - Ningun impuesto               [PASÓ]
CP-06    - Excluido + bolsas             [PASÓ]
CP-07    - Precio negativo               [PASÓ]
CP-08    - Letras en precio              [PASÓ]
CP-09    - Precio vacio                  [PASÓ]
CP-10    - Doble IVA                     [PASÓ]

============================================================
RESULTADO FINAL
============================================================
Pruebas ejecutadas: 10
Pruebas exitosas:   10
Pruebas fallidas:   0
Errores:            0

TODAS LAS PRUEBAS PASARON
============================================================
```

Las pruebas utilizan el módulo `unittest` de Python y permiten comprobar tanto los cálculos correctos como el manejo de situaciones excepcionales y errores de entrada.





## Ejecución de la aplicación por consola

La aplicación cuenta con una interfaz de consola que permite al usuario calcular los impuestos correspondientes a una compra.

El archivo principal de la interfaz se encuentra en:

```text
src/
└── view/
    └── console/
        └── consola_calculadora.py
```

### ¿Cómo ejecutar la aplicación?

Para ejecutar la aplicación, se debe abrir una terminal ubicada en la carpeta raíz del proyecto:

```text
calculadora_impuestos/
```

Luego ejecutar el siguiente comando:

```bash
python src/view/console/consola_calculadora.py
```

### Menú principal

Al iniciar la aplicación se muestra el siguiente menú:

```text
========================================
   CALCULADORA DE IMPUESTOS DE VENTA
========================================
1. Calcular impuestos de una compra
2. Salir
Seleccione una opcion:
```

Las opciones disponibles son:

* **1. Calcular impuestos de una compra:** inicia el proceso para calcular los impuestos de una compra.
* **2. Salir:** finaliza la aplicación.

### Proceso de cálculo

Al seleccionar la opción 1, la aplicación solicita el precio de la compra y posteriormente permite seleccionar el tipo de impuesto que corresponde al producto.

Las categorías disponibles son:

```text
1. IVA 19%
2. IVA 5%
3. Exento
4. Excluido
5. Impuesto Nacional al Consumo (INC)
6. Impuesto a licores
```

Después de seleccionar la categoría, la aplicación pregunta si la compra incluye bolsas plásticas:

```text
¿La compra incluye bolsas plasticas? (s/n):
```

Si la respuesta es `s`, se solicita la cantidad de bolsas incluidas en la compra.

Finalmente, la aplicación calcula y muestra el detalle de los impuestos y el valor total a pagar.

### Ejemplo de ejecución

Un ejemplo de cálculo utilizando un producto de $50.000 con IVA del 19% y sin bolsas plásticas es:

```text
========================================
   CALCULADORA DE IMPUESTOS DE VENTA
========================================
1. Calcular impuestos de una compra
2. Salir
Seleccione una opcion: 1

========================================
      CALCULADORA DE IMPUESTOS
========================================
Ingrese el precio del producto: 50000

Seleccione la categoria del producto:
1. IVA 19%
2. IVA 5%
3. Exento
4. Excluido
5. Impuesto Nacional al Consumo (INC)
6. Impuesto a licores
Seleccione una opcion: 1

¿La compra incluye bolsas plasticas? (s/n): n
```

El sistema realiza el cálculo correspondiente y muestra el detalle de la compra junto con el total a pagar.
