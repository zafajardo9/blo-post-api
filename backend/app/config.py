from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv
import os

load_dotenv()
DB_CONFIG = os.getenv("DATABASE_URL")

print(DB_CONFIG)


SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")

DB_CONFIG = os.getenv("DATABASE_URL")

# DB_CONFIG = f"postgresql+asyncpg://blog_hsun_user:fzKa3wNbcWTPViMNLXRdY4L0XABY8Z8X@dpg-cn6bt7icn0vc73dc2vvg-a.singapore-postgres.render.com/blog_hsun"

ACCESS_TOKEN_EXPIRE_MINUTES = 600




class AsyncDatabaseSession: 

    def __init__(self) -> None:
        self.session = None
        self.engine = None

    def __getattr__(self,name):
        return getattr(self.session,name)

    def init(self):
        self.engine = create_async_engine(DB_CONFIG, future=True, echo=True,pool_size=10, max_overflow=20)
        self.session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)()

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
            
    @property
    def is_active(self):
        return self.session.is_active if self.session else False 


db = AsyncDatabaseSession()

async def commit_rollback():
    if db.is_active: 
        try:
            await db.commit()
        except Exception:
            await db.rollback()
            raise
        
        