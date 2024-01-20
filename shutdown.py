import os

def shutdown(minutes):
    seconds = minutes * 60
    os.system(f"shutdown -s -t {seconds}")

# Get the number of minutes from the user
minutes = int(input("Enter the number of minutes to shutdown: "))

# Call the shutdown function
shutdown(minutes)



# minutes = int(input("Enter minutes to shutdown: "))