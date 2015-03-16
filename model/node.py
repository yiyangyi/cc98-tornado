class NodeModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "node"
        super(NodeModel, self).__init__()