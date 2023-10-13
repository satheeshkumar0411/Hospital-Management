// Copyright (c) 2023, Satheesh and contributors
// For license information, please see license.txt

frappe.ui.form.on('Patient Entry', {
	refresh: function(frm) {
		frm.disable_save();
	},
	confirm_appointment(frm) {	
		frm.call('confirm_appointment').then(r =>{	
			const mrp = frm.doc.mrp;
			const quantity = frm.doc.quantity;
			frm.set_value('total_amount', frm.doc.mrp * quantity);
		})
	},
	
});

