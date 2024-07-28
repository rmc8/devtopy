from typing import Optional, List

from pydantic import BaseModel, HttpUrl, Field


class ErrorResponse(BaseModel):
    error: str
    status: int


class User(BaseModel):
    name: str
    username: str
    twitter_username: Optional[str] = None
    github_username: Optional[str] = None
    user_id: int
    website_url: Optional[HttpUrl] = None
    profile_image: str
    profile_image_90: str


class Organization(BaseModel):
    name: str
    username: str
    slug: str
    profile_image: str
    profile_image_90: str


class FlareTag(BaseModel):
    name: str
    bg_color_hes: Optional[str] = None
    text_color_hex: str


class Article(BaseModel):
    type_of: str
    id: int
    title: str
    description: str
    readable_publish_date: Optional[str] = None
    slug: str
    path: str
    url: HttpUrl
    comments_count: int
    public_reactions_count: int
    collection_id: Optional[int] = None
    published_timestamp: Optional[str] = Field(default=None)
    positive_reactions_count: int
    cover_image: Optional[HttpUrl] = None
    social_image: HttpUrl
    canonical_url: HttpUrl
    created_at: str
    edited_at: Optional[str] = None
    crossposted_at: Optional[str] = None
    published_at: Optional[str] = None
    last_comment_at: str
    reading_time_minutes: int
    tag_list: str
    tags: List[str]
    body_html: str
    body_markdown: str
    user: User
    organization: Optional[Organization] = None
    flare_tag: Optional[FlareTag] = None


class PublishedArticle(BaseModel):
    type_of: str
    id: int
    title: str
    description: str
    readable_publish_date: Optional[str] = None
    slug: str
    path: str
    url: HttpUrl
    comments_count: int
    public_reactions_count: int
    collection_id: Optional[int] = None
    published_timestamp: str
    positive_reactions_count: int
    cover_image: Optional[HttpUrl] = None
    social_image: Optional[HttpUrl] = None
    canonical_url: HttpUrl
    created_at: Optional[str] = None
    edited_at: Optional[str] = None
    crossposted_at: Optional[str] = None
    published_at: Optional[str] = None
    last_comment_at: Optional[str] = None
    reading_time_minutes: int
    tag_list: List[str]
    tags: Optional[str] = None
    user: User
    organization: Optional[Organization] = None
    flare_tag: Optional[FlareTag] = None


class PublishedArticleList(BaseModel):
    articles: List[PublishedArticle]
