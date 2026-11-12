# Evaluación de Deuda Técnica Arquitectónica

## 1. Identificación de Antipatrones Actuales
* **God Object:** Servicios en NestJS que sobrepasan las 500 líneas de código resolviendo múltiples responsabilidades (registro, envío de correos, transacciones financieras).
* **Duplicidad de Código:** Consultas repetitivas a Supabase dispersas por todo el backend sin centralización.

## 2. Plan de Gestión y Petición de Refactoring
* **Acción 1:** Reducir la complejidad ciclomática de las funciones críticas mediante el uso de validadores y tuberías (*Pipes* y *Guards* de NestJS).
* **Acción 2:** Ejecutar escaneos estáticos automáticos en el pipeline de CI/CD para evitar que se introduzca nuevo código con alta complejidad.
