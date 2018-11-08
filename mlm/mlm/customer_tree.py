
from __future__ import unicode_literals

import json
import math
import frappe
from frappe import _
# from frappe.model.document import Document
# from frappe.utils import flt
# from frappe.utils.nestedset import NestedSet, update_nsm


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

