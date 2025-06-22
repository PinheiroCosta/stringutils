from fastapi import APIRouter
from app.services import string_ops
from app.schemas import TextInput, CharCountInput
from typing import Dict

router = APIRouter()


@router.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "ok"}


@router.post("/reverse")
def reverse(input: TextInput) -> Dict[str, str]:
    return {"result": string_ops.reverse(input.text)}


@router.post("/uppercase")
def uppercase(input: TextInput) -> Dict[str, str]:
    return {"result": string_ops.uppercase(input.text)}


@router.post("/lowercase")
def lowercase(input: TextInput) -> Dict[str, str]:
    return {"result": string_ops.lowercase(input.text)}


@router.post("/slugify")
def slugify(input: TextInput) -> Dict[str, str]:
    return {"result": string_ops.slugify(input.text)}


@router.post("/uuid")
def generate_uuid() -> Dict[str, str]:
    return {"result": string_ops.generate_uuid()}


@router.post("/charcount")
def count(input: CharCountInput) -> Dict[str, int]:
    return string_ops.count_characters(
        text=input.text,
        count_spaces=input.count_spaces,
        count_special=input.count_special,
        count_escaped=input.count_escaped,
    )


@router.post("/ascii")
def ascii_converter(input: TextInput) -> Dict[str, str]:
    return {"result": string_ops.ascii_converter(input.text)}


@router.post("/palindrome")
def palindrome(input: TextInput) -> Dict[str, bool]:
    return {"result": string_ops.is_palindrome(input.text)}
