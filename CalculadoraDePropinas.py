print("Bienvenido a la calculadora de propinas")
cuenta=float(input("¿Cuál es el total de la cuenta? $"))
propina=int(input("¿Qué porcentaje de propina te gustaría agregar? ¿10, 12, ó 15? "))
no_personas=int(input("¿Entre cuántas personas se dividirá la cuenta? "))

propina=propina/100+1

#Opcion 1
total=round((cuenta*propina)/no_personas,2)

#Opcion 2 (para que salga $33.60)

total2=(cuenta*propina)/no_personas
total2="{:.2f}".format(total2)
print(f"Cada persona debe pagar: ${total2}")