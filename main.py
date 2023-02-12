''' This Python CLI Script uses https://www.boredapi.com/api/activity to find something interesting to do when bored. 
'''
import requests as rq
base_url = 'https://www.boredapi.com/api/activity'
payLoad = {}
print('Note: This requires a working network connection and fetches all the activities from https://www.boredapi.com, we are not responsible for erroneous answers.\n\n')
print('Welcome to this program. If you\'re bored and looking to do something interesting, let\'s find you something to do today: ')

print("\nTell me what type of activity do you want to do out of the following: \n(Enter the corresponding number)")

print('''1. Educational
       \n2. Recreational
       \n3. Social
       \n4. DIY
       \n5. Charity
       \n6. Cooking
       \n7. Relaxation
       \n8. Music
       \n9. Busywork''')
n = int(input())
if n == 1:
    payLoad.update({'type': 'education'})
elif n == 2:
    payLoad.update({'type': 'recreational'})
elif n == 3:
    payLoad.update({'type': 'social'})
elif n == 4:
    payLoad.update({'type': 'diy'})
elif n == 5:
    payLoad.update({'type': 'charity'})
elif n == 6:
    payLoad.update({'type': 'cooking'})
elif n == 7:
    payLoad.update({'type': 'relaxation'})
elif n == 8:
    payLoad.update({'type': 'music'})
elif n == 9:
    payLoad.update({'type': 'busywork'})

request = rq.get(base_url, params=payLoad)
data = request.json()
# print(data) # Shows the data received from the API
print('\nHere\'s What you can do today: ', data['activity'])
print('\n\n Re-run the script to get another suggestion to do something interesting today\n\n')
