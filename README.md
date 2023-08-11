# PyNotes-API
Welcome to the PyNotes-API repository! This is a simple guide to help you get started with setting up and running the PyNotes-API project.

## Getting Started

Follow these steps to set up and run the project on your local machine:

**Clone the repository:**
```sh 
git clone git@github.com:vcjuliocesar/pynotes-api.git
```
**Create a Virtual Environment:**
```sh
 python3 -m venv env
```
**Activate the Virtual Environment:**
On macOS/Linux:
```sh
 source env/bin/activate
```
On Windows:
```sh
 .\env\Scripts\activate
```
**Install Dependencies:**
```sh
 pip3 install -r requirements.txt
```
**Run the Project:**
```sh
 uvicorn main:app --reload
```

## Docker
if you prefer to use docker follow these steps, it is important that you have docker installed on your computer
```sh
docker compose build
```
```sh
docker compose up
```
Once the project is up and running, you can access it through your browser or API client.