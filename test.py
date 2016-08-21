import sys, time, subprocess

method = sys.argv[1]

start = time.time()

word_path = './words'
result_path = './results'

with open(word_path, 'r') as f:
	words = f.read().split('\n')[:-1]
	print(len(words))
f.close()
result = []

if method == 'msc':
	for word in words:
		cmd = 'curl http://127.0.0.1:5000/word2vec/msc?word=' + word
		p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		r = p.wait()
		(stdoutput, erroutput) = p.communicate()
		# stdoutput = stdoutput.decode('utf-8')
		result.append(stdoutput)
elif method == 'sc':
	for word in words:
		cmd = 'curl http://127.0.0.1:5000/word2vec/msc?word=' + word
		p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		r = p.wait()
		(stdoutput, erroutput) = p.communicate()
		# stdoutput = stdoutput.decode('utf-8')
		result.append(stdoutput)

with open(result_path, 'wb') as f:
	for item in result:
		f.write(item)
f.close()

end = time.time()
print(end - start)