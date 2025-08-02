import re
from typing import Dict, List, Set
from models.resume_models import SkillAnalysis, SkillCategory, SkillSuggestion

class SkillAnalyzer:
    def __init__(self):
        # Comprehensive skill database
        self.skill_database = {
            'programming_languages': [
                'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'php', 'ruby',
                'go', 'rust', 'swift', 'kotlin', 'scala', 'r', 'matlab', 'perl', 'bash'
            ],
            'web_technologies': [
                'html', 'css', 'react', 'angular', 'vue.js', 'node.js', 'express',
                'django', 'flask', 'spring', 'laravel', 'bootstrap', 'sass', 'less'
            ],
            'databases': [
                'mysql', 'postgresql', 'mongodb', 'redis', 'cassandra', 'oracle',
                'sql server', 'sqlite', 'elasticsearch', 'dynamodb', 'firebase'
            ],
            'cloud_platforms': [
                'aws', 'azure', 'google cloud', 'gcp', 'heroku', 'digitalocean',
                'cloudflare', 'vercel', 'netlify'
            ],
            'devops_tools': [
                'docker', 'kubernetes', 'jenkins', 'gitlab ci', 'github actions',
                'terraform', 'ansible', 'chef', 'puppet', 'vagrant', 'nginx'
            ],
            'data_science': [
                'machine learning', 'deep learning', 'neural networks', 'tensorflow',
                'pytorch', 'scikit-learn', 'pandas', 'numpy', 'matplotlib', 'seaborn',
                'tableau', 'power bi', 'spark', 'hadoop', 'kafka'
            ],
            'mobile_development': [
                'ios', 'android', 'react native', 'flutter', 'xamarin', 'cordova',
                'phonegap', 'ionic'
            ],
            'soft_skills': [
                'leadership', 'communication', 'teamwork', 'problem solving',
                'analytical thinking', 'creativity', 'adaptability', 'time management',
                'project management', 'critical thinking', 'collaboration', 'mentoring'
            ],
            'methodologies': [
                'agile', 'scrum', 'kanban', 'waterfall', 'lean', 'six sigma',
                'devops', 'ci/cd', 'tdd', 'bdd', 'microservices', 'api design'
            ],
            'design_tools': [
                'figma', 'sketch', 'adobe xd', 'photoshop', 'illustrator',
                'indesign', 'canva', 'zeplin', 'invision'
            ],
            'testing': [
                'unit testing', 'integration testing', 'selenium', 'cypress',
                'jest', 'mocha', 'junit', 'pytest', 'postman', 'api testing'
            ]
        }
        
        # Industry-specific skill requirements
        self.industry_skills = {
            'software_engineering': {
                'essential': ['programming languages', 'databases', 'web_technologies', 'testing'],
                'preferred': ['cloud_platforms', 'devops_tools', 'methodologies']
            },
            'data_science': {
                'essential': ['data_science', 'programming_languages', 'databases'],
                'preferred': ['cloud_platforms', 'methodologies']
            },
            'web_development': {
                'essential': ['web_technologies', 'programming_languages', 'databases'],
                'preferred': ['devops_tools', 'cloud_platforms', 'design_tools']
            },
            'mobile_development': {
                'essential': ['mobile_development', 'programming_languages'],
                'preferred': ['cloud_platforms', 'methodologies', 'testing']
            },
            'devops': {
                'essential': ['devops_tools', 'cloud_platforms', 'programming_languages'],
                'preferred': ['databases', 'methodologies', 'testing']
            },
            'design': {
                'essential': ['design_tools', 'soft_skills'],
                'preferred': ['web_technologies', 'methodologies']
            }
        }
        
        # Trending skills by year
        self.trending_skills = {
            '2024': [
                'artificial intelligence', 'machine learning', 'generative ai',
                'large language models', 'prompt engineering', 'kubernetes',
                'microservices', 'blockchain', 'web3', 'cybersecurity',
                'cloud security', 'edge computing', 'iot'
            ]
        }
    
    async def analyze_skills(self, text: str) -> SkillAnalysis:
        """
        Comprehensive skill analysis of resume text
        """
        text_lower = text.lower()
        
        # Identify skills by category
        identified_skills = self._identify_skills_by_category(text_lower)
        
        # Identify technical vs soft skills
        technical_skills = self._get_technical_skills(identified_skills)
        soft_skills = self._get_soft_skills(identified_skills)
        
        # Get industry-relevant skills
        industry_relevant_skills = self._get_industry_relevant_skills(identified_skills)
        
        # Identify missing skills
        missing_skills = self._identify_missing_skills(identified_skills)
        
        # Generate skill recommendations
        skill_recommendations = self._generate_skill_recommendations(identified_skills, missing_skills)
        
        return SkillAnalysis(
            identified_skills=identified_skills,
            missing_skills=missing_skills,
            skill_recommendations=skill_recommendations,
            technical_skills=technical_skills,
            soft_skills=soft_skills,
            industry_relevant_skills=industry_relevant_skills
        )
    
    def _identify_skills_by_category(self, text: str) -> List[SkillCategory]:
        """
        Identify skills present in text, grouped by category
        """
        skill_categories = []
        
        for category, skills in self.skill_database.items():
            found_skills = []
            for skill in skills:
                # Use word boundaries to avoid partial matches
                pattern = r'\b' + re.escape(skill.lower()) + r'\b'
                if re.search(pattern, text):
                    found_skills.append(skill)
            
            if found_skills:
                # Determine proficiency level based on context
                proficiency = self._determine_proficiency(text, found_skills)
                skill_categories.append(SkillCategory(
                    category=category.replace('_', ' ').title(),
                    skills=found_skills,
                    proficiency_level=proficiency
                ))
        
        return skill_categories
    
    def _determine_proficiency(self, text: str, skills: List[str]) -> str:
        """
        Determine proficiency level based on context clues
        """
        # Look for proficiency indicators around skill mentions
        proficiency_indicators = {
            'expert': ['expert', 'advanced', 'senior', 'lead', 'architect', 'mastery'],
            'intermediate': ['intermediate', 'proficient', 'experienced', 'solid'],
            'beginner': ['beginner', 'basic', 'learning', 'familiar', 'exposure']
        }
        
        for level, indicators in proficiency_indicators.items():
            for indicator in indicators:
                if indicator in text.lower():
                    return level
        
        # Default proficiency based on skill frequency
        skill_mentions = sum(text.lower().count(skill.lower()) for skill in skills)
        if skill_mentions >= 5:
            return 'experienced'
        elif skill_mentions >= 2:
            return 'intermediate'
        else:
            return 'familiar'
    
    def _get_technical_skills(self, skill_categories: List[SkillCategory]) -> List[str]:
        """
        Extract technical skills from identified skills
        """
        technical_categories = [
            'Programming Languages', 'Web Technologies', 'Databases', 
            'Cloud Platforms', 'Devops Tools', 'Data Science', 
            'Mobile Development', 'Design Tools', 'Testing'
        ]
        
        technical_skills = []
        for category in skill_categories:
            if category.category in technical_categories:
                technical_skills.extend(category.skills)
        
        return technical_skills
    
    def _get_soft_skills(self, skill_categories: List[SkillCategory]) -> List[str]:
        """
        Extract soft skills from identified skills
        """
        soft_skills = []
        for category in skill_categories:
            if category.category == 'Soft Skills':
                soft_skills.extend(category.skills)
        
        return soft_skills
    
    def _get_industry_relevant_skills(self, skill_categories: List[SkillCategory]) -> List[str]:
        """
        Get skills that are highly relevant to current industry trends
        """
        trending_skills = self.trending_skills.get('2024', [])
        identified_skill_names = []
        
        for category in skill_categories:
            identified_skill_names.extend([skill.lower() for skill in category.skills])
        
        industry_relevant = []
        for trending_skill in trending_skills:
            if trending_skill.lower() in identified_skill_names:
                industry_relevant.append(trending_skill)
        
        return industry_relevant
    
    def _identify_missing_skills(self, skill_categories: List[SkillCategory]) -> List[str]:
        """
        Identify important skills that are missing from the resume
        """
        identified_categories = {cat.category.lower().replace(' ', '_') for cat in skill_categories}
        all_skills = set()
        
        for category in skill_categories:
            all_skills.update([skill.lower() for skill in category.skills])
        
        missing_skills = []
        
        # Check for missing essential skills in common categories
        essential_skills = {
            'version_control': ['git', 'github', 'gitlab', 'bitbucket'],
            'communication': ['communication', 'presentation', 'documentation'],
            'problem_solving': ['problem solving', 'analytical thinking', 'debugging'],
            'collaboration': ['teamwork', 'collaboration', 'cross-functional']
        }
        
        for category, skills in essential_skills.items():
            if not any(skill in all_skills for skill in skills):
                missing_skills.extend(skills[:2])  # Add top 2 missing skills from category
        
        # Add trending skills if missing
        trending_skills = self.trending_skills.get('2024', [])
        for skill in trending_skills[:5]:  # Top 5 trending skills
            if skill.lower() not in all_skills:
                missing_skills.append(skill)
        
        return missing_skills[:10]  # Limit to top 10 missing skills
    
    def _generate_skill_recommendations(self, skill_categories: List[SkillCategory], missing_skills: List[str]) -> List[str]:
        """
        Generate skill improvement recommendations
        """
        recommendations = []
        
        # Get current skill distribution
        technical_count = len(self._get_technical_skills(skill_categories))
        soft_skill_count = len(self._get_soft_skills(skill_categories))
        
        # Recommend skill balance
        if technical_count > soft_skill_count * 3:
            recommendations.append("Add more soft skills like leadership, communication, and teamwork")
        elif soft_skill_count > technical_count:
            recommendations.append("Include more technical skills relevant to your field")
        
        # Recommend trending skills
        if missing_skills:
            recommendations.append(f"Consider learning trending skills: {', '.join(missing_skills[:3])}")
        
        # Category-specific recommendations
        category_names = [cat.category.lower() for cat in skill_categories]
        
        if 'programming languages' in category_names and 'cloud platforms' not in category_names:
            recommendations.append("Add cloud platform experience (AWS, Azure, Google Cloud)")
        
        if 'web technologies' in category_names and 'devops tools' not in category_names:
            recommendations.append("Include DevOps tools like Docker, Kubernetes, or CI/CD pipelines")
        
        if len(skill_categories) < 3:
            recommendations.append("Expand your skill set across multiple technology categories")
        
        return recommendations[:5]  # Limit to top 5 recommendations
    
    async def get_skill_suggestions(self, industry: str = "", role: str = "") -> Dict:
        """
        Get skill suggestions based on industry and role
        """
        suggestions = {
            'trending_skills': [],
            'role_specific_skills': [],
            'learning_resources': {},
            'skill_priorities': {}
        }
        
        # Get trending skills
        suggestions['trending_skills'] = [
            SkillSuggestion(
                skill=skill,
                category="Trending",
                importance="high",
                learning_resources=[
                    f"Online courses for {skill}",
                    f"Official {skill} documentation",
                    f"{skill} certification programs"
                ],
                market_demand="high"
            ) for skill in self.trending_skills.get('2024', [])[:5]
        ]
        
        # Get role-specific suggestions
        if role.lower() in ['software engineer', 'developer', 'programmer']:
            role_skills = self.skill_database['programming_languages'][:5] + \
                         self.skill_database['web_technologies'][:5]
        elif role.lower() in ['data scientist', 'data analyst', 'ml engineer']:
            role_skills = self.skill_database['data_science'][:7]
        elif role.lower() in ['devops', 'sre', 'platform engineer']:
            role_skills = self.skill_database['devops_tools'][:7]
        else:
            role_skills = self.skill_database['soft_skills'][:5]
        
        suggestions['role_specific_skills'] = [
            SkillSuggestion(
                skill=skill,
                category="Role-Specific",
                importance="medium",
                learning_resources=[
                    f"Practice {skill} projects",
                    f"{skill} tutorials and guides",
                    f"Join {skill} communities"
                ],
                market_demand="medium"
            ) for skill in role_skills
        ]
        
        return suggestions