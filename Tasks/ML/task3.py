import requests
from bs4 import BeautifulSoup
from rake_nltk import Rake
from urllib import parse

def gettext(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}

    try:
        # загружаем страницу
        r = requests.get(url, headers=headers)
        char_set = r.encoding
        html_text = r.text
        soup = BeautifulSoup(html_text)

        # удаляем лишний текст на странице (js-скрипты и стили)
        for script in soup(["script", "style"]):
            script.extract()

        ### достаем текст файла
        text = soup.get_text()
        # lines = (line for line in text.splitlines())
        # chunks = [phrase.strip() for line in lines for phrase in line.split(" ")]
        # textT1 = '\n'.join(chunk.strip('-|,.!@#$?-%^&*()…...') for chunk in chunks if chunk)


        ### достаем все заголовки для T2
        h_list = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'p']
        textT2 = []

        for hn in h_list:
            hn_list = soup.find_all(hn, href=False)
            for h in hn_list:
                lines = h.text.strip('-|,!@#$?%^&*()…... ').splitlines()
                chunks = [phrase.strip(' ') for line in lines for phrase in line.split(" ") if phrase]
                textT2.append('\n'.join(chunk.strip('-|,!@#$?-%^&*()…... ') for chunk in chunks if len(chunk) > 1))

        ### Достаем все текста с url ну и пусть url тоже будет храниться
        # textT3 = [i.text.strip() for i in soup.find_all(['a', 'p'], href=True)]

        return textT2
    except Exception as e:
        print(f'{url}', e)



def getKeywords(texts):
    # Получаем список ключевых слов из каждого текста
    r = Rake(language='russian', punctuations= [')', '(', ',', '.', ':', '),', '«', '»', '+', '!', '..', '...', '?',
                                                '~', '"', '".', '-', '.,', '!!!', ').', '8', '!!!!!!!', '@', '».', '?-',
                                                '((((', '%', '1', '2', '3', '4', '5', '6', '7', '9', '0', '…', '….',
                                                '$', '#', '&', '%', '....', '?»', '®', '*'])
    r.extract_keywords_from_sentences(texts)
    # Производим отбор самых важных из них
    T_min = 1.35

    keywordsT1 = [x for x in r.get_ranked_phrases_with_scores() if x[0] >= T_min and x is not None]

    return [x for x in keywordsT1]

if __name__ == '__main__':
    lst = [
            ('https://www.woman.ru/health/medley7/thread/3834906/26/', 8),
            ('https://www.isramedportal.ru/communities/rak-mozga/forum', 7),
            ('https://media.nenaprasno.ru/articles/kolonki/pape-otmerili-8-mesyatsev-ugasaniya-no-proshlo-dva-goda-i-eto-vpolne-normalnaya-zhizn/', 5),
            ('https://forum.ngs.ru/board/health/flat/1876385339/?fpart=1&per-page=50#Post1876399170', 4),
            ('https://03ru.com/viewtopic.php?p=11323&hilit=%D0%BE%D0%BF%D1%83%D1%85%D0%BE%D0%BB%D1%8C+%D0%BC%D0%BE%D0%B7%D0%B3%D0%B0#p11323', 1),
            ('http://www.rakpobedim.ru/forum/index.php?/topic/1079-%d1%80%d0%b0%d0%ba-%d0%bc%d0%be%d0%b7%d0%b3%d0%b0-%d1%87%d1%82%d0%be-%d0%b4%d0%b5%d0%bb%d0%b0%d1%82%d1%8c/', 9),
            ('https://www.woman.ru/health/medley7/thread/4658891/', 2),
            ('https://www.woman.ru/health/medley7/thread/4600847/', 1),
            ('https://www.woman.ru/kids/teens/thread/5768875/', 3)
    ]

    nltk = []

    for i, data in enumerate(lst):
        url, rating = data
        site_name = parse.urlsplit(url).netloc
        text = gettext(url)
        rate = getKeywords(text)
        nltk.append(sorted(list(set(rate)), reverse=True))

    for i in nltk:
        print(i)
