#encoding:utf-8
from sanic import Sanic, response
from sanic.request import Request
from sanic.response import HTTPResponse
from sanic_cors import CORS

from cloudwords.cloudwords import Cloud

def create_app() -> Sanic:
	app = Sanic("funnybox")
	CORS(app)

	@app.get("/version")
	async def version(request: Request) -> HTTPResponse:
		return response.json(
			{
				"version": "0.1.1",
			}
		)
	
	@app.post("/generate/wordcount")
	async def generate_wordcount(request: Request) -> HTTPResponse:
		"""根据text,获取wordcount"""
		request_params = request.json
		text = request_params.get("text")
		wordcount = Cloud.generate_wordcount(text)
		return response.json({'data': wordcount})
    
	@app.post("/generate/png/wordcount")
	async def generate_png_wordcount(request: Request) -> HTTPResponse:
		"""根据word count, 生产图片"""
		request_params = request.json
		data = request_params.get("data")
		# 格式转换
		data_source = dict()
		for d in data:
			data_source[d['word']] = int(d['count'])

		png = Cloud.generate_png_from_wordcount(data_source)
		return response.json({'data': png})

	@app.get("/generate")
	async def generate(request: Request) -> HTTPResponse:
		Cloud.generate_png_file()
		return response.json(
			{
				"ok":"ok",
			}    
		)
	return app
