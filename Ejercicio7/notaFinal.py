taller1 = float(input( "la nota del taller 1 (1.0-5.0 : "))
taller2 = float(input( "la nota del taller 2 ( 1.0-5.0: "))
cuestionario1 = float(input("la nota del cuestionario 1 (1.0-5.0 : "))
cuestionario2 = float(input("la nota del cuestionario 2 (1.0-5.0 :"))
proyecto_final = float(input("la nota del proyecto final (1.0-5.0 :"))

pesos_taller1 = 0.20
pesos_taller2 = 0.15
pesos_cuestionario1 = 0.22
pesos_cuestionario2 = 0.10
pesos_proyecto_final = 0.36

nota_final = (taller1 * pesos_taller1) + (taller2 * pesos_taller2) + (cuestionario1 * pesos_cuestionario1) + (cuestionario2 * pesos_cuestionario2) + (proyecto_final * pesos_proyecto_final)

print(f"La nota final es: {nota_final:.2f}")

if 1.0<= nota_final >= 2.9:
    clasificacion = "excelente"

elif 2.9<= nota_final >=5.0 :
    clasificacion = "bien"

else:
    clasificacion = "deficiente"


