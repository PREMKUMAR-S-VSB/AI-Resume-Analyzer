import React, { useState } from 'react';
import { PlusCircle, Download, Eye, Save, FileText } from 'lucide-react';

const Builder = () => {
  const [selectedTemplate, setSelectedTemplate] = useState('modern');
  const [formData, setFormData] = useState({
    personalInfo: {
      fullName: '',
      email: '',
      phone: '',
      location: '',
      linkedin: '',
      github: ''
    },
    summary: '',
    experience: [],
    education: [],
    skills: [],
    projects: []
  });

  const templates = [
    { id: 'modern', name: 'Modern Professional', color: 'blue' },
    { id: 'traditional', name: 'Classic Traditional', color: 'gray' },
    { id: 'creative', name: 'Creative Designer', color: 'purple' },
    { id: 'minimal', name: 'Minimal Clean', color: 'green' }
  ];

  const handleInputChange = (section, field, value) => {
    setFormData(prev => ({
      ...prev,
      [section]: {
        ...prev[section],
        [field]: value
      }
    }));
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12 animate-slideUp">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Resume Builder
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Create a professional resume with our AI-powered builder and customizable templates.
          </p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Form Section */}
          <div className="lg:col-span-2 space-y-8">
            {/* Template Selection */}
            <div className="card">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Choose Template</h2>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {templates.map((template) => (
                  <div
                    key={template.id}
                    onClick={() => setSelectedTemplate(template.id)}
                    className={`p-4 rounded-lg border-2 cursor-pointer transition-all duration-300 ${
                      selectedTemplate === template.id
                        ? 'border-blue-500 bg-blue-50'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <div className={`h-24 bg-${template.color}-100 rounded mb-2`}></div>
                    <p className="text-sm font-medium text-center">{template.name}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Personal Information */}
            <div className="card">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Personal Information</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <input
                  type="text"
                  placeholder="Full Name *"
                  className="form-input"
                  value={formData.personalInfo.fullName}
                  onChange={(e) => handleInputChange('personalInfo', 'fullName', e.target.value)}
                />
                <input
                  type="email"
                  placeholder="Email Address *"
                  className="form-input"
                  value={formData.personalInfo.email}
                  onChange={(e) => handleInputChange('personalInfo', 'email', e.target.value)}
                />
                <input
                  type="tel"
                  placeholder="Phone Number *"
                  className="form-input"
                  value={formData.personalInfo.phone}
                  onChange={(e) => handleInputChange('personalInfo', 'phone', e.target.value)}
                />
                <input
                  type="text"
                  placeholder="Location *"
                  className="form-input"
                  value={formData.personalInfo.location}
                  onChange={(e) => handleInputChange('personalInfo', 'location', e.target.value)}
                />
                <input
                  type="url"
                  placeholder="LinkedIn Profile"
                  className="form-input"
                  value={formData.personalInfo.linkedin}
                  onChange={(e) => handleInputChange('personalInfo', 'linkedin', e.target.value)}
                />
                <input
                  type="url"
                  placeholder="GitHub Profile"
                  className="form-input"
                  value={formData.personalInfo.github}
                  onChange={(e) => handleInputChange('personalInfo', 'github', e.target.value)}
                />
              </div>
            </div>

            {/* Professional Summary */}
            <div className="card">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Professional Summary</h2>
              <textarea
                rows={4}
                placeholder="Write a compelling summary of your professional background and key achievements..."
                className="form-textarea"
                value={formData.summary}
                onChange={(e) => setFormData(prev => ({ ...prev, summary: e.target.value }))}
              />
            </div>

            {/* Experience Section */}
            <div className="card">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-semibold text-gray-900">Work Experience</h2>
                <button className="btn-outline text-sm">
                  <PlusCircle className="h-4 w-4 mr-2" />
                  Add Experience
                </button>
              </div>
              <div className="text-center py-8 text-gray-500">
                Click "Add Experience" to start building your work history
              </div>
            </div>

            {/* Education Section */}
            <div className="card">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-semibold text-gray-900">Education</h2>
                <button className="btn-outline text-sm">
                  <PlusCircle className="h-4 w-4 mr-2" />
                  Add Education
                </button>
              </div>
              <div className="text-center py-8 text-gray-500">
                Click "Add Education" to include your educational background
              </div>
            </div>

            {/* Skills Section */}
            <div className="card">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-semibold text-gray-900">Skills</h2>
                <button className="btn-outline text-sm">
                  <PlusCircle className="h-4 w-4 mr-2" />
                  Add Skills
                </button>
              </div>
              <div className="text-center py-8 text-gray-500">
                Add your technical and soft skills
              </div>
            </div>
          </div>

          {/* Preview Section */}
          <div className="lg:col-span-1">
            <div className="sticky top-8">
              <div className="card">
                <h3 className="text-lg font-semibold text-gray-900 mb-4">Resume Preview</h3>
                <div className="bg-gray-100 rounded-lg h-96 flex items-center justify-center mb-4">
                  <div className="text-center text-gray-500">
                    <FileText className="h-12 w-12 mx-auto mb-2" />
                    <p>Resume preview will appear here</p>
                  </div>
                </div>
                <div className="space-y-3">
                  <button className="btn-primary w-full">
                    <Eye className="h-4 w-4 mr-2" />
                    Full Preview
                  </button>
                  <button className="btn-secondary w-full">
                    <Download className="h-4 w-4 mr-2" />
                    Download PDF
                  </button>
                  <button className="btn-outline w-full">
                    <Save className="h-4 w-4 mr-2" />
                    Save Progress
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Builder;