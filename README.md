<img src="resources/imagenes/logo.svg" alt="Logo del sitio" width="42" height="42" align="left" style="margin-right: 12px;"/>

# Procesamiento y Visualización de Datos en R

Sitio web del curso **Procesamiento y Visualización de Datos en R**, del **Magíster en Métodos para la Investigación Social**.

**Docente:** Daniela Olivares Collío  
**Ayudante:** Katherine Aravena Herrera  
## Sitio web

**[udp-visualizacion-datos-r.netlify.app](https://udp-visualizacion-datos-r.netlify.app)**
---

## Descripción

Este repositorio contiene el sitio web del curso **Procesamiento y Visualización de Datos en R**.  
La página funciona como un espacio centralizado para organizar el programa, las clases, los materiales de apoyo, la bibliografía, los recursos para aprender R y las actualizaciones del curso.

El sitio fue desarrollado con **Quarto**, publicado mediante **Netlify** y versionado en **GitHub**.

---

## Contenidos del sitio

El sitio contiene:

- **Inicio:** presentación general del curso y guía rápida para navegar la página.
- **Curso:** programa, evaluaciones y calendarización integrada.
- **Clases:** páginas individuales por clase, con visor de diapositivas, descarga de materiales y espacio de comentarios.
- **Ayudantías:** materiales de apoyo y sesiones prácticas.
- **Bibliografía:** catálogo compacto de lecturas obligatorias, básicas, complementarias y sugeridas.
- **Recursos:** centro de apoyo con materiales para instalación, R, RStudio, Posit Cloud, Quarto, Tidyverse, visualización, bases de datos y errores frecuentes.
- **Última información:** avisos, noticias y actualizaciones del curso.

---

## Tecnologías utilizadas

- [Quarto](https://quarto.org/) — generación del sitio web estático.
- [Bootstrap 5](https://getbootstrap.com/) — componentes y estructura visual.
- [Netlify](https://www.netlify.com/) — publicación y despliegue continuo.
- [GitHub](https://github.com/) — control de versiones y alojamiento del repositorio.
- [Giscus](https://giscus.app/) — comentarios por clase mediante GitHub Discussions.
- HTML, CSS y JavaScript — ajustes visuales, filtros y componentes interactivos.

---

## Estructura del proyecto

```text
├── _quarto.yml                     # Configuración general del sitio
├── index.qmd                       # Página de inicio
├── curso.qmd                       # Programa, evaluaciones y calendarización
├── ayudantias.qmd                  # Página de ayudantías
├── bibliografia.qmd                # Catálogo bibliográfico del curso
├── Recursos.qmd                    # Centro de recursos para R, Quarto y datos
├── ultima-informacion.qmd          # Página general de avisos y noticias
├── styles.css                      # Estilos personalizados del sitio
│
├── clases/
│   ├── clase_00/
│   │   ├── index.qmd               # Página de la Clase 00
│   │   └── clase_00.pptx           # Diapositivas de la Clase 00
│   ├── clase_01/
│   │   ├── index.qmd               # Página de la Clase 01
│   │   └── clase_01.pptx           # Diapositivas de la Clase 01
│   └── clase_02/
│       ├── index.qmd               # Página de la Clase 02
│       └── clase_02.pptx           # Diapositivas de la Clase 02
│
├── includes/
│   ├── menu-clases.qmd             # Menú lateral compartido entre clases
│   └── comentarios-giscus.qmd      # Bloque de comentarios por clase
│
├── ultima-informacion/
│   └── *.qmd                       # Publicaciones, avisos y noticias del curso
│
├── resources/
│   ├── imagenes/                   # Logos, favicon e imágenes generales
│   ├── post/                       # Imágenes destacadas para noticias
│   ├── biblio/                     # PDFs de bibliografía
│   └── clases/                     # Materiales generales de clases, si corresponde
│
└── docs/                           # Sitio compilado para publicación en Netlify
```

## Licencias | Tipo | Licencia | |------|----------| | **Contenido** (textos, presentaciones) | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | | **Código** (HTML, CSS, configuración) | [MIT](https://opensource.org/licenses/MIT) | ---
