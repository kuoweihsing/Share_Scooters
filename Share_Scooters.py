# 讀入車輛各等級的每單位電量公里數及電池容量
data = input().split(sep = ",")
data_int = []
for i in data:
    data_int.append(int(i))
# 各等級的每單位電量公里數
kilometer_per_unit_battery = dict()
kilometer_per_unit_battery[1] = data_int[0]
kilometer_per_unit_battery[2] = data_int[2]
kilometer_per_unit_battery[3] = data_int[4]
# 各等級的電池容量
battery_capacity = dict()
battery_capacity[1] = data_int[1]
battery_capacity[2] = data_int[3]
battery_capacity[3] = data_int[5]

Wewo = ["Wewo", 0, []]
uRent = ["uRent", 0, []]
goshake = ["goshake", 0, []]

def add(company, scooter_number, scooter_level):
    if company == "Wewo":
        Wewo[1] += 1
        temp = []
        temp.append(scooter_number)  # 車牌號碼
        temp.append(scooter_level)  # 車輛等級
        temp.append(0)  # 總里程數（初始值為0）
        temp.append(0)  # 剩餘電量（初始值為0）
        temp.append(0)  # 是否乾淨（初始值為True）
        Wewo[2].append(temp)
    elif company == "uRent":
        uRent[1] += 1
        temp = []
        temp.append(scooter_number)  # 車牌號碼
        temp.append(scooter_level)  # 車輛等級
        temp.append(0)  # 總里程數（初始值為0）
        temp.append(0)  # 剩餘電量（初始值為0）
        temp.append(0)  # 是否乾淨（初始值為True）
        uRent[2].append(temp)
    elif company == "goshake":
        goshake[1] += 1
        temp = []
        temp.append(scooter_number)  # 車牌號碼
        temp.append(scooter_level)  # 車輛等級
        temp.append(0)  # 總里程數（初始值為0）
        temp.append(0)  # 剩餘電量（初始值為0）
        temp.append(0)  # 是否乾淨（初始值為True）
        goshake[2].append(temp)

def delete(company, scooter_number):
    if company == "Wewo":
        for i in Wewo[2]:
            if i[0] == scooter_number:
                Wewo[2].remove(i)
                Wewo[1] -= 1
    elif company == "uRent":
        for i in uRent[2]:
            if i[0] == scooter_number:
                uRent[2].remove(i)
                uRent[1] -= 1
    elif company == "goshake":
        for i in goshake[2]:
            if i[0] == scooter_number:
                goshake[2].remove(i)
                goshake[1] -= 1

def sell(sell_company, buy_company, scooter_number):
    if sell_company == "Wewo":
        if buy_company == "uRent":
            for i in Wewo[2]:
                if i[0] == scooter_number:
                    uRent[2].append(i)
                    uRent[1] += 1
                    Wewo[2].remove(i)
                    Wewo[1] -= 1
        elif buy_company == "goshake":
            for i in Wewo[2]:
                if i[0] == scooter_number:
                    goshake[2].append(i)
                    goshake[1] += 1
                    Wewo[2].remove(i)
                    Wewo[1] -= 1
    elif sell_company == "uRent":
        if buy_company == "Wewo":
            for i in uRent[2]:
                if i[0] == scooter_number:
                    Wewo[2].append(i)
                    Wewo[1] += 1
                    uRent[2].remove(i)
                    uRent[1] -= 1
        elif buy_company == "goshake":
            for i in uRent[2]:
                if i[0] == scooter_number:
                    goshake[2].append(i)
                    goshake[1] += 1
                    uRent[2].remove(i)
                    uRent[1] -= 1
    elif sell_company == "goshake":
        if buy_company == "Wewo":
            for i in goshake[2]:
                if i[0] == scooter_number:
                    Wewo[2].append(i)
                    Wewo[1] += 1
                    goshake[2].remove(i)
                    goshake[1] -= 1
        elif buy_company == "uRent":
            for i in goshake[2]:
                if i[0] == scooter_number:
                    uRent[2].append(i)
                    uRent[1] += 1
                    goshake[2].remove(i)
                    goshake[1] -= 1

def go(company, scooter_number, expected_consumption):
    if expected_consumption >= 0:
        if company == "Wewo":
            for i in Wewo[2]:
                if i[0] == scooter_number:
                    if i[3] >= expected_consumption:
                        i[3] -= expected_consumption
                        i[2] += expected_consumption * kilometer_per_unit_battery[i[1]]
                        i[4] += expected_consumption * kilometer_per_unit_battery[i[1]]
                        break
                    elif 0 < i[3] < expected_consumption:
                        i[2] += i[3] * kilometer_per_unit_battery[i[1]]
                        i[4] += i[3] * kilometer_per_unit_battery[i[1]]
                        i[3] = 0
                        break
        elif company == "uRent":
            for i in uRent[2]:
                if i[0] == scooter_number:
                    if i[3] >= expected_consumption:
                        i[3] -= expected_consumption
                        i[2] += expected_consumption * kilometer_per_unit_battery[i[1]]
                        i[4] += expected_consumption * kilometer_per_unit_battery[i[1]]
                        break
                    elif 0 < i[3] < expected_consumption:
                        i[2] += i[3] * kilometer_per_unit_battery[i[1]]
                        i[4] += i[3] * kilometer_per_unit_battery[i[1]]
                        i[3] = 0
                        break
        elif company == "goshake":
            for i in goshake[2]:
                if i[0] == scooter_number:
                    if i[3] >= expected_consumption:
                        i[3] -= expected_consumption
                        i[2] += expected_consumption * kilometer_per_unit_battery[i[1]]
                        i[4] += expected_consumption * kilometer_per_unit_battery[i[1]]
                        break
                    elif 0 < i[3] < expected_consumption:
                        i[2] += i[3] * kilometer_per_unit_battery[i[1]]
                        i[4] += i[3] * kilometer_per_unit_battery[i[1]]
                        i[3] = 0
                        break

def recharge(company, scooter_number, recharge_volume):
    if company == "Wewo":
        for i in Wewo[2]:
            if i[0] == scooter_number:
                if i[3] + recharge_volume <= battery_capacity[i[1]]:
                    i[3] += recharge_volume
                    break
                else:
                    i[3] = battery_capacity[i[1]]
                    break
    elif company == "uRent":
        for i in uRent[2]:
            if i[0] == scooter_number:
                if i[3] + recharge_volume <= battery_capacity[i[1]]:
                    i[3] += recharge_volume
                    break
                else:
                    i[3] = battery_capacity[i[1]]
                    break
    elif company == "goshake":
        for i in goshake[2]:
            if i[0] == scooter_number:
                if i[3] + recharge_volume <= battery_capacity[i[1]]:
                    i[3] += recharge_volume
                    break
                else:
                    i[3] = battery_capacity[i[1]]
                    break

def wash(company, scooter_number):
    if company == "Wewo":
        for i in Wewo[2]:
            if i[0] == scooter_number:
                i[-1] = 0
                break
    elif company == "uRent":
        for i in uRent[2]:
            if i[0] == scooter_number:
                i[-1] = 0
                break
    elif company == "goshake":
        for i in goshake[2]:
            if i[0] == scooter_number:
                i[-1] = 0
                break

# 讀入待分析資料
pending_analysis = []
while True:
    temp = input().split(sep = ",")
    temp_list = []
    if temp[0] != "BREAK":  # 非為終止條件持續讀取
        for i in temp:
            try:
                temp_list.append(int(i))
            except:
                temp_list.append(i)
        pending_analysis.append(temp_list)
    else:  # 若為終止條件停止讀取
        break

for i in pending_analysis:
    if i[0] == "A":
        add(i[1], i[2], i[3])
    elif i[0] == "D":
        delete(i[1], i[2])
    elif i[0] == "S":
        sell(i[1], i[2], i[3])
    elif i[0] == "G":
        go(i[1], i[2], i[3])
    elif i[0] == "R":
        recharge(i[1], i[2], i[3])
    elif i[0] == "W":
        wash(i[1], i[2])

dirty_scooter = []
for i in [Wewo[2], uRent[2], goshake[2]]:
    for j in i:
        if j[-1] >= 100:
            dirty_scooter.append(j[0])

dirty_scooter = sorted(dirty_scooter)
if len(dirty_scooter) == 0:
    print(-1)
else:
    print(",".join(dirty_scooter))

total_km = []
for i in [Wewo[2], uRent[2], goshake[2]]:
    for j in i:
        total_km.append(j[2])

max_km = max(total_km)
check_scooter = []
for i in [Wewo[2], uRent[2], goshake[2]]:
    for j in i:
        if j[2] == max_km:
            check_scooter.append(j[0])

check_scooter = sorted(check_scooter)
print(check_scooter[0])
