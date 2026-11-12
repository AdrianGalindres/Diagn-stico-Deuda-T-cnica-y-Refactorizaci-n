# Registro de Riesgos Arquitectónicos

## Riesgo 1: Acoplamiento Extremo con Proveedor Externo (Supabase Auth/DB)
* **Descripción:** La lógica de negocio está dispersa y depende directamente de las APIs nativas de Supabase dentro de los controladores HTTP.
* **Impacto:** Alto. Si Supabase cambia su SDK o se migra a otro proveedor (ej. AWS RDS / Auth0), se rompe todo el backend.
* **Probabilidad:** Media.
* **Mitigación / Refactorización:** Implementar el patrón Repositorio y Arquitectura Limpia (*Clean Architecture*) para aislar las llamadas a la base de datos detrás de interfaces.

## Riesgo 2: Anti-patrón "God Controller" en NestJS
* **Descripción:** Controladores que manejan validaciones, conexiones directas a base de datos y respuestas HTTP al mismo tiempo.
* **Impacto:** Medio-Alto. Dificulta las pruebas unitarias y aumenta la complejidad ciclomática.
* **Mitigación:** Aplicar refactorización separando la capa de controladores, servicios y repositorios.
