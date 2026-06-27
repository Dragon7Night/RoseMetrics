# 🌹 RoseMetrics | Optimizador de Precios de Suscripciones

RoseMetrics es una plataforma avanzada de análisis marginal diseñada para calcular la estabilidad financiera de modelos de suscripción, automatizando cálculos algebraicos complejos y optimización de tarifas mediante derivadas.

## Características principales
*  **Cálculo de usuarios estables:** Proyección de equilibrio de comunidad.
* **Optimización de precios:** Búsqueda del ingreso máximo mediante análisis marginal.
* **Análisis Bi-Mensual:** Comparativa reactiva de datos correlacionados.

---

## Pre-requisitos

### Gestión de Base de Datos
Se debe configurar una base de datos. De preferencia, se recomienda utilizar **XAMPP** con el motor **MySQL**. No obstante, el sistema es compatible con cualquier gestor relacional (por ejemplo, una instancia **Amazon RDS** en AWS).

* 🌐 [Descargar XAMPP de forma oficial](https://www.apachefriends.org/es/index.html)

### Librerías principales
El núcleo del proyecto utiliza las siguientes dependencias:
* `django` (Framework Web)
* `sympy` & `mpmath` (Cálculo analítico y simbólico de derivadas)
* `mysqlclient` & `pymysql` (Conectores de bases de datos)

> **Nota:** No es necesario instalarlas una por una; el proyecto cuenta con un archivo de requerimientos unificado.

---

## Pasos para la Instalación

1. **Ubicarse en la terminal** en la ruta de su preferencia.

   ```bash
   cd C:/
   mkdir ProyectosGit
   cd ProyectosGit
   ```

   - Sugerencia de codigo (opcional)

   ```bash
      cd C:/ ; mkdir ProyectosGit ; cd ProyectosGit
   ```
2. Clonación del repositorio.

   ```bash
      git clone https://github.com/Dragon7Night/RoseMetrics.git
   ```

3. Acceder a la carpeta del proyecto.

   ```bash
      cd RoseMetrics
   ```

   > **Nota:** Si no quieres crear un entorno virtual en el proyecto puedes saltarte al paso número 6 directamente. 

4. Crea entorno virtual. (Opcional)

   ```bash
      py -m venv .env
   ```

5. Activar entorno virtual (Opcional)

   ```bash
      .env\Scripts\activate
   ```

   > **Nota:** para desactivar el entorno virtual se usa el comando `deactivate`.

6. Instalación de requirements

   ```bash
      pip install -m requirements.txt
   ```

7. Verificar librerias instaladas (Opcional)

   ```bash
      pip list
   ```

8. Iniciar proyecto en Django

   ```bash
      py .\manage.py runserver
   ```

   o

   ```bash
      py -m django runserver
   ```


----------------------------


---

## 📝 3. Guía de Formatos en Markdown (Cómo estructurar tus datos)

Markdown (el lenguaje de los archivos `.md`) tiene muchas herramientas útiles además de los títulos (`###`) y las listas (`-`). Aquí tienes los elementos más poderosos que puedes usar para que tus textos se vean increíbles:

### A. Énfasis en el Texto (Estilos)
* **Negrita:** Coloca dos asteriscos `**texto**` para resaltar palabras clave. Resultado: **texto**.
* *Cursiva:* Coloca un asterisco `*texto*` o guion bajo `_texto_`. Resultado: *texto*.
* ~~Tachado:~~ Coloca dos virgulillas `~~texto~~`. Resultado: ~~texto~~.

### B. Bloques de Código e Inlines
* **Bloque completo (con lenguaje):** Se usan tres acentos graves (```). Si añades el nombre del lenguaje al lado (como ```bash o ```python), la plataforma pintará las palabras reservadas con colores (Syntax Highlighting).
* **Código en línea (Inline):** Si solo quieres resaltar un comando corto en medio de un párrafo, usa **un solo** acento grave (\`\). Por ejemplo, si escribes \`manage.py\`, se mostrará limpio como `manage.py`.

### C. Listas Avanzadas
* **Listas Ordenadas:** Simplemente escribe números seguidos de un punto (`1.`, `2.`). Markdown se encarga de alinearlos de forma perfecta automáticamente.
* **Sublistas (Anidadas):** Si das un salto de línea y presionas la tecla *Tabulación* o dejas 4 espacios antes del guion, creas un subpunto.
  ```markdown
  - Librerías matemáticas
    - SymPy
    - Mpmath