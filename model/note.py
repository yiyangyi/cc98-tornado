class NoteModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "note"
        super(NoteModel, self).__init__()