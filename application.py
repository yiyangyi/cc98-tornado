#!/usr/bin/env python
# coding=utf-8
# 
# Copyright 2015 cc98.org

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os.path
import re
import memcache
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from jinja2 import Environment, FileSystemLoader

# Define a new command line option
define("port", default = 80, type = int, help = "run on the given port")
define("mysql_host", default = "mysql_host", help = "community database host")
define("mysql_database", default = "mysql_database", help = "community database name")
define("mysql_user", default = "mysql_db_user", help = "community database user")
define("mysql_pwd", default = "mysql_db_pwd", help = "community database pwd")

class Application(tornado.web.Application):
	def __init__(self):
		settings = dict(

		)

		handlers = [
			(),
		]

		tornado.web.Application.__init__(self, handlers, settings)

		# Have one global connection to the blog DB  across all the handlers
		self.db = torndb.Connection(

		)

		# Have one global session controller


		# Have one global memcache controller
		self.mc = memcache.Client(["127.0.0.1:11211"]])


def main():
	tornado.options.parse_command_line()
	httpserver = tornado.httpserver.HTTPServer(Application())
	httpserver.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ = "__main__": 
	main()
















