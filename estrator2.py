import PyPDF2
import os

def listar_arquivos():
    """Lista apenas arquivos .pdf no diretório atual."""
    arquivos = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    
    if not arquivos:
        print("[-] Nenhum arquivo PDF encontrado neste diretório.")
        return None, None

    print("\n--- Conteúdo da Pasta (PDFs) ---")
    for f in arquivos:
        print(f"-> {f}")
    
    origem = input("\nDigite o nome do arquivo que deseja extrair: ").strip()
    
    if origem not in arquivos:
        print(f"[-] Erro: O arquivo '{origem}' não foi encontrado.")
        return None, None
    
    destino = input("Digite o nome do arquivo de saída (.txt): ").strip()
    # Garante extensão .txt
    if not destino.lower().endswith('.txt'):
        destino += ".txt"
        
    return origem, destino

def extrair_pdf(origem, destino):
    print(f"\n[!] Iniciando extração: {origem} -> {destino}")
    try:
        with open(origem, 'rb') as arquivo:
            leitor = PyPDF2.PdfReader(arquivo)
            total_paginas = len(leitor.pages)
            
            with open(destino, 'w', encoding='utf-8') as out:
                for i in range(total_paginas):
                    pagina = leitor.pages[i]
                    texto = pagina.extract_text()
                    
                    if texto and texto.strip():
                        out.write(texto + "\n\n")
                    else:
                        out.write(f"\n--- [Página {i+1} vazia ou contendo apenas imagem] ---\n\n")
                    
                    # Feedback de progresso
                    print(f"Processando: {i+1}/{total_paginas} páginas...", end="\r")
        
        print(f"\n[+] Sucesso! O arquivo '{destino}' está pronto.")
        
    except Exception as e:
        print(f"\n[-] Erro crítico: {e}")

if __name__ == "__main__":
    origem, destino = listar_arquivos()
    if origem and destino:
        extrair_pdf(origem, destino)
