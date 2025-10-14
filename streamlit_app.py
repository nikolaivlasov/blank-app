import streamlit as st





st.title("Заявка")
adrt = st.query_params["first_key"]
st.badge(adrt, color="blue")

if st.query_params["first_key"] == "1":
    st.title("нашел")
with st.container(border=True):
    order_types_names = ["корпоративная карта", "мне на ИП/СЗ", "счету или договору др. юр.лица"]
    order_type = st.radio("**Тип оплаты:**", order_types_names, index=None,
                          help="В одной заявке нельзя использовать разные типы оплат", horizontal=True)
    if order_type == "корпоративная карта":
        st.badge("пополнить карту", icon=":material/check:", color="green")
    elif order_type == "мне на ИП/СЗ":
        st.badge("доп. приложение договору", icon=":material/check:", color="green")
    elif order_type == "счету или договору др. юр.лица":
        st.badge("название юр.лица в комментариях", icon=":material/check:", color="green")
    else:
        st.markdown(
            ":orange-badge[⚠️ необходимо заполнить] "
        )

with st.container(border=True):

    order_destination = st.text_area('**Назначение:**',help="можно несколько")
    if order_destination:
        st.badge("", icon=":material/check:", color="green")
    else:
        st.markdown(
            ":orange-badge[⚠️ необходимо заполнить] "
        )


