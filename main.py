import funciones as fn
 
planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}
 
inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15]
}
 
opcion = 0
 
while opcion != 6:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")
 
    opcion = fn.leer_opcion()
 
    if opcion == 1:
        tipo = input("Ingrese el tipo de plan (mensual/trimestral/anual): ")
        fn.cupos_tipo(tipo, planes, inscripciones)
 
    elif opcion == 2:
        datos_validos = False
        while datos_validos == False:
            try:
                p_min = int(input("Ingrese el precio mínimo: "))
                p_max = int(input("Ingrese el precio máximo: "))
            except ValueError:
                print("Debe ingresar valores enteros")
                continue
 
            if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                datos_validos = True
            else:
                print("Debe ingresar valores enteros")
 
        fn.busqueda_precio(p_min, p_max, planes, inscripciones)
 
    elif opcion == 3:
        repetir = "s"
        while repetir == "s":
            codigo = input("Ingrese el código del plan: ")
 
            precio_valido = False
            while precio_valido == False:
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                except ValueError:
                    print("Debe ingresar valores enteros")
                    continue
 
                if nuevo_precio > 0:
                    precio_valido = True
                else:
                    print("Debe ingresar valores enteros")
 
            resultado = fn.actualizar_precio(codigo, nuevo_precio, planes, inscripciones)
            if resultado:
                print("Precio actualizado")
            else:
                print("El código no existe")
 
            repetir = input("¿Desea actualizar otro precio (s/n)? ")
            repetir = repetir.lower()
 
    elif opcion == 4:
        codigo = input("Ingrese el código del plan: ")
        nombre = input("Ingrese el nombre del plan: ")
        tipo = input("Ingrese el tipo de plan (mensual/trimestral/anual): ")
        duracion = input("Ingrese la duración en meses: ")
        acceso_piscina = input("¿Incluye acceso a piscina? (s/n): ")
        incluye_clases = input("¿Incluye clases grupales? (s/n): ")
        horario = input("Ingrese el horario disponible: ")
        precio = input("Ingrese el precio mensual: ")
        cupos = input("Ingrese la cantidad de cupos: ")
 
        if not fn.validar_codigo(codigo):
            print("El código no puede estar vacío. No se registró el plan.")
        elif fn.buscar_codigo(codigo, planes):
            print("El código ya existe. No se registró el plan.")
        elif not fn.validar_nombre(nombre):
            print("El nombre no puede estar vacío. No se registró el plan.")
        elif not fn.validar_tipo(tipo):
            print("El tipo debe ser mensual, trimestral o anual. No se registró el plan.")
        elif not fn.validar_duracion(duracion):
            print("La duración debe ser un número entero mayor que cero. No se registró el plan.")
        elif not fn.validar_acceso_piscina(acceso_piscina):
            print("El acceso a piscina debe ser s o n. No se registró el plan.")
        elif not fn.validar_incluye_clases(incluye_clases):
            print("Incluye clases debe ser s o n. No se registró el plan.")
        elif not fn.validar_horario(horario):
            print("El horario no puede estar vacío. No se registró el plan.")
        elif not fn.validar_precio(precio):
            print("El precio debe ser un número entero mayor que cero. No se registró el plan.")
        elif not fn.validar_cupos(cupos):
            print("Los cupos deben ser un número entero mayor o igual a cero. No se registró el plan.")
        else:
            fn.agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, planes, inscripciones)
            print("Plan agregado")
 
    elif opcion == 5:
        codigo = input("Ingrese el código del plan a eliminar: ")
        resultado = fn.eliminar_plan(codigo, planes, inscripciones)
        if resultado:
            print("Plan eliminado")
        else:
            print("El código no existe")
 
    elif opcion == 6:
        print("Programa finalizado.")