# Office Employee Management System

* The Office Employee Management System is a software application designed to efficiently manage employee information and track their respective departments within an office setting.


## Requirements

1. Must have docker installed on the machine


## Steps

1. Create a virtualenv

```
python -m venv .venv
```

2. Install all the requirements

```
pip install -r req.txt
```

3. Run the postgres in docker instance

```
bash run_db.sh
```

4. Now start the fastapi app

```
uvicorn main:app --reload --port 9999
```

5. Go to localhost:9999/docs and access the APIs

