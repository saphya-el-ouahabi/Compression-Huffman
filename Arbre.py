# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:59:59 2020

@author: elouahas
"""

#Arbre binaire

class Arbre:

    def __init__(self,valeur,label,fils_droit=None,fils_gauche=None):
        self.label=label
        self.valeur=valeur #frequence du char
        self.fils_droit=fils_droit
        self.fils_gauche=fils_gauche 
 
###############################################################################
#########################          GETTERS        #############################        
#méthode qui retourne l'étiquette d'un noeud (label)
    def get_content(self):
        return self.label

#méthode qui retourne la valeur d'un noeud    
    def get_valeur(self):
        return self.valeur
    
#méthode qui retourne les fils droit d'un noeud
    def get_fils_droit(self):
        return self.fils_droit.valeur
    
#méthode qui retourne les fils gauche d'un noeud
    def get_fils_gauche(self):
        return self.fils_gauche.valeur
    
#méthode qui retourne le noeud racine de l'arbre
#étant donné que le noeud racine est l'arbre
#alors il se retourne lui même
    def get_root(self):
        return self

###############################################################################
###############################################################################
        
#méthode qui parcourt l'arbre depuis son noeud racine "en profondeur"
#jusqu'au fils en partant du premier à gauche
#en affichant les labels de ces derniers
    def profondeur(self,char,code=""):
        
        if char == self.label:
            return code
        else:
            if self.fils_gauche != None:
                if self.fils_gauche.profondeur(char,code+"0") != None:
                    return self.fils_gauche.profondeur(char,code+"0")
                
            if self.fils_droit != None:
                if self.fils_droit.profondeur(char,code+"1") != None:
                    return self.fils_droit.profondeur(char,code+"1")
                
                






