import os.path
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtCore import Qt
from qgis.core import QgsFeatureRequest,QgsExpression

from qgis.core import QgsCoordinateReferenceSystem, QgsProject
from .constante import *
import subprocess



def modif_attribut_byid(layer,liste,champs,nouveau):
    # liste = selection : selectedFeatures()
    for feature in liste:
        layer.changeAttributeValue(feature.id(), layer.fields().indexOf(champs), nouveau)

def modif_champs(layer,champs,valeur, champs_a_modifier,new_valeur):
    expr = QgsExpression(f"{champs} = \"{valeur}\"")
    # layer.setSubsetString(expr)
    layer.getFeatures(QgsFeatureRequest(expr))
    for entite in layer.getFeatures():
        layer.changeAttributeValue(entite.id(), layer.fields().indexOf(champs_a_modifier), new_valeur)


def afficheDoc():
    fichier = os.path.join(os.path.dirname(__file__), "assistant complexe.pdf")
    if not os.path.isfile(fichier):
        afficheerreur("La documentation est introuvable", "Information")
    else:
        subprocess.Popen(['start', '', fichier], shell=True)


def afficherlog():
    # fic = os.path.dirname(__file__) + "/log.txt"
    fic = os.path.dirname(__file__) + "/transaction.xlsx"

    if not os.path.isfile(fic):
        afficheerreur("Le fichier de log n'existe pas\nIl sera crée dès la premiére transaction", "Information")
    else:
        subprocess.Popen(["start", "excel", fic], shell=True)


def afficheerreur(text, titre=TITRE):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setText(text)
    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
    msg.exec()


def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(titre)
    msg.setText(text)

    btnAnnuler = msg.addButton("Annuler", QMessageBox.RejectRole )
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")

    btnValider = msg.addButton("Retirer du complexe", QMessageBox.AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")

    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
    msg.exec()

    if msg.clickedButton() == btnAnnuler:
        return False
    if msg.clickedButton() == btnValider:
        return True


def list_submenus(menu):
    # Liste pour stocker les sous-menus
    submenus = []
    for action in menu.actions():
        # Vérifie si l'action a un sous-menu
        if action.menu():
            submenus.append(action.menu().title())
            # Récursivement lister les sous-menus
            submenus.extend(list_submenus(action.menu()))
        else:
            submenus.append(action.text())
    return submenus
