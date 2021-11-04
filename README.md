# Problem description
My solution is to classify whether breast cancer is benign or malignant based on the characteristics measured.

## Running without Docker
- Fisrt, install flask:
   - ```bash
        pip install flask
     ```

- Run the service:
   - ```bash
        python predict.py
     ```

- Test it from python:
   - ```python
        import requests
        url = 'http://localhost:9696/predict'
        response = requests.post(url, json=patient)
        result = response.json()
      ```

## Managing dependencies with Pipenv
- Install `pipenv`:
   - ```bash
        pip install pipenv
      ```

- Install the depencencies from the [Pipfile](Pipfile):
   - ```bash
        pipenv install
      ```

- Enter the pipenv virtual environment:
   - ```bash
        pipenv shell
      ```

- And run the code:
   - ```bash
        python predict.py
      ```

- Alternatively, you can do both steps with one command:
   - ```bash
        pipenv run python churn_serving.py
      ```

Now you can use the same code for testing the model locally.

## Running with Docker
- Build the image (defined in [Dockerfile](Dockerfile))
   - ```bash
    	 docker build -t modelling .
     ```

- Run it:
   - ```bash
    	docker run -it -p 9696:9696 modelling:latest    
     ```
