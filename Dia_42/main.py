"""
==============================================================
Dia 42 — Uso de ambientes virtuais e requirements.txt
==============================================================

Ambientes virtuais (virtual environments) em Python são usados
para isolar dependências de projetos diferentes, evitando
conflitos entre versões de bibliotecas instaladas no sistema.

Por que usar ambientes virtuais?
- Evita conflitos entre bibliotecas de projetos diferentes
- Mantém o ambiente de desenvolvimento organizado
- Facilita a reprodução do projeto em outras máquinas
- É uma boa prática profissional em projetos Python

--------------------------------------------------------------
Criando um ambiente virtual
--------------------------------------------------------------

No diretório do projeto, execute:

python -m venv venv

Isso cria uma pasta chamada "venv" contendo o ambiente virtual.

--------------------------------------------------------------
Ativando o ambiente virtual
--------------------------------------------------------------

Windows:
venv\\Scripts\\activate

Linux / macOS:
source venv/bin/activate

Quando ativado, o terminal passa a usar o Python e o pip
do ambiente virtual.

--------------------------------------------------------------
Instalando dependências
--------------------------------------------------------------

Após ativar o ambiente virtual:

pip install flask sqlalchemy pandas

As bibliotecas serão instaladas apenas dentro do ambiente virtual.

--------------------------------------------------------------
Arquivo requirements.txt
--------------------------------------------------------------

O arquivo requirements.txt lista todas as dependências do projeto
com suas versões, permitindo que outra pessoa instale exatamente
o mesmo ambiente.

Para gerar o requirements.txt:

pip freeze > requirements.txt

Exemplo de conteúdo:
flask==3.0.0
sqlalchemy==2.0.25
pandas==2.1.4

--------------------------------------------------------------
Instalando dependências via requirements.txt
--------------------------------------------------------------

Com o ambiente virtual ativado:

pip install -r requirements.txt

Isso instala todas as dependências listadas no arquivo.

--------------------------------------------------------------
Boas práticas
--------------------------------------------------------------
- Nunca versionar a pasta "venv" no Git
- Sempre versionar o requirements.txt
- Usar ambientes virtuais em todos os projetos Python
- Manter o requirements.txt atualizado

--------------------------------------------------------------
Conclusão
--------------------------------------------------------------

O uso de ambientes virtuais junto com o requirements.txt
é essencial para desenvolvimento profissional em Python,
garantindo isolamento, organização e reprodutibilidade
dos projetos.
"""
