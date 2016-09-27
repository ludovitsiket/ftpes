from ftplib import FTP_TLS
import os, sys

def connect_ftpes(server,user,passwd):
  ftps = FTP_TLS(server)
  ftps.connect(server, 21)
  ftps.auth()
  ftps.prot_p()
  ftps.login(user, passwd)
  ftps.retrlines('LIST')
  filename=input("Meno súboru na stiahnutie: ")
  file = open(filename, 'wb')
  ftps.retrbinary('RETR %s' % filename, file.write)
  print ("Sťahovanie ukončené. Súbor sa nachádza v aktuálnom adresári.")
  ftps.close()
  return

def main():
  server=sys.argv[1]
  user=sys.argv[2]
  passwd=sys.argv[3]
  connect_ftpes(server,user,passwd)

main()
