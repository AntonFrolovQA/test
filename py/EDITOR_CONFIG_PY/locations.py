import os
from turtle import update
import PySimpleGUI as sg
import xml.etree.ElementTree as ET
from colorama import init, Style, Fore

sg.theme('DarkGrey13')

# возможность активировать локации для посещения, редактирование времени обновления,
# возвращает значения для редактирования всех локаций или одной частным случаем, еще в процессе (ЧТО?)
# def mod_text(elem01, key, newitem):
#     for elem02 in elem01.findall(key):
#         output = elem02.text
#         output = newitem
#         # return output
def get_ProjPath():
    path = os.path.dirname(os.path.realpath(__name__)) + "\\locations.ini"
    if os.path.exists(path) and len(open(path).read()) > 0 and os.path.exists(open(path).read()):
        pass
    else:
        projectPath = sg.popup_get_folder('Outlander-client path...', no_titlebar=True, grab_anywhere=True)
        open(path, 'a').close()
        open(path, 'w').write(projectPath)
    ProjPath = open(path).read()

    Path = ProjPath + "\\ClientProject\\\Assets\\GamplaySystemsAndControllers\\Resources\\EditorConfig\\\EditorConfig.xml"
    return Path

def mod():
    tree, root, locations, bulean_list, time_list = ui_editor()
    working_dict = mk_dict(locations, bulean_list, time_list)

    for location in working_dict:
        for element_01 in root.find("Locations").findall("LocationCfg"):
            for element_02 in element_01.findall("SceneName"):
                if element_02.text == location:
                
                    try:
                        for element_01 in root.find("Locations").findall("LocationCfg"):
                            for element_02 in element_01.findall("SceneName"):
                                if element_02.text == location:
                                    
                                    for element_05 in element_01.findall("Active"):
                                        # active = element_05.text
                                        element_05.text = working_dict[location][0]

                                    for element_05 in element_01.findall("UpdateTime"):
                                        # update = element_05.text
                                        element_05.text = working_dict[location][1]
                    except:
                        pass
    
    with open(editor_path, 'wb') as f:
        tree.write(f)

def mk_dict(locations, bulean, time):
    new_dict = {}
    for i in range(0, len(locations)):
        new_dict.update([(locations[i], [bulean[i], time[i]])])
    
    print(new_dict)
    return new_dict

def ui_editor():
    locations, tree, root = get_locationStats(editor_path)
    _bulean = ['true', 'false']

    while True:
        event, values = sg.Window('locations',
         grab_anywhere_using_control=True,
         
         layout =
                    [[sg.Text('EditorId\t        Active     Update time\t  Location', text_color="YELLOW")]] + 
                    [
                        [

                    sg.Input(editorId_list[i], size=(10, 1)),
                    sg.Combo(_bulean, default_value=active_list[i], size=(5, 1), key=f"{i}_active"), 
                    sg.Input(updateTime_list[i], size=(9, 1), key=f"{i}_time"), 
                    sg.Text(f'{locations[i]}')
                        
                        ] for i in range(0,len(locations))
                    ] + [[sg.Button('OK'), sg.Button('Exit')]]).read(close=True)

        # есть три списка location, bulean, time
        # сделать атлас --- location:[bulean, time]
        # 
        if event == 'OK':
            time_list = []
            bulean_list = []


            for i in range(0, len(updateTime_list)):
                time = values[f"{i}_time"]
                time_list.append(time)
                
            for i in range(0, len(active_list)):
                
                active = values[f"{i}_active"]
                bulean_list.append(active)
            
            return tree, root, locations, bulean_list, time_list

        if event in ('Exit', None) or event == sg.WIN_CLOSED:
            break

def get_XML_Locations(path):
    tree = ET.parse(path)
    root = tree.getroot()
    locations_List = []
    for element in root.find("Locations").findall("LocationCfg"):
        for name in element.findall("SceneName"):
            location = name.text
            # print(location)
            locations_List.append(location)
    return tree, root, locations_List

def get_locationStats_exception(root, location):

    for element_01 in root.find("Locations").findall("LocationCfg"):
        for element_02 in element_01.findall("SceneName"):
            if element_02.text == location:
                for element_05 in element_01.findall("EditorId"):
                    editor_exc = element_05.text
                    editorId_list.append(editor_exc)
                    print("EditorId --- " + editor_exc)

                for element_05 in element_01.findall("Active"):
                    active_exc = element_05.text
                    active_list.append(active_exc)
                    print("Active --- " + active_exc)

                for element_05 in element_01.findall("UpdateTime"):
                    update_exc = element_05.text
                    updateTime_list.append(update_exc)
                    print("Update time --- " + update_exc)

def get_locationStats(path):
    tree, root, location_list = get_XML_Locations(path)

    for location in location_list:

        for element_01 in root.find("Locations").findall("LocationCfg"):
            for element_02 in element_01.findall("SceneName"):
                if element_02.text == location:
                    try:
                        print(Fore.GREEN +  f"Processing --- {location}" + Style.RESET_ALL)
                        get_locationStats_exception(root, location)
                        print("--------"*4)
                    except:
                        print(Fore.RED +  f"Exception --- {location}" + Style.RESET_ALL)
                        print("--------"*4)
                        pass
    # location_list.sort()
    return location_list, tree, root

def main():
    # get_XML_Locations(editor_path)
    # get_locationStats(editor_path)
    # ui_editor()
    mod()



if __name__ == "__main__":

    database_id = {
        
    }

    editorId_list = []
    active_list = []
    updateTime_list = []
    # balance_path = AskPath()
    # balance_path = get_ProjPath()
    # editor_path = "e:\\temp_folder\\test\\\EditorConfig.xml"
    editor_path = get_ProjPath()

    main()