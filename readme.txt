SOKOBAN - Tony PEREIRA et Davy MU
Nous nous excusons tout d'abord de l'oubli des readme.txt de la phase 2 et de la phase 1.

Voici le document readme.txt qui consiste à présenter notre projet:
Tout d'abord la répartition des tâches:
Davy s'est chargé des déplacements du gardien, du déplacement des caisses, du débug, du chargement, de la sauvegarde, de la lecture des fichiers ainsi que de l'extension "tirer".
Tony s'est occupé des clés et des doors, de tout l'affichage (texte, matrice) et de l'extension "Menu".

La structure de notre programme:
-La première partie (nos fonctions) sont donc divisés en deux:
	-L'affichage, celle-ci comprend toute les fonctions liées à l'affichage (Menu, matrice, texte)
	-les fonctionnalités, celle-ci comprend toute les fonctions liées aux fonctionnements de notre programme, elle 	contient donc toute les fonctions en rapport avec les déplacements du gardien, les clés et les doors, les déplacements des caisse (tirer et pousser), la sauvegarde, le chargement 	et la lecture du fichier.
-La seconde partie, c'est à dire notre programme principal:
Tout d'abord nous initions la matrice, pour cela une matrice est crée grâce à la fonction lire_f qui permet de lire un fichier et de créer la matrice associée. Nous initions toutes les variables qui vont être utilisés dans le programme tels que la condition du debug, ou les déplacements.
Toutes les actions sont donc effectués dans notre boucle while.

Explications du programme:
Deplacement du gardien: Tout simplement en vérifiant si le joueur clique sur une des touches ("haut","bas",...)
Debug: En appuyant sur la touche débug "d" du clavier la condition qui était jusque là None va devenir True.
Lorsque le débug sera actif, une condition if sera remplie, celle-dit stipule que si condition est équivalent à True, une direction aléatoire sera donnée puis le gardien se déplacera dans cette direction aléatoire et ainsi de suite.
En réappuyant sur la touche débug, la condition, si équivalent à True sera rendu False et ainsi le débug se stoppera.
Tirer: En appuyant sur t, une fonction vérifiera si le gardien est près d'une caisse, si oui la condition tirer_c sera rendu True.
Si la condition tirer_c est True, le gardien peut tirer n'importe quelle caisse (Attention elle ne peut pas la pousser) jusqu'au moment où l'utilisateur réappuye sur t (la touche tirer), a ce moment là il ne pourra plus tirer les caisses.
Lecture de fichier: La fonction lire_f ne prend qu'un seul paramètre le nom du fichier.
La fonction lit le fichier puis retourne une matrice.

CODE COULEUR :
En Bleu : les portes
En Rouge : les cibles
En jaune : le gardien
En noir : les murs
En orange : les clés
En marron : les caisses

Les problèmes rencontrés:
-Tout d'abord l'affichage a rencontré un problème, si la matrice présenté est trop grande, l'affichage qui est proportionnel à la matrice et à la dimension de la fenêtre peut dépasser la résolution de l'écran.
Ainsi certains éléments peuvent ne pas être afficher dû à la taille de la matrice.
-Finalement, pour quitter le jeu il faut appuyer trois fois sur "Quitter" de même pour charger la partie il faut cliquer 2 fois sur "Charger".

Nota bene:
-Nous n'avons pas utilisé d'image pour habiller la matrice.
