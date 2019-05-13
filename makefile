zip:
	gzip animations/*.fla
zip-sounds:
	gzip sounds/*
unzip:
	gunzip animations/*.gz

FILE ?= "references/church.png"
edge:
	@python3 edges.py $(FILE)

blur:
	@python3 blur.py $(FILE)
