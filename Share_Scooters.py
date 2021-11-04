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

class Company_Item:
    def __init__(self, company, total_scooter, scooter_list):
        self.company = company  # 車廠名稱
        self.total_scooter = total_scooter  # 總車數
        self.scooter_list = scooter_list  # 車輛名單
    def add(self, scooter_number, scooter_level):  # 新增車輛
        self.total_scooter += 1
        temp = []
        temp.append(scooter_number)  # 車牌號碼
        temp.append(scooter_level)  # 車輛等級
        temp.append(0)  # 總里程數（初始值為0）
        temp.append(0)  # 剩餘電量（初始值為0）
        temp.append(0)  # 是否乾淨（初始值為0）
        self.scooter_list.append(temp)
    def delete(self, scooter_number):  # 銷毀車輛
        for scooter in self.scooter_list:
            if scooter[0] == scooter_number:
                self.scooter_list.remove(scooter)
                self.total_scooter -= 1
                break
    def sell(self, buy_company, scooter_number):  # 買賣車輛
        if buy_company == "Wewo":
            for scooter in self.scooter_list:
                if scooter[0] == scooter_number:
                    Wewo.scooter_list.append(scooter)
                    Wewo.total_scooter += 1
                    self.scooter_list.remove(scooter)
                    self.total_scooter -= 1
        elif buy_company == "uRent":
            for scooter in self.scooter_list:
                if scooter[0] == scooter_number:
                    uRent.scooter_list.append(scooter)
                    uRent.total_scooter += 1
                    self.scooter_list.remove(scooter)
                    self.total_scooter -= 1
        elif buy_company == "goshake":
            for scooter in self.scooter_list:
                if scooter[0] == scooter_number:
                    goshake.scooter_list.append(scooter)
                    goshake.total_scooter += 1
                    self.scooter_list.remove(scooter)
                    self.total_scooter -= 1
    def go(self, scooter_number, expected_consumption):  # 租用車輛
        if expected_consumption >= 0:  # 預計消耗電量是否大於零
            for scooter in self.scooter_list:
                if scooter[0] == scooter_number:
                    if scooter[3] >= expected_consumption:  # 是否有足夠電量
                        scooter[3] -= expected_consumption
                        scooter[2] += expected_consumption * kilometer_per_unit_battery[scooter[1]]
                        scooter[4] += expected_consumption * kilometer_per_unit_battery[scooter[1]]
                        break
                    elif 0 < scooter[3] < expected_consumption:
                        scooter[2] += scooter[3] * kilometer_per_unit_battery[scooter[1]]
                        scooter[4] += scooter[3] * kilometer_per_unit_battery[scooter[1]]
                        scooter[3] = 0
                        break
    def recharge(self, scooter_number, recharge_volume):  # 充電
        for scooter in self.scooter_list:
            if scooter[0] == scooter_number:
                if scooter[3] + recharge_volume <= battery_capacity[scooter[1]]:
                    scooter[3] += recharge_volume
                    break
                else:
                    scooter[3] = battery_capacity[scooter[1]]
                    break
    def wash(self, scooter_number):  # 清洗車輛
        for scooter in self.scooter_list:
            if scooter[0] == scooter_number:
                scooter[-1] = 0
                break
            
Wewo = Company_Item("Wewo", 0, [])  # 生成Wewo車廠物件
uRent = Company_Item("uRent", 0, [])  # 生成uRent車廠物件
goshake = Company_Item("goshake", 0, [])  # 生成goshake車廠物件

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
    if i[0] == "A":  # 如為新增車輛
        if i[1] == "Wewo":
            Wewo.add(i[2], i[3])
        elif i[1] == "uRent":
            uRent.add(i[2], i[3])
        elif i[1] == "goshake":
            goshake.add(i[2], i[3])
    elif i[0] == "D":  # 如為銷毀車輛
        if i[1] == "Wewo":
            Wewo.delete(i[2])
        elif i[1] == "uRent":
            uRent.delete(i[2])
        elif i[1] == "goshake":
            goshake.delete(i[2])
    elif i[0] == "S":  # 如為買賣車輛
        if i[1] == "Wewo":
            Wewo.sell(i[2], i[3])
        elif i[1] == "uRent":
            uRent.sell(i[2], i[3])  
        elif i[1] == "goshake":
            goshake.sell(i[2], i[3])  
    elif i[0] == "G":  # 如為租用車輛
        if i[1] == "Wewo":
            Wewo.go(i[2], i[3])
        elif i[1] == "uRent":
            uRent.go(i[2], i[3])  
        elif i[1] == "goshake":
            goshake.go(i[2], i[3])
    elif i[0] == "R":  # 如為充電
        if i[1] == "Wewo":
            Wewo.recharge(i[2], i[3])
        elif i[1] == "uRent":
            uRent.recharge(i[2], i[3])  
        elif i[1] == "goshake":
            goshake.recharge(i[2], i[3])
    elif i[0] == "W":  # 如為清洗車輛
        if i[1] == "Wewo":
            Wewo.wash(i[2])
        elif i[1] == "uRent":
            uRent.wash(i[2])
        elif i[1] == "goshake":
            goshake.wash(i[2])

dirty_scooter = []  # 髒車名單
for i in [Wewo.scooter_list, uRent.scooter_list, goshake.scooter_list]:
    for j in i:
        if j[-1] >= 100:
            dirty_scooter.append(j[0])

dirty_scooter = sorted(dirty_scooter)
if len(dirty_scooter) == 0:
    print(-1)  # 都乾淨印出-1
else:
    print(",".join(dirty_scooter))  # 印出髒車

total_km = []
for i in [Wewo.scooter_list, uRent.scooter_list, goshake.scooter_list]:
    for j in i:
        total_km.append(j[2])

max_km = max(total_km)  # 找出最大里程數
check_scooter = []  # 最大里程數車牌名單
for i in [Wewo.scooter_list, uRent.scooter_list, goshake.scooter_list]:
    for j in i:
        if j[2] == max_km:
            check_scooter.append(j[0])

check_scooter = sorted(check_scooter)  # 車牌按字典排序
print(check_scooter[0])  # 印出排在最前面的車牌
