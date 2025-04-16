frappe.ui.ThemeSwitcher = class CustomThemeSwitcher extends frappe.ui.ThemeSwitcher {
	constructor() {
		super()
	}

	fetch_themes() {
		return new Promise((resolve) => {
			this.themes = [
				{
					name: "light",
					label: ("Frappe Light"),
					info: ("Light Theme"),
				},
				{
					name: "dark",
					label: "Timeless Night",
					info: "Dark Theme",
				},
				{
					name: "lsp_theme",
					label: "LSP Desk UI",
					info: "Theme for employees of LSP"
				},
				{
					name: "arp_theme",
					label: "ARP Desk UI",
					info: "Theme for employees of ARP"
				},
				{
					name: "automatic",
					label: "Automatic",
					info: "Uses system's theme to switch between light and dark mode",
				}
			];

			resolve(this.themes);
		});
	}
}