import json, os
from datetime import datetime

print("Welcome to My Mechanical App - MONEY EDITION! 💰🔧")

name = input("Enter your name: ")
print(f"Hello Boss {name}!\n")

# Files
CUST_FILE = "customers.json"
EARN_FILE = "earnings.json"
for f in [CUST_FILE, EARN_FILE]:
    if not os.path.exists(f):
        with open(f, "w") as file:
            json.dump([], file)

def save_earning(job, amount, commission=0):
    with open(EARN_FILE, "r") as f:
        data = json.load(f)
    data.append({
        "date": datetime.now().strftime("%d-%m-%Y"),
        "job": job,
        "amount": amount,
        "commission": commission,
        "profit": amount * 0.15 if commission else amount
    })
    with open(EARN_FILE, "w") as f:
        json.dump(data, f)

# --- A: DIAGNOSE ---
def diagnose():
    print("\n[A] DIAGNOSE")
    prob = input("Shida ya gari: ").lower()
    if "chemka" in prob: print("=> Angalia radiator + water pump")
    elif "lia" in prob: print("=> Brake pads / fan belt")
    else: print("=> Check battery / oil")

# --- B: CALCULATOR ---
def calc():
    print("\n[B] CALCULATOR")
    try:
        f = float(input("Force N: ")); d = float(input("Distance m: "))
        print(f"=> Torque = {f*d} Nm")
    except: print("Weka number")

# --- C: CUSTOMER + MONEY ---
def customers():
    print("\n[C] CUSTOMER TRACKER + PESA")
    print("1. Add Job (Mwenyewe) 2. Add Fundi Job (Commission 15%) 3. View")
    ch = input("Chagua: ")
    with open(CUST_FILE, "r") as f:
        data = json.load(f)

    if ch == "1":
        plate = input("Number plate: ")
        job = input("Kazi: ")
        amt = float(input("Amount ulilipwa Ksh: "))
        data.append({"plate": plate, "job": job, "amount": amt, "type": "My Job"})
        with open(CUST_FILE, "w") as f: json.dump(data, f)
        save_earning(job, amt)
        print(f"=> Saved! Profit yako = Ksh {amt}")

    elif ch == "2":
        fundi = input("Jina ya fundi: ")
        job = input("Kazi alifanya: ")
        amt = float(input("Client alilipa Ksh: "))
        comm = amt * 0.15
        data.append({"plate": fundi, "job": job, "amount": amt, "type": f"Fundi - Comm {comm}"})
        with open(CUST_FILE, "w") as f: json.dump(data, f)
        save_earning(job, amt, commission=True)
        print(f"=> Fundi Job! Commission yako = Ksh {comm} (15%)")
        print(f"=> M-Pesa: Tuma Ksh {amt-comm} kwa fundi, wewe baki na {comm}")

    elif ch == "3":
        for i, c in enumerate(data, 1):
            print(f"{i}. {c['plate']} - {c['job']} - {c['amount']} - {c['type']}")

# --- D: SPARE PARTS AFFILIATE ---
def spare_parts():
    print("\n[D] SPARE PARTS SHOP (Affiliate $$)")
    parts = {
        "1": ["Oil Filter Toyota", 1800, "https://jumia.co.ke/oil-filter - Comm 8% = 144"],
        "2": ["Brake Pads Front", 3500, "https://jumia.co.ke/brake-pads - Comm 8% = 280"],
        "3": ["Spark Plug x4", 2800, "https://kinga.co.ke - Comm 10% = 280"],
        "4": ["Fan Belt", 1200, "Link yako hapa"]
    }
    for k, v in parts.items():
        print(f"{k}. {v[0]} - Ksh {v[1]}")
    ch = input("Chagua part kuona affiliate link (1-4): ")
    if ch in parts:
        print(f"=> {parts[ch][0]}")
        print(f"=> Affiliate Link: {parts[ch][2]}")
        print("=> Mtu akinunua, Jumia anakutumia pesa M-Pesa!")

# --- E: EARNINGS DASHBOARD ---
def earnings():
    print("\n[E] EARNINGS DASHBOARD 💰")
    with open(EARN_FILE, "r") as f:
        data = json.load(f)
    if not data:
        print("Bado hujapata pesa. Add job kwanza!")
        return
    total = sum([d['amount'] for d in data])
    profit = sum([d['profit'] for d in data])
    print(f"Total Jobs: {len(data)}")
    print(f"Total Cash Flow: Ksh {total}")
    print(f"YOUR PROFIT (Commission + Jobs): Ksh {profit}")
    print("\nDetails:")
    for d in data:
        print(f"- {d['date']}: {d['job']} - Ksh {d['profit']}")

# --- F: ASSISTANT ---
def assistant():
    print("\n[F] MECHANICAL ASSISTANT")
    print("Uliza kitu (exit kutoka)")
    while True:
        q = input("You: ").lower()
        if q == "exit": break
        if "chemka" in q: print("Bot: Radiator maji + fan")
        elif "brake" in q: print("Bot: Badilisha pads")
        elif "oil" in q: print("Bot: 5W-30 kila 5000km")
        else: print("Bot: Jaribu 'chemka', 'brake', 'oil'")

# --- MENU ---
while True:
    print("\n--- MONEY MENU ---")
    print("1. Diagnose 2. Calculator 3. Customers & Commission")
    print("4. Spare Parts (Affiliate) 5. Earnings Dashboard")
    print("6. Assistant 7. Exit")
    c = input("Chagua 1-7: ")
    if c == "1": diagnose()
    elif c == "2": calc()
    elif c == "3": customers()
    elif c == "4": spare_parts()
    elif c == "5": earnings()
    elif c == "6": assistant()
    elif c == "7":
        print(f"\nApp closed! Pesa iko safe Boss {name}!")
        break