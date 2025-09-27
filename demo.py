#!/usr/bin/env python3
"""
Ejemplo de uso del SMARTFIX Solana Analyzer
"""

import asyncio
from solana_analyzer import SolanaAnalyzer

async def demo_analysis():
    """Demuestra las capacidades del analizador."""
    print("🚀 SMARTFIX Solana Analyzer - Demo")
    print("=" * 50)
    
    # Inicializar analizador
    analyzer = SolanaAnalyzer()
    
    # Probar conexiones
    print("\n1. Probando conexiones de red...")
    connections = await analyzer.test_network_connections()
    
    for network, status in connections.items():
        status_icon = "✅" if status else "❌"
        print(f"   {status_icon} {network.title()}: {'OK' if status else 'Error'}")
    
    # Ejemplo de análisis de wallet (usar una dirección conocida)
    if connections.get("mainnet", False):
        print("\n2. Investigando wallet de ejemplo...")
        
        # Wallet público conocido de Solana (puede no tener mucha actividad)
        example_wallet = "11111111111111111111111111111112"  # System Program
        
        wallet_result = await analyzer.investigate_wallet(example_wallet, "mainnet")
        
        if "error" not in wallet_result:
            print(f"   ✅ Wallet analizado: {wallet_result['address']}")
            print(f"   💰 Balance: {wallet_result['balance_sol']} SOL")
            print(f"   📊 Transacciones recientes: {len(wallet_result['recent_transactions'])}")
        else:
            print(f"   ❌ Error: {wallet_result['error']}")
        
        # Generar reportes
        print("\n3. Generando reportes...")
        results = [wallet_result] if "error" not in wallet_result else []
        
        if results:
            report_files = analyzer.generate_reports(results, "demo_analysis")
            print("   📄 Reportes generados:")
            for file in report_files:
                print(f"     - {file}")
    
    print(f"\n✅ Demo completada. Revisa los logs en: {analyzer.config['output']['logs_dir']}/")

if __name__ == "__main__":
    asyncio.run(demo_analysis())