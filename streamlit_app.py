import streamlit as st
import locale

st.title("An illustration of Kelly's Criterion")

# Delete all the items in Session state
for key in st.session_state.keys():
    #print( st.session_state[key])
    del st.session_state[key]

# Initialize imputs values for equity balance, win probaility when coming in first time
# This give user's a loaded example of how this works
if not len(st.session_state.keys()):
    st.session_state["equity_balance"] = 20000
    st.session_state["exp_return"] = 4.04
    st.session_state["prob_win"] = 59
    st.session_state["prob_loss"] = 41
    st.session_state["stoploss_percent"]=10



equity_balance=st.number_input("Equity balance", key="equity_balance")

exp_return=st.number_input("Expected return", key="exp_return")

prob_win=st.number_input("Probability of winning", key="prob_win")

prob_loss=st.number_input("Probability of losing", key="prob_loss")

stoploss_percent=st.number_input("Stop loss percentage",key="stoploss_percent")


st.divider()

st.number_input("Recommended position size (Kelly)")

st.number_input("Recommended position size (Fractional Kelly)")

st.number_input("Expected risk on equity")


def calculate():
    kelly_percent= (((exp_return * prob_win/100)- prob_loss/100)/exp_return) 
    
    #locale.setlocale( locale.LC_ALL, 'en_.UTF-8' )
    rounded_kelly_percent=round(kelly_percent,2)
    print("Rounded Kelly Percent=" + str(rounded_kelly_percent) )
    position_kelly= rounded_kelly_percent * equity_balance
    position_fractional_kelly= rounded_kelly_percent * 0.33 * equity_balance
    print("K="+ locale.currency(position_kelly))
    print("FK="+ locale.currency(position_fractional_kelly))
    return position_kelly

calculate()