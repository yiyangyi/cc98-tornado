def NotificationModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "notification"
        super(NotificationModel, self).__init__()