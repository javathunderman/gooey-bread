import subprocess

runMine = subprocess.run(['./ccminer', '--algo=scrypt:10', '-o', pool, '-u', address, '--max_temp=85'])
