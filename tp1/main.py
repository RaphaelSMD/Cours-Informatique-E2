from exo1 import calculer_imc
from exo2 import rangement
from exo3 import âge
from exo4 import approximation_pi
from exo5 import conversion
from exo6 import operation
from exo7 import plaque_immatriculation
exercice=input("Saisissez l'exercice que vous voulez ouvrir : \n1. Calculer l'IMC\n2. Rangement de nombres\n3. Conversion âge humain en âge canin\n4. Approximation de Pi\n5. Conversion de température\n6. Opérations mathématiques\n7. Génération de plaques d'immatriculation\n Choix de l'exercice : ")
if exercice=="1":
    calculer_imc()
elif exercice=="2":
    rangement()     
elif exercice=="3":
    âge()
elif exercice=="4":
    approximation_pi()
elif exercice=="5": 
    conversion()
elif exercice=="6":
    operation()
elif exercice=="7":
    plaque_immatriculation()
