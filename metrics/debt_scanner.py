import ast
import os

class TechnicalDebtAnalyzer(ast.NodeVisitor):
    """
    Analiza de forma estática archivos de código fuente en busca de 
    funciones con alta complejidad ciclomática (indicadores de Deuda Técnica).
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.functions_analyzed = 0
        self.debt_warnings = []

    def visit_FunctionDef(self, node):
        self.functions_analyzed += 1
        # Complejidad ciclomática inicial
        complexity = 1
        
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler, ast.With, ast.Assert)):
                complexity += 1

        # Si una función tiene alta complejidad, se cataloga como Deuda Técnica Arquitectónica
        if complexity > 5:
            self.debt_warnings.append({
                "function": node.name,
                "line": node.lineno,
                "complexity": complexity
            })
        
        self.generic_visit(node)

def run_debt_scan():
    print("=" * 60)
    print("ESCANER DE DEUDA TÉCNICA ARQUITECTÓNICA (PROYECTO 2)")
    print("=" * 60)
    
    # Simulación de análisis sobre archivos del proyecto
    target_dir = "."
    total_warnings = 0

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read(), filename=path)
                        analyzer = TechnicalDebtAnalyzer(path)
                        analyzer.visit(tree)
                        
                        if analyzer.debt_warnings:
                            print(f"\n[!] Archivo analizado con alertas: {path}")
                            for warning in analyzer.debt_warnings:
                                print(f"    -> Función: '{warning['function']}' (Línea {warning['line']}) | Complejidad: {warning['complexity']}")
                                total_warnings += 1
                    except Exception as e:
                        pass

    print("\n" + "=" * 60)
    print(f"RESUMEN DEL DIAGNÓSTICO: {total_warnings} puntos de Deuda Técnica detectados.")
    if total_warnings == 0:
        print("[+] ¡Excelente! No se detectaron funciones con complejidad excesiva.")
    else:
        print("[!] Se recomienda aplicar Refactoring Arquitectónico en las funciones listadas.")
    print("=" * 60)

if __name__ == "__main__":
    run_debt_scan()
