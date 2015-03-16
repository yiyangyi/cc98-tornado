#!/usr/bin/env python
# coding=utf-8

class UserModel(Query): 
	def __init__(self, db):
		self.db = db
		self.table_name = 'user'
		super(UserModel, self).__init__()


