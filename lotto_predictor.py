import os
import requests
from openai import OpenAI
from datetime import datetime, timedelta
from dotenv import load_dotenv
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

past_winning_numbers = []
past_encores = []

client = OpenAI(
    api_key=os.environ.get("OPEN_AI_API_KEY"),
)

def get_end_of_month(date):
    if date.month == 12:
        next_month = date.replace(year=date.year + 1, month=1, day=1)
    else:
        next_month = date.replace(month=date.month + 1, day=1)
    
    return next_month - timedelta(days=1)

def lotto_predictor():
    olg_api_url = "https://gateway.wma.olg.ca/feeds/past-winning-numbers?"
    game_type = "lottomax"

    today = datetime.today()
    one_year_ago = today.replace(year=today.year - 1)
    start_date = one_year_ago.replace(day=1)
    end_date = get_end_of_month(one_year_ago.replace(day=1))

    headers = {
        "user-agent": "my-app/0.0.1",
        "x-client-id": os.environ.get("X_CLIENT_ID")
    }

    while end_date <= datetime.now():
        try:
            response = requests.get(
                olg_api_url + 
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
        
    prompt = f"""
        I know it is impossible to predict the winning number for the next draw and each draw is independent of the previous draws. 
        But you can perform a frequency analysis or use some other method to generate a prediction. I'm just playing for fun!
        Given the following past winning numbers and encore numbers, predict the next Lotto Max numbers.

        Past Winning Numbers: {', '.join(past_winning_numbers)}
        Past Encore Numbers: {', '.join(past_encores)}

        Predicted Next Winning Numbers:
    """

    try:
        response = client.responses.create(
            model="gpt-3.5-turbo",
            instructions="You are an assistant helping to analyze Lotto Max numbers.",
            input=prompt,
        )

        print(response.output_text)

    except Exception as e:
        raise Exception(f"Open AI API Call Failed. {e}")

if __name__ == "__main__":
    lotto_predictor()