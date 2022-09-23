import os
import PySimpleGUI as sg
import xml.etree.ElementTree as ET
from colorama import init, Style, Fore
import collections

sg.theme('LightPurple')

# возможность открыть постройки, все или по одной локаьлно

def ui():
    _bulean = ['true', 'false']
    Stats = 0
    Active = 0
    BuildingId = 1
    Duration = 2
    ResultObjectBalanceId = 3
    Materials = 1

    while True:
        event, values = sg.Window('res_atlas',
         grab_anywhere_using_control=True,
         
         layout =
                    # [[sg.Text('EditorId\t        Active     Update time\t  Location', text_color="YELLOW")]] + 
                    [
                        [

                    sg.Input(res_atlas[i][Stats][Active], size=(10, 1)),
                    # sg.Combo(_bulean, default_value=_bulean[i], size=(5, 1), key=f"{i}_active"), 
                    # sg.Input(updateTime_list[i], size=(9, 1), key=f"{i}_time"), 
                    # sg.Text(f'{res_atlas[i]}')
                        
                        ] for i in range(0,len(res_atlas))
                    ] + [[sg.Button('OK'), sg.Button('Exit')]]).read(close=True)

        # есть три списка location, bulean, time
        # сделать атлас --- location:[bulean, time]
        # 
        if event == 'OK':
            pass
            time_list = []
            bulean_list = []


            # for i in range(0, len(updateTime_list)):
            #     time = values[f"{i}_time"]
            #     time_list.append(time)
                
            # for i in range(0, len(active_list)):
            #     active = values[f"{i}_active"]
            #     bulean_list.append(active)
            
            # return tree, root, locations, bulean_list, time_list

        if event in ('Exit', None) or event == sg.WIN_CLOSED:
            break

# in_progress

def get_BuildingResources(tree, building, building_List):

    Stats = []


    stats_list = ["AvailableByDefault","BuildingId",
                "Duration", "ResultObjectBalanceId"]

    stats_temp_list = []
    AvailableByDefault_list = []
    BuildingId_list = []
    Duration_list = []
    ResultObjectBalanceId_list = []

    # Blueprint -- Ingredients -- BlueprintIngredient
    ObjectBalanceId_list = []
    ObjectAmount_list = []

    for element_01 in tree.find("Blueprints").findall("Blueprint"):
        for element_02 in element_01.findall("BalanceName"):
            if element_02.text == building:

                print(Fore.GREEN +  f"Processing --- {building}" + Style.RESET_ALL)

                for stat in stats_list:
                    Stats = get_Stats(building, element_01, stats_temp_list, stat)

                for _ in element_01.findall("Ingredients"):
                    Ingredients = get_Ingredients(element_01)
    print()
    print("Stats --- ", Stats)
    print("Ingredients --- ", Ingredients)
    res_atlas.update({building:[Stats, Ingredients]})
    
def get_Stats(building, _element, _list, _attribute):
    for element_05 in _element.findall(_attribute):
        text = element_05.text
        # _atlas.update({building:[text]})
        _list.append(text)
        print(f"{_attribute} --- " + text)
        return _list

def get_Ingredients(element_01):

    return_Ingredients_list = []
    for element_03 in element_01.findall("Ingredients"):
        print("Materials:")
        for element_04 in element_03.findall("BlueprintIngredient"):
            for element_05 in element_04.findall("ObjectBalanceId"):
                ObjectBalanceId = element_05.text
            
            for element_06 in element_04.findall("ObjectAmount"):
                ObjectAmount = element_06.text
            
            return_Ingredients_list.append([ObjectBalanceId, ObjectAmount])

            # try:
            #     print(f"{material_atlas[ObjectBalanceId]} --- ObjectBalanceId / ObjectAmount   {ObjectBalanceId} / {ObjectAmount}")
            # except:
            #     print(Fore.CYAN + f"{'UNKNOWN MATERIAL'}" + Style.RESET_ALL + f"--- ObjectBalanceId / ObjectAmount {ObjectBalanceId} / {ObjectAmount}")
    return return_Ingredients_list
def get_Buildings(path):
    tree = ET.parse(path)
    root = tree.getroot()

    building_List = []
    
    for element in root.find("Blueprints").findall("Blueprint"):
        for name in element.findall("BalanceName"):
            building_List.append(name.text)
    
    return tree, root, building_List

def get_MetaData(path):
    tree, root, building_List = get_Buildings(path)
   
    print(building_List)

    for building in building_List:

        for element_01 in root.find("Blueprints").findall("Blueprint"):
            for element_02 in element_01.findall("BalanceName"):
                if element_02.text == building:
                    try:
                        get_BuildingResources(tree, building, building_List)
                        print("--------"*4)
                    except:
                        print(Fore.RED +  f"Exception --- {building}" + Style.RESET_ALL)
                        print("--------"*4)
    return building, tree, root




def check_print():
    Stats = 0
    Active = 0
    BuildingId = 1
    Duration = 2
    ResultObjectBalanceId = 3
    Materials = 1

    for building in res_atlas:
        print('==='*10)
        print(building)
        print(res_atlas[building][Stats][Active])
        print(res_atlas[building][Stats][BuildingId])
        print(res_atlas[building][Stats][Duration])
        print(res_atlas[building][Stats][ResultObjectBalanceId]) 
        
        for id_and_amount in res_atlas[building][Materials]:
            material_id = id_and_amount[0]
            material_amount = id_and_amount[1]

            print(material_id, material_amount)
        print('==='*10)


def main():
    # get_Buildings(balance_path)
    get_MetaData(balance_path)
    # ui()
    
    # check_print()

if __name__ == "__main__":
    # balance_path = AskPath()
    balance_path = "e:\\temp_folder\\test\\\SurvivalBalance.xml"
    res_atlas = {}
    # balance_path = "e:\\temp_folder\\test\\\oneItem_balance.xml"
        
    material_atlas = open("e:\py\material_atlas.xml", 'r+').read()
    
    main()
