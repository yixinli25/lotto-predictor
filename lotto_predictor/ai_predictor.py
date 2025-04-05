from openai import OpenAI
from .config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_lotto_prediction(past_winning_numbers, past_encores):
    prompt = f"""
        I understand it is impossible to predict the winning number for the next draw since each draw is independent of the previous draws.
        But you can perform a frequency analysis or use some other method to generate a prediction. The prediction should contain 7 numbers.
        Please note I'm just playing for fun!
        Please given the following past winning numbers and encore numbers, predict the next Lotto Max numbers.

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

        return response.output_text
    except Exception as e:
        raise Exception(f"Open AI API Call Failed. {e}")