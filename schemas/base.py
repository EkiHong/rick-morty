# models/base.py
from pydantic import BaseModel, ConfigDict

class APIResponseBase(BaseModel):
    # set extra='forbid' to confirm if API add the new column which will catched immediately.
    model_config = ConfigDict(extra='forbid', populate_by_name=True)