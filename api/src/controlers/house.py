from litestar import Controller, get, post, put, patch, delete
from litestar.datastructures import State
from litestar.dto import DTOData

from src.models import House, PartialHouseDTO


class HouseController(Controller):
    path = "/houses"

    @post()
    async def create_house(self, data: House, state: State) -> House:
        cursor = state.connection.cursor()
        cursor.execute("INSERT INTO houses (address, url) VALUES (:address, :url) RETURNING *", data.to_dict())
        results = cursor.fetchall()
        state.connection.commit()
        return results

    @get()
    async def list_houses(self, state: State) -> list[House]:
        cursor = state.connection.cursor()
        cursor.execute("SELECT * FROM houses")
        houses = cursor.fetchall()
        return houses

    @patch(path="/{house_id:int}", dto=PartialHouseDTO)
    async def partial_update_house(
        self, house_id: int, data: DTOData[House]
    ) -> House: ...

    @put(path="/{house_id:int}")
    async def update_house(self, house_id: int, data: House) -> House: ...

    @get(path="/{house_id:int}")
    async def get_house(self, house_id: int, state: State) -> House:
        cursor = state.connection.cursor()
        cursor.execute("SELECT * FROM houses WHERE id = ?", (house_id,))
        return cursor.fetchall()

    @delete(path="/{house_id:int}")
    async def delete_house(self, house_id: int) -> None: ...