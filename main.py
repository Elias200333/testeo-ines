import os
import tkinter as tk

# Emoji 🥲 en base64 (Twemoji 72x72) como respaldo offline y portable
EMOJI_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAMAAABiM0N1AAAAilBMVEVHcEz/zE3/zE3/zE3/zE3/zE3/zE3/"
    "zE3/zE3/zE3/zE3/zE3/zE3/zE1mRQBdrexwTQX1xEiku6bryGF5Vgpnr+LPojWziSfZqjr1yleGtcR7s87h"
    "xmu8kSupgCKMZxOWbxiDXg7XxHWaubCfeB2uvZ24vpNxsdi6pFjsu0NhgIXisz/GmTBfmsAuTkDOAAAADXRSTlMA"
    "36/PgFCPIJ/vQL9g4e8akwAAAiFJREFUeF69mNmSpSAMhvWoIEcDbmdfe5/1/V9vuiir6SaCYLrmu+Tir5AfCEni"
    "gdesSmEkrVjNkwUUZQqItCziVDgT4ECw8LjWK/CyWodFU8IsZUBUuYAARD4XTgaBZNxrlYBghMfAHKJwbq+ESEqS"
    "DlbCOhQlnB9ingpYiOUdF7AQ8fU8ZbCYjJggQ442Rtgcdp50BtZAZD0K4XdsO0g5bCF0fTVaj3WkZhu6DlwLMbBo"
    "G6lpWv+6gWkhZNlOjuz86wYxfTke5MiDc92mmPRefuBZxycg9Qj99K8bUuMZLSLgSf09QrU2n55sYEkFQLRfU+lc"
    "Ew6kyTZoSFdEo4Uol9YIEaAInTeb83cIHTZKbQ50ITiqd450oVeleaUJ6Y1ppjaXpBDOkxp5mjiQVYRj6oMzviIs"
    "LtMjR3xpawjlUX3iET0jfElAOCSOn9qmucwFhENKJwp/I+Vt77Zs2rhyohxd5DvP6HnvlUVvlSNcIJ91obhZhflF"
    "WbzYBTJhjgLZXD9rvSmLN1SykW+tVtLcrn/2mh/KgA8ld3xr2ru0+aUQnWng3B+tq7T4qxAn89HyNA/7QX5BTWC8"
    "931G210TKCT4TP/QXoYgoTzgw/77ch/mhLK4FuLkSrbgcU1N57K/iGyzeoXoHe1oGRlSt7CFPFhZOh2MDkEJ6UTl"
    "qbP2lS8eIPSdjurU9Z4BAn2kQR+y0Mc+9EHU/xuN0Yd19PHhP+9j3DbnmoOyAAAAAElFTkSuQmCC"
)

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Testeo Elías Inés y froilan")
    root.geometry("640x340")
    root.configure(bg="#f0f4f8")

    # Centrar la ventana en la pantalla
    root.update_idletasks()
    width = 640
    height = 340
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    # Cargar la imagen del emoji a color
    emoji_path = os.path.join(os.path.dirname(__file__), "assets", "emoji.png")
    if os.path.exists(emoji_path):
        emoji_img = tk.PhotoImage(file=emoji_path)
    else:
        emoji_img = tk.PhotoImage(data=EMOJI_BASE64)

    # Contenedor centrado
    frame = tk.Frame(root, bg="#f0f4f8")
    frame.pack(expand=True)

    # Etiqueta con el saludo y el emoji a todo color
    label = tk.Label(
        frame,
        text="¡Hola Elías e Inés!  ",
        image=emoji_img,
        compound="right",
        font=("Segoe UI", 32, "bold"),
        fg="#1e293b",
        bg="#f0f4f8"
    )
    label.image = emoji_img  # Mantener referencia para evitar garbage collection
    label.pack(pady=20)

    # Botón para cerrar
    btn_cerrar = tk.Button(
        frame,
        text="Cerrar",
        command=root.destroy,
        font=("Segoe UI", 12),
        bg="#3b82f6",
        fg="white",
        activebackground="#2563eb",
        activeforeground="white",
        relief="flat",
        padx=20,
        pady=8,
        cursor="hand2"
    )
    btn_cerrar.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
