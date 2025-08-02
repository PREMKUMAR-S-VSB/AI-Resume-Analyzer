import React, { useState } from 'react';
import { Building2, Upload, Search, TrendingUp } from 'lucide-react';

const CompanyAnalysis = () => {
  const [selectedCompany, setSelectedCompany] = useState('');
  
  const companies = [
    { id: 'google', name: 'Google', logo: '🟢' },
    { id: 'microsoft', name: 'Microsoft', logo: '🔷' },
    { id: 'amazon', name: 'Amazon', logo: '🟠' },
    { id: 'meta', name: 'Meta (Facebook)', logo: '🔵' },
    { id: 'apple', name: 'Apple', logo: '🍎' },
    { id: 'netflix', name: 'Netflix', logo: '🔴' },
  ];

  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12 animate-slideUp">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Company-Specific Analysis
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Analyze your resume against specific company requirements and get tailored recommendations 
            for top tech companies.
          </p>
        </div>

        {/* Company Selection */}
        <div className="max-w-4xl mx-auto mb-12 animate-fadeIn">
          <div className="card">
            <h2 className="text-2xl font-semibold text-gray-900 mb-6 text-center">
              Select Target Company
            </h2>
            <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
              {companies.map((company) => (
                <div
                  key={company.id}
                  onClick={() => setSelectedCompany(company.id)}
                  className={`p-6 rounded-lg border-2 cursor-pointer transition-all duration-300 text-center ${
                    selectedCompany === company.id
                      ? 'border-blue-500 bg-blue-50 shadow-lg'
                      : 'border-gray-200 hover:border-gray-300 hover:shadow-md'
                  }`}
                >
                  <div className="text-4xl mb-3">{company.logo}</div>
                  <h3 className="font-semibold text-gray-900">{company.name}</h3>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Upload Section */}
        <div className="max-w-2xl mx-auto mb-12 animate-slideUp">
          <div className="card">
            <div className="text-center">
              <Building2 className="mx-auto h-12 w-12 text-blue-600 mb-4" />
              <h3 className="text-xl font-semibold text-gray-900 mb-4">
                Upload Your Resume
              </h3>
              <div className="dropzone">
                <Upload className="mx-auto h-8 w-8 text-gray-400 mb-3" />
                <p className="text-gray-700 mb-2">
                  Drop your resume here or click to browse
                </p>
                <p className="text-sm text-gray-500">
                  PDF, DOC, DOCX up to 10MB
                </p>
              </div>
              <button 
                disabled={!selectedCompany}
                className="btn-primary mt-6 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <Search className="h-4 w-4 mr-2" />
                Analyze for {selectedCompany ? companies.find(c => c.id === selectedCompany)?.name : 'Company'}
              </button>
            </div>
          </div>
        </div>

        {/* Features Preview */}
        <div className="grid md:grid-cols-3 gap-8 animate-fadeIn">
          <div className="card text-center">
            <div className="bg-blue-100 text-blue-600 p-3 rounded-lg w-fit mx-auto mb-4">
              <TrendingUp className="h-6 w-6" />
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-3">
              Match Percentage
            </h3>
            <p className="text-gray-600">
              See how well your resume aligns with company-specific requirements
            </p>
          </div>

          <div className="card text-center">
            <div className="bg-green-100 text-green-600 p-3 rounded-lg w-fit mx-auto mb-4">
              <Building2 className="h-6 w-6" />
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-3">
              Cultural Fit Score
            </h3>
            <p className="text-gray-600">
              Understand how your experience matches company culture and values
            </p>
          </div>

          <div className="card text-center">
            <div className="bg-purple-100 text-purple-600 p-3 rounded-lg w-fit mx-auto mb-4">
              <Search className="h-6 w-6" />
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-3">
              Targeted Recommendations
            </h3>
            <p className="text-gray-600">
              Get specific suggestions to improve your chances at your target company
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CompanyAnalysis;