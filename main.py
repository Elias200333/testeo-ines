import tkinter as tk

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Testeo Inés")
    root.geometry("500x300")
    root.configure(bg="#f0f4f8")

    # Centrar la ventana en la pantalla
    root.update_idletasks()
    width = 500
    height = 300
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    # Contenedor centrado
    frame = tk.Frame(root, bg="#f0f4f8")
    frame.pack(expand=True)

    # Etiqueta con el saludo en grande
    label = tk.Label(
        frame,
        text="¡Hola Inés!",
        font=("Segoe UI", 36, "bold"),
        fg="#1e293b",
        bg="#f0f4f8"
    )
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

