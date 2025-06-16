# LifeHack App
App/\
    ├── README.md                         # Project overview, setup instructions, and contributors\
    ├── LICENSE                           # Open-source license (e.g., MIT, Apache 2.0)\
    ├── .gitignore                        # Specifies files to be ignored by Git\

    ├── frontend/                         # React Native Frontend\
    │   ├── App.js                        # Entry point of the mobile app\
    │   ├── package.json                  # Frontend dependencies and scripts\
    │   ├── components/                   # Reusable UI components (buttons, cards, etc.)\
    │   ├── screens/                      # Individual pages/screens of the app\
    │   ├── navigation/                   # Navigation logic and config\
    │   ├── services/                     # API calls to backend endpoints\
    │   └── accessibility/                # Screen reader support, text scaling, etc.\

    ├── backend/                          # Python Backend (FastAPI)\
    │   ├── main.py                       # Starts the backend server\
    │   ├── requirements.txt              # Backend dependencies\
    │   ├── app/\
    │   │   ├── api/\
    │   │   │   ├── routes_tts.py         # Endpoint for text-to-speech\
    │   │   │   ├── routes_asl.py         # Endpoint for ASL generation\
    │   │   │   ├── routes_captions.py    # Endpoint for real-time transcription/subtitles\
    │   │   │   ├── routes_alt_text.py    # Endpoint for alt text generation from images\
    │   │   │   ├── routes_lms.py         # LMS integration endpoint\
    │   │   │   └── routes_auth.py        # User login/authentication (if needed)\
    │   │   ├── services/\
    │   │   │   ├── tts.py                # Logic for TTS generation\
    │   │   │   ├── asl.py                # Logic for sign language rendering\
    │   │   │   ├── captions.py           # Real-time transcription logic\
    │   │   │   ├── alt_text.py           # Caption generation for images\
    │   │   │   └── lms.py                # Logic to connect with LMS systems\
    │   │   ├── utils/                    # Helper functions and file handling\
    │   │   └── models/\
    │   │       └── model_loader.py       # Shared model loading and caching\

    ├── integrations/                     # Third-Party & Assistive Integrations (optional)\
    │   ├── lms_adapter.py                # Adapters for LMS APIs (e.g., Moodle, Canvas)\
    │   └── screen_reader_support/        # Tools for screen reader compatibility\
    
    ├── models/                           # Pretrained / Custom ML Models\  
    │   ├── whisper/                      # ASR model (e.g., Whisper)\
    │   ├── asl_generation/               # ASL pose models or video assets\
    │   └── vision_captioning/            # Image-to-text captioning models\
    
    ├── data/                             # Sample data for testing (optional)\
    │   ├── sample_texts/                 # Sample text content for TTS/ASL\
    │   ├── sample_images/                # Images for alt-text generation\
    │   └── sample_videos/                # Videos for transcription testing\
    
    ├── scripts/                          # Development & Debugging Scripts (optional)\
    │   ├── test_tts.py                   # Test script for TTS service\
    │   ├── test_transcription.py         # Test script for transcription service\
    │   └── test_alt_text.py              # Test script for image captioning\
    
    ├── docs/                             # Developer Documenatation\
    │   ├── architecture.md               # Overall system design and architecture\
    │   ├── user_flows.md                 # Describes how users interact with features\
    │   ├── api_endpoints.md              # List of backend APIs with request/response formats\
    │   ├── accessibility_standards.md    # WCAG 2.1 checklist and compliance notes\
    │   └── lms_integration.md            # Guide for LMS (e.g., Moodle) integration\
    
    └── tests/                            # Testing (optional)\
        ├── test_routes.py                # Backend route tests\
        └── test_accessibility.py         # Accessibility unit checks\
