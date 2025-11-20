# 🌍 Generador de Configuración ERA5 - Copernicus CDS

Aplicación web para generar automáticamente archivos de configuración `CONFIG.conf` para el Copernicus Climate Data Store API, con una interfaz gráfica intuitiva similar a la interfaz oficial de descarga de ERA5.

![Fondo espacial de la Tierra](https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=100&w=1200)

## 📋 Características

- ✅ **Interfaz tipo Copernicus** - Diseño moderno con fondo espacial de la Tierra
- ✅ **Selección de datasets** - ERA5 Single Levels, Pressure Levels, Land y versiones mensuales
- ✅ **275+ variables de Single Levels** - Todas las variables disponibles en ERA5
- ✅ **16 variables de Pressure Levels** - Con selector de 37 niveles de presión (1-1000 hPa)
- ✅ **Selector visual de presión** - Checkboxes para elegir niveles específicos
- ✅ **Gestión de múltiples usuarios** - Añade todas las API keys que necesites
- ✅ **Vista previa en tiempo real** - Ve el archivo CONFIG.conf antes de descargarlo
- ✅ **Carga configuraciones existentes** - Edita archivos CONFIG.conf previos
- ✅ **Validación automática** - Verifica datos antes de generar
- ✅ **Diseño responsive** - Funciona en desktop, tablet y móvil
- ✅ **100% cliente** - Sin servidor, todo funciona en el navegador

## 🚀 Uso

### Abrir la Aplicación

1. Abre el archivo `index.html` en tu navegador web
2. La aplicación cargará con una configuración por defecto

### Configurar API

1. **URL del API**: Modifica si es necesario (por defecto: `https://cds.climate.copernicus.eu/api`)
2. **Claves API**: 
   - Agrega usuarios con el botón "➕ Añadir Usuario"
   - Introduce las claves API en formato UUID
   - Elimina usuarios innecesarios con "✕ Eliminar"

### Configurar Datasets

1. Agrega datasets con "➕ Añadir Dataset"
2. Selecciona el tipo de dataset ERA5:
   - ERA5 Single Levels
   - ERA5 Pressure Levels
   - ERA5 Land
   - ERA5 Monthly (single/pressure levels)

### Configurar Variables

1. Agrega variables con "➕ Añadir Variable"
2. **Selecciona el dataset primero** (Single Levels, Pressure Levels o Land)
3. **Elige la variable** del menú desplegable:
   - **Single Levels**: 275+ variables (temperatura, precipitación, viento, radiación, nubes, océano, etc.)
   - **Pressure Levels**: 16 variables (temperatura, viento, humedad, geopotencial, etc.)
   - **Land**: 16 variables específicas de superficie terrestre
4. **Para Pressure Levels**: Selecciona niveles de presión con checkboxes
   - 37 niveles disponibles: 1, 2, 3, 5, 7, 10, 20, 30, 50... hasta 1000 hPa
   - Botones "Todos/Ninguno" para selección rápida
5. Completa los campos adicionales:
   - **ID del Dataset**: Número del dataset en la configuración (1, 2, 3...)
   - **Año Inicial/Final**: Rango temporal de descarga (1940-2024)
   - **Región**: Coordenadas Norte Oeste Sur Este (ej: `90 -180 -90 180` para global)

### Generar Archivo

1. Haz clic en "🔄 Actualizar Vista Previa" para ver el resultado
2. Revisa el contenido en la sección de vista previa
3. Haz clic en "💾 Descargar CONFIG.conf"
4. El archivo se descargará automáticamente

### Otras Funciones

- **📂 Cargar Configuración Existente**: Carga un archivo CONFIG.conf previo
- **🔄 Resetear Formulario**: Vuelve a la configuración por defecto

## 📁 Estructura de Archivos

```
WEB/
├── index.html      # Estructura HTML de la aplicación
├── styles.css      # Estilos CSS con diseño moderno
├── script.js       # Lógica JavaScript para funcionalidad
├── CONFIG.conf     # Archivo de configuración (ejemplo)
└── README.md       # Este archivo
```

## 🔧 Formato del Archivo CONFIG.conf

El archivo generado sigue esta estructura:

```conf
CDSAPI_URL=https://cds.climate.copernicus.eu/api

CDSAPI_KEY_1=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
CDSAPI_KEY_2=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

DATASET_1=reanalysis-era5-single-levels
DATASET_2=reanalysis-era5-pressure-levels

VARIABLE_1=2m_temperature,0,1,1940,2024,90 -180 -90 180
VARIABLE_2=u_component_of_wind,20 50 100,2,1950,2024,90 -180 -90 180
```

### Formato de Variables

```
VARIABLE_N=nombre_variable,niveles_presión,periodicidad,año_inicio,año_fin,región
```

- **nombre_variable**: Nombre según Copernicus CDS
- **niveles_presión**: `0` para single level, o lista separada por espacios
- **periodicidad**: ID del dataset (DATASET_1 = 1, DATASET_2 = 2, etc.)
- **año_inicio/fin**: Rango temporal
- **región**: Norte Oeste Sur Este (ej: `90 -180 -90 180`)

## 🌐 Variables Disponibles

### ERA5 Single Levels (275+ variables)
Incluye variables de:
- **Atmósfera**: Temperatura 2m, presión, precipitación, nubosidad
- **Viento**: Componentes U/V a 10m y 100m, ráfagas
- **Radiación**: Solar, térmica, UV (directa, difusa, neta)
- **Océano**: Temperatura superficial, oleaje, corrientes
- **Lagos**: Temperatura, profundidad, cobertura de hielo
- **Suelo**: Temperatura (4 niveles), humedad volumétrica
- **Vegetación**: Índice de área foliar, tipo, cobertura
- **Nieve/Hielo**: Profundidad, densidad, albedo, derretimiento
- **Energía**: Flujos de calor latente y sensible
- **Indices**: K-index, Total Totals, Benjamin-Feir

### ERA5 Pressure Levels (16 variables)
- Divergencia, Fracción de cobertura nubosa
- Geopotencial, Ozono, Vorticidad potencial
- Humedad relativa y específica
- Contenido de agua (hielo, líquida, lluvia, nieve)
- Temperatura, Componentes U/V del viento
- Velocidad vertical, Vorticidad

### ERA5 Land (16 variables)
Variables específicas de superficie terrestre optimizadas para estudios continentales

### Niveles de Presión Disponibles
1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000 hPa

## 🎨 Características de Diseño

- **Fondo espacial** - Imagen de la Tierra desde el espacio con zoom
- **Paleta de colores** inspirada en Copernicus CDS
- **Animaciones suaves** para mejor experiencia de usuario
- **Diseño responsive** que se adapta a móviles y tablets
- **Vista previa estilo código** con scroll y sintaxis destacada
- **Selector de presión visual** con checkboxes organizados en grid
- **Validación visual** de campos del formulario
- **Interfaz moderna** con degradados y sombras sutiles

## 🔧 Tecnologías

- **HTML5** - Estructura semántica moderna
- **CSS3** - Diseño responsive con Grid y Flexbox
- **JavaScript ES6+** - Lógica del lado del cliente
- **Sin dependencias** - No requiere frameworks ni librerías externas
- **Compatible con todos los navegadores** modernos

## ⚠️ Notas de Seguridad

- Las claves API son sensibles: no las compartas públicamente
- El archivo CONFIG.conf debe mantenerse seguro
- No subas el archivo con tus claves a repositorios públicos

## 🔗 Enlaces Útiles

- [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/)
- [ERA5 Documentation](https://confluence.ecmwf.int/display/CKB/ERA5)
- [CDS API Documentation](https://cds.climate.copernicus.eu/api-how-to)

## 💡 Casos de Uso

- **Investigación climática** - Descarga datos históricos para análisis de tendencias
- **Meteorología** - Obtén variables atmosféricas para predicción y modelado
- **Oceanografía** - Accede a datos de oleaje, temperatura superficial del mar
- **Agricultura** - Variables de suelo, precipitación, temperatura para estudios agrícolas
- **Energía renovable** - Datos de viento y radiación solar
- **Hidrología** - Precipitación, evaporación, escorrentía
- **Educación** - Herramienta didáctica para aprender sobre datos ERA5

## 🚀 Ventajas

✅ **Sin instalación** - Funciona directamente en el navegador  
✅ **Interfaz familiar** - Similar a la de Copernicus oficial  
✅ **Ahorra tiempo** - No escribas configuraciones manualmente  
✅ **Sin errores** - Validación automática de sintaxis  
✅ **Reutilizable** - Carga y edita configuraciones existentes  
✅ **Multiplataforma** - Windows, Mac, Linux, móvil  

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso personal y académico.

---

**🌍 Desarrollado para facilitar la configuración de descargas ERA5 del Copernicus Climate Data Store**  
*Genera tus archivos CONFIG.conf de forma rápida, visual e intuitiva*
