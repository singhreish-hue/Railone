from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime, timedelta

from dummy_data import (
    TRAINS, SAMPLE_PNR_STATUSES, FOOD_MENU, WALLET, COMPLAINT_CATEGORIES,
    MY_BOOKINGS, USER_PROFILE
)

app = Flask(__name__)


# ---------- HOME ----------
@app.route("/")
def home():
    # Home page shows a small "quick search" form + quick action tiles
    return render_template("home.html", active="home")


# ---------- TICKET BOOKING ----------
@app.route("/booking")
def booking():
    # Search form page — user enters "from" and "to" city
    return render_template("booking.html", active="booking")


@app.route("/booking/results")
def booking_results():
    # Take from/to query params — for the demo we just show all dummy trains
    from_city = request.args.get("from", "New Delhi (NDLS)")
    to_city = request.args.get("to", "Mumbai Central (MMCT)")
    return render_template(
        "booking_results.html", trains=TRAINS, from_city=from_city, to_city=to_city, active="booking"
    )


@app.route("/booking/confirm", methods=["POST"])
def booking_confirm():
    # No real payment/booking happens — this just generates a dummy confirmation
    data = request.get_json()
    pnr = "".join(str(random.randint(0, 9)) for _ in range(10))
    booking_id = f"RC{random.randint(100000, 999999)}"
    return jsonify({
        "success": True,
        "pnr": pnr,
        "booking_id": booking_id,
        "train": data.get("train_name"),
        "class_label": data.get("class_label"),
        "fare": data.get("fare"),
        "passenger": data.get("passenger_name"),
    })


# ---------- PNR STATUS ----------
@app.route("/pnr")
def pnr_page():
    return render_template("pnr.html", active="pnr")


@app.route("/pnr/check", methods=["POST"])
def pnr_check():
    data = request.get_json()
    pnr_number = (data.get("pnr") or "").strip()

    if len(pnr_number) != 10 or not pnr_number.isdigit():
        return jsonify({"error": "PNR number must be 10 digits."}), 400

    # Dummy logic: seed randomness off the PNR digits for a "consistent" fake result
    seed = sum(int(d) for d in pnr_number)
    random.seed(seed)
    train = random.choice(TRAINS)
    status = random.choice(SAMPLE_PNR_STATUSES)
    coach = random.choice(["A1", "B2", "S4", "S7", "B1"])
    seat = random.randint(1, 72)
    random.seed()  # reset the seed so the rest of the app uses normal randomness

    return jsonify({
        "pnr": pnr_number,
        "train_name": train["name"],
        "train_number": train["number"],
        "from": train["from"],
        "to": train["to"],
        "date_of_journey": (datetime.now() + timedelta(days=3)).strftime("%d %b %Y"),
        "status": status,
        "coach": coach,
        "seat": seat,
    })


# ---------- MY BOOKINGS (bottom nav tab) ----------
@app.route("/my-bookings")
def my_bookings():
    return render_template("my_bookings.html", bookings=MY_BOOKINGS, active="my_bookings")


# ---------- YOU / PROFILE (bottom nav tab) ----------
@app.route("/account")
def account():
    return render_template("account.html", user=USER_PROFILE, active="account")


# ---------- LIVE TRAIN TRACKING ----------
@app.route("/tracking")
def tracking():
    return render_template("tracking.html", trains=TRAINS, active="tracking")


@app.route("/tracking/status/<train_number>")
def tracking_status(train_number):
    # Dummy live position: seed off the train number for a consistent % progress
    seed = sum(int(d) for d in train_number if d.isdigit())
    random.seed(seed + datetime.now().minute)
    progress = random.randint(15, 92)
    delay = random.choice([0, 0, 5, 12, 20, 35])
    next_station = random.choice(["Kanpur Central", "Bhopal Jn", "Vadodara Jn", "Nagpur Jn", "Kota Jn"])
    random.seed()

    return jsonify({
        "train_number": train_number,
        "progress_percent": progress,
        "delay_minutes": delay,
        "next_station": next_station,
        "eta_next_station": (datetime.now() + timedelta(minutes=random.randint(10, 90))).strftime("%H:%M"),
    })


# ---------- FOOD ORDERING ----------
@app.route("/food")
def food():
    return render_template("food.html", menu=FOOD_MENU, active="food")


@app.route("/food/order", methods=["POST"])
def food_order():
    data = request.get_json()
    order_id = f"FD{random.randint(1000, 9999)}"
    return jsonify({
        "success": True,
        "order_id": order_id,
        "items": data.get("items", []),
        "total": data.get("total", 0),
        "eta_minutes": random.randint(20, 45),
    })


# ---------- R-WALLET ----------
@app.route("/wallet")
def wallet():
    return render_template("wallet.html", wallet=WALLET, active="wallet")


# ---------- COMPLAINTS (RAIL MADAD STYLE) ----------
@app.route("/complaints")
def complaints():
    return render_template("complaints.html", categories=COMPLAINT_CATEGORIES, active="complaints")


@app.route("/complaints/submit", methods=["POST"])
def complaints_submit():
    data = request.get_json()
    complaint_id = f"CMP{random.randint(10000, 99999)}"
    return jsonify({
        "success": True,
        "complaint_id": complaint_id,
        "category": data.get("category"),
        "message": "Your complaint has been registered. (This is a demo — it won't be sent to a real team.)",
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")