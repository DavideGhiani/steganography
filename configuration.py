from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Path settings
    cover_path: str = Field(default = "/Users/davideghiani/Git/steganography/data/to_measure/cover_originale.png", env = "COVER_PATH")
    secret_path: str = Field(default="/Users/davideghiani/Git/steganography/data/to_measure/segreto_originale.png", env= "SECRET_PATH")
    encoded_path: str = Field(default="/Users/davideghiani/Git/steganography/data/to_measure/immagine_codificata.png", env="ENCODED_IMAGE")
    recovered_path: str = Field(default="/Users/davideghiani/Git/steganography/data/to_measure/recovered_secret_image.png",
                                  env="RECOVERED_IMAGE")
    post_morph_recovered_path: str = Field(default="/Users/davideghiani/Git/steganography/data/to_measure/zoom_morph_recovered.png",
                                  env="POST_MORPH_RECOVERED")

    to_resize: str = Field(default = "/Users/davideghiani/Git/steganography/data/input_to_resize",
                           env = "TO_RESIZE")

    processed_images_path: str = Field(default = "/Users/davideghiani/Git/steganography/data/output_resize", env = "PROCESSED_IMAGES")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create a settings instance
settings = Settings()
