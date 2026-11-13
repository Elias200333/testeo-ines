# 🚀 Guía Práctica de Git y GitHub

¡Bienvenida al mundo de Git y GitHub! Esta guía está diseñada para que entiendas de forma clara y directa cómo funciona el control de versiones y cómo colaborar en proyectos reales como **testeo-ines**.

---

## 1. 🧠 Git vs GitHub: ¿Cuál es la diferencia?

A menudo se confunden, pero son dos cosas distintas que trabajan juntas:

* **Git**: Es un software de control de versiones que se ejecuta **en tu ordenador (en local)**. Guarda un historial fotográfico de todos los cambios de tus archivos, permitiéndote volver atrás si algo se rompe y trabajar en ramas paralelas.
* **GitHub**: Es una **plataforma en la nube** (un sitio web) propiedad de Microsoft que aloja repositorios de Git. Sirve para compartir código con el mundo, colaborar en equipo, revisar cambios (Pull Requests) y respaldar tu trabajo.

---

## 2. 🗺️ El Mapa Mental: Las 4 Áreas de Git

Cuando trabajas en Git, tus archivos pasan por cuatro estados principales:

```
+-------------------+      git add      +-------------------+
|  Área de Trabajo  |  -------------->  |   Staging Area    |
| (Tus archivos en  |                   |   (Preparados     |
|   el editor)      |                   |   para foto)      |
+-------------------+                   +-------------------+
                                                  |
                                                  | git commit
                                                  v
+-------------------+      git push     +-------------------+
|     GitHub        |  <--------------  | Repositorio Local |
|   (En la nube)    |                   |   (Historial en   |
+-------------------+                   |    tu PC .git)    |
         |                              +-------------------+
         |             git pull                   ^
         +----------------------------------------+
```

1. **Working Directory (Directorio de trabajo):** Es la carpeta donde editas tus archivos (`main.py`, etc.).
2. **Staging Area (Área de preparación):** Como una bandeja donde colocas los archivos que quieres incluir en la siguiente "foto" (`git add`).
3. **Local Repository (Historial local):** El registro permanente de cambios en tu máquina (`git commit`).
4. **Remote Repository (GitHub):** El repositorio en internet donde tu equipo y tú compartís el código (`git push` y `git pull`).

---

## 3. 🛠️ Flujo de Trabajo Práctico (Paso a Paso)

Este es el ciclo que usarás el 95% de las veces cuando trabajes:

### Paso 1: Sincronizar con lo último (`git pull`)
Antes de tocar nada, asegúrate de tener los últimos cambios que haya subido tu compañero:
```bash
git pull origin main
```

### Paso 2: Crear una rama para tu trabajo (`git checkout -b`)
En proyectos profesionales **no se trabaja directamente sobre la rama `main`**. Se crea una rama propia para cada función o arreglo:
```bash
git checkout -b feature/mi-primera-contribucion
```
> **¿Por qué ramas?** Porque aíslan tus cambios. Si algo sale mal, la rama principal `main` sigue intacta y funcionando.

### Paso 3: Hacer tus cambios en el código
Modifica archivos, crea nuevos scripts o edita los existentes en tu editor favorito.

### Paso 4: Revisar qué has cambiado (`git status` y `git diff`)
Para ver qué archivos se han modificado:
```bash
git status
```
Para ver línea por línea qué cambiaste:
```bash
git diff
```

### Paso 5: Preparar los archivos para el commit (`git add`)
Añade los archivos que quieres guardar:
```bash
# Añadir un archivo concreto:
git add README.md

# O añadir todos los archivos modificados:
git add .
```

### Paso 6: Guardar la "foto" con un mensaje descriptivo (`git commit`)
El commit guarda tus cambios con un mensaje que explica el motivo:
```bash
git commit -m "feat: añadir documentación inicial y README"
```

### Paso 7: Publicar tu rama en GitHub (`git push`)
Envía tu rama local al repositorio remoto en GitHub:
```bash
git push -u origin feature/mi-primera-contribucion
```
*(La primera vez que lo hagas, Windows o tu navegador te pedirá iniciar sesión en GitHub para identificarte).*

### Paso 8: Abrir un Pull Request (PR) en GitHub
1. Entra en el repositorio en la web de GitHub: [https://github.com/Elias200333/testeo-ines](https://github.com/Elias200333/testeo-ines).
2. Verás un botón amarillo que dice **"Compare & pull request"**.
3. Haz clic, describe los cambios que hiciste y pulsa **"Create pull request"**.
4. Tu compañero Elías podrá revisar tu código, dejar comentarios y fusionarlo (**Merge**) en la rama `main`.

---

## 4. 👥 ¿Cómo colaborar con tu compañero? (Permisos)

Hay dos formas estándar de colaborar en GitHub:

### Escenario A: Eres colaboradora oficial (Recomendado entre compañeros)
* **Qué hace falta:** Elías debe entrar en su repositorio en GitHub -> **Settings** -> **Collaborators** -> **Add people** y escribir tu usuario de GitHub (`inessantanaagustin-lgtm`).
* **Qué puedes hacer:** Tienes permiso de escritura. Puedes subir ramas directamente con `git push origin <tu-rama>`.

### Escenario B: Contribución abierta / Fork (Si aún no te ha invitado)
* Si intentas hacer `git push` y GitHub te da un error `403 Permission Denied`, significa que no tienes permisos de escritura en su repo.
* **Solución:**
  1. Vas a [https://github.com/Elias200333/testeo-ines](https://github.com/Elias200333/testeo-ines).
  2. Arriba a la derecha haces clic en el botón **Fork**. Esto crea una copia exacta en tu propia cuenta (`inessantanaagustin-lgtm/testeo-ines`).
  3. Subes tus cambios a tu propio fork y luego pulsas **New Pull Request** para enviárselos a Elías.

---

## 5. ⚡ Chuleta Rápida de Comandos (Cheat Sheet)

| Comando | ¿Qué hace? |
| :--- | :--- |
| `git status` | Muestra el estado actual (archivos modificados, rama activa). |
| `git pull origin main` | Descarga e integra los cambios más recientes de GitHub en tu PC. |
| `git branch` | Lista las ramas existentes y te marca en cuál estás. |
| `git checkout -b <nombre>` | Crea una nueva rama y se cambia a ella. |
| `git checkout <nombre>` | Cambia a una rama que ya existe. |
| `git add <archivo>` | Pasa el archivo al área de preparación (staging). |
| `git commit -m "mensaje"` | Guarda permanentemente los cambios preparados con una nota. |
| `git push -u origin <rama>` | Sube la rama y sus commits a GitHub. |
| `git log --oneline` | Muestra el historial resumido de commits. |
| `git restore <archivo>` | Descarta los cambios no guardados de un archivo (vuelve al último commit). |

---

## 6. 💡 Buenas Prácticas para Principiantes

1. **Haz `git pull` antes de empezar a programar cada día**: Evita conflictos antes de que ocurran.
2. **Commits pequeños y frecuentes**: Es mucho mejor hacer 5 commits con propósitos claros ("añadir botón", "arreglar color de fondo") que un commit gigante con 200 cambios ("arreglos varios").
3. **Escribe mensajes de commit claros**: Explica qué hiciste y por qué.
4. **Nunca compartas contraseñas ni claves API**: Usa archivos `.gitignore` para no subir archivos sensibles o temporales.
