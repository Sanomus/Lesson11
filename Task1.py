import requests


def join_request(url='https://api.giphy.com/v1/gifs/search?',api_key='api_key=qvP4thm8ABFcQBEx09JpYD0ITKH7V2bw',search_word='cheese',search_quantity='20',offset='0',raiting='g',language='en',bundle='messaging_non_clips'):

    search_word = 'q='+search_word
    search_quantity = 'limit='+search_quantity
    offset = 'offset='+offset
    raiting = 'rating='+raiting
    language = 'lang='+language
    bundle = 'bundle='+bundle


    return url+'&'.join([api_key,search_word,search_quantity,offset,raiting,language,bundle])


resp = requests.get(join_request(search_word='apple', search_quantity='10'))
print(resp.status_code)


data = resp.json()['data']
links = []
for i in data:
    links.append(i['url'])
                 
print('Quantity of get gifs', len(links))
for link in links:
    print(link)
