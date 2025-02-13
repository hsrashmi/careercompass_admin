from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .converter import organization_converter
from ..dependencies import get_db
from ..domain.organization import service, schemas
from .util_functions import generate_uuid, success_message_response
from resources.strings import ORG_DOES_NOT_EXIST_ERROR

router = APIRouter(tags=["organization"])


@router.post("/organization/", response_model=schemas.OrganizationResponse)
def create_organization(organization: schemas.OrganizationBase, db: Session = Depends(get_db)):
    unique_id = str(generate_uuid())   
    updated_org = organization.model_copy(update={"organization_id": unique_id})   
    return service.create_organization(db=db, organization=updated_org)

@router.get("/organization/", response_model=List[schemas.OrganizationResponse])
def read_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    organizations = service.get_organizations(db, skip=skip, limit=limit)
    return organization_converter.convert_many(organizations)

@router.get("/organization/{organization_id}", response_model=schemas.OrganizationResponse)
def read_organization(organization_id: str, db: Session = Depends(get_db)):
    db_org = service.get_organization(db, org_id=organization_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail=ORG_DOES_NOT_EXIST_ERROR)
    return organization_converter.convert(db_org)

@router.put("/organization/{organization_id}", response_model=success_message_response)
def update_organization(organization_id: str, organization: schemas.OrganizationBase, db: Session = Depends(get_db)):
    db_org = service.get_organization(db, org_id=organization_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail=ORG_DOES_NOT_EXIST_ERROR)
    return service.update_organization(db=db, org_id=organization_id, organization=organization)

@router.delete("/organization/{organization_id}", response_model=success_message_response)
def delete_organization(organization_id: str, db: Session = Depends(get_db)):
    db_org = service.get_organization(db, org_id=organization_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail=ORG_DOES_NOT_EXIST_ERROR)
    return service.delete_organization(db=db, org_id=organization_id)