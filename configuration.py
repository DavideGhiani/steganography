from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Path settings
    cover_path: str = Field(deafult = "/Users/davideghiani/Git/steganography/data/cover_image.png",env = "COVER_PATH")
    secret_path: str = Field(deafult="/Users/davideghiani/Git/steganography/data/originale.png", env="SECRET_PATH")
    recovered_path_1: str = Field(deafult="/Users/davideghiani/Git/steganography/data/recovered_errata.png",
                                  env="RECOVERED_PATH_1")
    recovered_path_2: str = Field(deafult = "/Users/davideghiani/Git/steganography/data/stego_recovered_correct.png",
                                  env = "RECOVERED_PATH_2")
    recovered_path_3: str = Field(deafult = "/Users/davideghiani/Git/steganography/data/stegomodif_recovered.png",
                                  env = "RECOVERED_PATH_3")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create a settings instance
settings = Settings()