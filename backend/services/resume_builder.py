from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import io
from typing import Dict, List
from models.resume_models import ResumeRequest, Template

class ResumeBuilder:
    def __init__(self):
        self.templates = {
            'modern': {
                'id': 'modern',
                'name': 'Modern Professional',
                'description': 'Clean and modern design with accent colors',
                'category': 'modern',
                'suitable_for': ['Software Engineering', 'Data Science', 'Design', 'Marketing']
            },
            'traditional': {
                'id': 'traditional',
                'name': 'Classic Traditional',
                'description': 'Traditional black and white professional format',
                'category': 'traditional',
                'suitable_for': ['Finance', 'Legal', 'Healthcare', 'Education']
            },
            'creative': {
                'id': 'creative',
                'name': 'Creative Designer',
                'description': 'Bold and creative layout for creative professionals',
                'category': 'creative',
                'suitable_for': ['Graphic Design', 'Marketing', 'Media', 'Arts']
            },
            'minimal': {
                'id': 'minimal',
                'name': 'Minimal Clean',
                'description': 'Minimalist design focusing on content',
                'category': 'minimal',
                'suitable_for': ['Research', 'Academia', 'Consulting', 'Engineering']
            },
            'executive': {
                'id': 'executive',
                'name': 'Executive Leadership',
                'description': 'Professional layout for senior positions',
                'category': 'executive',
                'suitable_for': ['Management', 'Executive', 'Leadership', 'Business']
            }
        }
        
        # Color schemes for different templates
        self.color_schemes = {
            'modern': {
                'primary': colors.Color(0.2, 0.4, 0.8),  # Blue
                'secondary': colors.Color(0.3, 0.3, 0.3),  # Dark gray
                'accent': colors.Color(0.8, 0.8, 0.8)  # Light gray
            },
            'traditional': {
                'primary': colors.black,
                'secondary': colors.Color(0.3, 0.3, 0.3),
                'accent': colors.Color(0.7, 0.7, 0.7)
            },
            'creative': {
                'primary': colors.Color(0.8, 0.2, 0.4),  # Red
                'secondary': colors.Color(0.2, 0.6, 0.8),  # Blue
                'accent': colors.Color(0.9, 0.9, 0.9)
            },
            'minimal': {
                'primary': colors.Color(0.1, 0.1, 0.1),
                'secondary': colors.Color(0.5, 0.5, 0.5),
                'accent': colors.Color(0.9, 0.9, 0.9)
            },
            'executive': {
                'primary': colors.Color(0.1, 0.2, 0.4),  # Navy
                'secondary': colors.Color(0.4, 0.4, 0.4),
                'accent': colors.Color(0.8, 0.8, 0.8)
            }
        }
    
    async def create_resume(self, resume_data: ResumeRequest) -> bytes:
        """
        Create a PDF resume from the provided data
        """
        try:
            # Create PDF buffer
            buffer = io.BytesIO()
            
            # Get template configuration
            template_id = resume_data.template_id
            if template_id not in self.templates:
                template_id = 'modern'  # Default template
            
            # Create PDF document
            doc = SimpleDocTemplate(
                buffer,
                pagesize=letter,
                rightMargin=0.5*inch,
                leftMargin=0.5*inch,
                topMargin=0.5*inch,
                bottomMargin=0.5*inch
            )
            
            # Build resume content based on template
            if template_id == 'modern':
                content = self._build_modern_template(resume_data)
            elif template_id == 'traditional':
                content = self._build_traditional_template(resume_data)
            elif template_id == 'creative':
                content = self._build_creative_template(resume_data)
            elif template_id == 'minimal':
                content = self._build_minimal_template(resume_data)
            elif template_id == 'executive':
                content = self._build_executive_template(resume_data)
            else:
                content = self._build_modern_template(resume_data)
            
            # Build PDF
            doc.build(content)
            
            # Get PDF bytes
            pdf_bytes = buffer.getvalue()
            buffer.close()
            
            return pdf_bytes
            
        except Exception as e:
            raise Exception(f"Resume creation failed: {str(e)}")
    
    def _build_modern_template(self, data: ResumeRequest) -> List:
        """
        Build modern template layout
        """
        content = []
        styles = getSampleStyleSheet()
        colors_scheme = self.color_schemes['modern']
        
        # Custom styles
        header_style = ParagraphStyle(
            'CustomHeader',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors_scheme['primary'],
            spaceAfter=12,
            alignment=TA_CENTER
        )
        
        subheader_style = ParagraphStyle(
            'CustomSubHeader',
            parent=styles['Heading2'],
            fontSize=14,
            textColor=colors_scheme['primary'],
            spaceBefore=16,
            spaceAfter=8,
            borderWidth=1,
            borderColor=colors_scheme['accent'],
            borderPadding=8
        )
        
        contact_style = ParagraphStyle(
            'ContactStyle',
            parent=styles['Normal'],
            fontSize=10,
            alignment=TA_CENTER,
            spaceAfter=12
        )
        
        # Header - Name and Contact
        content.append(Paragraph(data.personal_info.full_name, header_style))
        
        contact_info = f"{data.personal_info.email} | {data.personal_info.phone} | {data.personal_info.location}"
        if data.personal_info.linkedin:
            contact_info += f" | {data.personal_info.linkedin}"
        content.append(Paragraph(contact_info, contact_style))
        
        content.append(Spacer(1, 0.2*inch))
        
        # Professional Summary
        content.append(Paragraph("PROFESSIONAL SUMMARY", subheader_style))
        content.append(Paragraph(data.professional_summary, styles['Normal']))
        content.append(Spacer(1, 0.15*inch))
        
        # Experience
        content.append(Paragraph("PROFESSIONAL EXPERIENCE", subheader_style))
        for exp in data.experience:
            # Job header
            job_header = f"<b>{exp.position}</b> | {exp.company}"
            if exp.current:
                date_range = f"{exp.start_date} - Present"
            else:
                date_range = f"{exp.start_date} - {exp.end_date or 'Present'}"
            
            content.append(Paragraph(job_header, styles['Normal']))
            content.append(Paragraph(date_range, styles['Normal']))
            
            # Job description
            for desc in exp.description:
                content.append(Paragraph(f"• {desc}", styles['Normal']))
            
            content.append(Spacer(1, 0.1*inch))
        
        # Education
        content.append(Paragraph("EDUCATION", subheader_style))
        for edu in data.education:
            edu_text = f"<b>{edu.degree} in {edu.field_of_study}</b><br/>{edu.institution} | {edu.graduation_date}"
            if edu.gpa:
                edu_text += f" | GPA: {edu.gpa}"
            content.append(Paragraph(edu_text, styles['Normal']))
            content.append(Spacer(1, 0.1*inch))
        
        # Skills
        content.append(Paragraph("TECHNICAL SKILLS", subheader_style))
        for skill_category in data.skills:
            skills_text = f"<b>{skill_category.category}:</b> {', '.join(skill_category.skills)}"
            content.append(Paragraph(skills_text, styles['Normal']))
        
        # Projects (if any)
        if data.projects:
            content.append(Spacer(1, 0.15*inch))
            content.append(Paragraph("PROJECTS", subheader_style))
            for project in data.projects:
                project_header = f"<b>{project.name}</b>"
                if project.url:
                    project_header += f" | <link href='{project.url}'>{project.url}</link>"
                content.append(Paragraph(project_header, styles['Normal']))
                content.append(Paragraph(project.description, styles['Normal']))
                if project.technologies:
                    tech_text = f"Technologies: {', '.join(project.technologies)}"
                    content.append(Paragraph(tech_text, styles['Normal']))
                content.append(Spacer(1, 0.1*inch))
        
        # Certifications (if any)
        if data.certifications:
            content.append(Spacer(1, 0.15*inch))
            content.append(Paragraph("CERTIFICATIONS", subheader_style))
            for cert in data.certifications:
                cert_text = f"<b>{cert.name}</b> | {cert.issuer} | {cert.date}"
                content.append(Paragraph(cert_text, styles['Normal']))
        
        return content
    
    def _build_traditional_template(self, data: ResumeRequest) -> List:
        """
        Build traditional template layout
        """
        content = []
        styles = getSampleStyleSheet()
        
        # Traditional black and white styling
        header_style = ParagraphStyle(
            'TraditionalHeader',
            parent=styles['Heading1'],
            fontSize=20,
            textColor=colors.black,
            spaceAfter=6,
            alignment=TA_CENTER
        )
        
        section_style = ParagraphStyle(
            'TraditionalSection',
            parent=styles['Heading2'],
            fontSize=12,
            textColor=colors.black,
            spaceBefore=12,
            spaceAfter=6,
            borderWidth=0,
            underlineWidth=1,
            underlineColor=colors.black
        )
        
        # Header
        content.append(Paragraph(data.personal_info.full_name.upper(), header_style))
        
        contact_info = f"{data.personal_info.email} • {data.personal_info.phone} • {data.personal_info.location}"
        content.append(Paragraph(contact_info, styles['Normal']))
        content.append(Spacer(1, 0.2*inch))
        
        # Objective/Summary
        content.append(Paragraph("OBJECTIVE", section_style))
        content.append(Paragraph(data.professional_summary, styles['Normal']))
        content.append(Spacer(1, 0.15*inch))
        
        # Experience
        content.append(Paragraph("EXPERIENCE", section_style))
        for exp in data.experience:
            job_line = f"{exp.position}, {exp.company}"
            date_line = f"{exp.start_date} - {'Present' if exp.current else exp.end_date or 'Present'}"
            
            content.append(Paragraph(f"<b>{job_line}</b>", styles['Normal']))
            content.append(Paragraph(date_line, styles['Normal']))
            
            for desc in exp.description:
                content.append(Paragraph(f"• {desc}", styles['Normal']))
            content.append(Spacer(1, 0.1*inch))
        
        # Education
        content.append(Paragraph("EDUCATION", section_style))
        for edu in data.education:
            content.append(Paragraph(f"<b>{edu.degree}, {edu.field_of_study}</b>", styles['Normal']))
            content.append(Paragraph(f"{edu.institution}, {edu.graduation_date}", styles['Normal']))
            if edu.gpa:
                content.append(Paragraph(f"GPA: {edu.gpa}", styles['Normal']))
            content.append(Spacer(1, 0.1*inch))
        
        # Skills
        content.append(Paragraph("SKILLS", section_style))
        all_skills = []
        for skill_category in data.skills:
            all_skills.extend(skill_category.skills)
        content.append(Paragraph(', '.join(all_skills), styles['Normal']))
        
        return content
    
    def _build_creative_template(self, data: ResumeRequest) -> List:
        """
        Build creative template with colors and modern styling
        """
        content = []
        styles = getSampleStyleSheet()
        colors_scheme = self.color_schemes['creative']
        
        # Creative styling with colors
        name_style = ParagraphStyle(
            'CreativeName',
            parent=styles['Heading1'],
            fontSize=28,
            textColor=colors_scheme['primary'],
            spaceAfter=8,
            alignment=TA_CENTER
        )
        
        section_style = ParagraphStyle(
            'CreativeSection',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors_scheme['secondary'],
            spaceBefore=16,
            spaceAfter=8,
            borderWidth=2,
            borderColor=colors_scheme['primary'],
            borderPadding=6,
            backColor=colors_scheme['accent']
        )
        
        # Header with creative styling
        content.append(Paragraph(data.personal_info.full_name, name_style))
        
        # Contact in a styled box
        contact_data = [
            [data.personal_info.email, data.personal_info.phone],
            [data.personal_info.location, data.personal_info.linkedin or '']
        ]
        
        contact_table = Table(contact_data, colWidths=[3*inch, 3*inch])
        contact_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors_scheme['primary']),
            ('BACKGROUND', (0, 0), (-1, -1), colors_scheme['accent'])
        ]))
        
        content.append(contact_table)
        content.append(Spacer(1, 0.2*inch))
        
        # Summary with creative styling
        content.append(Paragraph("✦ ABOUT ME ✦", section_style))
        content.append(Paragraph(data.professional_summary, styles['Normal']))
        
        # Continue with other sections using similar creative styling...
        # (Implementation continues with experience, education, skills, etc.)
        
        return content
    
    def _build_minimal_template(self, data: ResumeRequest) -> List:
        """
        Build minimal clean template
        """
        content = []
        styles = getSampleStyleSheet()
        
        # Minimal styling
        name_style = ParagraphStyle(
            'MinimalName',
            parent=styles['Normal'],
            fontSize=22,
            textColor=colors.black,
            spaceAfter=6,
            alignment=TA_LEFT
        )
        
        section_style = ParagraphStyle(
            'MinimalSection',
            parent=styles['Normal'],
            fontSize=12,
            textColor=colors.black,
            spaceBefore=16,
            spaceAfter=8,
            borderWidth=0,
            underlineWidth=0.5,
            underlineColor=colors.black
        )
        
        # Simple header
        content.append(Paragraph(data.personal_info.full_name, name_style))
        content.append(Paragraph(f"{data.personal_info.email} | {data.personal_info.phone}", styles['Normal']))
        content.append(Spacer(1, 0.2*inch))
        
        # Clean sections
        content.append(Paragraph("Summary", section_style))
        content.append(Paragraph(data.professional_summary, styles['Normal']))
        
        # Continue with minimal styling for other sections...
        
        return content
    
    def _build_executive_template(self, data: ResumeRequest) -> List:
        """
        Build executive template for senior positions
        """
        content = []
        styles = getSampleStyleSheet()
        colors_scheme = self.color_schemes['executive']
        
        # Executive styling - professional and authoritative
        name_style = ParagraphStyle(
            'ExecutiveName',
            parent=styles['Heading1'],
            fontSize=26,
            textColor=colors_scheme['primary'],
            spaceAfter=8,
            alignment=TA_CENTER
        )
        
        title_style = ParagraphStyle(
            'ExecutiveTitle',
            parent=styles['Normal'],
            fontSize=14,
            textColor=colors_scheme['secondary'],
            spaceAfter=12,
            alignment=TA_CENTER
        )
        
        # Header with executive positioning
        content.append(Paragraph(data.personal_info.full_name, name_style))
        
        # Add a professional title if target role is specified
        if data.target_role:
            content.append(Paragraph(data.target_role, title_style))
        
        # Professional contact layout
        contact_info = f"{data.personal_info.email} | {data.personal_info.phone} | {data.personal_info.location}"
        if data.personal_info.linkedin:
            contact_info += f" | {data.personal_info.linkedin}"
        content.append(Paragraph(contact_info, styles['Normal']))
        
        # Continue with executive-focused layout...
        
        return content
    
    async def get_templates(self) -> List[Dict]:
        """
        Get all available resume templates
        """
        return [
            {
                **template_data,
                'preview_url': f'/api/templates/{template_id}/preview'
            }
            for template_id, template_data in self.templates.items()
        ]
    
    def get_template_by_id(self, template_id: str) -> Dict:
        """
        Get specific template configuration
        """
        return self.templates.get(template_id, self.templates['modern'])
    
    def suggest_template(self, target_role: str = "", target_company: str = "") -> str:
        """
        Suggest best template based on role and company
        """
        role_lower = target_role.lower()
        company_lower = target_company.lower()
        
        # Company-specific preferences
        if company_lower in ['google', 'meta', 'microsoft', 'amazon']:
            return 'modern'
        elif company_lower in ['apple', 'netflix']:
            return 'minimal'
        elif company_lower in ['goldman sachs', 'jpmorgan', 'deloitte']:
            return 'traditional'
        
        # Role-specific preferences
        if any(keyword in role_lower for keyword in ['designer', 'creative', 'marketing']):
            return 'creative'
        elif any(keyword in role_lower for keyword in ['ceo', 'cto', 'vp', 'director', 'manager']):
            return 'executive'
        elif any(keyword in role_lower for keyword in ['researcher', 'scientist', 'academic']):
            return 'minimal'
        elif any(keyword in role_lower for keyword in ['finance', 'legal', 'consultant']):
            return 'traditional'
        else:
            return 'modern'  # Default for tech roles