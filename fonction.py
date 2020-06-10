from upemtk import *
from affichage import *
from main import *
import string

################################################################ Fonctionnalité ################################################################

def deplace_gardien (M,direction,compteur):
	'''
	renvoie la matrice après un pas de déplacement du gardien dans la direction renseignée
	'''
	m= len(M)
	n=len(M[0])
	for i in range (m):
		for j in range(n):
			if M[i][j] == "S":
				if direction=='haut':
					if M[i][j-1] == "." or M[i][j-1] == "T" or M[i][j-1]=="K":
						M[i][j-1],M[i][j]=M[i][j],"."
						return M
					elif M[i][j-1] == "D":
						if compteur > 0 :
							M[i][j-1],M[i][j]=M[i][j],"."
							return M
				if direction=='bas':
					if M[i][j+1] == "." or M[i][j+1] == "T" or M[i][j+1]=="K":
						M[i][j+1],M[i][j]=M[i][j],"."
						return M
					elif M[i][j+1] == "D":
						if compteur > 0 :
							M[i][j+1],M[i][j]=M[i][j],"."
							return M
				if direction=='gauche':
					if M[i-1][j] == "." or M[i-1][j] == "T" or M[i-1][j]=="K":
						M[i-1][j],M[i][j]=M[i][j],"."
						return M
					elif M[i-1][j] == "D":
						if compteur > 0 :
							M[i-1][j],M[i][j]=M[i][j],"."
							return M
				if direction=='droite':
					if M[i+1][j] == "." or M[i+1][j] == "T" or M[i+1][j]=="K":
						M[i+1][j],M[i][j]=M[i][j],"."
						return M
					elif M[i+1][j] == "D":
						if compteur > 0 :
							M[i+1][j],M[i][j]=M[i][j],"."
							return M
				return M

def gardien_sur_cle (M,direction):
	'''
	renvoie la matrice lorsque le gardien se déplace sur une clé
	'''
	m= len(M)
	n=len(M[0])
	for i in range (m):
		for j in range(n):
			if M[i][j] == "K":
				if direction=='haut':
					if M[i][j-1] == "S":
						M[i][j]="."
						return M
				if direction=='bas':
					if M[i][j+1] == "S":
						M[i][j]="."
						return M
				if direction=='gauche':
					if M[i-1][j] == "S":
						M[i][j]="."
						return M
				if direction=='droite':
					if M[i+1][j] == "S":
						M[i][j]="."
						return M
				return M

def deplace_caisse(M, direction,compteur):
	'''
	renvoie la matrice avec les caisses après que le gardien l'ai poussé
	'''
	m= len(M)
	n=len(M[0])
	for i in range (m):
		for j in range(n):
			if M[i][j] == "B":
				if direction=='haut':
					if M[i][j-1] == "D":
						if compteur == 0 :
							return M
					elif M[i][j-1]!="M" and M[i][j+1]=="S":
						M[i][j-1],M[i][j]=M[i][j],M[i][j-1]
						return M
				if direction=='bas':
					if M[i][j+1] == "D":
						if compteur == 0 :
							return M
					elif M[i][j+1]!="M" and M[i][j-1]=="S":    
						M[i][j+1],M[i][j]=M[i][j],M[i][j+1]
						return M
				if direction=='gauche':
					if M[i-1][j] == "D":
						if compteur == 0 :
							return M
					elif M[i-1][j]!="M" and M[i+1][j]=="S":   
						M[i-1][j],M[i][j]=M[i][j],M[i-1][j]
						return M
				if direction=='droite':
					if M[i+1][j] == "D":
						if compteur == 0 :
							return M
					elif M[i+1][j]!="M" and M[i-1][j]=="S":  
						M[i+1][j],M[i][j]=M[i][j],M[i+1][j]
						return M
	return M

def tirer(M, direction,compteur):
    '''
    renvoie la matrice avec les caisses après que le gardien l'ai tiré
    '''
    m= len(M)
    n=len(M[0])
    for i in range (m):
        for j in range(n):
            if M[i][j] == "S":            
                if direction=='haut':
                    if j+2<n:
                        if M[i][j+2]=="B" and M[i][j+1] != "M":
                            M[i][j+2],M[i][j+1]=M[i][j+1],M[i][j+2] 
                            return M
                if direction=='bas':
                    if j-2>=0:
                        if M[i][j-2]=="B" and M[i][j-1] != "M":    
                            M[i][j-2],M[i][j-1]=M[i][j-1],M[i][j-2]
                            return M
                if direction=='gauche':
                    if i+2<m:
                        if M[i+2][j]=="B" and M[i+1][j] != "M":   
                            M[i+2][j],M[i+1][j]=M[i+1][j],M[i+2][j]
                            return M
                if direction=='droite':
                    if i-2>=0:
                        if M[i-2][j]=="B" and M[i-1][j] != "M": 
                            M[i-2][j],M[i-1][j]=M[i-1][j],M[i-2][j]
                            return M
    return M

def tirer_caisse(M):
	'''
	Renvoie True lorsque qu'une caisse est à proximité du gardien
	'''
	m= len(M)
	n=len(M[0])
	for i in range (m):
		for j in range(n):
			if M[i][j] == "S":
				if M[i][j-1] == "B":
					return True
				if M[i][j+1] == "B":
					return True
				if M[i-1][j] == "B":
					return True
				if M[i+1][j] == "B":
					return True

def toute_caisse_sur_target (M,A):
	'''
	renvoie True si toutes les caisses sont sur les cibles
	'''
	m = len(A)
	n = len(A[0])
	for i in range (m):
		for j in range(n):
			if A[i][j] == "T":
				if M[i][j] != "B" :
					return False
	return True

def compteur_cle (M,A) :
	'''
	renvoie le nombre de clé que le gardien à pris
	'''
	c =0
	m = len(A)
	n = len(A[0])
	for i in range (m):
		for j in range(n):
			if A[i][j] =="K":
				if M[i][j] != "K" :
					c+=1
	return c

def porte_disparu (M,A,c):
	'''
	renvoie le nombre de clé restante après que le gardien ai ouvert une porte
	'''
	m = len(A)
	n = len(A[0])
	for i in range (m):
		for j in range(n):
			if A[i][j] =="D":
				if M[i][j] != "D" :
					c-=1
	return c

def debug():
	'''
	renvoie une direction aléatoire
	'''
	v_aleatoire=randint(1,4)
	if v_aleatoire==1:
		return "haut"
	if v_aleatoire==2:
		return "bas"
	if v_aleatoire==3:
		return "gauche"
	if v_aleatoire==4:
		return "droite"


def lire_f (fichier):
	A=[]
	A1=[]
	l = 0
	c = 0
	with open (fichier,"r") as f :
		e=f.readline()
		for e in f.readlines():
			for i in range((len(e))):
				if e[i] in string.whitespace:
					A1.append(A)
					A=[]
				elif e[i] != "\n":
					A.append(e[i])
	return A1

def titre (fichier):
	'''
	renvoie le titre du fichier ( Le titre du niveau )
	'''
	with open (fichier,"r") as f :
		for l in f.readlines():
			T = l.strip()
			return l

def sauvegarde(M):
	'''
	sauvegarde la matrice lorsque le joueur appuie sur s
	'''
	with open("sauvegarde","w") as fichier:
		Matricestr=''
		for i in range(len(M)):
			for j in range(len(M[0])):
				Matricestr+=M[i][j]
			Matricestr+="\n"
		fichier.write("Sauvegarde\n"+Matricestr)
  
def charger():
	'''
	charge la matrice sauvegardée
	'''
	with open("sauvegarde","r") as fichier:
		terrain=lire_f("sauvegarde")
	return terrain

def action_pousser(terrain,direction,c_key):
    deplace_caisse(terrain,direction,c_key)
    deplace_gardien(terrain,direction,c_key)

def action_tirer(terrain,direction,c_key):
    deplace_gardien(terrain,direction,c_key)
    tirer(terrain,direction,c_key)
###############################################################################################################################################

