Current_users = int(input("enter number of current users:"))
new_users = 50
minutes = 2
total_users = Current_users+(new_users*minutes)
if total_users > 1000:
    print("launch new server Instance")
else:
    print("server stable")



uptime = 97.5
bill = 50000
if uptime >= 99.9:
    refund = 0
elif uptime >= 98:
    refund = bill*0.10
else:
    refund = bill*0.25
    print("Refund Amount :",refund)