import streamlit as st
import locale

st.title("An illustration of Kelly's Criterion")



# Initialize imputs values for equity balance, win probaility when coming in first time
# This give user's a loaded example of how this works
if not len(st.session_state.keys()):
    st.session_state["equity_balance"] = 20000
    st.session_state["exp_return"] = 4.04
    st.session_state["prob_win"] = 59
    st.session_state["prob_loss"] = 41
    st.session_state["stoploss_percent"] = 10
   


equity_balance = st.number_input("Equity balance", key="equity_balance",min_value=1)

exp_return = st.number_input("Expected return", key="exp_return")

prob_win = st.number_input("Probability of winning", key="prob_win" , min_value=0, max_value=100)

prob_loss = st.number_input("Probability of losing", key="prob_loss" ,min_value=0, max_value=100)

stoploss_percent = st.number_input(
    "Stop loss percentage", key="stoploss_percent", min_value=0, max_value=100)


st.divider()

st.number_input("Recommended position size (Kelly)",key="position_kelly")

st.number_input("Recommended position size (Fractional Kelly)",key="position_fractional_kelly")

st.number_input("Expected risk on equity", key="pos_risk")

st.number_input("Expected risk on equity", key="percent_risk_on_equity")



def calculate():
    kelly_percent = (((exp_return * prob_win/100) - prob_loss/100)/exp_return)
    locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
    rounded_kelly_percent = round(kelly_percent, 2)
    print("Rounded Kelly Percent=" + str(rounded_kelly_percent))
    position_kelly = rounded_kelly_percent * equity_balance
    position_fractional_kelly =   position_kelly * .3333
    print("K=" + locale.currency(position_kelly))
    print("FK=" + locale.currency(round(position_fractional_kelly)))
    pos_risk=stoploss_percent * position_fractional_kelly/100 
    percent_risk_on_equity=(pos_risk/equity_balance) *100 
    st.session_state["position_fractional_kelly"]=position_fractional_kelly
    st.session_state["position_kelly"]=position_kelly
    st.session_state["pos_risk"]=pos_risk
    st.session_state["percent_risk_on_equity"]=percent_risk_on_equity
    return
    

st.metric("Recommended position size", st.session_state["position_fractional_kelly"], delta=None, delta_color="normal", help=None, label_visibility="visible")
st.button("Calculate",on_click=calculate)