import json
from pprint import pprint
from requests import Session
from bs4 import BeautifulSoup


class GoodReadsScraper:
    def __init__(self):
        self.url = None

    def scrape(self, url: list):
        self.url = url
        all_data = []
        for elem in self.url:
            with Session() as session:
                response = session.get(elem, timeout=10)

                assert response.status_code == 200, 'Bad response'
                print(response.status_code)

            soup = BeautifulSoup(response.content, 'html.parser')

            title = soup.select('#bookTitle')
            author = soup.select('#bookAuthors span div a span')
            rating = soup.select('span[itemprop = "ratingValue"]')
            text = soup.select('#description span')
            img_url = soup.select('#coverImage')
            reviews = [review.text for review in
                       soup.select('.reviewText span span')]

            data = {
                'title': title[0].text.strip(),
                'author': author[0].text.strip(),
                'rating': float(rating[0].text.strip()),
                'text': text[1].text.strip(),
                'img_url': img_url[0]['src'],
                'reviews': reviews
            }
            all_data.append(data)

        pprint(all_data)
        with open('book.json', 'w') as file:
                json.dump(all_data, file, indent=4)


def main():
    scrape1 = GoodReadsScraper()
    scrape1.scrape(['https://www.goodreads.com/book/show/136251',
                    'https://www.goodreads.com/book/show/29056083-'
                    'harry-potter-and-the-cursed-child',
                    'https://www.goodreads.com/book/show/1.Harry_'
                    'Potter_and_the_Half_Blood_Prince'])


if __name__ == '__main__':
    main()
