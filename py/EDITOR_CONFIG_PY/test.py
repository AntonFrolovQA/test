from ast import Index
from cProfile import label
from logging import root
from optparse import Values
import os
import PySimpleGUI as sg
import xml.etree.ElementTree as ET
from colorama import init, Style, Fore
import collections
import random
import _tkinter as Tk



sg.theme('LightPurple')

# def get_Ingredients(element_01):

#     for element_03 in element_01.findall("Ingredients"):
#         print("Materials:")
#         for element_04 in element_03.findall("BlueprintIngredient"):
#             root.find("BlueprintIngredient").remove(element_04)

# def create_logReciepe(element_01):
#     for element in element_01.findall("Ingredients"):

#         ET.SubElement(element, "BlueprintIngredient")

#         def sub(arg1, arg2):
#             ET.SubElement(element.find("BlueprintIngredient"), f"{arg1}")
#             for elem in element.find("BlueprintIngredient").findall(f"{arg1}"):
#                 elem.text = f"{arg2}"
#         sub("ObjectBalanceType", "MATERIAL")
#         sub("ObjectBalanceId", "1")
#         sub("ObjectAmount", "1")

# def get_Buildings(path):
#     tree = ET.parse(path)
#     root = tree.getroot()

#     building_List = []
    
#     for element in root.find("Blueprints").findall("Blueprint"):
#         for name in element.findall("BalanceName"):
#             building_List.append(name.text)
#     return tree, root, building_List

# def get_MetaData(path):
#     tree, root, building_List = get_Buildings(path)

#     for building in building_List:

#         for element_01 in root.find("Blueprints").findall("Blueprint"):
#             for element_02 in element_01.findall("BalanceName"):
#                 if element_02.text == building:
#                     print(building)

#                     for activaed in element_01.findall("AvailableByDefault"):
#                         activaed.text = "true"

#                     for element in element_01.findall("Ingredients"):
#                         for ss in element.findall("BlueprintIngredient"):
#                             element.remove(ss)
                    
#                     create_logReciepe(element_01)         

#     with open(path, 'wb') as f:
#         tree.write(f)



# def main():
#     get_MetaData(balance_path)

# if __name__ == "__main__":
#     balance_path = "e:\\temp_folder\\test\\\SurvivalBalance.xml"
#     # balance_path = "e:\\temp_folder\\test\\\oneItem_balance.xml"
    
#     main()

def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

stats = {
    "START_LEVEL":[1,15],
    "START_GOLD":[100, 1000],
    "START_SKILLPOINTS":[0, 0],
    "START_ENERGY":[100, 100],
    "ENERGY_MAX":[100, 100],
    "ENERGY_INCREASE_PERIOD":[300000, 3],
    "WALK_MILLISECONDS_PER_ENERGY":[40000, 4],
    "RUN_MILLISECONDS_PER_ENERGY":[500, 5], 
    "MELEE_AGRO_ZONE_RADIUS":[1000, 1000],
    "RANGED_AGRO_ZONE_RADIUS":[2000, 2000],
    "INVENTORY_CRAFT_DURATION":[1000, 1],
    "RUN_GLOBAL_MAP_SPEED":[1, 1],
    "MAX_LEVEL":[15, 15],
    "Fist_Attack":[3, 999],
    "Fist_Speed":[100, 999],
    "Fist_Range":[300, 999],
    "HealthPoints":[100, 999],
    "Armor":[0, 999],
    "Attack":[3, 999],
    "MoveSpeed":[490, 999],
    "Void Crystals":[0, 123456789]
    }

# for i in stats:
#     print(i)
#     print(stats[i][0])
#     print(stats[i][1])
#     print()

# first_key = list(stats.keys())[0]

# value01 = stats[first_key][0]

# print(value01)
new = []
for i in stats:
    new.append(stats[i][0])
    
