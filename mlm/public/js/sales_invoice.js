
frappe.ui.form.on('Sales Invoice', {
	refresh: function(frm) {
        frm.add_custom_button(__('Set'), function() {
        	frappe.call({
        		method: "mlm.mlm.sales.validate",
        		args: {},
        		callback: function (r) {
        			console.log(r.message)
        		}
        	});
        });
	}
});
