import flet
from flet import page, Text, ButtonStyle, Column, FilledButton, Row, TextField, colors 
from flet.buttons import RoundedRectangleBorder
from flet.ref import Ref
from calculator import simple_interest
def main(page: page):
    page.title = "Simple Interest Calculator"
    page.padding = 50 
    principal = Ref[TextField]()
    rate = Ref[TextField]()
    time = Ref[TextField]()
    result = Ref[Column]()

    def get_interest(e):
        p = int(principal.current.value)
        r = float(rate.current.value)/100
        t = int(time.current.value)
        result.current.controls.append(Text(f"congratulations, your simple interest is $ {simple_interest(p,r,t)}", size= 20,weight= "w600", color= "blue"))
        principal.current.value = ""
        rate.current.value = ""
        time.current.value = ""
        page.update()
        result.current.controls.pop()

    page.add(
    Row(
        [
            Text("Welcome to my Simple Interest Calculator",size = 30, weight = "bold", color= "blue"),
        ],
    ),
    Column(
        [ 
            TextField(ref=principal, label="input pricipal:", width=700),
            TextField(ref=rate, label= "input rate:", width=700),
            TextField(ref=time, label= "input time in years:", width=700),
                FilledButton(
                    "Get amount",

style=ButtonStyle(shape=RoundedRectangleBorder(radius=5), padding=14),
                    on_click=get_interest,      
              
            ),
            Column(ref=result),
        ] 
    ),
)       


flet.app(target=main)
