from dataclasses import dataclass

@dataclass
class Image:
    title: str
    access_link: str
    img_link : str
    site: str
    author: str
    alt: str
    format: str