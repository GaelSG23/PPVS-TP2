class ExcelProcessor:
    #Contructeur de la class ExcelProcessor.
    #Emmagasine le nom du dossier excel entrant et sortant 
    #ainsi que la classe SentimentAnalyzer.

    def __init__(self, input_file, output_file, analyzer):
        self.input_file = input_file
        self.output_file = output_file
        self.analyzer = analyzer