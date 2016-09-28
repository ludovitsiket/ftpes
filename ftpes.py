from ftplib import FTP_TLS
import os, sys

def connect_ftpes(ftps,server,user,passwd):
  ftps.connect(server, 21)
  ftps.auth()
  ftps.prot_p()
  ftps.login(user, passwd)
  ftps.cwd("Documents")
  ftps.retrlines('LIST')
  
def download(ftps,filenames):
  for item in filenames:
    local_filename = os.path.join(r"C:\Documents and Settings\user\Plocha\ftpes", item)
    print("Sťahujem: ",item, "do",local_filename)
    file = open(local_filename, 'wb')
    ftps.retrbinary('RETR '+ item, file.write)
    file.close()
    print ("Sťahovanie ukončené.")
  ftps.quit()
  
def hint():
  print("Nesprávny počet argumentov. Syntax: python ftpes.py <server> <prihlasovacie_meno> <heslo>")
  
def argument_control():
  hint()

def main():
  try:
    server=sys.argv[1]
    user=sys.argv[2]
    passwd=sys.argv[3]
  except:
    argument_control()
  ftps = FTP_TLS(server)
  connect_ftpes(ftps,server,user,passwd)
  filenames=ftps.nlst()
  download(ftps,filenames)

main()
