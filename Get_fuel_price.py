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

def showing(data):
    """Function to append to the list 'data_to_show' given an input of desired fuel day(s)"""
    data_to_show = []
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
    return data_to_show

def sort_Price(data):
    """sorts any list by the key term 'Price_of_Fuel', meant to work as a quiet function"""
    return data['Price_of_Fuel']

def filterloc(loc):
    return loc['Location']

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
            <a href="/" class="Standard_button">Home</a>
            <a href="/about" class="Standard_button">About</a>
            <a href="" class="Standard_button">Refresh</a>
            <p> KEY: Blue = Tomorrow, Green = Today. </p>
            <div class='search'>
            <input type='text' name='' placeholder= 'Type location to filter'>
            <a class='search-btn' href ='#'>Filter</a>
            </div>
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

    print(len(data))

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

def get_data(ftype=6, loc=None):
    """The main function being called.......aka Main."""

    # result_pM = prod_Men()
    # if result_pM == 8:
    #     test_parsed = feedparser.parse(FUELTEST)
    #     showing(test_parsed.entries)
    # today_url, tomorrow_url = [moded_Url(result_pM, T) for T in ['Today','Tomorrow']]
    today_url = moded_Url(ftype, 'Today')
    tomorrow_url = moded_Url(ftype, 'Tomorrow')
    try:
        today_data = requests.get(today_url)
        tomorrow_data = requests.get(tomorrow_url)
        # try and add a way to now go back to the local file when you dont have any internet. will help trust
    except requests.exceptions.ConnectionError:
        no_internet = '\n:----:----: Unabel to connect to the internt :----:----:\
            \nPlease check your internet connection and try again.\n\n'
        print(no_internet)
        no_internet_html = '''<h2>Please check your internet connection and try again.</h2>
        <a href="/scrape" class="Standard_button">Back</a>
        <a href="" class="Standard_button">Refresh</a>
            '''
        return no_internet_html
        sys.exit(0)

    today_parsed = feedparser.parse(today_data.text)
    tomorrow_parsed = feedparser.parse(tomorrow_data.text)

    for e in tomorrow_parsed.entries:
        e.update({'day':'Tomorrow'})
    for e in today_parsed.entries:
        e.update({'day':'Today'})
    all_parsed = today_parsed.entries + tomorrow_parsed.entries
    data_to_show = showing(all_parsed)
    show_sorted = sorted(data_to_show, key=sort_Price, reverse=False)

    if not loc == None:
        upper_loc = uppercase(loc)
        loclist = []
        for x in data_to_show['Location']:
            loclist.append(data_to_show)
            locfirst = sorted(data_to_show, key=filterloc)
            fkndone = table_Creation(loclist)
        return fkndone
    else:
        fkndone = table_Creation(show_sorted)
        return fkndone

if __name__ == '__main__':
    get_data()

print(':-----------:-----------: ENDED HERE :-----------:-----------:')
H = localtime().tm_hour
M = localtime().tm_min
S = localtime().tm_sec
print(f'Time: {H}:{M}:{S}')
