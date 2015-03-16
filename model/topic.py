class TopicModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "topic"
        super(TopicModel, self).__init__()
        