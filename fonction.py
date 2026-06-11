import webbrowser

from qgis.core import QgsFeatureRequest,QgsExpression

from .constante import *
from .mapping_version import *

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
    webbrowser.open("https://ignf.github.io/assistant-complexe-qgis-plugin/")

def afficheerreur(text, titre=TITRE):
    msg = QMessageBox()
    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setStandardButtons(Ok)
    msg.setText(text)
    msg.setWindowFlags(WindowStaysOnTopHint)
    msg.exec()


def affichemessageAvertissement(text, titre):
    msg = QMessageBox()
    msg.setIcon(Warning)
    msg.setWindowTitle(titre)
    msg.setText(text)

    btnAnnuler = msg.addButton("Annuler", RejectRole )
    btnAnnuler.setStyleSheet("color:red ; font-weight: bold")

    btnValider = msg.addButton("Retirer du complexe", AcceptRole)
    btnValider.setStyleSheet("color:green ; font-weight: bold")

    msg.setWindowFlags(WindowStaysOnTopHint)
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
