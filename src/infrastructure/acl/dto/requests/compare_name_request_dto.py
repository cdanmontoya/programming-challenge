from pydantic import BaseModel, field_validator


class CompareNameRequestDto(BaseModel):
    name: str
    threshold: float | None = 0.8

    @field_validator("threshold")
    @classmethod
    def threshold_must_be_in_valid_range(cls, v: float) -> float:
        if not 0 <= v <= 1:
            raise ValueError("Threshold must be a float between 0 and 1")
        return v
