#######
# A47 #
#######

import subprocess #module to execute system commands
import optparse   #module to pass arguments in termenal
import re         #module for Regex (Regular Expretions)

def mac_changer(interface ,new_mac):
    print("[+] Changing MAC address for "+interface +" to "+ new_mac)

    #this code is NOT secure because you can execute other commands 
    #by adding ; then your command after interface or new MAC
    # subprocess.call("ifconfig "+ interface +" down",shell=True)
    # subprocess.call("ifconfig "+ interface +" hw ether "+new_mac,shell=True)
    # subprocess.call("ifconfig "+ interface +" up",shell=True)

    #this is the secure version of the code 
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def arguments():
    parser = optparse.OptionParser() #create object from Optionparser CLASS
    parser.add_option("-i","--interface", dest="interface",help="The interface that you will change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac",help="The new MAC address for the interface")
    (options ,arguments) = parser.parse_args()
    
    #handle user input
    if not options.interface:
        parser.error("[-] Please Enter An Interface")
    elif not options.new_mac:
        parser.error("[-] Please Enter New MAC Address") 

    return options       

def current_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface],text=True)

    ifmac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
    if ifmac:
        return ifmac.group(0)
    else:
        print("[-] Sorry, there is an error in reading MAC address")    


options = arguments() #store the input arguments in options

curr_mac = current_mac(options.interface) #get the current MAC address

print ("[+] Current MAC address >> "+ str(curr_mac))

mac_changer(options.interface, options.new_mac)    #call mac_changer function

curr_mac = current_mac(options.interface)

if curr_mac == options.new_mac:
    print("[+] MAC address changed Successfully to >> "+ curr_mac)
else:
    print("[-] There is an error in changing MAC address")    

