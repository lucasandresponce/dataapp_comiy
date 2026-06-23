def calcular_salarios(sueldo,iva,nombre):
    salario  = sueldo * (1 - iva)
    
    return(f"{nombre}   ${salario:,.2f}")
    
calcular_salarios(85000,0.17,"ana")    

