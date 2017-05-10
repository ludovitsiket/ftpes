from ftplib import FTP_TLS
import os, sys, ftplib, time
from datetime import datetime,timedelta

def connect_ftpes(ftps,server,user,passwd,local_folder):
  print (ftps.connect(server, 21))
  print (ftps.auth())
  print (ftps.prot_p())
  print (ftps.login(user, passwd), "\n")
  check_local_file_size(ftps,local_folder,server,user,passwd)
  
def download(ftps,local_folder,connect_ftpes,server,user,passwd):
  ftps.set_debuglevel(2)
  ftp_filenames=ftps.nlst()
  for item in ftp_filenames:
    if not os.path.isfile(os.path.join(local_folder, item)):
      local_filename = os.path.join(local_folder, item)
      print("Sťahujem: ",item, "do",local_filename)
      with open(local_filename, 'wb') as f:
          try:
            print(ftps.retrbinary('RETR '+ item, f.write), "\n")
            f.close()
            #time.sleep(5)
          except ftplib.error_perm:
            pass
    else:
      pass

def check_local_file_size(ftps,local_folder,server,user,passwd):
  print("ftps: ",ftps)
  print("local_folder: ",local_folder)
  print("server: ",server)
  print("user: ",user)
  print("password: ",passwd)
  paths = [os.path.join(local_folder, item) for item in os.listdir(local_folder)]
  sorted_files = sorted(paths, key=os.path.getctime)
  if(len(sorted_files) > 0):
    newest = sorted_files[-1]
    file_to_remove=os.path.join(local_folder, newest)
    print(file_to_remove)
    os.remove(file_to_remove)
  
def argument_control():
  print("Syntax: python ftpes.py <server> <prihlasovacie_meno> <heslo> <lokalna_zlozka_pre_stahovanie (v uvodzovkach)>") 
  sys.exit()
  
def connect_download(ftps,server,user,passwd,local_folder,count, max_count):
  if (count <= max_count):
    connect_ftpes(ftps,server,user,passwd,local_folder)
    try:
      download(ftps,local_folder,connect_ftpes,server,user,passwd)
    except (TimeoutError, ConnectionResetError) as timeout:
      print("CHYBA pokus cislo ", count, " z celkoveho ", max_count)
      time.sleep(10)  #sleep v sekundach
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
    connect_download(ftps,server,user,passwd,local_folder,1,60)
    try:
      print(ftps.quit())
    except ConnectionResetError as connection_reset:
      print("Vziadleny server sa odpojil.")    
main()