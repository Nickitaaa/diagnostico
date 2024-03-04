## crea una clase llamda vehiculo capsa de procesar la informacion basica d los autos en una consecionaria. Debera tener constructor y los atributos del vehiculo serán: patente, goma, marca, modelo, kilometraje. Crear metodos (accesos) getter y (modifiacion) setter. mopstrar por pantalla al menos 1 atrubuto y modificar el kilometrajes

class Vehículo:
    def _init_(self, patente, marca, modelo, kilometraje):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje

    def get_patente(self):
        return self.patente

    def set_kilometraje(self, nuevo_kilometraje):
        self.kilometraje = nuevo_kilometraje
        print("El kilometraje ha sido actualizado.")
auto1 = Vehículo("ABC123", "Toyota", "Corolla", 50000)
print("Patente del vehículo:", auto1.get_patente())
print("Kilometraje actual:", auto1.kilometraje)
auto1.set_kilometraje(55000)
print("Nuevo kilometraje:", auto1.kilometraje)


 
