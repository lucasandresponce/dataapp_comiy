
precios = [8500, 32000, 15900, 7200, 54000, 123000]
impuesto = 0.19
total = 0



for precio in precios:
    precio_final = precio + (precio * impuesto)

    print(f"precio base: ${precio}")
    print(f"Precio final : {precio_final}")

    total = total + precio_final

print(f"Total general: ${total}")
                                
                        
