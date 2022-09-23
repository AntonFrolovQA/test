from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import re
from colorama import init, Style, Fore
init(convert=True)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = '167V0fAS_kSwuMitj0FVYbWSF5LQF1IMiR3BvMoJ8v0I'



def sprint(get_id, values):
    _id = 0
    _name = 4
    _amount = 6

    for item in values:
        if item[_id] == get_id:
            
            print(Fore.MAGENTA + "Item" + Style.RESET_ALL +  f" --- {item[_id]}")
            print(Fore.CYAN + "Name" + Style.RESET_ALL +  f" --- {item[_name]}")
            print(Fore.CYAN + "Amount" + Style.RESET_ALL + f" --- {item[_amount]}")
            print('---'*13)

def main():

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        
        # get values 
        result_item = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                      range="id_driopItem!A1:G").execute()

        result_set = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                      range="id_dropSet!A1:Q").execute()

        result_exp = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                      range="id_ExpReward!A1:B").execute()

        

        # update values
        # result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #                                 range="test02!B2",
        #                                 valueInputOption="USER_ENTERED",
        #                                 body={"values":test_list}).execute()


        # print(result)

        values_idDroprItem = result_item.get('values', [])
        values_idDroprSet = result_set.get('values', [])
        values_idExp = result_exp.get('values', [])


        while True:
            get_id =input("Input id (i222 - dropItem, s222 - dropSet, e222 - expReward, q - quit): \n")

            if get_id.startswith('i'):
                get_id = str(re.sub(r'.', '', get_id, count=1))
                print("---"*13)
                print(Fore.YELLOW + "dropItem" + Style.RESET_ALL+  f"--- {get_id}")
                print("---"*13)
                sprint(get_id, values_idDroprItem)

            if get_id.startswith('s'):
                get_id = str(re.sub(r'.', '', get_id, count=1))
               
                for _set in values_idDroprSet:
                    
                    if _set[0] == get_id:
                        _set.pop(1)

                        print("---"*13)
                        n = len(_set) - 1
                        print(Fore.YELLOW + "dropSet" + Style.RESET_ALL+  f"--- {_set[0]}: \t{n} items")
                        print("---"*13)
                        for elem in _set[1:]:
                            sprint(elem, values_idDroprItem)

            if get_id.startswith('e'):
                get_id = str(re.sub(r'.', '', get_id, count=1))
                print("---"*13)
                print(Fore.YELLOW + "expId" + Style.RESET_ALL+  f"--- {get_id}")
                print("---"*13)
                for exp in values_idExp:
                    if exp[0] == get_id:
                        print(Fore.MAGENTA + "exp" + Style.RESET_ALL +  f"---{exp[1]}")
                print("---"*13)


            if get_id == 'q':
                break
    except HttpError as err:
        print(err) 


if __name__ == '__main__':
    main()
