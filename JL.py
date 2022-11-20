import amino
import concurrent.futures
emails=["xamino18271@wuuvo.com"]
client = amino.Client()
pas="......."'
def spam(ch,num):	
	try:
		subclient.join_chat(chatId=ch)
		subclient.leave_chat(chatId=ch)
		print("\033[1;93mSpaming...",num)
	except:
		print("ld blocked by host/Kicked")
def thread():
	with concurrent.futures.ThreadPoolExecutor() as executor:
		_ = [executor.submit(spam,id,num) for num in range(15000)]
		
for email in emails:
	try:
		client.login(email=email,password=pas)
		print("Logged in using ",email)
	except amino.lib.util.exceptions.VerificationRequired:
		print("Verification required")
		try:
			client.login(email=email,password=pas)
		except Exception as e:
			print(e)
			s=input("\nWaiting for verification...")
			client.login(email=email,password=pas)
			print("Logged in using ",email)
	except:
		print("Error")
		break
	f=input("Enter chat link :-")
	fok=client.get_from_code(f)
	id=client.get_from_code(f).objectId
	cid=fok.path[1:fok.path.index("/")]
	print("comid=",cid)
	print()
	try:
		client.join_community(comId=cid)
		subclient=amino.SubClient(comId=cid,profile=client.profile)
		k=input("Enter Nickname: ")
		subclient.edit_profile(nickname=k)
	except:
		print("Id banned from community")
		break
	while True:
		thread()

