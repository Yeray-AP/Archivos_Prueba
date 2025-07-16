
import tkinter as tk


def ciudad_buscada():
    msg_ciudad = ciudad_entry.get()
    if msg_ciudad:
        weather_ciudad.config(text=f"La ciudad de la que quieres saber el clima es: {msg_ciudad}")
    else:
        weather_ciudad.config(text="Por favor, ingresa el nombre de una ciudad.")

windowApp = tk.Tk()

windowApp.title("Weather App")
windowApp.geometry("400x300")
windowApp.configure(bg="white")
windowApp.resizable(True,True)

ciudad = tk.Label(windowApp,bg="white", text="De que ciudad quieres saber el clima:",font=("Times New Roman", 14, "bold"), fg="black")
ciudad.pack(pady=(0, 10))

ciudad_entry = tk.Entry(windowApp,bg="white", relief="solid", bd=2)
ciudad_entry.pack(pady=(0, 20))

button_search = tk.Button(windowApp, text="Buscar Clima", font=("Times New Roman", 12), command=ciudad_buscada, highlightthickness=2, highlightbackground="gray", relief="solid", bd=2)
button_search.pack(pady=(0, 10))

weather_ciudad =tk.Label(windowApp, text="",bg="white", font=("Times New Roman", 11), fg="black")
weather_ciudad.pack()
windowApp.mainloop()
