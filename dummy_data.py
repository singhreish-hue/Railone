# dummy_data.py
# This file only stores SAMPLE/FAKE data.
# There's no connection to a real Indian Railways database — everything here is hard-coded for the demo.

TRAINS = [
    {
        "number": "12951",
        "name": "Mumbai Rajdhani Express",
        "from": "New Delhi (NDLS)",
        "to": "Mumbai Central (MMCT)",
        "departure": "16:25",
        "arrival": "08:35",
        "duration": "16h 10m",
        "classes": [
            {"code": "3A", "label": "AC 3 Tier", "fare": 2145, "seats_left": 24},
            {"code": "2A", "label": "AC 2 Tier", "fare": 3110, "seats_left": 9},
            {"code": "1A", "label": "AC First Class", "fare": 5240, "seats_left": 3},
        ],
    },
    {
        "number": "12259",
        "name": "Sealdah Duronto Express",
        "from": "New Delhi (NDLS)",
        "to": "Sealdah (SDAH)",
        "departure": "10:05",
        "arrival": "10:30",
        "duration": "24h 25m",
        "classes": [
            {"code": "SL", "label": "Sleeper", "fare": 785, "seats_left": 62},
            {"code": "3A", "label": "AC 3 Tier", "fare": 2015, "seats_left": 18},
            {"code": "2A", "label": "AC 2 Tier", "fare": 2890, "seats_left": 5},
        ],
    },
    {
        "number": "12002",
        "name": "Bhopal Shatabdi Express",
        "from": "New Delhi (NDLS)",
        "to": "Bhopal (BPL)",
        "departure": "06:00",
        "arrival": "13:30",
        "duration": "7h 30m",
        "classes": [
            {"code": "CC", "label": "AC Chair Car", "fare": 985, "seats_left": 41},
            {"code": "EC", "label": "Executive Chair Car", "fare": 1975, "seats_left": 7},
        ],
    },
    {
        "number": "22691",
        "name": "KSR Bengaluru Rajdhani",
        "from": "New Delhi (NDLS)",
        "to": "KSR Bengaluru (SBC)",
        "departure": "20:45",
        "arrival": "05:30",
        "duration": "32h 45m",
        "classes": [
            {"code": "3A", "label": "AC 3 Tier", "fare": 3260, "seats_left": 15},
            {"code": "2A", "label": "AC 2 Tier", "fare": 4590, "seats_left": 6},
        ],
    },
]

# Sample dummy PNRs for lookup — any 10-digit number
# generates a random-looking but consistent result.
SAMPLE_PNR_STATUSES = ["Confirmed", "RAC 12", "Waitlist 4", "Confirmed", "Waitlist 21"]

FOOD_MENU = {
    "Breakfast": [
        {"id": "f1", "name": "Veg Cutlet + Bread", "price": 90},
        {"id": "f2", "name": "Masala Omelette + Toast", "price": 110},
        {"id": "f3", "name": "Poha", "price": 70},
    ],
    "Meals": [
        {"id": "f4", "name": "Veg Thali", "price": 180},
        {"id": "f5", "name": "Chicken Biryani", "price": 220},
        {"id": "f6", "name": "Paneer Butter Masala + Rice", "price": 190},
    ],
    "Snacks & Beverages": [
        {"id": "f7", "name": "Samosa (2 pcs)", "price": 40},
        {"id": "f8", "name": "Masala Chai", "price": 20},
        {"id": "f9", "name": "Cold Coffee", "price": 60},
    ],
}

WALLET = {
    "balance": 1245.50,
    "transactions": [
        {"date": "24 Jul 2026", "desc": "Ticket booking – 12951 Rajdhani", "amount": -2145, "type": "debit"},
        {"date": "20 Jul 2026", "desc": "R-Wallet Top-up", "amount": 2000, "type": "credit"},
        {"date": "15 Jul 2026", "desc": "Food order – Meals", "amount": -180, "type": "debit"},
        {"date": "10 Jul 2026", "desc": "Unreserved ticket + 3% discount", "amount": -48, "type": "debit"},
    ],
}

MY_BOOKINGS = [
    {
        "pnr": "2847193056",
        "train_name": "Mumbai Rajdhani Express",
        "train_number": "12951",
        "from": "New Delhi (NDLS)",
        "to": "Mumbai Central (MMCT)",
        "date": "02 Aug 2026",
        "class_label": "AC 3 Tier",
        "status": "Confirmed",
        "coach": "B2", "seat": 34,
    },
    {
        "pnr": "9182736450",
        "train_name": "Bhopal Shatabdi Express",
        "train_number": "12002",
        "from": "New Delhi (NDLS)",
        "to": "Bhopal (BPL)",
        "date": "18 Jul 2026",
        "class_label": "AC Chair Car",
        "status": "Completed",
        "coach": "C1", "seat": 12,
    },
    {
        "pnr": "5610284739",
        "train_name": "Sealdah Duronto Express",
        "train_number": "12259",
        "from": "New Delhi (NDLS)",
        "to": "Sealdah (SDAH)",
        "date": "05 Jul 2026",
        "class_label": "Sleeper",
        "status": "Completed",
        "coach": "S4", "seat": 51,
    },
]

USER_PROFILE = {
    "name": "Rishabh Singh",
    "phone": "+91 98XXX XX210",
    "email": "rishabh.singh@example.com",
    "rwallet_balance": 1245.50,
    "verified": True,
}

COMPLAINT_CATEGORIES = [
    "Cleanliness", "Catering / Food Quality", "Security", "Punctuality",
    "Staff Behaviour", "Coach Maintenance", "Other",
]