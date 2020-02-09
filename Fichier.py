# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:59:59 2020

@author: elouahas
"""
from Arbre import Arbre

##############################################################################
###########################     CLASSE FICHIER       #########################
##############################################################################
class Fichier:
    
    def __init__(self,fichier):
        self.fichier=fichier #fichier texte qui va être compressé
        self.listeAlpha_freq=self.alpha_freq() #liste des tuples (char + fréqu)
        self.listeArbre=[] #liste des arbres initialisée à vide 

###############################################################################
##                                 ETAPE 1                                   ## 
##       Détermination de l’alphabet et des fréquences de caractères         ##        
        
#Méthode qui retourne l'alphabet du fichier (dans l'ordre croissant 
#des fréquences et par ordre de codage des caractères ASCII)
#avec leurs fréquences (en appelant la méthode freq() ) 

    def alpha_freq(self):
    #on ouvre un fichier texte:
        fichier = open(self.fichier + ".txt",'r') #r: fichier ouvert en lecture
   
    #création de la liste qui va contenir les tuples ((char + fréqu)):
        liste_finale=[] #initialisée à vide 
    #création d'une liste intermédiaire:   
        liste_new=[] #idem
        
    #on parcourt chaque ligne du fichier texte:
        for ligne in fichier:
            
        #ainsi que tous les caractères de chaque ligne:
            for char in ligne:
                
            #si le caractère de la ligne n'est pas dans la nouvelle liste
                if char not in liste_new:
                    
                #alors ajouter ce charactère dans la nouvelle liste 
                    liste_new.append(char)
                    
                #on appelle la méthode freq() qui va calculer 
                #le nombre d'apparition de chaque caractère:       
                    freq=self.freq(char) 
                                      
                #on ajoute ensuite dans la liste de base la fréquence des char:
                    liste_finale.append((freq,char)) #double (()) car tuple 
                    
        print("alphabet dans l'ordre croissant: ",sorted(liste_finale))
        
        #on crée un fichier texte de description de l’alphabet 
        #avec les fréquences des caractères:
        with open(self.fichier + "_freq.txt",'w') as f: #w:Ouvert en écriture
            
        #la 1ere ligne du fichier description indiquera le nombre total de char
            f.write("Nombre de caractère:"
                    +str(len(liste_finale))+"\n") #\n retour à la ligne
            
        #pour chaque caractère de la liste finale trier dans l'ordre croissant:
            for c in sorted(liste_finale):
                #écrire dans le fichier description le char avec sa fréq
                f.write(str(c)+"\n") 
            
        #on ferme le fichier donné par mesure de sécurité: 
        fichier.close   
        
        #et on retourne l'alphabet dans l'ordre croissant:
        return sorted(liste_finale)
    
###############################################################################

#la méthode suivante est appelée dans alpha_freq()           
#Méthode qui retourne la fréquence d'apparition de chaque caractère:   
        
    def freq(self,charactere):
    #on ouvre le fichier texte donné:
        fichier=open(self.fichier + ".txt",'r')
        
    #on initialise le compteur de la frequence des charactères à 0:
        cpt=0
    
    #on parourt chaque ligne du fichier:
        for ligne in fichier:
            
        #et chaque charactères de ces lignes:
            for char in ligne:
                
        #si le charactère de la ligne est le même que celui passé en paramètre:
                if char==charactere:
                
                #alors on incrémente de 1 le compteur de fréquence
                    cpt=cpt+1 
                    
     #on ferme le fichier texte ouvert en lecture:               
        fichier.close
        
    #et on retourne le compteur de fréquence:
        return cpt
        

###############################################################################
##                                 ETAPE 2                                   ## 
##                          Construction de l’arbre                          ## 
          
#Méthode qui créer tous les arbres/feuilles (tuple:char+freq) de l'arbre final
#pour chaque caractère de l'alphabet 

    def arbre_feuille(self):
        #pour chaque tuple(freq,char) de notre liste de l'alpha freq:
        for (freq,char) in self.listeAlpha_freq:
            #ajouter à la liste Arbre:
    # - la frequence correspondant à la "valeur" de l'arbre/feuille;
    # - le caractere correspondant au "label" de l'arbre/feuille; 
            self.listeArbre.append(Arbre(freq,char))
            
        #puis retourner la liste Arbre  
        return self.listeArbre
  
################################################################################

#Méthode qui va determiner les 2 Arbres (t1,t2) 
#de fréquence minimale t1.freq <= t2.freq

    def arbre(self):
    
    #le 1er arbre :
        arbre1=self.listeArbre[0]#le plus petit 
    #le 2eme arbre :
        arbre2=self.listeArbre[1]#le deuxième plus petit         
        
    #on crée un arbre qui va additionner la fréq des deux arbres/feuilles
    #et qui va mettre en fils droit l'arbre2 et en fils gauche l'arbre3
        arbre=Arbre(valeur=arbre1.valeur+arbre2.valeur,
                    label='',fils_droit=arbre2,fils_gauche=arbre1)
        
    #on supprime ensuite les deux arbres de gauche de la listeArbre
        self.listeArbre.pop(1)
        self.listeArbre.pop(0)
        
    #on appelle la méthode index() qui retourne l'index de l'arbre présent dans la liste en fct de sa valeur et label
        index=self.RecupIndexNewArbre(arbre) 
        
    #que l'on va utiliser pour ajouter l'arbre à 
    #la bonne place dans la liste Arbre:
        self.listeArbre[index:index]=[arbre] 
        
################################################################################

#Méthode qui va créer l'arbre final t avec les sous arbres t1 et t2 
#respectivement gauche et droite, avec t.freq=t1.freq+t2.freq
#Jusqu’à ce qu’il ne reste plus qu’un seul arbre

    def arbreFinal(self):
        
        #on appel la fonction qui crée les feuilles 
        self.arbre_feuille()
        
#et tant que dans la listeArbre il ne reste plus qu'un element 
#l'arbre n'est pas aboutit
        while len(self.listeArbre) != 1:
            self.arbre()


################################################################################

#Méthode qui va permettre de mettre au bon endroit l'arbre dans la listeArbre

    def RecupIndexNewArbre(self,arbre):
        liste=[] #on initialise la liste à vide 
        
       #pour chaque element de la listeArbre: 
        for element in self.listeArbre:
        #on ajoute tous les arbres dans la liste  
            liste.append((element.valeur,element.label))
            
        #et on rajoute le nouvel arbre créer dans la liste 
        liste.append((arbre.valeur,arbre.label))
        
        #on ordonne la liste:
        listeOrdonnee=sorted(liste)
        print("liste ordo AKA l'arbre:",listeOrdonnee)
        
#on retourne l'index de l'arbre présent dans la liste en fct de sa valeur et label
        return listeOrdonnee.index((arbre.valeur,arbre.label))
        

###############################################################################
##                                 ETAPE 3                                   ## 
##                             Codage du texte                               ## 
            
#Méthode qui va créer un dictionnaire pour faciliter 
#le codage du texte qui va suivre 
        
    def dico_alpha(self):
        
        dico={}
    #pour chaque tuple de la listeAlpha:
        for (freq,char) in self.listeAlpha_freq:
            
      #ajouter dans le dico le code/chemin de chaque char       
            dico[char]=self.listeArbre[0].profondeur(char)
        #print("dico:",dico)

        return dico
    
###############################################################################    

#Méthode pour afficher le code bianire de chaque caractère du fichier texte
        
    def afficherCode(self):
    #on ouvre le fichier texte donné :
        fichier=open(self.fichier + ".txt",'r')
        
    #on appelle la méthode dico_alpha() :
        dico=self.dico_alpha()
    
    #on crée une liste vide qui contiendra les codes de chaque char 
        liste=[]
        
    #on parcourt chaque ligne du fichier:
        for ligne in fichier:            
        #ainsi que tous les charactères de chaque ligne: 
            for char in ligne:
                #on ajoute à la liste le code de chaque char
                    liste.append(dico[char])
                    
        resultat= ''
    #on parcourt les elements de la liste: 
        for element in liste :
           #on concatene le résultat avec le string de l'element:
            resultat = resultat + str(element)
            #print("le résultat de la concatenation sans 0 en plus:",resultat)

    #si le nombre d'element de resultat (concatenation bianire) 
    #n'est pas un multiple de 8: 
        if (len(resultat)%8)==0:
            #alors séparer le resulat par octet
            resultFinal = [resultat[i:i+8] for i in range(0, len(resultat), 8)]
        
    #si ce n'est pas un multiple
        else : 
        #tant que le nombre d'element de resultat n'est pas un multiple de 8
            while(len(resultat)%8)!=0:
                #ajoute un 0 à droite du resultat
                resultat=resultat+'0'
                
       #et séparer le resulat par octet :   
            resultFinal = [resultat[i:i+8] for i in range(0, len(resultat), 8)]
            
        #print("séparation par octet",resultFinal)
        
        
        resultat2= ''
    #on parcourt les éléments de la liste resultat final: 
        for element2 in resultFinal :
        #et on concatene:
            resultat2 = resultat2 + str(element2)
        #print("le résultat de la concatenation finale:",resultat2)
        
            
    #tx de compression 
        longueurRes2=len(resultat2)
        print("taux de compression:",self.tx_compression(longueurRes2))
    ##    
        
#Méthode pour convertir la chaîne binaire de longueur quelconque 
#en -> nombre entier positif
        
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
                            
###############################################################################
##                                 ETAPE 4                                   ## 
##                    Détermination du taux de compression                   ## 
    

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
            
###############################################################################
###############################################################################
         

