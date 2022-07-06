# Script such_wow
Se asume que este script tiene que iterar sobre un intervalo de 10.000 valores enteros como máximo en un hardware domestico de actualidad.

###### Recibe: Desde la linea de comandos, separados por espacios, dos valores enteros como parametros.
* Los dos valores pueden ser enteros positivos o enteros negativos.
* El primer valor debe ser menor o igual al segundo valor.
###### Retorna: La impresion de una lista con ciertos valores remplazados por palabras clave:
* Si el numero es multiplo de 3 y de 5: Se remplaza por 'SuchWow'
* Si el numero es multiplo de 3: Se remplaza por 'Such'
* Si el numero es multiplo de 5: Se remplaza por 'Wow'

# Instalación
### 1) Requisitos de dependencias
1) Python 3.8.10 (puede funcionar con versiones anteriores pero no se asegura)
2) Virtualenv

### 2) Clonar proyecto
```sh
git clone https://github.com/giulianobrunero/such-wow.git
```

### 3) Crear y activar entorno virtual
1) Acceder al directorio donde se clonó el proyecto
    ```sh
    cd such-wow
    ```

2) Crear un nuevo entorno virtual
    ```sh
    ~.../such-wow$ virtualenv -p python3 env
    ```

2) Activar el entorno virtual
    ```sh
    ~.../such-wow$ source env/bin/activate
    ```

### 4) Correr scrip
**Prueba 1)**
```sh
(env)~.../such-wow$ python such_wow.py 1 10
```
Resultado:
```sh
[1, 2, 'Such', 4, 'Wow', 'Such', 7, 8, 'Such', 'Wow']
```
* Tiempo de ejecución: 9.179115295410156e-05 segundos
* Recursos de hardware: RAM 4GB, Intel Core i5-2450M 2th generation
#
**Prueba 2)**
```sh
(env)~.../such-wow$ python such_wow.py 10 16
```
Resultado:
```sh
['Wow', 11, 'Such', 13, 14, 'SuchWow', 16]
```
* Tiempo de ejecución: 8.249282836914062e-05 segundos
* Recursos de hardware: RAM 4GB, Intel Core i5-2450M 2th generation
#
**Prueba 3)**
```sh
(env)~.../such-wow$ python such_wow.py -10 10
```
Resultado:
```sh
['Wow', 'Such', -8, -7, 'Such', 'Wow', -4, 'Such', -2, -1, 'SuchWow', 1, 2, 'Such', 4, 'Wow', 'Such', 7, 8, 'Such', 'Wow']
```
* Tiempo de ejecución: 6.103515625e-05 segundos
* Recursos de hardware: RAM 4GB, Intel Core i5-2450M 2th generation
#
**Prueba 4)**
```sh
(env)~.../such-wow$ python such_wow.py -1000000 1000000
```
* Tiempo de ejecución: 2.8315999507904053
* Recursos de hardware: RAM 4GB, Intel Core i5-2450M 2th generation