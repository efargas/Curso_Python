import classPunto as cP

#Puntos para validar con los ejemplos
PuntoA = cP.Punto(3)
PuntoA.cuadrante()
PuntoB = cP.Punto(10,2)
PuntoA.vector(PuntoB)
PuntoC = cP.Punto(16)
PuntoA.distancia(PuntoC)

#Puntos para mostrar cuadrantes
P0 = cP.Punto()
P1 = cP.Punto(3,7)
P2 = cP.Punto(-3,7)
P3 = cP.Punto(-3,-7)
P4 = cP.Punto(3,-7)
PX = cP.Punto(7,0)
PY = cP.Punto(0,7)

P0.cuadrante()
P1.cuadrante()
P2.cuadrante()
P3.cuadrante()
P4.cuadrante()
PX.cuadrante()
PY.cuadrante()
