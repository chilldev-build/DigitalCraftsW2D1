## 9/3/19 Day 4 Morning Python Exercises

# Day of the week input and return

#day = int(input('Day (0-6)? '))
#
#if day == 0:
#    print('Sunday')
#elif day == 1:
#    print('Monday')
#elif day == 2:
#    print('Tuesday')
#elif day == 3:
#    print('Wednesday')
#elif day == 4:
#    print('Thursday')
#elif day == 5:
#    print('Friday')
#elif day == 6:
#    print('Saturday')
#else:
#    print('You failed to enter 0-6!')

# Work or sleep in?

#day = int(input('Day (0-6)? '))
#
#if (day == 0) or (day == 6):
#    print('Sleep in')
#elif (day >= 1) and (day <= 5):
#    print('Go to work')
#else:
#    print('You failed to enter 0-6!')
#

# Celsius to Fahrenheit
#
#celcius = int(input('Enter the temperature in degrees celsius? '))
#
#print(float(celcius * 1.8 + 32), "degrees F")

# Tip Calculator

total_bill = float(input("What is the bill total? "))
service_level = input("Was the service good, fair or bad? ")


if service_level.lower() == 'good':
    print('Tip Amount = ' + str(float(.2 * total_bill)))
    print('Total Amount = ' + str(float(.2 * total_bill) + total_bill))
elif service_level.lower() == 'fair':
    print('Tip Amount = ' + str(float(.15 * total_bill)))
    print('Total Amount = ' + str(float(.15 * total_bill) + total_bill))
elif service_level.lower() == 'bad':
    print('Tip Amount = ' + str(float(.1 * total_bill)))
    print('Total Amount = ' + str(float(.1 * total_bill) + total_bill))


