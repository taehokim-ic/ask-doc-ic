from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DB_NAME = "ask_doc_db"
DATABASE_URL = f"postgresql+asyncpg://postgres:password@localhost/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession :
    async_session = sessionmaker(
        engine , class_ = AsyncSession , expire_on_commit=False
    )
    async with async_session() as session:
        yield session
        
# from sqlmodel import create_engine, SQLModel
# from backend.models.data_models import *

# db_file_name = "ask_doc_db"
# DATABASE_URL = f"postgresql://postgres:password@localhost/{db_file_name}"

# # db_file_name = "database2.db"
# # DATABASE_URL = f"sqlite:///{db_file_name}"

# engine = create_engine(DATABASE_URL, echo=False)

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# if __name__ == "__main__":
#     create_db_and_tables()