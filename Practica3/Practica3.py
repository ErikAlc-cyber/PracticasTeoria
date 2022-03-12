import random
import time
import graphviz 
import tempfile

def grafica():
  f = graphviz.Digraph('finite_state_machine')

  f.attr('node', shape='doublecircle')
  f.node('Q0')

  f.attr('node', shape='plaintext')
  f.edge('', 'Q0', label='Inicio')

  f.attr('node', shape='circle')
  f.edge('Q0', 'Q2', label='1', constraint='false')
  f.edge('Q0', 'Q1', label='0')
  f.edge('Q2', 'Q0', label='1')
  f.edge('Q1', 'Q0', label='0')
  f.edge('Q1', 'Q3', label='1', constraint='false')
  f.edge('Q3', 'Q1', label='1', constraint='false')
  f.edge('Q2', 'Q3', label='0', constraint='false')
  f.edge('Q3', 'Q2', label='0', constraint='false')
  f.view(tempfile.mktemp('.png'))

def par(num):
  if num % 2 == 0:
    return True
  else:
    return False

def repre_adf(pre, simbolo, arch):
    if(pre == "q0"):
        if(simbolo == "1"):
            siguiente = "q2"
        else:
            siguiente = "q1"
    elif(pre == "q1"):
        if(simbolo == "1"):
            siguiente = "q3"
        else:
            siguiente = "q0"
    elif(pre == "q2"):
        if(simbolo == "1"):
            siguiente = "q0"
        else:
            siguiente = "q3"
    elif(pre == "q3"):
        if(simbolo == "1"):
            siguiente = "q1"
        else:
            siguiente = "q2"
    arch.write("| f("+pre+", "+simbolo+") -> "+siguiente+" |")
    return siguiente

def binario_random(n):
    anterior = "q0"
    
    filelog = open("Practica3/Automata.txt", "a+")
    key1 = ""
    
    for i in range(n):
         
        temp = str(random.randint(0, 1))
        anterior = repre_adf(anterior, temp, filelog)
        key1 += temp
    
    filelog.write("\n")
    filelog.close()
    return key1

def transformar(num):
  unos = 0
  global aceptados
  global rechazados
  
  for i in num:
    unos += int(i)
  ceros = len(num) - unos
  return unos, ceros
  
def adf(array, num, acep, rec):
  
  num.write(array+"\n")
  unos, ceros = transformar(array)
  
  if(par(unos) and par(ceros)):
    acep.write(array+"\n")
  else:
    rec.write(array+"\n")
  
def new_gen():
  
  filenum = open("Practica3/Numeros.txt", "w")
  fileace = open("Practica3/Aceptados.txt", "w")
  filerec = open("Practica3/Rechazados.txt", "w")
  
  num = []
  inicio = time.time()  
  
  for i in range(10**6): #(10**6)
    try:
      task = binario_random(64) #64
      num.append(task)
      del task
          
    except (KeyboardInterrupt, OverflowError):
      break
    
  fin = time.time()
  
  print("El tiempo de ejecucion de generacion de cadenas es: "+str(fin-inicio))
  print("Inicia el ADF")
  
  for i in num:
    adf(i, filenum, fileace, filerec)
  return num

  filenum.close() 
  fileace.close() 
  filerec.close() 
  
def protocolo():
  repeticiones = 0
  while(bool(random.getrandbits(1))):
    estado = bool(random.getrandbits(1))
    filelog = open("Practica3/Automata.txt", "w")
    filelog.close()
      
    if(estado):
      numeros=new_gen()
      time.sleep(1)
      print("Total cadenas:"+str(len(numeros)))
      del numeros
    else:
      print(estado)
    repeticiones += 1
    
  print("El programa se ejecuto: "+str(repeticiones)+" veces")
  
if __name__ == "__main__":
    """Main function"""
    
    print("Practica #3")
    
    while(True):
      print("1) Ejecutar programa")
      print("2) Graficar Automata")
      print("3) Salir")
      opc = int(input("Selecciona la opcion: "))
      if(opc == 1):
        protocolo()
      
      elif(opc == 2):
        grafica()
      
      elif(opc == 3):
        break
      
      else:
        print("Opcion no valida, porfavor introduzca una opcion correcta")