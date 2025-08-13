a1 policy server/
│
├── main.py                         # Main entrypoint to start Flask server
├── config.py                       # Configuration variables
├── policy-fetch/fetch.py           # InfluxDB connection and query
├── policy-trigger/trigger.py       # Logic to trigger A1 policies
├── routes/policy-routes.py         # All Flask endpoints related to policy
├── template/view.html              # HTML template to render policies             
└── requirements.txt                # Python dependencies


#Create a Python Virtual Environment (Optional but Recommended)
 
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


#Install Dependencies

pip install -r requirements.txt

#Run Flask Server 

python main.py


#Check Outputs on 

http://<ip>:5002/metrics -- Fetch InfluxDB metrics and trigger policies

http://<ip>:5002/policies -- Accept POST requests 

http://<ip>:5002/poliices/view -- Display all created policies on Dashboard(in HTML form)
