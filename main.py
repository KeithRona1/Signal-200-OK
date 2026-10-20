from pyscript import document

# --- 1. COIN CALCULATOR ---
calc_counter = 0

def calculate_wifi_time(event):
    global calc_counter
    input_elem = document.querySelector("#coins")
    result_elem = document.querySelector("#calc-result")
    
    try:
        val = input_elem.value.strip()
        if not val:
            result_elem.className = "result error"
            result_elem.innerHTML = "Please enter an amount in pesos."
            return
            
        pesos = float(val)
        if pesos <= 0:
            result_elem.className = "result error"
            result_elem.innerHTML = "Amount must be greater than zero."
            return
            
        # Pricing logic tiers
        if pesos >= 10:
            hours = (pesos / 10) * 3.5
        elif pesos >= 5:
            hours = (pesos / 5) * 1.0
        else:
            hours = pesos * 0.25 # 15 mins = 0.25 hours
            
        total_minutes = int(hours * 60)
        hrs = total_minutes // 60
        mins = total_minutes % 60
        
        time_str = f"{hrs} hour(s) and {mins} minute(s)" if hrs > 0 else f"{mins} minutes"
        calc_counter += 1
        
        result_elem.className = "result"
        result_elem.innerHTML = f"""
            <div class="big">₱{pesos:.0f} = {time_str}</div>
            <p style="margin-top:4px; font-size:0.9rem; color:var(--muted);">Enough time to check modules, submit assignments, and browse online! (Calculation #{calc_counter})</p>
        """
    except ValueError:
        result_elem.className = "result error"
        result_elem.innerHTML = "Please enter a valid number."

# Bind calculator button
calc_btn = document.querySelector("#calc-btn")
if calc_btn:
    calc_btn.onclick = calculate_wifi_time


# --- 2. DEAD ZONE VOTING SYSTEM ---
votes = {
    "Canteen": 8,
    "Classrooms": 10,
    "ComLabs": 3,
    "GBG Building": 5,
    "Library": 4
}

def render_vote_chart():
    total_votes = sum(votes.values())
    total_elem = document.querySelector("#vote-total")
    chart_elem = document.querySelector("#vote-chart")
    
    if total_elem:
        total_elem.innerText = f"Total community votes recorded: {total_votes}"
        
    if chart_elem:
        html_content = ""
        for zone, count in sorted(votes.items(), key=lambda x: x[1], reverse=True):
            pct = (count / total_votes * 100) if total_votes > 0 else 0
            html_content += f"""
                <div class="bar-row">
                    <div class="bar-label">
                        <span>{zone}</span>
                        <span>{count} votes ({pct:.1f}%)</span>
                    </div>
                    <div class="track">
                        <div class="fill" style="width: {pct}%;"></div>
                    </div>
                </div>
            """
        chart_elem.innerHTML = html_content

def handle_vote(zone_name):
    if zone_name in votes:
        votes[zone_name] += 1
        render_vote_chart()

# Bind voting buttons dynamically
vote_buttons = document.querySelectorAll(".vote-btn")
for btn in vote_buttons:
    zone = btn.getAttribute("data-zone")
    def make_handler(z):
        return lambda event: handle_vote(z)
    btn.onclick = make_handler(zone)

# Initial render of the chart on load
render_vote_chart()


# --- 3. THEATER MODE TOGGLE ---
def toggle_theater(event):
    ad_section = document.querySelector("#advertisement")
    body = document.body
    btn = document.querySelector("#theater-btn")
    
    if "theater" in ad_section.className:
        ad_section.className = "page"
        body.className = ""
        btn.innerText = "Theater mode"
        btn.setAttribute("aria-pressed", "false")
    else:
        ad_section.className = "page alt theater"
        body.className = "no-scroll"
        btn.innerText = "Exit theater"
        btn.setAttribute("aria-pressed", "true")

theater_btn = document.querySelector("#theater-btn")
if theater_btn:
    theater_btn.onclick = toggle_theater


# --- 4. CONTACT FORM SUBMISSION ---
def handle_contact(event):
    event.preventDefault()
    name_input = document.querySelector("#c-name").value.strip()
    form_result = document.querySelector("#form-result")
    
    if name_input:
        form_result.className = "msg-ok"
        form_result.innerHTML = f"<strong>Thank you, {name_input}!</strong> Your message has been sent to the Signal 200 OK team. We'll get back to you shortly."
        document.querySelector("#contact-form").reset()

contact_form = document.querySelector("#contact-form")
if contact_form:~
    contact_form.onsubmit = handle_contact