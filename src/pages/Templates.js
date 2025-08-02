import React, { useState } from 'react';
import { Eye, Download, Star } from 'lucide-react';

const Templates = () => {
  const [selectedCategory, setSelectedCategory] = useState('all');

  const categories = [
    { id: 'all', name: 'All Templates' },
    { id: 'modern', name: 'Modern' },
    { id: 'traditional', name: 'Traditional' },
    { id: 'creative', name: 'Creative' },
    { id: 'minimal', name: 'Minimal' },
    { id: 'executive', name: 'Executive' }
  ];

  const templates = [
    {
      id: 'modern-pro',
      name: 'Modern Professional',
      category: 'modern',
      description: 'Clean design with blue accents, perfect for tech roles',
      rating: 4.9,
      downloads: '12.5k',
      color: 'blue',
      suitableFor: ['Software Engineering', 'Data Science', 'Product Management']
    },
    {
      id: 'classic-traditional',
      name: 'Classic Traditional',
      category: 'traditional',
      description: 'Timeless black and white format for conservative industries',
      rating: 4.7,
      downloads: '8.2k',
      color: 'gray',
      suitableFor: ['Finance', 'Legal', 'Healthcare', 'Government']
    },
    {
      id: 'creative-designer',
      name: 'Creative Designer',
      category: 'creative',
      description: 'Bold and colorful layout for creative professionals',
      rating: 4.8,
      downloads: '6.1k',
      color: 'purple',
      suitableFor: ['Graphic Design', 'Marketing', 'Advertising', 'Media']
    },
    {
      id: 'minimal-clean',
      name: 'Minimal Clean',
      category: 'minimal',
      description: 'Simple and elegant design focusing on content',
      rating: 4.6,
      downloads: '9.3k',
      color: 'green',
      suitableFor: ['Research', 'Academia', 'Consulting', 'Startups']
    },
    {
      id: 'executive-leader',
      name: 'Executive Leadership',
      category: 'executive',
      description: 'Professional layout for senior-level positions',
      rating: 4.9,
      downloads: '4.7k',
      color: 'indigo',
      suitableFor: ['C-Level', 'VP', 'Director', 'Senior Management']
    },
    {
      id: 'tech-innovator',
      name: 'Tech Innovator',
      category: 'modern',
      description: 'Modern design with tech-focused elements',
      rating: 4.8,
      downloads: '7.8k',
      color: 'cyan',
      suitableFor: ['DevOps', 'Cloud Engineering', 'AI/ML', 'Blockchain']
    }
  ];

  const filteredTemplates = selectedCategory === 'all' 
    ? templates 
    : templates.filter(template => template.category === selectedCategory);

  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12 animate-slideUp">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Professional Resume Templates
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Choose from our collection of professionally designed resume templates. 
            Each template is ATS-friendly and optimized for different industries.
          </p>
        </div>

        {/* Category Filter */}
        <div className="flex flex-wrap justify-center gap-4 mb-12 animate-fadeIn">
          {categories.map((category) => (
            <button
              key={category.id}
              onClick={() => setSelectedCategory(category.id)}
              className={`px-6 py-3 rounded-lg font-medium transition-all duration-300 ${
                selectedCategory === category.id
                  ? 'bg-blue-600 text-white shadow-lg'
                  : 'bg-white text-gray-700 border border-gray-300 hover:border-blue-300 hover:shadow-md'
              }`}
            >
              {category.name}
            </button>
          ))}
        </div>

        {/* Templates Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 animate-slideUp">
          {filteredTemplates.map((template, index) => (
            <div 
              key={template.id} 
              className="card-interactive"
              style={{ animationDelay: `${index * 100}ms` }}
            >
              {/* Template Preview */}
              <div className={`bg-${template.color}-100 rounded-lg h-64 mb-4 flex items-center justify-center relative overflow-hidden`}>
                <div className={`w-3/4 h-5/6 bg-white rounded shadow-lg border-l-4 border-${template.color}-500`}>
                  <div className="p-4">
                    <div className={`h-2 bg-${template.color}-400 rounded mb-2`}></div>
                    <div className="h-1 bg-gray-300 rounded mb-1"></div>
                    <div className="h-1 bg-gray-300 rounded mb-4"></div>
                    <div className="space-y-2">
                      <div className="h-1 bg-gray-200 rounded"></div>
                      <div className="h-1 bg-gray-200 rounded"></div>
                      <div className="h-1 bg-gray-200 rounded w-3/4"></div>
                    </div>
                  </div>
                </div>
                
                {/* Overlay Buttons */}
                <div className="absolute inset-0 bg-black bg-opacity-50 opacity-0 hover:opacity-100 transition-opacity duration-300 flex items-center justify-center space-x-4">
                  <button className="bg-white text-gray-900 p-2 rounded-lg hover:bg-gray-100 transition-colors">
                    <Eye className="h-5 w-5" />
                  </button>
                  <button className="bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700 transition-colors">
                    <Download className="h-5 w-5" />
                  </button>
                </div>
              </div>

              {/* Template Info */}
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <h3 className="text-lg font-semibold text-gray-900">{template.name}</h3>
                  <div className="flex items-center space-x-1">
                    <Star className="h-4 w-4 text-yellow-400 fill-current" />
                    <span className="text-sm text-gray-600">{template.rating}</span>
                  </div>
                </div>
                
                <p className="text-gray-600 text-sm">{template.description}</p>
                
                <div className="flex items-center justify-between text-sm text-gray-500">
                  <span>{template.downloads} downloads</span>
                  <span className={`badge badge-${template.color}`}>
                    {template.category}
                  </span>
                </div>

                <div className="space-y-2">
                  <p className="text-xs font-medium text-gray-700">Best for:</p>
                  <div className="flex flex-wrap gap-1">
                    {template.suitableFor.map((role, roleIndex) => (
                      <span key={roleIndex} className="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded">
                        {role}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="flex space-x-3 pt-4">
                  <button className="btn-outline flex-1 text-sm">
                    <Eye className="h-4 w-4 mr-2" />
                    Preview
                  </button>
                  <button className="btn-primary flex-1 text-sm">
                    <Download className="h-4 w-4 mr-2" />
                    Use Template
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* CTA Section */}
        <div className="text-center mt-16 animate-fadeIn">
          <div className="bg-white rounded-2xl shadow-xl p-8 max-w-3xl mx-auto">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              Need a Custom Template?
            </h2>
            <p className="text-gray-600 mb-6">
              Can't find the perfect template? Contact us for a custom design tailored to your industry and role.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button className="btn-primary">
                Request Custom Template
              </button>
              <button className="btn-secondary">
                Contact Support
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Templates;