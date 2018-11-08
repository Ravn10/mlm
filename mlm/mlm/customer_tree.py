
from __future__ import unicode_literals


import frappe
from frappe.model.document import Document
from frappe.utils import flt
from frappe.utils.nestedset import NestedSet, update_nsm
# from __future__ import unicode_literals
# import frappe
# import urllib
# import copy
# from frappe import _
# import json
# import math
# from frappe.utils import nowdate, cint, cstr
# from frappe.utils.nestedset import NestedSet
# from frappe.website.website_generator import WebsiteGenerator
# from frappe.website.render import clear_cache
# from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow
# from erpnext.shopping_cart.product_info import set_product_info_for_website
# from erpnext.utilities.product import get_qty_in_stock
# from frappe.utils.html_utils import clean_html


@frappe.whitelist()
def get_children(doctype, parent=None, customer=None, is_root=False):
	if parent is None or parent == "All Customers":
		parent = ""


	fields = ['name as value', 'is_group as expandable']
	filters = [
		['ifnull(`parent_customer`, "")', '=', parent]
	]

	customers = frappe.get_list(doctype, fields=fields, filters=filters, order_by='name')

	return customers
	# return frappe.db.sql("""
	# 	select
	# 		name as value,
	# 		is_group as expandable
	# 	from
	# 		`tab{doctype}` comp
	# 	where
	# 		ifnull(parent_customer, "")={parent}
	# 	""".format(
	# 		doctype=doctype,
	# 		parent=frappe.db.escape(parent)
	# 	), as_dict=1)

@frappe.whitelist()
def add_node():
	from frappe.desk.treeview import make_tree_args
	args = frappe.form_dict
	args = make_tree_args(**args)

	if args.parent_customer == 'All Customers':
		args.parent_customer = None

	frappe.get_doc(args).insert()

@frappe.whitelist()
def validate(customer, method):
	if not customer.route:
		customer.route = ''
		if customer.parent_customer:
			parent_customer = frappe.get_doc('Customer', customer.parent_customer)

			# make parent route only if not root
			if parent_customer.parent_customer or parent_customer.route:
				customer.route = parent_customer.route + '/'
				print(customer.route)

		# customer_name = customer.customer_name.replace(' ','_').replace('-', '_').lower()
		customer.route += customer.customer_name

		return customer.route