class VoteModel(Query):
    def __init__(self):
        self.db = db
        self.table_name = "vote"
        super(VoteModel, self).__init__()