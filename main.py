from pyscript import document

# --- 1. COIN CALCULATOR ---
calc_counter = 0

def calculate_wifi_time(event):
    global calc_counter
    input_elem = document.querySelector("#coins")
    result_elem = document.querySelector("#calc-result")
    
    if not input_elem or not result_elem:
        return
    
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
        
        if hrs > 0 and mins > 0:
            time_str = f"{hrs} hour(s) and {mins} minute(s)"
        elif hrs > 0:
            time_str = f"{hrs} hour(s)"
        else:
            time_str = f"{mins} minutes"
            
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


# --- 2. THEATER MODE TOGGLE ---
def toggle_theater(event):
    ad_section = document.querySelector("#advertisement")
    body = document.body
    btn = document.querySelector("#theater-btn")
    
    if not ad_section or not btn:
        return

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


# --- 3. CONTACT FORM SUBMISSION ---
def handle_contact(event):
    event.preventDefault()
    name_input_elem = document.querySelector("#c-name")
    form_result = document.querySelector("#form-result")
    
    if not name_input_elem or not form_result:
        return
        
    name_input = name_input_elem.value.strip()
    
    if name_input:
        form_result.className = "msg-ok"
        form_result.innerHTML = f"<strong>Thank you, {name_input}!</strong> Your message has been sent to the Signal 200 OK team. We'll get back to you shortly."
        contact_form_elem = document.querySelector("#contact-form")
        if contact_form_elem:
            contact_form_elem.reset()

contact_form = document.querySelector("#contact-form")
if contact_form:
    contact_form.onsubmit = handle_contact