# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import Extra,  BaseModel, Field, conint, constr, validator

class ActiveLearningScoreTypesV2Data(BaseModel):
    """
    ActiveLearningScoreTypesV2Data
    """
    id: constr(strict=True) = Field(..., description="MongoDB ObjectId")
    dataset_id: constr(strict=True) = Field(..., alias="datasetId", description="MongoDB ObjectId")
    prediction_uuid_timestamp: conint(strict=True, ge=0) = Field(..., alias="predictionUUIDTimestamp", description="unix timestamp in milliseconds")
    task_name: constr(strict=True) = Field(..., alias="taskName", description="Since we sometimes stitch together SelectionInputTask+ActiveLearningScoreType, they need to follow the same specs of ActiveLearningScoreType. However, this can be an empty string due to internal logic (no minLength). Also v2config.filespecs.ts has this pattern for predictionTaskJSONSchema as well. ")
    score_type: constr(strict=True, min_length=1) = Field(..., alias="scoreType", description="Type of active learning score")
    created_at: conint(strict=True, ge=0) = Field(..., alias="createdAt", description="unix timestamp in milliseconds")
    __properties = ["id", "datasetId", "predictionUUIDTimestamp", "taskName", "scoreType", "createdAt"]

    @validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-f0-9]{24}$", value):
            raise ValueError(r"must validate the regular expression /^[a-f0-9]{24}$/")
        return value

    @validator('dataset_id')
    def dataset_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-f0-9]{24}$", value):
            raise ValueError(r"must validate the regular expression /^[a-f0-9]{24}$/")
        return value

    @validator('task_name')
    def task_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9_+=,.@:\/-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_+=,.@:\/-]*$/")
        return value

    @validator('score_type')
    def score_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9_+=,.@:\/-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_+=,.@:\/-]*$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True
        use_enum_values = True
        extra = Extra.forbid

    def to_str(self, by_alias: bool = False) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.dict(by_alias=by_alias))

    def to_json(self, by_alias: bool = False) -> str:
        """Returns the JSON representation of the model"""
        return json.dumps(self.to_dict(by_alias=by_alias))

    @classmethod
    def from_json(cls, json_str: str) -> ActiveLearningScoreTypesV2Data:
        """Create an instance of ActiveLearningScoreTypesV2Data from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        _dict = self.dict(by_alias=by_alias,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActiveLearningScoreTypesV2Data:
        """Create an instance of ActiveLearningScoreTypesV2Data from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActiveLearningScoreTypesV2Data.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ActiveLearningScoreTypesV2Data) in the input: " + str(obj))

        _obj = ActiveLearningScoreTypesV2Data.parse_obj({
            "id": obj.get("id"),
            "dataset_id": obj.get("datasetId"),
            "prediction_uuid_timestamp": obj.get("predictionUUIDTimestamp"),
            "task_name": obj.get("taskName"),
            "score_type": obj.get("scoreType"),
            "created_at": obj.get("createdAt")
        })
        return _obj

