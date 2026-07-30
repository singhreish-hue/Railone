# RailClone — Demo App (RailOne-inspired UI clone)

⚠️ **Ye ek SAMPLE/DEMO project hai.** Isme koi real ticket booking, real payment, real PNR database,
ya real GPS tracking nahi hai. Sara data `dummy_data.py` me hardcoded hai. Isse real Indian Railways
services ke jagah kabhi use na karein.

## Kya-kya hai isme
- **Home** — hero + quick action tiles + departure-board style stats
- **Ticket Booking** — search form → sample train list → class select → dummy "payment" modal → fake PNR/Booking ID
- **PNR Status** — koi bhi 10-digit number daalo, ek consistent (fake) result milta hai
- **Live Tracking** — train choose karo, dummy progress bar + next station + ETA
- **Food Ordering** — menu se items add karo, cart bar, dummy order confirmation
- **R-Wallet** — dummy balance aur transaction history
- **Rail Madad (Complaints)** — form submit karo, dummy complaint ID milta hai

## Tech Stack
- Backend: Python + Flask
- Frontend: HTML (Jinja templates) + vanilla CSS + vanilla JavaScript
- Data: `dummy_data.py` me Python dicts/lists (koi database nahi)

## Kaise chalayein

```bash
pip install -r requirements.txt
python app.py
```

Fir browser me kholein: **http://127.0.0.1:5000**

## Folder Structure
```
railone-clone/
├── app.py                 → sabhi Flask routes
├── dummy_data.py          → fake trains, menu, wallet, complaint categories
├── requirements.txt
├── templates/
│   ├── base.html          → shared navbar + layout
│   ├── home.html
│   ├── booking.html
│   ├── booking_results.html
│   ├── pnr.html
│   ├── tracking.html
│   ├── food.html
│   ├── wallet.html
│   └── complaints.html
└── static/
    ├── css/style.css      → design tokens, sab styling
    └── js/main.js         → har page ka interactivity (init functions)
```

## Design decisions (line-by-line samajhne ke liye)
- **Colors**: Navy (`#0B1F3A`) + steel blue = train/night-sky feel; amber (`#E8871E`) accent = railway
  signal lamp; ye hi rang har page pe consistently use hue hain (`style.css` ke `:root` variables me).
- **Fonts**: Headings ke liye **Rajdhani** (railway ki Rajdhani Express se naam liya — subject se juda hua
  choice), body ke liye Inter, aur PNR/fare/seat jaise numbers ke liye **IBM Plex Mono** (ticket-printout
  jaisa feel dene ke liye).
  ke liye).
- **Signature element**: `.flap-board` — ek departure-board (split-flap) style component jo Home, PNR
  Status aur Live Tracking teeno pages pe repeat hota hai, taaki app ek consistent "railway station board"
  identity feel de.
- **No real backend calls**: `app.py` ke andar har `/xyz/confirm` ya `/xyz/check` route `random` module se
  fake data generate karta hai — koi external API, database ya payment gateway call nahi hoti.
