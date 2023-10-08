import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
)


class CalculatorApp(UserControl):
    def build(self):
        self.reset()
        self.result = Text(value="0", color=colors.WHITE, size=50)


        return Container(
            width=300,
            height=450,
            bgcolor=colors.GREY,
            border_radius=border_radius.all(10),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.result], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="C",
                                bgcolor=colors.RED,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                height=40,
                                data="AC",
                            ),
                            ElevatedButton(
                                text="+/-",
                                bgcolor=colors.RED,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                height=40,
                                data="+/-",
                            ),
                            ElevatedButton(
                                text="%",
                                bgcolor=colors.RED,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                height=40,
                                data="%",
                            ),
                            ElevatedButton(
                                text="/",
                                bgcolor=colors.RED,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                height=40,
                                data="/",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="7",
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="8",
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="9",
                            ),
                            ElevatedButton(
                                text="*",
                                bgcolor=colors.RED,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="*",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="4",
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="5",
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="6",
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.RED,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="-",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="1",
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="2",
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="3",
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.RED,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="+",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=2,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="0",
                            ),
                            ElevatedButton(
                                text=".",
                                bgcolor=colors.ORANGE_50,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data=".",
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.BLUE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                width=100,
                                height=60,
                                data="=",
                            ),
                        ]
                    ),
                ],
            ),
        )

    def button_clicked(self, e):
        data = e.control.data
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif data in ("%"):
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)

            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )

        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):

        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: Page):
    page.title = "Calc App"


    calc = CalculatorApp()


    page.add(calc)


flet.app(target=main)