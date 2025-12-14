# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
    - **Description:** 
      - aktueller_status: Information not found
      - key_features: Information not found
      - tech_stack: Information not found

## 2. Installation 
    ### Dependencies
    ```plaintext
    - aiohttp==4.2.2
    - annotated-types==0.7.0
    - anyio==4.11.0
    - attrs==25.4.0
    - bcrypt==5.0.0
    - blinker==1.9.0
    - cachetools==6.2.2
    - captcha==0.7.1
    - certifi==2025.11.12
    - cffi==2.0.0
    - charset-normalizer==3.4.4
    - click==8.3.1
    - colorama==0.4.6
    - contourpy==1.3.3
    - cryptography==46.0.3
    - cycler==0.12.1
    - distro==1.9.0
    - dns-python==2.8.0
    - dotenv==0.9.9
    - entrypoints==0.4
    - extra-streamlit-components==0.1.81
    - filetype==1.2.0
    - fonttools==4.61.0
    - gitdb==4.0.12
    - GitPython==3.1.45
    - google-ai-generative-language==0.9.0
    - google-api-core==2.28.1
    - google-auth==2.43.0
    - googleapis-common-protos==1.72.0
    - grpcio==1.76.0
    - grpcio-status==1.76.0
    - h11==0.16.0
    - httpcore==1.0.9
    - httpx==0.28.1
    - idna==3.11
    - Jinja2==3.1.6
    - jiter==0.12.0
    - jsonpatch==1.33
    - jsonpointer==3.0.0
    - jsonschema==4.25.1
    - jsonschema-specifications==2025.9.1
    - kiwisolver==1.4.9
    - langchain==1.0.8
    - langchain-core==1.1.0
    - langchain-google-genai==3.1.0
    - langchain-ollama==1.0.0
    - langchain-openai==1.1.0
    - langgraph==1.0.3
    - langgraph-checkpoint==3.0.1
    - langgraph-prebuilt==1.0.5
    - langsmit==0.4.46
    - MarkupSafe==3.0.3
    - matplotlib==3.10.7
    - numpy==2.3.5
    - ollama==0.6.1
    - openai==2.8.1
    - orjson==3.11.4
    - ormsgpack==1.12.0
    - packaging==25.0
    - pandas==2.3.3
    - pillow==12.0.0
    - proto-plus==1.26.1
    - protobuf==6.33.1
    - pyarrow==2.1.0
    - PyJWT==2.10.1
    - pymongo==4.15.4
    - pydantic==2.12.4
    - pydantic-core==2.41.5
    - pydieck==0.9.1
    - PyJWT==2.10.1
    - pymongo==4.15.4
    - pydantic==2.12.4
    - pydantic-core==2.41.5
    - pydieck==0.9.1
    - PyJWT==2.10.1
    - pymongo==4.15.4
    - pydantic==2.12.4
    - pydantic-core==2.41.5
    - pydieck==0.9.1
    - reference==0.3.7
    - regex==2025.11.3
    - requests==2.32.5
    - requests-toolbelt==1.0.0
    - rpds-py==0.2.9
    - rsa==4.9.1
    - setuptools==69.0.1
    - six==1.17.0
    - smmap==5.0.2
    - sniffio==1.3.1
    - streamlit==1.51.0
    - streamlit-authenticator==0.1.0
    - tenacity==9.1.2
    - tiktoken==0.12.0
    - toml==0.10.2
    - toolz==1.1.0
    - toon-format @ git+https://github.com/toon-format/toon-python.git@9c4f0c0c024f2a0b0b37
    - tornado==6.5.2
    - tqdm==4.67.1
    - typing-inspection==0.4.2
    - typing_extensions==4.15.0
    - tzdata==2025.2
    - url3==2.5.0
    - watchdog==6.0.0
    - xxhash==3.6.0
    - zstandard==0.25.0
    ```
    If Repo contains requirements.txt note: 
    ```plaintext
    pip install -r requirements.txt
    ``` 
    ### Setup Guide
    Information not found
    ### Quick Startup
    Information not found

## 3. Use Cases & Commands
Information not found.

## 4. Architecture

## 5. Code Analysis

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:** 
    *   *Description:* 
    *   *Parameters:* 
*   **Methods:** 

#### Class: `ASTAnalyzer`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:** 
    *   *Description:* 
    *   *Parameters:* 
*   **Methods:** 

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:** 
    *   *Description:* 
    *   *Parameters:* 
*   **Methods:** 

### File: `backend/HelperLLM.py`

#### Class: `LLMHelper`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:** 
    *   *Description:* 
    *   *Parameters:* 
*   **Methods:** 

### File: `backend/MainLLM.py`

#### Class: `MainLLM`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:** 
    *   *Description:* 
    *   *Parameters:* 
*   **Methods:** 

### File: `backend/basic_info.py`

#### Class: `ProjektInfoExtractor`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:** 
    *   *Description:* 
    *   *Parameters:* 
*   **Methods:** 

### File: `backend/callgraph.py`

#### Class: `CallGraph`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:** 
    *   *Description:* 
    *   *Parameters:* 
*   **Methods:** 

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:** 
    *   *Description:* 
    *   *Parameters:* 
*   **Methods:** 

#### Class: `GitRepository`
*   **Summary:** 
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:** 
    *   *Description:* 
    *   *Parameters:* 
*   **Methods:** 

### File: `database/db.py`

#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str) -> str`
*   **Description:** 
*   **Parameters:** 
    - **text** (`str`): 
*   **Returns:** 
    - **encrypted_text** (`str`): 

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str) -> str`
*   **Description:** 
*   **Parameters:** 
    - **text** (`str`): 
*   **Returns:** 
    - **result** (`str`): 

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
    - **name** (`str`): 
    - **password** (`str`): 
*   **Returns:** 
    - **inserted_id** (`ObjectId`): 

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    - **result** (`list`): 

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
*   **Returns:** 
    - **result** (`Any`): 

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
    - **new_name** (`str`): 
*   **Returns:** 
    - **result.modified_count** (`int`): 

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
    - **gemini_api_key** (`str`): 
*   **Returns:** 
    - **modified_count** (`int`): 

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
    - **ollama_base_url** (`str`): 
*   **Returns:** 
    - **modified_count** (`int`): 

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
*   **Returns:** 
    - **gemini_api_key** (`Optional[str]`): 

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
*   **Returns:** 
    - **ollama_base_url** (`Optional[str]`): 

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
*   **Returns:** 
    - **deleted_count** (`int`): 

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
*   **Returns:** 
    - **gemini_plain** (`str`): 
    - **ollama_plain** (`str`): 

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
    - **chat_name** (`str`): 
*   **Returns:** 
    - **result.inserted_id** (`str`): 

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
*   **Returns:** 
    - **chats** (`list`): 

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
    - **chat_name** (`str`): 
*   **Returns:** 
    - **exists** (`bool`): 

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
    - **old_name** (`str`): 
    - **new_name** (`str`): 
*   **Returns:** 
    - **modified_count** (`int`): 

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str = "", main_used: str = "", total_time: str = "", helper_time: str = "", main_time: str = "")`
*   **Description:** 
*   **Parameters:** 
    - **question** (`str`): 
    - **answer** (`str`): 
    - **feedback** (`str`): 
    - **username** (`str`): 
    - **chat_name** (`str`): 
    - **helper_used** (`str`): 
    - **main_used** (`str`): 
    - **total_time** (`str`): 
    - **helper_time** (`str`): 
    - **main_time** (`str`): 
*   **Returns:** 
    - **new_id** (`str`): 

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
*   **Returns:** 
    - **exchanges** (`list`): 

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
    - **chat_name** (`str`): 
*   **Returns:** 
    - **exchanges** (`list`): 

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
*   **Description:** 
*   **Parameters:** 
    - **exchange_id** (`Any`): 
    - **feedback** (`int`): 
*   **Returns:** 
    - **result.modified_count** (`int`): 

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
*   **Description:** 
*   **Parameters:** 
    - **exchange_id** (`Any`): 
    - **feedback_message** (`str`): 
*   **Returns:** 
    - **modified_count** (`int`): 

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** 
*   **Parameters:** 
    - **exchange_id** (`str`): 
*   **Returns:** 
    - **deleted_count** (`int`): 

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** 
*   **Parameters:** 
    - **username** (`str`): 
    - **chat_name** (`str`): 
*   **Returns:** 
    - **deleted_count** (`int`): 

---
</enddoc>