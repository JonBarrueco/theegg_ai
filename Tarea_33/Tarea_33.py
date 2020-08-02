class Picachu: # Defino clase picachu con atributos vida y ataque y método win que muestra el mensaje de ganador
    vida = 55
    ataque = 45
    def win():
        print("Picachu wins")

class Bulbasur: # Defino clase bulbasur con atributos vida y ataque y método win que muestra el mensaje de ganador
    vida = 55
    ataque = 45
    def win():
        print("Bulbasur wins")

turno = 1 # Inicializo la variable turno a 0. Cuando es 0 el turno es de picachu, si es uno de bulbasur

while Picachu.vida >= 0 and Bulbasur.vida >= 0:
    if turno == 1: # Ataca Picachu
        Bulbasur.vida = Bulbasur.vida - Picachu.vida # Actualizamos la vida de Bulbasur
        turno = 0 # El turno pasa a Bulbasur
    else: # Ataca Bulbasur
        Picachu.vida = Picachu.vida - Bulbasur.vida # Actualizamos la vida de Picachu
        turno = 1 # El turno pasa a Picachu

if Picachu.vida < 0: # Gana Bulbasur
    Bulbasur.win() # Mostramos mensaje vencedor
else: # Gana Picachu
    Picachu.win() #Mostramos mensaje vencedor