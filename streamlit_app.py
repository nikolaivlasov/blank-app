import streamlit as st


st.title("Заявка")

adrt=st.query_params["first_key"]
st.header(adrt)
st.badge(adrt, color="blue")

if st.query_params["first_key"] == "1":
    st.title("нашел")


order_types_names=["корпоративная карта","мне на ИП/СЗ","по счету или договору др. юр.лица"]
order_type=st.radio("**Тип оплаты:**",order_types_names,index=None,help="нельзя в одной заявке использовать разные типы оплат",horizontal=True)
if order_type == "корпоративная карта":
    st.badge("пополнить карту", icon=":material/check:", color="green")
if order_type == "мне на ИП/СЗ":
    st.badge("дополнить приложение к вашему договору", icon=":material/check:", color="green")
if order_type == "по счету или договору др. юр.лица":
    st.badge("укажите название юр.лица в комментариях", icon=":material/check:", color="green")
else:
    st.markdown(
        ":orange-badge[⚠️ необходимо заполнить] "
    )
order_destination = st.text_area('Назначение',"",help="можно несколько")
if order_destination:
    st.badge("", icon=":material/check:", color="green")
else:
    st.markdown(
        ":orange-badge[⚠️ необходимо заполнить] "
    )




