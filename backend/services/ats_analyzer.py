import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import textstat
from typing import Dict, List, Tuple
from models.resume_models import ATSScore, MissingComponent, ImprovementSuggestion

class ATSAnalyzer:
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.download('punkt', quiet=True)
            nltk.download('stopwords', quiet=True)
        except:
            pass
        
        # Common ATS keywords by category
        self.ats_keywords = {
            'action_verbs': [
                'achieved', 'developed', 'implemented', 'managed', 'led', 'created',
                'designed', 'optimized', 'improved', 'increased', 'decreased',
                'coordinated', 'supervised', 'executed', 'delivered', 'launched'
            ],
            'technical_skills': [
                'python', 'java', 'javascript', 'sql', 'html', 'css', 'react',
                'node.js', 'docker', 'kubernetes', 'aws', 'azure', 'git', 'agile',
                'machine learning', 'data analysis', 'project management'
            ],
            'soft_skills': [
                'leadership', 'communication', 'teamwork', 'problem-solving',
                'analytical', 'creative', 'detail-oriented', 'organized',
                'time management', 'adaptable', 'collaborative'
            ]
        }
        
        # Required resume sections
        self.required_sections = [
            'contact', 'summary', 'experience', 'education', 'skills'
        ]
        
        # Section patterns for detection
        self.section_patterns = {
            'contact': r'(?:contact|phone|email|address|linkedin)',
            'summary': r'(?:summary|objective|profile|about)',
            'experience': r'(?:experience|work|employment|career|professional)',
            'education': r'(?:education|academic|degree|university|college)',
            'skills': r'(?:skills|competencies|technologies|proficiencies)',
            'projects': r'(?:projects|portfolio|work samples)',
            'certifications': r'(?:certifications|certificates|licenses|credentials)'
        }
    
    async def calculate_ats_score(self, text: str) -> ATSScore:
        """
        Calculate comprehensive ATS score for resume
        """
        formatting_score = self._analyze_formatting(text)
        keyword_score = self._analyze_keywords(text)
        content_score = self._analyze_content_quality(text)
        readability_score = self._analyze_readability(text)
        section_score = self._analyze_sections(text)
        
        # Calculate overall score with weights
        overall_score = (
            formatting_score * 0.2 +
            keyword_score * 0.25 +
            content_score * 0.25 +
            readability_score * 0.15 +
            section_score * 0.15
        )
        
        return ATSScore(
            overall_score=round(overall_score, 1),
            formatting_score=round(formatting_score, 1),
            keyword_score=round(keyword_score, 1),
            content_score=round(content_score, 1),
            readability_score=round(readability_score, 1),
            section_score=round(section_score, 1)
        )
    
    def _analyze_formatting(self, text: str) -> float:
        """
        Analyze formatting quality for ATS compatibility
        """
        score = 100.0
        
        # Check for excessive special characters
        special_chars = len(re.findall(r'[^\w\s\-@.,():/\n]', text))
        if special_chars > 50:
            score -= min(20, special_chars * 0.4)
        
        # Check for proper spacing
        lines = text.split('\n')
        too_long_lines = sum(1 for line in lines if len(line) > 120)
        if too_long_lines > 5:
            score -= min(15, too_long_lines * 3)
        
        # Check for consistent formatting
        bullet_points = len(re.findall(r'[•\-\*]\s', text))
        if bullet_points > 0:
            score += 10  # Bonus for using bullet points
        
        # Check for proper email and phone formatting
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        phones = re.findall(r'(?:\+?1[-.\s]?)?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}', text)
        
        if emails:
            score += 5
        if phones:
            score += 5
        
        return max(0, min(100, score))
    
    def _analyze_keywords(self, text: str) -> float:
        """
        Analyze keyword density and relevance
        """
        text_lower = text.lower()
        total_keywords = 0
        found_keywords = 0
        
        for category, keywords in self.ats_keywords.items():
            total_keywords += len(keywords)
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    found_keywords += 1
        
        # Calculate keyword density
        keyword_density = (found_keywords / total_keywords) * 100
        
        # Bonus for action verbs
        action_verb_count = sum(1 for verb in self.ats_keywords['action_verbs'] 
                               if verb.lower() in text_lower)
        action_verb_bonus = min(20, action_verb_count * 2)
        
        return min(100, keyword_density + action_verb_bonus)
    
    def _analyze_content_quality(self, text: str) -> float:
        """
        Analyze content quality and completeness
        """
        score = 0
        
        # Length analysis
        word_count = len(text.split())
        if 300 <= word_count <= 800:
            score += 30
        elif 200 <= word_count < 300 or 800 < word_count <= 1000:
            score += 20
        else:
            score += 10
        
        # Quantifiable achievements
        numbers = len(re.findall(r'\b\d+(?:[%$]|\s*(?:percent|million|thousand|k|m))\b', text))
        score += min(25, numbers * 5)
        
        # Professional language
        sentences = sent_tokenize(text)
        if sentences:
            avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)
            if 15 <= avg_sentence_length <= 25:
                score += 20
            else:
                score += 10
        
        # Variety in vocabulary
        words = word_tokenize(text.lower())
        unique_words = set(words)
        vocabulary_ratio = len(unique_words) / len(words) if words else 0
        score += vocabulary_ratio * 25
        
        return min(100, score)
    
    def _analyze_readability(self, text: str) -> float:
        """
        Analyze readability using various metrics
        """
        try:
            # Flesch Reading Ease (higher is better, 60-70 is ideal for professional documents)
            flesch_score = textstat.flesch_reading_ease(text)
            
            # Flesch-Kincaid Grade Level (lower is better, 8-12 is ideal)
            grade_level = textstat.flesch_kincaid_grade(text)
            
            # Convert to 0-100 scale
            readability_score = 0
            
            # Flesch score component (40% weight)
            if 60 <= flesch_score <= 70:
                readability_score += 40
            elif 50 <= flesch_score < 60 or 70 < flesch_score <= 80:
                readability_score += 30
            else:
                readability_score += 20
            
            # Grade level component (30% weight)
            if 8 <= grade_level <= 12:
                readability_score += 30
            elif 6 <= grade_level < 8 or 12 < grade_level <= 15:
                readability_score += 20
            else:
                readability_score += 10
            
            # Sentence structure (30% weight)
            sentences = sent_tokenize(text)
            if sentences:
                avg_words_per_sentence = sum(len(s.split()) for s in sentences) / len(sentences)
                if 15 <= avg_words_per_sentence <= 20:
                    readability_score += 30
                elif 10 <= avg_words_per_sentence < 15 or 20 < avg_words_per_sentence <= 25:
                    readability_score += 20
                else:
                    readability_score += 10
            
            return min(100, readability_score)
        except:
            return 50  # Default score if analysis fails
    
    def _analyze_sections(self, text: str) -> float:
        """
        Analyze presence and quality of required sections
        """
        text_lower = text.lower()
        section_scores = {}
        
        for section, pattern in self.section_patterns.items():
            if re.search(pattern, text_lower):
                section_scores[section] = 1
            else:
                section_scores[section] = 0
        
        # Required sections score
        required_score = sum(section_scores[section] for section in self.required_sections)
        required_percentage = (required_score / len(self.required_sections)) * 70
        
        # Optional sections bonus
        optional_sections = ['projects', 'certifications']
        optional_score = sum(section_scores.get(section, 0) for section in optional_sections)
        optional_bonus = optional_score * 15
        
        return min(100, required_percentage + optional_bonus)
    
    async def identify_missing_components(self, text: str) -> List[MissingComponent]:
        """
        Identify missing components in the resume
        """
        missing_components = []
        text_lower = text.lower()
        
        # Check for missing sections
        for section in self.required_sections:
            pattern = self.section_patterns.get(section, '')
            if not re.search(pattern, text_lower):
                importance = "high" if section in ['contact', 'experience'] else "medium"
                missing_components.append(MissingComponent(
                    component=section.title() + " Section",
                    importance=importance,
                    description=f"No {section} section found in the resume",
                    suggestion=f"Add a dedicated {section} section with relevant information"
                ))
        
        # Check for specific missing elements
        if not re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text):
            missing_components.append(MissingComponent(
                component="Email Address",
                importance="high",
                description="No email address found",
                suggestion="Include a professional email address in your contact information"
            ))
        
        if not re.search(r'(?:\+?1[-.\s]?)?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}', text):
            missing_components.append(MissingComponent(
                component="Phone Number",
                importance="high",
                description="No phone number found",
                suggestion="Include a phone number in your contact information"
            ))
        
        # Check for quantifiable achievements
        numbers = re.findall(r'\b\d+(?:[%$]|\s*(?:percent|million|thousand|k|m))\b', text)
        if len(numbers) < 3:
            missing_components.append(MissingComponent(
                component="Quantifiable Achievements",
                importance="medium",
                description="Limited quantifiable achievements found",
                suggestion="Include specific numbers, percentages, and metrics to demonstrate impact"
            ))
        
        # Check for action verbs
        action_verbs_found = sum(1 for verb in self.ats_keywords['action_verbs'] 
                                if verb.lower() in text_lower)
        if action_verbs_found < 5:
            missing_components.append(MissingComponent(
                component="Action Verbs",
                importance="medium",
                description="Limited use of strong action verbs",
                suggestion="Use more action verbs like 'achieved', 'developed', 'implemented' to describe your experience"
            ))
        
        return missing_components
    
    async def get_improvement_suggestions(self, text: str) -> List[ImprovementSuggestion]:
        """
        Generate improvement suggestions based on analysis
        """
        suggestions = []
        text_lower = text.lower()
        
        # Analyze word count
        word_count = len(text.split())
        if word_count < 300:
            suggestions.append(ImprovementSuggestion(
                category="Content Length",
                priority="high",
                suggestion="Your resume is too short. Expand on your experiences and achievements.",
                impact="ATS systems prefer resumes with sufficient detail (300-800 words)",
                examples=["Add more bullet points under each job", "Include project descriptions", "Expand on your achievements"]
            ))
        elif word_count > 800:
            suggestions.append(ImprovementSuggestion(
                category="Content Length",
                priority="medium",
                suggestion="Your resume might be too long. Consider condensing information.",
                impact="Keep it concise while maintaining important details",
                examples=["Remove redundant information", "Combine similar achievements", "Focus on most relevant experiences"]
            ))
        
        # Check for passive voice
        passive_indicators = ['was', 'were', 'been', 'being']
        passive_count = sum(text_lower.count(word) for word in passive_indicators)
        if passive_count > 10:
            suggestions.append(ImprovementSuggestion(
                category="Writing Style",
                priority="medium",
                suggestion="Reduce use of passive voice and use more active language.",
                impact="Active voice makes your accomplishments more impactful",
                examples=["'Led a team' instead of 'Was responsible for leading'", "'Developed software' instead of 'Software was developed'"]
            ))
        
        # Check for keywords
        keyword_score = self._analyze_keywords(text)
        if keyword_score < 50:
            suggestions.append(ImprovementSuggestion(
                category="Keywords",
                priority="high",
                suggestion="Include more industry-relevant keywords and skills.",
                impact="ATS systems scan for specific keywords related to the job",
                examples=["Add technical skills", "Include industry buzzwords", "Use job posting keywords"]
            ))
        
        # Check for formatting issues
        if len(re.findall(r'[^\w\s\-@.,():/\n]', text)) > 50:
            suggestions.append(ImprovementSuggestion(
                category="Formatting",
                priority="medium",
                suggestion="Simplify formatting by removing excessive special characters.",
                impact="Clean formatting improves ATS readability",
                examples=["Use simple bullet points", "Avoid complex symbols", "Use standard fonts"]
            ))
        
        return suggestions