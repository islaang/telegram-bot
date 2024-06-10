from database.models import *
from sqlalchemy import select, update, delete, insert 


async def get_departments():
    async with async_session() as session:
        result = await session.scalars(select(Department))
        return result 
    
async def get_rabs(department_id):
    async with async_session() as session:
        result = await session.scalars(select(Rab).where(Rab.department_id == department_id))
        return result
    