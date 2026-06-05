# Tarea3.0

## ejercicio:3.0.0

### Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación básica en Python denominada **ejercicio:3.0.0**, implementada como una calculadora simple capaz de realizar operaciones matemáticas básicas. El objetivo principal es aplicar conceptos de desarrollo de software, pruebas automatizadas, contenedorización mediante Docker e Integración Continua y Entrega Continua (CI/CD) utilizando GitHub Actions.

---

## Objetivos

* Desarrollar una aplicación funcional en Python.
* Implementar pruebas automatizadas utilizando Pytest.
* Automatizar la ejecución de pruebas mediante GitHub Actions.
* Construir una imagen Docker funcional de la aplicación.
* Publicar la imagen en GitHub Container Registry (GHCR).
* Aplicar buenas prácticas de Integración Continua y Entrega Continua.

---

## Tecnologías Utilizadas

* Python 3.12
* Pytest
* Docker
* GitHub Actions
* GitHub Container Registry (GHCR)
* Git y GitHub

---

## Estructura del Proyecto

```text
Tarea3.0/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
    └── workflows/
        └── python-application.yml
```

---

## Funcionalidades

La aplicación permite realizar operaciones matemáticas básicas mediante funciones desarrolladas en Python.

### Ejemplo de ejecución

```bash
python app.py
```

Salida esperada:

```text
Resultado suma: 15
```

---

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/Tarea3.0.git
cd Tarea3.0
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución de la Aplicación

```bash
python app.py
```

---

## Pruebas Automatizadas

El proyecto incluye pruebas automatizadas desarrolladas con Pytest para verificar el correcto funcionamiento de la aplicación.

### Ejecutar pruebas

```bash
pytest
```

Resultado esperado:

```text
==================== test session starts ====================
1 passed
==================== 100% ====================
```

---

## Docker

Docker permite empaquetar la aplicación junto con todas sus dependencias para ejecutarla en cualquier entorno de forma consistente.

### Construcción de la imagen

```bash
docker build -t ejercicio:3.0.0 .
```

### Verificar la imagen creada

```bash
docker images
```

### Ejecutar el contenedor

```bash
docker run ejercicio:3.0.0
```

Salida esperada:

```text
Resultado suma: 15
```

### Publicación en GitHub Container Registry

La imagen Docker se publica utilizando la siguiente nomenclatura:

```text
ghcr.io/TU_USUARIO/ejercicio:3.0.0
```

---

## Integración Continua y Entrega Continua (CI/CD)

Se implementó un flujo automatizado mediante GitHub Actions que ejecuta las siguientes tareas:

1. Descarga del código fuente.
2. Instalación de dependencias.
3. Ejecución de pruebas automatizadas.
4. Ejecución de la aplicación.
5. Simulación del despliegue.
6. Construcción de la imagen Docker.
7. Autenticación en GitHub Container Registry.
8. Publicación automática de la imagen Docker.

El workflow utilizado se encuentra en:

```text
.github/workflows/python-application.yml
```

---

## Evidencia de Funcionamiento

Para la entrega se incluye:

* URL del repositorio GitHub.
* Evidencia de ejecución exitosa de GitHub Actions.
* Evidencia de construcción de la imagen Docker.
* Archivo README.md con instrucciones de uso.

---

## Autor

**Marcos Alexander Villalva Cherrez**

Ingeniería en Tecnologías de la Información

---

## Fecha

Junio 2026
