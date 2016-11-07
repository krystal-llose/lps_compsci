print('Enter amount of purchases, in cents.')
purchase = int(raw_input())

if purchase > 1000:
	amount = purchase * 0.10
	final_price = purchase - int(amount)
	print('You spent over $10! Your final price is ' + str(final_price) + ' cents.')

if purchase <= 1000:
	print('Your final price is ' + str(purchase) + ' cents.')






