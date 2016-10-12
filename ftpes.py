from ftplib import FTP_TLS
import os, sys, ftplib, time

def connect_ftpes(ftps,server,user,passwd):
  print (ftps.connect(server, 21))
  print (ftps.auth())
  print (ftps.prot_p())
  print (ftps.login(user, passwd), "\n")
  
#python ftplib Timeout Error: [WinError 10060]
def download(ftps,local_folder,connect_ftpes,server,user,passwd):
  ftps.set_debuglevel(2)
  ftp_filenames=ftps.nlst()
  for item in ftp_filenames:
    if not os.path.isfile(os.path.join(local_folder, item)):
      local_filename = os.path.join(local_folder, item)
      #raise TimeoutError
      print("Sťahujem: ",item, "do",local_filename)
      file = open(local_filename, 'wb')
      try:
        print(ftps.retrbinary('RETR '+ item, file.write), "\n")
      except ftplib.error_perm:
        pass  
      file.close()
    else:
      print("Súbor ",item," už je stiahnutý.")
  
def argument_control():
  print("Nesprávny počet argumentov.\nSyntax: python ftpes.py <server> <prihlasovacie_meno> <heslo> <lokalna_zlozka_pre_stahovanie (v uvodzovkach)>") 
  sys.exit()
  
def connect_download(ftps,server,user,passwd,local_folder,count, max_count):
  if (count <= max_count):
    connect_ftpes(ftps,server,user,passwd)
    try:
      download(ftps,local_folder,connect_ftpes,server,user,passwd)
    except (TimeoutError, ConnectionResetError) as timeout:
    #except ConnectionResetError as timeout:
      print("CHYBA pokus cislo ", count, " z celkoveho ", max_count)
      print(timeout)
      #sleep v sekundach
      time.sleep(30)
      connect_download(ftps,server,user,passwd,local_folder,count+1, max_count) 

def main():
  server=sys.argv[1]
  user=sys.argv[2]
  passwd=sys.argv[3]
  local_folder=sys.argv[4]  
  if len(sys.argv) != 5:
    argument_control()
  else:
    ftps = FTP_TLS(server)
    connect_download(ftps,server,user,passwd,local_folder,1,5)
    print(ftps.quit())
main()
