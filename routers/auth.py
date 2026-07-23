from fastapi import APIRouter,Depends,HTTPException,status

from sqlalchemy.orm import Session
import models
import schemas
import utils
import oauth2
from database import get_db
from services.activity_service import create_activity
from fastapi.security import OAuth2PasswordRequestForm
router= APIRouter(
    prefix="/auth",
    tags=["Authentication"]

)

#rigister user

@router.post(
    "/register",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user:schemas.UserCreate,
    db:Session=Depends(get_db)
):
    
    #check email already exists
    existing_user=(
        db.query(models.User)
        .filter(models.User.email==user.email)
        .first()
    )
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
        
    #hash password
    
    hashed_password= utils.hash_password(user.password)
    new_user=models.User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password,
        role=user.role
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    #activity log
    
    create_activity(db=db,
                    user_id=new_user.id,
                    action="user Registered",
                    entity_type="user",
                    entity_id=new_user.id,
                    description=f"{new_user.full_name}registered successfully."
                    )
    return new_user

#login user

@router.post("/login")
def login(
    user_credentials:OAuth2PasswordRequestForm=Depends(),
    db:Session=Depends(get_db)
):
    
    #check user
    user=(
        db.query(models.User)
        .filter(models.User.email==user_credentials.username)
        .first()
    )
    
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Email or password"
            
        )
        
    # verify password


   
    print("user.password")
    if not utils.verify(user_credentials.password,
                        user.password # pyright: ignore[reportArgumentType]
     ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Email or Password"
        )
    
    #create JWT Token
    
    access_token=oauth2.create_access_token(
        data={"user_id":user.id}
    )
    
    #activity log
    
   # create_activity(
    #    db=db,
     #   user_id=user.id,
      #  action="User Login",
       # entity_type="User",
        #entity_id=user.id,
        #description=f"{user.full_name}logged into the system."
        #)
    return{
        "access_token":access_token,
        "token_type": "bearer",
        "user":{
            "id":user.id,
            "full_name":user.full_name,
            "email":user.email,
            "role":user.role
        }
    }
    
#get current user

@router.get(
    "/me",
    response_model=schemas.UserResponse
)
def get_current_user_details(
    current_user=Depends(oauth2.get_current_user)
):
    return current_user

#logout user

@router.post("/logout")
def logout(
    current_user=Depends(oauth2.get_current_user),
    db:Session=Depends(get_db)
):
    create_activity(
        db=db,
        user_id=current_user.id,
        action="User Logout",
        entity_type="User",
        entity_id=current_user.id,
        description=f"{current_user.full_name}logged out."
        
)
    return{
        "message":"logout successfully."
    }