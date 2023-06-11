import requests
from bs4 import BeautifulSoup
import json
import csv
import re
import time
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
def get_source(url):
        try:
            session = HTMLSession()
            response = session.get(url)
            return response

        except requests.exceptions.RequestException as e:
            print(e)
class GoogleScraper:

    pagination_params = {
        'q': 'gaming',
        'sxsrf': 'ACYBGNRmhZ3C1fo8pX_gW_d8i4gVeu41Bw:1575654668368',
        'ei': 'DJXqXcmDFumxrgSbnYeQBA',
        'start': '',
        'sa': 'N',
        'ved': '2ahUKEwjJua-Gy6HmAhXpmIsKHZvOAUI4FBDy0wN6BAgMEDI',
        'biw': '811',
        'bih': '628'
    }
    
    initial_params = {
        'sxsrf': 'ACYBGNQ16aJKOqQVdyEW9OtCv8zRsBcRig:1575650951873',
        'source': 'hp',
        'ei': 'h4bqXcT0MuPzqwG87524BQ',
        'q': '',
        'oq': '',
        'gs_l': 'psy-ab.1.1.35i362i39l10.0.0..139811...4.0..0.0.0.......0......gws-wiz.....10.KwbM7vkMEDs'
    }
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'CGIC=InZ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIz; HSID=AenmNVZxnoADsXz_x; SSID=AjbLhhwkjh8f3FOM8; APISID=IqkNtUA0V2DXlees/A0tA9iPSadMC2X6dt; SAPISID=8-N4B06I_D5N1mvR/AleccT6Zt0QllrukC; CONSENT=YES+UA.en+; OTZ=5204669_48_48_123900_44_436380; SID=rAd3UAFN_dCIGQ87HqDZZGiNyxdz0dL4dZKy_XquqSr_CHTzqSzfDdNTfLmA2xCMEZOZMA.; ANID=AHWqTUnDWUSHdvWhJiIoPxMAKYXmVtHCQIq7LBMYgiSlZZr3AMGTwY2aVUdjeY7z; NID=193=QImFbOa1vnKpflG8yJytqPXbJYJ9k8fWbIzQMGExsMa4g5oJwdnI56WNjgEVFAyAPJ1SEEOQ-zlW4HAUv-JLj0yAUImTgeT1syDIgFTMWAqxdz10lWRlzFC-3Fmjv6xJcqm2o6RKI50dmb7GetiheNdSAYPkAjng_c0lOHoXZLmtMwFOpkPTrQwVyUW8R2x4o1ux3OW3_kEbR_BREowRV8lVqrsnyo1ffC_Pm40zf81k7aS0cv9esYweGHF6Lxd532z4wA; 1P_JAR=2019-12-06-16; DV=k7BRh0-RaJtZsO9g7sjbrkcKoUjC7RYhxDh5AdfYgQAAAID1UoVsAVkvPgAAAFiry7niUB6qLgAAAGCQehpdCXeKnikKAA; SEARCH_SAMESITE=CgQIvI4B; SIDCC=AN0-TYv-lU3aPGmYLEYXlIiyKMnN1ONMCY6B0h_-owB-csTWTLX4_z2srpvyojjwlrwIi1nLdU4',
        'pragma': 'no-cache',
        'referer': 'https://www.google.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/75.0.3770.142 Chrome/75.0.3770.142 Safari/537.36'
    }
    
    results = []
    
    def fetch(self, query, page,inf):
        '''Makes HTTP GET request to fetch search results from google'''
        
        self.initial_params['q'] = query
        
        if not page:
            params = self.initial_params
        

        else:
            params = self.pagination_params
            
            params['start'] = str(page * 10 )
            params['first'] = str(page * 10 + 1)

            params['q'] = query
        
        print(inf)
        if (inf == 'Bing '):
            print("true")
            base_url = 'https://www.Bing.com/search'
        else:
            base_url = 'https://www.google.com/search'
        response = requests.get(base_url, params=params, headers=self.headers)
        print('HTTP GET request to URL: %s | Status code: %s' % (response.url, response.status_code))
        
        return response
        
    def parse(self, response):
        resp = get_source(response.url)
        links = list(resp.html.absolute_links)
        google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.',
                     'https://google.news',
                     'https://ar.wikipedia.org',
                     'https://wikipedia.org',
                      'https://play.google.com',
                     'https://twitter.com/',
                     'https://en.wikipedia.org',
                     'https://en.wikipedia.org',
                     'https://www.facebook.com',
                     'https://fr.wikipedia.org',
                     'https://www.youtube.com',
                     'http://ar.wikipedia.org',
                     'http://en.wikipedia.org',
                     'https://translate.google.com',
                    'https://books.google')
        
        for url in links[:]:
             if  url.startswith(google_domains) :
                links.remove(url)
        with open ("C:\\Users\\Planete Gaming\\Documents\\WEB SCRAPING\\Main\\url.txt","a") as f:
            for i in links : 
                f.write(i+"\n")
    def write_csv(self):
        '''Writes scpared results to CSV file'''
        
        if len(self.results):
            print('Writing results to "res.csv"... ', end='')
            
            with open('res.csv', 'w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
                
                writer.writeheader()
                

                for row in self.results:
                    writer.writerow(row)
            
            print('Done')
       
    def store_response(self, response):
        '''Stores HTML response to file for debugging parser'''
        
        if response.status_code == 200:
            print('Saving response to "res.html"... ', end='')
            
            with open('res.html', 'w') as html_file:
                html_file.write(response.text)
            
            print('Done')
        else:
            print('Bad response!')
    
    def load_response(self):
        '''Loads HTML response for debugging parser'''
        html = ''
        
        with open('res.html', 'r') as html_file:
            for line in html_file.read():
                html += line
        
        return html
        
    def run(self,query,inf,pages):
        '''Starts crawler'''

        for page in range(0, pages):
            response = self.fetch(query, page ,inf)
            
            self.parse(response)
            
            time.sleep(5)
        


if __name__ == '__main__':
    query=''
    inf =''
    pages = 0
    gg = GoogleScraper()
    gg.run(query,inf,pages)