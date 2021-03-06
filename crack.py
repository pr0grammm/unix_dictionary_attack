import sys
import datetime
import crypt

def test(username,password):
	#get ctype
	ctype = password.split('$')[1]
	#get salt
	salt = password.split('$')[2]
	#get insalt
	insalt = '$' + ctype + '$' + salt + '$'

	fdict = open(dictionary_file,'r',errors='ignore')

	try:
		for word in fdict.readlines():
			word=word.strip('\n')
			maybe = crypt.crypt(word,insalt)
			if maybe == password :
				print('[+],' + username + ',' + word)
				fresult.write('[+],' + username + ',' + word + '\n')
				return
		print('[-] '+username)
		fresult.write('[-],' + username + '\n')
		fdict.close()

	except Exception as e:
		print('the following problem was encountered:\n'+str(e))
		exit()
	

def main():
	
	print('program has started on '+str(datetime.datetime.now()))
	fshadow = open(shadow_file,'r')
	for line in fshadow.readlines():
		if line.split(':')[1].startswith('$6') or line.split(':')[1].startswith('$1'):
			#get username
			username = line.split(':')[0]
			#get password
			password =line.split(':')[1]
			print('trying user ' +username)
			test(username,password)
	print('finished! '+str(datetime.datetime.now()))
	fshadow.close()

shadow_file = sys.argv[1]
dictionary_file = sys.argv[2]
fresult = open('result.csv','w')

main()
fresult.close()
