"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import burgeroutput as components_burgeroutput
from typing import Optional


@dataclasses.dataclass
class ReadBurgerRequest:
    burger_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'burger_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class ReadBurgerResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    burger_output: Optional[components_burgeroutput.BurgerOutput] = dataclasses.field(default=None)
    r"""Successful Response"""
    

