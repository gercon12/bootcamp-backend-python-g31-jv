

class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

clasico = Vehiculo("Ford", "Mustang", 1967, 30000)
deportivo = Vehiculo("Chevrolet", "Camaro", 2020, 40000)
suv = Vehiculo("Toyota", "RAV4", 2021, 35000)

print(f"Vehículo clásico: {clasico.marca} {clasico.modelo}, Año: {clasico.anio}, Precio: ${clasico.precio}")
print(f"Vehículo deportivo: {deportivo.marca} {deportivo.modelo}, Año: {deportivo.anio}, Precio: ${deportivo.precio}")
print(f"Vehículo SUV: {suv.marca} {suv.modelo}, Año: {suv.anio}, Precio: ${suv.precio}")