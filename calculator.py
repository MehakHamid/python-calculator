import streamlit as st

# Initialize session state for history and number count
if "history" not in st.session_state:
    st.session_state.history = []
if "num_count" not in st.session_state:
    st.session_state.num_count = 2  # Default 2 numbers

# Dark Mode Toggle
dark_mode = st.checkbox("🌙 Dark Mode")

# Apply dark mode if enabled
if dark_mode:
    st.markdown(
        """
        <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stButton>button {
            background-color: #333;
            color: white;
        }
        .stSelectbox, .stNumber_input {
            background-color: #222;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# App Title
st.title("🧮 MH-Python Calculator")

# Buttons to Add/Remove Number Inputs
col1, col2 = st.columns(2)
with col1:
    if st.button("➕ Add Number"):
        st.session_state.num_count += 1
with col2:
    if st.button("➖ Remove Number") and st.session_state.num_count > 2:
        st.session_state.num_count -= 1

# User Input for Numbers
numbers = []
for i in range(st.session_state.num_count):
    num = st.number_input(f"Enter Number {i+1}", value=0.0, key=f"num_{i}")
    numbers.append(num)

# Dropdown for Operations
operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division", "Percentage"])

# Perform Calculation
result = None

if st.button("Calculate"):
    if operation == "Addition":
        result = sum(numbers)
    elif operation == "Subtraction":
        result = numbers[0] - sum(numbers[1:])  # First number minus the sum of others
    elif operation == "Multiplication":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "Division":
        result = numbers[0]
        try:
            for num in numbers[1:]:
                if num == 0:
                    raise ZeroDivisionError("Division by zero is not allowed!")
                result /= num
        except ZeroDivisionError as e:
            st.error(str(e))
            result = None
    elif operation == "Percentage":
        result = (numbers[0] / 100) * numbers[1]  # First number ka second number percent

    if result is not None:
        st.success(f"Result: {result}")
        st.session_state.history.append(f"{operation} {numbers} = {result}")

# Show Calculation History
st.subheader("📜 Calculation History")
if st.session_state.history:
    for item in reversed(st.session_state.history[-10:]):  # Show last 10 calculations
        st.write(item)
else:
    st.write("No history available.")

# Clear History Button
if st.button("Clear History"):
    st.session_state.history = []
    st.experimental_rerun()
