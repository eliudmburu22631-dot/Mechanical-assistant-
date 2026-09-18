import json
import os

print("Welcome to My Mechanical App - Garage Edition! 🔧")

name = input("Enter your name: ")
print(f"Hello Eng. {name}!\n")

# File ya kuhifadhi customers
CUSTOMER_FILE = "customers.json"
if not os.path.exists(CUSTOMER_FILE):
    with open(CUSTOMER_FILE, "w") as f:
        json.dump([], f)

# --- MECHANICAL ASSISTANT BRAIN ---
def mechanical_assistant():
    print("\n🤖 MECHANICAL ASSISTANT: Niulize kitu (andika 'exit' kutoka)")
    print("Mfano: 'gari inachemka', 'brake inalia', 'torque ni nini'")
    while True:
        q = input("You: ").lower()
        if q == "exit":
            break
        if "chemka" in q or "overheat" in q:
            print("Assistant: Check radiator maji, thermostat, na cooling fan. Usifungue radiator ikiwa moto!")
        elif "brake" in q:
            print("Assistant: Brake pads zimeisha ama brake fluid iko low. Skia kama kuna mluzi - badilisha pads.")
        elif "torque" in q:
            print("Assistant: Torque = Force x Distance. Unit ni Nm. Ndio nguvu ya kufunga bolt.")
        elif "oil" in q:
            print("Assistant: Oil ya Toyota 5W-30, service kila 5000km. Black oil = badilisha haraka.")
        elif "battery" in q or "haina moto" in q:
            print("Assistant: Check battery terminals kama ziko na kutu, ama alternator haichaji.")
        elif "consumption" in q or "mafuta" in q:
            print("Assistant: High consumption? Check spark plugs, air filter, na tyre pressure.")
        else:
            print("Assistant: Sijashika vizuri, jaribu maneno kama 'brake', 'overheat', 'oil', 'battery', 'torque'.")

# --- FUNCTIONS ---
def diagnose():
    print("\n[A] DIAGNOSE CAR PROBLEM")
    prob = input("Elezea shida: (e.g. gari inachemka / inalia mbele / haiwaki): ").lower()
    if "chemka" in prob: print("=> SOLUTION: Angalia maji ya radiator, water pump, na gasket.")
    elif "lia" in prob or "squeak" in prob: print("=> SOLUTION: Fan belt ama brake pads. Piga WD-40 kwa belt ujaribu.")
    elif "haiwaki" in prob or "start" in prob: print("=> SOLUTION: Battery, starter motor, ama fuel pump.")
    elif "moshi" in prob: print("=> SOLUTION: Moshi mweusi = oil inaungua. Moshi mweupe = coolant inaingia engine.")
    else: print("=> SOLUTION: Nipe details zaidi - sauti, moshi, ama dashboard light gani?")

def engineering_calc():
    print("\n[B] ENGINEERING CALCULATOR")
    print("1. Torque (N*m) 2. Power (HP) 3. Stress")
    c = input("Chagua 1-3: ")
    try:
        if c == "1":
            f = float(input("Force (N): ")); d = float(input("Distance (m): "))
            print(f"=> Torque = {f*d} Nm")
        elif c == "2":
            t = float(input("Torque (Nm): ")); rpm = float(input("RPM: "))
            hp = (t * rpm) / 7127
            print(f"=> Power = {hp:.2f} HP")
        elif c == "3":
            force = float(input("Force (N): ")); area = float(input("Area (m2): "))
            print(f"=> Stress = {force/area} Pa")
    except: print("Weka numbers tu!")

def customer_manager():
    print("\n[C] FUNDI CUSTOMER TRACKER")
    print("1. Add Customer 2. View Customers")
    c = input("Chagua: ")
    with open(CUSTOMER_FILE, "r") as f:
        data = json.load(f)

    if c == "1":
        car = input("Number plate: ")
        job = input("Kazi gani? (e.g. oil change): ")
        amount = input("Amount Ksh: ")
        data.append({"plate": car, "job": job, "amount": amount})
        with open(CUSTOMER_FILE, "w") as f:
            json.dump(data, f)
        print("=> Customer saved!")
    elif c == "2":
        if not data: print("Hakuna customers bado.")
        for i, cust in enumerate(data, 1):
            print(f"{i}. {cust['plate']} - {cust['job']} - Ksh {cust['amount']}")

# --- MAIN LOOP ---
while True:
    print("\n--- MAIN MENU ---")
    print("1. A - Diagnose Gari")
    print("2. B - Engineering Calculator")
    print("3. C - Customer Tracker")
    print("4. D - Mechanical Assistant (AI)")
    print("5. Exit")

    choice = input("Chagua 1-5: ")

    if choice == "1": diagnose()
    elif choice == "2": engineering_calc()
    elif choice == "3": customer_manager()
    elif choice == "4": mechanical_assistant()
    elif choice == "5":
        print(f"\nMechanical App is working! Kazi njema Eng. {name}!")
        break
    else: print("Chagua 1-5 tu!")