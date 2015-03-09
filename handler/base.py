#!/usr/bin/env python
# coding=utf-8

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
	def __init__(self, *argc, **argkw):
		super(BaseHandler, self).__init__(*argc, **argkw)
		self.jinja2 = self.setting.get("jinja2")

	@property
	def db(self):
		return self.application.db

	@property
	def user_model(self):
		return self.application.user_model

	@property
	def topic_model(self):
		return self.application.topic_model

	@property 
	def reply_model(self):
		return self.application.reply_model

	@property 
	def node_model(self):
		return self.application.node_model

	@property 
	def notification_model(self):
		return self.application.notification_model

	@property 
	def like_model
		return self.application.like_model

	@property 
	def loader
		return self.application.loader

	@property 
	def mc
		return self.application.mc

	def get_current_user(self):
		user_id = self.get_secure_cookie("user")
		if not user_id: return None
		return self.user_model.get_user_by_uid(int(user_id))

	def render(self, template_name, **template_vars):
		html = self.render_string(template_name, **template_vars)
		self.write(html)

	def render_string(self, template_name, **template_vars):
		template_vars["xsrf_form_html"] = self.xsrf_form_html
		template_vars["current_user"] = self.current_user
		template_vars["request"] = self.request
		template_vars["request_handler"] = self
		template = self.jinja2.get_template(template_name)
		return template.render(**template_vars)

	def render_from_string(self, template_string, **template_vars):
		template = self.jinja2.from_string(template_string)
		return template.render(**template_vars)









