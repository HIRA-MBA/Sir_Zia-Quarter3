
import streamlit as st

# unit-convertor app
# required input 1:unit from , 2: unit to and 3:value to change


st.title("unit-convertor")


category = st.selectbox("Select conversion type", ["length", "weight"])


if category == "length":
    units = ["km", "meter", "cm"]
elif category == "weight":
    units = ["kg", "gram", "pounds"]
else:
    units = []

# Step 3: Choose from/to units and enter value
unit_from = st.selectbox("Convert from", units)
unit_to = st.selectbox("Convert to", units)
value = st.number_input("Enter value to convert", min_value=0.0)

def convert_unit(value:float,unit_from:str,unit_to:str,category:str):
    match category:

    # 1 km= 1000m 
    # 1 m ={ 0.001 km , 100 cm , 1000 mm}

    # 1 kg = 1000gm = 2.2 lbs
    # 1 g = 0.001 kg
        case "length":
            if unit_from == "km" and unit_to == "meter":
                return value * 1000
            elif unit_from=="km" and unit_to =="cm":
                return value * 100000
            elif unit_from =="meter" and unit_to=="km":
                return value/0.001
            elif unit_from =="cm" and unit_to== "meter":
                return value/0.01
            else:
                return "conversion is not supported"
        case "weight":
            if unit_from == "kg" and unit_to == "gram":
                return value * 1000
            elif unit_from=="kg" and unit_to =="pounds":
                return value * 2.2            
            else:
                return "conversion is not supported"
        case _:
            return "conversion not supported"


if st.button("Convert"):
    if unit_from == unit_to:
        st.info("Both units are the same — no conversion needed.")
    else:
        result = convert_unit(value, unit_from, unit_to, category)
        st.success(f"Result: {result} {unit_to}")




