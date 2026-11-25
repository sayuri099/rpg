while True:
  ataque()
  defesa()
  
  vida_1p = 100
  vida_monstro = 80
  personagem = True
  espada = 100
  poçao = 2
  valor_poçao = 100
  
def ataque():
  vida_1p - 10
  print("*dano* personagem -10 life")



def defesa():
 if vida_1p > 0 and espada > 100:
   vida_monstro - 40
   print("*dano* personagem -40 life")
