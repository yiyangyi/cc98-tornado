class SectionModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "section"
        super(SectionModel, self).__init__()