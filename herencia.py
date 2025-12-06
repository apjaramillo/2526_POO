class Persona:  # (defino la clase Persona)
    def hablar(self):  # (creo el metodo hablar)
        print("Hola")  # (muestro Hola)

class Estudiante(Persona):  # (defino la clase Estudiante y heredo de Persona)
    def estudiar(self):  # (creo el metodo estudiar)
        print("Estudio")  # (muestro Estudio)

e = Estudiante()  # (creo un objeto e de la clase Estudiante)
e.hablar()  # (ejecuto el mEtodo hablar heredado de Persona)
e.estudiar()  # (ejecuto el metodo estudiar propio de Estudiante)  #fin