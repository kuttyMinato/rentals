// Copyright (c) 2024, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("parent",{
	refresh(frm) {

    },
});

frappe.ui.form.on("child",{
    refresh(frm) {

    },
    linked:function (frm, cdt, cdn){
        const child = locals[cdt][cdn];
        if (child.linked) {
            frappe.db.get_doc('Parent', child.linked).then(parent => {
                // Update child fields with parent data
                frappe.model.set_value(cdt, cdn, '', parent.name);
                frappe.model.set_value(cdt, cdn, '', parent.email);
                frappe.model.set_value(cdt, cdn, '', parent.mknlk);
            });
        }
    }   
});



