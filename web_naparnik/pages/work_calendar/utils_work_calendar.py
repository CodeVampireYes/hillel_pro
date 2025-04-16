import datetime
import streamlit as st
from PIL import Image, ImageDraw, ImageFont


today = datetime.date.today()
month_now = today.month


st.markdown("""
    <style>
    input[value="23"] {
        background-color: #ffe6e6;
        color: black;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


class Help():
    def create_list_date(self):
        list_date = []
        start_date = datetime.date(2025, 1, 1)
        for date in range(366):
            list_date.append([str(start_date), start_date.weekday()])
            start_date += datetime.timedelta(1)
        return list_date

    def get_month_date(self, list_date, month_now: int) -> list:
        result = []
        month_now = str(month_now)
        if len(month_now) <= 1:
            month_now = f'0{month_now}'

        for date in list_date:
            if str(date[0][5:7]) == month_now:
                result.append(date)

        if result[0][1] == 6:
            for el in range(6):
                result.insert(0, [0, 0])
        elif result[0][1] == 5:
            for el in range(5):
                result.insert(0, [0, 0])
        elif result[0][1] == 4:
            for el in range(4):
                result.insert(0, [0, 0])
        elif result[0][1] == 3:
            for el in range(3):
                result.insert(0, [0, 0])
        elif result[0][1] == 2:
            for el in range(2):
                result.insert(0, [0, 0])
        elif result[0][1] == 1:
            for el in range(1):
                result.insert(0, [0, 0])
        len_list = len(result)
        count = 42 - len_list
        for el in range(count):
            result.append([0, 0])
        return result

    def get_day(self,my_list, num):
        if num == '0-0':
            if my_list[0][0] != 0:
                return my_list[0][0][8:10]
        if num == '0-1':
            if my_list[7][0] != 0:
                return my_list[7][0][8:10]
        if num == '0-2':
            if my_list[14][0] != 0:
                return my_list[14][0][8:10]
        if num == '0-3':
            if my_list[21][0] != 0:
                return my_list[21][0][8:10]
        if num == '0-4':
            if my_list[28][0] != 0:
                return my_list[28][0][8:10]
        if num == '0-5':
            if my_list[35][0] != 0:
                return my_list[35][0][8:10]

        if num == '1-0':
            if my_list[1][0] != 0:
                return my_list[1][0][8:10]
        if num == '1-1':
            if my_list[8][0] != 0:
                return my_list[8][0][8:10]
        if num == '1-2':
            if my_list[15][0] != 0:
                return my_list[15][0][8:10]
        if num == '1-3':
            if my_list[22][0] != 0:
                return my_list[22][0][8:10]
        if num == '1-4':
            if my_list[29][0] != 0:
                return my_list[29][0][8:10]
        if num == '1-5':
            if my_list[36][0] != 0:
                return my_list[36][0][8:10]

        if num == '2-0':
            if my_list[2][0] != 0:
                return my_list[2][0][8:10]
        if num == '2-1':
            if my_list[9][0] != 0:
                return my_list[9][0][8:10]
        if num == '2-2':
            if my_list[16][0] != 0:
                return my_list[16][0][8:10]
        if num == '2-3':
            if my_list[23][0] != 0:
                return my_list[23][0][8:10]
        if num == '2-4':
            if my_list[30][0] != 0:
                return my_list[30][0][8:10]
        if num == '2-5':
            if my_list[37][0] != 0:
                return my_list[37][0][8:10]

        if num == '3-0':
            if my_list[3][0] != 0:
                return my_list[3][0][8:10]
        if num == '3-1':
            if my_list[10][0] != 0:
                return my_list[10][0][8:10]
        if num == '3-2':
            if my_list[17][0] != 0:
                return my_list[17][0][8:10]
        if num == '3-3':
            if my_list[24][0] != 0:
                return my_list[24][0][8:10]
        if num == '3-4':
            if my_list[31][0] != 0:
                return my_list[31][0][8:10]
        if num == '3-5':
            if my_list[38][0] != 0:
                return my_list[38][0][8:10]

        if num == '4-0':
            if my_list[4][0] != 0:
                return my_list[4][0][8:10]
        if num == '4-1':
            if my_list[11][0] != 0:
                return my_list[11][0][8:10]
        if num == '4-2':
            if my_list[18][0] != 0:
                return my_list[18][0][8:10]
        if num == '4-3':
            if my_list[25][0] != 0:
                return my_list[25][0][8:10]
        if num == '4-4':
            if my_list[32][0] != 0:
                return my_list[32][0][8:10]
        if num == '4-5':
            if my_list[39][0] != 0:
                return my_list[39][0][8:10]

        if num == '5-0':
            if my_list[5][0] != 0:
                return my_list[5][0][8:10]
        if num == '5-1':
            if my_list[12][0] != 0:
                return my_list[12][0][8:10]
        if num == '5-2':
            if my_list[19][0] != 0:
                return my_list[19][0][8:10]
        if num == '5-3':
            if my_list[26][0] != 0:
                return my_list[26][0][8:10]
        if num == '5-4':
            if my_list[33][0] != 0:
                return my_list[33][0][8:10]
        if num == '5-5':
            if my_list[40][0] != 0:
                return my_list[40][0][8:10]

        if num == '6-0':
            if my_list[6][0] != 0:
                return my_list[6][0][8:10]
        if num == '6-1':
            if my_list[13][0] != 0:
                return my_list[13][0][8:10]
        if num == '6-2':
            if my_list[20][0] != 0:
                return my_list[20][0][8:10]
        if num == '6-3':
            if my_list[27][0] != 0:
                return my_list[27][0][8:10]
        if num == '6-4':
            if my_list[34][0] != 0:
                return my_list[34][0][8:10]
        if num == '6-5':
            if my_list[41][0] != 0:
                return my_list[41][0][8:10]

        if num == '7-0':
            if my_list[7][0] != 0:
                return my_list[7][0][8:10]
        if num == '7-1':
            if my_list[14][0] != 0:
                return my_list[14][0][8:10]
        if num == '7-2':
            if my_list[21][0] != 0:
                return my_list[21][0][8:10]
        if num == '7-3':
            if my_list[28][0] != 0:
                return my_list[28][0][8:10]
        if num == '7-4':
            if my_list[35][0] != 0:
                return my_list[35][0][8:10]
        if num == '7-5':
            if my_list[42][0] != 0:
                return my_list[42][0][8:10]


def block_ui_calendar():
    help_instance = Help()
    help_instance.create_list_date()
    list_month = help_instance.get_month_date(help_instance.create_list_date(), month_now)

    col = st.columns(2)
    with col[0]:
        coll = st.columns(7)
        with coll[0]:
            for el in range(6):
                st.text_input(label=' ', key=f'0-{el}', value=help_instance.get_day(
                    help_instance.get_month_date(help_instance.create_list_date(), month_now), f'0-{el}'))
        with coll[1]:
            for el in range(6):
                st.text_input(label=' ', key=f'1-{el}', value=help_instance.get_day(
                    help_instance.get_month_date(help_instance.create_list_date(), month_now),f'1-{el}'))
        with coll[2]:
            for el in range(6):
                st.text_input(label=' ', key=f'2-{el}', value=help_instance.get_day(
                    help_instance.get_month_date(help_instance.create_list_date(), month_now), f'2-{el}'))
        with coll[3]:
            for el in range(6):
                st.text_input(label=' ', key=f'3-{el}', value=help_instance.get_day(
                    help_instance.get_month_date(help_instance.create_list_date(), month_now), f'3-{el}'))
        with coll[4]:
            for el in range(6):
                st.text_input(label=' ', key=f'4-{el}', value=help_instance.get_day(
                    help_instance.get_month_date(help_instance.create_list_date(), month_now), f'4-{el}'))
        with coll[5]:
            for el in range(6):
                st.text_input(label=' ', key=f'5-{el}', value=help_instance.get_day(
                    help_instance.get_month_date(help_instance.create_list_date(), month_now), f'5-{el}'))
        with coll[6]:
            for el in range(6):
                st.text_input(label=' ', key=f'6-{el}', value=help_instance.get_day(
                    help_instance.get_month_date(help_instance.create_list_date(), month_now), f'6-{el}'))

    with col[1]:
        pass


def generate_png(year: int, month: int):
    width = 800
    height = 600
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)  # "Рисовалка" для img
    font = ImageFont.load_default(size=44)

    draw.text(xy=(width/2-64, 5), text=str(year), fill='black', font=font)



    # Сохраняем в PNG
    img.save(f"{year}_{month}.png")


generate_png(2025, 4)