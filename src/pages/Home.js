import React from 'react';
import { Link } from 'react-router-dom';
import { 
  Search, 
  PlusCircle, 
  Building2, 
  FileText, 
  Award, 
  TrendingUp, 
  Users, 
  Zap,
  CheckCircle,
  ArrowRight,
  Star,
  Layout
} from 'lucide-react';

const Home = () => {
  const features = [
    {
      icon: Search,
      title: 'AI-Powered Analysis',
      description: 'Get real-time ATS scores and detailed feedback on your resume',
      color: 'text-blue-600',
      bgColor: 'bg-blue-100'
    },
    {
      icon: Building2,
      title: 'Company-Specific Insights',
      description: 'Tailor your resume for Google, Microsoft, Amazon, and more',
      color: 'text-purple-600',
      bgColor: 'bg-purple-100'
    },
    {
      icon: PlusCircle,
      title: 'Professional Builder',
      description: 'Create stunning resumes with our professionally designed templates',
      color: 'text-green-600',
      bgColor: 'bg-green-100'
    },
    {
      icon: TrendingUp,
      title: 'Skill Gap Analysis',
      description: 'Identify missing skills and get personalized recommendations',
      color: 'text-orange-600',
      bgColor: 'bg-orange-100'
    },
    {
      icon: Award,
      title: 'Multiple Templates',
      description: 'Choose from modern, traditional, creative, and executive layouts',
      color: 'text-pink-600',
      bgColor: 'bg-pink-100'
    },
    {
      icon: Zap,
      title: 'Instant Results',
      description: 'Get comprehensive analysis in seconds, not hours',
      color: 'text-indigo-600',
      bgColor: 'bg-indigo-100'
    }
  ];

  const benefits = [
    'Real-time ATS scoring with detailed breakdown',
    'Company-specific requirement analysis',
    'Missing components identification',
    'Skill recommendations based on industry trends',
    'Professional resume templates',
    'PDF generation and download',
    'Mobile-friendly responsive design',
    'Completely free to use'
  ];

  const testimonials = [
    {
      name: 'Sarah Johnson',
      role: 'Software Engineer at Google',
      content: 'This tool helped me identify exactly what my resume was missing. Got the job at Google!',
      rating: 5
    },
    {
      name: 'Michael Chen',
      role: 'Data Scientist at Microsoft',
      content: 'The company-specific analysis was a game-changer. Perfect for tech applications.',
      rating: 5
    },
    {
      name: 'Emily Rodriguez',
      role: 'Product Manager at Amazon',
      content: 'Love the ATS scoring feature. Finally understood why my resume wasn\'t getting through.',
      rating: 5
    }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative overflow-hidden bg-gradient-to-br from-blue-600 via-purple-600 to-indigo-800 text-white">
        <div className="absolute inset-0 bg-black opacity-20"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 lg:py-32">
          <div className="text-center animate-slideUp">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              AI-Powered Resume
              <span className="block text-yellow-400">Analyzer & Builder</span>
            </h1>
            <p className="text-xl md:text-2xl mb-8 text-gray-200 max-w-3xl mx-auto">
              Get instant ATS scores, company-specific insights, and build professional resumes 
              that land interviews at top tech companies.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <Link
                to="/analyzer"
                className="inline-flex items-center px-8 py-4 bg-white text-blue-600 font-semibold rounded-lg 
                         shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300"
              >
                <Search className="mr-2 h-5 w-5" />
                Analyze Resume
                <ArrowRight className="ml-2 h-5 w-5" />
              </Link>
              <Link
                to="/builder"
                className="inline-flex items-center px-8 py-4 border-2 border-white text-white font-semibold 
                         rounded-lg hover:bg-white hover:text-blue-600 transition-all duration-300"
              >
                <PlusCircle className="mr-2 h-5 w-5" />
                Build Resume
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16 animate-fadeIn">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Everything You Need to Land Your Dream Job
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Our AI-powered platform provides comprehensive resume analysis and building tools
              used by thousands of job seekers worldwide.
            </p>
          </div>

          <div className="grid-responsive">
            {features.map((feature, index) => {
              const Icon = feature.icon;
              return (
                <div 
                  key={index} 
                  className="card-interactive animate-slideUp"
                  style={{ animationDelay: `${index * 100}ms` }}
                >
                  <div className={`${feature.bgColor} ${feature.color} p-3 rounded-lg w-fit mb-4`}>
                    <Icon className="h-6 w-6" />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-3">
                    {feature.title}
                  </h3>
                  <p className="text-gray-600">
                    {feature.description}
                  </p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Benefits Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="lg:grid lg:grid-cols-2 lg:gap-16 items-center">
            <div className="animate-slideUp">
              <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
                Why Choose Our Resume Analyzer?
              </h2>
              <p className="text-lg text-gray-600 mb-8">
                Our advanced AI technology analyzes your resume against real industry standards 
                and provides actionable insights to improve your chances of landing interviews.
              </p>
              <div className="space-y-4">
                {benefits.map((benefit, index) => (
                  <div key={index} className="flex items-center space-x-3">
                    <CheckCircle className="h-5 w-5 text-green-500 flex-shrink-0" />
                    <span className="text-gray-700">{benefit}</span>
                  </div>
                ))}
              </div>
              <div className="mt-8">
                <Link
                  to="/analyzer"
                  className="btn-primary inline-flex items-center"
                >
                  Get Started Free
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Link>
              </div>
            </div>

            <div className="mt-12 lg:mt-0 animate-fadeIn">
              <div className="relative">
                <div className="bg-white rounded-2xl shadow-2xl p-8">
                  <div className="flex items-center justify-between mb-6">
                    <h3 className="text-xl font-semibold text-gray-900">ATS Score</h3>
                    <div className="text-3xl font-bold text-green-600">87%</div>
                  </div>
                  <div className="space-y-4">
                    <div>
                      <div className="flex justify-between text-sm text-gray-600 mb-1">
                        <span>Formatting</span>
                        <span>92%</span>
                      </div>
                      <div className="progress-bar">
                        <div className="progress-fill" style={{ width: '92%' }}></div>
                      </div>
                    </div>
                    <div>
                      <div className="flex justify-between text-sm text-gray-600 mb-1">
                        <span>Keywords</span>
                        <span>85%</span>
                      </div>
                      <div className="progress-bar">
                        <div className="progress-fill" style={{ width: '85%' }}></div>
                      </div>
                    </div>
                    <div>
                      <div className="flex justify-between text-sm text-gray-600 mb-1">
                        <span>Content Quality</span>
                        <span>89%</span>
                      </div>
                      <div className="progress-bar">
                        <div className="progress-fill" style={{ width: '89%' }}></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Success Stories
            </h2>
            <p className="text-xl text-gray-600">
              Join thousands of professionals who landed their dream jobs
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <div key={index} className="card animate-slideUp" style={{ animationDelay: `${index * 200}ms` }}>
                <div className="flex items-center mb-4">
                  {Array.from({ length: testimonial.rating }).map((_, i) => (
                    <Star key={i} className="h-5 w-5 text-yellow-400 fill-current" />
                  ))}
                </div>
                <p className="text-gray-600 mb-4 italic">"{testimonial.content}"</p>
                <div className="border-t pt-4">
                  <p className="font-semibold text-gray-900">{testimonial.name}</p>
                  <p className="text-sm text-gray-500">{testimonial.role}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 gradient-bg-primary">
        <div className="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
          <div className="animate-fadeIn">
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
              Ready to Optimize Your Resume?
            </h2>
            <p className="text-xl text-gray-200 mb-8">
              Upload your resume now and get instant AI-powered insights to land more interviews.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                to="/analyzer"
                className="inline-flex items-center px-8 py-4 bg-white text-blue-600 font-semibold 
                         rounded-lg shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300"
              >
                <FileText className="mr-2 h-5 w-5" />
                Analyze My Resume
              </Link>
              <Link
                to="/templates"
                className="inline-flex items-center px-8 py-4 border-2 border-white text-white 
                         font-semibold rounded-lg hover:bg-white hover:text-blue-600 transition-all duration-300"
              >
                <Layout className="mr-2 h-5 w-5" />
                View Templates
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;