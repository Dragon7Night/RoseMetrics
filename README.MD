# 🌹 RoseMetrics | Optimizador de Precios de Suscripciones

RoseMetrics es una plataforma diseñada para calcular la estabilidad financiera de modelos de suscripción, automatizando cálculos algebraicos complejos y optimización de tarifas mediante derivadas.

## Características principales
*  **Cálculo de usuarios estables:** Proyección de equilibrio de comunidad.
* **Optimización de precios:** Búsqueda del ingreso máximo mediante análisis marginal.
* **Análisis Bi-Mensual:** Comparativa reactiva de datos correlacionados.

---

## Pre-requisitos

### Gestión de Base de Datos
Se debe configurar una base de datos. De preferencia, se recomienda utilizar **XAMPP** con el motor **MySQL**. No obstante, el sistema es compatible con cualquier gestor relacional (por ejemplo, una instancia **Amazon RDS** en AWS).

* 🌐 [Descargar XAMPP oficial](https://www.apachefriends.org/es/index.html)

### Librerías principales
El núcleo del proyecto utiliza las siguientes dependencias:
* `django` (Framework Web)
* `sympy` & `mpmath` (Cálculo analítico y simbólico de derivadas)
* `mysqlclient` & `pymysql` (Conectores de bases de datos)

> **Nota:** No es necesario instalarlas una por una; el proyecto cuenta con un archivo de requerimientos unificado.

---

## Pasos para la Instalación

1. **Ubicarse en la terminal en la ruta de su preferencia.**

   > **Sugerencia:** para crear los direcctorios (opcional).
   ```bash
   cd C:/
   mkdir ProyectosGit
   cd ProyectosGit
   ```

2. **Clonación del repositorio.**

   ```bash
   git clone https://github.com/Dragon7Night/RoseMetrics.git
   ```

3. **Acceder a la carpeta del proyecto.**

   ```bash
   cd RoseMetrics
   ```

   > **Nota:** Si no quieres crear un entorno virtual en el proyecto puedes saltarte al paso número 6 directamente. 

4. **Crea entorno virtual** (Opcional).

   ```bash
   py -m venv .env
   ```

5. **Activar entorno virtual** (Opcional).

   ```bash
   .env\Scripts\activate
   ```

   > **Nota:** para desactivar el entorno virtual se usa el comando `deactivate` en la terminal del proyecto.

6. **Instalación de requirements**

   ```bash
   pip install -m requirements.txt
   ```
   > **Sugerencia:** verificar librerias instaladas (Opcional).
   ```bash
   pip list
   ```

8. **Iniciar proyecto en Django**

   Opción 1
   ```bash
   py .\manage.py runserver
   ```
   Opción 2 
   ```bash
   py -m django runserver
   ```

