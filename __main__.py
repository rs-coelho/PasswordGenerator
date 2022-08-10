from PasswordGenerator import Execute
import os

if __name__=='__main__':
    os.system('pip3 install -r requirements.txt')
    os.system('sudo apt-get install docker-engine')
    os.system('sudo service docker start')
    os.system('docker build && docker run')
    pg = Execute()
    pg.run()