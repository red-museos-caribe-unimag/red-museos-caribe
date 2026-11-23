# Red de Museos del Caribe — Alternativa EE

**Universidad del Magdalena · Fundamentos de Programación**  
**Integrantes:** Leandro García, Diego Mejía y Jesús Jiménez.

## Descripción

Programa de consola en Python para administrar museos y sus registros de visitantes. Permite crear museos, registrar y simular días de asistencia, generar indicadores estadísticos, comparar museos y cargar archivos CSV.

## Organización del repositorio

- `business_logic.py`: clases `Museo` y `RedDeMuseos`, validaciones y cálculos.
- `user_interface.py`: menú de consola y manejo de entradas.
- `verificar_casos.py`: script de verificación automática.
- `casos_de_verificacion_incremento_1.md` a `casos_de_verificacion_incremento_5.md`: descripción de casos organizados por incremento.
- `resultados_verificacion.md`: registro conservado de una ejecución automatizada de 95 casos con resultado OK; el equipo debe contrastar los resultados con su propia ejecución.
- `datos/`: diez archivos CSV de entrada y prueba.
- `documentacion/`: documento de análisis, informe integral, informe de uso de IA y presentación de arquitectura.
- `evidencias_ia/`: tres archivos con enlaces compartidos a las conversaciones de los integrantes y el índice de evidencias.
- `video/ENLACE_VIDEO.md`: vínculo al video explicativo.
- `.github/ISSUE_TEMPLATE/tarea.md`: plantilla para registrar tareas en GitHub.
- `.gitignore`: exclusiones de archivos temporales y de configuración local.

## Ejecutar el programa

Se requiere Python 3. No se necesitan dependencias externas.

Desde la carpeta raíz del proyecto:

```bash
python user_interface.py
```

Para verificar los casos:

```bash
python verificar_casos.py
```

Para ejecutar un incremento específico, por ejemplo el primero:

```bash
python verificar_casos.py --incremento 1
```

Para probar la opción de carga CSV pueden usarse `datos/museos.csv` y `datos/visitantes.csv`.

## Documentación

- [Documento de análisis](documentacion/Documento_de_Analisis.pdf)
- [Informe integral del trabajo](documentacion/Informe_Integral.pdf)
- [Informe del uso de IA](documentacion/Informe_del_Uso_de_IA.pdf)
- [Presentación de arquitectura](documentacion/Presentacion_Arquitectura_del_Codigo.pptx) — material complementario.
- [Casos de verificación y resultados](resultados_verificacion.md)

## Video explicativo

[Ver video en YouTube](https://youtu.be/X3JT-Q_iUZs)

El equipo informó que el video dura **14:46**, muestra a los tres integrantes en cámara y puede reproducirse sin iniciar sesión.

## Evidencias de inteligencia artificial

Período general indicado por el equipo: **19 al 22 de noviembre de 2026**.

- [Leandro García — Claude](evidencias_ia/conversacion-01.md)
- [Diego Mejía — Claude](evidencias_ia/conversacion-02.md)
- [Jesús Jiménez — ChatGPT](evidencias_ia/conversacion-03.md)
- [Índice general de evidencias](evidencias_ia/indice-evidencias.md)

El equipo confirmó el acceso a los enlaces en modo incógnito sin iniciar sesión. Los enlaces son las fuentes de las conversaciones completas y deben permanecer accesibles durante la revisión académica.

## Organización y seguimiento

El trabajo está organizado mediante una organización de GitHub, un equipo de tres integrantes, cinco hitos (*milestones*), tareas (*issues*) y un tablero de *GitHub Projects*. Las asignaciones y estados se consultan en las secciones correspondientes del repositorio.

**Nota sobre la verificación:** el archivo `resultados_verificacion.md` documenta una ejecución conservada del verificador con la misma versión de código y datos de este paquete. Para corroborar ese resultado, ejecutar las pruebas en el equipo de los estudiantes.


## Trabajo colaborativo y contribuciones del equipo

El proyecto **Red de Museos del Caribe — Alternativa E** fue desarrollado colaborativamente por Leandro García, Diego Mejía y Jesús Jiménez, estudiantes de la Universidad del Magdalena.

### Leandro García

Participó en el desarrollo de la lógica del programa en `business_logic.py`, principalmente en:

- **Issue #1:** Creación y validación de museos.
- **Issue #2:** Registro y simulación de visitantes.
- **Issue #4:** Clasificación de niveles de asistencia, cálculo de rachas y días pendientes.
- **Revisión final:** Colaboró con Jesús Jiménez en la revisión del proyecto, comprobando los archivos, las funcionalidades y la preparación de la entrega.

### Diego Mejía

Participó en el desarrollo de las funcionalidades de análisis y comparación de museos, principalmente en:

- **Issue #3:** Cálculo de indicadores estadísticos y generación de informes.
- **Issue #5:** Búsqueda y comparación entre museos.
- **Evidencias de IA:** Colaboró con Jesús Jiménez en la organización de las conversaciones y evidencias del uso de inteligencia artificial generativa.

### Jesús Jiménez

Participó en la integración, organización y publicación del proyecto en GitHub, realizando las siguientes actividades:

- Creación de la organización y configuración del repositorio.
- Integración y publicación de los archivos desarrollados por el equipo.
- Creación de Issues y asignación de responsabilidades.
- Configuración y seguimiento de los cinco Milestones.
- Organización del tablero GitHub Projects.
- Organización de las evidencias de IA con la colaboración de Diego Mejía.
- Incorporación de los informes académicos y el enlace al video.
- Revisión final del proyecto con la colaboración de Leandro García.
- Preparación de la entrega final.

### Evidencia del trabajo colaborativo

Leandro García y Diego Mejía desarrollaron gran parte del código y compartieron sus archivos para integrarlos en el repositorio común.

Jesús Jiménez realizó la publicación inicial de los archivos en GitHub, por lo que los commits de carga aparecen asociados a su cuenta.

Las contribuciones individuales también están documentadas en los Issues del proyecto mediante asignaciones y comentarios realizados desde las cuentas de los integrantes.

Los cinco incrementos se encuentran organizados en GitHub Milestones y el seguimiento de las actividades está registrado en GitHub Projects.
