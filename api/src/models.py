from uuid import UUID

from dataclasses import dataclass
from litestar.dto import DTOConfig, DataclassDTO


@dataclass
class House:
    address: str
    url: str
    id: int

    def to_dict(self) -> dict:
        return {'address': self.address, 'url': self.url}


class PartialHouseDTO(DataclassDTO[House]):
    config = DTOConfig(exclude={"id"}, partial=True)
    def to_dict(self):
        super().to_dict()
