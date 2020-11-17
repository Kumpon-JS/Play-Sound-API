from typing import Optional

from fastapi import FastAPI
from playsound import playsound
import threading
import time
import os.path

app = FastAPI()

global isRun
isRun = False
ROOT_DIR = os.getcwd()
FILE_DIR = os.path.join(ROOT_DIR,'files')

def reRun():
    time.sleep(5)
    print('set rerun')
    global isRun
    isRun = False


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/play/{item_id}")
async def play(item_id: str, q: Optional[str] = None):
    print('request')
    global isRun
    print(isRun)
    if isRun:
        return {"item_id": item_id}
    isRun = True
    open_file = os.path.join(FILE_DIR,item_id+'.mp3')
    print(open_file)
    playsound(open_file)
    t1 = threading.Thread(target=reRun)
    t1.start()
    # t1.join()
    return {"item_id": item_id}