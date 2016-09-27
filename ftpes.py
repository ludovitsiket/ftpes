from ftplib import FTP_TLS
import os

def connect_ftpes(server,user,passwd):
  ftps = FTP_TLS(server)
  ftps.connect(server, 21)
  ftps.auth()
  ftps.prot_p()
  ftps.login(user, passwd)
  ftps.retrlines('LIST')
  filename=input("Meno súboru na stiahnutie: ")
  ftps.retrbinary('RETR %s' % filename, file.write)
  ftps.close()
  return

def main():
  server="192.168.49.207"
  user="csirke"
  passwd="poop"
  connect_ftpes(server,user,passwd)

main()
