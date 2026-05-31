from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from opentelemetry import trace

import crud
import schemas
from database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

tracer = trace.get_tracer(__name__)


@router.post(
    "/",
    response_model=schemas.UserResponse
)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    with tracer.start_as_current_span(
        "create_user_span"
    ):

        return crud.create_user(
            db,
            user
        )


@router.get(
    "/",
    response_model=list[
        schemas.UserResponse
    ]
)
def get_users(
    db: Session = Depends(get_db)
):

    with tracer.start_as_current_span(
        "get_users_span"
    ):

        return crud.get_users(db)


@router.get(
    "/{user_id}",
    response_model=schemas.UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    with tracer.start_as_current_span(
        "get_user_span"
    ):

        user = crud.get_user(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user


@router.put(
    "/{user_id}",
    response_model=schemas.UserResponse
)
def update_user(
    user_id: int,
    user: schemas.UserUpdate,
    db: Session = Depends(get_db)
):

    with tracer.start_as_current_span(
        "update_user_span"
    ):

        updated_user = crud.update_user(
            db,
            user_id,
            user
        )

        if not updated_user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return updated_user


@router.delete(
    "/{user_id}"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    with tracer.start_as_current_span(
        "delete_user_span"
    ):

        user = crud.delete_user(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return {
            "message": "User deleted"
        }
