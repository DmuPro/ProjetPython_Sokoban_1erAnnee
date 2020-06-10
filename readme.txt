SOKOBAN - Tony PEREIRA et Davy MU
Nous nous excusons tout d'abord de l'oubli des readme.txt de la phase 2 et de la phase 1.

Voici le document readme.txt qui consiste � pr�senter notre projet:
Tout d'abord la r�partition des t�ches:
Davy s'est charg� des d�placements du gardien, du d�placement des caisses, du d�bug, du chargement, de la sauvegarde, de la lecture des fichiers ainsi que de l'extension "tirer".
Tony s'est occup� des cl�s et des doors, de tout l'affichage (texte, matrice) et de l'extension "Menu".

La structure de notre programme:
-La premi�re partie (nos fonctions) sont donc divis�s en deux:
	-L'affichage, celle-ci comprend toute les fonctions li�es � l'affichage (Menu, matrice, texte)
	-les fonctionnalit�s, celle-ci comprend toute les fonctions li�es aux fonctionnements de notre programme, elle 	contient donc toute les fonctions en rapport avec les d�placements du gardien, les cl�s et les doors, les d�placements des caisse (tirer et pousser), la sauvegarde, le chargement 	et la lecture du fichier.
-La seconde partie, c'est � dire notre programme principal:
Tout d'abord nous initions la matrice, pour cela une matrice est cr�e gr�ce � la fonction lire_f qui permet de lire un fichier et de cr�er la matrice associ�e. Nous initions toutes les variables qui vont �tre utilis�s dans le programme tels que la condition du debug, ou les d�placements.
Toutes les actions sont donc effectu�s dans notre boucle while.

Explications du programme:
Deplacement du gardien: Tout simplement en v�rifiant si le joueur clique sur une des touches ("haut","bas",...)
Debug: En appuyant sur la touche d�bug "d" du clavier la condition qui �tait jusque l� None va devenir True.
Lorsque le d�bug sera actif, une condition if sera remplie, celle-dit stipule que si condition est �quivalent � True, une direction al�atoire sera donn�e puis le gardien se d�placera dans cette direction al�atoire et ainsi de suite.
En r�appuyant sur la touche d�bug, la condition, si �quivalent � True sera rendu False et ainsi le d�bug se stoppera.
Tirer: En appuyant sur t, une fonction v�rifiera si le gardien est pr�s d'une caisse, si oui la condition tirer_c sera rendu True.
Si la condition tirer_c est True, le gardien peut tirer n'importe quelle caisse (Attention elle ne peut pas la pousser) jusqu'au moment o� l'utilisateur r�appuye sur t (la touche tirer), a ce moment l� il ne pourra plus tirer les caisses.
Lecture de fichier: La fonction lire_f ne prend qu'un seul param�tre le nom du fichier.
La fonction lit le fichier puis retourne une matrice.

CODE COULEUR :
En Bleu : les portes
En Rouge : les cibles
En jaune : le gardien
En noir : les murs
En orange : les cl�s
En marron : les caisses

Les probl�mes rencontr�s:
-Tout d'abord l'affichage a rencontr� un probl�me, si la matrice pr�sent� est trop grande, l'affichage qui est proportionnel � la matrice et � la dimension de la fen�tre peut d�passer la r�solution de l'�cran.
Ainsi certains �l�ments peuvent ne pas �tre afficher d� � la taille de la matrice.
-Finalement, pour quitter le jeu il faut appuyer trois fois sur "Quitter" de m�me pour charger la partie il faut cliquer 2 fois sur "Charger".

Nota bene:
-Nous n'avons pas utilis� d'image pour habiller la matrice.
