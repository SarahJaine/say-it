import $ from 'jquery'
import 'foundation'
import 'foundation-mediaquery'
import 'foundation-responsivemenu'
import 'foundation-responsivetoggle'
import 'intl-tel-input'

// Initialize foundation
$(document).foundation()

// Initialize international phone object
let phone = $("#id_phone").attr('type', 'tel')
let fancyPhone = phone.intlTelInput({
	utilsScript: "../utils.js",
	preferredCountries: ['us', 'fr'],
})

// Autoformat phone number as user types
phone.on("keyup change", function(e) {
	if (e.keyCode != 8 && e.keyCode != 46) {
		let input = phone.intlTelInput("getNumber")
		let digitCount = input.length;
		if (input.slice(0,2) == "+1") {
			if (digitCount == 5) {
				phone.val(`(${input.slice(2,5)}) `)
			}
			if (digitCount == 8) {
				phone.val(`(${input.slice(2,5)}) ${input.slice(5,8)}-`)
			}
		} else if (input.slice(0,3) == "+33") {
			if (digitCount == 5) {
				phone.val(`${input.slice(3,5)} `)
			}
			if (digitCount == 7) {
				phone.val(`${input.slice(3,5)} ${input.slice(5,7)} `)
			}
			if (digitCount == 9) {
				phone.val(`${input.slice(3,5)} ${input.slice(5,7)} ${input.slice(7,9)} `)
			}
			if (digitCount == 11) {
				phone.val(`${input.slice(3,5)} ${input.slice(5,7)} ${input.slice(7,9)} ${input.slice(9,11)} `)
			}
		}
	}
})

// Autoformat phone number when country is changed
phone.on("countrychange", function(e, countryData) {
	let input = phone.intlTelInput("getNumber")
	let digitCount = input.length;
	if (digitCount > 1) {
		if (countryData.name == "France") {
			if (digitCount > 11) {
				phone.val(`${input.slice(3,5)} ${input.slice(5,7)} ${input.slice(7,9)} ${input.slice(9,11)} ${input.slice(11,13)}`)
			} else if (digitCount > 9){
				phone.val(`${input.slice(3,5)} ${input.slice(5,7)} ${input.slice(7,9)} ${input.slice(9,11)}`)
			} else if (digitCount > 7) {
				phone.val(`${input.slice(3,5)} ${input.slice(5,7)} ${input.slice(7,9)}`)
			} else if (digitCount > 5) {
				phone.val(`${input.slice(3,5)} ${input.slice(5,7)}`)
			} else {
				phone.val(`${input.slice(3,5)}`)
			}
  		} else if (countryData.name == "United States") {
  			if (digitCount > 8) {
  				phone.val(`(${input.slice(2,5)}) ${input.slice(5,8)}-${input.slice(8,12)}`)
			} else if (digitCount > 5) {
				phone.val(`(${input.slice(2,5)}) ${input.slice(5,8)}`)
			} else {
				phone.val(`(${input.slice(2,5)}`)
			}
  		}
	}
});

// Create function to apply formatted international number to hidden phone input
function storeFancyPhoneValue(idVisable, idHidden) {
	let dialCode = $(idVisable).intlTelInput("getSelectedCountryData")['dialCode']
	let seven = $(idVisable).val()
	let fullNumber = `+${dialCode} ${seven}`
	$(idHidden).val(fullNumber)
}

// On form submit, call storing function
$("#submit").click(function() {
	storeFancyPhoneValue("#id_phone","#id_phone_hidden")
})
