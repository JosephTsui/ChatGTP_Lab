from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def get_sentiments(model_name, string_arrays):
    # Initialize tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Tokenize the input strings
    inputs = tokenizer(string_arrays, padding=True, truncation=True, return_tensors="pt")

    # Initialize model
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Make predictions
    outputs = model(**inputs)

    # Softmax to convert logits to get probabilities
    predicitions = torch.nn.functional.softmax(outputs.logits, dim=-1)

    return predicitions

if __name__ == "__main__":
    model_name = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"

    string_arr = [
        "我會披星戴月的想你，我會奮不顧身的前進，遠方燈火越來越唏嘘，凝視前方身後的距離",
        "鯊魚寶寶 doo doo doo doo doo doo 鯊魚寶寶"
    ]

    predictions = get_sentiments(model_name, string_arr)
    print(predictions)