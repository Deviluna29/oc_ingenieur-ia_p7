import pandas as pd
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client(key, endpoint):
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

# Function for detecting sentiment in text
def sentiment_analysis(client, data):

    batch_size = 10

    X = data["text"].values
    positive = []
    neutral = []
    negative = []

    for i in range (0, len(X), batch_size):

        batch = [text for text in X[i : i + batch_size]]
        response = client.analyze_sentiment(batch)

        for idx, sentence in enumerate(response):

            positive.append(sentence.confidence_scores.positive)
            neutral.append(sentence.confidence_scores.neutral)
            negative.append(sentence.confidence_scores.negative)

    d = {'text': data['text'].values, 'positive': positive, 'neutral': neutral, 'negative': negative, 'target': data['target'].values}

    return pd.DataFrame(data=d)