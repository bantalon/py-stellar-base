# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
import base64
from typing import List
from xdrlib import Packer, Unpacker

from .base import String
from .sc_spec_udt_struct_field_v0 import SCSpecUDTStructFieldV0

__all__ = ["SCSpecUDTStructV0"]


class SCSpecUDTStructV0:
    """
    XDR Source Code::

        struct SCSpecUDTStructV0
        {
            string name<60>;
            SCSpecUDTStructFieldV0 fields<40>;
        };
    """

    def __init__(
        self,
        name: bytes,
        fields: List[SCSpecUDTStructFieldV0],
    ) -> None:
        _expect_max_length = 40
        if fields and len(fields) > _expect_max_length:
            raise ValueError(
                f"The maximum length of `fields` should be {_expect_max_length}, but got {len(fields)}."
            )
        self.name = name
        self.fields = fields

    def pack(self, packer: Packer) -> None:
        String(self.name, 60).pack(packer)
        packer.pack_uint(len(self.fields))
        for fields_item in self.fields:
            fields_item.pack(packer)

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> "SCSpecUDTStructV0":
        name = String.unpack(unpacker)
        length = unpacker.unpack_uint()
        fields = []
        for _ in range(length):
            fields.append(SCSpecUDTStructFieldV0.unpack(unpacker))
        return cls(
            name=name,
            fields=fields,
        )

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> "SCSpecUDTStructV0":
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> "SCSpecUDTStructV0":
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.name == other.name and self.fields == other.fields

    def __str__(self):
        out = [
            f"name={self.name}",
            f"fields={self.fields}",
        ]
        return f"<SCSpecUDTStructV0 [{', '.join(out)}]>"
