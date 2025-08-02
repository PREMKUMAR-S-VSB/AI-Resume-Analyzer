from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime

class ATSScore(BaseModel):
    overall_score: float = Field(..., ge=0, le=100, description="Overall ATS score (0-100)")
    formatting_score: float = Field(..., ge=0, le=100)
    keyword_score: float = Field(..., ge=0, le=100)
    content_score: float = Field(..., ge=0, le=100)
    readability_score: float = Field(..., ge=0, le=100)
    section_score: float = Field(..., ge=0, le=100)

class SkillCategory(BaseModel):
    category: str
    skills: List[str]
    proficiency_level: Optional[str] = None

class SkillAnalysis(BaseModel):
    identified_skills: List[SkillCategory]
    missing_skills: List[str]
    skill_recommendations: List[str]
    technical_skills: List[str]
    soft_skills: List[str]
    industry_relevant_skills: List[str]

class MissingComponent(BaseModel):
    component: str
    importance: str  # "high", "medium", "low"
    description: str
    suggestion: str

class ImprovementSuggestion(BaseModel):
    category: str
    priority: str  # "high", "medium", "low"
    suggestion: str
    impact: str
    examples: Optional[List[str]] = None

class CompanyRequirement(BaseModel):
    skill: str
    importance: str
    description: str
    alternatives: Optional[List[str]] = None

class CompanyAnalysis(BaseModel):
    company_name: str
    match_percentage: float
    required_skills: List[CompanyRequirement]
    missing_skills: List[str]
    recommendations: List[str]
    cultural_fit_score: float
    role_specific_feedback: Dict[str, Any]

class ResumeAnalysis(BaseModel):
    ats_score: ATSScore
    skill_analysis: SkillAnalysis
    missing_components: List[MissingComponent]
    improvement_suggestions: List[ImprovementSuggestion]
    extracted_text: str
    analysis_timestamp: datetime

class PersonalInfo(BaseModel):
    full_name: str
    email: str
    phone: str
    location: str
    linkedin: Optional[str] = None
    portfolio: Optional[str] = None
    github: Optional[str] = None

class Experience(BaseModel):
    company: str
    position: str
    start_date: str
    end_date: Optional[str] = None
    current: bool = False
    description: List[str]
    technologies: Optional[List[str]] = None

class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: str
    graduation_date: str
    gpa: Optional[str] = None
    honors: Optional[List[str]] = None

class Project(BaseModel):
    name: str
    description: str
    technologies: List[str]
    url: Optional[str] = None
    github_url: Optional[str] = None

class Certification(BaseModel):
    name: str
    issuer: str
    date: str
    credential_id: Optional[str] = None
    url: Optional[str] = None

class ResumeRequest(BaseModel):
    personal_info: PersonalInfo
    professional_summary: str
    experience: List[Experience]
    education: List[Education]
    skills: List[SkillCategory]
    projects: Optional[List[Project]] = None
    certifications: Optional[List[Certification]] = None
    template_id: str = "modern"
    target_role: Optional[str] = None
    target_company: Optional[str] = None

class Template(BaseModel):
    id: str
    name: str
    description: str
    preview_url: str
    category: str  # "modern", "traditional", "creative", "minimal"
    suitable_for: List[str]  # industries or roles

class SkillSuggestion(BaseModel):
    skill: str
    category: str
    importance: str
    learning_resources: List[str]
    market_demand: str  # "high", "medium", "low"