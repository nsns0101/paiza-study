date, time = input().split(" ")

date_m, date_d = date.split("/")
time_h, time_m = time.split(":")
date_m, date_d, time_h, time_m = int(date_m), int(date_d), int(time_h), int(time_m)

while time_h >= 24:

    if(time_h >= 24):
        time_h -= 24
        date_d += 1
    else:
        break
    
if(time_m < 10):
    time_m = "0" + str(time_m)
if(time_h < 10):
    time_h = "0" + str(time_h)
if(date_d < 10):
    date_d = "0" + str(date_d)
if(date_m < 10):
    date_m = "0" + str(date_m)

print( str(date_m) + "/" + str(date_d), str(time_h) + ":" + str(time_m))



# if(result_h < 10):
#     result_h = "0" + str(result_h)
# if(result_m < 10):
#     result_m = "0" + str(result_m)

# print( str(result_h) + ":" + str(result_m) )