from Cuadrado import cuadrado
from TrianguloRectangulo import trianguloRectangulo
from Circulo import circulo
from Coordenadas import coordenadas

baseTri = int(input())
alturaTri = int(input())
coordenadaTriangulo = coordenadas(float(input()),float(input()))
trianguloRectangulo1 = trianguloRectangulo(baseTri, alturaTri,coordenadaTriangulo)

baseCuadrado = int(input())
alturaCuadrado = int(input())
coordenadaCuadrado = coordenadas(float(input()),float(input()))
cuadrado1 = cuadrado(baseCuadrado, alturaCuadrado, coordenadaCuadrado)

radioCirculo = int(input())
coordenadaCirculo = coordenadas(float(input()),float(input()))
circulo1 = circulo(radioCirculo, coordenadaCirculo)

print(f"Triangle Area: {trianguloRectangulo1.CalcularArea()}")
print(f"Triangle Perimeter: {trianguloRectangulo1.CalcularPerimetro()}")
print(trianguloRectangulo1.getCoordenadas())
print()

print(f"Rectangle Area: {cuadrado1.CalcularArea()}")
print(f"Rectangle Perimeter: {cuadrado1.CalcularPerimetro()}")
print(cuadrado1.getCoordenadas())
print()

print(f"Circle Area: {circulo1.CalcularArea()}")
print(f"Circle Perimeter: {circulo1.CalcularPerimetro()}")
print(circulo1.getCoordenadas())
