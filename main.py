
from sentiment_analyzer import SentimentAnalyzer
from excel_processor import ExcelProcessor


model_name = (
    "Yuu-Xie/distilbert-base-multilingual-cased-sentiment"
)

input_file = "5d5TP2a - liste commentaires - vEtu.xlsx"
output_file = "resultats_sentiment.xlsx"

analyzer = SentimentAnalyzer(model_name)

processor = ExcelProcessor(
    input_file,
    output_file,
    analyzer
)

processor.process_file()