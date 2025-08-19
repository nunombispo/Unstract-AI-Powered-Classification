# Unstract AI-Powered Document Classification

A Streamlit web application that uses the Unstract API to automatically classify and organize PDF documents by type. Upload multiple PDFs and get them automatically categorized using AI-powered document classification.

## 🚀 Features

- **Multi-file Upload**: Upload multiple PDF documents simultaneously
- **AI-Powered Classification**: Automatically classify documents using Unstract's AI
- **Smart Organization**: Documents are automatically organized by classification type
- **PDF Viewer**: Built-in PDF viewer for each classified document
- **Duplicate Detection**: Automatically removes duplicate files during processing
- **Real-time Processing**: Live API integration with progress tracking
- **Responsive UI**: Clean, modern interface built with Streamlit

## 📋 Prerequisites

- Python 3.7 or higher
- Unstract API credentials (API URL and API Key)
- Internet connection for API calls

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone <your-repository-url>
   cd Unstract-AI-Powered-Classification
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root with your Unstract API credentials:

   ```env
   API_URL=your_unstract_api_endpoint_here
   API_KEY=your_unstract_api_key_here
   ```

## 🚀 Usage

1. **Start the application**

   ```bash
   streamlit run app.py
   ```

2. **Open your browser**

   - Navigate to `http://localhost:8501`
   - The application will open automatically

3. **Upload PDFs**

   - Click "Browse files" to select PDF documents
   - You can upload multiple files at once
   - Supported format: PDF only

4. **Start Classification**
   - Click "🚀 Start Document Classification" button
   - Wait for the AI processing to complete
   - View results organized by document type

## 📁 Project Structure

```
Unstract-AI-Powered-Classification/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## 🔧 Configuration

### Environment Variables

| Variable  | Description                          | Required |
| --------- | ------------------------------------ | -------- |
| `API_URL` | Your Unstract API endpoint           | Yes      |
| `API_KEY` | Your Unstract API authentication key | Yes      |

### API Settings

- **Timeout**: 300 seconds (5 minutes) for processing
- **Metadata**: Disabled by default for cleaner results
- **File Handling**: Processes multiple files in a single API call

## 📊 How It Works

1. **File Upload**: Users upload multiple PDF files through the Streamlit interface
2. **Duplicate Removal**: The system automatically removes duplicate files based on filename
3. **API Processing**: All files are sent to the Unstract API in a single batch request
4. **AI Classification**: Unstract's AI analyzes each document and determines its type
5. **Result Organization**: Documents are grouped by classification type
6. **Display**: Results are shown in an organized, column-based layout with PDF viewers

## 🎯 Supported Document Types

The application automatically detects and classifies various document types based on Unstract's AI analysis. Document types will vary depending on your specific Unstract configuration and the documents you upload.

## 🐛 Troubleshooting

### Common Issues

1. **API Connection Failed**

   - Verify your API credentials in the `.env` file
   - Check your internet connection
   - Ensure the API endpoint is correct

2. **Processing Timeout**

   - Large files may take longer to process
   - The default timeout is 5 minutes
   - Consider breaking large documents into smaller files

3. **No Results Returned**
   - Check the API response in the debug section
   - Verify file formats are supported
   - Ensure files are not corrupted

### Debug Information

The application displays the full API response for debugging purposes. Check the "API Response" section if you encounter issues.

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your API credentials secure
- The application processes files locally before sending to the API

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Powered by [Unstract](https://unstract.com/) AI document classification
- PDF viewing capabilities provided by `streamlit-pdf-viewer`

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the API response for error details
3. Ensure your Unstract API credentials are valid
4. Contact your Unstract support team for API-related issues

---

**Note**: This application requires an active Unstract API subscription to function. Please ensure you have the necessary API access before using this tool.
