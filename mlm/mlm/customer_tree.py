
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


@frappe.whitelist()
def validate(sales_invoices, method):
	sales_invoices = frappe.db.get_list("Sales Invoice", 
						filters={"status": "Paid", "posting_date": nowdate()},
						fields=["name", "route", "total_distribution_amount"])

	for x in sales_invoices:
		arr = x.route.split("/")
		arr = arr[::-1]

		row = []
		for y in arr:
			if y == x.customer:
				row.append({
						'account': frappe.db.get_single_value("MLM Settings", "debtors_account"),
						'party_type': 'Customer',
						'party': customer.name,
						'credit_in_account_currency': 0.3* flt(x.total_distribution_amount),
						'debit_in_account_currency': 0
				})

			elif arr.index(y) > 0 and arr.index(y) < 8:
				row.append({
						'account': frappe.db.get_single_value("MLM Settings", "debtors_account"),
						'party_type': 'Customer',
						'party': customer.name,
						'credit_in_account_currency': 0.1* flt(x.total_distribution_amount),
						'debit_in_account_currency': 0
				})

			elif arr.index(y) > 7 and arr.index(y) < 10:
				row.append({
						'account': frappe.db.get_single_value("MLM Settings", "debtors_account"),
						'party_type': 'Customer',
						'party': customer.name,
						'credit_in_account_currency': 0.05* flt(x.total_distribution_amount),
						'debit_in_account_currency': 0
				})
	

	joiningjv = frappe.get_doc({
	'doctype': 'Journal Entry',
	'is_ewallet_entry': 1,
	'type': 'Joining Bonus',
	'posting_date': nowdate(),
	'voucher_type': 'Journal Entry',
	'accounts': row,
	'user_remark': 'Referal bonus.'
	}).insert(ignore_permissions=True)
	
