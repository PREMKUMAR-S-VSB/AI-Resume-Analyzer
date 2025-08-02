import re
from typing import Dict, List
from models.resume_models import CompanyAnalysis, CompanyRequirement

class CompanyRequirements:
    def __init__(self):
        # Company-specific requirements database
        self.company_requirements = {
            'google': {
                'technical_skills': [
                    {'skill': 'Python', 'importance': 'high', 'description': 'Primary programming language'},
                    {'skill': 'Java', 'importance': 'high', 'description': 'Core backend development'},
                    {'skill': 'C++', 'importance': 'medium', 'description': 'Systems programming'},
                    {'skill': 'Machine Learning', 'importance': 'high', 'description': 'AI/ML initiatives'},
                    {'skill': 'Distributed Systems', 'importance': 'high', 'description': 'Large-scale systems'},
                    {'skill': 'Google Cloud Platform', 'importance': 'high', 'description': 'Cloud infrastructure'},
                    {'skill': 'Kubernetes', 'importance': 'medium', 'description': 'Container orchestration'},
                    {'skill': 'TensorFlow', 'importance': 'medium', 'description': 'ML framework'},
                ],
                'soft_skills': [
                    {'skill': 'Problem Solving', 'importance': 'high', 'description': 'Complex algorithmic thinking'},
                    {'skill': 'Collaboration', 'importance': 'high', 'description': 'Cross-functional teamwork'},
                    {'skill': 'Innovation', 'importance': 'high', 'description': 'Creative problem solving'},
                    {'skill': 'Leadership', 'importance': 'medium', 'description': 'Technical leadership'},
                ],
                'cultural_values': ['Innovation', 'User Focus', 'Boldness', 'Collaboration'],
                'education': 'Computer Science or related field preferred',
                'experience_level': 'Strong algorithmic and data structure knowledge'
            },
            'microsoft': {
                'technical_skills': [
                    {'skill': 'C#', 'importance': 'high', 'description': '.NET ecosystem'},
                    {'skill': 'Azure', 'importance': 'high', 'description': 'Cloud platform'},
                    {'skill': 'TypeScript', 'importance': 'medium', 'description': 'Frontend development'},
                    {'skill': 'SQL Server', 'importance': 'medium', 'description': 'Database management'},
                    {'skill': 'PowerShell', 'importance': 'medium', 'description': 'Automation scripting'},
                    {'skill': 'Docker', 'importance': 'medium', 'description': 'Containerization'},
                    {'skill': 'Git', 'importance': 'high', 'description': 'Version control'},
                    {'skill': 'Agile', 'importance': 'high', 'description': 'Development methodology'},
                ],
                'soft_skills': [
                    {'skill': 'Customer Obsession', 'importance': 'high', 'description': 'Customer-first mindset'},
                    {'skill': 'Growth Mindset', 'importance': 'high', 'description': 'Continuous learning'},
                    {'skill': 'Inclusion', 'importance': 'high', 'description': 'Diverse perspectives'},
                    {'skill': 'Accountability', 'importance': 'medium', 'description': 'Ownership mentality'},
                ],
                'cultural_values': ['Respect', 'Integrity', 'Accountability', 'Inclusive'],
                'education': 'Bachelor\'s degree preferred',
                'experience_level': 'Strong problem-solving and analytical skills'
            },
            'amazon': {
                'technical_skills': [
                    {'skill': 'Java', 'importance': 'high', 'description': 'Backend services'},
                    {'skill': 'Python', 'importance': 'high', 'description': 'Automation and scripting'},
                    {'skill': 'AWS', 'importance': 'high', 'description': 'Cloud services'},
                    {'skill': 'Distributed Systems', 'importance': 'high', 'description': 'Scalable architectures'},
                    {'skill': 'Linux', 'importance': 'medium', 'description': 'Operating systems'},
                    {'skill': 'SQL', 'importance': 'medium', 'description': 'Database queries'},
                    {'skill': 'NoSQL', 'importance': 'medium', 'description': 'DynamoDB, etc.'},
                    {'skill': 'Microservices', 'importance': 'high', 'description': 'Service architecture'},
                ],
                'soft_skills': [
                    {'skill': 'Customer Obsession', 'importance': 'high', 'description': 'Customer-first approach'},
                    {'skill': 'Ownership', 'importance': 'high', 'description': 'Take responsibility'},
                    {'skill': 'Invent and Simplify', 'importance': 'high', 'description': 'Innovation mindset'},
                    {'skill': 'Bias for Action', 'importance': 'high', 'description': 'Speed in decision-making'},
                ],
                'cultural_values': ['Customer Obsession', 'Ownership', 'Invent and Simplify', 'High Standards'],
                'education': 'Computer Science or Engineering degree',
                'experience_level': 'Strong system design and coding skills'
            },
            'meta': {
                'technical_skills': [
                    {'skill': 'React', 'importance': 'high', 'description': 'Frontend framework'},
                    {'skill': 'JavaScript', 'importance': 'high', 'description': 'Primary web language'},
                    {'skill': 'Python', 'importance': 'high', 'description': 'Backend development'},
                    {'skill': 'GraphQL', 'importance': 'medium', 'description': 'API development'},
                    {'skill': 'React Native', 'importance': 'medium', 'description': 'Mobile development'},
                    {'skill': 'Node.js', 'importance': 'medium', 'description': 'Server-side JavaScript'},
                    {'skill': 'Machine Learning', 'importance': 'medium', 'description': 'AI initiatives'},
                    {'skill': 'A/B Testing', 'importance': 'medium', 'description': 'Experimentation'},
                ],
                'soft_skills': [
                    {'skill': 'Move Fast', 'importance': 'high', 'description': 'Rapid iteration'},
                    {'skill': 'Be Bold', 'importance': 'high', 'description': 'Take risks'},
                    {'skill': 'Focus on Impact', 'importance': 'high', 'description': 'Meaningful outcomes'},
                    {'skill': 'Build Social Value', 'importance': 'medium', 'description': 'Community impact'},
                ],
                'cultural_values': ['Move Fast', 'Be Bold', 'Focus on Impact', 'Build Social Value'],
                'education': 'Computer Science or related field',
                'experience_level': 'Strong product engineering experience'
            },
            'apple': {
                'technical_skills': [
                    {'skill': 'Swift', 'importance': 'high', 'description': 'iOS development'},
                    {'skill': 'Objective-C', 'importance': 'medium', 'description': 'Legacy iOS code'},
                    {'skill': 'C++', 'importance': 'medium', 'description': 'System-level programming'},
                    {'skill': 'iOS', 'importance': 'high', 'description': 'Mobile platform'},
                    {'skill': 'macOS', 'importance': 'medium', 'description': 'Desktop platform'},
                    {'skill': 'Xcode', 'importance': 'high', 'description': 'Development environment'},
                    {'skill': 'Core Data', 'importance': 'medium', 'description': 'Data persistence'},
                    {'skill': 'Metal', 'importance': 'low', 'description': 'Graphics programming'},
                ],
                'soft_skills': [
                    {'skill': 'Attention to Detail', 'importance': 'high', 'description': 'Quality focus'},
                    {'skill': 'User Experience', 'importance': 'high', 'description': 'User-centric design'},
                    {'skill': 'Innovation', 'importance': 'high', 'description': 'Creative solutions'},
                    {'skill': 'Collaboration', 'importance': 'medium', 'description': 'Cross-team work'},
                ],
                'cultural_values': ['Innovation', 'Quality', 'Simplicity', 'User Focus'],
                'education': 'Computer Science or Engineering degree',
                'experience_level': 'Strong mobile development experience'
            },
            'netflix': {
                'technical_skills': [
                    {'skill': 'Java', 'importance': 'high', 'description': 'Backend microservices'},
                    {'skill': 'Python', 'importance': 'high', 'description': 'Data science and automation'},
                    {'skill': 'Scala', 'importance': 'medium', 'description': 'Data processing'},
                    {'skill': 'AWS', 'importance': 'high', 'description': 'Cloud infrastructure'},
                    {'skill': 'Microservices', 'importance': 'high', 'description': 'Architecture pattern'},
                    {'skill': 'Kafka', 'importance': 'medium', 'description': 'Event streaming'},
                    {'skill': 'Cassandra', 'importance': 'medium', 'description': 'NoSQL database'},
                    {'skill': 'Machine Learning', 'importance': 'high', 'description': 'Recommendation systems'},
                ],
                'soft_skills': [
                    {'skill': 'Freedom and Responsibility', 'importance': 'high', 'description': 'Autonomous work'},
                    {'skill': 'High Performance', 'importance': 'high', 'description': 'Excellence standard'},
                    {'skill': 'Innovation', 'importance': 'high', 'description': 'Creative problem solving'},
                    {'skill': 'Data-Driven', 'importance': 'medium', 'description': 'Evidence-based decisions'},
                ],
                'cultural_values': ['Freedom', 'Responsibility', 'Innovation', 'Data-Driven'],
                'education': 'Computer Science or related technical field',
                'experience_level': 'Strong experience with large-scale systems'
            }
        }
    
    async def analyze_for_company(self, resume_text: str, company_name: str) -> Dict:
        """
        Analyze resume against specific company requirements
        """
        company = company_name.lower().strip()
        
        if company not in self.company_requirements:
            # Generic tech company analysis
            return await self._generic_tech_analysis(resume_text, company_name)
        
        company_data = self.company_requirements[company]
        resume_lower = resume_text.lower()
        
        # Analyze technical skills match
        tech_match = self._analyze_technical_match(resume_lower, company_data['technical_skills'])
        
        # Analyze soft skills match
        soft_match = self._analyze_soft_skills_match(resume_lower, company_data['soft_skills'])
        
        # Calculate overall match percentage
        overall_match = self._calculate_match_percentage(tech_match, soft_match)
        
        # Identify missing skills
        missing_skills = self._identify_missing_skills(resume_lower, company_data)
        
        # Generate recommendations
        recommendations = self._generate_company_recommendations(tech_match, soft_match, company_data, company_name)
        
        # Cultural fit analysis
        cultural_fit = self._analyze_cultural_fit(resume_lower, company_data['cultural_values'])
        
        return {
            'company_name': company_name.title(),
            'match_percentage': overall_match,
            'technical_match': tech_match,
            'soft_skills_match': soft_match,
            'missing_skills': missing_skills,
            'recommendations': recommendations,
            'cultural_fit_score': cultural_fit,
            'role_specific_feedback': {
                'education_match': self._check_education_requirements(resume_lower, company_data),
                'experience_level': self._assess_experience_level(resume_lower, company_data),
                'company_specific_technologies': self._check_company_tech_stack(resume_lower, company)
            }
        }
    
    def _analyze_technical_match(self, resume_text: str, required_skills: List[Dict]) -> Dict:
        """
        Analyze how well resume matches technical requirements
        """
        matched_skills = []
        missing_skills = []
        
        for skill_req in required_skills:
            skill_name = skill_req['skill'].lower()
            if self._skill_mentioned(resume_text, skill_name):
                matched_skills.append(skill_req)
            else:
                missing_skills.append(skill_req)
        
        # Calculate match score based on importance weights
        total_weight = sum(3 if s['importance'] == 'high' else 2 if s['importance'] == 'medium' else 1 
                          for s in required_skills)
        matched_weight = sum(3 if s['importance'] == 'high' else 2 if s['importance'] == 'medium' else 1 
                           for s in matched_skills)
        
        match_score = (matched_weight / total_weight) * 100 if total_weight > 0 else 0
        
        return {
            'score': round(match_score, 1),
            'matched_skills': matched_skills,
            'missing_skills': missing_skills,
            'critical_missing': [s for s in missing_skills if s['importance'] == 'high']
        }
    
    def _analyze_soft_skills_match(self, resume_text: str, soft_skills: List[Dict]) -> Dict:
        """
        Analyze soft skills alignment
        """
        matched_skills = []
        missing_skills = []
        
        for skill_req in soft_skills:
            skill_keywords = self._get_soft_skill_keywords(skill_req['skill'])
            if any(keyword in resume_text for keyword in skill_keywords):
                matched_skills.append(skill_req)
            else:
                missing_skills.append(skill_req)
        
        match_score = (len(matched_skills) / len(soft_skills)) * 100 if soft_skills else 100
        
        return {
            'score': round(match_score, 1),
            'matched_skills': matched_skills,
            'missing_skills': missing_skills
        }
    
    def _skill_mentioned(self, text: str, skill: str) -> bool:
        """
        Check if a skill is mentioned in the text
        """
        # Handle multi-word skills and variations
        skill_variations = self._get_skill_variations(skill)
        
        for variation in skill_variations:
            pattern = r'\b' + re.escape(variation.lower()) + r'\b'
            if re.search(pattern, text):
                return True
        
        return False
    
    def _get_skill_variations(self, skill: str) -> List[str]:
        """
        Get variations of a skill name
        """
        variations = [skill]
        
        # Add common variations
        skill_mappings = {
            'machine learning': ['ml', 'machine learning', 'artificial intelligence', 'ai'],
            'javascript': ['js', 'javascript', 'ecmascript'],
            'typescript': ['ts', 'typescript'],
            'react': ['react.js', 'reactjs', 'react'],
            'node.js': ['nodejs', 'node', 'node.js'],
            'c#': ['c sharp', 'csharp', 'c#'],
            'c++': ['cpp', 'c plus plus', 'c++'],
            'google cloud platform': ['gcp', 'google cloud', 'google cloud platform'],
            'amazon web services': ['aws', 'amazon web services'],
            'microsoft azure': ['azure', 'microsoft azure'],
            'distributed systems': ['distributed computing', 'distributed systems', 'scalable systems']
        }
        
        if skill.lower() in skill_mappings:
            variations.extend(skill_mappings[skill.lower()])
        
        return variations
    
    def _get_soft_skill_keywords(self, soft_skill: str) -> List[str]:
        """
        Get keywords that indicate presence of soft skills
        """
        soft_skill_keywords = {
            'problem solving': ['problem solving', 'troubleshooting', 'debugging', 'analytical'],
            'collaboration': ['collaboration', 'teamwork', 'cross-functional', 'team player'],
            'leadership': ['leadership', 'led', 'managed', 'mentored', 'guided'],
            'innovation': ['innovation', 'creative', 'invented', 'pioneered', 'designed'],
            'customer obsession': ['customer', 'user', 'client', 'customer-focused'],
            'ownership': ['ownership', 'responsible', 'accountable', 'delivered'],
            'growth mindset': ['learning', 'growth', 'development', 'continuous improvement'],
            'attention to detail': ['detail', 'quality', 'precision', 'accuracy'],
            'user experience': ['ux', 'user experience', 'usability', 'user-centered']
        }
        
        return soft_skill_keywords.get(soft_skill.lower(), [soft_skill.lower()])
    
    def _calculate_match_percentage(self, tech_match: Dict, soft_match: Dict) -> float:
        """
        Calculate overall match percentage
        """
        # Weight technical skills more heavily (70% vs 30%)
        overall_score = (tech_match['score'] * 0.7) + (soft_match['score'] * 0.3)
        return round(overall_score, 1)
    
    def _identify_missing_skills(self, resume_text: str, company_data: Dict) -> List[str]:
        """
        Identify top missing skills for the company
        """
        missing_skills = []
        
        # Add critical technical skills
        for skill in company_data['technical_skills']:
            if skill['importance'] == 'high' and not self._skill_mentioned(resume_text, skill['skill']):
                missing_skills.append(skill['skill'])
        
        # Add important soft skills
        for skill in company_data['soft_skills']:
            if skill['importance'] == 'high':
                skill_keywords = self._get_soft_skill_keywords(skill['skill'])
                if not any(keyword in resume_text for keyword in skill_keywords):
                    missing_skills.append(skill['skill'])
        
        return missing_skills[:8]  # Limit to top 8 missing skills
    
    def _generate_company_recommendations(self, tech_match: Dict, soft_match: Dict, 
                                        company_data: Dict, company_name: str) -> List[str]:
        """
        Generate company-specific recommendations
        """
        recommendations = []
        
        # Technical recommendations
        if tech_match['score'] < 70:
            critical_missing = [s['skill'] for s in tech_match['critical_missing']]
            if critical_missing:
                recommendations.append(f"Focus on learning {company_name}'s core technologies: {', '.join(critical_missing[:3])}")
        
        # Soft skills recommendations
        if soft_match['score'] < 60:
            missing_soft = [s['skill'] for s in soft_match['missing_skills'][:2]]
            if missing_soft:
                recommendations.append(f"Highlight experiences that demonstrate {', '.join(missing_soft)}")
        
        # Company-specific advice
        company_advice = {
            'google': "Emphasize algorithmic thinking and large-scale system experience",
            'microsoft': "Highlight Azure experience and customer-focused projects",
            'amazon': "Demonstrate ownership mentality and AWS expertise",
            'meta': "Show rapid iteration experience and React/mobile development",
            'apple': "Focus on user experience and iOS development quality",
            'netflix': "Highlight microservices architecture and machine learning experience"
        }
        
        if company_name.lower() in company_advice:
            recommendations.append(company_advice[company_name.lower()])
        
        return recommendations[:5]
    
    def _analyze_cultural_fit(self, resume_text: str, cultural_values: List[str]) -> float:
        """
        Analyze cultural fit based on resume content
        """
        cultural_indicators = {
            'innovation': ['innovative', 'created', 'pioneered', 'invented', 'designed'],
            'collaboration': ['collaborated', 'teamwork', 'cross-functional', 'partnership'],
            'customer focus': ['customer', 'user', 'client', 'user-focused'],
            'quality': ['quality', 'excellence', 'precision', 'attention to detail'],
            'leadership': ['led', 'managed', 'mentored', 'guided', 'directed'],
            'freedom': ['autonomous', 'independent', 'self-directed', 'initiative'],
            'responsibility': ['responsible', 'accountable', 'ownership', 'delivered']
        }
        
        matches = 0
        for value in cultural_values:
            value_lower = value.lower()
            indicators = cultural_indicators.get(value_lower, [value_lower])
            if any(indicator in resume_text for indicator in indicators):
                matches += 1
        
        return round((matches / len(cultural_values)) * 100, 1) if cultural_values else 100
    
    def _check_education_requirements(self, resume_text: str, company_data: Dict) -> bool:
        """
        Check if education requirements are met
        """
        education_keywords = [
            'computer science', 'cs', 'software engineering', 'electrical engineering',
            'engineering', 'mathematics', 'physics', 'bachelor', 'master', 'phd'
        ]
        
        return any(keyword in resume_text for keyword in education_keywords)
    
    def _assess_experience_level(self, resume_text: str, company_data: Dict) -> str:
        """
        Assess experience level based on resume content
        """
        # Count years of experience mentions
        years_pattern = r'(\d+)[\s\-]*(?:years?|yrs?)'
        years_matches = re.findall(years_pattern, resume_text)
        
        if years_matches:
            max_years = max(int(year) for year in years_matches)
            if max_years >= 5:
                return 'Senior'
            elif max_years >= 2:
                return 'Mid-level'
            else:
                return 'Junior'
        
        # Count job positions
        position_indicators = len(re.findall(r'(?:software engineer|developer|programmer|analyst)', resume_text))
        
        if position_indicators >= 3:
            return 'Senior'
        elif position_indicators >= 2:
            return 'Mid-level'
        else:
            return 'Junior'
    
    def _check_company_tech_stack(self, resume_text: str, company: str) -> List[str]:
        """
        Check for company-specific technology stack
        """
        tech_stacks = {
            'google': ['tensorflow', 'kubernetes', 'go', 'bigtable', 'spanner'],
            'microsoft': ['azure', '.net', 'sql server', 'powershell', 'sharepoint'],
            'amazon': ['aws', 'dynamo', 'lambda', 'ec2', 's3'],
            'meta': ['react', 'graphql', 'hack', 'flow', 'mercurial'],
            'apple': ['swift', 'xcode', 'core data', 'metal', 'webkit'],
            'netflix': ['microservices', 'cassandra', 'kafka', 'hystrix', 'eureka']
        }
        
        found_tech = []
        if company in tech_stacks:
            for tech in tech_stacks[company]:
                if tech in resume_text:
                    found_tech.append(tech)
        
        return found_tech
    
    async def _generic_tech_analysis(self, resume_text: str, company_name: str) -> Dict:
        """
        Generic analysis for companies not in database
        """
        return {
            'company_name': company_name,
            'match_percentage': 75.0,
            'message': f'Analysis for {company_name} not available. Showing general tech recommendations.',
            'recommendations': [
                'Include relevant programming languages for the role',
                'Highlight problem-solving and analytical skills',
                'Show examples of teamwork and collaboration',
                'Demonstrate continuous learning and growth mindset',
                'Include quantifiable achievements and impact'
            ],
            'cultural_fit_score': 75.0,
            'role_specific_feedback': {
                'education_match': True,
                'experience_level': 'Mid-level',
                'company_specific_technologies': []
            }
        }
    
    async def get_requirements(self, company_name: str) -> Dict:
        """
        Get detailed requirements for a specific company
        """
        company = company_name.lower().strip()
        
        if company in self.company_requirements:
            return {
                'company': company_name.title(),
                'requirements': self.company_requirements[company],
                'available': True
            }
        else:
            return {
                'company': company_name.title(),
                'message': f'Detailed requirements for {company_name} not available',
                'available': False,
                'general_advice': [
                    'Research the company\'s tech stack and values',
                    'Check recent job postings for required skills',
                    'Look at employee profiles on LinkedIn',
                    'Review the company\'s engineering blog'
                ]
            }