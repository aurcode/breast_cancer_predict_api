# Problem description
My solution is to classify whether breast cancer is benign or malignant based on the characteristics measured.

- To run it, Simply execute the command below:
   - ```bash
        docker build -t modelling .
        docker run -it -p 9696:9697 modelling:latest    
      ```


## Running with Docker

- Build the image (defined in [Dockerfile](Dockerfile))

   - ```bash
	docker build -t breast-cancer-prediction .
     ```

- Run it:

   - ```bash
	docker run -it -p 9696:9696 breast-cancer-prediction:latest
     ```
