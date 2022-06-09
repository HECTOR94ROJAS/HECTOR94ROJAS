Declaramos una variable
calificacion = input("Introduce tu calificaciòn de la AZ-900: ")

calificacion = int(calificacion)

#Preguntamos si la calificaciòn es menor a 700
if calificacion < 700 : 
    print("Veeees, por no estudiar") #Si es menos a 700, muestra esto
elif calificacion == 700:
    print("PANZAZOOOO")
elif calificacion > 1000 :
    print("Mientes!! No puedes sacar màs de mil")
else :#Si no se cumple el if anterior, pasa a esta linea
 print("Felicidades, pasa por tu Certificado") #Se ejecuta si ninguno de los if se cumple

#Verificador de mayorìa de edad
edad = input ("Introduce tu edad?")
edad = int(edad)

if edad >= 18 and edad <= 100 :
  print("¡¡Bienvenidos al mamitas!!")
elif edad > 100 :
  print ("Si vienes acompañada de tus abuelitos, si te podemos fiar")
elif edad < 0 :
  print("NI QUE FUERAS VIAJERO DEL TIEMPO")
else :
  print("¡¡NO PUEDES LLEVARTE ESOS CIGARROS!!")

#En PYTHON NO HAY SWITCHES CASE