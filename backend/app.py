from fastapi import FastAPI, Depends
from pymongo import MongoClient
from dotenv import load_dotenv  
from pydantic import BaseModel, Field, field_validator
import os
from datetime import datetime, timedelta, timezone
from typing import Optional, List
import random
from jose import JWTError, jwt
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends
from typing import Annotated
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
print(
    os.getenv('localone'), 
    os.getenv('localtwo'), 
    os.getenv('localthree'), 
    os.getenv('localfour'), 
    os.getenv('frontendone'), 
    os.getenv('frontendtwo'), 
    os.getenv('frontendthree'), 
    os.getenv('frontendfour'),
)

client = MongoClient(os.getenv("uri"))
db = client['grocerycollectlocations']
grocerycollection = db['grocerycollection']

app = FastAPI()

origins = [
    # os.getenv('localone'), 
    # os.getenv('localtwo'), 
    # os.getenv('localthree'), 
    # os.getenv('localfour'), 
    os.getenv('frontendone'), 
    os.getenv('frontendtwo'), 
    os.getenv('frontendthree'), 
    os.getenv('frontendfour'), 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# pydantic models for evaluating data --------------------------------------------------------------
class organizerDetails(BaseModel):
    organization_type: str
    first_name: str
    mobile_number: str
    verified: Optional[bool] = Field(default=False)
    created_at : Optional[datetime] = Field(default_factory=lambda:datetime.now())
    code: Optional[int] = Field(default_factory=lambda:random.randint(1000, 9999))
    code_send_time : datetime = Field(default_factory=lambda:datetime.now())
    accepted : Optional[bool] = Field(default=False)

    # @field_validator('code', mode='before')
    # def generate_code(cls, v):
    #     if v == 0:
    #         return random.randint(1000, 9999)
    #     return 

class verificationCode(BaseModel):
    mobile_number: str
    code : int
    verified: Optional[bool] = Field(default=True)
    verified_time : datetime = Field(default_factory=lambda: datetime.now(timezone.utc) + timedelta(hours=5, minutes=30))

class details(BaseModel):
    item_list : List[str]
    district : str
    town : str
    exact_place : str
    cordination : List[float]
    distributed_to : str
    descriptions : str
    archived : Optional[bool] = Field(default=False)
    end_date : Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc) + timedelta(hours=5, minutes=30))

# functions for check database --------------------------------------------------------------

def checkDuplicateNumber(mnum):
    # perepose : check provided mobile number is alredy in the database or not
    # return : {status : True, data : data} - duplicated | {status : False, data : None} - not duplicated
    data = grocerycollection.find_one({'mobile_number' : mnum})
    if data == None:
        return {'status' : False, 'data' : None}
    elif data != None:
        return {'status' : True, 'data' : data}

def storeUseData(data):
    # perpose : store user related data
    # return : True - success | False - error
    store = grocerycollection.insert_one(data)
    if store.inserted_id:
        return True
    else:
        return False
    
def sendVerification(code, mobile_num):
    # perpose : send OTP to user's mobile
    # return : True - success | Flase - error
    print(f'{code} should be send to the {mobile_num} via mobile msm API. ')
    return True

def getLocaitonData(mnum):
    # perpose : get all data related to mobile number
    # return : {stauts : True, data : data } - available | {stauts : Flase, data : [] } - not-available
    data = grocerycollection.find_one({'mobile_number' : mnum})
    if data != None:
        return {'status' : True, 'data' : data}
    elif data == None:
        return {'status' : False, 'data' : []}

def getAllLocationsData():
    # perpose : get all locations data from the database
    # return : data
    data = grocerycollection.find({})
    return data

def getAllLocationByDistrict(district):
    # perpose : get all locations data from the database by district
    # return : data
    data = grocerycollection.find({'district' : district})
    return data

def updateDatabase(mnum, data):
    # perpose : re-generate OTP and update the database
    # return : True - updated | False - not-updated
    store = grocerycollection.update_one({'mobile_number': mnum}, {'$set' : data})
    if store.matched_count == 1:
        return True
    elif store.matched_count == 0:
        return False

def getCurrentTimeUTC():
    # perpose : get current time accordint to the UTC
    # return datetime 
    return datetime.now() - timedelta(hours=5, minutes=30)

def timeConversion(obj):
    # perpose : convert datetime object to ISO 8601 string format
    # return : ISO 8601 string
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError

def locationSerializer(locationList):
    # perpose : serialize location data to send via API
    # return : serialized data list
    locations = []
    for location in locationList:
        location_info = {
            'item_list': location['item_list'],
            'district': location['district'],
            'town': location['town'],
            'exact_place': location['exact_place'],
            'cordination' : location['cordination'],
            'descriptions': location['descriptions'],
            'distributed_to' : location['distributed_to'],
            'archived' : location['archived'],
            'end_date' : timeConversion(location['end_date']),
            'verified' : location['verified'],
            'organization_type' : location['organization_type'],
            'first_name' : location['first_name'],
            'mobile_number' : location['mobile_number'],
        }
        locations.append(location_info)
    return locations

# authontications ------------------------------------------mobile_number--------------------------------
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
@app.post('/createaccount')
async def getOrganiserData(data : organizerDetails):
    # check number is duplicated or not
        # if duplicated + verified -> this is alredy in the system - error message
        # if duplicated + not verified 
            # if less than 30 minutes, send error
            # if more that 30 minutes
                # store new code and code generation time in datebase
                # send OPT
    # not duplicated
        # store datapass
        # send verification code
        # send success message  
    duplication = checkDuplicateNumber(data.mobile_number)
    if duplication['status'] == False:
        storedata = storeUseData(data.model_dump())
        if storedata:
            sendOTP = sendVerification(data.code, data.mobile_number)
            if sendOTP:
                return JSONResponse(status_code=200, content={'message' : 'OTP send'})
            elif sendOTP == False:
                return JSONResponse(status_code=500, content={'message' : 'something go wrong'})
        else:
                return JSONResponse(status_code=500, content={'message' : 'something go wrong'})
    elif duplication['status'] == True:
        currentTime = getCurrentTimeUTC()
        if duplication['data']['verified'] == True:
            return JSONResponse(status_code=400, content={'message' : 'number alredy registered'})
        elif duplication['data']['verified'] == False and (currentTime - duplication["data"]["code_send_time"]).total_seconds()/60 < 10.0:
            return JSONResponse(status_code=400, content={'message' : 'use alredy sent code'})
        elif duplication['data']['verified'] == False and (currentTime - duplication["data"]["code_send_time"]).total_seconds()/60 > 10.0:
            new_code = random.randint(1000, 9999)
            updateData = {
                'code' : new_code,
                'code_send_time' : currentTime
            }
            updateOTP = updateDatabase(data.mobile_number, updateData)
            if updateOTP:
                sendOPT = sendVerification(new_code, data.mobile_number)
                if sendOPT:
                    return JSONResponse(status_code=200, content={'message' : 'OTP send'})
                else:
                    return JSONResponse(status_code=500, content={'message' : 'something go wrong'})
            else:
                return JSONResponse(status_code=500, content={'message' : 'something go wrong'})



@app.post('/verification')
async def verifyOrganizer(dataset : verificationCode):
    # check mobile number is in the database
    # if not send error message
    # then check code with existing dataset
    # if not matched send error message
    # if matched update verified status and verified time
    # send JTW tocken
    locationData = getLocaitonData(dataset.mobile_number)
    if locationData['status'] == False:
        return JSONResponse(status_code=400, content={'message' : 'number not found'})
    elif locationData['data']['verified'] == True:
        return JSONResponse(status_code=400, content={'message' : 'number alredy verified'})
    elif locationData['status'] == True and locationData['data']['code'] != dataset.code:
        return JSONResponse(status_code=400, content={'message' : 'invalid code'})
    elif locationData['status'] == True and locationData['data']['code'] == dataset.code:
        dataset.code = 0
        updateStatus = updateDatabase(dataset.mobile_number, dataset.model_dump(include={'verified', 'verified_time', 'code'}))
        if updateStatus:
            token = encodeToken(dataset.mobile_number)
            return JSONResponse(status_code=200, content={'message' : 'successfull', 'token' : token})
        else:
            return JSONResponse(status_code=500, content={'message' : 'something go wrong'})


@app.post('/details')
async def addLocation(data : details, authData = Depends(authVerification)):
    # check token is valied or not and account is verified
    # if invalied send error message
    # if valied store data in token's mobile number
    # send success message
    if authData == False:
        return JSONResponse(status_code=401, content={'message' : 'invalid token'})
    locationData = getLocaitonData(authData['mobile'])
    if locationData['status'] == False:
        return JSONResponse(status_code=400, content={'message' : 'number not found'})
    elif locationData['status'] == True and locationData['data']['verified'] == False:
        return JSONResponse(status_code=400, content={'message' : 'account not verified'})
    elif locationData['status'] == True and locationData['data']['verified'] == True:
        updateStatus = updateDatabase(authData['mobile'], data.model_dump())
        if updateStatus:
            return JSONResponse(status_code=200, content={'message' : 'details added successfully'})
        else:
            return JSONResponse(status_code=500, content={'message' : 'something go wrong'})

@app.get('/location/all')
async def getAllLocations():
    # send all collection locaions list without 'id, code, enddate, cordination, mobile number, first name, destinations'
    data = getAllLocationsData()
    locations = locationSerializer(data)
    return JSONResponse(status_code=200, content={'message' : 'successfull', 'locations': locations})

@app.get('/location/{district}')
async def getDistrictLocations(district: str):
    # send requested location - locaions list without 'code'
    data = getAllLocationByDistrict(district)
    locations = locationSerializer(data)
    return JSONResponse(status_code=200, content={'message' : 'successfull', 'locations': locations})

@app.patch('/resendcode/{mobile_number}')
async def resendCode(mobile_number: str):
    # 1. check mobile number is in the database
    # 2. if not send error message
    # 3. if available, check the send time more than 15 minutes and note verified
    # 4. if more that send again
    # 5. else send error message
    locationData = getLocaitonData(mobile_number)
    if locationData['status'] == False:
        return JSONResponse(status_code=400, content={'message' : 'number not found'})
    elif locationData['status'] == True and locationData['data']['verified'] == True:
        return JSONResponse(status_code=400, content={'message' : 'number alredy verified'})
    elif locationData['status'] == True and locationData['data']['verified'] == False:
        currentTime = getCurrentTimeUTC()
        if (currentTime - locationData["data"]["code_send_time"]).total_seconds()/60 > 10.0:
            new_code = random.randint(1000, 9999)
            updateData = {
                'code' : new_code,
                'code_send_time' : currentTime
            }
            updateOTP = updateDatabase(mobile_number, updateData)
            if updateOTP:
                sendOPT = sendVerification(new_code, mobile_number)
                if sendOPT:
                    return JSONResponse(status_code=200, content={'message' : 'OTP send'})
                else:
                    return JSONResponse(status_code=500, content={'message' : 'something go wrong'})
            else:
                return JSONResponse(status_code=500, content={'message' : 'something go wrong'})
        else:
            return JSONResponse(status_code=400, content={'message' : 'use alredy sent code'})
