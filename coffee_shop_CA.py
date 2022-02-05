import sys
from utils import print_message, get_size, order_latte

def coffee_bot():
  print('Welcome to the cafe!')
  drinks = []
  order_drinks = True
  while order_drinks:
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)
    while True:
      order_drinks = input('Would you like to order another drink? (y/n)\n>')
      if order_drinks in ['y', 'yes', 'sure']:
        order_drinks = True
        break
      
      elif order_drinks in ['n', 'no']:
        order_drinks = False
        break

  print('Okay, so I have:')
  for drink in drinks:
    print('-', drink)
  
  #name = input('Can I get your name please? \n> ')
  #print('Thanks, {}! Your order will be ready shortly.'.format(name))

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  stop_words = ['bye', 'stop']
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  elif res in stop_words:
    print("order cancelled")
    sys.exit()
  else:
    print_message()
    return get_drink_type()
  
# Define new functions here!
def order_mocha():
  while True:
    res = input('Would you like to try our limited edition peppermint mocha \n[a] Sure! \n[b] Maybe next time! \n>')

    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'
    
    print_message()


coffee_bot()
