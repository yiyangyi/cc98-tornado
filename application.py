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

import handler.base
import handler.user
import handler.topic
import handler.page
import handler.notification

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
			blog_title = u"CC98 Forum",
			template_path = os.path.join(os.path.dirname(__file__), "templates"),
			static_path = os.path.join(os.path.dirname(__file__), "static"),
			xsrf_cookies = True,
			cookie_secret = "xxxxxxxxxxxxx",
			login_url = "/login",
			autoescape = None,
			jinja2 = Environment(loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")), trim_blocks = True),
		)

		handlers = [
			(r"/", handler.topic.IndexHandler),
            (r"/login", handler.user.LogoutHandler),
            (r"/logout", handler.user.LogoutHandler),
            (r"/forgot", handler.user.ForgotPasswordHandler),
            (r"/register", handler.user.RegisterHandler),
            (r"/setting/avatar", handler.user.SettingAvatarHandler),
            (r"/setting/gravatar", handler.user.SettingAvatarFromGravatarHandler),
            (r"/setting/password", handler.user.SettingPasswordHandler),
            (r"/vote", handler.topic.VoteHandler),
            (r"/favorites", handler.topic.FavoriteHandler),
            (r"/unfavorites", handler.topic.CancelFavoriteHandler),
            (r"/topic/(\d+)", handler.topic.ViewHandler),
            (r"/topic/create", handler.topic.CreateHandler),
            (r"/topic/edit", handler.topic.EditHandler),
            (r"/reply/edit/(.*)", handler.topic.ReplyEditHandler),
            (r"/node/(.*)", handler.topic.NodeTopicHandler),
            (r"/user/(.*)", handler.user.ProfileHandler),
            (r"/user/(.*)/topics", handler.user.UserTopicsHandler),
            (r"/user/(.*)/replies", handler.user.UserRepliesHandler),
            (r"/user/(.*)/favorites", handler.user.UserFavoritesHandler),
            (r"/members", handler.user.MembersHandler),
            (r"/notifications", handler.notification.ListHandler),
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
















