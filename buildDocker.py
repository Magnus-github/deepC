import os, argparse
from sys import platform

def main():

	parser = argparse.ArgumentParser(description="run docker in any os")
	parser.add_argument("-dev", "--developer", action="store_true", help="ssh inside docker container without running make")
	args = parser.parse_args()

	if args.developer:
		# Mac and Linux
		if os.name == "posix":
			if platform == "darwin":
				util_cmd = "launchctl"
			elif platform == "linux" or platform == "linux2":
				util_cmd = "systemctl"
				
			try:
				os.system(f'{util_cmd} start docker')
			except:
				os.system(f'{util_cmd} unmask docker.service && {util_cmd} unmask docker.socket && {util_cmd} start docker.service')
			os.system('sudo docker build -t dnnc .')
			os.system('sudo docker run -it dnnc /bin/bash')

		# Windows
		elif os.name == "nt":
			os.system('docker build -t dnnc .')
			# don't use single quotes inside command, always use duble quotes, similar problem listed below
			# https://stackoverflow.com/questions/24673698/unexpected-eof-while-looking-for-matching-while-using-sed
			os.system('docker run -it dnnc /bin/bash -c "cd /dnnCompiler && make clean && make all"')

	else:
		# Mac and Linux
		if os.name == "posix":
			if platform == "darwin":
				util_cmd = "launchctl"
			elif platform == "linux" or platform == "linux2":
				util_cmd = "systemctl"
				
			try:
				os.system(f'{util_cmd} start docker')
			except:
				os.system(f'{util_cmd} unmask docker.service && {util_cmd} unmask docker.socket && {util_cmd} start docker.service')
			os.system('sudo docker build -t dnnc .')
			os.system('sudo docker run -it dnnc /bin/bash -c "cd /dnnCompiler && make clean && make all"')

		# Windows
		elif os.name == "nt":
			os.system('docker build -t dnnc .')
			# don't use single quotes inside command, always use duble quotes, similar problem listed below
			# https://stackoverflow.com/questions/24673698/unexpected-eof-while-looking-for-matching-while-using-sed
			os.system('docker run -it dnnc /bin/bash -c "cd /dnnCompiler && make clean && make all"')


if __name__ == "__main__":
	main()