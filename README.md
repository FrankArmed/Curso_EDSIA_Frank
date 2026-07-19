# Curso_EDSIA_Frank
Repositorio donde se encontrarán las actividades realizadas durante este curso EDSIA.
# Semana 1

**Autor:** Frank Asael Méndez García  
**Fecha:** 18/07/2026

## Descripción

Este repositorio contiene los ejercicios desarrollados durante el curso EDSIA.

La Semana 1 se enfoca en:

- Máquinas de estados finitos.
- Programación orientada a objetos.
- Principios SOLID aplicados a sensores.
- Pruebas automáticas con pytest.
- Diseño de un driver UART modernizado.
- Inyección de dependencias.
- Persistencia en formato JSON Lines.
- Extensiones con CAN y un buffer circular seguro para varios hilos.

## Estructura principal

```text
semana1/
── fsm_demo.py
── test_fsm.py
── solid_srp_ocp_lsp.py
── test_solid_srp_ocp_lsp.py
── solid_isp_dip.py
── test_solid_isp_dip.py
── uart_driver/
    ── config.py
    ── parsers.py
    ── device.py
    ── recorder.py
    ── buffer.py
    ── tests/
        ── test_config.py
        ── test_parsers.py
        ── test_device.py
        ── test_recorder.py
        ── test_buffer.py
