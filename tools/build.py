#!/usr/bin/env python3
"""Builds the Padharo Invites static site into /home/user/padharo-site."""
import os, json

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DOMAIN = "https://padharoinvites.in"
UPDATED = "26 November 2026"

CO = {
    "entity": "KwikReach Solutions",
    "phone": "+91 83472 00125",
    "tel": "+918347200125",
    "wa": "https://wa.me/918347200125",
    "email": "kwikreach.solutions@gmail.com",
    "city": "Ahmedabad, Gujarat, India",
    "address": "Ahmedabad, Gujarat 380015, India",
    "hours": "Monday to Saturday, 10:00 AM to 7:00 PM IST",
}

P = {
 "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 "send": '<path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/>',
 "message": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
 "checkcircle": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="m9 11 3 3L22 4"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "bed": '<path d="M2 20v-8a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v8"/><path d="M4 10V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v4"/><path d="M12 4v6"/><path d="M2 18h20"/>',
 "utensils": '<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/>',
 "wallet": '<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>',
 "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
 "calendar": '<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/>',
 "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "lock": '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 "gift": '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5A4.8 8 0 0 1 12 8a4.8 8 0 0 1 4.5-5 2.5 2.5 0 0 1 0 5"/>',
 "clipboard": '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/>',
 "image": '<rect width="18" height="18" x="3" y="3" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.09-3.09a2 2 0 0 0-2.82 0L6 21"/>',
 "usercheck": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/>',
 "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
 "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
 "gem": '<path d="M6 3h12l4 6-10 13L2 9Z"/><path d="M11 3 8 9l4 13 4-13-3-6"/><path d="M2 9h20"/>',
 "baby": '<path d="M9 12h.01"/><path d="M15 12h.01"/><path d="M10 16c.5.3 1.2.5 2 .5s1.5-.2 2-.5"/><path d="M19 6.3a9 9 0 0 1 1.8 3.9 2 2 0 0 1 0 3.6 9 9 0 0 1-17.6 0 2 2 0 0 1 0-3.6A9 9 0 0 1 12 3c2 0 3.5 1.1 3.5 2.5s-.9 2.5-2 2.5c-.8 0-1.5-.4-1.5-1"/>',
 "cake": '<path d="M20 21v-8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8"/><path d="M4 16s.5-1 2-1 2.5 2 4 2 2.5-2 4-2 2.5 2 4 2 2-1 2-1"/><path d="M2 21h20"/><path d="M7 8v3"/><path d="M12 8v3"/><path d="M17 8v3"/>',
 "plus": '<path d="M5 12h14"/><path d="M12 5v14"/>',
 "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
 "menu": '<line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>',
 "smartphone": '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>',
 "trash": '<path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>',
 "briefcase": '<rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
 "listchecks": '<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
 "eye": '<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>',
 "sparkle": '<path d="M12 3l1.9 5.8L20 10.7l-5 3.6 1.9 5.9L12 16.6l-4.9 3.6L9 14.3l-5-3.6 6.1-1.9Z"/>',
 "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9v12h14V9"/>',
}

def ic(name, size=22, sw=1.8):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>')

NAV = [("/#features", "Features"), ("/#how", "How it works"), ("/#faq", "FAQ"), ("/contact/", "Contact")]

def header(current):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand-link" href="/" aria-label="Padharo Invites home"><img src="/assets/lockup.svg" alt="Padharo Invites" width="133" height="44"></a>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav">{ic("menu")}</button>
    <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn btn-sm" href="/#apps">Get the app</a></nav>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="/assets/lockup-on-maroon.svg" alt="Padharo Invites" width="157" height="52">
        <p>One simple app to invite guests and run every family event, from the first list to the last thank you.</p>
      </div>
      <div>
        <h4>Product</h4>
        <ul>
          <li><a href="/#features">Features</a></li>
          <li><a href="/#how">How it works</a></li>
          <li><a href="/#apps">Android and iOS apps</a></li>
          <li><a href="/#faq">FAQ</a></li>
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="/privacy-policy/">Privacy Policy</a></li>
          <li><a href="/terms/">Terms and Conditions</a></li>
          <li><a href="/data-deletion/">Data deletion</a></li>
          <li><a href="/contact/">Contact us</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{CO["tel"]}">{CO["phone"]}</a></li>
          <li><a href="mailto:{CO["email"]}">{CO["email"]}</a></li>
          <li><a href="{CO["wa"]}" rel="noopener">Chat on WhatsApp</a></li>
          <li>{CO["city"]}</li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 Padharo Invites, a product of {CO["entity"]}. All rights reserved.</span>
      <span>WhatsApp is a trademark of Meta Platforms, Inc.</span>
    </div>
  </div>
</footer>
<script>
(function(){{var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');if(!b||!n)return;
b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Close menu':'Open menu');}});
n.addEventListener('click',function(e){{if(e.target.tagName==='A'){{n.classList.remove('open');b.setAttribute('aria-expanded','false');}}}});}})();
</script>'''

def page(path, title, desc, body, current="", extra_head=""):
    url = DOMAIN + path
    html = f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#8C1D40">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Padharo Invites">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/padharo-invites-instagram-1080.png">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/assets/favicon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon-180.png">
<link rel="preload" href="/assets/fonts/plus-jakarta-sans-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
{extra_head}
</head>
<body>
{header(current)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
'''
    if path.endswith(".html"):
        fn = os.path.join(OUT, path.strip("/"))
    else:
        d = os.path.join(OUT, path.strip("/"))
        os.makedirs(d, exist_ok=True)
        fn = os.path.join(d, "index.html")
    open(fn, "w").write(html)

def tick(t):
    return f'<li>{ic("check", 20, 2.4)}<span>{t}</span></li>'

# ---------------------------------------------------------------- HOME
features = [
 ("users", "Guest list by family", "Add families, not loose names. Pick from your phone contacts, add members, and see who is a guest of which side."),
 ("send", "WhatsApp invites", "Send invites one by one from your own WhatsApp, or to everyone at once from Padharo’s verified business number."),
 ("image", "Name on every card", "Upload your own card as an image or PDF. Each family’s name and count is printed on it before it goes out."),
 ("checkcircle", "RSVP in one tap", "Guests reply with Coming or Not coming buttons. Counts update for every function on their own."),
 ("eye", "See who read it", "Know which invites were delivered and read, and who still needs a gentle nudge."),
 ("calendar", "Functions and invites", "Plan Haldi, Mehendi, Sangeet, the main day and more, each with its own time, venue and guest list."),
 ("bell", "Automatic reminders", "Schedule reminders a day before each function, or at the time you choose. Padharo warns you before late-night sends."),
 ("bed", "Rooms for guests", "Give rooms to each visiting family, add room numbers later, and message only the families whose room changed."),
 ("utensils", "Food plan", "Set your main food, then mark only the exceptions such as Jain or Swaminarayan. Share plate counts with your caterer."),
 ("wallet", "Money and expenses", "Track budget, payments and dues. Split shared costs and settle up with the fewest payments."),
 ("gift", "Gifts and shagun", "Note who gave what with a quick name search, and see it on each family’s page later."),
 ("briefcase", "Team and work areas", "Invite family members as Admin, Helper or Viewer, and give someone charge of catering, decor or travel."),
 ("usercheck", "Arrivals on the day", "Mark who actually arrived at each function and keep notes about any guest, with a full change history."),
 ("lock", "Lock before you send", "Padharo checks dates, venues, card and sender before a bulk send, so nothing goes out half ready."),
 ("layers", "Many events, one app", "Run a wedding and a birthday side by side. You can be the Owner of one and a Helper on another."),
]
feat_html = "".join(
    f'<article class="feat"><div class="ic">{ic(i)}</div><h3>{t}</h3><p>{d}</p></article>' for i, t, d in features)

types = [("heart", "Weddings"), ("gem", "Engagements"), ("baby", "Baby showers"), ("cake", "Birthdays"),
         ("home", "Griha pravesh"), ("plus", "Your own event type")]
types_html = "".join(f'<span class="type"><span class="ic">{ic(i, 18)}</span>{t}</span>' for i, t in types)

faqs = [
 ("When can I download Padharo Invites?",
  "The Android and iOS apps are launching soon on Google Play and the App Store. Message us on WhatsApp or email us and we will tell you the day they go live."),
 ("Do my guests need to install the app?",
  "No. Guests get your invite on WhatsApp and reply with a tap. Only you and the family members who help you plan use the app."),
 ("Which number sends the invites?",
  "You can send one by one from your own WhatsApp. For bulk sends, invites go from Padharo’s verified WhatsApp business number, and every message names you as the host."),
 ("Can guests stop getting messages?",
  "Yes. Every invite and reminder lets the guest opt out, and Padharo stops all further messages to that number for your event."),
 ("Is it only for weddings?",
  "No. Padharo works for engagements, baby showers, birthdays, griha pravesh and any event type you create yourself. Features follow your event type, so a birthday stays simple."),
 ("Is my guest list safe?",
  "Your guest list is used only to run your event. We never sell it or use it for advertising. You can delete your event or your account whenever you want."),
 ("How much does it cost?",
  "You can start free with a small guest list. Plans for bigger events will be shown clearly in the app before you pay anything, and you pay once per event, not every month."),
]
faq_html = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)

jsonld = {
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "Organization", "name": "Padharo Invites", "url": DOMAIN, "logo": DOMAIN + "/assets/favicon-192.png",
     "parentOrganization": {"@type": "Organization", "name": CO["entity"]},
     "email": CO["email"], "telephone": CO["tel"],
     "address": {"@type": "PostalAddress", "addressLocality": "Ahmedabad", "addressRegion": "Gujarat", "postalCode": "380015", "addressCountry": "IN"}},
    {"@type": "SoftwareApplication", "name": "Padharo Invites", "operatingSystem": "Android, iOS",
     "applicationCategory": "LifestyleApplication",
     "description": "Send event invites on WhatsApp, collect RSVPs and manage guests, rooms, food and money for weddings and family events."}
  ]}

home = f'''
<section class="hero">
  <div class="wrap">
    <div>
      <span class="eyebrow"><span class="dot"></span>Android and iOS apps launching soon</span>
      <h1>Invite everyone. <em>Welcome</em> every guest.</h1>
      <p class="lead">Padharo Invites is one simple app for weddings and family events. Send invites on WhatsApp, collect RSVPs in a tap, and manage guests, rooms, food and money in one place. No spreadsheets.</p>
      <div class="hero-actions">
        <a class="btn" href="#apps">Get notified at launch</a>
        <a class="btn btn-ghost" href="#features">See all features</a>
      </div>
      <div class="store-row" aria-label="App availability">
        <span class="store">{ic("smartphone", 26)}<span><small>Android app</small><b>Google Play <span class="soon">Soon</span></b></span></span>
        <span class="store">{ic("smartphone", 26)}<span><small>iPhone app</small><b>App Store <span class="soon">Soon</span></b></span></span>
      </div>
    </div>
    <div class="phone-stage" aria-hidden="true">
      <div class="float-card fc-1"><span class="ic" style="background:var(--success-tint);color:var(--success-ink)">{ic("checkcircle", 18, 2)}</span><span>Shah family is coming<small>4 people, Haldi and Wedding</small></span></div>
      <div class="phone">
        <div class="notch"></div>
        <div class="p-top"><div><div class="t">Your event</div><div class="n">Riya &amp; Arjun’s Wedding</div></div><div class="p-avatar">RA</div></div>
        <div class="p-hero">
          <span class="pill">12 Dec, 4 functions</span>
          <h4>16 days to go</h4>
          <p>Wedding day, Sat 27 Dec, Ahmedabad</p>
          <div class="p-stats"><div><b>212</b><span>Families</span></div><div><b>168</b><span>Coming</span></div><div><b>31</b><span>To reply</span></div></div>
        </div>
        <div class="p-next"><span class="ic">{ic("bell", 18, 2)}</span><span><b>Remind 31 families</b><span>Mehendi is tomorrow at 5 PM</span></span></div>
        <div class="p-list">
          <div class="p-row"><span class="av">MP</span><span class="nm">Mehta Parivar<small>5 people</small></span><span class="tag tag-yes">Coming</span></div>
          <div class="p-row"><span class="av">KD</span><span class="nm">Kavita Desai<small>In couple</small></span><span class="tag tag-read">Read</span></div>
          <div class="p-row"><span class="av">JP</span><span class="nm">Jignesh Patel<small>Solo</small></span><span class="tag tag-wait">Sent</span></div>
        </div>
        <div class="p-tabs"><span class="on"><i></i>Home</span><span><i></i>Guests</span><span><i></i>Invites</span><span><i></i>Money</span><span><i></i>More</span></div>
      </div>
      <div class="float-card fc-2"><span class="ic" style="background:var(--brand-tint);color:var(--brand)">{ic("send", 18, 2)}</span><span>212 invites sent<small>198 delivered, 176 read</small></span></div>
    </div>
  </div>
</section>

<section class="band" style="padding:48px 0">
  <div class="wrap">
    <div class="section-head center" style="margin-bottom:24px"><p style="font-weight:700;color:var(--ink)">Made for every family occasion</p></div>
    <div class="types">{types_html}</div>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <div class="section-head center">
      <span class="kicker">How it works</span>
      <h2>Ready in three simple steps</h2>
      <p>If you can use WhatsApp, you can use Padharo. No training needed.</p>
    </div>
    <div class="steps">
      <div class="step"><div class="num">1</div><h3>Create your event</h3><p>Pick the event type, add your functions with dates and venues, and upload your invitation card.</p></div>
      <div class="step"><div class="num">2</div><h3>Add your guests</h3><p>Choose families from your contacts. Padharo stops duplicates, even when the same number is saved under another name.</p></div>
      <div class="step"><div class="num">3</div><h3>Send and relax</h3><p>Send personalised invites on WhatsApp. RSVPs, counts and reminders take care of themselves.</p></div>
    </div>
  </div>
</section>

<section class="band" id="features">
  <div class="wrap">
    <div class="spot">
      <div>
        <span class="kicker">Invites on WhatsApp</span>
        <h3>A personal invite for every family, sent in minutes</h3>
        <p>Your card, with each family’s name on it, reaches them on the app they already use. Guests tap a button to reply, and you see the answer straight away.</p>
        <ul class="ticks">
          {tick("Send one by one from your own number, or in bulk from Padharo’s verified business number")}
          {tick("Family name and count printed on your own card design")}
          {tick("Delivered and read status for every invite")}
          {tick("A main invite plus separate invites for close-family functions")}
        </ul>
      </div>
      <div class="spot-media" aria-hidden="true">
        <div class="wa-wall">
          <div class="wa-bubble">
            <div class="wa-card"><div class="ornament">SHUBH VIVAH</div><h5>Riya weds Arjun</h5><p>Saturday, 27 December 2026<br>Ahmedabad</p><span class="guest">Mehta Parivar, 5 guests</span></div>
            <div class="wa-text">Namaste Mehta Parivar, the Shah family warmly invites you to Riya and Arjun’s wedding. Please let us know if you can come.</div>
            <div class="wa-meta">10:24 AM</div>
            <div class="wa-btns"><span>Yes, we’re coming</span><span>Sorry, can’t come</span></div>
          </div>
        </div>
      </div>
    </div>

    <div class="spot flip">
      <div>
        <span class="kicker">RSVP and headcount</span>
        <h3>Know exactly who is coming to each function</h3>
        <p>Each function keeps its own count. Families are grouped as Solo, In couple or With family, so seating and catering are easy to plan.</p>
        <ul class="ticks">
          {tick("Counts per function, updated the moment a guest replies")}
          {tick("Change a family’s count for one function without touching the rest")}
          {tick("Scheduled reminders, with a warning before late-night sends")}
          {tick("Mark actual arrivals on the day")}
        </ul>
      </div>
      <div class="spot-media" aria-hidden="true">
        <div class="mini-head"><b>Replies so far</b><span>212 families</span></div>
        <div class="bar"><i style="width:79%;background:var(--success)"></i><i style="width:6%;background:var(--brand)"></i><i style="width:15%;background:var(--marigold)"></i></div>
        <div class="legend"><span style="--c:var(--success)">Coming 168</span><span style="--c:var(--brand)">Not coming 13</span><span style="--c:var(--marigold)">Waiting 31</span></div>
        <div style="margin-top:18px">
          <div class="fn-row"><span><b>Haldi</b><small>Fri 26 Dec, 9 AM, Home</small></span><span class="chip chip-ok">64 people</span></div>
          <div class="fn-row"><span><b>Mehendi</b><small>Fri 26 Dec, 5 PM, Lawn</small></span><span class="chip chip-ok">142 people</span></div>
          <div class="fn-row"><span><b>Wedding</b><small>Sat 27 Dec, 7 PM, Party plot</small></span><span class="chip chip-ok">486 people</span></div>
          <div class="fn-row"><span><b>Reminder</b><small>1 day before each function</small></span><span class="chip chip-brand">Scheduled</span></div>
        </div>
      </div>
    </div>

    <div class="spot">
      <div>
        <span class="kicker">Rooms and food</span>
        <h3>Stays and meals sorted, family by family</h3>
        <p>Give rooms to visiting families now and add room numbers when the hotel confirms. Plan food by marking only the exceptions.</p>
        <ul class="ticks">
          {tick("Rooms per family, with room numbers added later")}
          {tick("Only families whose room changed get a new message")}
          {tick("Main food plus Jain, Swaminarayan, Vegan and other choices")}
          {tick("Plate counts per meal, ready to share with your caterer")}
        </ul>
      </div>
      <div class="spot-media" aria-hidden="true">
        <div class="mini-head"><b>Rooms</b><span>Hotel Shyam, 38 rooms</span></div>
        <div class="room-grid">
          <div class="room"><b>Mehta Parivar</b><span>2 rooms, 204 and 205</span></div>
          <div class="room"><b>Desai family</b><span>1 room, 118</span></div>
          <div class="room"><b>Joshi family</b><span>2 rooms, numbers later</span></div>
          <div class="room"><b>Kavita Desai</b><span>1 room, 121</span></div>
        </div>
        <div class="note-box"><b>Wedding dinner:</b> 486 plates. Main food Veg, with 42 Jain, 18 Swaminarayan and 6 kids meals.</div>
      </div>
    </div>

    <div class="spot flip">
      <div>
        <span class="kicker">Money and team</span>
        <h3>Plan together, and keep the money clear</h3>
        <p>Bring in family members to help, each with the right access. Track every expense and settle up fairly when it is all over.</p>
        <ul class="ticks">
          {tick("Roles for Owner, Admin, Helper and Viewer, set per event")}
          {tick("Work areas such as catering, decor and travel, each with its own person in charge")}
          {tick("Budget, payments, due-date alerts and gift records")}
          {tick("Settle shared costs with the fewest payments")}
        </ul>
      </div>
      <div class="spot-media" aria-hidden="true">
        <div class="mini-head"><b>Budget</b><span>62% used</span></div>
        <div class="bar"><i style="width:62%;background:var(--brand)"></i></div>
        <div style="margin-top:18px">
          <div class="fn-row"><span><b>Caterer advance</b><small>Paid by Rakesh</small></span><span class="chip chip-ok">Paid</span></div>
          <div class="fn-row"><span><b>Decor balance</b><small>Due on 20 Dec</small></span><span class="chip chip-wait">Due soon</span></div>
          <div class="fn-row"><span><b>Catering area</b><small>Nisha is in charge</small></span><span class="chip chip-brand">Admin</span></div>
          <div class="fn-row"><span><b>Settle up</b><small>3 payments clear everything</small></span><span class="chip">Ready</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head center">
      <span class="kicker">All features</span>
      <h2>Everything your event needs, nothing it doesn’t</h2>
      <p>Padharo shows only the features that suit your event type. You can add more any time from the More tab.</p>
    </div>
    <div class="grid">{feat_html}</div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head center">
      <span class="kicker">Your privacy</span>
      <h2>Respectful to you and your guests</h2>
    </div>
    <div class="trust">
      <div>{ic("shield", 28)}<h3>Your list stays yours</h3><p>Guest details are used only to run your event. We never sell them or use them for ads.</p></div>
      <div>{ic("message", 28)}<h3>Messages guests expect</h3><p>Only event invites, updates and reminders, from people they know. Guests can opt out at any time.</p></div>
      <div>{ic("trash", 28)}<h3>Delete whenever you want</h3><p>Remove a guest, an event or your whole account from the app. <a href="/data-deletion/">See how</a>.</p></div>
    </div>
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="section-head center"><span class="kicker">FAQ</span><h2>Questions families ask us</h2></div>
    <div class="faq">{faq_html}</div>
  </div>
</section>

<section id="apps" style="padding-top:16px">
  <div class="wrap">
    <div class="cta">
      <h2>Android and iOS apps launching soon</h2>
      <p>Planning an event in the coming months? Message us and we will let you know the day Padharo Invites is live on Google Play and the App Store.</p>
      <div class="row">
        <a class="btn" href="{CO["wa"]}?text=Hi%2C%20please%20notify%20me%20when%20Padharo%20Invites%20launches." rel="noopener">{ic("message", 20, 2)}Notify me on WhatsApp</a>
        <a class="btn btn-line" href="mailto:{CO["email"]}?subject=Notify%20me%20when%20Padharo%20Invites%20launches">{ic("mail", 20, 2)}Email us</a>
      </div>
    </div>
  </div>
</section>
'''
page("/", "Padharo Invites | WhatsApp invites and event planning app",
     "Send wedding and family event invites on WhatsApp, collect RSVPs in a tap, and manage guests, rooms, food and money in one simple app. Android and iOS launching soon.",
     home, extra_head=f'<script type="application/ld+json">{json.dumps(jsonld)}</script>')

# ---------------------------------------------------------------- LEGAL helper
def legal(path, title, h1, intro, sections, current=""):
    toc = "".join(f'<li><a href="#{sid}">{t}</a></li>' for sid, t, _ in sections)
    body_s = "".join(f'<h2 id="{sid}">{t}</h2>{c}' for sid, t, c in sections)
    body = f'''<div class="wrap">
  <div class="page-head"><h1>{h1}</h1><p>{intro}</p><span class="updated">Last updated: {UPDATED}</span></div>
  <div class="doc"><aside class="toc" aria-label="On this page"><b>On this page</b><ol>{toc}</ol></aside><article class="prose">{body_s}</article></div>
</div>'''
    page(path, title, intro, body, current)

contact_block = f'''<div class="table-scroll"><table>
<tr><th>Business</th><td>Padharo Invites, a product of {CO["entity"]}</td></tr>
<tr><th>Address</th><td>{CO["address"]}</td></tr>
<tr><th>Email</th><td><a href="mailto:{CO["email"]}">{CO["email"]}</a></td></tr>
<tr><th>Phone and WhatsApp</th><td><a href="tel:{CO["tel"]}">{CO["phone"]}</a></td></tr>
<tr><th>Hours</th><td>{CO["hours"]}</td></tr>
</table></div>'''

# ---------------------------------------------------------------- PRIVACY
privacy = [
 ("who", "Who we are", f'''<p>Padharo Invites (“Padharo”, “we”, “us”) is a mobile app and website for sending event invitations and managing events such as weddings, engagements, baby showers and birthdays. Padharo is a product of <strong>{CO["entity"]}</strong>, {CO["address"]}.</p>
<p>This policy explains what personal data we collect through the Padharo app, the website at padharoinvites.in, and the WhatsApp messages sent through Padharo, how we use it, and the choices you have. It is written to meet the Digital Personal Data Protection Act, 2023 and the Information Technology Act, 2000 of India.</p>'''),
 ("roles", "Hosts and guests", '''<p>Padharo has two kinds of people:</p>
<ul><li><strong>Hosts</strong> are people who create an account and plan an event, along with the family members they invite to help (Admins, Helpers and Viewers).</li>
<li><strong>Guests</strong> are people a host adds to an event so they can receive invites, reminders and event updates. Guests do not need to install the app.</li></ul>
<p>For guest details, the host decides whom to invite and what to record. We process guest details on the host’s behalf, only to run that host’s event. Hosts must add only people they personally know and who would expect to hear from them about the event.</p>'''),
 ("collect", "Information we collect", '''<h3>From hosts</h3>
<ul><li>Account details: name, mobile number and, if you give it, email address.</li>
<li>Event details: event type, functions, dates, times, venues, invitation card images or PDFs, and settings.</li>
<li>Planning records you enter: rooms, food choices, budget, expenses, payments between family members, gifts, notes and work areas.</li>
<li>Purchase records: which plan or message pack was bought for an event. Payments are handled by Google Play or the Apple App Store, and we do not receive your card or bank details.</li></ul>
<h3>About guests (entered by the host)</h3>
<ul><li>Name, mobile number (and a second number if added), family or household members, relation or side (“guest of”), and counts per function.</li>
<li>RSVP replies, food choices, room assignments, arrival status, gifts and notes the host records.</li></ul>
<h3>When guests reply on WhatsApp</h3>
<ul><li>The guest’s WhatsApp number and profile name, their reply (for example “Coming” or “Not coming”), and message status such as sent, delivered and read, as provided by the WhatsApp Business Platform.</li></ul>
<h3>Phone contacts</h3>
<p>If a host chooses to add guests from their phone contacts, the app asks for permission first. Only the contacts the host picks are uploaded. We do not upload the whole address book.</p>
<h3>Technical data</h3>
<ul><li>Device type, operating system, app version, crash reports and basic usage events, used to keep the app working and improve it.</li>
<li>This website does not use advertising or tracking cookies. Our web host may keep standard server logs (such as IP address and pages requested) for security.</li></ul>'''),
 ("use", "How we use information", '''<ul><li>To create and secure your account, including verifying your mobile number with a one-time code.</li>
<li>To send invitations, RSVP requests, reminders, room details and event updates to guests on WhatsApp, as the host instructs.</li>
<li>To show hosts RSVP replies, counts, delivery and read status, and other event information.</li>
<li>To let family members a host invites see and edit the parts of the event their role allows.</li>
<li>To process purchases and show purchase history.</li>
<li>To give support, prevent misuse and spam, and meet legal duties.</li></ul>
<p>We do <strong>not</strong> sell personal data, and we do not use guest details for advertising or to message guests about anything other than the host’s event.</p>'''),
 ("whatsapp", "WhatsApp messages", '''<p>Padharo sends messages through the WhatsApp Business Platform (Cloud API) provided by Meta Platforms, Inc. When a message is sent, the recipient’s number and the message content pass through Meta’s systems under Meta’s own terms and privacy policy.</p>
<ul><li>Messages are only about the host’s event: invitations, RSVP requests, reminders, room details and updates.</li>
<li>Every bulk message names the host, so guests know who invited them.</li>
<li><strong>Opting out:</strong> a guest can reply “STOP” or use the opt-out option in a message at any time. We then stop all further messages to that number for that event, and record the opt-out.</li>
<li>A host may also send invites one by one from their own WhatsApp. Those messages go from the host’s phone, and we do not read them.</li></ul>'''),
 ("share", "Who we share information with", '''<p>We share personal data only as needed to run Padharo:</p>
<ul><li><strong>Meta Platforms, Inc.</strong>, to deliver WhatsApp messages.</li>
<li><strong>Cloud hosting and database providers</strong>, to store data securely.</li>
<li><strong>Google Play and Apple App Store</strong>, to process in-app purchases.</li>
<li><strong>Crash reporting and SMS one-time code providers</strong>, to keep the app reliable and secure.</li>
<li><strong>Other members of the same event</strong>, as allowed by the roles the event Owner sets. For example, money details can be hidden from Helpers.</li>
<li><strong>Authorities</strong>, only when the law requires it.</li></ul>
<p>Our providers may process data outside India. When they do, we require them to protect it as this policy describes.</p>'''),
 ("keep", "How long we keep information", '''<ul><li>Event data is kept while the event is active and for 12 months after the last function, so hosts can look back at it. Hosts can delete an event sooner.</li>
<li>Account data is kept until you delete your account.</li>
<li>When an event or account is deleted, we remove its data from our live systems within 30 days, and from backups within 90 days.</li>
<li>We may keep limited records longer where the law requires it, such as purchase and tax records, or records of opt-outs so we keep honouring them.</li></ul>'''),
 ("security", "How we protect information", '''<p>Data is encrypted in transit (HTTPS) and at rest. Access inside an event follows the roles the Owner sets, and access by our staff is limited to support and security needs. No system is perfectly secure, but we work to protect your data and will tell affected users and authorities about a serious breach as the law requires.</p>'''),
 ("rights", "Your choices and rights", '''<p>You can ask to access, correct or delete your personal data, withdraw consent, or nominate someone to act for you. Hosts can edit or delete most data directly in the app.</p>
<ul><li><strong>Guests:</strong> to stop messages, reply “STOP”. To have your details removed from an event, ask the host, or contact us with your mobile number and the event name.</li>
<li><strong>Deleting your account:</strong> see our <a href="/data-deletion/">data deletion instructions</a>.</li></ul>
<p>We reply to requests within 7 days and complete them within 30 days.</p>'''),
 ("children", "Children", '''<p>Hosts must be 18 or older. Hosts may record children as members of a guest family (for example, for headcounts or kids meals). We do not knowingly let children create accounts, and we do not use children’s data for tracking or advertising.</p>'''),
 ("changes", "Changes to this policy", '''<p>We may update this policy as Padharo grows. We will post the new version here with a new date, and tell hosts in the app about important changes.</p>'''),
 ("grievance", "Contact and Grievance Officer", f'''<p>For any privacy question or complaint, contact our Grievance Officer. We acknowledge complaints within 24 hours and resolve them within 15 working days.</p>{contact_block}
<p>If you are not satisfied with our response, you may approach the Data Protection Board of India.</p>'''),
]
legal("/privacy-policy/", "Privacy Policy | Padharo Invites", "Privacy Policy",
      "How Padharo Invites collects, uses and protects the personal data of hosts and their guests.", privacy)

# ---------------------------------------------------------------- TERMS
terms = [
 ("accept", "About these terms", f'''<p>These terms are an agreement between you and <strong>{CO["entity"]}</strong> (“we”, “us”), the maker of Padharo Invites (“Padharo”). They apply when you use the Padharo app, the website padharoinvites.in, or messages sent through Padharo. By creating an account or using Padharo, you agree to these terms and to our <a href="/privacy-policy/">Privacy Policy</a>.</p>'''),
 ("service", "What Padharo does", '''<p>Padharo helps you plan events and invite guests. It lets you build a guest list, send invitations and reminders on WhatsApp, collect RSVPs, and manage functions, rooms, food, money, gifts and your planning team. Some features depend on your event type and plan.</p>
<p>The Android and iOS apps are launching soon. Features may change as we improve the service.</p>'''),
 ("account", "Your account", '''<ul><li>You must be at least 18 years old and give a mobile number you own.</li>
<li>Keep your phone and one-time codes safe. You are responsible for activity on your account.</li>
<li>The person who creates an event is its <strong>Owner</strong>. The Owner decides who can join the event and what each role can see and change.</li></ul>'''),
 ("messaging", "Rules for sending messages", '''<p>Padharo is for personal and family events. When you send messages through Padharo, you agree that:</p>
<ul><li>You will only add guests you personally know, who would expect to hear from you about your event, and you have their permission to use their number for it.</li>
<li>You will only send event invitations, RSVP requests, reminders and event updates. No advertising, promotions, sales messages, political or religious campaigns, or anything unrelated to your event.</li>
<li>You will not send content that is unlawful, hateful, obscene, threatening, misleading, or that infringes anyone’s rights.</li>
<li>You will respect opt-outs. Padharo stops messages to anyone who opts out, and you must not try to get around this.</li>
<li>You will follow the WhatsApp Business Messaging Policy and Meta’s terms that apply to messages sent through the WhatsApp Business Platform.</li></ul>
<p>We may pause sending, remove content, or suspend an account that breaks these rules, gets many spam reports, or puts our WhatsApp number at risk.</p>'''),
 ("content", "Your content", '''<p>You keep ownership of what you upload, such as invitation cards, photos, names and notes. You give us permission to store, process, print guest names on your cards, and send this content only to run your event. You confirm you have the right to use any card design or image you upload.</p>'''),
 ("payments", "Plans and payments", '''<ul><li>You can start for free. Paid plans and message packs, where offered, are shown with their price in the app before you pay.</li>
<li>Purchases are one-time per event, not subscriptions, unless the app clearly says otherwise.</li>
<li>Payments are processed by Google Play or the Apple App Store, and their refund rules apply. If something went wrong with a purchase, contact us and we will help.</li>
<li>Only the event Owner, or an Admin the Owner allows, can buy plans for an event.</li>
<li>Message charges set by Meta can change. If they change, new prices apply only to purchases made after the change.</li></ul>'''),
 ("availability", "Availability", '''<p>We work to keep Padharo running smoothly, but we cannot promise it will always be available or error free. WhatsApp delivery depends on Meta, mobile networks and the guest’s phone, and some messages may be delayed or not delivered. Please keep your own backup of anything critical, such as final guest counts for your caterer.</p>'''),
 ("ip", "Our rights", '''<p>The Padharo name, logo, app and website belong to us. You may not copy, resell, reverse engineer or misuse them, or use Padharo to build a competing service.</p>'''),
 ("ending", "Ending your use", '''<p>You can stop using Padharo and delete your account at any time. See <a href="/data-deletion/">data deletion</a>. We may suspend or close accounts that break these terms or the law, and we will tell you why where we can.</p>'''),
 ("liability", "Limits of our responsibility", '''<p>Padharo is provided “as is”. To the extent the law allows, we are not responsible for indirect losses, such as costs from a guest not receiving a message, event changes, or decisions made from data in the app. Our total responsibility to you for any claim is limited to the amount you paid us for the event in question in the 12 months before the claim.</p>
<p>You agree to cover us against claims arising from messages you send or content you upload in breach of these terms.</p>'''),
 ("law", "Governing law", '''<p>These terms are governed by the laws of India. Courts in Ahmedabad, Gujarat have exclusive jurisdiction, subject to any consumer rights you have that cannot be waived.</p>'''),
 ("changes", "Changes to these terms", '''<p>We may update these terms. We will post the new version here with a new date and tell you in the app about important changes. If you keep using Padharo after that, the new terms apply.</p>'''),
 ("contact", "Contact", contact_block),
]
legal("/terms/", "Terms and Conditions | Padharo Invites", "Terms and Conditions",
      "The rules for using the Padharo Invites app, website and WhatsApp messages.", terms)

# ---------------------------------------------------------------- DATA DELETION
deletion = [
 ("app", "Delete your account in the app", '''<ol class="steps-list">
<li><span>Open the Padharo Invites app and sign in.</span></li>
<li><span>Go to the <strong>More</strong> tab, then <strong>Account</strong>.</span></li>
<li><span>Tap <strong>Delete my account</strong>.</span></li>
<li><span>Read what will be deleted, then confirm with the one-time code sent to your mobile number.</span></li>
</ol>
<div class="callout"><p>If you are the Owner of an event that other family members still use, the app first asks you to hand ownership to someone else or delete that event.</p></div>'''),
 ("request", "Ask us to delete it", f'''<p>If you cannot use the app, send a deletion request to us by email or WhatsApp. Please send it from, or include, the mobile number on your account so we can verify it is you.</p>
<ul><li>Email: <a href="mailto:{CO["email"]}?subject=Padharo%20Invites%20data%20deletion%20request">{CO["email"]}</a> with the subject “Data deletion request”</li>
<li>WhatsApp: <a href="{CO["wa"]}?text=Data%20deletion%20request%20for%20Padharo%20Invites" rel="noopener">{CO["phone"]}</a></li></ul>
<p>We confirm your request within 7 days and complete it within 30 days.</p>'''),
 ("event", "Delete one event", '''<p>An event Owner can delete a single event from <strong>More</strong>, then <strong>Event settings</strong>, then <strong>Delete event</strong>. This removes the event’s guest list, RSVPs, rooms, food, money records, cards and messages history for everyone in that event.</p>'''),
 ("guests", "If you are a guest", f'''<p>You may have received an invite because a host added your number to their event.</p>
<ul><li><strong>To stop messages:</strong> reply “STOP” to the message, or use the opt-out option in it.</li>
<li><strong>To remove your details:</strong> ask the host to remove you from their guest list, or contact us with your mobile number and the event or host name, and we will remove your details from that event.</li></ul>'''),
 ("what", "What gets deleted", '''<ul><li>Your account details: name, mobile number and email.</li>
<li>Events you own, with their guest lists, RSVPs, cards, rooms, food plans, money records, gifts and notes.</li>
<li>Your membership in events owned by others. Changes you made there stay in that event’s history under “Former member”.</li></ul>
<p>Data is removed from live systems within 30 days and from backups within 90 days. We keep only what the law requires, such as purchase and tax records, and a record of opt-outs so we keep honouring them.</p>'''),
 ("facebook", "Signed in with Facebook or Meta?", '''<p>If you ever connected Padharo using a Meta or Facebook login, you can also remove Padharo from Facebook: go to <strong>Settings and privacy</strong>, then <strong>Settings</strong>, then <strong>Apps and websites</strong>, select Padharo Invites and tap <strong>Remove</strong>. Then send us a deletion request as above to delete the data we hold.</p>'''),
]
legal("/data-deletion/", "Data deletion | Padharo Invites", "Delete your data",
      "How to delete your Padharo Invites account and data, or remove your details from an event if you are a guest.", deletion)

# ---------------------------------------------------------------- CONTACT
contact = f'''<div class="wrap">
  <div class="page-head"><h1>Contact us</h1><p>Questions about Padharo Invites, the launch, or your data? We usually reply within a few hours on WhatsApp, and within 24 hours by email.</p></div>
  <div class="contact-grid">
    <div class="c-card"><span class="ic">{ic("message", 24)}</span><div><h3>WhatsApp</h3><p><a href="{CO["wa"]}" rel="noopener">{CO["phone"]}</a></p><small>Fastest way to reach us</small></div></div>
    <div class="c-card"><span class="ic">{ic("phone", 24)}</span><div><h3>Phone</h3><p><a href="tel:{CO["tel"]}">{CO["phone"]}</a></p><small>{CO["hours"]}</small></div></div>
    <div class="c-card"><span class="ic">{ic("mail", 24)}</span><div><h3>Email</h3><p><a href="mailto:{CO["email"]}">{CO["email"]}</a></p><small>Reply within 24 hours</small></div></div>
    <div class="c-card"><span class="ic">{ic("pin", 24)}</span><div><h3>Address</h3><p>{CO["entity"]}</p><small>{CO["address"]}</small></div></div>
  </div>
  <div class="prose" style="margin-top:24px">
    <h2>Business details</h2>
    <p>Padharo Invites is a product of <strong>{CO["entity"]}</strong>, based in {CO["city"]}.</p>
    <h2>Privacy and data requests</h2>
    <p>For privacy questions, complaints or deletion requests, write to <a href="mailto:{CO["email"]}">{CO["email"]}</a>. See our <a href="/privacy-policy/">Privacy Policy</a> and <a href="/data-deletion/">data deletion instructions</a>.</p>
    <h2>Got an invite you didn’t expect?</h2>
    <p>Reply “STOP” to the message and you won’t get any more for that event. You can also tell us the number it came to, and we will look into it.</p>
  </div>
</div>'''
page("/contact/", "Contact us | Padharo Invites",
     "Contact Padharo Invites by WhatsApp, phone or email. Padharo Invites is a product of KwikReach Solutions, Ahmedabad, Gujarat, India.",
     contact, current="/contact/")

# ---------------------------------------------------------------- 404
page("/404.html", "Page not found | Padharo Invites", "This page could not be found.",
     '''<div class="wrap"><div class="page-head" style="padding-bottom:120px"><h1>We couldn’t find that page</h1><p>The link may be old or mistyped.</p><div class="hero-actions"><a class="btn" href="/">Go to the home page</a><a class="btn btn-ghost" href="/contact/">Contact us</a></div></div></div>''')

# extras
open(os.path.join(OUT, "CNAME"), "w").write("padharoinvites.in\n")
open(os.path.join(OUT, ".nojekyll"), "w").write("")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
urls = ["/", "/privacy-policy/", "/terms/", "/data-deletion/", "/contact/"]
open(os.path.join(OUT, "sitemap.xml"), "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>2026-11-26</lastmod></url>\n" for u in urls) + "</urlset>\n")
print("built")
