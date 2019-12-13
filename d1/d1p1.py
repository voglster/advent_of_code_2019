
with open("input_p1") as f:
    data = f.readlines()

def calc_fuel_req(mass):
    return int(mass/3)-2


data = [int(d.strip()) for d in data if d]

total_from_modules = sum(calc_fuel_req(mass) for mass in data)

print("module fuel req", total_from_modules)

def calc_fuel_req_2(mass):
    new_value = int(mass/3)-2
    if new_value > 0:
        return new_value + calc_fuel_req_2(new_value)
    return 0

total_from_modules = sum(calc_fuel_req_2(mass) for mass in data)
print("module fuel req with fuel weight ", total_from_modules)

def test_2():
    print("14 is 2 : ", calc_fuel_req_2(14))
    print("1969 is 966 : ", calc_fuel_req_2(1969))







