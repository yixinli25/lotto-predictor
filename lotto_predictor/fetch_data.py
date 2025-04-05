import requests
from datetime import datetime
from .utils import get_end_of_month
from .config import LOTTO_URL, LOTTO_X_CLIENT_KEY

def fetch_past_numbers(game_type="lottomax"):
    past_winning_numbers = []
    past_encores = []

    today = datetime.today()
    one_year_ago = today.replace(year=today.year - 1)
    start_date = one_year_ago.replace(day=1)
    end_date = get_end_of_month(one_year_ago.replace(day=1))

    headers = {
        "user-agent": "my-app/0.0.1",
        "x-client-id": LOTTO_X_CLIENT_KEY
    }

    while end_date <= datetime.now():
        try:
            response = requests.get(
                LOTTO_URL + 
                "game=" + game_type + 
                "&startDate=" + start_date.strftime("%Y-%m-%d") + 
                "&endDate=" + end_date.strftime("%Y-%m-%d"), 
                headers=headers
            )

            response_json = response.json()

            draws = response_json["response"]["winnings"]["lottomax"]["draw"]

            for draw in draws:
                past_winning_numbers.append(draw["main"]["regular"])
                past_encores.append(draw["encore"]["number"])

            if start_date.month == 12:
                start_date = start_date.replace(year=start_date.year + 1, month=1, day=1)
            else:
                start_date = start_date.replace(month=start_date.month + 1, day=1)

            end_date = get_end_of_month(start_date)

        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
        
    return past_winning_numbers, past_encores