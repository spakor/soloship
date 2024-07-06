# Define the name of the virtual environment directory
VENV_DIR=venv

# Define the python executable inside the virtual environment
PYTHON=$(VENV_DIR)/bin/python

# Define the pip executable inside the virtual environment
PIP=$(VENV_DIR)/bin/pip

# Create a virtual environment
$(VENV_DIR)/bin/activate: 
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip setuptools

# Install dependencies
install: $(VENV_DIR)/bin/activate
	$(PIP) install -r requirements.txt

# Freeze the current environment packages into requirements.txt
freeze: $(VENV_DIR)/bin/activate
	$(PIP) freeze > requirements.txt

# Run Streamlit app
run: $(VENV_DIR)/bin/activate
	$(PYTHON) -m streamlit run solopreunership/app.py

# Clean up the virtual environment
clean:
	rm -rf $(VENV_DIR)

# Reinstall dependencies (clean + install)
reinstall: clean install

.PHONY: install freeze run clean reinstall
