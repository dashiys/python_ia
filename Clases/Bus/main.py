from bus import Bus
from pasajeros import Pasajero

def NumValido(msj):
    while True:
        try:
            opcion = int(input(msj))
            return opcion
        except ValueError:
            print("Error: Introduce un número válido")

def gestionar_bus(bus):
    """Submenú para manejar un bus específico"""
    while True:
        opcion = NumValido(
        f"=== GESTIONANDO BUS {bus.id} ===\n"\
        f"Capacidad total: {bus.getCapacidad()}\n"\
        f"Ocupados: {bus.getBilletes()}\n"\
        f"Libres: {bus.asientosLibres()}\n"\
            "\nOpciones:\n"\
            "1. Comprar billete\n"\
            "2. Mostrar pasajeros\n"\
            "3. Devolver billete\n"\
            "0. Volver al menú principal\n")
    
        if opcion == 1:
            nombre = input("Nombre de la persona: ")
            persona = Pasajero(nombre)
            bus.comprarBillete(persona)
            input("\nPresione Enter para continuar...")

        elif opcion == 2:
            bus.mostrarPasajeros()
            input("\nPresione Enter para continuar...")

        elif opcion == 3:
            nombre = input("Nombre del pasajero a devolver: ")
            bus.devolverBillete(nombre)
            input("\nPresione Enter para continuar...")

        elif opcion == 0:
            break
        else:
            print("Opción no válida.")
            input("\nPresione Enter para continuar...")

buses = {}
contador_id = 1

while True:
    
    opcion = NumValido(
        "\nOpciones:\n"\
        "1. Crear nuevo bus\n"\
        "2. Listar buses\n"\
        "3. Seleccionar un bus\n"\
        "0. Salir\n")

    if opcion == 1:
        while True:
            capacidad = NumValido("Capacidad del bus: ")
            if capacidad > 0:
                break
            else:
                print(f"El numero no puede ser negativo")
                
        bus = Bus(capacidad)
        bus.id = contador_id  # asignar un ID único
        buses[contador_id] = bus
        print(f"Bus {contador_id} creado con capacidad {capacidad}.")
        contador_id += 1
        input("\nPresione Enter para continuar...\n")

    elif opcion == 2:
        if not buses:
            print("No hay buses creados.")
        else:
            print("\nLista de buses:")
            for bid, bus in buses.items():
                print(f"- Bus {bid}: {bus.getBilletes()}/{bus.getCapacidad()} ocupados, {bus.asientosLibres()} libres")
        input("\nPresione Enter para continuar...")

    elif opcion == 3:
        if not buses:
            print("No hay buses creados.")
            input("\nPresione Enter para continuar...")
        else:
            bus_id = NumValido("Ingrese el numero del bus: ")
            if bus_id in buses:
                gestionar_bus(buses[bus_id])
            else:
                print("Bus no encontrado.")
                input("\nPresione Enter para continuar...")

    elif opcion == 0:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")
        input("\nPresione Enter para continuar...")