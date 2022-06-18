class SafeOpenFile:
    def __init__(self, path, type):
        self.file = open(path, type)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with SafeOpenFile('test.txt', 'wt') as file:
    file.write("Этот контекстный менеджер делает то же самое, что и 'Open'")
