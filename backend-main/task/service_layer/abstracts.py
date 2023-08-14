import typing
import re
from pydantic import BaseModel, validator, constr, root_validator, Field


class DataModel(BaseModel):
    """base model for form data"""

    class Config:
        allow_mutation = False
        # arbitrary_types_allowed = True
        extra = "ignore"
        check_fields = False


class AddTask(DataModel):
    title: constr(strip_whitespace=True, max_length=100)
    description: constr(strip_whitespace=True)

    @root_validator(pre=True, allow_reuse=True)
    def title_must_be_valid(cls, values):
        title = values.get("title")
        if title.strip() == "" or not title or title == "":
            raise Exception("Task title cannot be empty, whitespace or null")
        if len(title) > 100:
            raise Exception("Task title cannot be greater than 150 characters")
        return values


class UpdateTask(AddTask):
    completed: bool
