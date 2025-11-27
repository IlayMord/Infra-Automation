from pydantic import BaseModel,field_validator

class Machine(BaseModel):
    Name: str
    OS: str
    CPU: int
    RAM: int
    DiskSize: int

    #Validators.
    @field_validator("Name")
    def name_check(cls, value):
        value = value.strip()
        if not 2 <= len(value) <= 20:
            raise ValueError("Name must contain between 2 and 20 characters")
        return value

    @field_validator("OS")
    def os_check(cls, value):
        valid_os = ["windows","debian","ubuntu"]
        value_clean = value.strip().lower()

        if value_clean not in valid_os:
            raise ValueError(f"OS must to be one of: {valid_os}")
        return value_clean.capitalize()

    @field_validator("RAM")
    def ram_check(cls, value):
        if not 1 <= value <= 2400:
            raise ValueError("RAM must be between 1 and 2400 GB")
        return value

    @field_validator("CPU")
    def cpu_check(cls, value):
        if not 1 <= value <= 128:
            raise ValueError("CPU must be between 1 and 128 cores")
        return value
    
    @field_validator("DiskSize")
    def disksize_check(cls, value):
        if not 10 <= value <= 2000:
            raise ValueError("Disk Size must be between 10GB and 2000GB")
        return value
    
    #Convert object to dict.
    def change_to_dict(self):
        return self.model_dump()
    
