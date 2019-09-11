#Author 'Ananth Venkateswarlu aka she11z'

import requests
import urlparse
import optparse

parser = optparse.OptionParser()
parser.add_option('-u', '--url', dest='url', help='Domain URL NOTE: Do not include HTTP or HTTPS')
parser.add_option('-w', '--wordlist', dest='wordlist', help='Wordlist to use')
parser.add_option('-m', '--mode', dest='mode', help='HTTP or HTTPS If not mentioned, Default: Http')
parser.add_option('-o', '--opt', dest='option', help='dir=directory : sub=subdomain')

(options, arguments) = parser.parse_args()
if not options.url:
	print('\nERROR: Please provide URL or --help for Options\n')
	exit()
if not options.wordlist:
	print('\nERROR: Please provide Wordlist or --help for Options\n')
	exit()
if not options.option:
	print('\nERROR: Please provide the option(dir/sub) or --help for options\n')
	exit()

def get_request(url):
	try:
		return requests.get(url)

	except Exception as e:
		pass

def directory_brute():
	print("\t--------------------------------")
	print("\tDirectory Brute Force by she11z" )
	print("\t--------------------------------\n\n")
	try:
		with open(options.wordlist, 'r') as dictionary:
			for line in dictionary:
				word = line.strip()
				if not "#" in word:
					if options.mode == 'https':
						try:
							test_url = 'https://' + urlparse.urljoin(options.url, word)
							response = get_request(test_url)

							code = response.status_code
							if response:
								print("[+]  {}  \t| Status Code: {} |").format(test_url, code)
						except Exception as e:
							print('\tDomain {} do not support SSL').format(options.url)
							print('\tTry again with -m http\n')
							exit()
			
					else:
						try:
							test_url = 'http://' + urlparse.urljoin(options.url, word)
							response = get_request(test_url)

							code = response.status_code
							if response:
								print("[+]  {}  \t| Status Code: {} |").format(test_url, code)
						except Exception as e:
							print('\tSomething went wrong\n')
							exit()
						
			
			print("\n\t\tFinished\n")

	except KeyboardInterrupt:
		print("\n\n\t\tStopped\n")
	


def subdomains_brute():
	print("\t--------------------------------")
	print("\tSub-Domain Brute Force by she11z" )
	print("\t--------------------------------\n\n")
				
	try:
		with open(options.wordlist, 'r') as dictionary:
			for line in dictionary:
				word = line.strip()

				if not "#" in word:
					if options.mode == 'https':
						try:
							test_domain = ('https://' + word + '.' + options.url)
						
							response = get_request(test_domain)
							if response:
								print("[+] {} ").format(test_domain)

						except Exception as e:
							print('\tDomain {} do not support SSL').format(options.url)
							print('\tTry again with -m http\n')
							exit()
			
						
					else:
						
						try:
							test_domain = ('http://' + word + '.' + options.url)
						
							response = get_request(test_domain)
							if response:
								print("[+] {} ").format(test_domain)

						except Exception as e:
							print('\tSomething went wrong\n')
							exit()			
						

			print("\n\nFinished")	
			
	except KeyboardInterrupt:
		print("\n\nStopped\n")	

if options.option == 'dir':
	directory_brute()
	
if options.option == 'sub':
	subdomains_brute()
			

