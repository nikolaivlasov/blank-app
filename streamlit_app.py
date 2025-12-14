
import streamlit as st

images = [
    "3.jpg",
    "4.jpg",
    "5.jpg",
    "6.jpg"
]
avatar_master = 'Master.jpg'
photo_from_tg_player  = '2.jpg'
gift = 'gift.jpg'


# Проверяем, есть ли в session_state переменная для страницы
if 'page' not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

if st.session_state.page == 1:
    with st.container(border=True):
        # Display avatar
        st.image(avatar_master, caption="Мастер", width=200, clamp=True)
        st.markdown('Привет, Алена! Немного магии?')

    with st.container(border=True):
        st.image(photo_from_tg_player, width=200, clamp=True)
        if 'clicked' not in st.session_state:
            st.session_state.clicked = False


        def click_button():
            st.session_state.clicked = True


        st.button('Ну,конечно!', on_click=click_button)
        if st.session_state.clicked:
            next_page()
            # The message and nested widget will remain on the page

elif st.session_state.page == 2:
    with st.container(border=True):
        # Display avatar
        st.image(avatar_master, caption="Мастер", width=200)
        st.markdown('Так, так... мы посмотрели твои воспоминания из поездки. Какой образ твой?')

    with st.container(border=True):
        # Имена или пути к изображениям
        images = [
            "3.jpg",
            "4.jpg",
            "5.jpg",
            "6.jpg"
        ]

        # Инициализация выбранного изображения
        if "chosen_image" not in st.session_state:
            st.session_state["chosen_image"] = None

        # Создаем 2 ряда по 2 столбца
        cols = st.columns(2)
        cols += st.columns(2)

        for i, col in enumerate(cols):
            with col:
                st.image(images[i])
                if st.button(f" {i + 1}", key=f"button_{i}"):
                    st.session_state["chosen_image"] = i

        # После выбора
        if st.session_state["chosen_image"] is not None:
            index = st.session_state["chosen_image"]
            st.session_state["selected_image_path"] = images[index]
            next_page()

elif st.session_state.page == 3:
    with st.container(border=True):
        # Display avatar
        st.image(avatar_master, caption="Мастер", width=200)
        st.markdown('Ma chérie, ты великолепна!!!')
        st.markdown('А теперь первое задание..загляни внутрь себя:')
        st.markdown('Как думаешь, какой твой основной язык любви?')

    with st.container(border=True):
        st.image(st.session_state["selected_image_path"], width=200, clamp=True)

        buttons = ["Помощь", "Слова", "Подарки", "Время вместе", "Прикосновения"]

        # Верхний ряд - первые 3 кнопки
        cols1 = st.columns(3)
        for i in range(3):
            with cols1[i]:
                if st.button(buttons[i]):
                    st.write(f"Нажата {buttons[i]}")

        # Нижний ряд - оставшиеся 3 кнопки
        cols2 = st.columns(3)
        for i in range(3, 5):
            with cols2[i - 3]:
                if st.button(buttons[i]):
                    st.write(f"Нажата {buttons[i]}")

        if st.session_state.clicked:
            next_page()

elif st.session_state.page == 4:
    with st.container(border=True):
        st.image(avatar_master, caption="Мастер", width=200)
        st.markdown('Ma chérie, поздравляю ! Первый сундучок твой!!!')

    with st.container(border=True):
        st.image(gift, width=500)
        st.markdown("<style>.big-btn{ font-size:24px; padding:20px 40px;} </style>", unsafe_allow_html=True)

        # Центрируем через колонки
        if 'clicked' not in st.session_state:
            st.session_state.clicked = False


        def click_button():
            st.session_state.clicked = True
        cols = st.columns([1, 2, 1])  # 2 колонны для кнопки посередине
        with cols[1]:
            if st.button("Открыть", key="big_button", on_click=click_button):
                if st.session_state.clicked:
                    next_page()
elif st.session_state.page == 5:
    with st.container(border=True):
        st.image(avatar_master, caption="Мастер", width=200)
        st.markdown('Приятного просмотра!')

    with st.container(border=True):
        st.image("present_1.jpg", caption="Поход в кино", width=200)

    with st.container(border=True):
        st.image(st.session_state["selected_image_path"], width=200, clamp=True)
        if 'clicked' not in st.session_state:
            st.session_state.clicked = False


        def click_button():
            st.session_state.clicked = True


        st.button('А ужин?', on_click=click_button)
        if st.session_state.clicked:
            next_page()
elif st.session_state.page == 6:
    with st.container(border=True):
        st.image(avatar_master, caption="Мастер", width=200)
        st.markdown('Шазам! ... и ужин!')

    with st.container(border=True):
        st.image("about.jpg", width=400)
            # The message and nested widget will remain on the page











