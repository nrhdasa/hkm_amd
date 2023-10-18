// Copyright (c) 2023, HKM Ahmedabad and contributors
// For license information, please see license.txt

frappe.ui.form.on('DB Donor', {
    refresh: function(frm) {
        if (frm.doc.mobile_no) {
            frappe.call({
                method: 'calculate_sms_count',
                doc: frm.doc,
                callback: function(r) {
                    if (r.message) {
                        frm.set_value('sms_count', r.message);
                    }
                }
            });
        }
    }
});

