
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
from frappe import _, msgprint, scrub
from frappe.utils import nowdate, cint, cstr
# from frappe.utils.nestedset import NestedSet
# from frappe.website.website_generator import WebsiteGenerator
# from frappe.website.render import clear_cache
# from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow
# from erpnext.shopping_cart.product_info import set_product_info_for_website
# from erpnext.utilities.product import get_qty_in_stock
# from frappe.utils.html_utils import clean_html


@frappe.whitelist()
def validate(sales_invoice, method):
	sales_invoices = frappe.db.get_list("Sales Invoice", 
						filters={"status": "Paid", "posting_date": nowdate()},
						fields=["name", "route", "total_distribution_amt"])

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
						'credit_in_account_currency': 0.3* flt(x.total_distribution_amt),
						'debit_in_account_currency': 0
				})

			elif arr.index(y) > 0 and arr.index(y) < 8:
				row.append({
						'account': frappe.db.get_single_value("MLM Settings", "debtors_account"),
						'party_type': 'Customer',
						'party': customer.name,
						'credit_in_account_currency': 0.1* flt(x.total_distribution_amt),
						'debit_in_account_currency': 0
				})

			elif arr.index(y) > 7 and arr.index(y) < 10:
				row.append({
						'account': frappe.db.get_single_value("MLM Settings", "debtors_account"),
						'party_type': 'Customer',
						'party': customer.name,
						'credit_in_account_currency': 0.05* flt(x.total_distribution_amt),
						'debit_in_account_currency': 0
				})
	
		print(row)
	# 	joiningjv = frappe.get_doc({
	# 	'doctype': 'Journal Entry',
	# 	'is_ewallet_entry': 1,
	# 	'type': 'Joining Bonus',
	# 	'posting_date': nowdate(),
	# 	'voucher_type': 'Journal Entry',
	# 	'accounts': row,
	# 	'user_remark': 'Referal bonus.'
	# 	}).insert(ignore_permissions=True)
		
