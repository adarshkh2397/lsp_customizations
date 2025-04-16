import frappe

@frappe.whitelist()
def switch_theme(theme):
	if theme in ["Dark", "Light", "Automatic", "lsp_theme", "arp_theme"]:
		frappe.db.set_value("User", frappe.session.user, "desk_theme", theme)