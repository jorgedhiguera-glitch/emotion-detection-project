function RunSentimentAnalysis() {
  const textToAnalyze = document.getElementById("textToAnalyze").value;
  const request = new XMLHttpRequest();

  request.onreadystatechange = function handleResponse() {
    if (this.readyState === 4 && this.status === 200) {
      document.getElementById("system_response").textContent = this.responseText;
    }
  };

  const query = encodeURIComponent(textToAnalyze);
  request.open("GET", `/emotionDetector?textToAnalyze=${query}`, true);
  request.send();
}
