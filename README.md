# MSEngage
1) Run `Model.ipynb` to generate the required dataset
2) `streamlit run app.py` to run the project on frontend

Note:
Too many API requests can cause the app to throw the following error
    `ConnectionError: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))`.
The error can be resolved by halting the app by using `time.sleep(1)` after every poster fetch.
