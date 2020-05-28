# Populate Utility MIB w/ "show interface <int> extensive" output


JunOS Config Prerequisites  
set event-options generate-event FIVE_MINUTES time-interval 300  
set event-options policy UTILITY_MIB_SCRIPT events FIVE_MINUTES  
set event-options policy UTILITY_MIB_SCRIPT then event-script utility_mib.py  
set event-options event-script file utility_mib.py python-script-user escript  


Other Prerequisites  
Copy file to switch using 'escript' user for auth.  
e.g. scp ./utility_mib.py escript@127.127.127.127:/var/db/scripts/event/  

This results in escript being the owner and allows execution of the script for that user by default  
-rw-r--r--  1 escript wheel      1670 Mar 30 11:37 utility_mib.py  
