# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:59:59 2020

@author: elouahas
"""
from Arbre import Arbre
#from str import join
##############################################################################
###########################     CLASSE FICHIER       #########################
##############################################################################
class Fichier:
    
    def __init__(self,fichier):
        self.fichier=fichier 
        self.listeAlpha_freq=self.alpha_freq()
        self.listeArbre=[]

###############################################################################
##             ETAPE 2              ##     
        
#Méthode qui retourne l'alphabet du fichier dans l'ordre croissant 
#avec les fréquences des charactères (en utilisant la méthode d'après) 

    def alpha_freq(self):
    #on ouvre le fichier texte donné
        fichier = open(self.fichier + ".txt",'r') #r= fichier ouvert en lecture
            
        liste_base=[]
        liste_new=[]
        
    #on parourt chaque ligne du fichier
        for ligne in fichier:
            
        #ainsi que tous les charactères par ligne 
            for char in ligne:
                
            #si le charactère de la ligne n'est pas dans la nouvelle liste
                if char not in liste_new:
                    
                #alors ajouter ce charactère dans la nouvelle liste 
                    liste_new.append(char)
                    
                #on appelle la méthode freq qui va calculer 
                #le nombre d'apparition de chaque caractère       
                    freq=self.freq(char) 
                    
                    
                #on ajoute ensuite dans la liste de base la fréquence des char
                    liste_base.append((freq,char)) #double (()) car tuple 

        
        #on crée un fichier de description de l’alphabet 
        #utilisé avec les fréquences de caractère:
        with open(self.fichier + "_freq.txt",'w') as f: #w= pour écrire 
            
            #la 1ere ligne du fichier indiquera le nombre de caractères 
            f.write(str(len(liste_base)) + "\n") #\n retour à la ligne
            
            #pour chaque caractère de la liste trier dans l'ordre croissant
            for c in sorted(liste_base):
                #écrire dans le nouveau fichier le char avec sa fréq
                f.write(str(c)+"\n") #avec un saut à la ligne
            
    
        #on ferme le fichier donné par sécurité 
        fichier.close   
        
        #et retourne l'alphabet dans l'ordre croissant
        return sorted(liste_base)
    
    
###############################################################################
            
#Méthode création du dico pour faciliter le codage 
        
    def dico_alpha(self):
        dico={}
        for (freq,char) in self.listeAlpha_freq:
            dico[char]=self.listeArbre[0].profondeur(char)
        return dico

        

###############################################################################
            
#Méthode qui retourne la fréquence d'apparition de chaque caractère       
    def freq(self,charactere):
    #on ouvre le fichier texte donné
        fichier=open(self.fichier + ".txt",'r')
        
    #on initialise le compteur de la frequence des charactères à 0
        cpt=0
    
    #on parourt chaque ligne du fichier
        for ligne in fichier:
            
        #et chaque charactères de ces lignes
            for char in ligne:
                
        #si le charactère de la ligne est le même que celui passé en paramètre
                if char==charactere:
                
                #alors on incrémente de 1 le compteur de fréquence
                    cpt=cpt+1 
                    
        fichier.close
        #on retourne le compteur 
        return cpt
    
###############################################################################

##             ETAPE 2              ##
        
#Méthode qui créer toutes les feuilles (tuple) de l'arbre 
#pour chaque caractère de l'alpha avec les freq associées   

    def feuille(self):
        #pour chaque tuple(freq,char) de notre liste de l'alpha freq 
        for (freq,char) in self.listeAlpha_freq:
            self.listeArbre.append(Arbre(freq,char))
        return self.listeArbre
            
################################################################################

#Méthode qui va créer les 2 Arbres (t1,t2) 
#de fréquence minimale t1.freq <= t2.freq
    def arbre(self):
        
        arbre1=self.listeArbre[0]#qui rpz le plus petit 
        arbre2=self.listeArbre[1]#et le plus grand
        
        #création de l'arbre avec la class Arbre
        #en créant d'abord le droit puis le gauche 
        arbre=Arbre(valeur=arbre1.valeur+arbre2.valeur,
                    label='',fils_droit=arbre2,fils_gauche=arbre1)
        
        #on enleve ensuite le deuxième et premier arbre de la liste
        self.listeArbre.pop(1)
        self.listeArbre.pop(0)
        
        #appel de la méthode index
        index=self.indexNewArbre(arbre) 
        
    #que l'on va utiliser pour ajouter l'arbre à la bonne place dans la liste 
        self.listeArbre[index:index]=[arbre] 
        
################################################################################

#Méthode pour les index

    def indexNewArbre(self,arbre):
        liste=[] 
        
        #pour chaque element de la liste 
        for element in self.listeArbre:
            #on ajoute les elements qui sont dans la listearbre dans la liste vide
            liste.append((element.valeur,element.label))
            
        #et on rajoute à la liste 
        liste.append((arbre.valeur,arbre.label))
        
        #on ordonne
        listeOrdonnee=sorted(liste)
        #print("liste ordo",listeOrdonnee)
        
#on retourne l'index de l'arbre présent dans la liste en fct de sa valeur et label
        return listeOrdonnee.index((arbre.valeur,arbre.label))
        
################################################################################

#Méthode qui va créer l'arbre final t avec t1 et t2 
#comme sous-arbres respectivement gauche et droite avec t.freq=t1.freq+t2.freq
#Jusqu’à ce qu’il ne reste plus qu’un seul arbre

    def arbreFinal(self):
        
        #on appel la fonction qui crée les feuilles 
        self.feuille()
        
#et tant que dans la listeArbre il ne reste plus qu'un element 
#l'arbre n'est pas aboutit
        while len(self.listeArbre) != 1:
            self.arbre()
        
        return self.listeArbre[0].profondeur("e")

################################################################################

##             ETAPE 3              ##

#Méthode pour afficher le code bianire de chaque char du fichier texte
        
    def afficherCode(self):
    #on ouvre le fichier texte donné
        fichier=open(self.fichier + ".txt",'r')
        dico=self.dico_alpha()
        liste=[]
    #on parcourt chaque ligne du fichier
        for ligne in fichier:            
        #ainsi que tous les charactères par ligne 
            for char in ligne:
                    #print(self.listeArbre[0].profondeur(char))
                    liste.append(dico[char])
                    
        #print("la liste des codes binaires :",liste)
                    
        resultat= ''
        for element in liste :
            resultat = resultat + str(element)
        #print("le résultat de la concatenation sans 0 en plus:",resultat)


    #si le nombre d'element de resultat (concatenation bianire) 
    #n'est pas un multiple de 8 alors 
        if (len(resultat)%8)==0:
            resultFinal = [resultat[i:i+8] for i in range(0, len(resultat), 8)]
            
        else : 
            while(len(resultat)%8)!=0:
                resultat=resultat+'0'
                
            resultFinal = [resultat[i:i+8] for i in range(0, len(resultat), 8)]
            
        #print("séparation par octet",resultFinal)
        
        
        resultat2= ''
        for element2 in resultFinal :
            resultat2 = resultat2 + str(element2)
        #print("le résultat de la concatenation finale:",resultat2)
        
        
        
    #tx de compression 
        longueurRes2=len(resultat2)
        print("tx de compression:",self.tx_compression(longueurRes2))
        
        
        #conversion chaîne binaire de longueur quelconque -> nombre entier positif
        listeDec=[]
        for element in resultFinal:
            listeDec.append(int(element,2))  
        #print("binaire to decimal",listeDec)
            
                
       #création du fichier final !! 
        with open(self.fichier + '_comp.bin', 'wb') as f: #wb= pour écrire en binaire

            for i in listeDec:     
                i_byte=(i).to_bytes(1,byteorder='big') #transforme str en byte  
                f.write(bytes(i_byte))   

                         
        fichier.close         
                
            
################################################################################
                
#Méthode qui va générer un fichier du texte compressé  

        # Ecrire des données binaires dans un fichier
        
    


################################################################################

##             ETAPE 4              ##
                

#Méthode qui va calculer le tx de compression 
    
    def tx_compression(self,longVolFinal):
        fichier = open(self.fichier + ".txt",'r') #r= fichier ouvert en lecture
        texte = fichier.read()
        volume_final=longVolFinal
        volume_initial=len(texte)*8 #*8 car chaque element est codé en octet
        
        print("volume_final:",volume_final)
        print("volume_initial:",volume_initial)
        
        
            
        tx= (1 - (volume_final/volume_initial) )  * 100 
        
        fichier.close()
        
        return tx
            
        
################################################################################

##             ETAPE 5              ##        
        
         
            
###############################################################################
########################             TEST          ############################
###############################################################################
        
#f=Fichier("extraitalice")
f=Fichier("alice")
#f=Fichier("textesimple")
#f=Fichier("bonjour")


#print("l'alphabet et ses fréquences:",f.alpha_freq())
f.alpha_freq()

#print("l'arbre:",f.arbreFinal())
f.arbreFinal()

print("le code binaire du fichier donné:")
f.afficherCode()







