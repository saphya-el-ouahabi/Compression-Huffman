# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:59:59 2020

@author: elouahas
"""

###############################################################################
#########################      CLASSE ARBRE       #############################        
###############################################################################   

class Arbre:

    def __init__(self,valeur,label,fils_droit=None,fils_gauche=None):
        self.label=label
        self.valeur=valeur #frequence du char
        self.fils_droit=fils_droit
        self.fils_gauche=fils_gauche 
 
###############################################################################
##                                 ETAPE 3                                   ## 
##                             Codage du texte                               ## 
          
#méthode qui parcourt l'arbre depuis son noeud racine "en profondeur":
#Le code d’un caractère est alors la concaténation des étiquettes 
#rencontrées (0:gauche ou 1:droite) en partant de la racine et en descendant 
#jusqu’à la feuille contenant ce caractère
        
    def profondeur(self,char,code=""):
    
    #si le caractère passé en paramètre est le meme que celui du noeud:
        if char == self.label:
        #alors on retourne le code 
            return code
        
    #si le caractère passé en paramètre n'est pas le meme:
        else:
            #alors:
            #si le fils gauche du noeud existe:
            if self.fils_gauche != None:
                if self.fils_gauche.profondeur(char,code+"0") != None:
                    #on ajoute 0 à droite du code du noeud 
                    return self.fils_gauche.profondeur(char,code+"0")
                
            #si le fils droit du noeud existe:    
            if self.fils_droit != None:
                if self.fils_droit.profondeur(char,code+"1") != None:
                    #on ajoute 1 à droite du code du noeud 
                    return self.fils_droit.profondeur(char,code+"1")
                
                






