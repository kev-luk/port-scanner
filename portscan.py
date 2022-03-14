import socket
import sys
from datetime import datetime

# Ask for target
input_target = input("Enter a target to scan: ")
remote_ip = None

# Determine if target input was IPv4 address or domain name
try:
    # Test if target is IPv4 address or domain name
    remote_ip = socket.gethostbyname(input_target)
except OSError:
    # End program if input is not IPv4 address or domain name
    print("Illegal target inputted. Exiting")
    sys.exit()

# Ask for range of ports to scan
print("Please enter the range of ports you would like to scan on the target")

range_start_in = input("Enter a start port: ")
range_end_in = input("Enter a end port: ")

# Convert range inputs from string to int
range_start = int(range_start_in)
range_end = int(range_end_in)

# Get start time of scan
start_time = datetime.now()

print("Scanning started at: {}".format(start_time))
print("Please wait, scanning target now: {}".format(remote_ip))

# try to connect to each port in range
# add 1 to range_end in order to scan all ports
for port in range(range_start, range_end + 1):
    try:
        # Create socket instance
        # AF_INET allows socket to communicate with IPv4 addresses
        # SOCK_STREAM sets protocol to Transmission Control Protocol (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # If target has not responded in 5 seconds, then timeout
        s.settimeout(5.0)

        # Try to connect port and target IPs.
        result = s.connect_ex((remote_ip, port))
        
        # If no error, port is open
        if result == 0:
            print("Port {}:\tOpen".format(port))
        else:
            print("Port {}:\tClosed".format(port))

        # Close the socket that was used to connect to target
        s.close()
    except OSError:    # Handle no connection and timeout
        print("Unable to connect to target. Exiting")
        sys.exit()
    except KeyboardInterrupt: # Handle user end program
        print("Scanning interrupted. Exiting")
        sys.exit()

# Finish scanning target
print("Port Scanning Completed")