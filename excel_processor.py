class ExcelProcessor:
    #Contructeur de la class ExcelProcessor.
    #Emmagasine le nom du dossier excel entrant et sortant 
    #ainsi que la classe SentimentAnalyzer.

    def __init__(self, input_file, output_file, analyzer):
        self.input_file = input_file
        self.output_file = output_file
        self.analyzer = analyzer

    def load_workbook(self):
        #Ouvre le dossier excel avec le chemin et retourne la première page et le dossier.

        workbook = load_workbook(self.input_file)
        sheet = workbook.active

        return workbook, sheet