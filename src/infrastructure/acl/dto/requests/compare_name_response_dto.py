from pydantic import BaseModel, field_validator, RootModel


class NameResponseDto(BaseModel):
    name: str
    similarity: float

    @field_validator("similarity")
    @classmethod
    def threshold_must_be_in_valid_range(cls, v: float) -> float:
        if not 0 <= v <= 1:
            raise ValueError("Similarity must be a float between 0 and 1")
        return v


class CompareNameResponseDto(RootModel):
    root: dict[str, NameResponseDto]
