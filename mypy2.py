!/usr/bin/python
from socket import *
import optparse
from threading import *
def connScan(tgtHost,tgtPort):
 try:
  sock=socket(AF_INET,SOCK_STREAM)
  sock.connect((tgtHost,tgtPort))
  print(f'[+] {tgtPort} /tcp open')
 except:
  print(f'[-] /tcp closed')
 finally:
  sock.close()
 
def portScan(tgtHost,tgtPorts):
 try:
  tgtip=gethostbyname(tgtHost)
 except:
  print(f'unknown host is {tgtHost}')
 try:
  tgtname=gethostbyname(tgtHost)
  print(f'scan results for  {tgtname}')
 except:
  print(f'[+] scan results for {tgtip}')
 setdefaulttimeout(1)
 for tgtport in tgtPorts:
  t=Thread(target=connScan,args=(tgtHost,int(tgtport)))
  t.start()

def main():
 

 print("""                                                    ,---,                                                                                                                                                
                                                              ,`--.' |                                                                                                                                                
              ,---,                              ___          |   :  :                                                  ___                                                                                          
            ,--.' |                            ,--.'|_    ,--,|   |  '                 ,-.----.                       ,--.'|_                                                                                        
            |  |  :      __  ,-.         ,--,  |  | :,' ,--.'|'   :  |                 \    /  \    ,---.    __  ,-.  |  | :,'                                                  ,---,       ,---,             __  ,-.
  .--.--.   :  :  :    ,' ,'/ /|       ,'_ /|  :  : ' : |  |, ;   |.'.--.--.           |   :    |  '   ,'\ ,' ,'/ /|  :  : ' :           .--.--.                            ,-+-. /  |  ,-+-. /  |          ,' ,'/ /|
 /  /    '  :  |  |,--.'  | |' |  .--. |  | :.;__,'  /  `--'_ '---' /  /    '          |   | .\ : /   /   |'  | |' |.;__,'  /           /  /    '     ,---.     ,--.--.    ,--.'|'   | ,--.'|'   |   ,---.  '  | |' |
|  :  /`./  |  :  '   ||  |   ,','_ /| :  . ||  |   |   ,' ,'|     |  :  /`./          .   : |: |.   ; ,. :|  |   ,'|  |   |           |  :  /`./    /     \   /       \  |   |  ,"' ||   |  ,"' |  /     \ |  |   ,'
|  :  ;_    |  |   /' :'  :  /  |  ' | |  . .:__,'| :   '  | |     |  :  ;_            |   |  \ :'   | |: :'  :  /  :__,'| :           |  :  ;_     /    / '  .--.  .-. | |   | /  | ||   | /  | | /    /  |'  :  /  
 \  \    `. '  :  | | ||  | '   |  | ' |  | |  '  : |__ |  | :      \  \    `.         |   : .  |'   | .; :|  | '     '  : |__          \  \    `. .    ' /    \__\/: . . |   | |  | ||   | |  | |.    ' / ||  | '    
  `----.   \|  |  ' | :;  : |   :  | : ;  ; |  |  | '.'|'  : |__     `----.   \        :     |`-'|   :    |;  : |     |  | '.'|          `----.   \'   ; :__   ," .--.; | |   | |  |/ |   | |  |/ '   ;   /|;  : |    
 /  /`--'  /|  :  :_:,'|  , ;   '  :  `--'   \ ;  :    ;|  | '.'|   /  /`--'  /        :   : :    \   \  / |  , ;     ;  :    ;         /  /`--'  /'   | '.'| /  /  ,.  | |   | |--'  |   | |--'  '   |  / ||  , ;    
'--'.     / |  | ,'     ---'    :  ,      .-./ |  ,   / ;  :    ;  '--'.     /         |   | :     `----'   ---'      |  ,   /         '--'.     / |   :    :;  :   .'   \|   |/      |   |/      |   :    | ---'    
  `--'---'  `--''                `--`----'      ---`-'  |  ,   /     `--'---'          `---'.|                         ---`-'            `--'---'   \   \  / |  ,     .-./'---'       '---'        \   \  /          
                                                         ---`-'                          `---`                                                       `----'   `--`---'                              `----'            
                                                                                                                                                                                                                     

 """)
 parser = optparse.OptionParser("usage of program :"+"-H<target host> -p<target port>")
 parser.add_option('-H',dest='tgtHost',type='string',help='specify target hosts')
 parser.add_option('-p',dest='tgtPort',type='string',help='specify target port seperated by coma')
 (options, args)=parser.parse_args()
 tgtHost = options.tgtHost
 tgtPorts = str(options.tgtPort).split(',')
 if (tgtHost == None) | (tgtPorts[0] == None):
  print (parser.usage)
  exit(0)
 portScan(tgtHost,tgtPorts)
if __name__ == '__main__':
 main()
