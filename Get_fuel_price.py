import requests
import os
import sys
import feedparser
from pprint import pprint
from time import localtime
from Product_Menu import product_Menu as prod_Men



FUELTEST = 'file:///Users/leviix/Desktop/Scripts/Python_scripts/Cheap_fuel/Fuelinformation.html'

def moded_Url(prod, day):
    """Creates the required urls for both today and tomororw and return them to """

    url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={product}&Day={days}'
    modded_url = url.format(product=prod, days=day)
    return modded_url

data_to_show = []

def showing(data):
    """Function to append to the list 'data_to_show' given an input of desired fuel day(s)"""

    for entry in data:
        data_to_show.append({
            'Store_Name':entry['trading-name'],
            'Price_of_Fuel':entry.price,
            'Location':entry.location,
            'Coordinates':[{
            'Lat':entry.latitude,
            'Long':entry.longitude}],
            'Address':entry.address,
            'Date': entry.date,
            'Day':entry.day,
            })

def sort_Price(data):
    """sorts any list by the key term 'Price_of_Fuel', meant to work as a quiet function"""

    return data['Price_of_Fuel']

def table_Creation(data):
    """creates the whole html page that is being rendered,(in this case it just being html responded)"""
    # if __name__ == '__main__':
    #     f = open('table.html', 'w')
    # else:
    title = '''
        <head>
            <title>
                Fuel Scrapper
            </title>
            <h1>Fuel Slicer</h1>
            <a href="http://localhost:8000/home/" class="Standard_button">Home</a>
            <a href="http://localhost:8000/home/about" class="Standard_button">About</a>
            <p> KEY: Blue = Tomorrow, Green = Today. </p>
        </head>
        '''
    t_head = '''
        <thead>
            <tr>
                <th colspan = '6'>Fuel Scrapped</th>
            </tr>
            <tr>
                <td><b> Store Name  </b></td>
                <td><b> Price       </b></td>
                <td><b> Address     </b></td>
                <td><b> Location    </b></td>
                <td><b> Date        </b></td>
            </tr>
        </thead>
        '''

    # t_body = ''.join('''
    #         <tr>
    #             <td>{Store_Name}</td>
    #             <td>{Price_of_Fuel}</td>
    #             <td>{Address}</td>
    #             <td>{Location}</td>
    #             <td>{Date}</td>
    #         </tr>
    #         '''.format(**entry) for entry in data)
    # if data.day == 'Tomorrow':
    #     colour == blue
    # else:
    #     colour == white

    t_body = ['''

        <tr style ='background-color: {c}'>
            <td>{Store_Name}</td>
            <td>{Price_of_Fuel}</td>
            <td>{Address}</td>
            <td>{Location}</td>
            <td>{Date}</td>
        </tr>
        '''.format(**entry, c = 'Blue' if entry['Day'] == 'Tomorrow' else 'Green') for entry in data]

    n_table = ''.join(t_body)

    whole_page = '''
    <!DOCTYPE html>
    <html>
        {}
        <table>
            <tbody>
                {}
                {}
            </tbody>
        </table>
    </html>
        '''.format(title, t_head, n_table)
    return whole_page

def get_data():
    """The main function being called.......aka Main."""

    # result_pM = prod_Men()
    # if result_pM == 8:
    #     test_parsed = feedparser.parse(FUELTEST)
    #     showing(test_parsed.entries)
    # today_url, tomorrow_url = [moded_Url(result_pM, T) for T in ['Today','Tomorrow']]
    today_url = moded_Url(6, 'Today')
    tomorrow_url = moded_Url(6, 'Tomorrow')
    try:
        today_data = requests.get(today_url)
        tomorrow_data = requests.get(tomorrow_url)
        # try and add a way to now go back to the local file when you dont have any internet. will help trust
    except requests.exceptions.ConnectionError:
        no_internet = '\n:----:----: Unabel to connect to the internt :----:----:\
            \nPlease check your internet connection and try again.\n\n'
        print(no_internet)
        sys.exit(0)

    today_parsed = feedparser.parse(today_data.text)
    tomorrow_parsed = feedparser.parse(tomorrow_data.text)

    for e in tomorrow_parsed.entries:
        e.update({'day':'Tomorrow'})
    for e in today_parsed.entries:
        e.update({'day':'Today'})
    all_parsed = today_parsed.entries + tomorrow_parsed.entries
    showing(all_parsed)
    show_sorted = sorted(data_to_show, key=sort_Price, reverse=False)
    fkndone = table_Creation(show_sorted)


    # print(fkndone)
    return fkndone

if __name__ == '__main__':
    get_data()


# print(data_to_show)
print(':-----------:-----------: ENDED HERE :-----------:-----------:')
H = localtime().tm_hour
M = localtime().tm_min
S = localtime().tm_sec
print('Time: {}:{}:{}'.format(H, M, S))
