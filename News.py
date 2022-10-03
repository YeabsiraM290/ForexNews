from bs4 import BeautifulSoup
from datetime import datetime
import urllib


class News:

    @staticmethod
    def getNews():
        url = "https://www.forexfactory.com/calendar?day=today"
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        response = opener.open(url)
        result = response.read().decode('utf-8', errors='replace')
        soup = BeautifulSoup(result, "lxml")
        today_date = datetime.today().strftime('%Y-%m-%d')

        data_table = soup.find("table", {"class": "calendar__table"})
        news_row = data_table.select("tr.calendar__row.calendar_row")

        data = {"Date": today_date, "Currencies": []}

        for row in news_row:

            impact = row.find("div", {
                "class": "calendar__impact-icon calendar__impact-icon--screen"}).findChild()['class'][0]

            if impact in ["high", "medium"]:

                Currency = row.find(
                    "td", {"class": ["currency", "calendar__currency"]}).text.strip()
                Time = row.find_all(
                    "td", {"class": "calendar__time"})[0].text.strip()

                currency = {"name": Currency, "Time": Time, "Impact": impact}

                data["Currencies"].append(currency)

        print(data)

        return data

News.getNews()
