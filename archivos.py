def leer_archivo(file_name):
    print(f'Intentas abrir este archivo {file_name}')
    #Abrir open()
    #Procesar read/write
    #Cerrar close()
    #With nos permite agrupar el trabajp con archivos
    
    with open(file_name, 'r') as file:
        lineas = file.readline()
        for linea in lineas:
            print(linea)
        #while(linea):
        #    print(linea)
        #   linea = file.readline()
            
    #print('Archivo leido y cerrado')
    
def agregar_equipo(file_name, equipo):
    with open(file_name, 'a') as file:
        file.write(f"\n{equipo}")
    print("equipo guardado")
    
def eliminar_equipo(file_name, equipo):
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()
    try:
        lista_equipos.remove(equipo)
        print("Equipo eliminado!")
        with open(file_name, 'w') as file:
            file.writelines(lista_equipos)
    except ValueError:
        print('El equipo que deseas eliminar no existe')
        
def actualiza_equipo(file_name, equipo , new_equipo):
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()
    try:
        index_equipo = lista_equipos.index(f'{equipo}\n')
        lista_equipos[index_equipo] = new_equipo
        with open(file_name, 'w') as file:
            file.writelines(f'{lista_equipos}\n')
    except ValueError:
        print('El equipo no se encontró')
