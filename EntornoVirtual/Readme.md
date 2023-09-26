# ENTORNO VIRTUAL
Son pequeños espacios de trabajo aislados para poder gestionar 
>  PYENV: No es un entorno virtual, es un controlador o manejador de versiones de python.
> CONDA: 
> PIPENV: Creador de entornor vistuales desfasado (ya no se usa). 

para usar las herramientas se necesita un manejador de paquetes,comando que permite instalar distintos paquetes dentro del ordenador, o proyectos

- poetry
- virtualenv
- 
- venv: viene de manera predeterminada con el pauqte de python

1. para crear una maquina virtual
nos ubicamos en la carpeta que deseamos crear el entorno virtual
ingresamos con cd y la ruta del archivo 
ejemplo:

```bash
cd <ruta del archivo>
#EJEMPLO
cd nombre_carpeta/entorno_uno
```
2. creamos un entorno virtual con el siguiente comando:

```bash
python -m venv <nombre de nuestro entorno virtual>
#EJEMPLO
python -m venv mi_entorno
```
3. para activar el entorno virtual

```bash
source venv_uno/Scripts/activate
```
> ### OBSERVACION: 
> Para poder ejecutarlo en powershell como terminal determinado ejecutar el siguiente comando.
```powershell
venv_uno/Scripts/activate.ps1
```
# PARA INSTALAR PAQUETES EN NUESTRO ENTORNO VIRTUAL
1. Primero verifiquemos que no tengamos el paquete instalado y lo listamos con el siguiente comando.

debemos tener activado nuestro entorno virtual.
```bash
pip list
```
2. luego instalamos con el siguiente comando
```bash
pip install <nombre del paqute>
#ejemplo
pip install pandas
```