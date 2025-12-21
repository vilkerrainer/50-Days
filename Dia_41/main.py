# ======================================== #
# ------ORM básico com SQLAlchemy--------- #
# Defina uma tabela e faça operações CRUD. #
# ======================================== #

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os


DATABASE_URL = "sqlite:///usuarios.db"

Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', idade={self.idade})>"


engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()


def criar_tabela():
    Base.metadata.create_all(engine)


def criar_usuario(nome, idade):
    usuario = Usuario(nome=nome, idade=idade)
    session.add(usuario)
    session.commit()
    print("Usuário criado:", usuario)


def listar_usuarios():
    usuarios = session.query(Usuario).all()
    for u in usuarios:
        print(u)


def atualizar_usuario(usuario_id, novo_nome, nova_idade):
    usuario = session.query(Usuario).get(usuario_id)
    if usuario:
        usuario.nome = novo_nome
        usuario.idade = nova_idade
        session.commit()
        print("Usuário atualizado:", usuario)
    else:
        print("Usuário não encontrado.")


def deletar_usuario(usuario_id):
    usuario = session.query(Usuario).get(usuario_id)
    if usuario:
        session.delete(usuario)
        session.commit()
        print("Usuário deletado.")
    else:
        print("Usuário não encontrado.")


if __name__ == "__main__":
    if not os.path.exists("usuarios.db"):
        criar_tabela()

    criar_usuario("Ana", 30)
    criar_usuario("João", 25)

    print("\nLista de usuários:")
    listar_usuarios()

    print("\nAtualizando usuário ID 1:")
    atualizar_usuario(1, "Ana Silva", 31)

    print("\nLista atualizada:")
    listar_usuarios()

    print("\nDeletando usuário ID 2:")
    deletar_usuario(2)

    print("\nLista final:")
    listar_usuarios()


# ================================= #
# Para rodar: python -m Dia_41.main #
# ================================= #
