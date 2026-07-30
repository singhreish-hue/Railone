// ============================================
// main.js — RailClone demo interactivity
// Each function belongs to one page; a function not needed on the current page
// simply never gets called (only the bottom-nav menu toggle runs on every page).
// ============================================

// ---------- Bottom nav "Menu" slide-up sheet (runs on every page) ----------
document.addEventListener("DOMContentLoaded", () => {
    const menuBtn = document.getElementById("menuTabBtn");
    const sheet = document.getElementById("menuSheet");
    const overlay = document.getElementById("menuOverlay");

    function openMenu() {
        sheet.classList.add("show");
        overlay.classList.add("show");
    }
    function closeMenu() {
        sheet.classList.remove("show");
        overlay.classList.remove("show");
    }

    if (menuBtn) menuBtn.addEventListener("click", openMenu);
    if (overlay) overlay.addEventListener("click", closeMenu);
});


// ---------- Booking Results page: class select + dummy payment modal ----------
function initBookingResults() {
    const modal = document.getElementById("bookingModal");
    const modalTrainName = document.getElementById("modalTrainName");
    const modalClassInfo = document.getElementById("modalClassInfo");
    const resultBanner = document.getElementById("bookingResult");
    let selectedBooking = null;

    document.querySelectorAll(".class-chip").forEach((chip) => {
        chip.addEventListener("click", () => {
            const trainBlock = chip.closest(".class-chips");
            selectedBooking = {
                train_number: trainBlock.dataset.trainNumber,
                train_name: trainBlock.dataset.trainName,
                class_code: chip.dataset.code,
                class_label: chip.dataset.label,
                fare: chip.dataset.fare,
            };
            modalTrainName.textContent = selectedBooking.train_name;
            modalClassInfo.textContent =
                `${selectedBooking.class_label} (${selectedBooking.class_code}) · ₹${selectedBooking.fare}`;
            resultBanner.classList.remove("show");
            resultBanner.innerHTML = "";
            modal.style.display = "block";
        });
    });

    document.getElementById("cancelBookingBtn").addEventListener("click", () => {
        modal.style.display = "none";
    });

    document.getElementById("confirmBookingBtn").addEventListener("click", async () => {
        const name = document.getElementById("passengerName").value.trim();
        const age = document.getElementById("passengerAge").value.trim();
        if (!name || !age) {
            alert("Please enter passenger name and age.");
            return;
        }
        const payload = {
            ...selectedBooking,
            passenger_name: name,
            passenger_age: age,
        };
        const res = await fetch("/booking/confirm", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });
        const data = await res.json();
        resultBanner.innerHTML = `
            <strong>Booking Confirmed (Demo)</strong><br>
            PNR: <span class="mono">${data.pnr}</span><br>
            Booking ID: <span class="mono">${data.booking_id}</span><br>
            ${data.passenger} · ${data.train} · ${selectedBooking.class_label}
        `;
        resultBanner.classList.add("show");
    });
}


// ---------- PNR Status page ----------
function initPnrChecker() {
    const input = document.getElementById("pnrInput");
    const btn = document.getElementById("checkPnrBtn");
    const errorEl = document.getElementById("pnrError");
    const resultEl = document.getElementById("pnrResult");

    btn.addEventListener("click", async () => {
        const pnr = input.value.trim();
        errorEl.style.display = "none";
        resultEl.style.display = "none";

        if (pnr.length !== 10 || isNaN(pnr)) {
            errorEl.textContent = "PNR number must be 10 digits.";
            errorEl.style.display = "block";
            return;
        }

        const res = await fetch("/pnr/check", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ pnr }),
        });

        if (!res.ok) {
            const err = await res.json();
            errorEl.textContent = err.error || "Something went wrong.";
            errorEl.style.display = "block";
            return;
        }

        const data = await res.json();
        document.getElementById("rTrain").textContent = `#${data.train_number} ${data.train_name}`;
        document.getElementById("rRoute").textContent = `${data.from} → ${data.to}`;
        document.getElementById("rDate").textContent = data.date_of_journey;
        document.getElementById("rSeat").textContent = `${data.coach} / ${data.seat}`;

        const statusEl = document.getElementById("rStatus");
        statusEl.textContent = data.status;
        statusEl.className = "badge " + (
            data.status.includes("Confirmed") ? "badge-confirmed" :
            data.status.includes("RAC") ? "badge-rac" : "badge-waitlist"
        );

        resultEl.style.display = "block";
    });
}


// ---------- Live Tracking page ----------
function initTracking() {
    const btn = document.getElementById("trackBtn");
    const select = document.getElementById("trainSelect");
    const trackCard = document.getElementById("trackCard");

    btn.addEventListener("click", async () => {
        const trainNumber = select.value;
        const trainName = select.options[select.selectedIndex].text;

        const res = await fetch(`/tracking/status/${trainNumber}`);
        const data = await res.json();

        document.getElementById("trackTrainName").textContent = trainName;
        document.getElementById("trackFill").style.width = data.progress_percent + "%";
        document.getElementById("trackDot").style.left = data.progress_percent + "%";
        document.getElementById("trackProgress").textContent = data.progress_percent + "%";
        document.getElementById("trackDelay").textContent =
            data.delay_minutes === 0 ? "On Time" : `${data.delay_minutes} min late`;
        document.getElementById("trackNextStation").textContent = data.next_station;
        document.getElementById("trackEta").textContent = data.eta_next_station;

        trackCard.style.display = "block";
    });
}


// ---------- Food Ordering page ----------
function initFoodOrdering() {
    const cart = {}; // id -> {name, price, qty}
    const cartBar = document.getElementById("cartBar");
    const cartSummary = document.getElementById("cartSummary");
    const resultBanner = document.getElementById("foodOrderResult");

    function updateCartBar() {
        const items = Object.values(cart).filter((i) => i.qty > 0);
        const totalItems = items.reduce((sum, i) => sum + i.qty, 0);
        const totalPrice = items.reduce((sum, i) => sum + i.qty * i.price, 0);
        if (totalItems === 0) {
            cartBar.style.display = "none";
        } else {
            cartBar.style.display = "flex";
            cartSummary.textContent = `${totalItems} items · ₹${totalPrice}`;
        }
    }

    document.querySelectorAll(".menu-item").forEach((row) => {
        const id = row.dataset.id;
        const name = row.dataset.name;
        const price = parseFloat(row.dataset.price);
        const qtyValueEl = row.querySelector(".qty-value");

        cart[id] = { name, price, qty: 0 };

        row.querySelector(".qty-plus").addEventListener("click", () => {
            cart[id].qty += 1;
            qtyValueEl.textContent = cart[id].qty;
            updateCartBar();
        });
        row.querySelector(".qty-minus").addEventListener("click", () => {
            cart[id].qty = Math.max(0, cart[id].qty - 1);
            qtyValueEl.textContent = cart[id].qty;
            updateCartBar();
        });
    });

    document.getElementById("placeOrderBtn").addEventListener("click", async () => {
        const items = Object.values(cart).filter((i) => i.qty > 0);
        const total = items.reduce((sum, i) => sum + i.qty * i.price, 0);
        const seat = document.getElementById("seatNumber").value.trim() || "N/A";

        const res = await fetch("/food/order", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ items, total, seat }),
        });
        const data = await res.json();

        resultBanner.innerHTML = `
            <strong>Order Placed (Demo)</strong><br>
            Order ID: <span class="mono">${data.order_id}</span><br>
            Total: ₹${data.total} · Seat: ${seat}<br>
            Estimated delivery: ~${data.eta_minutes} minutes
        `;
        resultBanner.classList.add("show");
    });
}


// ---------- Complaints page ----------
function initComplaints() {
    document.getElementById("submitComplaintBtn").addEventListener("click", async () => {
        const category = document.getElementById("complaintCategory").value;
        const details = document.getElementById("complaintDetails").value.trim();
        const train = document.getElementById("complaintTrain").value.trim();
        const resultBanner = document.getElementById("complaintResult");

        if (!details) {
            alert("Please describe the complaint details.");
            return;
        }

        const res = await fetch("/complaints/submit", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ category, details, train }),
        });
        const data = await res.json();

        resultBanner.innerHTML = `
            <strong>Complaint ID: <span class="mono">${data.complaint_id}</span></strong><br>
            ${data.message}
        `;
        resultBanner.classList.add("show");
    });
}