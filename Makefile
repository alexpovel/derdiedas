RUN = poetry run

serverup:
	${RUN} uvicorn main:app --reload

typecheck:
	${RUN} mypy main.py

lighthouse:
	lighthouse --view http://localhost:8000

update:
	curl -L https://unpkg.com/htmx.org/dist/htmx.min.js > static/js/htmx.min.js
	curl -L https://raw.githubusercontent.com/SamHerbert/SVG-Loaders/master/svg-loaders/three-dots.svg > static/img/spinner.svg
	poetry update

# Convenience conversion targets for working with the list of terms. Make sure to
# install the `data` dependency group via `poetry` first (taken care of by `poetry
# install`).
terms.xlsx: data/terms.json
	python -c "import pandas as pd; pd.read_json('$<').to_excel('$@', index=False)"

data/terms.json: terms.xlsx
	python -c "import pandas as pd; pd.read_excel('$<').to_json('$@', orient='records', force_ascii=False, indent=2)"
