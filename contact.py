import ansa
import math
from ansa import base
from ansa import constants
from ansa import mesh
global deck
deck = base.SetCurrentDeck(constants.LSDYNA)
vals = {"Name":"CONTACT_AUTOMATIC_NODES_TO_SURFACE",
        "TYPE":"TIED_NODES_TO_SURFACE",
        "SSID":"1",
        "MSID":"2",
        "SSTYP":"4:Node set",
        "MSTYP":"3:Part id",
        }
vals ={'Name': '*CONTACT_AUTOMATIC_NODES_TO_SURFACE', 
       'TYPE': 'TIED_NODES_TO_SURFACE', 
       'SSID': 1, 
       'MSID': 2, 
       'SSTYP': '4: Node set', 
       'MSTYP': '3: Part id'}
vals = {'Name': '*CONTACT_AUTOMATIC_SINGLE_SURFACE0.3', 
        'TYPE': 'AUTOMATIC_SINGLE_SURFACE', 
        'SSID': 0, 
        'SSTYP': '2: Part set', 
        'FS': 0.3, 
        'FD': 0.3, 
        'OPTIONAL CARDS A,B,C,D,E': 'A & B & C',
        'SOFT': '  1', 
        'IGNORE': '  1'}
vals = {'Name': '*CONTACT_AUTOMATIC_SINGLE_SURFACE0.3', 
        'TYPE': 'AUTOMATIC_SINGLE_SURFACE', 
        'SSID': 0, 
        'SSTYP': '2: Part set', 
        'FS': 0.3, 
        'FD': 0.3, 
        'OPTIONAL CARDS A,B,C,D,E': 'A & B & C',
        'SOFT': '  1', 
        'IGNORE': '  1'}

vals = {'Name': '*CONTACT_AUTOMATIC_SURFACE_TO_SURFACE11', 
        'TYPE': 'AUTOMATIC_SURFACE_TO_SURFACE', 
        'SSID': 2, 
        'MSID': 1, 
        'SSTYP': '3: Part id', 
        'MSTYP': '3: Part id', 
        'FS': 0.3, 
        'FD': 0.3, 
        'OPTIONAL CARDS A,B,C,D,E': 'A & B & C', 
        'SOFT': '  0', 
        'IGNORE': '  1'}
vals = {'Name': '*CONTACT_AUTOMATIC_SURFACE_TO_SURFACE', 
        'TYPE': 'AUTOMATIC_ONE_WAY_SURFACE_TO_SURFACE_TIEBREAK', 
        'SSID': 1, 
        'MSID': 2, 
        'SSTYP': '2: Part set', 
        'MSTYP': '2: Part set',  
        'OPTION': '', 
        'NFLS': 50.0, 
        'SFLS': 60.0, 
        'PARAM': 2.0, 
        'ERATEN': 5.0, 
        'ERATES': 6.0, }
res = base.CreateEntity(deck=deck, element_type="CONTACT", fields=vals)
print(res)

con = base.GetEntity(deck=deck, type="CONTACT", element_id=1)
a = base.GetEntityCardValues(deck,con,('Name','TYPE','SSID','MSID','SSTYP','MSTYP'))

con = base.GetEntity(deck=deck, type="CONTACT", element_id=10)
a = base.GetEntityCardValues(deck,con,('Name','TYPE','SSID','MSID','SSTYP','MSTYP','FS','FD','OPTION','NFLS','SFLS','PARAM','ERATEN','ERATES','OPTIONAL CARDS A,B,C,D,E','SOFT','IGNORE'))
print(a)