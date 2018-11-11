# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mlm"
app_title = "Mlm"
app_publisher = "Crisco Consulting"
app_description = "Multi Level Marketing"
app_icon = "octicon octicon-file-directory"
app_color = "Blue"
app_email = "support@criscoconsulting.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mlm/css/mlm.css"
# app_include_js = "/assets/mlm/js/mlm.js"

# include js, css files in header of web template
# web_include_css = "/assets/mlm/css/mlm.css"
# web_include_js = "/assets/mlm/js/mlm.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doctype_tree_js = {
	"Customer" : "public/js/customer_tree.js"
}
# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "mlm.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mlm.install.before_install"
# after_install = "mlm.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mlm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	"Customer": {
		"validate": "mlm.mlm.customer_tree.validate"
	},
	"Sales Invoice": {
		"validate": "mlm.mlm.sales.validate"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mlm.tasks.all"
# 	],
# 	"daily": [
# 		"mlm.tasks.daily"
# 	],
	# "hourly": [
	# 	"mlm.mlm.customer_tree.hourly"
	# ],
# 	"weekly": [
# 		"mlm.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mlm.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mlm.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mlm.event.get_events"
# }

