def clasificar_transaccion():
    monto = 45750

    if monto < 1000:
        categoria = "micro transacción"
    elif monto <= 9999:
        categoria = "transacción estándar"
    elif monto <= 99999:
        categoria = "transacción importante"
    else:
        categoria = "transacción de alto valor"

    print(f"Monto: ${monto} — Categoría: {categoria}")

clasificar_transaccion()

