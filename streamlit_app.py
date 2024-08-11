import streamlit as st
import locale

st.title("An illustration of Kelly's Criterion")


# Definitions

EQUITY_BALANCE= "The total capital available for investment."
EXPECTED_RETURN= "The multiplier by which an investment's value might grow or shrink. "

def calculate(equity_balance,exp_return, prob_win, prob_loss, stoploss_percent):
    kelly_percent = (((exp_return * prob_win/100) - prob_loss/100)/exp_return)
    locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
    rounded_kelly_percent = round(kelly_percent, 2)
    print("Rounded Kelly Percent=" + str(rounded_kelly_percent))
    position_kelly = rounded_kelly_percent * equity_balance
    position_fractional_kelly =   position_kelly * .3333
   
    pos_risk=stoploss_percent * position_fractional_kelly/100 
    percent_risk_on_equity=(pos_risk/equity_balance)
    st.session_state["position_kelly"]=locale.currency(position_kelly)
    st.session_state["position_fractional_kelly"]= locale.currency(int(position_fractional_kelly)).split('.')[0]
    print("K=" +  st.session_state["position_kelly"])
    print("FK=" +  st.session_state["position_fractional_kelly"])
    print("Percent Risk on Equity=" + str(percent_risk_on_equity) )
    st.session_state["pos_risk"]= locale.currency(pos_risk).split('.')[0]
    st.session_state["percent_risk_on_equity"]="{:.2%}".format(percent_risk_on_equity)
    return

def reset():
    # Delete all the items in Session state
    for key in st.session_state.keys():
        del st.session_state[key]


# Initialize imputs values for equity balance, win probaility when coming in first time
# This give user's a loaded example of how this works
if not len(st.session_state.keys()):
    st.session_state["equity_balance"] = 20000
    st.session_state["exp_return"] = 4.04
    st.session_state["prob_win"] = 59
    st.session_state["prob_loss"] = 41
    st.session_state["stoploss_percent"] = 10
    calculate(st.session_state["equity_balance"],st.session_state["exp_return"], st.session_state["prob_win"], st.session_state["prob_loss"],st.session_state["stoploss_percent"])


equity_balance = st.number_input("Equity balance", key="equity_balance",min_value=1, help=EQUITY_BALANCE)

exp_return = st.number_input("Expected return", key="exp_return",help=EXPECTED_RETURN)

prob_win = st.number_input("Probability of winning", key="prob_win" , min_value=0, max_value=100)

prob_loss = st.number_input("Probability of losing", key="prob_loss" ,min_value=0, max_value=100)

stoploss_percent = st.number_input(
    "Stop loss percentage", key="stoploss_percent", min_value=0, max_value=100)



st.subheader("Results", divider="orange")

st.metric("Recommended position size", st.session_state["position_fractional_kelly"], delta=None,  help="None", )
st.metric("Position risk", st.session_state["pos_risk"], delta=None,  help="None", )
st.metric("Percent risk on equity", st.session_state["percent_risk_on_equity"], delta=None,  help="None", )




col1, col2 = st.columns(2)

with col1:
    st.button("Calculate",on_click=calculate, args=(equity_balance,exp_return, prob_win, prob_loss,stoploss_percent))
with col2:
    st.button("Reset",on_click=reset)


    




