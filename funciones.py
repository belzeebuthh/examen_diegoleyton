def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Debe seleccionar una opción válida")
            continue
 
        if opcion >= 1 and opcion <= 6:
            return opcion
        else:
            print("Debe seleccionar una opción válida")
 
 
def buscar_codigo(codigo, planes):
    for clave in planes:
        if clave.lower() == codigo.lower():
            return True
    return False
 
 
def cupos_tipo(tipo, planes, inscripciones):
    total = 0
    for codigo in planes:
        info = planes[codigo]
        tipo_plan = info[1]
        if tipo_plan.lower() == tipo.lower():
            total = total + inscripciones[codigo][1]
 
    print("Total de cupos disponibles para el tipo", tipo, "es:", total)
 
 
def busqueda_precio(p_min, p_max, planes, inscripciones):
    lista_resultados = []
 
    for codigo in inscripciones:
        precio_actual = inscripciones[codigo][0]
        cupos_actual = inscripciones[codigo][1]
 
        if precio_actual >= p_min and precio_actual <= p_max and cupos_actual != 0:
            nombre = planes[codigo][0]
            lista_resultados.append(nombre + "--" + codigo)
 
    if len(lista_resultados) == 0:
        print("No hay planes en ese rango de precios.")
        return
 
    lista_resultados.sort()
    for elemento in lista_resultados:
        print(elemento)
 
 
def actualizar_precio(codigo, nuevo_precio, planes, inscripciones):
    existe = buscar_codigo(codigo, planes)
    if existe == False:
        return False
 
    for clave in inscripciones:
        if clave.lower() == codigo.lower():
            inscripciones[clave][0] = nuevo_precio
 
    return True
 
 
def eliminar_plan(codigo, planes, inscripciones):
    if not buscar_codigo(codigo, planes):
        return False
 
    clave_encontrada = ""
    for clave in planes:
        if clave.lower() == codigo.lower():
            clave_encontrada = clave
 
    del planes[clave_encontrada]
    del inscripciones[clave_encontrada]
    return True

 
def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    return True
 
 
def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True
 
 
def validar_tipo(tipo):
    tipos_permitidos = ["mensual", "trimestral", "anual"]
    if tipo in tipos_permitidos:
        return True
    return False
 
 
def validar_duracion(duracion):
    try:
        valor = int(duracion)
    except ValueError:
        return False
 
    if valor > 0:
        return True
    return False
 
 
def validar_acceso_piscina(valor):
    valor = valor.lower()
    if valor == "s" or valor == "n":
        return True
    return False
 
 
def validar_incluye_clases(valor):
    valor = valor.lower()
    if valor == "s" or valor == "n":
        return True
    return False
 
 
def validar_horario(horario):
    if horario.strip() == "":
        return False
    return True
 
 
def validar_precio(precio):
    try:
        valor = int(precio)
    except ValueError:
        return False
 
    if valor > 0:
        return True
    return False
 
 
def validar_cupos(cupos):
    try:
        valor = int(cupos)
    except ValueError:
        return False
 
    if valor >= 0:
        return True
    return False
 
 
def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, planes, inscripciones):
    if buscar_codigo(codigo, planes):
        return False
 
    if acceso_piscina.lower() == "s":
        acceso_bool = True
    else:
        acceso_bool = False
 
    if incluye_clases.lower() == "s":
        clases_bool = True
    else:
        clases_bool = False
 
    planes[codigo] = [nombre, tipo, int(duracion), acceso_bool, clases_bool, horario]
    inscripciones[codigo] = [int(precio), int(cupos)]
 
    return True