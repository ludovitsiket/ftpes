from ftplib import FTP_TLS
import os, sys, ftplib

def connect_ftpes(ftps,server,user,passwd):
  ftps.connect(server, 21)
  ftps.auth()
  ftps.prot_p()
  ftps.login(user, passwd)
  ftps.retrlines('LIST')
  
def download(ftps,filenames,local_folder):
  for item in filenames:
    local_filename = os.path.join(local_folder, item)
    print("Sťahujem: ",item, "do",local_filename)
    file = open(local_filename, 'wb')
    try:
      ftps.retrbinary('RETR '+ item, file.write)
    except ftplib.error_perm:
      pass
    file.close()
    print ("Sťahovanie ukončené.")
  ftps.quit()

def wrong_arguments():
  print("Nesprávny počet argumentov.\nSyntax: python ftpes.py <server> <prihlasovacie_meno> <heslo> <lokalna_zlozka_pre_stahovanie (v uvodzovkach)>")
  sys.exit()
  
def argument_control():
  if len(sys.argv) < 5:
    wrong_arguments() 
  elif len(sys.argv) > 5:
    wrong_arguments() 

def main():
  try:
    server=sys.argv[1]
    user=sys.argv[2]
    passwd=sys.argv[3]
    local_folder=sys.argv[4]
  except:
    argument_control()
  ftps = FTP_TLS(server)
  connect_ftpes(ftps,server,user,passwd)
  filenames=ftps.nlst()
  download(ftps,filenames,local_folder)

main()
