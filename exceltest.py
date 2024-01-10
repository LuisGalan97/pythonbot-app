import openpyxl

# Crear un nuevo libro de trabajo (Excel)
libro_trabajo = openpyxl.Workbook()

# Seleccionar la hoja activa (por defecto es la primera hoja)
hoja_activa = libro_trabajo.active

# Añadir contenido a la hoja activa
hoja_activa['A1'] = 'Nombre'
hoja_activa['B1'] = 'Edad'

# Añadir datos
hoja_activa['A2'] = 'Juan'
hoja_activa['B2'] = 25
hoja_activa['A3'] = 'María'
hoja_activa['B3'] = 30

# Guardar el libro de trabajo en un archivo
libro_trabajo.save('archivo_excel.xlsx')
