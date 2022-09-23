from logging import root
import os
import PySimpleGUI as sg
from PySimpleGUI import SYMBOL_DOWN
import xml.etree.ElementTree as ET
import sys
import random

sg.theme('DarkGrey3')

# from AppKit import NSSound
# sound = NSSound.alloc()
# sound.initWithContentsOfFile_byReference_('E:\\py\\dist\\gimn.mp3', True)
# sound.play()

# этот быстрокод заменить, возможность забирать конфиги из созданной xml,
# возможность добавлять свои статы, сейчас все захардкожено
# добавить кнопку save_preset

def global_print():
    for i in global_list:
        print(i)
def AskPath():
    
    layout = [
        [sg.Text("outlander-client", text_color='red')],
        [sg.InputText(default_text = f"e:\main\outlander-client", key = "-MASTER-"),sg.FolderBrowse()],
        [sg.OK(key='OK'), sg.Cancel()]
    ]

    window = sg.Window(f'path to client', layout)
    while True:
        event, values = window.read(close=True)
        master = values["-MASTER-"]
        # =========================
        if event == "OK":
            return master + "\\ClientProject\\Assets\\GamplaySystemsAndControllers\\Resources\\SurvivalBalance.xml"
        if event in ('Cancel', None) or event == sg.WIN_CLOSED:
            break
    window.close()
def random_pos():
    x = random.randint(10, 1800)
    y = random.randint(10, 1000)

    global_list.append(f"""x = {x}, y = {y}""")
    return x, y
def get_ProjPath():
    path = os.path.dirname(os.path.realpath(__name__)) + "\\balance.ini"
    # _backup = os.path.dirname(os.path.realpath(__name__)) + "\\backup_SurvivalBalance.xml"
    
    if os.path.exists(path) and len(open(path).read()) > 0 and os.path.exists(open(path).read()):
        pass
    else:
        projectPath = sg.popup_get_folder('Outlander-client path...', no_titlebar=True, grab_anywhere=True)
        nword = 0
        
        
        while True:
            if os.path.exists(projectPath + "\\ClientProject\\\Assets\\GamplaySystemsAndControllers\\Resources\\SurvivalBalance.xml"):
                break
            else:
                nword = nword + 1
                if nword == 2:
                    projectPath = sg.popup_get_folder('Fabulous idiot...', no_titlebar=True, grab_anywhere=True)
                elif nword == 3:
                    projectPath = sg.popup_get_folder("I see, you are comedian", no_titlebar=True, grab_anywhere=True)
                elif nword == 4:
                    projectPath = sg.popup_get_folder("A Fcking comedian...", no_titlebar=True, grab_anywhere=True)
                elif nword == 5:
                    projectPath = sg.popup_get_folder("-___-", no_titlebar=True, grab_anywhere=True)
                    while True:
                        x, y = random_pos()

                        sg.popup_annoying('Hahahahahahahaha, still funny?', location=(x, y))
                        # exit(0)
                else:
                    projectPath = sg.popup_get_folder('Wrong path, try again\nExample: e:\main\outlander-client', no_titlebar=True, grab_anywhere=True)


        open(path, 'a').close()
        open(path, 'r+').write(projectPath)
    ProjPath = open(path).read()

    Path = ProjPath + "\\ClientProject\\\Assets\\GamplaySystemsAndControllers\\Resources\\SurvivalBalance.xml"

    # if os.path.exists(_backup):
    #     pass
    # else:
    #     copy2(Path, _backup)   

    return Path
def overkill(window, stats, n):
    amounts = []
    for i in stats:
        amounts.append(stats[i][n])
    
    for i in range(1, 23):
        key = str(i)
        window.find_element(key).update(amounts[i-1])
def get_UI(prefab_list):
    createSimpleRecepies = 0
    stats = {
    "START_LEVEL":[1,90],
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
    "MAX_LEVEL":[15, 90],
    "Fist_Attack":[3, 999],
    "Fist_Speed":[100, 999],
    "Fist_Range":[300, 999],
    "HealthPoints":[100, 999],
    "Armor":[0, 999],
    "Attack":[3, 999],
    "MoveSpeed":[490, 999],
    "Void Crystals":[0, 10000],
    "Stick dropSet":[69, 69],
    "Stone dropSet":[70, 70],
    "Berry dropSet":[6, 6],
    }

    def stat_key(n):
        return_key = list(stats.keys())[n]
        return return_key

    Amounts = []

    testSize = 10

    layout = [
        [sg.Input(default_text=stats[stat_key(0)][0], size=(testSize, 10), key="1"), sg.Text(stat_key(0))],
        [sg.Input(default_text=stats[stat_key(1)][0], size=(testSize, 10), key="2"), sg.Text(stat_key(1))],
        [sg.Input(default_text=stats[stat_key(2)][0], size=(testSize, 10), key="3"), sg.Text(stat_key(2))],
        [sg.Input(default_text=stats[stat_key(3)][0], size=(testSize, 10), key="4"), sg.Text(stat_key(3))],
        [sg.Input(default_text=stats[stat_key(4)][0], size=(testSize, 10), key="5"), sg.Text(stat_key(4))],
        [sg.Input(default_text=stats[stat_key(5)][0], size=(testSize, 10), key="6"), sg.Text(stat_key(5))],
        [sg.Input(default_text=stats[stat_key(6)][0], size=(testSize, 10), key="7"), sg.Text(stat_key(6))],
        [sg.Input(default_text=stats[stat_key(7)][0], size=(testSize, 10), key="8"), sg.Text(stat_key(7))],
        [sg.Input(default_text=stats[stat_key(8)][0], size=(testSize, 10), key="9"), sg.Text(stat_key(8))],
        [sg.Input(default_text=stats[stat_key(9)][0], size=(testSize, 10), key="10"), sg.Text(stat_key(9))],
        [sg.Input(default_text=stats[stat_key(10)][0], size=(testSize, 10), key="11"), sg.Text(stat_key(10))],
        [sg.Input(default_text=stats[stat_key(11)][0], size=(testSize, 10), key="12"), sg.Text(stat_key(11))],
        [sg.Input(default_text=stats[stat_key(12)][0], size=(testSize, 10), key="13"), sg.Text(stat_key(12))],
        [sg.HSeparator()],
        [sg.Input(default_text=stats[stat_key(13)][0], size=(testSize, 10), key="14"), sg.Text(stat_key(13))],
        [sg.Input(default_text=stats[stat_key(14)][0], size=(testSize, 10), key="15"), sg.Text(stat_key(14))],
        [sg.Input(default_text=stats[stat_key(15)][0], size=(testSize, 10), key="16"), sg.Text(stat_key(15))],
        [sg.HSeparator()],
        [sg.Input(default_text=stats[stat_key(16)][0], size=(testSize, 10), key="17"), sg.Text(stat_key(16))],
        [sg.Input(default_text=stats[stat_key(17)][0], size=(testSize, 10), key="18"), sg.Text(stat_key(17))],
        [sg.Input(default_text=stats[stat_key(18)][0], size=(testSize, 10), key="19"), sg.Text(stat_key(18))],
        [sg.Input(default_text=stats[stat_key(19)][0], size=(testSize, 10), key="20"), sg.Text(stat_key(19))],
        [sg.HSeparator()],
        [sg.Input(default_text=stats[stat_key(20)][0], size=(testSize, 10), key="21"), sg.Text(stat_key(20))],
        [sg.HSeparator()],
        
        [
            sg.Input(default_text=stats[stat_key(21)][0], size=(5, 10), key="22"),
            sg.Text(stat_key(21), text_color='white'),
            sg.Combo(prefab_list, default_value='Prefab_wood_log', size=(30, 10), key="stick")
        ],
        
        [
            sg.Input(default_text=stats[stat_key(22)][0], size=(5, 10), key="23"),
            sg.Text(stat_key(22), text_color='blue'),
            sg.Combo(prefab_list, default_value='Prefab_stone', size=(30, 10), key="stone")
        ],


        [
            sg.Input(default_text=stats[stat_key(23)][0], size=(5, 10), key="24"),
            sg.Text(stat_key(23), text_color='red'),
            sg.Combo(prefab_list, default_value='Prefab_bush', size=(30, 10), key="berry")
        ],


        [sg.Checkbox("Unlock recepies",enable_events=True, key='simple'), sg.Text('(Открывает все рецепты)', text_color="grey")],
        [sg.Checkbox("Log recepies",enable_events=True, key='log'), sg.Text('(все рецепты за 1 бревно)', text_color="grey")],
        [sg.Checkbox("Easy Death", change_submits = True, enable_events=True, key='fast'), sg.Text('(Быстро сфидить: поднять и выпить)', text_color="grey")],

        [sg.Text("Preset")], 
        [sg.Button("Soft", key='-PUSSY-', size=(20, None), ), sg.Button("Hard", key='-KILLER-', size=(20, None))],
        
        [sg.Text(f"{random_phrase[random.randint(0, len(random_phrase) - 1)]}")],
        [sg.Text("\t\t\t\t\t"), sg.OK(button_color="GREEN", size=(10, 1))]
    ]
    window = sg.Window('\U0001f638 balance v0.23', layout, grab_anywhere=1)

    while True:
        event, Values = window.read()

        if event in ('Cancel', None) or event == sg.WIN_CLOSED:
            sys.exit(1)

        # сложили префабы моделей для stick/stone в список
        prefabCombo.clear()
        prefabCombo.append(Values["stick"])
        prefabCombo.append(Values["stone"])
        prefabCombo.append(Values["berry"])

        if event == "-PUSSY-":
            overkill(window, stats, 0)

        if event == "-KILLER-":
            overkill(window, stats, 1)
        logRecepies = 0
        if Values["log"] == True:
            logRecepies = 1

            Values["simple"] = True
            window["simple"].update(Values["simple"])

        fastDeath = 0

        if event == "OK":
            for i in range(1, 25):
                key = str(i)
                Amounts.append(Values[key])
            if Values["simple"] == True:
                createSimpleRecepies = 1
            if Values["fast"] == True:
                # window["23"].update(readonly=False)
                fastDeath = 1
            if Values["log"] == True:
                logRecepies = 1

                

            global_list.append(f"Amounts: {Amounts}")
            return Amounts, createSimpleRecepies, fastDeath, logRecepies
            


def get_Lists_Stats():
    constant_List = [
        "START_LEVEL",
        "START_GOLD",
        "START_SKILLPOINTS",
        "START_ENERGY",
        "ENERGY_MAX",
        "ENERGY_INCREASE_PERIOD",
        "WALK_MILLISECONDS_PER_ENERGY",
        "RUN_MILLISECONDS_PER_ENERGY",
        "MELEE_AGRO_ZONE_RADIUS",
        "RANGED_AGRO_ZONE_RADIUS",
        "INVENTORY_CRAFT_DURATION",
        "RUN_GLOBAL_MAP_SPEED",
        "MAX_LEVEL"
       
        ]

    weapons_List = [
        "Fists"
    ]
    
    mob_List = [
        "HealthPoints",
        "Armor",
        "Attack",
        "MoveSpeed"
    ]

    crystals_List = ["Void Crystals"]

    use_list = ["Stone", "Stick", 'Healthberry bush']
    return constant_List, weapons_List, mob_List, crystals_List, use_list

def get_XMLconstant_Stats(root, stat, amounts):
    for element in root.find("Constants").findall("Constant"):
        for name in element.findall("Name"):
            if name.text == f"{stat}":
                for name in element.findall("Value"):
                    name.text = amounts

                    global_list.append(f"Stats --- {stat}: {name.text}")
def get_XMLweapons_Stats(root, stat, amounts):
    for element in root.find("Weapons").findall("Weapon"):
        for name in element.findall("BalanceName"):
            if name.text == f"{stat}":
                for attack in element.findall("Attack"):
                    attack.text = amounts[13]

                    global_list.append(f"Attack --- {attack}: {attack.text}")

                for speed in element.findall("SpeedAttackModifier"):
                    speed.text = amounts[14]

                    global_list.append(f"Speed --- {speed}: {speed.text}")

                for arange in element.findall("AttackRange"):
                    arange.text = amounts[15]

                    global_list.append(f"ARange --- {arange}: {arange.text}")
def get_XMLmob_Stats(root, amounts):
    for element in root.find("Mobs").findall("Mob"):
        for name in element.findall("BalanceName"):
            if name.text == "Outlander":
                
                for hpoints in element.findall("HealthPoints"):
                    hpoints.text = amounts[16]

                    global_list.append(f"HP --- {hpoints}: {hpoints.text}")


                for armor in element.findall("Armor"):
                    armor.text = amounts[17]

                    global_list.append(f"Armor --- {armor}: {armor.text}")

                for attack in element.findall("AttackRange"):
                    attack.text = amounts[18]

                    global_list.append(f"Attack --- {attack}: {attack.text}")

                for move in element.findall("MoveSpeed"):
                    move.text = amounts[19]

                    global_list.append(f"MoveSpeed --- {move}: {move.text}")
def get_crystals(root, amounts):
    for element in root.find("Currencies").findall("Currency"):
        for name in element.findall("BalanceName"):
            if name.text == "Void Crystals":
              
                for crystals in element.findall("StartAmount"):
                    crystals.text = amounts[20]
                    
                    global_list.append(f"VoidCrystals --- {crystals}: {crystals.text}")

def find_dropItems_FromSets(root, id1):
    return_items = []
    for element in root.find("DropSet").findall("DropSet"):
        for BalanceId in element.findall("BalanceId"):
            if BalanceId.text == f"{id1}":
                for DropItems in element.findall("DropItems"):
                    for dItem in DropItems.findall("int"):
                        print(f"DropItem --- {dItem.text}")
                        return_items.append(dItem.text)        
    
    
    return return_items
def set_prefabModel(root, name, num):
    # prefabCombo[0]
    for element in root.find("ResourceObjects").findall("ResourceObject"):
        for BalanceName in element.findall("BalanceName"):
            if BalanceName.text == f"{name}":
                for elem in element.findall("ModelId"):
                    elem.text = prefabCombo[num]
def remove_int(root, id):
    for element in root.find("DropSet").findall("DropSet"):
        for BalanceId in element.findall("BalanceId"):
            if BalanceId.text == f"{id}":
                for DropItems in element.findall("DropItems"):
                    for intt in DropItems.findall("int"):
                        DropItems.remove(intt)
def add_int(root, amount, id1, id2, fastDeath):
    for element in root.find("DropSet").findall("DropSet"):
        for BalanceId in element.findall("BalanceId"):
            if BalanceId.text == f"{id1}":
                for DropItems in element.findall("DropItems"):
                    ET.SubElement(DropItems, 'int').text = f"{id2}"
                    elemId = str(amount)

                    return_items = find_dropItems_FromSets(root, elemId)
                    for item in return_items:
                        if elemId != f"{id1}":
                            ET.SubElement(DropItems, 'int').text = item

                    if fastDeath == 1:
                        ET.SubElement(DropItems, 'int').text = "166"


def get_useItems(root, amounts, fastDeath, logRecepies):
    remove_int(root, 69)
    remove_int(root, 70)
    remove_int(root, 6)

    add_int(root, amounts[21], "69", "72", fastDeath)
    add_int(root, amounts[22], "70", "73", fastDeath)
    add_int(root, amounts[23], "6", "6", fastDeath)

    set_prefabModel(root, "Stick", 0)
    set_prefabModel(root, "Stone", 1)
    set_prefabModel(root, "Healthberry bush", 2)

def get_prefab(root):
    prefab_list = [
        "Prefab_bonfire_with_boiler_props",
        "Prefab_dead_khan_orc_v4",
        "Prefab_dead_dwarves_v4",
        "Prefab_range_goblin2_dead2",
        "Prefab_guldji",
        "Prefab_goblin_chieftain",
        "Prefab_teleport_post",
        "Prefab_stone_zogdash_broken",
        "Prefab_guldji_sick",
        "Prefab_bardy_boat_miniriver",
        "Prefab_goat",
        "Prefab_dwarfs_borkan",
        "Prefab_boar",
        "Prefab_kobold",
        "Prefab_predator_plant",
        "Prefab_rabbitoad_v1"

    ]
    for element in root.find("ResourceObjects").findall("ResourceObject"):
        for name in element.findall("ModelId"):
            prefab = name.text
            prefab_list.append(prefab)
    prefab_list.sort() 
    return prefab_list
def xml_parseBalance(path):
    constantList, weaponsList, mobList, crystalsList, useList = get_Lists_Stats()
    tree = ET.parse(path)

    root = tree.getroot()

    # список префабов, отправляем в UI
    prefab_list = get_prefab(root)
    

    amounts, createSimpleRecepies, fastDeath, logRecepies = get_UI(prefab_list)

    n = -1
    for constantStat in constantList:
        n = n + 1
        get_XMLconstant_Stats(root, constantStat, amounts[n])

    for weaponStat in weaponsList:
        get_XMLweapons_Stats(root, weaponStat, amounts)

    for _ in mobList:
        get_XMLmob_Stats(root, amounts)

    for _ in crystalsList:
        get_crystals(root, amounts)

    # for _ in useList:
    get_useItems(root, amounts, fastDeath, logRecepies)

    tree.write(path, encoding="utf-8")
    return createSimpleRecepies, fastDeath, logRecepies

def create_logReciepe(element_01):
    # рецепты за 1 бревно, сейчас заморожен (если че работает)
    for element in element_01.findall("Ingredients"):

        ET.SubElement(element, "BlueprintIngredient")

        def sub(arg1, arg2):
            ET.SubElement(element.find("BlueprintIngredient"), f"{arg1}")
            for elem in element.find("BlueprintIngredient").findall(f"{arg1}"):
                elem.text = f"{arg2}"
        
        sub("ObjectBalanceType", "MATERIAL")
        sub("ObjectBalanceId", "1")
        sub("ObjectAmount", "1")

# открыть все рецепты
def Unlock_recepies(typeTomodify, ResultObject, building, element_01, logRecepies):
    if ResultObject.text == f"{typeTomodify}":
        for element_02 in element_01.findall("BalanceName"):
            if element_02.text == building:

                for activaed in element_01.findall("AvailableByDefault"):
                    activaed.text = "true"

                if logRecepies == 1:
                # улучшения построек за 1 бревно
                # --------------------------------
                    for element in element_01.findall("Ingredients"):
                        for ingredient in element.findall("BlueprintIngredient"):
                            element.remove(ingredient)
                    create_logReciepe(element_01)

def get_Ingredients(element_01):

    for element_03 in element_01.findall("Ingredients"):
        # print("Materials:")
        for element_04 in element_03.findall("BlueprintIngredient"):
            root.find("BlueprintIngredient").remove(element_04)
        

def get_Buildings(path):
    tree = ET.parse(path)
    root = tree.getroot()

    building_List = []
    
    for element in root.find("Blueprints").findall("Blueprint"):
        for name in element.findall("BalanceName"):
            building_List.append(name.text)
    global_list.append(f"building_List --- {building_List}")
    return tree, root, building_List

def get_MetaData(path, logRecepies):
    # copyfile(path, os.path.dirname(os.path.realpath(__name__)) + "backup.xml")
    tree, root, building_List = get_Buildings(path)

    for building in building_List:
        countAmount = 0


        for element_01 in root.find("Blueprints").findall("Blueprint"):
            for ResultObject in  element_01.findall("ResultObjectResourceType"):

                # ------------------------------------------------------------------------------
                # открывает все постройки
                # ------------------------------------------------------------------------------
                to_unlock = ["BUILDING", "ARMOR", "WEAPON"]
                for unlock in to_unlock: 
                    Unlock_recepies(unlock, ResultObject, building, element_01, logRecepies)

                # ------------------------------------------------------------------------------    
                # Для замены рецептов на 1 бревно; т.к. рецепты не структурированы в конфиге, получается рандом, пока заморожен, но работает 
                # ------------------------------------------------------------------------------
                
                # elif test.text == "MATERIAL":
                #     for element_02 in element_01.findall("BalanceName"):
                #         if element_02.text == building:

                #             for activaed in element_01.findall("AvailableByDefault"):
                #                 activaed.text = "true"

                #             for element in element_01.findall("Ingredients"):
                                
                #                 for ingredient in element.findall("BlueprintIngredient"):
                                    
                #                     for material in ingredient.findall("ObjectBalanceId"):
                #                         material.text = "1"
                                    
                #                     for amount in ingredient.findall("ObjectAmount"):
                #                         countAmount = countAmount + 1
                #                         amount.text = str(countAmount)

    tree.write(path, encoding="utf-8")
    
def set_DirtyWater(path):
    tree, root, _ = get_Buildings(path)
    
    for elem in root.find("Consumables").findall('Consumable'):
        for elem02 in elem.findall("BalanceName"):
            # print(elem02.text)

            if elem02.text == "Bottle of dirty water":
                
                for ver in elem.findall('V1'):
                    ver.text = "-40000"
    

    tree.write(path, encoding="utf-8")

def main():
    createSimpleRecepies, fastDeath, logRecepies = xml_parseBalance(balance_path)
    if createSimpleRecepies == 1:
        get_MetaData(balance_path, logRecepies)
    if fastDeath == 1:
        set_DirtyWater(balance_path)

    # print(prefabCombo)
    # get_Buildings(balance_path)
    # get_MetaData(balance_path)

if __name__ == "__main__":

    prefabCombo = []
    global_list = []

    random_phrase = [

        """Воистину убогого подаянием поддержи.\nНо вместо того, чтобы дать убогому целый арбуз,\nдай ему пол-арбуза, ибо иначе убогий может свихнуться от счастья.""",
        """Помни об умеренности во всем: и в еде, и в питии, и в плотских утехах,\nибо тот, кто злоупотребит радостями этими,\nпроснется наутро с великой головной болью и вялым членом""",
        """Не делай ближнему того, что себе не желаешь,\nесли только ближний не причинил тебе чрезвычайного ущерба\nи если не изобиловали подлостью деянея его""",
        """Всегда говори правду, кроме тех случаев,\nкогда правду говорить вредно. Вот тогда можешь врать""",
        """Побрейся, причешись, женись, заведи детей, купи скайрим"""

    ]


    # balance_path = AskPath()
    
    # balance_path, _backup = get_ProjPath()

    balance_path = get_ProjPath()
    # balance_path = "e:\\temp_folder\\test\\balance023\\SurvivalBalance.xml"

    # copy2(_backup, balance_path)
    main()
    # global_print()
    for i in prefabCombo:
        print(i)