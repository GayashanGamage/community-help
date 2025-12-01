from fastapi import FastAPI, Depends
from pymongo import MongoClient
from dotenv import load_dotenv  
from pydantic import BaseModel, Field
import os
from datetime import datetime
from typing import Optional, List
import random
from jose import JWTError, jwt
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends
from typing import Annotated


load_dotenv()
client = MongoClient(os.getenv("uri"))
db = client['grocery']
grocerycollection = db['grocerycollection']

app = FastAPI()

# pydantic models for evaluating data --------------------------------------------------------------
class organizerDetails(BaseModel):
    organization_type: str
    first_name: str
    mobile_number: str
    verified: bool = False
    created_at : datetime = Field(default_factory=datetime.now)
    code: int = Field(default_factory=lambda: random.randint(1000, 9999))

class verificationCode(BaseModel):
    mobile_number: str
    code : int
    verified_time : datetime = Field(default_factory=datetime.now)

class details(BaseModel):
    item_list : List[str]
    district : str
    town : str
    exact_place : str
    cordination : List[float]
    distributed_to : List[str]
    descriptions : List[str]
    end_date : Optional[datetime] = Field(default=datetime.now)

# functions for check database --------------------------------------------------------------
def checkDuplicateNumber(mnum):
    pass

def getCreatedTime(data):
    pass

def getVerificationCode(mnum):
    pass


# authontications --------------------------------------------------------------------------
security = HTTPBearer()

def encodeToken(mobile):
    token = jwt.encode({'mobile': mobile}, os.getenv('jwt_token'), algorithm='HS256')
    return token

def decodeToken(token):
    try:
        data = jwt.decode(token, os.getenv('jwt_token'), algorithms=['HS256'])
        return data
    except JWTError:
        return False

def authVerification(details: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    return decodeToken(details.credentials)

# API endpoints ----------------------------------------------------------------------------
@app.post('/organiser')
async def getOrganiserData(data : organizerDetails):
    # check number is duplicated or not
        # if duplicated + verified -> this is alredy in the system - error message
        # if duplicated + not verified -> send the time that try to create account
    # not duplicated
        # store data
        # send verification code
        # send success message  
    pass

@app.post('/verification')
async def verifyOrganizer(data : verificationCode):
    # check mobile number is verified or not
    # if allredy verified + 30 minites pass
    # send code again
    # else send error code to ask wait
    # check mobile number + code
    # if pass, then send jwt tocken
    # else send error code 
    pass

@app.post('/details')
async def addLocation(data : details, authData = Depends(authVerification)):
    # check token is valied or not
    # if invalied send error message
    # if valied store data in token's mobile number
    # send success message
    pass

@app.patch('/update')
async def updateDetails(authData = Depends(authVerification)):
    # check token is valied or not
    # if invalied send error message
    # if valied store data in token's mobile number
    # send success message
    pass

@app.get('/location/all')
async def getAllLocations():
    # send all collection locaions list without 'id, code, enddate, cordination, mobile number, first name, destinations'
    pass

@app.get('/location/{district}')
async def getDistrictLocations():
    # send requested location - locaions list without 'code'
    pass
