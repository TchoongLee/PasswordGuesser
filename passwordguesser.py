import argparse
from multiprocessing import Pool
import os
import sys
import itertools


#########################MODIFIABLE###########################
#chaine de base avec les 1 à 4 mots clefs
chaine=["word1","word2","word3"]
#chaine qui s'ajoute a la fin de chaque mdp generé
wordappend=""
#chaine qui s'ajoute au debut de chaque mdp generé
wordprepend=""

#Caractère que l'on veut transformer (ceux de base sont bien)
LEET_1_TRANSLATIONS = str.maketrans('oOaAeEiIsS', '0044331155')
LEET_2_TRANSLATIONS = str.maketrans('oOaA', '00@@')
LEET_3_TRANSLATIONS = str.maketrans('oOaAiIeE', '00@@!!$$')
LEET_4_TRANSLATIONS = str.maketrans('aA', '@@')
LEET_5_TRANSLATIONS = str.maketrans('oO', '00')
LEET_6_TRANSLATIONS = str.maketrans('eE', '$$')
LEET_7_TRANSLATIONS = str.maketrans('iI', '!!')
#########################MODIFIABLE###########################



outputfinal=[]
cpt = 0
chainelen = len(chaine)


###########################FONCTION LEET###########################
def leet(mot: str) -> str:

    line = mot.translate(LEET_1_TRANSLATIONS)
    outputfinal.append(str(line))
    line = mot.translate(LEET_2_TRANSLATIONS)
    outputfinal.append(str(line))
    line = mot.translate(LEET_3_TRANSLATIONS)
    outputfinal.append(str(line))
    line = mot.translate(LEET_4_TRANSLATIONS)
    outputfinal.append(str(line))
    line = mot.translate(LEET_5_TRANSLATIONS)
    outputfinal.append(str(line))
    line = mot.translate(LEET_6_TRANSLATIONS)
    outputfinal.append(str(line))
    line = mot.translate(LEET_7_TRANSLATIONS)
    outputfinal.append(str(line))



###########################FONCTION GLOBAL ACTIVE###########################
def active_global_parsing():
    leet(str(mot).upper())
    leet(str(mot).lower())
    leet(str([i.capitalize() for i in mot]))
    outputfinal.append(str(mot))
    outputfinal.append(str(mot).lower())
    outputfinal.append(str(mot).upper())
    outputfinal.append([i.capitalize() for i in mot])
    


############################MAIN############################

for mot in chaine:
    leet(str(wordappend+mot).upper())
    leet(str(mot).lower())
    outputfinal.append(mot)
    outputfinal.append(str(mot).lower())
    outputfinal.append(str(mot).upper())
    outputfinal.append(str(mot).capitalize())



#chainelen définit le nombre de mot de la chaine de caractere
if chainelen == 1:
    active_global_parsing()

elif chainelen == 2:

    listpermutte = itertools.permutations(chaine)
    for mot in (listpermutte):
        active_global_parsing()

elif chainelen == 3:
    

    listpermutte = itertools.permutations(chaine)
    for mot in (listpermutte):
        active_global_parsing()

    listpermutte = itertools.permutations([chaine[0],chaine[1]])
    for mot in (listpermutte):
        active_global_parsing()

    listpermutte = itertools.permutations([chaine[0],chaine[2]])
    for mot in (listpermutte):
        active_global_parsing()

    listpermutte = itertools.permutations([chaine[1],chaine[2]])
    for mot in (listpermutte):
        active_global_parsing()



elif chainelen == 4:
    
    
    listpermutte = itertools.permutations(chaine)
    for mot in (listpermutte):
        active_global_parsing()

    listpermutte = itertools.permutations([chaine[0],chaine[1]])
    for mot in (listpermutte):
        active_global_parsing()


    listpermutte = itertools.permutations([chaine[0],chaine[2]])
    for mot in (listpermutte):
        active_global_parsing()

    listpermutte = itertools.permutations([chaine[0],chaine[3]])
    for mot in (listpermutte):
        active_global_parsing()

    listpermutte = itertools.permutations([chaine[1],chaine[2]])
    for mot in (listpermutte):
        active_global_parsing()

    listpermutte = itertools.permutations([chaine[1],chaine[3]])
    for mot in (listpermutte):
        active_global_parsing()

    listpermutte = itertools.permutations([chaine[2],chaine[3]])
    for mot in (listpermutte):
        active_global_parsing()



else:

    print("error entre 2 et 4 mots ")

    
    



###########################OUTPUT FINAL###########################
outputfinal2=[]


# on convertit la liste outputfinal en vrai mot collés (outputfinal2)
for t in outputfinal:
    
    t = str(t).replace("(", "").replace(")", "").replace("'", "").replace(",", "").replace(" ", "").replace("[", "").replace("]", "")
    t = (wordprepend+t+wordappend)
    outputfinal2.append(t)

f = open("output.txt", "w")

for i in outputfinal2:
    print(i)
    f.write(i)
    f.write("\n")

f.close()



