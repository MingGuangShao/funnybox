#encoding:utf-8
import os
import base64
from io import BytesIO
from typing import Text,Dict
from os import path
from wordcloud import WordCloud

class Cloud:
	"""word cloud"""
	def generate_wordcount(text: Text) -> Dict:
		"""根据分词后的一段文本，生成文本的统计数据"""
		wordcloud = WordCloud()
		return wordcloud.process_text(text)
	
	def generate_png_from_wordcount(wordcount: Dict) -> Text:
		"""根据wordcount生成png格式的图片"""
		path='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
		wordcloud = WordCloud(font_path=path, width=600, height=400).generate_from_frequencies(wordcount)
		img = wordcloud.to_image()
		# save img
		f = BytesIO()
		img.save(f, 'png')
		return base64.b64encode(f.getvalue()).decode()

	def generate_png_from_wordcount(wordcount: Dict) -> Text:
		"""根据wordcount生成png格式的图片"""
		path='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
		wordcloud = WordCloud(font_path=path, width=600, height=400).generate_from_frequencies(wordcount)
		img = wordcloud.to_image()
		# save img
		f = BytesIO()
		img.save(f, 'png')
		return base64.b64encode(f.getvalue()).decode()

	def generate_png_file():
		text = open(path.join(path.dirname(os.path.abspath(__file__)),'constitution.txt')).read()
		# Generate a word cloud image
		wordcloud = WordCloud().generate(text)
		wordcloud.to_file(path.join(path.dirname(os.path.abspath(__file__)),'test.png'))
		#print(wordcloud.to_image())
	
	def generate_png_bytes():
		text = open(path.join(path.dirname(os.path.abspath(__file__)),'constitution.txt')).read()
		# Generate a word cloud image
		wordcloud = WordCloud().generate(text)
		img = wordcloud.to_image()
		
		# save img
		f = BytesIO()
		img.save(f, 'png')
		return base64.b64encode(f.getvalue()).decode()

#Cloud.generate_png_file()
#print(Cloud.generate_png_bytes())
#print(Cloud.generate_wordcount("e e e e b b c d"))
#print(Cloud.generate_png_from_wordcount({'a':3,'b':2}))
