# Kiu System

Ejercicio de compañía aérea.
- Hice reporte detallado por consola, con fake data preparada de paquetes.
- Hice que se agregaran paquetes para despachar uno por uno para casos de unit testing.

## Uso

Correr los tests desde el root

```bash
py.test -q
```

## Reporte detallado por consola
Fechas a elegir
- 2024-02-25
- 2024-01-11
```python
python main.py report_by_date '2024-02-25'
```

```python
Code:  UYTK789
Date:  2024-02-25
Client Name:  David Houton
Client Passport Number:  AA67789
Origin:  Buenos Aires
Destination:  Bogotá
Description:  heavy
----------------------

Code:  UYTK790
Date:  2024-02-25
Client Name:  David Houton
Client Passport Number:  AA67789
Origin:  Buenos Aires
Destination:  Bogotá
Description:  heavy
----------------------

Code:  UYTK791
Date:  2024-02-25
Client Name:  David Houton
Client Passport Number:  AA67789
Origin:  Buenos Aires
Destination:  Bogotá
Description:  heavy
----------------------

NUMBER OF PACKAGES:  3

TOTAL RAISED:  30
```