import graphviz
import tempfile
from os.path import exists
import urllib.request
from inscriptis import get_text

def decision(actual, condicion, paso, transformacion):
    print("Decisiones")

def Grafo():
    Grafo = graphviz.Digraph('Diccionario')
    Grafo.attr(rankdir='LR')
    Grafo.attr('node', shape='circle')
    Grafo.node('Q0')
    Grafo.attr('node', shape='plaintext')
    Grafo.edge('', 'Q0', label='Inicio')

    Grafo.attr('node', shape='circle')
    Grafo.edge('Q0', 'Q1', label='w')
    Grafo.edge('Q1', 'Q2', label='e')
    Grafo.edge('Q2', 'Q3', label='b')
    Grafo.edge('Q3', 'Q4', label='p')
    Grafo.edge('Q3', 'Q5', label='s')
    Grafo.edge('Q3', 'Q6', label='m')
    Grafo.edge('Q4', 'Q7', label='a')
    Grafo.edge('Q7', 'Q8', label='g')
    Grafo.edge('Q5', 'Q10', label='i')
    Grafo.edge('Q10', 'Q11', label='t')
    Grafo.edge('Q6', 'Q13', label='a')
    Grafo.edge('Q13', 'Q14', label='s')
    Grafo.edge('Q14', 'Q15', label='t')
    Grafo.edge('Q15', 'Q16', label='e')
    Grafo.edge('Q0', 'Q18', label='e')
    Grafo.edge('Q18', 'Q19', label='b')
    Grafo.edge('Q19', 'Q20', label='a')
    Grafo.edge('Q0', 'Q22', label='p')
    Grafo.edge('Q22', 'Q23', label='a')
    Grafo.edge('Q23', 'Q24', label='g')
    Grafo.edge('Q0', 'Q26', label='s')
    Grafo.edge('Q26', 'Q27', label='i')
    Grafo.edge('Q27', 'Q28', label='t')
    

    Grafo.attr('node',shape='doublecircle')
    Grafo.edge('Q8', 'Q9', label='e')
    Grafo.edge('Q11', 'Q12', label='e')
    Grafo.edge('Q16', 'Q17', label='r')
    Grafo.edge('Q20', 'Q21', label='y')
    Grafo.edge('Q24', 'Q25', label='e')
    Grafo.edge('Q28', 'Q29', label='e')
    Grafo.view(tempfile.mktemp())

def DIAGRAMA():
    try:
        Grafo()
    except Exception:
        print("Error")
        
def Escritura(lista):
    diccionario = ["web","website","webpage","webmaster","ebay","site"]
    Pos = open("Concurrencia.txt", "w+" )
    index = 0
    for i in diccionario:
        Pos.write("\n"+i+"'s encontrados: ")
        Pos.write(str(len(lista[index])))
        Pos.write("\n*En las posiciones:*\n")
        Pos.write(', '.join(map(str,lista[index])))
        index += 1
    Pos.close()

def DES(direccion, flag):

    if (flag == 1):
        archivo = open(direccion, 'r')
        palabras = archivo.read()
        
    elif (flag == 2):
        html = urllib.request.urlopen(direccion).read().decode('utf-8')
        palabras = get_text(html)
        
    else:
        print("Error, contacte al programador")
        return None
    

    web = [ ]
    webpage = [ ]
    website = [ ]
    webmaster = [ ]
    ebay = [ ]
    page = [ ]
    site = [ ]
    listas = [ ]
    
    contador = 0
    estado = 1
    his = open("Historia.txt", "w")
    
    for letra in palabras:
        contador = contador + 1
        his.write("f( Q"+str(estado)+","+letra.lower()+")-> ")
        
        if(estado == 1):
            if(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 2):
            if(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 3
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 3):
            if(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "b"):
                web.append(contador-3)
                estado = 4
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 4):
            if(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 5
            elif(letra.lower() == "s"):
                estado = 6
            elif(letra.lower() == "m"):
                estado = 7
            elif(letra.lower() == "a"):
                estado = 21
            else:
                estado = 1
            continue
        
        if(estado == 5):
            if(letra.lower() == "a"):
                estado = 8
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 6):
            if(letra.lower() == "i"):
                estado = 11
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 7):
            if(letra.lower() == "a"):
                estado = 14
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 8):
            if(letra.lower() == "g"):
                estado = 9
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 9):
            if(letra.lower() == "e"):
                webpage.append(contador-7)
                estado = 10
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 10):
            if(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 11):
            if(letra.lower() == "t"):
                estado = 12
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 12):
            if(letra.lower() == "e"):
                website.append(contador-7)
                estado = 10
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 14):
            if(letra.lower() == "s"):
                estado = 15
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            else:
                estado = 1
            continue
        
        if(estado == 15):
            if(letra.lower() == "t"):
                estado = 16
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 16):
            if(letra.lower() == "e"):
                estado = 17
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 17):
            if(letra.lower() == "r"):
                webmaster.append(contador-9)
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 19):
            if(letra.lower() == "b"):
                estado = 19
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 20):
            if(letra.lower() == "a"):
                estado = 21
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 21):
            if(letra.lower() == "y"):
                ebay.append(contador-4)
                estado = 10
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 23):
            if(letra.lower() == "a"):
                estado = 24
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 24):
            if(letra.lower() == "g"):
                estado = 25
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 25):
            if(letra.lower() == "e"):
                page.append(contador-4)
                estado = 10
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 27):
            if(letra.lower() == "i"):
                estado = 28
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 28):
            if(letra.lower() == "t"):
                estado = 29
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "e"):
                estado = 19
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue
        
        if(estado == 29):
            if(letra.lower() == "e"):
                site.append(contador-4)
                estado = 10
            elif(letra.lower() == "w"):
                estado = 2
            elif(letra.lower() == "p"):
                estado = 23
            elif(letra.lower() == "s"):
                estado = 27
            else:
                estado = 1
            continue  
        
    listas.append(web)
    listas.append(website)
    listas.append(webpage)
    listas.append(webmaster)
    listas.append(ebay)
    listas.append(site)
    
    Escritura(listas)
    his.close()    
    if(flag == 1):
        archivo.close()       
        
if __name__ == "__main__":

    while(True):
      print("****Diccionario****")  
      print("1.- Cargar el archivo")
      print("2.- Grafo")
      print("3.- Salir")
      OP = int(input("Seleccione una opcion: "))
      if(OP == 1):
        direccion = str(input('Escribe el nombre del archivo o el link (incluyendo www o http) de la pagina web: '))
        if(exists(direccion)):
            DES(direccion, 1)
        elif(direccion[:3] == "www" or direccion[:4] == "http"):
            print("Selecciono web, espere en lo que analizamos la pagina")
            DES(direccion, 2)
        else:
            print("El archivo especificado no existe")
      elif(OP == 2):
        DIAGRAMA()
        
      elif(OP == 3):
          print("¡ADIOS!")
          break

      else:
        print("Esa opcion no es valida, ¡ADIOS!")
        break