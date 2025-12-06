class Figura:  # (defino la clase Figura)
    def dibujar(self):  # (creo el metodo dibujar)
        print("Dibujo figura")  # (muestro Dibujo figura)

class Circulo(Figura):  # (defino la clase Circulo y heredo de Figura)
    def dibujar(self):  # (sobrescribo el metodo dibujar)
        print("Dibujo círculo")  # (muestro Dibujo círculo)

Figura().dibujar()  # (creo un objeto Figura y dibujo figura)
Circulo().dibujar()  # (creo un objeto Circulo y dibujo círculo)