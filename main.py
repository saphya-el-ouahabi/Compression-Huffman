# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 08:58:06 2020

@author: elouahas
"""
from Fichier import  Fichier


###############################################################################
###########################            MAIN          ##########################
###############################################################################

if __name__ == '__main__':
    
    
    #fichier="extraitalice"
    fichier="alice"
    #fichier="bonjour"
    #fichier="textesimple"
    
    f=Fichier(fichier)
    
    f.arbreFinal()
    f.afficherCode()









        
