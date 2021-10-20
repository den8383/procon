install:
	docker exec procon-python-container bash -c "cd app && pipenv install"
check_python:
	docker exec procon-python-container bash -c "cd app && pipenv run python src/check_python.py"

exec-docker:
	docker exec -it procon-python-container bash
