// Copyright (c) 2023, Satheesh and contributors
// For license information, please see license.txt

frappe.ui.form.on('Refill Medicine Details', {
	refresh: function(frm) {
		frm.disable_save();
	},
	refill_item(frm) {	
		frm.call('refill_item').then(r =>{	
		})
	},
});
