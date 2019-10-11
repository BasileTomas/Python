def main():
    presentacion = " Calculadora de divisas "
    print(presentacion.center(80, "="))
    print(" Calcula el monto ingresado en Peso Argentinos a USD o EUR \n")
    divisa()

def divisa():
    while(True):
        try:
            monto = float(input("Ingrese el monto que desea calcular: "))
            break
        except ValueError:
            print("Debe ingresar un valor numerico. \n") 
    div = (input("Ingrese a qué divisa desea convertir su monto: \n 1) USD. \n 2) EUR. \n")).upper()
    while((div != "USD") & (div != "EUR")):
        print("\n Opcion invalida, debe seleccionar alguna de las opciones. \n")
        div = input("Ingrese a qué divisa desea convertir su monto: \n 1) USD. \n 2) EUR. \n")
    calculadora(div, monto)

def calculadora (divisa, monto):
    cotizacion_usd = 59.5
    cotizacion_eur = 67.1
    if(divisa == "USD"):
        monto = monto / (cotizacion_usd)
    elif(divisa == "EUR"):
        monto = monto / (cotizacion_eur)
    
    print("Su monto representa a {:.2f} {}".format(monto,divisa))

if __name__ == '__main__':
    main()
    