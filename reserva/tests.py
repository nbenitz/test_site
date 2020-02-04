#from django.test import TestCase



# Create your tests here.

"""

    for habitacion in lista_habitaciones:
        for id_habitacion in habitacion.keys():
            flag_habitacion_libre = True
            for hab_reservada in lista_hab_reservada:            
                for id_hab_reservada in hab_reservada.keys():
                    if hab_reservada[id_hab_reservada]==habitacion[id_habitacion]:
                        flag_habitacion_libre = False
                if flag_habitacion_libre == False:
                    print("Habitacion %s reservada" %(habitacion[id_habitacion]))
                    break
            if flag_habitacion_libre == True:
                print("Habitacion %s libre" %(habitacion[id_habitacion]))
                lista_hab_disponible.append({'id': habitacion[id_habitacion]})


    
    for habitacion in lista_habitaciones:
        flag_habitacion_libre = True
        for hab_reservada in lista_hab_reservada:            
            if hab_reservada[id_hab_reservada]==habitacion[habitacion]:
                flag_habitacion_libre = False
            if flag_habitacion_libre == False:
                print("Habitacion %s reservada" %(habitacion[habitacion]))
                break
        if flag_habitacion_libre == True:
            print("Habitacion %s libre" %(habitacion[habitacion]))
            print(habitacion)
            lista_hab_disponible.append({'id': habitacion[habitacion]})
            #lista_hab_disponible.append({'nro': habitacion[id_habitacion]})
    """


                    

