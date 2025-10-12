import streamlit as st


if st.query_params["first_key"] == "1":
    st.title("нашел")
st.title("Заявка")

order_destination = st.text_area('Назначение',"")
if order_destination:
    st.badge("", icon=":material/check:", color="green")
else:
    st.markdown(
        ":orange-badge[⚠️ необходимо заполнить] "
    )

order_types_names=["корпоративная карта","мне на ИП/СЗ","счет от организации"]
order_type=st.radio("**Тип оплаты:**",order_types_names,index=None,help="в разработке",horizontal=True)
if order_type == "корпоративная карта":
    st.badge("пополнить карту", icon=":material/check:", color="green")
else:
    st.markdown(
        ":orange-badge[⚠️ необходимо заполнить] "
    )
