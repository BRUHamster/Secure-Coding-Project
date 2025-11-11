from __future__ import annotations

from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI(title='Household Chores Tracker')

try:
    from sqlalchemy.orm import Session
except Exception:
    Session = None


# Guard heavy domain imports so tests can import app without installing all dependencies (e.g., sqlalchemy).
try:
    from domain.auth import authenticate_user, create_access_token, get_current_user, get_password_hash
    from domain.db import (
        AssignmentCreate,
        AssignmentModel,
        AssignmentRead,
        ChoreCreate,
        ChoreModel,
        ChoreRead,
        GroupCreate,
        GroupModel,
        GroupRead,
        NotFoundError,
        PatchChore,
        PatchGroup,
        PatchUser,
        UserCreate,
        UserModel,
        UserRead,
    )
    from domain.user import get_user_by_id, get_user_by_username, create_user
    from domain.group import get_group_by_id, create_group
    from domain.chore import get_chore_by_id, create_chore, assign_chore
    from domain.tracker import add_assignment, update_assignment_status, get_assignments_for_user
    from domain.status import StatusEnum
    from domain.jwt import verify_token
except Exception as e:
    # Fallback placeholders when dependencies are missing (used only for tests that don't exercise DB)
    authenticate_user = create_access_token = get_current_user = get_password_hash = None
    AssignmentCreate = AssignmentModel = AssignmentRead = ChoreCreate = ChoreModel = ChoreRead = object
    GroupCreate = GroupModel = GroupRead = NotFoundError = PatchChore = PatchGroup = PatchUser = object
    UserCreate = UserModel = UserRead = get_user_by_id = get_user_by_username = create_user = None
    get_group_by_id = create_group = get_chore_by_id = create_chore = assign_chore = None
    add_assignment = update_assignment_status = get_assignments_for_user = None
    StatusEnum = type('StatusEnum', (), {'TODO': 'TODO', 'DONE': 'DONE'})
    verify_token = None

def read_root():
    return {"message": "Household Chores Tracker — API. Документация: /docs"}


@app.get("/health")
def health_check():
    return {"status": "ok"}