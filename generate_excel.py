from openpyxl import Workbook

# Crear un nuevo libro de Excel
wb = Workbook()

# Activar la primera hoja
ws1 = wb.active
ws1.title = "Plan de pruebas"

# Encabezados
headers = ["ID", "Módulo", "Caso de prueba", "Entrada", "Resultado Esperado", "Prioridad", "Tipo de prueba", "Estado"]
ws1.append(headers)

# Casos de prueba
test_cases = [
    ["TC01", "Login", "Login exitoso", "Usuario válido + contraseña válida", "You logged into a secure area!", "Alta", "Funcional", "Aprobado"],
    ["TC02", "Login", "Login fallido (usuario incorrecto)", "Usuario inválido + contraseña válida", "Your username is invalid!", "Alta", "Funcional negativa", "Aprobado"],
    ["TC03", "Login", "Campo usuario vacío", '"" + contraseña válida', "Your username is invalid!", "Media", "Funcional negativa", "No ejecutado"],
    ["TC04", "Login", "Campo contraseña vacía", "Usuario válido + \"\"", "Your password is invalid!", "Media", "Funcional negativa", "No ejecutado"]
]

# Agregamos los datos
for case in test_cases:
    ws1.append(case)

# Guardar el archivo
wb.save("QA_Report.xlsx")

print("✅ Archivo QA_Report.xlsx creado con la hoja 'Plan de pruebas'")
