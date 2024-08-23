// Copyright (c) 2023, ERPGulf and contributors
// For license information, please see license.txt

// frappe.ui.form.on("whatsapp message", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("whatsapp message", {
    refresh: function(frm) {
       
      frm.add_custom_button(__("Send"), function() {
        
        frm.call("msg", {
			apikey: frm.doc.apikey,
			recipient :frm.doc.to,
			message_url:frm.doc.message_url,
			messagebody:frm.doc.messagebody,
			srcname:frm.doc.srcname,
			source:frm.doc.source
        
				}).then(r => {
			frappe.msgprint(r.message);; 	
			})
			}, __("Send Test Message"));
    }
});
  
