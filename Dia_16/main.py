# ==================================================================================== #
# ---------------------------Hashing e criptografia simples--------------------------- #
# Use o módulo hashlib para gerar um hash SHA-256 de uma senha fornecida pelo usuário. #
# ==================================================================================== #

import hashlib

def gerar_hash_sha256(senha):

    senha_em_bytes = senha.encode('utf-8')    
    hash_obj = hashlib.sha256(senha_em_bytes)    
    hash_hexadecimal = hash_obj.hexdigest()    
    return hash_hexadecimal

senha_usuario = input("Digite a senha para gerar o hash: ")

if not senha_usuario:
    print("Nenhuma senha foi digitada. Saindo.")
else:
    hash_gerado = gerar_hash_sha256(senha_usuario)
    
    print("\n--- Resultado ---")
    print(f"Senha original: {senha_usuario}")
    print(f"Hash SHA-256 gerado: {hash_gerado}")

# ================================= #
# Para rodar: python -m Dia_16.main #
# ================================= #