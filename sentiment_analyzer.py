
from transformers import pipeline
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

tokenizer = DistilBertTokenizer.from_pretrained
class SentimentAnalyzer:
 
    #Contructeur de la class SentimentAnalyzer. Emmagasine le model dans la classe.
    def __init__(self, model_name):
        tokenizer = DistilBertTokenizer.from_pretrained(model_name)
        model = DistilBertForSequenceClassification.from_pretrained(model_name)
        self.nlp = pipeline(
            "sentiment-analysis",
            model=model,
            tokenizer=tokenizer
        )

    #Calcule le score en supressant le resultat positif du commentaire avec le resultat negatif.
    def calculate_score(self, comment):

        results = self.nlp(comment)[0]

        #Crée un dicationnaire avec le resultat Negatif et Positif de chaque commentaire.
        label = results["label"].lower()
        confidence = results["score"]


        if label == "positive":
            score = confidence
        elif label == "neutral":
            score = 0
        elif label == "negative":
            score = -confidence

        return score