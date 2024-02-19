import string

def provera(element,br,sl): #da li je uneti potez na tabli
    # da ne prelazi granice table
    
    Abc=65 #ascci A
    pozicijaX=br    

    if(ord(sl)>=Abc):        
        pozicijaY=ord(sl)-Abc  #C 68-65=3    
        
        
        if(pozicijaY>m-1 or pozicijaY<0):
            print("Doslo je do greske, elemnet je van table")
            
            return False    
        if(pozicijaX>n or pozicijaX<0):
            print("Doslo je do greske, elemnet je van table")
             
            return False    

        #da li je van tabele 
        if(provera2(element,br,sl)):
           
            return True
        else:
            return False
    return True

def provera2(element,br,sl):
    #da li može da se odigra na toj poziciji 

    if(element=="X"):
        naPotezu=0
    elif(element=="O"):
        naPotezu=1
    kolNum=n
    pratiMatricu=0
    Abc=65    
    if(ord(sl)>=Abc):
        pozicijaY=ord(sl)-Abc 
        
        while(kolNum!=0):
            if(kolNum==br):
                if(naPotezu==0):
                    
                    if(prva_Matrica[pratiMatricu][pozicijaY]!=[None] or  prva_Matrica[pratiMatricu-1][pozicijaY]!=[None]):
                            print("Vec postoji X na tom mestu")         
                            return False 
                           
                elif(naPotezu==1):
                        
                        if(prva_Matrica[pratiMatricu][pozicijaY]!=[None] or  prva_Matrica[pratiMatricu][pozicijaY+1]!=[None]):
                            print("Vec postoji O na tom mestu")          
                            return False    
            pratiMatricu+=1
            kolNum-=1
    return True

def startGame():    
    global m,n,naPotezu,prva_Matrica, xv, ov
    m = int(input("Unesite broj vrsta: "))
    n = int(input("Unesite broj kolona: "))
    naPotezu = int(input("unesite igraca koji je prvi na potezu (0 - |X|, 1 - |O|): "))
    stanje=naPotezu
    if(m < 3 or n < 3):
        print("Velicina table ne validna, najmanja tabla je 4x4")
        return False
    if(naPotezu != 0 and naPotezu != 1):
        print("unos nije validan")
        return False

    prva_Matrica=[[[None] for x in range(n)]for x in range(m)]
    xv= (m-1)*n
    ov= (n-1)*m

    z = int(input("unesite 0 ili 1 (0 - igrac vs igrac, 1 - igrac vs pc):"))
    if(z==0):
        PromenaStanja()
        while(Kraj(naPotezu)==False): # da li se završila igra
            if(stanje==1): 
                naPotezu=0
                stanje=0     
                Upisi(prva_Matrica)
                print("Na sledecem potezu je O")
            else:
                naPotezu=1
                stanje=1
                Upisi(prva_Matrica)
                print("Na sledecem potezu je X")
    elif(z==1):
        CovekProtivRacunara()
    else:
        print("Greska")
    

    #proverava sve pozicije za x i o
def racunaj_XVal():
    global n,m, naPotezu
    x = 0
    naPotezu = 0
    for row in range(0, m):
        for col in range(65, 65+n):
           
            if(provera("X",row,chr(col))):
                x += 1
    return x
    
def racunaj_OVal():
    global n,m, naPotezu
    o = 0
    naPotezu = 1
    for row in range(0, m):
        for col in range(65, 65+n):
           
            if(provera("O",row,chr(col))):
                o += 1
    return o

def showTable(matt): #prikazuje tablu 
    mat=matt
    tablaKolona = "  "
    tablaIvica = "  "
    for number in range(0,m):
        tablaKolona += " " + chr(ord("A")+number)
        tablaIvica += " ="
    print(tablaKolona)
    print(tablaIvica)
    kolNum = n
    for row in mat:
        redStr = str(kolNum)+"||"
        redIspod = "  "
        for el in row:
            if(el == [None]):
                redStr += " |"
                redIspod += " -"
            if(el == "X"):
                redStr += "X|"
                redIspod += " -"
            if(el == "O"):
                redStr += "O|"
                redIspod += " -"
        redStr += "|" + str(kolNum)
        print(redStr)
        if(kolNum != 1):
            print(redIspod)
        kolNum -= 1

    print(tablaIvica)
    print(tablaKolona)

#upisuje potez, traži ulaz sa tastature
def Upisi(matt):
    mat=matt
    br=int(input("Unesite za poziciju Y kordinate(broj): "))
    slovo=input("Unesite za poziciju X kordinate(slovo): ")    
    sl=slovo.upper()
    if(naPotezu==0):
        element="X"
    elif(naPotezu==1):
        element="O"
    
    

    proveraTF=provera(element,br,sl)
    if(proveraTF):
        Abc=65
        y=ord(sl)-Abc
        kolNum=n     
        
        pratiMatricu=0
        while(kolNum!=0):
            if(kolNum==br):
                if(naPotezu==0):                
                    element="X"
                    mat[pratiMatricu][y]=element
                    mat[pratiMatricu-1][y]=element
                elif(naPotezu==1):
                    element="O"
                    mat[pratiMatricu][y]=element
                    mat[pratiMatricu][y+1]=element       
            pratiMatricu+=1
            kolNum-=1
    else:
        print("GRESKA")
        Upisi(mat)
    
    if(proveraTF):
        showTable(prva_Matrica)

def UpisiRacunar(matt, potez):
    global xv,ov
    mat=matt
    br=(potez["broj"])
    slovo=potez["slovo"]     
    sl=slovo.upper()
    if(naPotezu==0):
        element="X"
    elif(naPotezu==1):
        element="O"
    
    

    proveraTF=provera(element,br,sl)
    if(proveraTF):
        Abc=65
        y=ord(sl)-Abc
        kolNum=n     
        
        pratiMatricu=0
        while(kolNum!=0):
            if(kolNum==br):
                if(naPotezu==0):                
                    element="X"
                    mat[pratiMatricu][y]=element
                    mat[pratiMatricu-1][y]=element
                    #xv = racunaj_XVal()
                    #ov = racunaj_OVal()
                elif(naPotezu==1):
                    element="O"
                    mat[pratiMatricu][y]=element
                    mat[pratiMatricu][y+1]=element
                    #xv = racunaj_XVal()
                    #ov = racunaj_OVal()    
            pratiMatricu+=1
            kolNum-=1
    else:
        print("GRESKA")
        p = {
            "broj": int(input("Unesite za poziciju Y kordinate(broj): ")),
            "slovo": input("Unesite za poziciju X kordinate(slovo): ")
            }
        UpisiRacunar(mat, potez)
    
    if(proveraTF):
        showTable(prva_Matrica)

def Kraj(naPotezu1):
    PozicijaX=1
    pozicijaY=0
    naPotezu=naPotezu1
    if(naPotezu==0):
        element="X"
    elif(naPotezu==1):
        element="O"
    p="A"
    brojac=0
    
    while(PozicijaX<=n) :
        pozicijaY=0
        brojac=0  
        while(brojac<m-1):
                pozicijaY=brojac         
                if(naPotezu==0):
                    if(prva_Matrica[PozicijaX][pozicijaY]==[None]):
                        pozicijaY=chr(pozicijaY+65)
                        p=pozicijaY
                        proveraTF=provera(element,PozicijaX,pozicijaY)  
                        pozicijaY=ord(p)-65  
                        if(proveraTF):
                           pozicijaY=chr(pozicijaY+65)
                           print("Slobodan potez X je moguc na poziciji"+str(PozicijaX)+" "+str(pozicijaY)) 
                           #Upisi(prva_Matrica)
                           pozicijaY=ord(p)-65 
                           return False                                                 
                elif(naPotezu==1):
                    if(prva_Matrica[PozicijaX][pozicijaY]==[None]):                        
                        pozicijaY=chr(pozicijaY+65)
                        proveraTF=provera(element,PozicijaX,pozicijaY) 
                        pozicijaY=ord(p)-65             
                        if(proveraTF):
                            pozicijaY=chr(pozicijaY+65)
                            print("Slobodan potez O je moguc na poziciji"+str(PozicijaX)+" "+str(pozicijaY))
                            pozicijaY=ord(p)-65   
                           # Upisi(prva_Matrica)            
                            return False
                brojac+=1
        PozicijaX+=1  


  


    print("Kraj igre")
    return True
    
#drugi deo 

def PromenaStanja(): #zadate vrednosti: potez i stanje na tabli
    n1=n
    m1=m
    x=0
    y=0
    kopijaMatrice=[[[None] for x in range(n1)]for x in range(m1)] #na svim poljima none
    while(x<n1):
        while(y<m1):
            kopijaMatrice[x][y]==prva_Matrica[x][y]
            y+=1
        x+=1
    Upisi(kopijaMatrice) #formira se novo stanje
    #proveriti:
    while(x<n1):
        while(y<m1):
            prva_Matrica[x][y]==kopijaMatrice[x][y]
            y+=1
        x+=1
    showTable(kopijaMatrice) #vraća se matrica sa novim potezom


def NoviPotez(xv, ov, prva_Matrica, naPotezu,vrsta,kolona):
    novi_potez = {
    "xValue": xv,
    "oValue": ov,
    "matrica": [x.copy() for x in prva_Matrica],
    "na_potezu": naPotezu,
    "broj": int(vrsta+1),
    "slovo": chr(kolona+65)
    }
    br=(novi_potez["broj"])
    slovo=novi_potez["slovo"]    
    sl=slovo.upper()
    if(novi_potez["naPotezu"]==0):
        element="X"
    elif(novi_potez["naPotezu"]==1):
        element="O"


    proveraTF=provera(element,br,sl)
    if(proveraTF):
        Abc=65
        y=ord(sl)-Abc
        kolNum=n
        pratiMatricu=0
        while(kolNum!=0):
            if(kolNum==br):
                if(novi_potez["naPotezu"]==0):                
                    element="X"
                    novi_potez["matrica"][pratiMatricu][y]=element
                    novi_potez["matrica"][pratiMatricu-1][y]=element
                    return novi_potez
                elif(novi_potez["naPotezu"]==1):
                    element="O"
                    novi_potez["matrica"][pratiMatricu][y]=element
                    novi_potez["matrica"][pratiMatricu][y+1]=element 
                    return novi_potez      
            pratiMatricu+=1
            kolNum-=1
    else:
        print("GRESKA")


def proceni_stanje(xv, ov):
    global naPotezu

    if(naPotezu):
        if(xv == 0):
            return 999
        if(ov == 0):
            return -999
        ret = xv - ov/6
    else:
        if(ov == 0):
            return 999
        if(xv == 0):
            return -999
        ret = ov - xv/6
    return ret

def nova_stanja(xv, ov, prva_Matrica, naPotezu):
    Lista = list()
    for row in range(0, n):
        for col in range(0, m):
            ns = NoviPotez(xv, ov, prva_Matrica, naPotezu,row,col)
            if(ns):
                Lista.append(ns)
    return Lista

def CovekProtivRacunara():
    global naPotezu, prva_Matrica, xv, ov
    showTable(prva_Matrica)

    while(Kraj(naPotezu)==0):
        if(naPotezu=="X"):
            Upisi(prva_Matrica)
            showTable(prva_Matrica)
        else:
            state = max_value(xv, ov, prva_Matrica, naPotezu,3,[xv, ov, prva_Matrica, naPotezu,-9999],[xv, ov, prva_Matrica, naPotezu,9999])[0]
            p = {
            "broj": state["broj"],
            "slovo": state["slovo"]
            }
            
            UpisiRacunar(prva_Matrica,p)
            showTable(prva_Matrica)
    return True

def max_value(xv, ov, prva_Matrica, naPotezu,dubina,alpha,beta):

    lista_novih_stanja = nova_stanja(xv, ov, prva_Matrica, naPotezu)
    if(dubina == 0 or len(lista_novih_stanja) == 0):
        return (xv, ov, prva_Matrica, naPotezu,proceni_stanje(xv, ov))
    else:
        for s in lista_novih_stanja:
            alpha = max(alpha,min_value(s,dubina-1,alpha,beta), key = lambda x: x[1])
            if(alpha[1] >= beta[1]):
                return beta
    return alpha

def min_value(xv, ov, prva_Matrica, naPotezu,dubina,alpha,beta):

    lista_novih_stanja = nova_stanja(xv, ov, prva_Matrica, naPotezu)
    if(dubina == 0 or len(lista_novih_stanja) == 0):
        return (xv, ov, prva_Matrica, naPotezu,proceni_stanje(xv, ov))
    else:
        for s in lista_novih_stanja:
            beta = min(beta,max_value(s,dubina-1,alpha,beta), key = lambda x: x[1])
            if(beta[1] <= alpha[1]):
                return alpha
    return beta
startGame()
