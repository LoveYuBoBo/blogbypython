import asyncio,os,inspect,logging,functools
from urllib import parse
from aiohttp import web
from apis import APIError

def get(path):
	def decorator(func):
		@functools.wrap(func):
		def wrapper(*args,**kw):
			return func(*args,**kw)
		wrapper.__method__='GET'
		wrapper.__route__=path
		return wrapper
	return decorator

def post(path):
	def decorator(func):
		@functools.wrap(func)
		def wrapper(*args,**kw):
			return func(*args,**kw)
		wrapper.__method__='POST'
		wrapper.__route__=path
		return wrapper
	return decorator
	