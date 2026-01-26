# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview
    - **Description:** 
      - Could not be determined due to a missing README file and insufficient context.
    - **Key Features:** 
      - Information not found
    - **Tech Stack:** 
      - Information not found

## 2. Installation
### Dependencies
The project dependencies are listed below:
- altair==4.2.2
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
- jsonpatch==1.33.0
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
- langs mith==0.4.46
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
- pyasrn1==0.6.1
- pyasrn1_modules==0.4.2
- pycparser==2.23
- pydantic==2.12.4
- pydantic-core==2.41.5
- pydeck==6.0.3
- referencing==0.37.0
- regex==2025.11.3
- requests==2.32.5
- requests-toolbelt==1.0.0
- rpds-py==0.29.0
- rsa==4.9.1
- setuptools==69.0.1
- six==1.17.0
- smmap==5.0.2
- sniffio==1.3.1
- streamlit==1.5.1
- streamlit-mermaid==0.1.0
- tenacity==9.1.2
- tiktoken==0.12.0
- toml==0.10.2
- toolz==1.1.0
- toon-format==9c4f0c0c2a0b0b376315f4b8707f8c9

### Setup Guide
Information not found

### Quick Startup
Information not found


## 3. Use Cases & Commands
The project appears to be a repository onboarding agent designed to streamline and automate the process of integrating new repositories into an existing development environment or platform. Key functionalities likely include:
- **Repository Cloning:** The agent can clone a given repository URL into a temporary directory for analysis.
- **Static Code Analysis:** It performs static analysis on the codebase using Abstract Syntax Trees (ASTs) to extract information about functions, classes, and their interdependencies.
- **Dependency Analysis:** The agent analyzes and documents dependencies between different parts of the codebase.
- **Documentation Generation:** It leverages Large Language Models (LLMs) to generate detailed documentation for functions and classes, including descriptions, parameters, return values, and usage context.

## 4. Architecture

## 5. Code Analysis

### File: `backend/AST_Schema.py`
#### Class: `ASTVisitor`
*   **Summary:** A class designed to traverse an Abstract Syntax Tree (AST) generated from Python source code. It collects information about imports, classes, and functions, organizing them into a structured schema.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It sets up internal tracking variables such as module path, schema structure, and current class context.
    *   *Parameters:* 
      - **self**
      - **source_code** (`str`): The full source code string of the file being analyzed.
      - **file_path** (`str`): The file path of the source code being processed.
      - **project_root** (`str`): The root directory of the project being analyzed.

### File: `backend/File_Dependency.py`
#### Class: `FileDependencyGraph`
*   **Summary:** A class designed to analyze Python file dependencies by parsing import statements and resolving both absolute and relative imports. It extends NodeVisitor to traverse AST nodes representing import structures, building a dependency graph that maps files to their imported modules.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with a filename and repository root path. Sets up the instance variables to track the current file being analyzed and the root directory of the repository for resolving relative paths.
    *   *Parameters:* 
      - **self**
      - **filename** (`str`): The name of the file being analyzed for dependencies.
      - **repo_root** (`Any`): The root directory path of the repository containing the file.

### File: `backend/HelperLLM.py`
#### Class: `LLMHelper`
*   **Summary:** A class serving as a centralized interface for interacting with various language models, particularly for generating and validating code documentation for functions and classes. It handles configuration of different LLM backends based on model names, manages batching and rate limiting for API calls, and ensures structured output using Pydantic models.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with API credentials and prompt files. It reads system prompts from specified paths, configures batch settings based on the model name, and sets up appropriate LLM clients for function and class documentation generation.
    *   *Parameters:* 
      - **self**
      - **api_key** (`str`): API key for accessing the language model service.
      - **function_prompt_path** (`str`): Path to the file containing the system prompt for function documentation generation.
      - **class_prompt_path** (`str`): Path to the file containing the system prompt for class documentation generation.
      - **model_name** (`str`): Name of the language model to use. Defaults to 'gemini-2.0-flash-lite'.
      - **base_url** (`str`): Base URL for custom API endpoints. Optional.

### File: `backend/MainLLM.py`
#### Class: `MainLLM`
*   **Summary:** A class serving as the central interface for interacting with various Large Language Models (LLMs). It supports multiple LLM providers including Google Generative AI, OpenAI-compatible APIs, and Ollama-based models. The class initializes with configuration parameters such as API keys, prompt file paths, and model specifications, and provides two core methods for interacting with the LLM: one for synchronous calls and another for streaming responses.
*   **Instantiation:** 
*   **Dependencies:** 
*   **Constructor:**
    *   *Description:* Initializes the MainLLM instance by validating the API key, loading the system prompt from a specified file, and setting up the appropriate LLM client based on the model name. It supports different LLM backends like Google Generative AI, custom OpenAI-compatible endpoints, and Ollama.
    *   *Parameters:* 
      - **self**
      - **api_key** (`str`): The API key used for authenticating with the LLM provider.
      - **prompt_file_path** (`str`): The file path to the system prompt that will be loaded and used for LLM interactions.
      - **model_name** (`str`): The name of the model to use. Determines which backend (Google, OpenAI, or Ollama) will be initialized.
      - **base_url** (`str`): Optional base URL for connecting to a custom LLM endpoint. Defaults to None.

### File: `database/db.py`
#### Function: `encrypt_text`
*   **Signature:** `def encrypt_text(text: str) -> str`
*   **Description:** The function encrypts a given text string using a cipher suite, returning the encrypted result as a string. It first checks if the input text is empty or if the cipher suite is not available, in which case it returns the original text unchanged. If both conditions are met, it encodes the stripped text to bytes, encrypts it using the cipher suite, and then decodes the result back to a string.
*   **Parameters:**
      - **text** (`str`): The text string to be encrypted.
*   **Returns:**
      - **encrypted_text** (`str`): The encrypted version of the input text, or the original text if encryption was not performed.

#### Function: `decrypt_text`
*   **Signature:** `def decrypt_text(text: str) -> str`
*   **Description:** The function decrypts a given text using a cipher suite if available; otherwise, it returns the original text unchanged. It handles potential decryption errors gracefully by returning the original text in case of exceptions. The function performs basic validation to ensure the input text and cipher suite are present before attempting decryption.
*   **Parameters:**
      - **text** (`str`): The encrypted text to be decrypted.
*   **Returns:**
      - **return_value** (`str`): The decrypted text if successful, otherwise the original input text.

#### Function: `insert_user`
*   **Signature:** `def insert_user(username: str, name: str, password: str)`
*   **Description:** The function inserts a new user into the database by creating a user document with the provided username, name, and password. The password is hashed before being stored. It also initializes additional fields such as API keys and returns the ID of the inserted document.
*   **Parameters:**
      - **username** (`str`): The unique identifier for the user, used as the '_id' field in the database.
      - **name** (`str`): The full name of the user.
      - **password** (`str`): The plain text password of the user, which gets hashed before storage.
*   **Returns:**
      - **inserted_id** (`ObjectId`): The unique identifier of the newly inserted user document in the database.

#### Function: `fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function retrieves all user documents from a MongoDB collection named 'dbusers'. It performs a database query using the 'find()' method and returns the results as a list. The function does not accept any parameters and directly accesses a global or module-level variable 'dbusers' which is expected to be a MongoDB collection object.
*   **Parameters:** 
*   **Returns:**
      - **result** (`list`): A list containing all user documents retrieved from the 'dbusers' MongoDB collection.

#### Function: `fetch_user`
*   **Signature:** `def fetch_user(username: str)`
*   **Description:** The function fetch_user retrieves a single user document from a MongoDB collection named 'dbusers' based on the provided username. It uses the find_one method to query the database with a filter that matches the '_id' field to the given username. The function assumes the existence of a global or module-level variable 'dbusers' that represents the MongoDB collection. This function serves as a simple data retrieval utility for fetching specific user information.
*   **Parameters:**
      - **username** (`str`): The unique identifier (username) used to locate and retrieve a specific user document from the MongoDB collection.
*   **Returns:**
      - **result** (`Any`): A single user document retrieved from the MongoDB collection, or None if no matching document is found.

#### Function: `update_user_name`
*   **Signature:** `def update_user_name(username: str, new_name: str)`
*   **Description:** This function updates the name field of a user document in a MongoDB collection identified by the username. It uses the MongoDB update_one method to modify only the name field, leaving other fields unchanged. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
      - **username** (`str`): The unique identifier of the user whose name needs to be updated.
      - **new_name** (`str`): The new name value to set for the specified user.
*   **Returns:**
      - **result.modified_count** (`int`): The number of documents that were modified as a result of the update operation.

#### Function: `update_gemini_key`
*   **Signature:** `def update_gemini_key(username: str, gemini_api_key: str)`
*   **Description:** This function updates a user's Gemini API key in the database after encrypting it. It takes a username and an unencrypted API key as inputs, strips any leading or trailing whitespace from the key, encrypts it using a helper function, and then updates the corresponding document in the 'dbusers' collection with the encrypted key. The function returns the number of documents modified, which should be 1 if the update was successful.
*   **Parameters:**
      - **username** (`str`): The unique identifier for the user whose Gemini API key needs to be updated.
      - **gemini_api_key** (`str`): The unencrypted Gemini API key provided by the user, which will be stripped of whitespace and encrypted before storage.
*   **Returns:**
      - **modified_count** (`int`): The number of documents that were successfully modified in the database. This should typically be 1 if the user exists and the update succeeds.

#### Function: `update_ollama_url`
*   **Signature:** `def update_ollama_url(username: str, ollama_base_url: str)`
*   **Description:** This function updates the Ollama base URL for a specified user in the database. It takes a username and a new Ollama base URL as inputs, strips any leading or trailing whitespace from the URL, and attempts to update the corresponding document in the 'dbusers' collection. The function returns the count of modified documents, which should be 1 if the update was successful or 0 if no matching document was found.
*   **Parameters:**
      - **username** (`str`): The unique identifier of the user whose Ollama base URL needs to be updated.
      - **ollama_base_url** (`str`): The new Ollama base URL to be set for the specified user. Leading and trailing whitespace will be stripped.
*   **Returns:**
      - **modified_count** (`int`): The number of documents that were successfully modified by the update operation. This will typically be 1 if the user exists, or 0 if no matching user was found.

#### Function: `fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username: str)`
*   **Description:** The function retrieves a Gemini API key associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'gemini_api_key' field. If no matching user is found, it returns None.
*   **Parameters:**
      - **username** (`str`): The unique identifier for the user whose Gemini API key is to be retrieved.
*   **Returns:**
      - **gemini_api_key** (`str` or `None`): The Gemini API key associated with the user, or None if the user is not found.

#### Function: `fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username: str)`
*   **Description:** The function retrieves the Ollama base URL associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'ollama_base_url' field. If no matching user is found, it returns None.
*   **Parameters:**
      - **username** (`str`): The unique identifier for the user whose Ollama base URL is to be retrieved.
*   **Returns:**
      - **ollama_base_url** (`str` or `None`): The Ollama base URL associated with the user, or None if the user is not found.

#### Function: `delete_user`
*   **Signature:** `def delete_user(username: str)`
*   **Description:** The function 'delete_user' removes a user document from a MongoDB collection based on the provided username. It uses the 'delete_one' method to target a specific user by their '_id', which corresponds to the username. The function returns the count of deleted documents, which will be 1 if the user was found and deleted, or 0 if no such user existed.
*   **Parameters:**
      - **username** (`str`): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
      - **deleted_count** (`int`): The number of documents deleted, either 1 if the user was found and removed, or 0 if no matching user was found.

#### Function: `get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username: str)`
*   **Description:** This function retrieves and decrypts API keys for a given username from a database. It first fetches the user document using the username as the identifier. If the user does not exist, it returns two None values. If the user exists, it attempts to decrypt the 'gemini_api_key' field using a decryption function and retrieves the 'ollama_base_url' directly. It then returns both the decrypted Gemini API key and the Ollama base URL.
*   **Parameters:**
      - **username** (`str`): The unique identifier for the user whose API keys are to be retrieved.
*   **Returns:**
      - **gemini_plain** (`str`): The decrypted Gemini API key for the user, or an empty string if not found.
      - **ollama_plain** (`str`): The Ollama base URL for the user, or an empty string if not found.

#### Function: `insert_chat`
*   **Signature:** `def insert_chat(username: str, chat_name: str)`
*   **Description:** The function 'insert_chat' creates a new chat entry in the database with a unique identifier, associated username, chat name, and creation timestamp. It generates a UUID for the chat entry, populates the necessary fields, and inserts the document into the 'dbchats' collection. The function then returns the ID of the inserted document.
*   **Parameters:**
      - **username** (`str`): The username associated with the chat.
      - **chat_name** (`str`): The name of the chat.
*   **Returns:**
      - **result.inserted_id** (`str`): The unique identifier of the newly inserted chat document.

#### Function: `fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username: str)`
*   **Description:** Die Funktion fetch_chats_by_user ruft alle Chats eines bestimmten Benutzers aus einer MongoDB-Datenbank ab. Sie verwendet den Benutzernamen als Filterkriterium und sortiert die Ergebnisse nach dem Erstellungsdatum in aufsteigender Reihenfolge. Das Ergebnis ist eine Liste der gefundenen Chat-Dokumente.
*   **Parameters:**
      - **username** (`str`): Der Benutzername, dessen Chats abgerufen werden sollen.
*   **Returns:**
      - **chats** (`list`): Eine Liste aller Chat-Dokumente des angegebenen Benutzers, sortiert nach Erstellungsdatum.

#### Function: `check_chat_exists`
*   **Signature:** `def check_chat_exists(username: str, chat_name: str)`
*   **Description:** This function checks whether a specific chat entry exists in the database for a given username and chat name. It performs a query using MongoDB's find_one method to locate a matching document. If a document is found, the function returns True; otherwise, it returns False.
*   **Parameters:**
      - **username** (`str`): The username associated with the chat.
      - **chat_name** (`str`): The name of the chat to check for existence.
*   **Returns:**
      - **exists** (`bool`): True if a chat with the specified username and chat name exists, False otherwise.

#### Function: `rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username: str, old_name: str, new_name: str)`
*   **Description:** This function renames a chat and updates all associated exchanges in the database. It first updates the chat entry in the chats collection, then updates all related exchange entries in the exchanges collection. The function returns the number of modified chat documents.
*   **Parameters:**
      - **username** (`str`): The username associated with the chat to be renamed.
      - **old_name** (`str`): The current name of the chat to be renamed.
      - **new_name** (`str`): The new name to assign to the chat.
*   **Returns:**
      - **modified_count** (`int`): The number of chat documents that were successfully modified.

#### Function: `insert_exchange`
*   **Signature:** `def insert_exchange(question: str, answer: str, feedback: str, username: str, chat_name: str, helper_used: str = "", main_used: str = "", total_time: str = "", helper_time: str = "", main_time: str = "")`
*   **Description:** This function inserts a new exchange record into a MongoDB collection. It generates a unique ID for the exchange, constructs a dictionary with all the provided details including question, answer, feedback, and metadata, and attempts to insert this record into the database. If the insertion fails, it catches the exception, prints an error message, and returns None. Otherwise, it returns the generated unique ID.
*   **Parameters:**
      - **question** (`str`): The question associated with the exchange.
      - **answer** (`str`): The answer provided in response to the question.
      - **feedback** (`str`): Feedback related to the exchange.
      - **username** (`str`): The username of the user involved in the exchange.
      - **chat_name** (`str`): The name of the chat session.
      - **helper_used** (`str`): The helper component used during the exchange (optional).
      - **main_used** (`str`): The main component used during the exchange (optional).
      - **total_time** (`str`): Total time taken for the exchange (optional).
      - **helper_time** (`str`): Time taken by the helper component (optional).
      - **main_time** (`str`): Time taken by the main component (optional).
*   **Returns:**
      - **new_id** (`str`): The unique identifier of the inserted exchange record, or None if insertion failed.

#### Function: `fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username: str)`
*   **Description:** This function retrieves all exchange records from a MongoDB collection for a given username, sorted by creation timestamp in ascending order. It uses the pymongo library to query the database and returns the results as a list. The sorting ensures that exchanges are displayed chronologically.
*   **Parameters:**
      - **username** (`str`): The username associated with the exchange records to be fetched.
*   **Returns:**
      - **exchanges** (`list`): A list of exchange records retrieved from the database, sorted by creation timestamp in ascending order.

#### Function: `fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username: str, chat_name: str)`
*   **Description:** This function retrieves a sorted list of exchanges from a MongoDB collection based on a given username and chat name. It queries the 'dbexchanges' collection with specific criteria and orders the results by creation date in ascending order. The function returns the fetched documents as a list.
*   **Parameters:**
      - **username** (`str`): The username associated with the exchanges to be retrieved.
      - **chat_name** (`str`): The name of the chat associated with the exchanges to be retrieved.
*   **Returns:**
      - **exchanges** (`list`): A list of exchange documents matching the provided username and chat name, sorted by creation date in ascending order.

#### Function: `update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback: int)`
*   **Description:** This function updates the feedback field of a document in the 'dbexchanges' collection within a MongoDB database. It takes an exchange ID and a feedback value, then attempts to update the corresponding document with the new feedback value. The function returns the count of modified documents, which should be 1 if the update was successful or 0 if no matching document was found.
*   **Parameters:**
      - **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
      - **feedback** (`int`): The feedback value to be set in the document.
*   **Returns:**
      - **modified_count** (`int`): The number of documents that were modified as a result of the update operation.

#### Function: `update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message: str)`
*   **Description:** This function updates the feedback message associated with a specific exchange document in a MongoDB collection. It takes an exchange ID and a new feedback message as inputs, then performs an atomic update operation on the database to set the feedback_message field. The function returns the count of modified documents, which should typically be 1 if the update was successful.
*   **Parameters:**
      - **exchange_id** (`Any`): The unique identifier of the exchange document to be updated.
      - **feedback_message** (`str`): The new feedback message to be stored in the exchange document.
*   **Returns:**
      - **modified_count** (`int`): The number of documents that were successfully modified by the update operation.

#### Function: `delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id: str)`
*   **Description:** This function deletes a document from the 'dbexchanges' collection in a MongoDB database based on a provided exchange ID. It performs a deletion operation using the 'delete_one' method and returns the count of deleted documents. The function takes a single string parameter representing the unique identifier of the exchange to be deleted from the database.
*   **Parameters:**
      - **exchange_id** (`str`): A string representing the unique identifier of the exchange document to be deleted from the database.
*   **Returns:**
      - **deleted_count** (`int`): An integer indicating the number of documents successfully deleted from the database. This will typically be 0 or 1.

#### Function: `delete_full_chat`
*   **Signature:** `def delete_full_chat(username: str, chat_name: str)`
*   **Description:** The function deletes all exchanges and the chat entry associated with a given username and chat name from the database. It first removes all exchange records matching the criteria, then deletes the corresponding chat record. The function returns the count of deleted chat entries, which should be 1 if the operation was successful.
*   **Parameters:**
      - **username** (`str`): The username associated with the chat to be deleted.
      - **chat_name** (`str`): The name of the chat to be deleted.
*   **Returns:**
      - **deleted_count** (`int`): The number of chat documents deleted from the database.