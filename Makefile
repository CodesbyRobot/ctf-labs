.PHONY: test cookie-trust rebuild-png

test:
	python3 -m unittest discover -s tests -v

cookie-trust:
	python3 challenges/03-cookie-trust/app.py

rebuild-png:
	python3 challenges/04-png-breadcrumb/build_evidence.py
