"""Módulo de detección de emociones mediante Watson NLP."""

import requests


WATSON_NLP_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

WATSON_NLP_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyse):
    """Analiza un texto y devuelve sus emociones y la emoción dominante."""
    input_json = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(
        WATSON_NLP_URL,
        headers=WATSON_NLP_HEADERS,
        json=input_json,
        timeout=30,
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted_response = response.json()
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": max(emotions, key=emotions.get),
    }
