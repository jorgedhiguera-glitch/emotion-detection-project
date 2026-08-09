"""Provide the Flask web server for the emotion-detection application."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector


APP = Flask(__name__)


@APP.route("/emotionDetector")
def emotion_analyzer():
    """Analyze the text received from the web interface."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score} and "
        f"'sadness': {sadness_score}. The dominant emotion is "
        f"{dominant_emotion}."
    )


@APP.route("/")
def render_index_page():
    """Render the application's home page."""
    return render_template("index.html")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
