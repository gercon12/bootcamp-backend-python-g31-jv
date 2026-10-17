frutas = ["manzana", "uva", "mango", "piña","palta"]

#frutas.slice(1,3)


# INTERBANK
# El siguiente usuario esta teniendo los siguientes movimientos
movimientos = [
{ "fecha": "2024-01-15", "tipo": "deposito", "monto": 1500.00},
{ "fecha": "2024-01-20", "tipo": "retiro", "monto": 200.00},
{ "fecha": "2024-02-05", "tipo": "deposito", "monto": 500.00},
{ "fecha": "2024-02-10", "tipo": "retiro", "monto": 100.00},
{ "fecha": "2024-02-15", "tipo": "deposito", "monto": 300.00},
{ "fecha": "2024-02-20", "tipo": "retiro", "monto": 50.00},
{ "fecha": "2024-02-25", "tipo": "deposito", "monto": 1000.00 }
]


# 01. Sumar todos los depositos
# 02. Sumar todos los retiros

retiro=0;
deposito=0;
for movimiento in movimientos:
    if movimiento["tipo"] == "deposito":
        deposito += movimiento["monto"]
        
    elif movimiento["tipo"] == "retiro":
        retiro += movimiento["monto"]

print("Total Deposito:", deposito)

print("Total Retiro:", retiro)


# 03. Calcular el balance final (depositos - retiros)

print("Balance final:", deposito - retiro)

# 04. Mostrar el deposito mas grande

deposito_mas_grande=0
for movimiento in movimientos:
    if movimiento["tipo"] == "deposito" and movimiento["monto"] > deposito_mas_grande:
        deposito_mas_grande = movimiento["monto"]
print("Deposito mas grande:", deposito_mas_grande)


# 05. Mostrar el retiro mas grande
retiro_mas_grande=0
for movimiento in movimientos:
    if movimiento["tipo"] == "retiro" and movimiento["monto"] > retiro_mas_grande:
        retiro_mas_grande = movimiento["monto"] 
print("Retiro mas grande:", retiro_mas_grande)
