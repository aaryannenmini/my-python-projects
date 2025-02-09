class Pencil:
    def use(self):
        return "Using the pencil to write or draw."

class Eraser:
    def use(self):
        return "Using the eraser to erase pencil marks."

class Notebook:
    def use(self):
        return "Using the notebook to write notes or doodle."

supplies = [Pencil(), Eraser(), Notebook()]

for supply in supplies:
    print(f"{supply.__class__.__name__}: {supply.use()}")


