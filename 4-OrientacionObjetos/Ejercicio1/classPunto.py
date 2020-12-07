import math

class Punto:
    'Clase que define un punto en un plano'
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    def cuadrante(self):
        if self.X == 0 and self.Y == 0:
            print(f'El Punto ubicado en ({self.X}, {self.Y}) se sitúa en Origen de Coordenadas')
            return 0
        if self.X == 0 and self.Y != 0:
            print(f'El Punto ubicado en ({self.X}, {self.Y}) se sitúa sobre el eje Y')
            return 'Y'
        if self.X != 0 and self.Y == 0:
            print(f'El Punto ubicado en ({self.X}, {self.Y}) se sitúa sobre el eje X')
            return 'X'
        if self.X > 0 and self.Y > 0:
            print(f'El Punto ubicado en ({self.X}, {self.Y}) se sitúa en el 1er Cuadrante')
            return 1
        if self.X > 0 and self.Y < 0:
            print(f'El Punto ubicado en ({self.X}, {self.Y}) se sitúa en el 4º Cuadrante')
            return 4
        if self.X < 0 and self.Y > 0:
            print(f'El Punto ubicado en ({self.X}, {self.Y}) se sitúa en el 2º Cuadrante')
            return 2
        if self.X < 0 and self.Y < 0:
            print(f'El Punto ubicado en ({self.X}, {self.Y}) se sitúa en el 3er Cuadrante')
            return 3

    def vector(self,punto):
        v = [punto.X-self.X, punto.Y-self.Y]
        print(f'El vector resultante es: {v[0], v[1]}')
        return v
    
    def distancia(self,punto):
        d = math.sqrt( math.pow((punto.X - self.X),2) + math.pow((punto.Y - self.Y),2) )
        print(f'La distancia desde el punto ({self.X}, {self.Y}) hasta el punto ({punto.X}, {punto.Y}) es = {d}')
        return d