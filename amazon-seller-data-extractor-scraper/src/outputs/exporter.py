thonimport json

class Exporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def export(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)