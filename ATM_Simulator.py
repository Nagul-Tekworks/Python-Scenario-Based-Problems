import streamlit as st

# Predefined user data
users = {
    "user1": {"pin": "1234", "balance": 10000},
    "user2": {"pin": "4321", "balance": 5000}
}

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None
if "attempts" not in st.session_state:
    st.session_state.attempts = 3

st.title("🏦 Python ATM Simulator")

# Login block
if not st.session_state.logged_in:
    username = st.text_input("Enter Username")
    pin = st.text_input("Enter 4-digit PIN", type="password")

    if st.button("Login"):
        if username in users and pin == users[username]["pin"]:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("✅ Login Successful!")
        else:
            st.session_state.attempts -= 1
            if st.session_state.attempts > 0:
                st.error(f"❌ Incorrect username or PIN. Attempts left: {st.session_state.attempts}")
            else:
                st.error("🚫 Card Blocked. Please contact the bank.")
else:
    username = st.session_state.username
    st.subheader(f"Welcome, {username} 👋")
    option = st.radio("Select an Option", ["Check Balance", "Deposit Money", "Withdraw Money", "Logout"])

    if option == "Check Balance":
        st.info(f"💰 Your current balance is: ₹{users[username]['balance']}")

    elif option == "Deposit Money":
        amount = st.number_input("Enter amount to deposit (₹)", min_value=1.0, step=100.0)
        if st.button("Deposit"):
            if amount > 50000:
                st.warning("⚠️ Deposit limit exceeded. Max ₹50,000 allowed.")
            else:
                users[username]["balance"] += amount
                st.success(f"✅ ₹{amount} deposited successfully.")
                st.info(f"New Balance: ₹{users[username]['balance']}")

    elif option == "Withdraw Money":
        amount = st.number_input("Enter amount to withdraw (₹)", min_value=100.0, step=100.0)
        if st.button("Withdraw"):
            balance = users[username]["balance"]
            if amount % 100 != 0:
                st.warning("⚠️ Withdrawal amount must be multiples of 100.")
            elif amount > 20000:
                st.warning("⚠️ Withdrawal limit exceeded. Max ₹20,000 per transaction.")
            elif amount > balance - 1000:
                st.warning("⚠️ Insufficient funds or minimum balance requirement not met.")
            else:
                users[username]["balance"] -= amount
                st.success(f"✅ ₹{amount} withdrawn successfully.")
                st.info(f"New Balance: ₹{users[username]['balance']}")

    elif option == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.attempts = 3
        st.info("🔒 You have logged out.")
