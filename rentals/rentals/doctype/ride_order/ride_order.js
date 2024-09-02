// Copyright (c) 2024, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    on_load(frm) {
        
    },
    refresh(frm) {
        if (frm.doc.status === "New") {
            frm.add_custom_button("Accept", () => {
                // frappe.show_alert("Button Clicked...!!!");
                frm.set_value("status", "Accepted");
                frm.save();
            }, "Actions")
       
            frm.add_custom_button("Reject", () => {
                // frappe.show_alert("Button Clicked...!!!");
                frm.set_value("status", "Rejected");
                frm.save();
            }, "Actions")
        }
	},
});
