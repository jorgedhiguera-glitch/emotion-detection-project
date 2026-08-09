"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify the dominant emotion returned for representative texts."""

    @staticmethod
    def _watson_response(dominant_emotion):
        """Build a simulated Watson response for an isolated unit test."""
        emotions = {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01,
        }
        emotions[dominant_emotion] = 0.96
        response = Mock()
        response.json.return_value = {
            "emotionPredictions": [{"emotion": emotions}]
        }
        return response

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        """The joy statement must return joy as the dominant emotion."""
        mock_post.return_value = self._watson_response("joy")
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        """The anger statement must return anger as the dominant emotion."""
        mock_post.return_value = self._watson_response("anger")
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        """The disgust statement must return disgust as the dominant emotion."""
        mock_post.return_value = self._watson_response("disgust")
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        """The sadness statement must return sadness as the dominant emotion."""
        mock_post.return_value = self._watson_response("sadness")
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, mock_post):
        """The fear statement must return fear as the dominant emotion."""
        mock_post.return_value = self._watson_response("fear")
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
