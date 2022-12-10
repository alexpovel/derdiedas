serverup:
	@uvicorn main:app --reload

typecheck:
	mypy main.py

update:
	curl -L https://unpkg.com/htmx.org/dist/htmx.min.js > static/htmx.min.js
	curl -L https://unpkg.com/htmx.org/dist/ext/json-enc.js > static/json-enc.js
	curl -L https://raw.githubusercontent.com/SamHerbert/SVG-Loaders/master/svg-loaders/three-dots.svg > static/spinner.svg
	poetry update
