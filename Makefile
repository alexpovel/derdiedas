RUN = uv run

serverup:
	${RUN} uvicorn src.derdiedas:app --reload

typecheck:
	${RUN} --only-dev mypy src/

lint:
	${RUN} --only-dev ruff check src/

formatcheck:
	${RUN} --only-dev ruff format --check src/

lighthouse:
	npx @lhci/cli@0.14.0 autorun

terms.xlsx: data/terms.json
	${RUN} --group=data python -c "import pandas as pd; pd.read_json('$<').to_excel('$@', index=False)"

data/terms.json: terms.xlsx
	${RUN} --group=data python -c "import pandas as pd; pd.read_excel('$<').to_json('$@', orient='records', force_ascii=False, indent=2)"
