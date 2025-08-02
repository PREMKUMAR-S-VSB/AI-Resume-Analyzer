import React, { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { toast } from 'react-hot-toast';
import { 
  Upload, 
  FileText, 
  AlertCircle, 
  CheckCircle, 
  TrendingUp, 
  Award,
  Target,
  Lightbulb,
  Download,
  RefreshCw
} from 'lucide-react';
import axios from 'axios';

const Analyzer = () => {
  const [file, setFile] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [analysis, setAnalysis] = useState(null);
  const [error, setError] = useState(null);

  const onDrop = useCallback((acceptedFiles, rejectedFiles) => {
    if (rejectedFiles.length > 0) {
      toast.error('Please upload a PDF or DOCX file');
      return;
    }

    const uploadedFile = acceptedFiles[0];
    if (uploadedFile) {
      setFile(uploadedFile);
      setAnalysis(null);
      setError(null);
      toast.success('File uploaded successfully!');
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive, isDragReject } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
      'application/msword': ['.doc']
    },
    maxFiles: 1,
    maxSize: 10485760 // 10MB
  });

  const analyzeResume = async () => {
    if (!file) {
      toast.error('Please upload a resume first');
      return;
    }

    setAnalyzing(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post('/analyze-resume', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setAnalysis(response.data);
      toast.success('Analysis completed!');
    } catch (err) {
      const errorMessage = err.response?.data?.detail || 'Analysis failed. Please try again.';
      setError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setAnalyzing(false);
    }
  };

  const getScoreColor = (score) => {
    if (score >= 80) return 'score-excellent';
    if (score >= 65) return 'score-good';
    if (score >= 50) return 'score-fair';
    return 'score-poor';
  };

  const getScoreLabel = (score) => {
    if (score >= 80) return 'Excellent';
    if (score >= 65) return 'Good';
    if (score >= 50) return 'Fair';
    return 'Needs Improvement';
  };

  const ScoreCard = ({ title, score, description }) => (
    <div className="card">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
        <div className={`px-3 py-1 rounded-full text-sm font-medium ${getScoreColor(score)}`}>
          {score.toFixed(1)}%
        </div>
      </div>
      <div className="progress-bar mb-2">
        <div 
          className="progress-fill" 
          style={{ width: `${score}%` }}
        ></div>
      </div>
      <p className="text-sm text-gray-600">{description}</p>
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12 animate-slideUp">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            AI Resume Analyzer
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Upload your resume and get instant ATS scores, missing components analysis, 
            and personalized improvement recommendations.
          </p>
        </div>

        {/* Upload Section */}
        <div className="max-w-2xl mx-auto mb-12 animate-fadeIn">
          <div 
            {...getRootProps()} 
            className={`dropzone ${isDragActive ? 'active' : ''} ${isDragReject ? 'reject' : ''}`}
          >
            <input {...getInputProps()} />
            <div className="text-center">
              <Upload className="mx-auto h-12 w-12 text-gray-400 mb-4" />
              {isDragActive ? (
                <p className="text-lg text-blue-600">Drop your resume here...</p>
              ) : (
                <>
                  <p className="text-lg text-gray-700 mb-2">
                    Drag & drop your resume here, or click to browse
                  </p>
                  <p className="text-sm text-gray-500">
                    Supports PDF, DOC, and DOCX files (max 10MB)
                  </p>
                </>
              )}
            </div>
          </div>

          {file && (
            <div className="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200 animate-slideUp">
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-3">
                  <FileText className="h-8 w-8 text-blue-600" />
                  <div>
                    <p className="font-medium text-blue-900">{file.name}</p>
                    <p className="text-sm text-blue-600">
                      {(file.size / 1024 / 1024).toFixed(2)} MB
                    </p>
                  </div>
                </div>
                <button
                  onClick={analyzeResume}
                  disabled={analyzing}
                  className="btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {analyzing ? (
                    <>
                      <RefreshCw className="animate-spin h-4 w-4 mr-2" />
                      Analyzing...
                    </>
                  ) : (
                    <>
                      <TrendingUp className="h-4 w-4 mr-2" />
                      Analyze Resume
                    </>
                  )}
                </button>
              </div>
            </div>
          )}
        </div>

        {/* Error Display */}
        {error && (
          <div className="max-w-2xl mx-auto mb-8 animate-slideUp">
            <div className="bg-red-50 border border-red-200 rounded-lg p-4">
              <div className="flex items-center">
                <AlertCircle className="h-5 w-5 text-red-600 mr-3" />
                <p className="text-red-800">{error}</p>
              </div>
            </div>
          </div>
        )}

        {/* Analysis Results */}
        {analysis && (
          <div className="animate-slideUp">
            {/* Overall Score */}
            <div className="text-center mb-12">
              <div className="inline-block bg-white rounded-2xl shadow-2xl p-8">
                <div className="flex items-center justify-center mb-4">
                  <Award className="h-8 w-8 text-yellow-500 mr-3" />
                  <h2 className="text-2xl font-bold text-gray-900">Overall ATS Score</h2>
                </div>
                <div className="text-6xl font-bold text-blue-600 mb-2">
                  {analysis.ats_score.overall_score}%
                </div>
                <div className={`inline-block px-4 py-2 rounded-full text-lg font-medium ${getScoreColor(analysis.ats_score.overall_score)}`}>
                  {getScoreLabel(analysis.ats_score.overall_score)}
                </div>
              </div>
            </div>

            {/* Detailed Scores */}
            <div className="grid-responsive mb-12">
              <ScoreCard
                title="Formatting Score"
                score={analysis.ats_score.formatting_score}
                description="How well your resume is formatted for ATS systems"
              />
              <ScoreCard
                title="Keyword Score"
                score={analysis.ats_score.keyword_score}
                description="Relevance and density of industry keywords"
              />
              <ScoreCard
                title="Content Quality"
                score={analysis.ats_score.content_score}
                description="Overall quality and completeness of content"
              />
              <ScoreCard
                title="Readability"
                score={analysis.ats_score.readability_score}
                description="How easy your resume is to read and understand"
              />
              <ScoreCard
                title="Section Structure"
                score={analysis.ats_score.section_score}
                description="Presence and organization of key resume sections"
              />
            </div>

            <div className="grid lg:grid-cols-2 gap-8">
              {/* Skills Analysis */}
              <div className="card">
                <div className="flex items-center mb-6">
                  <Target className="h-6 w-6 text-green-600 mr-3" />
                  <h3 className="text-xl font-semibold text-gray-900">Skills Analysis</h3>
                </div>
                
                {analysis.skill_analysis.identified_skills.map((category, index) => (
                  <div key={index} className="mb-4">
                    <h4 className="font-medium text-gray-900 mb-2">{category.category}</h4>
                    <div className="flex flex-wrap gap-2">
                      {category.skills.map((skill, skillIndex) => (
                        <span key={skillIndex} className="badge-primary">
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>
                ))}

                {analysis.skill_analysis.missing_skills.length > 0 && (
                  <div className="mt-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="font-medium text-yellow-800 mb-2">Suggested Skills to Add:</h4>
                    <div className="flex flex-wrap gap-2">
                      {analysis.skill_analysis.missing_skills.map((skill, index) => (
                        <span key={index} className="badge-warning">
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {/* Missing Components */}
              <div className="card">
                <div className="flex items-center mb-6">
                  <AlertCircle className="h-6 w-6 text-orange-600 mr-3" />
                  <h3 className="text-xl font-semibold text-gray-900">Missing Components</h3>
                </div>
                
                {analysis.missing_components.length === 0 ? (
                  <div className="flex items-center text-green-600">
                    <CheckCircle className="h-5 w-5 mr-2" />
                    <span>All essential components are present!</span>
                  </div>
                ) : (
                  <div className="space-y-4">
                    {analysis.missing_components.map((component, index) => (
                      <div key={index} className="p-4 bg-red-50 rounded-lg border border-red-200">
                        <div className="flex items-start justify-between mb-2">
                          <h4 className="font-medium text-red-900">{component.component}</h4>
                          <span className={`badge text-xs ${
                            component.importance === 'high' ? 'badge-error' : 
                            component.importance === 'medium' ? 'badge-warning' : 'badge-primary'
                          }`}>
                            {component.importance} priority
                          </span>
                        </div>
                        <p className="text-sm text-red-700 mb-2">{component.description}</p>
                        <p className="text-sm text-red-600 font-medium">
                          💡 {component.suggestion}
                        </p>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>

            {/* Improvement Suggestions */}
            <div className="card mt-8">
              <div className="flex items-center mb-6">
                <Lightbulb className="h-6 w-6 text-yellow-600 mr-3" />
                <h3 className="text-xl font-semibold text-gray-900">Improvement Suggestions</h3>
              </div>
              
              <div className="space-y-4">
                {analysis.improvement_suggestions.map((suggestion, index) => (
                  <div key={index} className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <div className="flex items-start justify-between mb-2">
                      <h4 className="font-medium text-blue-900">{suggestion.category}</h4>
                      <span className={`badge text-xs ${
                        suggestion.priority === 'high' ? 'badge-error' : 
                        suggestion.priority === 'medium' ? 'badge-warning' : 'badge-primary'
                      }`}>
                        {suggestion.priority} priority
                      </span>
                    </div>
                    <p className="text-sm text-blue-700 mb-2">{suggestion.suggestion}</p>
                    <p className="text-sm text-blue-600">
                      <strong>Impact:</strong> {suggestion.impact}
                    </p>
                    {suggestion.examples && suggestion.examples.length > 0 && (
                      <div className="mt-2">
                        <p className="text-sm text-blue-600 font-medium">Examples:</p>
                        <ul className="text-sm text-blue-600 list-disc list-inside ml-2">
                          {suggestion.examples.map((example, exIndex) => (
                            <li key={exIndex}>{example}</li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>

            {/* Action Buttons */}
            <div className="text-center mt-12">
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <button className="btn-primary">
                  <Download className="h-4 w-4 mr-2" />
                  Download Report
                </button>
                <button 
                  onClick={() => {
                    setFile(null);
                    setAnalysis(null);
                    setError(null);
                  }}
                  className="btn-secondary"
                >
                  Analyze Another Resume
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Analyzer;