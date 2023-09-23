## AVERIGUAR SOBRE ENTORNOS VIRTUALES EN PYTHON

## ¿Qué son los entornos virtuales?
**Entornos virtuales** son entornos aislados e independientes que contienen el código y las dependencias de un proyecto.

**Pero, ¿por qué utilizar entornos virtuales?**

Pues bien, los entornos virtuales permiten instalar y utilizar distintas versiones de las mismas bibliotecas para varios proyectos. El uso de entornos virtuales también garantiza que no se produzcan cambios de última hora cuando dos o más proyectos utilicen versiones diferentes. Vamos a entender esto con más detalle.

#### **Beneficios:**

- Puedes tener varios entornos, con varios conjuntos de paquetes, sin conflictos entre ellos. De esta manera, los requisitos de diferentes proyectos se pueden satisfacer al mismo tiempo.
- Puedes lanzar fácilmente tu proyecto con sus propios módulos dependientes.
  
## HERRAMIENTAS PARA CREAR ENTORNOS VIRTUALES:

![img](https://geekflare.com/wp-content/uploads/2022/11/Tools-to-Create-Virtual-Environments.png)

### 1. Virtualenv
Virtualenv es una de las herramientas más utilizadas para crear y gestionar entornos virtuales para proyectos Python. Un subconjunto de la funcionalidad de virtualenv está disponible en venv paquete. Sin embargo, el virtualenv es más rápido y extensible que venv.

### 2. Pipenv
Con pipnevdispone tanto de la funcionalidad de entorno virtual de virtualenv y gestión de paquetes de pip. Utiliza gestiona pipfiles para gestionar las dependencias del proyecto dentro de un entorno virtual utilizando.

Puede probar pipenv directamente desde el navegador en este Parque infantil Pipenv.

### 3. Conda
Si utiliza el Distribución Anaconda de Python para el desarrollo, puede utilizar conda para la gestión de paquetes y la creación de entornos virtuales.

Para saber más, consulte esta completa guía sobre gestión de entornos con conda.

### 4. Poesía
Poesía es una herramienta de gestión de paquetes que le permite gestionar las dependencias en todos los proyectos de Python. Para empezar a usar Poetry, necesitas tener Python 3.7 o una versión posterior instalada.

### 5. Venv
Como ya se ha dicho, venv ofrece un subconjunto de las funciones de virtualenv pero tiene la ventaja de que está integrado en la biblioteca estándar de Python, a partir de Python 3.3.

Está disponible con la instalación de Python y no requiere la instalación de paquetes externos. Lo usaremos en este tutorial para crear y trabajar con entornos virtuales. ✅
