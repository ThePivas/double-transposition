class Table:
    def __init__(self, cipher, rows, cols):
        self.rows = rows
        self.cols = cols
        self.content = []
        self.__set_content(cipher)

    def __set_content(self, cipher):
        position = 0
        for i in range(self.rows):
            col = []
            for j in range(self.cols):
                col.append((str(cipher)[position]).lower())
                position += 1
            self.content.append(col)

    def get_columnar_transcript(self):
        transcript = ""
        for i in range(self.cols):
            for j in range(self.rows):
                transcript += self.content[j][i]
        return transcript
