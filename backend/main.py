from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Dict, List, Optional
import uvicorn
import os
from datetime import datetime

from services.pdf_processor import PDFProcessor
from services.ats_analyzer import ATSAnalyzer
from services.skill_analyzer import SkillAnalyzer
from services.company_requirements import CompanyRequirements
from services.resume_builder import ResumeBuilder
from models.resume_models import ResumeAnalysis, CompanyAnalysis, ResumeRequest

app = FastAPI(
    title="AI Resume Analyzer",
    description="Advanced AI-powered resume analysis and builder tool",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
pdf_processor = PDFProcessor()
ats_analyzer = ATSAnalyzer()
skill_analyzer = SkillAnalyzer()
company_requirements = CompanyRequirements()
resume_builder = ResumeBuilder()

@app.get("/")
async def root():
    return {"message": "AI Resume Analyzer API", "version": "1.0.0"}

@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):
    """
    Analyze uploaded resume and provide comprehensive feedback
    """
    try:
        # Validate file type
        if not file.filename.lower().endswith(('.pdf', '.docx', '.doc')):
            raise HTTPException(status_code=400, detail="Only PDF and DOC files are supported")
        
        # Extract text from uploaded file
        file_content = await file.read()
        extracted_text = await pdf_processor.extract_text(file_content, file.filename)
        
        if not extracted_text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from the file")
        
        # Perform comprehensive analysis
        ats_score = await ats_analyzer.calculate_ats_score(extracted_text)
        skill_analysis = await skill_analyzer.analyze_skills(extracted_text)
        missing_components = await ats_analyzer.identify_missing_components(extracted_text)
        improvement_suggestions = await ats_analyzer.get_improvement_suggestions(extracted_text)
        
        # Prepare response
        analysis_result = {
            "ats_score": ats_score,
            "skill_analysis": skill_analysis,
            "missing_components": missing_components,
            "improvement_suggestions": improvement_suggestions,
            "extracted_text": extracted_text[:500] + "..." if len(extracted_text) > 500 else extracted_text,
            "analysis_timestamp": datetime.now().isoformat()
        }
        
        return JSONResponse(content=analysis_result)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/company-analysis")
async def analyze_for_company(file: UploadFile = File(...), company: str = ""):
    """
    Analyze resume against specific company requirements
    """
    try:
        if not company:
            raise HTTPException(status_code=400, detail="Company name is required")
        
        # Extract text from uploaded file
        file_content = await file.read()
        extracted_text = await pdf_processor.extract_text(file_content, file.filename)
        
        # Get company-specific analysis
        company_analysis = await company_requirements.analyze_for_company(extracted_text, company)
        
        return JSONResponse(content=company_analysis)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Company analysis failed: {str(e)}")

@app.get("/company-requirements/{company}")
async def get_company_requirements(company: str):
    """
    Get specific requirements for a company
    """
    try:
        requirements = await company_requirements.get_requirements(company)
        return JSONResponse(content=requirements)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get requirements: {str(e)}")

@app.post("/build-resume")
async def build_resume(resume_data: ResumeRequest):
    """
    Build a new resume using provided data and templates
    """
    try:
        resume_pdf = await resume_builder.create_resume(resume_data)
        return {"message": "Resume built successfully", "download_url": "/download-resume"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Resume building failed: {str(e)}")

@app.get("/templates")
async def get_templates():
    """
    Get available resume templates
    """
    try:
        templates = await resume_builder.get_templates()
        return JSONResponse(content=templates)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get templates: {str(e)}")

@app.get("/skill-suggestions")
async def get_skill_suggestions(industry: str = "", role: str = ""):
    """
    Get skill suggestions based on industry and role
    """
    try:
        suggestions = await skill_analyzer.get_skill_suggestions(industry, role)
        return JSONResponse(content=suggestions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get skill suggestions: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)