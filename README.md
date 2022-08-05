# Python cli app  
This is a simple command-line application that will calculate the ranking 
table for a league from a text file.  
### How to run the app  
Clone the repo  
`git clone git@github.com:Tauraih/cli-app.git && cd cli-app`  

create a virtualenv  
`python -m venv venv`  

activate venv  
`source venv/bin/activate`  

Install the Python requirements  
    `pip install -r requirements`  

Run the app  
    `python main.py text_filename`  
    
To run tests  
    `pytest --cov=.` 
