RUN = poetry run

serverup:
	${RUN} uvicorn main:app --reload

typecheck:
	${RUN} mypy main.py

update:
	curl -L https://unpkg.com/htmx.org/dist/htmx.min.js > static/js/htmx.min.js
	curl -L https://raw.githubusercontent.com/SamHerbert/SVG-Loaders/master/svg-loaders/three-dots.svg > static/img/spinner.svg
	poetry update
