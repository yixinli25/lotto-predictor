from lotto_predictor.fetch_data import fetch_past_numbers
from lotto_predictor.ai_predictor import get_lotto_prediction

def main():
    past_winning_numbers, past_encores = fetch_past_numbers()
    prediction = get_lotto_prediction(past_winning_numbers, past_encores)
    print(prediction)

if __name__ == "__main__":
    main()