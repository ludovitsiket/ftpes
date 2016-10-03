from ftplib import FTP_TLS
import os, sys, ftplib

def connect_ftpes(ftps,server,user,passwd):
  print (ftps.connect(server, 21))
  print (ftps.auth())
  print (ftps.prot_p())
  print (ftps.login(user, passwd), "\n")
  
def download(ftps,local_folder):
  ftps.set_debuglevel(2)
  ftp_filenames=ftps.nlst()
  for item in ftp_filenames:
    if not os.path.isfile(os.path.join(local_folder, item)):
      local_filename = os.path.join(local_folder, item)
      print("Sťahujem: ",item, "do",local_filename)
      file = open(local_filename, 'wb')
      try:
        print(ftps.retrbinary('RETR '+ item, file.write), "\n")
      except ftplib.error_perm:
        pass
      file.close()
    else:
      print("subor ",item," uz existuje")
  
def argument_control():
  print("Nesprávny počet argumentov.\nSyntax: python ftpes.py <server> <prihlasovacie_meno> <heslo> <lokalna_zlozka_pre_stahovanie (v uvodzovkach)>") 
  sys.exit()
  
def main():
  
  if len(sys.argv) != 5:
    argument_control()
  else:
    server=sys.argv[1]
    user=sys.argv[2]
    passwd=sys.argv[3]
    local_folder=sys.argv[4]
    ftps = FTP_TLS(server)
    connect_ftpes(ftps,server,user,passwd)
    download(ftps,local_folder)
    print(ftps.quit())
main()
