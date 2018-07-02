from random import *

def proba2D6(seuil):
    liste = [1.0/36,2.0/36,3.0/36,4.0/36,5.0/36,6.0/36,5.0/36,4.0/36,3.0/36,2.0/36,1.0/36]
    try:
        index=seuil.index('-')
        bas=int(seuil[0:index])
        haut=int(seuil[index+1:])
    except:
        bas=haut=int(seuil)
    return sum(liste[bas-2:haut-1])

def getseuil(seuil):
    try:
        index=seuil.index('-')
        bas=int(seuil[0:index])
        haut=int(seuil[index+1:])
    except:
        bas=haut=int(seuil)
    return (bas,haut)

def lance():
    return randint(1,6)+randint(1,6)

def getresult(de,liste):
    for seuil,result in liste.iteritems():
        seuils = getseuil(seuil)
        if de>=seuils[0] and de<=seuils[1]:
            return result

def makedict():
    dict =  {}
    for i in range(2,13):
        for j in range(i+1,13):
            seuil=str(i)+'-'+str(j)
            proba=round(proba2D6(seuil),3)
            #print "%d-%d : %s %f" % (i,j,seuil,proba)
            if dict.has_key(proba):
                dict[proba].append(seuil)
            else:
                dict[proba]=[seuil]
    for i in range(2,13):
        seuil=str(i)
        proba=round(proba2D6(seuil),3)
        #print "%d-%d : %s %f" % (i,j,seuil,proba)
        if dict.has_key(proba):
            dict[proba].append(seuil)
        else:
            dict[proba]=[seuil]
    dict[0]=['0']
    return dict

def mini(liste):
    result=[]
    for i in range(len(liste)):
        result.append(liste[i][1])
    return result

def closeast(values,liste):
    final = []
    for i in range(len(values)):
        prop = []
        for j in range(len(liste)):
            prop.append((abs(values[i]-liste[j]),liste[j]))
        final.append(sorted(prop))   
    return final

def tester(liste):
    somme=sum(liste)
    if abs(somme-1.0)>0.001:
        print "ERREUUUUUUR : %f" % (somme)
        exit()

def least(liste,indices):
    mini=1
    column=-1
    for i in range(len(liste)):
         if liste[i][indices[i]][0]<mini:
            mini=liste[i][indices[i]][0]
            column=i
    return column

def testlist(liste,indices):
    sum=0
    for i in range(len(liste)):
         sum=liste[i][indices[i]][1]+sum
    return sum

def testdicelist(liste):
    full=[0]*11
    for i in range(len(liste)):
         if liste[i]!='0':
            seuils=getseuil(liste[i])
            #print seuils
            for j in range(seuils[0]-2,seuils[1]-1):
                if full[j]==0:
                    full[j]=1
                else:
                    return False
            #print full
    if sum(full)==11:
        return True
    else:
        return False

def returnlist(liste,indices):
    list=[]
    for i in range(len(liste)):
         list.append(liste[i][indices[i]][1])
    return list

def closeastlist(liste,resultats):
    indices=[0]*len(liste)
    near=closeast(liste,resultats)
    #print near
    while abs(testlist(near,indices)-1.0)>0.0011: 
        print "Somme:%f, proche:%d" % (abs(testlist(near,indices)-1.0),least(near,indices))
        print indices
        retenue=True
        for i in range(0,len(indices)):
             if retenue:
                 indices[i]=indices[i]+1
                 if indices[i]==len(resultats):
                        indices[i]=0
                        retenue=True
                 else:
                        break
        if len(resultats) in indices:
            print "impossible !"
            exit()
    #print "Somme:%f, proche:%d" % (testlist(near,indices),least(near,indices))
    list=returnlist(near,indices)
    return list

def brutlist(liste,dict):
    tester(liste)
    resultats=list(dict)
    resultats.sort()
    #print resultats
    liste=closeastlist(liste,resultats)
    print "Approche probabiliste"
    print liste
    proba=[]
    for i in range(len(liste)):
        proba.append(dict[liste[i]])
    print "Arrangements possibles"
    print proba
    #raw_input("...")
    indices=[0]*len(liste)
    test=[]
    for i in range(len(liste)):
            test.append(proba[i][indices[i]])
    print "Solutions"
    while True:
            if testdicelist(test):
                print test
            retenue=True
            for i in range(0,len(indices)):
                if retenue:
                    if i==len(indices)-1:
                        print "fin des solutions"
                        exit()
                    indices[i]=indices[i]+1
                    if indices[i]==len(proba[i]):
                        indices[i]=0
                        retenue=True
                    else:
                        break
            test=[]
            for i in range(len(liste)):
                test.append(proba[i][indices[i]])     
            #print test


import sys 
if len(sys.argv)<2:
    print "Manque argument: liste a atteindre"
    exit()
liste= sys.argv[1].split(",")
for i in range(len(liste)):
    liste[i]=float(liste[i])
dict=makedict()
#print dict
essai=brutlist(liste,dict)
print essai
