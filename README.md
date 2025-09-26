# SMARTFIX-TOOL-ENFORCEMENT-SOLANA-ANALYZER

Script Completo con Testnet API, Logs de Eventos y Reportes Automáticos

## 📋 Características

✅ **Conexiones Multi-Red**: Prueba conexiones con mainnet y testnet de Solana  
📊 **Análisis de Transacciones**: Analiza transacciones específicas con detalles completos  
🔍 **Investigación de Wallets**: Investiga wallets (origen y destino) con historial  
📝 **Logs en Tiempo Real**: Genera logs de eventos con timestamps  
💾 **Reportes Múltiples**: Crea reportes en JSON, CSV y HTML  

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/sjhallo07/SMARTFIX-TOOL-ENFORCEMENT-SOLANA-ANALIZER.git
cd SMARTFIX-TOOL-ENFORCEMENT-SOLANA-ANALIZER
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 📖 Uso

### Probar Conexiones
```bash
python solana_analyzer.py --test-connections
```

### Analizar una Transacción
```bash
python solana_analyzer.py --tx <TRANSACTION_SIGNATURE> --network mainnet
```

### Investigar un Wallet
```bash
python solana_analyzer.py --wallet <WALLET_ADDRESS> --network mainnet
```

### Ejemplo Completo
```bash
python demo.py
```

## ⚙️ Configuración

El archivo `config.json` permite configurar:
- URLs de las redes (mainnet, testnet, devnet)
- Directorios de salida para logs y reportes
- Parámetros de análisis

## 📊 Reportes Generados

El script genera automáticamente:
- **JSON**: Datos estructurados completos
- **CSV**: Tabular para análisis en Excel
- **HTML**: Reporte visual navegable

## 📝 Logs

Los logs se guardan automáticamente en `logs/` con:
- Timestamp de cada evento
- Status de conexiones
- Progreso del análisis
- Errores y advertencias

## 🔧 Parámetros CLI

```
--tx, --transaction     Signature de transacción a analizar
--wallet, --address     Dirección de wallet a investigar  
--network              Red a usar: mainnet|testnet|devnet
--test-connections     Solo probar conexiones
--config               Archivo de configuración personalizado
```

## 📄 Licencia

MIT License - ver `LICENSE` para detalles.
