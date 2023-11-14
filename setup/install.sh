echo "+ | Creating virtual environment..."
python -m venv .venv
echo "+ | Activating virtual environment..."
source .venv/bin/activate

echo "+ | Installing requirements..."
pip install -r requirements.txt

echo "+ | Creating .env file..."
touch .env