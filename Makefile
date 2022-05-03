all: requirements.txt
	@echo "Creating execution environment..."
	@pip3 install -r requirements.txt
	@echo "Done"

remove: requirements.txt
	@echo "Deleting execution environment..."
	@pip3 uninstall -r requirements.txt -y
	@echo "Done"