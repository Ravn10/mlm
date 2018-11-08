frappe.treeview_settings["Customer"] = {
	ignore_fields: ["parent_customer"],
	get_tree_nodes: 'mlm.mlm.customer_tree.get_children',
	add_tree_node: 'mlm.mlm.customer_tree.add_node',
	// filters: [
	// 	{
	// 		fieldname: "location",
	// 		fieldtype: "Link",
	// 		options: "Location",
	// 		label: __("Location"),
	// 		get_query: function () {
	// 			return {
	// 				filters: [["Location", "is_group", "=", 1]]
	// 			};
	// 		}
	// 	},
	// ],
	root_label: "All Customers",
	get_tree_root: false,
	// menu_items: [
	// 	{
	// 		label: __("New Location"),
	// 		action: function () {
	// 			frappe.new_doc("Location", true);
	// 		},
	// 		condition: 'frappe.boot.user.can_create.indexOf("Location") !== -1'
	// 	}
	// ],
	onload: function (treeview) {
		treeview.make_tree();
	}
};