import requests, csv
from bs4 import BeautifulSoup

page = requests.get('https://www.imdb.com/list/ls043474895/')
soup = BeautifulSoup(page.text, 'html.parser')

movies = soup.find_all('div', class_='lister-item-content')
information = []
def get_info():
    for movie in movies:
        rating = movie.find('span', class_="ipl-rating-star__rating").get_text()
        if float(rating) >= 7:
            title = movie.h3.find('a').get_text()
            
            
            url = movie.h3.a['href']
            full_url = f'https://www.imdb.com{url}?ref_=tts_li_tt'

            genre = movie.p.find('span', class_='genre').get_text().strip()

            rating = rating

            info = [title, full_url, genre]
            information.append(info)
            

def save_to_csv():
    with open('movies.csv', 'w', newline='') as myfile:
        writer = csv.writer(myfile)
        headers = ['Name', 'URL', 'Genre']
        writer.writerow(headers)
        writer.writerows(information)

get_info()
save_to_csv()