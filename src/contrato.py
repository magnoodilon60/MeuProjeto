from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, validator
from datetime import datetime
from enum import Enum

# vamos setar cada variavel ou coluna que o nosos documento vai ter

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"




class Vendas(BaseModel):
    """
    Modelo de dados para as vendas;
    args:
        emial (str): emial do comprador
        data (int): data da compra
        valor (float): valor da compra
        protudo (str): nome do produto
        quantidade (int): quantidade de produtos
        categoria (str): categorai do produto
    
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    produto: str
    quantidade: PositiveInt
    categoria: CategoriaEnum


    @validator('categoria')
    def categoria_deve_estar_no_enum(cls, error):
        return error


