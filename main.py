###################################### 
# 
# Created By X - ZhnDvs
# Don't Forget To Follow Me On Github
# Don't be script Kiddie
# Github : github.com/xnbl354
# Instagram : instagram.com/xnbl354
#
######################################
import requests
from os import system as SYSS
from sys import exit as EXT

brblue = '\x1b[94m'
white = '\x1b[37m'
your_apikey = 'YOUR_APIKEY_BINTABLE' # Change Your API Key, Get API Key on https:?/api.bintable.com first regist and get free apikey limit 100/req


def banner():
    my_banner = """
 {}____  _              ____ _               _    
| __ )(_)_ __        / ___| |__   ___  ___| | __
|  _ \| | '_ \ _____| |   | '_ \ / _ \/ __| |/ /
| |_) | | | | |_____| |___| | | |  __/ (__|   < -> {}Made By
{}|____/|_|_| |_|      \____|_| |_|\___|\___|_|\_\-> {}X - ZhnDvs{}""".format(brblue, white, brblue, white, brblue)
    print(my_banner)


if __name__ == '__main__':
    banner()
    while True:
        try:
            BINS = input('\n[{}?{}] Bins : {}'.format(white, brblue, white))
            req = requests.get("https://api.bintable.com/v1/"+BINS+"?api_key="+your_apikey)
            requests_json = req.json()
            if requests_json['result'] == 404:
                print('[!] Bins Error! / Not Found!')
            else:
                data = {
                    'Scheme': requests_json['data']['card']['scheme'],
                    'Type': requests_json['data']['card']['type'],
                    'Category': requests_json['data']['card']['category'],
                    'Length': requests_json['data']['card']['length'],
                    'Checkluhn': requests_json['data']['card']['checkluhn'],
                    'Cvvlen': requests_json['data']['card']['cvvlen'],
                    'Country': requests_json['data']['country']['name'],
                    'CountryCode': requests_json['data']['country']['code'],
                    'Flag': requests_json['data']['country']['flag'],
                    'Currency': requests_json['data']['country']['currency'],
                    'CurrencyCode': requests_json['data']['country']['currency_code'],
                    'Bank': requests_json['data']['bank']['name'],
                    'Bank Url': requests_json['data']['bank']['website'],
                    'Bank Phone': requests_json['data']['bank']['phone'],
                }
                print("""
{}[{}+{}] Scheme : {}{}
{}[{}+{}] Type : {}{}
{}[{}+{}] Category : {}{}
{}[{}+{}] Length : {}{}
{}[{}+{}] Checkluhn : {}{}
{}[{}+{}] Cvvlen : {}{}
{}[{}+{}] Country : {}{}
{}[{}+{}] CountryCode : {}{}
{}[{}+{}] Flag : {}{}
{}[{}+{}] Currency : {}{}
{}[{}+{}] CurrencyCode : {}{}
{}[{}+{}] Bank : {}{}
{}[{}+{}] Bank Url : {}{}
{}[{}+{}] Bank Phone : {}{}""".format(white, brblue, white, brblue, data['Scheme'], white, brblue, white, brblue, data['Type'], white, brblue, white, brblue, data['Category'], white, brblue, white, brblue, data['Length'], white, brblue, white, brblue, data['Checkluhn'], white, brblue, white, brblue, data['Cvvlen'], white, brblue, white, brblue, data['Country'], white, brblue, white, brblue, data['CountryCode'], white, brblue, white, brblue, data['Flag'], white, brblue, white, brblue, data['Currency'], white, brblue, white, brblue, data['CurrencyCode'], white, brblue, white, brblue, data['Bank'], white, brblue, white, brblue, data['Bank Url'], white, brblue, white, brblue, data['Bank Phone'], white))
        except KeyboardInterrupt:
            EXT('\nOke Byeeeeeee, Thanks For Using My Tools....')
