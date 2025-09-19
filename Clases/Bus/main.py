from bus import Bus
from pasajeros import Pasajero

def gestionar_bus(bus):
    """Submenú para manejar un bus específico"""
    while True:
        print(f"=== GESTIONANDO BUS {bus.id} ===")
        print(f"Capacidad total: {bus.getCapacidad()}")
        print(f"Ocupados: {bus.getBilletes()}")
        print(f"Libres: {bus.asientosLibres()}")
        print("\nOpciones:")
        print("1. Comprar billete")
        print("2. Mostrar pasajeros")
        print("3. Devolver billete")
        print("0. Volver al menú principal")

        opcion = int(input("\nSeleccione una opción: "))

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
    print("1. Crear nuevo bus")
    print("2. Listar buses")
    print("3. Seleccionar un bus")
    print("0. Salir")

    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 1:
        capacidad = int(input("Capacidad del bus: "))
        bus = Bus(capacidad)
        bus.id = contador_id  # asignar un ID único
        buses[contador_id] = bus
        print(f"Bus {contador_id} creado con capacidad {capacidad}.")
        contador_id += 1
        input("\nPresione Enter para continuar...")

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
            bus_id = int(input("Ingrese el ID del bus: "))
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