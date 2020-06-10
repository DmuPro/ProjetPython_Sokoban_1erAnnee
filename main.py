from upemtk import *
from random import randint
from copy import *
from affichage import *
from fonction import *
import string
import sys
################################################################################################################################################
dimension_fenetre = 700
nb_cases = 10
assert((dimension_fenetre-200) % nb_cases==0)
taille_case = (dimension_fenetre-200) // nb_cases
################################################################################################################################################

def mise_a_jour_direction(direction):
	'''
	Lorsque l'on clic sur une touche définie renvoi la direction associée
	'''
	if direction=="Right":
		return "droite"
	if direction=="Left":
		return "gauche"
	if direction=="Down":
		return "bas"
	if direction=="Up":
		return "haut"

#######################################  Affichage  ############################################################################################
def affichage_texte(c_key,deplacement,M):
    '''
    affiche les textes
    '''
    longueur_M=longueur(M)
    largeur_M=largeur(M)
    texte(longueur_M,0,(titre(niveau)),couleur="black",taille= 12,police = "Courier")
    texte(0,largeur_M,("Commande:"),couleur="black",taille= 12,police = "Courier")
    texte(0,largeur_M*1.05,("Sauvegarde : s "),couleur="black",taille= 12,police = "Courier")
    texte(0,largeur_M*1.1,("Reset : r"),couleur="black",taille= 12,police = "Courier")
    texte(0,largeur_M*1.15,("Debug : d"),couleur="black",taille= 12,police = "Courier")
    texte(0,largeur_M*1.2,("Changer de niveau : n"),couleur="black",taille= 12,police = "Courier")
    texte(longueur_M,largeur_M*0.05,"Nombre de clé :",couleur="black",taille= 12,police="Courier")
    texte(longueur_M*1.31,largeur_M*0.05,c_key,couleur="black", taille = 12 , police ="Courier")
    texte(longueur_M,largeur_M*0.1,"Nombre de déplacement:",couleur="black",taille = 11,police = "Courier")
    texte(longueur_M*1.1,largeur_M*0.14,deplacement,couleur="black",taille = 16,police = "Courier")

def MENU():
	""" Gère l'affichage du Menu """

	while True :
		#####  Choisir le niveau  ######################################
		if menu() == "cn":
			niveau = choix_niv()
			if niveau != "r":
				cree_fenetre(dimension_fenetre,dimension_fenetre)
				ready()
				terrain = lire_f(niveau)
				memo = deepcopy(lire_f(niveau))
				return terrain,memo,niveau
		#####  Charge la sauvegarde  ###################################
		elif menu() == "c":
			cree_fenetre(dimension_fenetre,dimension_fenetre)
			ready()
			terrain = charger()
			niveau = "sauvegarde"
			memo = deepcopy(terrain)
			return terrain,memo,niveau
		#####  Quitter  ################################################
		elif menu() == "q":
			sys.exit(0)

#####################################################         PROGRAMME PRINCIPALE        #####################################################
if __name__ == "__main__" :
### Données du jeu ############################################################################################################################
	terrain,memo,niveau = MENU()
	direction=''
	condition = ''
	deplacement = 0

###############################################################################################################################################
############################################################   Controle du jeu   ##############################################################
###############################################################################################################################################
	variable=''
	tirer_c=''
	while True:
		efface_tout()
		c_key = compteur_cle(terrain,memo)
		c_key = porte_disparu(terrain,memo,c_key)
		affichage_texte(c_key,deplacement,terrain)
		ev = donne_evenement()
		tev = type_evenement(ev)
######## Debug #################################################################################################################################
		if condition==True:
			direction=debug()
			action_pousser(terrain,direction,c_key)
			deplacement +=1
			texte(300,550,"Debug Activé !",couleur="red",taille= 30,police = "Courier")
		if tev == "Touche":
			tev=touche(ev)
			if tirer_c:
				if tev=="Right" or tev=="Left" or tev=="Up" or tev=="Down":
					direction=mise_a_jour_direction(tev)
					action_tirer(terrain,direction,c_key)
			if tev=="d":
				if condition == True:
					condition = False
				else:
					condition = True
############Contrôle des direction #############################################################################################################
			elif tev=="Right" or tev=="Left" or tev=="Up" or tev=="Down":
				if tirer_c!=True:
					direction=mise_a_jour_direction(tev)
					deplace_caisse(terrain,direction,c_key)
					deplace_gardien(terrain,direction,c_key)
					direction=''
					deplacement +=1
########### Reset ##############################################################################################################################
			elif tev=="r":
				terrain=deepcopy(memo)
############ Sauvegarde ########################################################################################################################
			elif tev=="s":
				sauvegarde(terrain)
############ Changer de niveau #################################################################################################################
			elif tev=="n":
				ferme_fenetre()
				terrain,memo,niveau = MENU()
				direction=''
				condition = ''
				deplacement = 0
			elif tev=="t":
				if tirer_c != True:    
					tirer_c=tirer_caisse(terrain)
				else:
					tirer_c=False
######## Véifie si le joueur à gagné ############################################################################################################
		if toute_caisse_sur_target(terrain,memo)== True :
			texte(300,550,("Gagné"),couleur="red",taille= 30,police = "Courier")
			attente_touche()
			ferme_fenetre()
			terrain,memo,niveau = MENU()
			direction=''
			condition=''
			deplacement = 0
		affichage(terrain,direction,memo,c_key)
		mise_a_jour()


########################################################         FIN PROGRAMME          ##########################################################
