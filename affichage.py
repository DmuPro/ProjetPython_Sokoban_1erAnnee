from upemtk import *
from main import *

################################################# Fonction Affichage ###########################################################################
def ready():
	'''
	crée la fenêtre
	'''
	texte(dimension_fenetre//2,dimension_fenetre//2,"Cliquez sur une touche !","red","center")
	attente_touche()

def longueur(M):
	return len(M)*taille_case

def largeur(M):
	return len(M[0])*taille_case

def affiche_case(i,j,couleur):
	'''
	crée un rectangle avec comme paramètre des coordonées et une couleur
	'''
	c=list((i,j))
	rectangle(c[0]*taille_case,c[1]*taille_case,c[0]*taille_case+(taille_case-1),c[1]*taille_case+(taille_case-1),couleur,couleur)


def affiche_caisse(M):
	'''
	affiche les caisses en marron
	'''
	m= len(M)
	n=len(M[0])
	for i in range (m):
		for j in range(n):
			if M[i][j] == "B":
				affiche_case(i,j,'brown')

def affiche_petite_case(i,j,couleur):
	c=list((i,j))
	rectangle(c[0]*taille_case+10 ,c[1]*taille_case+10  ,c[0]*taille_case+(taille_case-1)-10,c[1]*taille_case+(taille_case-1)-10,couleur,couleur)

def affiche_cle(M):
	'''
	affiche les clés en orange
	'''
	m= len(M)
	n=len(M[0])
	for i in range (m):
		for j in range(n):
			if M[i][j] == "K":
				affiche_petite_case(i,j,"orange")
def affiche_porte (M) :
	'''
	affiche les portes
	'''
	m= len(M)
	n=len(M[0])
	for i in range (m):
		for j in range(n):
			if M[i][j] == "D":
				affiche_case(i,j,'blue')

def affiche_mur (M):
	"""
	affiche le mur en noir 
	"""
	m= len(M)
	n=len(M[0])
	for i in range (m):
		for j in range(n):
			if M[i][j] == "M":
				affiche_case(i,j,'black')


def affiche_target (M):
	'''
	affiche les cibles en rouge
	'''
	m= len(M)
	n=len(M[0])
	for i in range (m):
		for j in range(n):
			if M[i][j] == "T":
				affiche_case(i,j,'red')

def affiche_gardien (M):
	'''
	affiche le gardien en jaune
	'''
	m= len(M)
	n=len(M[0])
	for i in range (m):
		for j in range(n):
			if M[i][j] == "S":
				affiche_case(i,j,'yellow')
def affiche_caisse_sur_target (M,A):
	'''
	affiche les caisses qui sont sur les cibles en vert
	'''
	m= len(A)
	n=len(A[0])
	for i in range (m):
		for j in range(n):
			if A[i][j] == "T" :
				if M[i][j] == "B":
					affiche_case(i,j,'green')

def retablir_target (M,A):
	'''
	retablie les target qui ont disparus
	'''
	m = len(A)
	n= len(A[0])
	for i in range (m):
		for j in range(n):
			if A[i][j] =="T":
				if M[i][j] == "S" or M[i][j] =="B":
					pass
				elif M[i][j] == "." :
					M[i][j] = "T"
	return M

def affichage(terrain,direction,memo,compteur):
	'''
	affiche tous les éléments du jeu
	'''
	affiche_gardien(terrain)
	affiche_caisse(terrain)
	affiche_mur(terrain)
	affiche_cle(terrain)
	gardien_sur_cle(terrain,direction)
	affiche_porte(terrain)
	affiche_target(terrain)
	affiche_target(terrain)
	affiche_caisse_sur_target(terrain,memo)
	retablir_target(terrain,memo)


def menu():
	cree_fenetre(500,500)
	while True :
		ev = donne_evenement()
		tev = type_evenement(ev)
		texte(10,10,"SOKOBAN",couleur="black",taille=30,police = "Courier")
		texte(10,40,"par Tony PEREIRA et Davy MU",couleur="black",taille=12,police= "Courier")
		rectangle(10,200,490,110,"blue")
		rectangle(10,300,490,210,"blue")
		rectangle(10,400,490,310,"blue")
		texte(45,130,"Nouvelle partie",couleur="blue",taille=35,police = "Courier")
		texte(150,230,"Charger",couleur="blue",taille=35,police = "Courier")
		texte(150,330,"Quitter",couleur="blue",taille=35,police = "Courier")
		clic = attente_clic_ou_touche()
		if clic[2] == "ClicGauche":
			if 490>clic[0]>10 and 200>clic[1]>110:
				n="cn"
				break
		if clic[2] == "ClicGauche":
			if 490>clic[0]>10 and 400>clic[1]>310:
				n="q"
				break
		if 490>clic[0]>10 and 300>clic[1]>210:
				n ="c"
				break
		mise_a_jour()
	ferme_fenetre()
	return n
	

def choix_niv ():
	cree_fenetre(500, 500)
	while True :
		ev = donne_evenement()
		tev = type_evenement(ev)
		texte(10,10,"Choisissez votre niveau : ",couleur="black",taille=12,police = "Courier")
		affiche_petite_case(3,0.5,"white")
		affiche_petite_case(3,1.5,"yellow")
		affiche_petite_case(3,2.5,"orange")
		affiche_petite_case(3,3.5,"green")
		affiche_petite_case(3,4.5,"blue")
		affiche_petite_case(3,5.5,"brown")
		affiche_petite_case(3,6.5,"black")
		texte(200,40,"Level 1",couleur="black",taille=12,police = "Courier")
		texte(200,90,"Level 2",couleur="black",taille=12,police = "Courier")
		texte(200,140,"Level 3",couleur="black",taille=12,police = "Courier")
		texte(200,190,"Level 4",couleur="black",taille=12,police = "Courier")
		texte(200,240,"Level 5",couleur="black",taille=12,police = "Courier")
		texte(200,290,"Level 6",couleur="black",taille=12,police = "Courier")
		texte(200,340,"Level 7",couleur="black",taille=12,police = "Courier")
		rectangle(10,480,490,420,"blue")
		texte(160,425,"Retour",couleur="blue",taille=35,police = "Courier")
		clic = attente_clic_ou_touche()
		if clic[2] == "ClicGauche":
			if 190>clic[0]>160 and 65>clic[1]>35:
				n ="Level1"
				break
			if 190>clic[0]>160 and 115>clic[1]>85:
				n ="Level2"
				break
			if 190>clic[0]>160 and 165>clic[1]>135:
				n ="Level3"
				break
			if 190>clic[0]>160 and 215>clic[1]>185:
				n ="Level4"
				break
			if 190>clic[0]>160 and 265>clic[1]>235:
				n ="Level5"
				break
			if 190>clic[0]>160 and 315>clic[1]>285:
				n ="Level6"
				break
			if 190>clic[0]>160 and 365>clic[1]>335:
				n ="Level7"
				break
			if 490>clic[0]>10 and 480>clic[1]>420:
				n ="r"
				break
		mise_a_jour()
	ferme_fenetre()
	return n
################################################################################################################################################
################################################################################################################################################

