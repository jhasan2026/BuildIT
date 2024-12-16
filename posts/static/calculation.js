
const booking = document.getElementById('instalment')
const tax = document.getElementById('tax')



const booking_cost = Number(booking.getAttribute("data-value"))
const tax_cost = Number(tax.getAttribute("data-value"))

document.getElementById('total').textContent = booking_cost + tax_cost