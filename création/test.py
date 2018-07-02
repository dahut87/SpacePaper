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


def lance():
    return randint(1,6)+randint(1,6)

def getresult(de,liste):
    for seuil,result in liste.iteritems():
        seuils = getseuil(seuil)
        if de>=seuils[0] and de<=seuils[1]:
            return result

lancer=1000000
prob=0
print "Evaluations statistiques sur %d lances" % lancer
etoiles={'2':'Naine Brune','6-7':'Naine Rouge','8-9':'Naine Jaune','3-4':'Geante rouge','5':'Geante bleue','11':'Super geante R','12':'Etoile double','10':'Trou noir'}
types={
'Naine Brune': {'2':'Tellurique','10-12':'Gazeuse','5-7':'Gelee','4':'Oceanique','8-9':'Sterile','3':'Lave','0':'Vivante'},
'Naine Rouge': {'11-12':'Tellurique','9-10':'Gazeuse','6-7':'Gelee','8':'Oceanique','2-4':'Sterile','5':'Lave','0':'Vivante'},
'Naine Jaune': {'7-8':'Tellurique','10':'Gazeuse','9':'Gelee','5-6':'Oceanique','3-4':'Sterile','11-12':'Lave','2':'Vivante'},
'Geante rouge': {'10-12':'Tellurique','5-6':'Gazeuse','3':'Gelee','4':'Oceanique','9':'Sterile','7-8':'Lave','2':'Vivante'},
'Geante bleue': {'12':'Tellurique','5-6':'Gazeuse','3':'Gelee','4':'Oceanique','7-8':'Sterile','9-11':'Lave','2':'Vivante'},
'Super geante R': {'11':'Tellurique','2-4':'Gazeuse','0':'Gelee','12':'Oceanique','5':'Sterile','6-10':'Lave','0':'Vivante'},
'Etoile double': {'2-4':'Tellurique','5-6':'Gazeuse','8-9':'Gelee','10':'Oceanique','7':'Sterile','11-12':'Lave','0':'Vivante'}}

nombres={
'Naine Brune': {'5-8':1,'9-11':2,'4':3,'3':4,'2':5,'12':6},
'Naine Rouge': {'11-12':1,'5-6':2,'7-8':3,'9-10':4,'3-4':5,'2':6},
'Naine Jaune': {'12':1,'2-3':2,'4-5':3,'6-7':4,'8-9':5,'10-11':6},
'Geante rouge': {'8-9':1,'6-7':2,'2-5':3,'10-11':4,'12':5,'0':6},
'Geante bleue': {'6-7':1,'8-10':2,'2-5':3,'11-12':4,'0':5,'0':6},
'Super geante R': {'7-11':1,'2-6':2,'12':3,'0':4,'0':5,'0':6},
'Etoile double': {'2-3':1,'4-5':2,'6-7':3,'8-9':4,'10-11':5,'12':6}}
probabilite={}
allplanet=0
print "Verification des intervals..."
print "Recapitulatif \t %s" % (testdicelist(list(etoiles)))
for type in list(types):
    print "%s \t %s : %s" % (type,testdicelist(list(types[type])),testdicelist(list(nombres[type])))
raw_input("...")

for i in range(lancer):
    de=lance()
    result_etoile=getresult(de,etoiles)
    print "**************** \nDetermination etoile...%d : %s" % (de,result_etoile)
    prob="1."+result_etoile;
    if probabilite.has_key(prob):
        value=probabilite[prob]
        probabilite[prob]=value+1
    else:
        probabilite[prob]=1
    if result_etoile!="Trou noir":
        de=lance()
        result_nombre=getresult(de,nombres[result_etoile])
        print "Determination taille...%d : %s" % (de,result_nombre)
        prob="2."+str(result_nombre);
        if probabilite.has_key(prob):
            value=probabilite[prob]
            probabilite[prob]=value+1
        else:
            probabilite[prob]=1
        allplanet=allplanet+result_nombre
        for j in range(result_nombre):
            de=lance()
            result_type=getresult(de,types[result_etoile])
            print "       Determination type...%d : %s" % (de,result_type)
            prob="3."+result_type;
            if probabilite.has_key(prob):
                value=probabilite[prob]
                probabilite[prob]=value+1
            else:
                probabilite[prob]=1
        resultats=list(probabilite)
        resultats.sort()
print resultats
for i in range(len(resultats)):
    if resultats[i][0]=='3':
        proba=probabilite[resultats[i]]/float(allplanet)*100.0;
    else:
        proba=probabilite[resultats[i]]/float(lancer)*100.0;
    print "       Caracteristique %s : %d, %f" % (resultats[i],probabilite[resultats[i]],proba)







