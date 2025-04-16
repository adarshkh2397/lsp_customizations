$(document).ready(function () {

	const boot = frappe.boot;
	const userPermissions = boot?.user?.user_permissions;

	let company = "";

	if (userPermissions?.Company){
		company = userPermissions?.Company[0].doc;
		//console.log(company);
	}

	if(company === ""){
		company = frappe?.boot?.user?.defaults?.company;
	}

	let logoPath = "";

	if (company === "Lakeshore Products") {
		logoPath = "/files/lsp-logo-large.avif";
	} else if (company === "Alumiramp") {
		logoPath = "/files/lifts.avif";
	}

	if (logoPath) {
		const $logo = $(".navbar-brand .app-logo");
		if ($logo.length) {
			$logo.attr("src", logoPath);
		}
	}
});