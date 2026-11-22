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
