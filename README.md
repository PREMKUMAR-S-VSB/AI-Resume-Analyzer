# AI Resume Analyzer & Builder

A comprehensive AI-powered resume analysis and building platform that provides real-time ATS scores, company-specific insights, and professional resume templates.

## 🚀 Features

### 📊 AI Resume Analysis
- **Real-time ATS Scoring**: Get instant feedback on how well your resume will perform with Applicant Tracking Systems
- **Detailed Score Breakdown**: Separate scores for formatting, keywords, content quality, readability, and section structure
- **Missing Components Detection**: Identify what essential elements your resume is missing
- **Improvement Suggestions**: Get actionable recommendations to enhance your resume

### 🏢 Company-Specific Analysis
- **Target Company Analysis**: Tailor your resume for specific companies (Google, Microsoft, Amazon, Meta, Apple, Netflix)
- **Cultural Fit Score**: Understand how well your experience aligns with company values
- **Technical Skills Matching**: See which company-specific technologies you have or need
- **Personalized Recommendations**: Get advice specific to your target company's requirements

### 🎨 Professional Resume Builder
- **Multiple Templates**: Choose from Modern, Traditional, Creative, Minimal, and Executive layouts
- **AI-Powered Suggestions**: Get intelligent recommendations for content and formatting
- **Real-time Preview**: See your resume as you build it
- **PDF Export**: Download professional-quality PDF resumes

### 🔍 Skill Gap Analysis
- **Skill Identification**: Automatically detect technical and soft skills from your resume
- **Industry Trends**: Get insights on trending skills in your field
- **Learning Recommendations**: Receive suggestions for skills to develop
- **Skill Categorization**: Organize skills by category and proficiency level

## 🛠️ Tech Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **PyPDF2**: PDF text extraction
- **python-docx**: Word document processing
- **NLTK**: Natural language processing
- **scikit-learn**: Machine learning for text analysis
- **ReportLab**: PDF generation for resume building
- **Pydantic**: Data validation and serialization

### Frontend
- **React 18**: Modern frontend framework
- **Tailwind CSS**: Utility-first CSS framework
- **React Router**: Client-side routing
- **Axios**: HTTP client for API requests
- **React Dropzone**: File upload handling
- **Lucide React**: Beautiful icons
- **Framer Motion**: Smooth animations

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/resume-analyzer.git
   cd resume-analyzer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data**
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

5. **Start the backend server**
   ```bash
   cd backend
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. **Install Node.js dependencies**
   ```bash
   npm install
   ```

2. **Start the development server**
   ```bash
   npm start
   ```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 📚 API Documentation

### Main Endpoints

#### Resume Analysis
```http
POST /analyze-resume
Content-Type: multipart/form-data

# Upload a PDF or DOCX file for analysis
```

#### Company Analysis
```http
POST /company-analysis
Content-Type: multipart/form-data

# Analyze resume against specific company requirements
```

#### Resume Building
```http
POST /build-resume
Content-Type: application/json

# Generate a PDF resume from structured data
```

#### Templates
```http
GET /templates
# Get available resume templates
```

#### Skill Suggestions
```http
GET /skill-suggestions?industry=tech&role=developer
# Get skill recommendations for specific roles
```

## 🏗️ Project Structure

```
resume-analyzer/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── models/
│   │   └── resume_models.py    # Pydantic models
│   └── services/
│       ├── pdf_processor.py    # PDF/DOCX text extraction
│       ├── ats_analyzer.py     # ATS scoring algorithms
│       ├── skill_analyzer.py   # Skill analysis and recommendations
│       ├── company_requirements.py  # Company-specific analysis
│       └── resume_builder.py   # Resume generation
├── src/
│   ├── components/
│   │   ├── Header.js           # Navigation header
│   │   └── Footer.js           # Site footer
│   ├── pages/
│   │   ├── Home.js             # Landing page
│   │   ├── Analyzer.js         # Resume analysis interface
│   │   ├── Builder.js          # Resume builder
│   │   ├── CompanyAnalysis.js  # Company-specific analysis
│   │   └── Templates.js        # Template showcase
│   ├── App.js                  # Main React component
│   └── App.css                 # Global styles
├── public/
├── requirements.txt            # Python dependencies
├── package.json               # Node.js dependencies
├── tailwind.config.js         # Tailwind configuration
└── README.md
```

## 🎯 Key Features Explained

### ATS Scoring Algorithm
Our AI analyzer evaluates resumes across multiple dimensions:

1. **Formatting Score (20% weight)**
   - Font compatibility
   - Section organization
   - White space usage
   - Bullet point consistency

2. **Keyword Score (25% weight)**
   - Industry-relevant keywords
   - Action verbs usage
   - Technical skills presence
   - Role-specific terminology

3. **Content Quality (25% weight)**
   - Quantifiable achievements
   - Professional language
   - Vocabulary variety
   - Length optimization

4. **Readability (15% weight)**
   - Flesch reading ease
   - Sentence structure
   - Grade level appropriateness

5. **Section Structure (15% weight)**
   - Required sections presence
   - Logical organization
   - Complete information

### Company Analysis
We maintain detailed profiles for major tech companies including:

- **Technical Requirements**: Specific technologies and skills
- **Cultural Values**: Company-specific soft skills and values
- **Experience Expectations**: Seniority and background preferences
- **Industry Focus**: Specialized knowledge areas

### Resume Templates
Our templates are designed by professionals and optimized for:

- **ATS Compatibility**: Clean formatting that ATS systems can parse
- **Visual Appeal**: Modern designs that stand out to human reviewers
- **Industry Appropriateness**: Different styles for different fields
- **Customization**: Easy to modify and personalize

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the backend directory:

```env
# Optional: OpenAI API key for enhanced analysis
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Custom company requirements
CUSTOM_COMPANIES_PATH=./data/custom_companies.json

# Optional: Analytics tracking
ANALYTICS_ENABLED=false
```

### Custom Company Requirements
You can add custom company requirements by creating a JSON file:

```json
{
  "your_company": {
    "technical_skills": [
      {"skill": "Python", "importance": "high", "description": "Primary language"}
    ],
    "soft_skills": [
      {"skill": "Leadership", "importance": "medium", "description": "Team leadership"}
    ],
    "cultural_values": ["Innovation", "Collaboration"],
    "education": "Bachelor's degree preferred",
    "experience_level": "3+ years experience"
  }
}
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
python -m pytest tests/ -v
```

### Frontend Tests
```bash
npm test
```

### End-to-End Tests
```bash
npm run test:e2e
```

## 🚀 Deployment

### Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

### Manual Deployment

1. **Backend (FastAPI)**
   ```bash
   pip install gunicorn
   gunicorn backend.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
   ```

2. **Frontend (React)**
   ```bash
   npm run build
   # Serve the build folder with your preferred web server
   ```

### Environment-Specific Configurations

- **Development**: Use `npm start` and `uvicorn --reload`
- **Production**: Use optimized builds and proper web servers
- **Docker**: Use provided `Dockerfile` and `docker-compose.yml`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint and Prettier for JavaScript code
- Write tests for new features
- Update documentation for API changes
- Ensure mobile responsiveness for UI changes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for inspiring AI-powered text analysis
- **Tailwind CSS** for the amazing utility-first CSS framework
- **FastAPI** for the high-performance Python web framework
- **React** team for the excellent frontend framework

## 📞 Support

- **Documentation**: Check this README and inline code comments
- **Issues**: Open an issue on GitHub for bugs or feature requests
- **Contact**: email@your-domain.com

## 🔄 Changelog

### Version 1.0.0 (Current)
- ✅ AI-powered resume analysis with ATS scoring
- ✅ Company-specific requirement analysis
- ✅ Professional resume builder with multiple templates
- ✅ Skill gap analysis and recommendations
- ✅ Modern React frontend with responsive design
- ✅ FastAPI backend with comprehensive API

### Planned Features
- 🔄 Integration with job boards
- 🔄 Advanced AI recommendations using GPT
- 🔄 Resume optimization suggestions
- 🔄 Career path recommendations
- 🔄 Interview preparation tools

---

**Built with ❤️ for job seekers worldwide**