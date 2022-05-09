fmt:
	isort .
	black .

lint:
	isort . --check-only
	black . --check

patch:
	bumpversion patch

minor:
	bumpversion minor

major:
	bumpversion major
