# Project Documentation: repo-onboarding-agent documentation

## 1. Project Overview (can be accessed under 'basic_info')
    - **Description:** Information not found
    - **Key Features:** 
      - Information not found
    - **Tech Stack:** Information not found

*   **Repository Structure:**
    ```mermaid
    graph LR
        root --> .env.example
        root --> .gitignore
        root --> SystemPrompts
        root --> analysis_output.json
        root --> backend
        root --> database
        root --> frontend
        root --> notizen
        root --> output.json
        root --> output.toon
        root --> readme.md
        root --> requirements.txt
        root --> result
        root --> schemas
        root --> statistics

        SystemPrompts --> SystemPrompts/SystemPromptClassHelperLLM.txt
        SystemPrompts --> SystemPrompts/SystemPromptFunctionHelperLLM.txt
        SystemPrompts --> SystemPrompts/SystemPromptHelperLLM.txt
        SystemPrompts --> SystemPrompts/SystemPromptMainLLM.txt
        SystemPrompts --> SystemPrompts/SystemPromptMainLLMToon.txt

        backend --> backend/AST_Schema.py
        backend --> backend/File_Dependency.py
        backend --> backend/HelperLLM.py
        backend --> backend/MainLLM.py
        backend --> backend/__init__.py
        backend --> backend/basic_info.py
        backend --> backend/callgraph.py
        backend --> backend/getRepo.py
        backend --> backend/main.py
        backend --> backend/relationship_analyzer.py
        backend --> backend/scads_key_test.py

        database --> database/db.py

        frontend --> frontend/.streamlit
        frontend --> frontend/Frontend.py
        frontend --> frontend/__init__.py
        frontend --> frontend/gifs

        frontend/.streamlit --> frontend/.streamlit/config.toml

        frontend/gifs --> frontend/gifs/4j.gif

        notizen --> notizen/Report Agenda.txt
        notizen --> notizen/Zwischenpraesentation Agenda.txt
        notizen --> notizen/doc_bestandteile.md
        notizen --> notizen/grafiken
        notizen --> notizen/notizen.md
        notizen --> notizen/paul_notizen.md
        notizen --> notizen/praesentation_notizen.md
        notizen --> notizen/technische_notizen.md

        notizen/grafiken --> notizen/grafiken/1
        notizen/grafiken --> notizen/grafiken/2
        notizen/grafiken --> notizen/grafiken/Flask-Repo
        notizen/grafiken --> notizen/grafiken/Repo-onboarding

        notizen/grafiken/1 --> notizen/grafiken/1/File_Dependency_Graph_Repo.dot
        notizen/grafiken/1 --> notizen/grafiken/1/global_callgraph.png
        notizen/grafiken/1 --> notizen/grafiken/1/global_graph.png
        notizen/grafiken/1 --> notizen/grafiken/1/global_graph_2.png
        notizen/grafiken/1 --> notizen/grafiken/1/repo.dot

        notizen/grafiken/2 --> notizen/grafiken/2/FDG_repo.dot
        notizen/grafiken/2 --> notizen/grafiken/2/fdg_graph.png
        notizen/grafiken/2 --> notizen/grafiken/2/fdg_graph_2.png
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_callgraph_flask.png
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_callgraph_repo-agent.png
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_callgraph_repo-agent_3.png
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_repo_callgraph_flask.dot
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_repo_callgraph_repo-agent-3.dot
        notizen/grafiken/2 --> notizen/grafiken/2/filtered_repo_callgraph_repo-agent.dot
        notizen/grafiken/2 --> notizen/grafiken/2/global_callgraph.png
        notizen/grafiken/2 --> notizen/grafiken/2/graph_flask.md
        notizen/grafiken/2 --> notizen/grafiken/2/repo.dot

        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/__init__.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/__main__.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/app.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/auth.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/blog.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/blueprints.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/cli.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/conf.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/config.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/conftest.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/ctx.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/db.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/debughelpers.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/factory.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/flask.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/globals.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/hello.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/helpers.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/importerrorapp.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/logging.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/make_celery.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/multiapp.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/provider.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/scaffold.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/sessions.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/signals.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/tag.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/tasks.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/templating.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_appctx.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_async.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_auth.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_basic.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_blog.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_blueprints.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_cli.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_config.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_config.png
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_converters.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_db.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_factory.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_helpers.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_instance_config.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_js_example.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_json.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_json_tag.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_logging.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_regression.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_reqctx.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_request.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_session_interface.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_signals.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_subclassing.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_templating.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_testing.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_user_error_handler.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/test_views.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/testing.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing_app_decorators.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing_error_handler.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/typing_route.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/views.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/wrappers.dot
        notizen/grafiken/Flask-Repo --> notizen/grafiken/Flask-Repo/wsgi.dot

        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/AST.dot
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/Frontend.dot
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/HelperLLM.dot
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/HelperLLM.png
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/MainLLM.dot
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/agent.dot
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/basic_info.dot
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/callgraph.dot
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/getRepo.dot
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/graph_AST.png
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/graph_AST2.png
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/graph_AST3.png
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/main.dot
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/tools.dot
        notizen/grafiken/Repo-onboarding --> notizen/grafiken/Repo-onboarding/types.dot

        result --> result/ast_schema_01_12_2025_11-49-24.json
        result --> result/report_01_12_2025_12-26-46_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result --> result/report_01_12_2025_12-55-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result --> result/report_01_12_2025_13-37-30_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result --> result/report_01_12_2025_14-15-04_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
        result --> result/report_01_12_2025_14-42-38_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
        result --> result/report_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.md
        result --> result/report_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.md
        result --> result/report_03_12_2025_22-46-01_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result --> result/report_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.md
        result --> result/report_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.md
        result --> result/report_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.md
        result --> result/report_14_11_2025_14-52-36.md
        result --> result/report_14_11_2025_15-21-53.md
        result --> result/report_14_11_2025_15-26-24.md
        result --> result/report_21_11_2025_15-43-30.md
        result --> result/report_21_11_2025_16-06-12.md
        result --> result/report_22_11_2025_14-01-50_Helper_llama3_Main_geminipro.md
        result --> result/report_22_11_2025_14-39-55_Helper_llama3_MainLLM_llama3.md
        result --> result/result_2025-11-11_12-30-53.md
        result --> result/result_2025-11-11_12-43-51.md
        result --> result/result_2025-11-11_12-45-37.md

        statistics --> statistics/savings_01_12_2025_15-27-23_Helper_gemini-2.5-flash-lite_MainLLM_gemini-2.5-pro.png
        statistics --> statistics/savings_02_12_2025_15-41-27_Helper_gemini-2.5-flash_MainLLM_gemini-2.5-pro.png
        statistics --> statistics/savings_03_12_2025_23-13-20_Helper_gemini-flash-latest_MainLLM_gemini-2.5-pro.png
        statistics --> statistics/savings_05_12_2025_11-07-10_Helper_alias-ha_MainLLM_gemini-2.5-pro.png
        statistics --> statistics/savings_09_12_2025_14-07-49_Helper_alias-code_MainLLM_alias-ha.png
    ```

    ## 2. Installation (can be accessed under 'basic_info')
    ### Dependencies
    - a l t a i r = = 4 . 2 . 2 
    -  
    -  a n n o t a t e d - t y p e s = = 0 . 7 . 0 
    -  
    -  a n y i o = = 4 . 1 1 . 0 
    -  
    -  a t t r s = = 2 5 . 4 . 0 
    -  
    -  b c r y p t = = 5 . 0 . 0 
    -  
    -  b l i n k e r = = 1 . 9 . 0 
    -  
    -  c a c h e t o o l s = = 6 . 2 . 2 
    -  
    -  c a p t c h a = = 0 . 7 . 1 
    -  
    -  c e r t i f i = = 2 0 2 5 . 1 1 . 1 2 
    -  
    -  c f f i = = 2 . 0 . 0 
    -  
    -  c h a r s e t - n o r m a l i z e r = = 3 . 4 . 4 
    -  
    -  c l i c k = = 8 . 3 . 1 
    -  
    -  c o l o r a m a = = 0 . 4 . 6 
    -  
    -  c o n t o u r p y = = 1 . 3 . 3 
    -  
    -  c r y p t o g r a p h y = = 4 6 . 0 . 3 
    -  
    -  c y c l e r = = 0 . 1 2 . 1 
    -  
    -  d i s t r o = = 1 . 9 . 0 
    -  
    -  d n s p y t h o n = = 2 . 8 . 0 
    -  
    -  d o t e n v = = 0 . 9 . 9 
    -  
    -  e n t r y p o i n t s = = 0 . 4 
    -  
    -  e x t r a - s t r e a m l i t - c o m p o n e n t s = = 0 . 1 . 8 1 
    -  
    -  f i l e t y p e = = 1 . 2 . 0 
    -  
    -  f o n t t o o l s = = 4 . 6 1 . 0 
    -  
    -  g i t d b = = 4 . 0 . 1 2 
    -  
    -  G i t P y t h o n = = 3 . 1 . 4 5 
    -  
    -  g o o g l e - a i - g e n e r a t i v e l a n g u a g e = = 0 . 9 . 0 
    -  
    -  g o o g l e - a p i - c o r e = = 2 . 2 8 . 1 
    -  
    -  g o o g l e - a u t h = = 2 . 4 3 . 0 
    -  
    -  g o o g l e a p i s - c o m m o n - p r o t o s = = 1 . 7 2 . 0 
    -  
    -  g r p c i o = = 1 . 7 6 . 0 
    -  
    -  g r p c i o - s t a t u s = = 1 . 7 6 . 0 
    -  
    -  h 1 1 = = 0 . 1 6 . 0 
    -  
    -  h t t p c o r e = = 1 . 0 . 9 
    -  
    -  h t t p x = = 0 . 2 8 . 1 
    -  
    -  i d n a = = 3 . 1 1 
    -  
    -  J i n j a 2 = = 3 . 1 . 6 
    -  
    -  j i t e r = = 0 . 1 2 . 0 
    -  
    -  j s o n p a t c h = = 1 . 3 3 
    -  
    -  j s o n p o i n t e r = = 3 . 0 . 0 
    -  
    -  j s o n s c h e m a = = 4 . 2 5 . 1 
    -  
    -  j s o n s c h e m a - s p e c i f i c a t i o n s = = 2 0 2 5 . 9 . 1 
    -  
    -  k i w i s o l v e r = = 1 . 4 . 9 
    -  
    -  l a n g c h a i n = = 1 . 0 . 8 
    -  
    -  l a n g c h a i n - c o r e = = 1 . 1 . 0 
    -  
    -  l a n g c h a i n - g o o g l e - g e n a i = = 3 . 1 . 0 
    -  
    -  l a n g c h a i n - o l l a m a = = 1 . 0 . 0 
    -  
    -  l a n g c h a i n - o p e n a i = = 1 . 1 . 0 
    -  
    -  l a n g g r a p h = = 1 . 0 . 3 
    -  
    -  l a n g g r a p h - c h e c k p o i n t = = 3 . 0 . 1 
    -  
    -  l a n g g r a p h - p r e b u i l t = = 1 . 0 . 5 
    -  
    -  l a n g g r a p h - s d k = = 0 . 2 . 9 
    -  
    -  l a n g s m i t h = = 0 . 4 . 4 6 
    -  
    -  M a r k u p S a f e = = 3 . 0 . 3 
    -  
    -  m a t p l o t l i b = = 3 . 1 0 . 7 
    -  
    -  n a r w h a l s = = 2 . 1 2 . 0 
    -  
    -  n e t w o r k x = = 3 . 6 
    -  
    -  n u m p y = = 2 . 3 . 5 
    -  
    -  o l l a m a = = 0 . 6 . 1 
    -  
    -  o p e n a i = = 2 . 8 . 1 
    -  
    -  o r j s o n = = 3 . 1 1 . 4 
    -  
    -  o r m s g p a c k = = 1 . 1 2 . 0 
    -  
    -  p a c k a g i n g = = 2 5 . 0 
    -  
    -  p a n d a s = = 2 . 3 . 3 
    -  
    -  p i l l o w = = 1 2 . 0 . 0 
    -  
    -  p r o t o - p l u s = = 1 . 2 6 . 1 
    -  
    -  p r o t o b u f = = 6 . 3 3 . 1 
    -  
    -  p y a r r o w = = 2 1 . 0 . 0 
    -  
    -  p y a s n 1 = = 0 . 6 . 1 
    -  
    -  p y a s n 1 _ m o d u l e s = = 0 . 4 . 2 
    -  
    -  p y c p a r s e r = = 2 . 2 3 
    -  
    -  p y d a n t i c = = 2 . 1 2 . 4 
    -  
    -  p y d a n t i c _ c o r e = = 2 . 4 1 . 5 
    -  
    -  p y d e c k = = 0 . 9 . 1 
    -  
    -  P y J W T = = 2 . 1 0 . 1 
    -  
    -  p y m o n g o = = 4 . 1 5 . 4 
    -  
    -  p y p a r s i n g = = 3 . 2 . 5 
    -  
    -  p y t h o n - d a t e u t i l = = 2 . 9 . 0 . p o s t 0 
    -  
    -  p y t h o n - d o t e n v = = 1 . 2 . 1 
    -  
    -  p y t z = = 2 0 2 5 . 2 
    -  
    -  P y Y A M L = = 6 . 0 . 3 
    -  
    -  r e f e r e n c i n g = = 0 . 3 7 . 0 
    -  
    -  r e g e x = = 2 0 2 5 . 1 1 . 3 
    -  
    -  r e q u e s t s = = 2 . 3 2 . 5 
    -  
    -  r e q u e s t s - t o o l b e l t = = 1 . 0 . 0 
    -  
    -  r p d s - p y = = 0 . 2 9 . 0 
    -  
    -  r s a = = 4 . 9 . 1 
    -  
    -  s e t u p t o o l s = = 7 5 . 9 . 1 
    -  
    -  s i x = = 1 . 1 7 . 0 
    -  
    -  s m m a p = = 5 . 0 . 2 
    -  
    -  s n i f f i o = = 1 . 3 . 1 
    -  
    -  s t r e a m l i t = = 1 . 5 1 . 0 
    -  
    -  s t r e a m l i t - a u t h e n t i c a t o r = = 0 . 4 . 2 
    -  
    -  s t r e a m l i t - m e r m a i d = = 0 . 3 . 0 
    -  
    -  t e n a c i t y = = 9 . 1 . 2 
    -  
    -  t i k t o k e n = = 0 . 1 2 . 0 
    -  
    -  t o m l = = 0 . 1 0 . 2 
    -  
    -  t o o l z = = 1 . 1 . 0 
    -  
    -  t o o n _ f o r m a t   @   g i t + h t t p s : / / g i t h u b . c o m / t o o n - f o r m a t / t o o n - p y t h o n . g i t @ 9 c 4 f 0 c 0 c 2 4 f 2 a 0 b 0 b 3 7 6 3 1 5 f 4 b 8 7 0 7 f 8 c 9 0 0 6 d e 6 
    -  
    -  t o r n a d o = = 6 . 5 . 2 
    -  
    -  t q d m = = 4 . 6 7 . 1 
    -  
    -  t y p i n g - i n s p e c t i o n = = 0 . 4 . 2 
    -  
    -  t y p i n g _ e x t e n s i o n s = = 4 . 1 5 . 0 
    -  
    -  t z d a t a = = 2 0 2 5 . 2 
    -  
    -  u r l l i b 3 = = 2 . 5 . 0 
    -  
    -  w a t c h d o g = = 6 . 0 . 0 
    -  
    -  x x h a s h = = 3 . 6 . 0 
    -  
    -  z s t a n d a r d = = 0 . 2 5 . 0 
    -  
    -  "
    ### Setup Guide
    Information not found
    ### Quick Startup
    Information not found

3. **Use Cases & Commands**
This project appears to be a documentation generation pipeline that analyzes GitHub repositories. It clones repositories, parses their code using Abstract Syntax Trees (AST), analyzes relationships between code components (functions, classes), and leverages Large Language Models (LLMs) to generate documentation.

Key use cases include:
*   **Automated Code Documentation:** Generating comprehensive documentation for Python projects hosted on GitHub.
*   **Repository Analysis:** Understanding the structure, dependencies, and call graphs within a codebase.
*   **LLM-Powered Insights:** Utilizing LLMs to provide natural language descriptions and analysis of code components.
*   **Format Comparison:** Evaluating the efficiency of different data serialization formats (JSON vs. TOON) for documentation storage and transmission, including token usage and savings.

Primary commands or workflows would likely involve:
*   Providing a GitHub repository URL as input.
*   Configuring API keys for LLM services (e.g., Gemini, OpenAI, Ollama).
*   Specifying LLM models for different stages of the documentation process.
*   Executing the main workflow which orchestrates the entire analysis and documentation generation pipeline.

4. **Architecture**
The Mermaid Syntax to visualize Graphs is not set up yet and will be added
but if there is mermaid syntax in your input json display it here

5. **Code Analysis**

### File: `backend/AST_Schema.py`

#### Class: `ASTVisitor`
*   **Summary:** The ASTVisitor class is designed to traverse an Abstract Syntax Tree (AST) generated from Python source code. It collects information about imports, classes, and functions, organizing them into a structured schema. The visitor maintains context for class definitions and their methods, allowing for detailed analysis of modules, including their structure, dependencies, and relationships.
*   **Instantiation:** `analyze_repository` in `AST_Schema.py`
*   **Dependencies:** `ast`, `networkx`, `os`, `callgraph.build_filtered_callgraph`, `getRepo.GitRepository`
*   **Constructor:**
    *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It sets up internal tracking variables such as module path, schema structure, and current class context.
    *   *Parameters:*
        *   **source_code** (str): The full source code string of the file being analyzed.
        *   **file_path** (str): The file path of the source code being processed.
        *   **project_root** (str): The root directory of the project being analyzed.
*   **Methods:**
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import nodes in the AST by extracting the names of imported modules and appending them to the schema's imports list. It ensures that all imports are recorded for further analysis.
        *   *Parameters:*
            *   **node** (ast.Import): An AST node representing an import statement.
        *   *Returns:*
        *   **Usage:** This method is called automatically by the AST traversal mechanism when an import node is encountered.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Processes import-from nodes in the AST by collecting the fully qualified names of imported items and adding them to the schema's imports list. It supports both direct imports and relative imports.
        *   *Parameters:*
            *   **node** (ast.ImportFrom): An AST node representing an import-from statement.
        *   *Returns:*
        *   **Usage:** This method is called automatically by the AST traversal mechanism when an import-from node is encountered.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Handles class definition nodes in the AST by creating a structured representation of the class, including its identifier, name, docstring, and source code segment. It also tracks the class in the schema and sets the current class context for subsequent method processing.
        *   *Parameters:*
            *   **node** (ast.ClassDef): An AST node representing a class definition.
        *   *Returns:*
        *   **Usage:** This method is called automatically by the AST traversal mechanism when a class definition node is encountered.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Processes function definition nodes in the AST. If a class context is active, it records the function as a method of that class. Otherwise, it treats the function as a top-level function and adds it to the schema accordingly. It captures details like arguments, docstrings, and source segments.
        *   *Parameters:*
            *   **node** (ast.FunctionDef): An AST node representing a function definition.
        *   *Returns:*
        *   **Usage:** This method is called automatically by the AST traversal mechanism when a function definition node is encountered.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definition nodes in the AST by delegating to the standard function definition handler. This allows async functions to be treated similarly to regular functions during schema collection.
        *   *Parameters:*
            *   **node** (ast.AsyncFunctionDef): An AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:** This method is called automatically by the AST traversal mechanism when an async function definition node is encountered.

#### Class: `ASTAnalyzer`
*   **Summary:** The ASTAnalyzer class is responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs) and enriching the resulting schema with call graph information. It merges relationship data into the schema and supports repository-wide analysis by processing multiple files and building a structured representation of functions, classes, and their relationships.
*   **Instantiation:** `HelperLLM_evaluation.py` (line 128), `MainLLM_evaluation.py` (line 131), `main.py` (line 187)
*   **Dependencies:** `ast`, `networkx`, `os`, `callgraph.build_filtered_callgraph`, `getRepo.GitRepository`
*   **Constructor:**
    *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any initialization actions.
    *   *Parameters:*
*   **Methods:**
    *   **`_enrich_schema_with_callgraph`**
        *   *Signature:* `def _enrich_schema_with_callgraph(self, schema, call_graph, filename)`
        *   *Description:* Enriches a given schema with call graph information by adding 'calls' and 'called_by' details for functions and methods based on a provided call graph. It iterates through functions and class methods in the schema and updates their context with successors and predecessors from the call graph.
        *   *Parameters:*
            *   **schema** (dict): A dictionary representing the schema containing functions and classes.
            *   **call_graph** (nx.DiGraph): A NetworkX directed graph representing the call relationships between functions and methods.
            *   **filename** (str): The filename associated with the schema being enriched.
        *   *Returns:*
        *   **Usage:** This method is called by the analyze_repository method.
    *   **`merge_relationship_data`**
        *   *Signature:* `def merge_relationship_data(self, full_schema, relationship_data)`
        *   *Description:* Merges relationship data into a full schema by updating function and class context with 'called_by' information. It builds a lookup table from the relationship data and applies this information to functions, classes, and methods within the schema.
        *   *Parameters:*
            *   **full_schema** (dict): A dictionary representing the full schema of the repository.
            *   **relationship_data** (list): A list of dictionaries containing relationship information for identifiers.
        *   *Returns:*
            *   **full_schema** (dict): The updated schema with merged relationship data.
        *   **Usage:** This method is called by the evaluation function in HelperLLM_evaluation.py, the prepare_shared_input function in MainLLM_evaluation.py, and the main_workflow function in main.py.
    *   **`analyze_repository`**
        *   *Signature:* `def analyze_repository(self, files, repo)`
        *   *Description:* Analyzes a repository by processing a list of files, parsing their content into ASTs, and generating a schema for each file. It enriches the schema with call graph information and aggregates results into a full schema structure. Handles errors during parsing and filters out non-Python files.
        *   *Parameters:*
            *   **files** (list): A list of file objects to be analyzed.
            *   **repo** (GitRepository): An object representing the Git repository being analyzed.
        *   *Returns:*
            *   **full_schema** (dict): A dictionary containing the aggregated schema for all processed files.
        *   **Usage:** This method is called by the evaluation function in HelperLLM_evaluation.py, the prepare_shared_input function in MainLLM_evaluation.py, and the main_workflow function in main.py.

### File: `backend/File_Dependency.py`

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze Python file dependencies by parsing import statements and resolving both absolute and relative imports. It extends NodeVisitor to traverse AST nodes representing import structures, building a dependency graph that maps files to their imported modules. The class handles complex relative imports by resolving module names against the repository structure and checks for symbol existence in package __init__.py files. It maintains a dictionary of import dependencies for each file, which can be used to construct a call graph or visualize module relationships.
*   **Instantiation:** `build_file_dependency_graph` in `File_Dependency.py`
*   **Dependencies:** `networkx`, `os`, `ast.Assign`, `ast.AST`, `ast.ClassDef`, `ast.FunctionDef`, `ast.Import`, `ast.ImportFrom`, `ast.Name`, `ast.NodeVisitor`, `ast.literal_eval`, `ast.parse`, `ast.walk`, `keyword.iskeyword`, `pathlib.Path`, `getRepo.GitRepository`, `callgraph.make_safe_dot`
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with a filename and repository root path. Sets up the instance variables to track the current file being analyzed and the root directory of the repository for resolving relative paths.
    *   *Parameters:*
        *   **filename** (str): The name of the file being analyzed for dependencies.
        *   **repo_root** (Any): The root directory path of the repository containing the file.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* Resolves relative import statements by analyzing the import node and mapping it to actual module or symbol names. It determines the correct base directory based on the import level and checks whether the resolved modules or symbols exist in the repository structure. The method supports both direct module file existence checks and symbol resolution through __init__.py files. It raises ImportError if no valid module or symbol can be resolved.
        *   *Parameters:*
            *   **node** (ImportFrom): An AST node representing a relative import statement.
        *   *Returns:*
            *   A list of resolved module or symbol names.
        *   **Usage:** This method calls helper functions 'module_file_exists' and 'init_exports_symbol' to check for module existence and symbol availability in __init__.py files respectively.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name=None)`
        *   *Description:* Handles import statements by adding the imported module names to the dependency tracking dictionary. It ensures that the current file's dependencies are recorded under its filename key in the import_dependencies dictionary. The method supports both regular imports and those with base names derived from more complex import structures.
        *   *Parameters:*
            *   **node** (Import | ImportFrom): An AST node representing an import statement.
            *   **base_name** (str | None): Optional base name for the imported module, used in complex import cases.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal of the AST.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Processes 'from ... import ...' style import statements by extracting the module name and delegating to visit_Import for handling. For relative imports without explicit module names, it attempts to resolve the module names using _resolve_module_name. If resolution fails, it prints an error message but continues processing.
        *   *Parameters:*
            *   **node** (ImportFrom): An AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method calls '_resolve_module_name' to resolve relative imports and 'visit_Import' to record dependencies.

#### Function: `backend.File_Dependency.build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It takes a filename, an abstract syntax tree (AST), and a repository root path as inputs. It uses a custom visitor class to traverse the AST and extract import dependencies. These dependencies are then added to a NetworkX DiGraph, where nodes represent files and edges represent dependency relationships.
*   **Parameters:**
    *   **filename** (str): The name of the file being analyzed for dependencies.
    *   **tree** (AST): The abstract syntax tree of the file being analyzed.
    *   **repo_root** (str): The root directory path of the repository being analyzed.
*   **Returns:**
    *   **graph** (nx.DiGraph): A NetworkX directed graph representing file dependencies, where nodes are files and edges indicate import relationships.
*   **Usage:** This function is called by the 'build_repository_graph' function in the 'File_Dependency.py' file at line 177.

#### Function: `backend.File_Dependency.build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function constructs a dependency graph for all Python files within a given Git repository. It iterates through each Python file, parses its content into an abstract syntax tree (AST), and builds a file-level dependency graph. These individual graphs are then merged into a single global directed graph representing dependencies across the entire repository. The function ensures that only Python files are processed and properly handles nodes and edges in the resulting graph.
*   **Parameters:**
    *   **repository** (GitRepository): The Git repository object containing the files to analyze for dependencies.
*   **Returns:**
    *   **global_graph** (nx.DiGraph): A NetworkX directed graph representing the dependency relationships between Python files in the repository.
*   **Usage:** This function is called by the backend.File_Dependency module at line 200 in File_Dependency.py.

#### Function: `backend.File_Dependency.get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function retrieves all Python files (.py) from a specified directory and its subdirectories, returning them as relative paths from the given directory. It uses pathlib to resolve the directory path and recursively searches for files with the .py extension.
*   **Parameters:**
    *   **directory** (str): The path to the directory from which to search for Python files.
*   **Returns:**
    *   A list of Path objects representing all Python files found in the directory and its subdirectories, relative to the specified directory.
*   **Usage:** This function is called by _resolve_module_name in File_Dependency.py at line 43.

### File: `backend/HelperLLM.py`

#### Function: `backend.HelperLLM.main_orchestrator`
*   **Signature:** `def main_orchestrator()`
*   **Description:** The main_orchestrator function serves as a dummy data and processing loop for testing the LLMHelper class. It defines pre-computed analysis for several example functions including add_item, check_stock, and generate_report, and simulates the process of generating documentation for these functions using an LLMHelper instance. The function sets up mock inputs and expected outputs for these functions, initializes an LLMHelper with specific prompt files, and processes the results to build a final documentation structure.
*   **Parameters:**
*   **Returns:**
*   **Usage:** backend.HelperLLM (line 419 in HelperLLM.py)

#### Class: `LLMHelper`
*   **Summary:** The LLMHelper class serves as a centralized interface for interacting with various language models, particularly for generating and validating code documentation for functions and classes. It handles configuration of different LLM backends based on model names, manages batching and rate limiting for API calls, and ensures structured output using Pydantic models. The class supports multiple providers including Google Gemini, OpenAI, custom APIs, and Ollama, with appropriate batch size configurations per model.
*   **Instantiation:** `HelperLLM.py` (line 387), `HelperLLM_evaluation.py` (line 222), `MainLLM_evaluation.py` (line 214), `main.py` (line 284)
*   **Dependencies:** `os`, `json`, `logging`, `time`, `typing.List`, `typing.Dict`, `typing.Any`, `typing.Optional`, `typing.Union`, `dotenv.load_dotenv`, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI`, `langchain.messages.HumanMessage`, `langchain.messages.SystemMessage`, `langchain.messages.AIMessage`, `pydantic.ValidationError`, `schemas.types.FunctionAnalysis`, `schemas.types.ClassAnalysis`, `schemas.types.FunctionAnalysisInput`, `schemas.types.FunctionContextInput`, `schemas.types.ClassAnalysisInput`, `schemas.types.ClassContextInput`
*   **Constructor:**
    *   *Description:* Initializes the LLMHelper with API credentials and prompt files. It reads system prompts from specified paths, configures batch settings based on the model name, and sets up appropriate LLM clients for function and class documentation generation. The initialization also validates the presence of required API keys and handles different model types by selecting the correct backend client.
    *   *Parameters:*
        *   **api_key** (str): API key for accessing the language model service.
        *   **function_prompt_path** (str): Path to the file containing the system prompt for function documentation generation.
        *   **class_prompt_path** (str): Path to the file containing the system prompt for class documentation generation.
        *   **model_name** (str): Name of the language model to use. Defaults to 'gemini-2.0-flash-lite'.
        *   **base_url** (str): Base URL for custom API endpoints. Optional.
*   **Methods:**
    *   **`_configure_batch_settings`**
        *   *Signature:* `def _configure_batch_settings(self, model_name)`
        *   *Description:* Configures the batch size for processing requests based on the specified model name. It assigns different batch sizes depending on the model type, defaulting to a conservative value for unknown models. This method ensures efficient processing while respecting model-specific constraints.
        *   *Parameters:*
            *   **model_name** (str): Name of the language model for which to configure batch settings.
        *   *Returns:*
        *   **Usage:** This method is called during the initialization of the LLMHelper class.
    *   **`generate_for_functions`**
        *   *Signature:* `def generate_for_functions(self, function_inputs)`
        *   *Description:* Processes a batch of function inputs to generate and validate documentation using the configured LLM. It divides inputs into batches according to the configured batch size, sends them to the LLM for processing, and handles errors gracefully by returning None values for failed items. Rate limiting is enforced between batches to comply with API constraints.
        *   *Parameters:*
            *   **function_inputs** (List[FunctionAnalysisInput]): A list of function input models containing information needed for documentation generation.
        *   *Returns:*
            *   A list of validated function analysis results or None for failed items.
        *   **Usage:** This method is called by evaluation, prepare_shared_input, and main_workflow functions.
    *   **`generate_for_classes`**
        *   *Signature:* `def generate_for_classes(self, class_inputs)`
        *   *Description:* Processes a batch of class inputs to generate and validate documentation using the configured LLM. Similar to generate_for_functions, it batches inputs, sends them to the LLM, and handles errors by returning None values for failed items. Rate limiting is applied between batches to respect API constraints.
        *   *Parameters:*
            *   **class_inputs** (List[ClassAnalysisInput]): A list of class input models containing information needed for documentation generation.
        *   *Returns:*
            *   A list of validated class analysis results or None for failed items.
        *   **Usage:** This method is called by evaluation, prepare_shared_input, and main_workflow functions.

### File: `backend/callgraph.py`

#### Function: `backend.callgraph.make_safe_dot`
*   **Signature:** `def make_safe_dot(graph, out_path)`
*   **Description:** The function 'make_safe_dot' takes a NetworkX directed graph and a file path as inputs. It creates a copy of the graph and generates a safe node naming scheme by prefixing each original node name with 'n' followed by its index. The function then relabels the nodes in the graph according to this safe naming scheme and assigns the original node names as labels to the new nodes. Finally, it writes the modified graph to a DOT file at the specified output path.
*   **Parameters:**
    *   **graph** (nx.DiGraph): A NetworkX directed graph object to be processed and saved.
    *   **out_path** (str): The file path where the DOT representation of the graph will be written.
*   **Returns:**
*   **Usage:** This function is called by 'backend.callgraph' in the file 'callgraph.py' at line 244.

#### Function: `backend.callgraph.build_filtered_callgraph`
*   **Signature:** `def build_filtered_callgraph(repo)`
*   **Description:** Die Funktion erstellt einen globalen Call-Graphen basierend auf allen Python-Dateien eines Git-Repositories und filtert diesen anschließend, sodass nur Aufrufe zwischen selbst geschriebenen Funktionen erhalten bleiben. Sie durchläuft alle Dateien, parst deren Inhalt mit dem Abstract Syntax Tree (AST), extrahiert Funktionsaufrufe und baut einen gerichteten Graphen auf, der nur die relevanten Verbindungen zwischen eigenen Funktionen enthält.
*   **Parameters:**
    *   **repo** (GitRepository): Ein Objekt, das Zugriff auf alle Dateien des Git-Repositories bietet.
*   **Returns:**
    *   **global_graph** (nx.DiGraph): Ein gerichteter Graph, der die Aufrufbeziehungen zwischen selbst geschriebenen Funktionen darstellt.
*   **Usage:** Diese Funktion wird von 'analyze_repository' in 'AST_Schema.py' und von 'backend.callgraph' in 'callgraph.py' aufgerufen.

#### Class: `CallGraph`
*   **Summary:** The CallGraph class is designed to construct a call graph from Python AST nodes, tracking function and method calls within a given file. It uses the Abstract Syntax Tree (AST) visitor pattern to traverse the code and builds a directed graph representing these relationships. The class maintains mappings for local definitions, imports, and function names to resolve and track inter-function dependencies. It supports handling of classes, functions, asynchronous functions, imports, and conditional blocks like main block detection.
*   **Instantiation:** `build_filtered_callgraph` in `callgraph.py` (lines 199, 206)
*   **Dependencies:** `ast`, `networkx`
*   **Constructor:**
    *   *Description:* Initializes the CallGraph with a filename and sets up internal data structures including local definitions, a directed graph, import mappings, a function set, and edges for tracking function calls.
    *   *Parameters:*
        *   **filename** (str): The name of the file being processed to build the call graph.
*   **Methods:**
    *   **`_recursive_call`**
        *   *Signature:* `def _recursive_call(self, node)`
        *   *Description:* Recursively extracts the dotted name components from an AST node representing a function or attribute call. It handles different types of AST nodes such as ast.Call, ast.Name, and ast.Attribute to build a list of name parts.
        *   *Parameters:*
            *   **node** (ast.AST): The AST node to extract name components from.
        *   *Returns:*
            *   parts (list[str]): A list of strings representing the dotted name components.
        *   **Usage:** This method is called by the _resolve_all_callee_names method.
    *   **`_resolve_all_callee_names`**
        *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
        *   *Description:* Resolves a list of dotted name components into full qualified names by checking local definitions, import mappings, and constructing appropriate names based on current class context. It processes each component list to determine the correct fully qualified name for each callee.
        *   *Parameters:*
            *   **callee_nodes** (list[list[str]]): A list of lists containing name components for callees.
        *   *Returns:*
            *   resolved (list[str]): A list of fully qualified names for the callees.
        *   **Usage:** This method is called by the visit_Call method.
    *   **`_make_full_name`**
        *   *Signature:* `def _make_full_name(self, basename, class_name=None)`
        *   *Description:* Constructs a fully qualified name for a function or method by combining the filename, optional class name, and base name. This helps in uniquely identifying functions within the context of a file and class hierarchy.
        *   *Parameters:*
            *   **basename** (str): The base name of the function or method.
            *   **class_name** (Optional[str]): The name of the class if the function belongs to one.
        *   *Returns:*
            *   full_name (str): The fully qualified name constructed from the filename, class name, and base name.
        *   **Usage:** This method is called by the visit_FunctionDef method.
    *   **`_current_caller`**
        *   *Signature:* `def _current_caller(self)`
        *   *Description:* Determines the current caller's name, either from the current function or defaults to a global scope identifier if no function is active. This is used to label nodes in the call graph.
        *   *Parameters:*
        *   *Returns:*
            *   caller (str): The name of the current caller.
        *   **Usage:** This method is called by the visit_Call method.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST by mapping aliases to their actual module names. It updates the import mapping dictionary to resolve imported names later during call resolution.
        *   *Parameters:*
            *   **node** (ast.Import): The AST node representing an import statement.
        *   *Returns:*
        *   **Usage:** This method is called by the AST visitor framework.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements by extracting the module name and mapping aliases to their respective modules. It updates the import mapping dictionary accordingly.
        *   *Parameters:*
            *   **node** (ast.ImportFrom): The AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method is called by the AST visitor framework.
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Processes class definitions in the AST by temporarily setting the current class name and visiting the class body. After processing, it restores the previous class name to maintain proper scoping.
        *   *Parameters:*
            *   **node** (ast.ClassDef): The AST node representing a class definition.
        *   *Returns:*
        *   **Usage:** This method is called by the AST visitor framework.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Processes function definitions by creating a fully qualified name for the function, updating local definitions, adding the function to the graph, and visiting the function body. It also tracks the function in a set for future reference.
        *   *Parameters:*
            *   **node** (ast.FunctionDef): The AST node representing a function definition.
        *   *Returns:*
        *   **Usage:** This method is called by the AST visitor framework.
    *   **`visit_AsyncFunctionDef`**
        *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
        *   *Description:* Handles asynchronous function definitions by delegating to the standard function definition handler. This ensures that async functions are treated similarly to regular functions in terms of call graph construction.
        *   *Parameters:*
            *   **node** (ast.AsyncFunctionDef): The AST node representing an asynchronous function definition.
        *   *Returns:*
        *   **Usage:** This method is called by the AST visitor framework.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Processes function calls in the AST by determining the caller, resolving the callee names, and recording the edge in the call graph. It manages the edges dictionary to store function call relationships.
        *   *Parameters:*
            *   **node** (ast.Call): The AST node representing a function call.
        *   *Returns:*
        *   **Usage:** This method is called by the AST visitor framework.
    *   **`visit_If`**
        *   *Signature:* `def visit_If(self, node)`
        *   *Description:* Handles conditional statements, specifically detecting when the condition checks for '__name__ == '__main__''. In such cases, it temporarily sets the current function to '<main_block>' before visiting the conditional body and then restores the original function name.
        *   *Parameters:*
            *   **node** (ast.If): The AST node representing an if statement.
        *   *Returns:*
        *   **Usage:** This method is called by the AST visitor framework.

### File: `backend/main.py`

#### Function: `backend.main.create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** Die Funktion erstellt ein Balkendiagramm zur Darstellung des Token-Vergleichs zwischen JSON und TOON Format. Sie verwendet matplotlib zur Erstellung des Diagramms und speichert das Ergebnis in einer Datei. Das Diagramm zeigt die Anzahl der Token für beide Formate sowie den prozentualen Einsparungswert. Die Funktion setzt einen Titel mit dem Einsparungsprozentsatz, fügt eine y-Achsenbeschriftung hinzu und zeigt die Werte über den Balken an.
*   **Parameters:**
    *   **json_tokens** (int): Die Anzahl der Token im JSON-Format.
    *   **toon_tokens** (int): Die Anzahl der Token im TOON-Format.
    *   **savings_percent** (float): Der prozentuale Einsparungswert zwischen den beiden Formaten.
    *   **output_path** (str): Der Dateipfad, unter dem das generierte Diagramm gespeichert wird.
*   **Returns:**
*   **Usage:** Die Funktion wird von der Funktion 'main_workflow' in der Datei 'main.py' aufgerufen.

#### Function: `backend.main.calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** The function calculates the net time duration between a start and end time, excluding sleep times caused by rate limits. It specifically adjusts the calculation when the model name starts with 'gemini-', applying a correction based on the number of batches and a fixed sleep interval per batch. If the total items count is zero, it returns zero directly. The result is never negative, ensuring a non-negative net time.
*   **Parameters:**
    *   **start_time** (float or datetime): The starting timestamp or time value.
    *   **end_time** (float or datetime): The ending timestamp or time value.
    *   **total_items** (int): The total number of items processed.
    *   **batch_size** (int): The size of each processing batch.
    *   **model_name** (str): The name of the model being used, which determines whether rate limit adjustments are applied.
*   **Returns:**
    *   **net_time** (float or int): The calculated net time after subtracting sleep durations, ensuring a minimum value of zero.
*   **Usage:** This function is called by the evaluation function in HelperLLM_evaluation.py at lines 249 and 275, and by the main_workflow function in main.py at lines 311 and 342.

#### Function: `backend.main.main_workflow`
*   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive code analysis pipeline that processes a GitHub repository input. It begins by extracting API keys and model names, then clones the repository and analyzes its structure. The function performs static analysis on the codebase using various components like AST analyzers, relationship analyzers, and information extractors. It prepares inputs for a helper LLM to analyze functions and classes, and subsequently calls a main LLM to generate a final documentation report. The workflow includes error handling, logging, and performance metrics collection.
*   **Parameters:**
    *   **input**: The input containing the repository URL to be analyzed.
    *   **api_keys** (dict): A dictionary containing API keys for different services such as Gemini, OpenAI, and SCADsLLM.
    *   **model_names** (dict): A dictionary specifying the names of models to be used for helper and main LLMs.
    *   **status_callback** (Callable[[str], None]): An optional callback function to report progress updates.
*   **Returns:**
    *   **report** (str): The final documentation report generated by the main LLM.
    *   **metrics** (dict): Performance metrics including execution times and model names used.
*   **Usage:** This function is called by both 'frontend.Frontend' in 'Frontend.py' at line 489 and 'backend.main' in 'main.py' at line 533.

#### Function: `backend.main.update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** The function 'update_status' is designed to handle status updates by invoking an optional callback function if one is defined, followed by logging the message using the standard logging module. It serves as a centralized mechanism for reporting status messages throughout the application.
*   **Parameters:**
    *   **msg**: The status message to be processed and logged.
*   **Returns:**
*   **Usage:** This function is called multiple times by the 'main_workflow' function in 'main.py', specifically at lines 81, 134, 158, 167, 175, 185, 195, 205, 301, 333, 336, 409, 412, and 430.

### File: `backend/relationship_analyzer.py`

#### Function: `backend.relationship_analyzer.path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles cases where the filepath is not under the project root by falling back to the basename of the file. If the resulting path ends with '__init__', it removes the trailing part to correctly represent the package structure.
*   **Parameters:**
    *   **filepath** (str): The absolute or relative path to a Python file.
    *   **project_root** (str): The root directory of the project used to compute the relative path.
*   **Returns:**
    *   **module_path** (str): A dot-separated module path derived from the given file path.
*   **Usage:** This function is called by _collect_definitions and __init__ methods in relationship_analyzer.py.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is responsible for analyzing Python project structures by identifying definitions (functions, classes, methods) and tracking their interdependencies through call relationships. It recursively scans a given project root directory to find Python files, parses their Abstract Syntax Trees (ASTs) to extract definitions, and resolves function calls between these definitions. The analyzer maintains internal data structures such as a dictionary of definitions and a call graph to store relationships. After processing, it formats and returns the collected information in a structured output.
*   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
*   **Dependencies:** `ast`, `os`, `logging`, `collections.defaultdict`
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer with a project root directory. Sets up internal data structures including a dictionary for storing definitions, a defaultdict for maintaining a call graph, and a dictionary for caching ASTs of processed files. Also defines a set of directories to ignore during scanning.
    *   *Parameters:*
        *   **project_root** (str): The absolute path to the root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* The main analysis method that orchestrates the process of finding Python files, collecting definitions from those files, resolving call relationships, and formatting the results. It iterates over all Python files in the project, collects definitions and resolves calls for each file, clears cached ASTs after processing, and finally returns formatted results.
        *   *Parameters:*
        *   *Returns:*
            *   output_list (list): A list of dictionaries containing information about each definition and the callers that reference it.
        *   **Usage:** This method is called by functions in HelperLLM_evaluation.py, MainLLM_evaluation.py, and main.py.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* Recursively walks through the project root directory and identifies all Python (.py) files while excluding certain directories such as .git, venv, etc. It returns a list of absolute paths to these Python files.
        *   *Parameters:*
        *   *Returns:*
            *   py_files (list): A list of absolute file paths to Python source files found in the project.
        *   **Usage:** This method is called by the `analyze` method.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* Parses a given Python file's content into an AST and extracts definitions such as functions, classes, and methods. It associates each definition with metadata like file location and line number. It also handles errors during parsing by logging them and marking the file's AST as None.
        *   *Parameters:*
            *   **filepath** (str): The absolute path to the Python file whose definitions need to be collected.
        *   *Returns:*
        *   **Usage:** This method is called by the `analyze` method.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* Given an AST node and a tree, this method attempts to find the parent node of the specified node by walking the AST. It is used to determine whether a function or method definition belongs to a class.
        *   *Parameters:*
            *   **tree** (ast.AST): The AST tree to search within.
            *   **node** (ast.AST): The AST node for which the parent needs to be found.
        *   *Returns:*
            *   parent (ast.AST or None): The parent AST node of the given node, or None if not found.
        *   **Usage:** This method is called by the `_collect_definitions` method.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* Resolves function calls within a given Python file by using a CallResolverVisitor to traverse the AST and identify calls. It updates the global call graph with the resolved call relationships. Errors during resolution are logged.
        *   *Parameters:*
            *   **filepath** (str): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
        *   **Usage:** This method is called by the `analyze` method.
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* Formats the collected definitions and call relationships into a structured list of dictionaries. Each dictionary contains details about a definition and a list of callers that reference it. Duplicate calls are removed, and the result is sorted by file and line number.
        *   *Parameters:*
        *   *Returns:*
            *   output_list (list): A list of dictionaries representing definitions and their callers, formatted for output.
        *   **Usage:** This method is called by the `analyze` method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST (Abstract Syntax Tree) visitor designed to analyze Python code and resolve call relationships between functions and methods. It tracks the current execution context (such as class and function names) and records calls made within the code. Additionally, it maintains scope information for imports and resolves qualified names for function calls. It also tracks instance types to determine the class of objects being instantiated.
*   **Instantiation:** `relationship_analyzer.py` (line 92)
*   **Dependencies:** None explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes the CallResolverVisitor with the file path, project root, and a set of definitions. It sets up internal tracking structures such as scope, instance types, and call records, and determines the module path based on the file path and project root.
    *   *Parameters:*
        *   **filepath** (str): The path to the Python file being analyzed.
        *   **project_root** (str): The root directory of the project, used to compute relative module paths.
        *   **definitions** (dict): A dictionary containing known definitions (functions, classes, etc.) to resolve call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Handles the visiting of class definitions in the AST. It updates the current class name context before traversing the class body and restores the previous class name after traversal.
        *   *Parameters:*
            *   **node** (ast.ClassDef): The AST node representing the class definition.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Handles the visiting of function definitions in the AST. It updates the current caller name context to the function name before traversing the function body and restores the previous caller name after traversal.
        *   *Parameters:*
            *   **node** (ast.FunctionDef): The AST node representing the function definition.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Processes function calls in the AST. It resolves the qualified name of the called function and records the call if the resolved name exists in the definitions. It also tracks the caller's context (module, method, or function) and stores call metadata including file, line number, and caller information.
        *   *Parameters:*
            *   **node** (ast.Call): The AST node representing the function call.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST. It adds imported names to the current scope, mapping aliases to their actual names for later resolution.
        *   *Parameters:*
            *   **node** (ast.Import): The AST node representing the import statement.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements in the AST. It computes the full module path for relative imports and maps imported names to their fully qualified names in the scope.
        *   *Parameters:*
            *   **node** (ast.ImportFrom): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* Handles assignment statements in the AST. Specifically, it identifies assignments to instances of classes defined in the project and records the class type associated with the assigned variable.
        *   *Parameters:*
            *   **node** (ast.Assign): The AST node representing the assignment statement.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* A helper method that resolves the qualified name of a function call. It handles both simple names and attribute access (e.g., obj.method). For simple names, it checks the scope and constructs a local qualified name. For attribute access, it uses stored instance types or scope mappings to resolve the full path.
        *   *Parameters:*
            *   **func_node** (ast.AST): The AST node representing the function being called.
        *   *Returns:*
            *   qualified_name (str or None): The fully qualified name of the function, or None if it cannot be resolved.
        *   **Usage:** This method is called by the `visit_Call` method to resolve the qualified name of a function call.

### File: `backend/getRepo.py`

#### Class: `RepoFile`
*   **Summary:** The RepoFile class represents a single file within a Git repository. It implements lazy loading for file metadata such as content and size to optimize performance by only loading data when necessary. The class provides properties to access these lazily-loaded attributes and includes utility methods for basic file analysis and serialization.
*   **Instantiation:** `get_all_files` in `getRepo.py`
*   **Dependencies:** None explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes a RepoFile object with a file path and a commit tree. Sets up internal attributes for lazy loading including blob, content, and size.
    *   *Parameters:*
        *   **file_path** (str): The path to the file within the repository.
        *   **commit_tree** (git.Tree): The tree object of the commit from which the file originates.
*   **Methods:**
    *   **`blob`**
        *   *Signature:* `def blob(self)`
        *   *Description:* A property that lazily loads and returns the Git Blob object associated with the file. If the blob hasn't been loaded yet, it attempts to retrieve it from the commit tree using the stored file path. Raises a FileNotFoundError if the file cannot be found in the commit tree.
        *   *Parameters:*
        *   *Returns:*
            *   blob (git.Blob): The Git Blob object representing the file.
        *   **Usage:** This method is not called by any other functions according to the provided context.
    *   **`content`**
        *   *Signature:* `def content(self)`
        *   *Description:* A property that lazily loads and returns the decoded UTF-8 content of the file. If the content hasn't been loaded yet, it reads the data stream from the blob and decodes it, ignoring encoding errors. Returns the decoded string representation of the file's content.
        *   *Parameters:*
        *   *Returns:*
            *   content (str): The decoded content of the file.
        *   **Usage:** This method is not called by any other functions according to the provided context.
    *   **`size`**
        *   *Signature:* `def size(self)`
        *   *Description:* A property that lazily loads and returns the size of the file in bytes. If the size hasn't been determined yet, it retrieves the size directly from the blob object. Returns the integer size of the file.
        *   *Parameters:*
        *   *Returns:*
            *   size (int): The size of the file in bytes.
        *   **Usage:** This method is not called by any other functions according to the provided context.
    *   **`analyze_word_count`**
        *   *Signature:* `def analyze_word_count(self)`
        *   *Description:* An example analysis method that counts the number of words in the file's content. It splits the content on whitespace and returns the length of the resulting list, effectively counting the words.
        *   *Parameters:*
        *   *Returns:*
            *   word_count (int): The total number of words in the file's content.
        *   **Usage:** This method is not called by any other functions according to the provided context.
    *   **`__repr__`**
        *   *Signature:* `def __repr__(self)`
        *   *Description:* Provides a useful string representation of the RepoFile object, displaying the file path for debugging and logging purposes.
        *   *Parameters:*
        *   *Returns:*
            *   repr_string (str): A string representation of the RepoFile object.
        *   **Usage:** This method is not called by any other functions according to the provided context.
    *   **`to_dict`**
        *   *Signature:* `def to_dict(self, include_content=False)`
        *   *Description:* Serializes the RepoFile object into a dictionary format. Includes basic file information like path, name, size, and type. Optionally includes the file's content if requested. Uses os.path.basename to extract the filename from the path.
        *   *Parameters:*
            *   **include_content** (bool): If True, includes the file's content in the returned dictionary.
        *   *Returns:*
            *   data (dict): A dictionary containing file metadata and optionally the content.
        *   **Usage:** This method is not called by any other functions according to the provided context.

#### Class: `GitRepository`
*   **Summary:** The GitRepository class manages a Git repository by cloning it into a temporary directory and providing functionality to access files and their hierarchical structure. It supports retrieving all files as RepoFile objects, constructing a file tree representation, and cleaning up the temporary directory upon closing. The class implements context manager protocols (__enter__ and __exit__) to facilitate automatic resource management.
*   **Instantiation:** `HelperLLM_evaluation.py` (line 86), `MainLLM_evaluation.py` (line 116), `main.py` (line 141)
*   **Dependencies:** `tempfile`, `shutil`, `git.Repo`, `git.GitCommandError`, `logging`, `os`
*   **Constructor:**
    *   *Description:* Initializes a GitRepository instance by cloning the specified repository URL into a temporary directory. It sets up necessary attributes such as the repository URL, temporary directory path, and references to the cloned repository and its latest commit. If cloning fails, it raises a RuntimeError after attempting to clean up resources.
    *   *Parameters:*
        *   **repo_url** (str): The URL of the Git repository to clone.
*   **Methods:**
    *   **`get_all_files`**
        *   *Signature:* `def get_all_files(self)`
        *   *Description:* Retrieves a list of all files in the repository and creates RepoFile instances for each file. These instances are stored in the internal 'files' attribute and returned. The method uses git ls-files to obtain the file paths and filters out any empty entries.
        *   *Parameters:*
        *   *Returns:*
            *   list[RepoFile]: A list of RepoFile instances representing all files in the repository.
        *   **Usage:** This method is called by the function prepare_shared_input in MainLLM_evaluation.py at line 117.
    *   **`close`**
        *   *Signature:* `def close(self)`
        *   *Description:* Deletes the temporary directory and its contents associated with the repository. It also resets the temp_dir attribute to None to indicate that cleanup has occurred.
        *   *Parameters:*
        *   *Returns:*
        *   **Usage:** This method is called by the function prepare_shared_input in MainLLM_evaluation.py at line 136.
    *   **`__enter__`**
        *   *Signature:* `def __enter__(self)`
        *   *Description:* Enables the use of the GitRepository instance in a 'with' statement, returning itself so that it can be used within the context block.
        *   *Parameters:*
        *   *Returns:*
            *   self (GitRepository): The GitRepository instance itself.
        *   **Usage:** This method is not directly called by any other function according to the provided context.
    *   **`__exit__`**
        *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
        *   *Description:* Implements the context manager protocol's exit behavior by calling the close() method when exiting a 'with' block, ensuring proper cleanup of the temporary directory.
        *   *Parameters:*
            *   **exc_type** (Any): Exception type if an exception was raised in the with block.
            *   **exc_val** (Any): Exception value if an exception was raised in the with block.
            *   **exc_tb** (Any): Exception traceback if an exception was raised in the with block.
        *   *Returns:*
        *   **Usage:** This method is not directly called by any other function according to the provided context.
    *   **`get_file_tree`**
        *   *Signature:* `def get_file_tree(self, include_content=False)`
        *   *Description:* Constructs a hierarchical tree representation of the repository's file structure. If no files have been loaded yet, it retrieves them first. Then, it iterates through each file and builds nested dictionaries reflecting the folder hierarchy, appending each file as a leaf node at the appropriate level.
        *   *Parameters:*
            *   **include_content** (bool): Flag indicating whether to include file content in the returned dictionary representation.
        *   *Returns:*
            *   tree (dict): A dictionary representing the hierarchical file tree structure.
        *   **Usage:** This method is called by the function prepare_shared_input in MainLLM_evaluation.py at line 125.

### File: `database/db.py`

#### Function: `database.db.encrypt_text`
*   **Signature:** `def encrypt_text(text)`
*   **Description:** The function encrypts a given text string using a cipher suite, returning the encrypted result as a string. It first checks if the input text is empty or if the cipher suite is not available, in which case it returns the original text unchanged. If both conditions are met, it encodes the stripped text to bytes, encrypts it using the cipher suite, and then decodes the result back to a string.
*   **Parameters:**
    *   **text** (str): The text string to be encrypted.
*   **Returns:**
    *   encrypted_text (str): The encrypted version of the input text, or the original text if encryption was not performed.
*   **Usage:** This function is called by the update_gemini_key function in the db.py file.

#### Function: `database.db.decrypt_text`
*   **Signature:** `def decrypt_text(text)`
*   **Description:** The function decrypts a given text using a cipher suite if available; otherwise, it returns the original text unchanged. It handles potential decryption errors gracefully by returning the original text in case of exceptions. The function performs basic validation to ensure the input text and cipher suite are present before attempting decryption.
*   **Parameters:**
    *   **text** (str): The encrypted text to be decrypted.
*   **Returns:**
    *   return_value (str): The decrypted text if successful, otherwise the original input text.
*   **Usage:** This function is called by get_decrypted_api_keys in db.py at line 93.

#### Function: `database.db.insert_user`
*   **Signature:** `def insert_user(username, name, password)`
*   **Description:** The function inserts a new user into the database by creating a user document with the provided username, name, and password. The password is hashed before being stored. It also initializes additional fields such as API keys and returns the ID of the inserted document.
*   **Parameters:**
    *   **username** (str): The unique identifier for the user, used as the '_id' field in the database.
    *   **name** (str): The full name of the user.
    *   **password** (str): The plain text password of the user, which gets hashed before storage.
*   **Returns:**
    *   inserted_id (ObjectId): The unique identifier of the newly inserted user document in the database.
*   **Usage:** This function is called by the 'frontend.Frontend' class in the 'Frontend.py' file at line 294.

#### Function: `database.db.fetch_all_users`
*   **Signature:** `def fetch_all_users()`
*   **Description:** This function retrieves all user documents from a MongoDB collection named 'dbusers'. It performs a database query using the 'find()' method and returns the results as a list. The function does not accept any parameters and directly accesses a global or module-level variable 'dbusers' which is expected to be a MongoDB collection object.
*   **Parameters:**
*   **Returns:**
    *   result (list): A list containing all user documents retrieved from the 'dbusers' MongoDB collection.
*   **Usage:** This function is called by the 'frontend.Frontend' class in the 'Frontend.py' file at line 244.

#### Function: `database.db.fetch_user`
*   **Signature:** `def fetch_user(username)`
*   **Description:** The function fetch_user retrieves a single user document from a MongoDB collection named 'dbusers' based on the provided username. It uses the find_one method to query the database with a filter that matches the '_id' field to the given username. The function assumes the existence of a global or module-level variable 'dbusers' that represents the MongoDB collection. This function serves as a simple data retrieval utility for fetching specific user information.
*   **Parameters:**
    *   **username** (str): The unique identifier (username) used to locate and retrieve a specific user document from the MongoDB collection.
*   **Returns:**
    *   result (Any): A single user document retrieved from the MongoDB collection, or None if no matching document is found.
*   **Usage:** This function is not called by any other functions within the provided context.

#### Function: `database.db.update_user_name`
*   **Signature:** `def update_user_name(username, new_name)`
*   **Description:** This function updates the name field of a user document in a MongoDB collection identified by the username. It uses the MongoDB update_one method to modify only the name field, leaving other fields unchanged. The function returns the count of modified documents, which indicates whether the update was successful.
*   **Parameters:**
    *   **username** (str): The unique identifier of the user whose name needs to be updated.
    *   **new_name** (str): The new name value to set for the specified user.
*   **Returns:**
    *   result.modified_count (int): The number of documents that were modified as a result of the update operation.
*   **Usage:** This function is not called by any other functions according to the provided context.

#### Function: `database.db.update_gemini_key`
*   **Signature:** `def update_gemini_key(username, gemini_api_key)`
*   **Description:** This function updates a user's Gemini API key in the database after encrypting it. It takes a username and an unencrypted API key as inputs, strips any leading or trailing whitespace from the key, encrypts it using a helper function, and then updates the corresponding document in the 'dbusers' collection with the encrypted key. The function returns the number of documents modified, which should be 1 if the update was successful.
*   **Parameters:**
    *   **username** (str): The unique identifier for the user whose Gemini API key needs to be updated.
    *   **gemini_api_key** (str): The unencrypted Gemini API key provided by the user, which will be stripped of whitespace and encrypted before storage.
*   **Returns:**
    *   modified_count (int): The number of documents that were successfully modified in the database. This should typically be 1 if the user exists and the update succeeds.
*   **Usage:** This function is called by save_gemini_cb in Frontend.py at line 42 and by frontend.Frontend in Frontend.py at line 407.

#### Function: `database.db.update_ollama_url`
*   **Signature:** `def update_ollama_url(username, ollama_base_url)`
*   **Description:** This function updates the Ollama base URL for a specified user in the database. It takes a username and a new Ollama base URL as inputs, strips any leading or trailing whitespace from the URL, and attempts to update the corresponding document in the 'dbusers' collection. The function returns the count of modified documents, which should be 1 if the update was successful or 0 if no matching document was found.
*   **Parameters:**
    *   **username** (str): The unique identifier of the user whose Ollama base URL needs to be updated.
    *   **ollama_base_url** (str): The new Ollama base URL to be set for the specified user. Leading and trailing whitespace will be stripped.
*   **Returns:**
    *   modified_count (int): The number of documents that were successfully modified by the update operation. This will typically be 1 if the user exists, or 0 if no matching user was found.
*   **Usage:** This function is called by save_ollama_cb in Frontend.py at line 42 and by frontend.Frontend in Frontend.py at line 407.

#### Function: `database.db.fetch_gemini_key`
*   **Signature:** `def fetch_gemini_key(username)`
*   **Description:** The function retrieves a Gemini API key associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'gemini_api_key' field. If no matching user is found, it returns None.
*   **Parameters:**
    *   **username** (str): The unique identifier for the user whose Gemini API key is to be retrieved.
*   **Returns:**
    *   gemini_api_key (str or None): The Gemini API key associated with the user, or None if the user is not found.
*   **Usage:** This function is not called by any other functions according to the provided context.

#### Function: `database.db.fetch_ollama_url`
*   **Signature:** `def fetch_ollama_url(username)`
*   **Description:** The function retrieves the Ollama base URL associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'ollama_base_url' field. If no matching user is found, it returns None.
*   **Parameters:**
    *   **username** (str): The unique identifier for the user whose Ollama base URL is to be retrieved.
*   **Returns:**
    *   ollama_base_url (str or None): The Ollama base URL associated with the user, or None if the user is not found.
*   **Usage:** This function is not called by any other functions according to the provided context.

#### Function: `database.db.delete_user`
*   **Signature:** `def delete_user(username)`
*   **Description:** The function 'delete_user' removes a user document from a MongoDB collection based on the provided username. It uses the 'delete_one' method to target a specific user by their '_id', which corresponds to the username. The function returns the count of deleted documents, which will be 1 if the user was found and deleted, or 0 if no such user existed.
*   **Parameters:**
    *   **username** (str): The unique identifier (username) of the user to be deleted from the database.
*   **Returns:**
    *   deleted_count (int): The number of documents deleted, either 1 if the user was found and removed, or 0 if no matching user was found.
*   **Usage:** This function is not called by any other functions within the provided context.

#### Function: `database.db.get_decrypted_api_keys`
*   **Signature:** `def get_decrypted_api_keys(username)`
*   **Description:** This function retrieves and decrypts API keys for a given username from a database. It first fetches the user document using the username as the identifier. If the user does not exist, it returns two None values. If the user exists, it attempts to decrypt the 'gemini_api_key' field using a decryption function and retrieves the 'ollama_base_url' directly. It then returns both the decrypted Gemini API key and the Ollama base URL.
*   **Parameters:**
    *   **username** (str): The unique identifier for the user whose API keys are to be retrieved.
*   **Returns:**
    *   gemini_plain (str): The decrypted Gemini API key for the user, or an empty string if not found.
    *   ollama_plain (str): The Ollama base URL for the user, or an empty string if not found.
*   **Usage:** This function is called by the frontend.Frontend class in Frontend.py at lines 380 and 479.

#### Function: `database.db.insert_chat`
*   **Signature:** `def insert_chat(username, chat_name)`
*   **Description:** The function 'insert_chat' creates a new chat entry in the database with a unique identifier, associated username, chat name, and creation timestamp. It generates a UUID for the chat entry, populates the necessary fields, and inserts the document into the 'dbchats' collection. The function then returns the ID of the inserted document.
*   **Parameters:**
    *   **username** (str): The username associated with the chat.
    *   **chat_name** (str): The name of the chat.
*   **Returns:**
    *   result.inserted_id (str): The unique identifier of the newly inserted chat document.
*   **Usage:** This function is called by load_data_from_db in Frontend.py at line 81, handle_delete_chat in Frontend.py at line 122, and frontend.Frontend in Frontend.py at line 344.

#### Function: `database.db.fetch_chats_by_user`
*   **Signature:** `def fetch_chats_by_user(username)`
*   **Description:** Die Funktion fetch_chats_by_user ruft alle Chats eines bestimmten Benutzers aus einer MongoDB-Datenbank ab. Sie verwendet den Benutzernamen als Filterkriterium und sortiert die Ergebnisse nach dem Erstellungsdatum in aufsteigender Reihenfolge. Das Ergebnis ist eine Liste der gefundenen Chat-Dokumente.
*   **Parameters:**
    *   **username** (str): Der Benutzername, dessen Chats abgerufen werden sollen.
*   **Returns:**
    *   chats (list): Eine Liste aller Chat-Dokumente des angegebenen Benutzers, sortiert nach Erstellungsdatum.
*   **Usage:** Die Funktion wird von der Funktion load_data_from_db in der Datei Frontend.py aufgerufen.

#### Function: `database.db.check_chat_exists`
*   **Signature:** `def check_chat_exists(username, chat_name)`
*   **Description:** "This function checks whether a specific chat entry exists in the database for a given username and chat name. It performs a query using MongoDB's find_one method to locate a matching document. If a document is found, the function returns True; otherwise, it returns False."
*   **Parameters:**
    *   **username** (str): The username associated with the chat.
    *   **chat_name** (str): The name of the chat to check for existence.
*   **Returns:**
    *   exists (bool): True if a chat with the specified username and chat name exists, False otherwise.
*   **Usage:** This function is not called by any other functions according to the provided context.

#### Function: `database.db.rename_chat_fully`
*   **Signature:** `def rename_chat_fully(username, old_name, new_name)`
*   **Description:** "This function renames a chat and updates all associated exchanges in the database. It first updates the chat entry in the chats collection, then updates all related exchange entries in the exchanges collection. The function returns the number of modified chat documents."
*   **Parameters:**
    *   **username** (str): The username associated with the chat to be renamed.
    *   **old_name** (str): The current name of the chat to be renamed.
    *   **new_name** (str): The new name to assign to the chat.
*   **Returns:**
    *   modified_count (int): The number of chat documents that were successfully modified.
*   **Usage:** This function is called by the frontend.Frontend function in Frontend.py at line 462.

#### Function: `database.db.insert_exchange`
*   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used='', main_used='', total_time='', helper_time='', main_time='')`
*   **Description:** "This function inserts a new exchange record into a MongoDB collection. It generates a unique ID for the exchange, constructs a dictionary with all the provided details including question, answer, feedback, and metadata, and attempts to insert this record into the database. If the insertion fails, it catches the exception, prints an error message, and returns None. Otherwise, it returns the generated unique ID."
*   **Parameters:**
    *   **question** (str): The question associated with the exchange.
    *   **answer** (str): The answer provided in response to the question.
    *   **feedback** (str): Feedback related to the exchange.
    *   **username** (str): The username of the user involved in the exchange.
    *   **chat_name** (str): The name of the chat session.
    *   **helper_used** (str): The helper component used during the exchange (optional).
    *   **main_used** (str): The main component used during the exchange (optional).
    *   **total_time** (str): Total time taken for the exchange (optional).
    *   **helper_time** (str): Time taken by the helper component (optional).
    *   **main_time** (str): Time taken by the main component (optional).
*   **Returns:**
    *   new_id (str): The unique identifier of the inserted exchange record, or None if insertion failed.
*   **Usage:** This function is called by the frontend.Frontend class in the Frontend.py file at line 530.

#### Function: `database.db.fetch_exchanges_by_user`
*   **Signature:** `def fetch_exchanges_by_user(username)`
*   **Description:** "This function retrieves all exchange records from a MongoDB collection for a given username, sorted by creation timestamp in ascending order. It uses the pymongo library to query the database and returns the results as a list. The sorting ensures that exchanges are displayed chronologically."
*   **Parameters:**
    *   **username** (str): The username associated with the exchange records to be fetched.
*   **Returns:**
    *   exchanges (list): A list of exchange records retrieved from the database, sorted by creation timestamp in ascending order.
*   **Usage:** This function is called by the load_data_from_db function in Frontend.py at line 64.

#### Function: `database.db.fetch_exchanges_by_chat`
*   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
*   **Description:** This function retrieves a sorted list of exchanges from a MongoDB collection based on a given username and chat name. It queries the 'dbexchanges' collection with specific criteria and orders the results by creation date in ascending order. The function returns the fetched documents as a list.
*   **Parameters:**
    *   **username** (str): The username associated with the exchanges to be retrieved.
    *   **chat_name** (str): The name of the chat associated with the exchanges to be retrieved.
*   **Returns:**
    *   exchanges (list): A list of exchange documents matching the provided username and chat name, sorted by creation date in ascending order.
*   **Usage:** The function is not called by any other functions according to the provided context.

#### Function: `database.db.update_exchange_feedback`
*   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
*   **Description:** "This function updates the feedback field of a document in the 'dbexchanges' collection within a MongoDB database. It takes an exchange ID and a feedback value, then attempts to update the corresponding document with the new feedback value. The function returns the count of modified documents, which should be 1 if the update was successful."
*   **Parameters:**
    *   **exchange_id**: The unique identifier of the exchange document to be updated.
    *   **feedback** (int): The feedback value to be set in the document.
*   **Returns:**
    *   modified_count (int): The number of documents that were modified as a result of the update operation.
*   **Usage:** This function is called by 'handle_feedback_change' in 'Frontend.py'.

#### Function: `database.db.update_exchange_feedback_message`
*   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
*   **Description:** "This function updates the feedback message associated with a specific exchange document in a MongoDB collection. It takes an exchange ID and a new feedback message as inputs, then performs an atomic update operation on the database to set the feedback_message field. The function returns the count of modified documents, which should typically be 1 if the update was successful."
*   **Parameters:**
    *   **exchange_id**: The unique identifier of the exchange document to be updated.
    *   **feedback_message** (str): The new feedback message to be stored in the exchange document.
*   **Returns:**
    *   modified_count (int): The number of documents that were successfully modified by the update operation.
*   **Usage:** This function is called by the render_exchange function in the Frontend.py file at line 211.

#### Function: `database.db.delete_exchange_by_id`
*   **Signature:** `def delete_exchange_by_id(exchange_id)`
*   **Description:** This function deletes a document from the 'dbexchanges' collection in a MongoDB database based on a provided exchange ID. It performs a deletion operation using the 'delete_one' method and returns the count of deleted documents. The function takes a single string parameter representing the unique identifier of the exchange to be deleted.
*   **Parameters:**
    *   **exchange_id** (str): A string representing the unique identifier of the exchange document to be deleted from the database.
*   **Returns:**
    *   deleted_count (int): An integer indicating the number of documents successfully deleted from the database. This will typically be 0 or 1.
*   **Usage:** This function is called by 'handle_delete_exchange' in 'Frontend.py' at line 102.

#### Function: `database.db.delete_full_chat`
*   **Signature:** `def delete_full_chat(username, chat_name)`
*   **Description:** "The function deletes all exchanges and the chat entry associated with a given username and chat name from the database. It first removes all exchange records matching the criteria, then deletes the corresponding chat record. The function returns the count of deleted chat entries, which should be 1 if the operation was successful."
*   **Parameters:**
    *   **username** (str): The username associated with the chat to be deleted.
    *   **chat_name** (str): The name of the chat to be deleted.
*   **Returns:**
    *   deleted_count (int): The number of chat documents deleted from the database.
*   **Usage:** This function is called by the handle_delete_chat function in the Frontend.py file.

### File: `frontend/Frontend.py`

#### Function: `frontend.Frontend.save_gemini_cb`
*   **Signature:** `def save_gemini_cb()`
*   **Description:** "This function handles the saving of a Gemini API key entered by the user in a Streamlit frontend application. It retrieves the key from the session state, updates the database with the new key for the current user, clears the input field, and displays a success message to the user. The function does not take any parameters and does not return any value."
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function is not called by any other functions according to the provided context.

#### Function: `frontend.Frontend.save_ollama_cb`
*   **Signature:** `def save_ollama_cb()`
*   **Description:** "This function is designed to save a new Ollama URL entered by the user into the database. It retrieves the URL from the Streamlit session state, checks if it's non-empty, and then updates the database with the new URL associated with the current user. Upon successful update, it displays a success message to the user via a toast notification."
*   **Parameters:**
*   **Returns:**
*   **Usage:** This function is not called by any other function within the provided context.

#### Function: `frontend.Frontend.load_data_from_db`
*   **Signature:** `def load_data_from_db(username)`
*   **Description:** "Die Funktion 'load_data_from_db' lädt Chats und Exchanges konsistent aus einer Datenbank für einen bestimmten Benutzer. Sie prüft zunächst, ob der Benutzer bereits geladen wurde, und lädt nur dann neue Daten, wenn dies erforderlich ist. Zunächst werden Chats aus der Datenbank abgerufen und in den Session-State eingefügt. Anschließend werden Exchanges geladen und den entsprechenden Chats zugeordnet. Bei Bedarf wird ein Standard-Chat erstellt und als aktiv markiert."
*   **Parameters:**
    *   **username** (str): Der Name des Benutzers, für den die Daten aus der Datenbank geladen werden sollen.
*   **Returns:**
*   **Usage:** Die Funktion wird von der Methode 'frontend.Frontend' in der Datei 'Frontend.py' auf Zeile 310 aufgerufen.

#### Function: `frontend.Frontend.handle_feedback_change`
*   **Signature:** `def handle_feedback_change(ex, val)`
*   **Description:** "This function updates the feedback value for a given exchange object in the database and triggers a re-render of the Streamlit application. It takes an exchange dictionary and a new feedback value, updates the feedback field in the dictionary, saves the updated feedback to the database using the exchange ID, and then refreshes the Streamlit UI."
*   **Parameters:**
    *   **ex** (dict): A dictionary representing an exchange object, expected to contain at least '_id' and 'feedback' keys.
    *   **val**: The new feedback value to be assigned to the exchange object.
*   **Returns:**
*   **Usage:** This function is called by the 'render_exchange' function in 'Frontend.py' at lines 199 and 204.

#### Function: `frontend.Frontend.handle_delete_exchange`
*   **Signature:** `def handle_delete_exchange(chat_name, ex)`
*   **Description:** "This function handles the deletion of an exchange from the database and updates the session state accordingly. It first deletes the exchange from the database using its ID, then checks if the exchange exists in the session state for a given chat and removes it if found. Finally, it triggers a rerun of the Streamlit app to reflect the changes."
*   **Parameters:**
    *   **chat_name** (str): The name of the chat from which the exchange should be removed.
    *   **ex** (dict): A dictionary representing the exchange to be deleted, expected to contain an '_id' key.
*   **Returns:**
*   **Usage:** This function is called by render_exchange in Frontend.py at lines 228 and 234.

#### Function: `frontend.Frontend.handle_delete_chat`
*   **Signature:** `def handle_delete_chat(username, chat_name)`
*   **Description:** "The function handles the deletion of a chat by first removing the chat from the database and then cleaning up the session state. It ensures that the active chat is updated appropriately, either by switching to another existing chat or creating a new default chat if none remain. Finally, it triggers a rerun of the Streamlit app to reflect the changes."
*   **Parameters:**
    *   **username** (str): The username associated with the chat to be deleted.
    *   **chat_name** (str): The name of the chat to be deleted.
*   **Returns:**
*   **Usage:** "This function is called by the frontend module, specifically from the Frontend class in Frontend.py at line 367."

#### Function: `frontend.Frontend.extract_repo_name`
*   **Signature:** `def extract_repo_name(text)`
*   **Description:** "The function 'extract_repo_name' takes a text input and attempts to extract a repository name from any URL present in the text. It uses regular expressions to find a URL, parses it using urllib.parse.urlparse, extracts the path component, and then derives the repository name from the last segment of the path. If the repository name ends with '.git', it removes the extension. If no URL is found or the path is empty, it returns None."
*   **Parameters:**
    *   **text** (str): A string that may contain a URL from which to extract the repository name.
*   **Returns:**
    *   repo_name (str): The extracted repository name from the URL, with '.git' suffix removed if present.
    *   None: Returned when no valid URL is found in the input text or when the URL path is empty.
*   **Usage:** "This function is called by the 'frontend.Frontend' class, specifically at line 442 in the file 'Frontend.py'."

#### Function: `frontend.Frontend.stream_text_generator`
*   **Signature:** `def stream_text_generator(text)`
*   **Description:** "The function `stream_text_generator` takes a string of text as input and yields each word in the text followed by a space, with a small delay between each word. This creates a streaming effect where words are produced one at a time. The function uses `time.sleep(0.01)` to introduce a brief pause between yielding each word."
*   **Parameters:**
    *   **text** (str): A string containing the text to be streamed word by word.
*   **Returns:**
*   **Usage:** This function is called by the function `render_text_with_mermaid` in the file `Frontend.py` at line 160.

#### Function: `frontend.Frontend.render_text_with_mermaid`
*   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream=False)`
*   **Description:** "This function processes a markdown text string to identify and render Mermaid diagrams embedded within code blocks. It splits the input text based on Mermaid code block delimiters and handles regular markdown content versus Mermaid diagram content differently. For non-Mermaid content, it either streams or displays the text as markdown depending on the streaming flag. For Mermaid content, it attempts to render the diagram using a Mermaid component, falling back to displaying the raw code if rendering fails."
*   **Parameters:**
    *   **markdown_text** (str): A string containing markdown-formatted text that may include Mermaid code blocks enclosed in triple backticks with 'mermaid' as the language identifier.
    *   **should_stream** (bool): A boolean flag indicating whether to stream the regular markdown text instead of rendering it all at once.
*   **Returns:**
*   **Usage:** This function is called by 'render_exchange' in 'Frontend.py' at line 238 and by 'frontend.Frontend' in 'Frontend.py' at line 524.

#### Function: `frontend.Frontend.render_exchange`
*   **Signature:** `def render_exchange(ex, current_chat_name)`
*   **Description:** "This function renders a chat exchange in a Streamlit interface, displaying a user's question and an assistant's response. It handles both regular responses and error cases, providing interactive feedback mechanisms such as like/dislike buttons, comment popups, download options, and deletion capabilities. The function uses Streamlit components to build a rich UI for each exchange entry."
*   **Parameters:**
    *   **ex** (dict): A dictionary containing the exchange data including the question, answer, feedback information, and other metadata.
    *   **current_chat_name** (str): The name of the current chat session, used for handling exchange deletions.
*   **Returns:**
*   **Usage:** This function is called by the frontend.Frontend class in Frontend.py at line 429.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to represent and validate the metadata of a single function parameter. It encapsulates three essential attributes: the parameter's name, its type, and a descriptive explanation. This class serves as a structured way to define and enforce the shape of parameter descriptions, ensuring consistency and type safety when working with function signatures.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* The class is initialized with three required string fields: 'name', 'type', and 'description'. These fields collectively define the essential metadata for describing a function parameter.
    *   *Parameters:*
        *   **name** (str): The name of the function parameter.
        *   **type** (str): The data type of the function parameter.
        *   **description** (str): A human-readable description of the function parameter's purpose or usage.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic model designed to represent and validate the description of a function's return value. It encapsulates three key pieces of information about a return value: its name, type, and a textual description. This class ensures data integrity and structure for return value metadata, making it suitable for use in API documentation, code analysis tools, or any system requiring standardized return value specifications.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a ReturnDescription instance with a name, type, and description. This constructor leverages Pydantic's BaseModel functionality to enforce type safety and validation for the attributes.
    *   *Parameters:*
        *   **name** (str): The name of the return value.
        *   **type** (str): The type of the return value.
        *   **description** (str): A textual description of the return value.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model designed to represent and validate the calling context of a function, specifically capturing information about what functions are called and by whom. It serves as a structured data container for documenting usage relationships within a codebase.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a UsageContext instance with two string fields: 'calls' and 'called_by'. These fields are intended to store textual descriptions of the functions being called and the entities that call them, respectively.
    *   *Parameters:*
        *   **calls** (str): A string describing the functions or methods that are called within the context.
        *   **called_by** (str): A string describing the entity or function that calls the function in question.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to encapsulate detailed information about a function's purpose, parameters, return values, and usage context. It serves as a structured representation for documenting function signatures and behaviors, making it easier to analyze and communicate function details within a system.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a FunctionDescription instance with fields for overall function description, a list of parameter descriptions, a list of return value descriptions, and usage context information.
    *   *Parameters:*
        *   **overall** (str): A string describing the overall purpose and functionality of the function.
        *   **parameters** (List[ParameterDescription]): A list of ParameterDescription objects detailing each parameter of the function.
        *   **returns** (List[ReturnDescription]): A list of ReturnDescription objects detailing each return value of the function.
        *   **usage_context** (UsageContext): An object providing context on how the function is used within the system.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic model designed to represent the complete JSON schema for a function. It serves as a structured data container that holds essential information about a function, including its identifier, a detailed description, and an optional error field. This class is intended to provide a standardized way to encapsulate function metadata and potential errors in a type-safe manner.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysis model with required fields for the function's identifier and description, along with an optional error field that defaults to None.
    *   *Parameters:*
        *   **identifier** (str): A string identifier for the function.
        *   **description** (FunctionDescription): An instance of FunctionDescription that contains detailed information about the function.
        *   **error** (Optional[str]): An optional string field that can hold error messages related to the function.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic model designed to represent and validate the description of a class's __init__ method. It encapsulates two key pieces of information: a textual description of the constructor and a list of parameter descriptions that define its inputs. This class serves as a structured way to document and enforce the schema of constructor metadata, making it suitable for use in tools that analyze or generate API documentation, code introspection systems, or automated code generation processes.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a ConstructorDescription instance with a description string and a list of ParameterDescription objects.
    *   *Parameters:*
        *   **description** (str): A textual description of the __init__ method.
        *   **parameters** (List[ParameterDescription]): A list of ParameterDescription objects detailing each parameter of the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic model designed to encapsulate information about a class's external dependencies and the entities that instantiate it. It serves as a structured representation of metadata related to class usage and integration within a system.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a ClassContext instance with two string attributes: 'dependencies' and 'instantiated_by'. These fields are intended to store information about the class's external dependencies and the entities responsible for its instantiation.
    *   *Parameters:*
        *   **dependencies** (str): A string describing the external dependencies of the class.
        *   **instantiated_by** (str): A string describing the entities or components that instantiate the class.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It holds information about the class's overall purpose, its constructor details, a list of its methods along with their descriptions, and contextual usage information. This structure serves as a standardized way to represent detailed metadata and analysis of classes within a codebase.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ClassDescription model with specified attributes for overall purpose, constructor description, methods analysis, and usage context.
    *   *Parameters:*
        *   **overall** (str): A string describing the overall purpose and role of the class being analyzed.
        *   **init_method** (ConstructorDescription): An instance of ConstructorDescription that contains detailed information about the class's constructor.
        *   **methods** (List[FunctionAnalysis]): A list of FunctionAnalysis objects, each representing a method within the class and its associated metadata.
        *   **usage_context** (ClassContext): An object providing context on how the class is used or depends on other components.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the primary data model for representing the complete JSON schema of a class. It encapsulates essential metadata about the class, including its identifier, a detailed description, and an optional error field for capturing any issues during processing. This class is designed to be a structured representation of class information, facilitating consistent serialization and deserialization using Pydantic's validation mechanisms.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysis instance with an identifier string, a ClassDescription object, and an optional error message. The constructor sets up the core attributes required to represent a class's metadata in a standardized format.
    *   *Parameters:*
        *   **identifier** (str): A unique string identifier for the class being analyzed.
        *   **description** (ClassDescription): An object containing detailed descriptive information about the class.
        *   **error** (Optional[str]): An optional string field to store error messages related to class analysis.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure for capturing metadata related to code interactions.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a CallInfo instance with file, function, mode, and line attributes to represent a call event.
    *   *Parameters:*
        *   **file** (str): The file path where the call event occurred.
        *   **function** (str): The name of the function that made the call.
        *   **mode** (str): The mode of the call, such as 'method', 'function', or 'module'.
        *   **line** (int): The line number in the file where the call occurred.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model designed to structure contextual information for analyzing a function. It encapsulates two key pieces of information: a list of function names that the analyzed function calls, and a list of CallInfo objects representing the functions that call the analyzed function. This class serves as a data container to facilitate function analysis and dependency tracking within a codebase.
*   **Instantiation:** `HelperLLM_evaluation.py` (line 162), `MainLLM_evaluation.py` (line 156), `main.py` (line 223)
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the FunctionContextInput instance with two attributes: 'calls', which is a list of strings representing function names called by the analyzed function, and 'called_by', which is a list of CallInfo objects representing functions that call the analyzed function.
    *   *Parameters:*
        *   **calls** (List[str]): A list of strings representing the names of functions called by the analyzed function.
        *   **called_by** (List[CallInfo]): A list of CallInfo objects representing the functions that call the analyzed function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates essential metadata and contextual information required for function analysis, including the mode of operation, identifier, source code, imports, and associated context.
*   **Instantiation:** `HelperLLM_evaluation.py` (line 167), `MainLLM_evaluation.py` (line 161), `main.py` (line 228)
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysisInput instance with fields defining the analysis mode, identifier, source code, imports list, and context. It sets up the foundational structure needed for function analysis workflows.
    *   *Parameters:*
        *   **mode** ("function_analysis"): A literal string indicating the mode of operation for the analysis, constrained to the value 'function_analysis'.
        *   **identifier** (str): A string identifier for the function being analyzed.
        *   **source_code** (str): The raw source code of the function to be analyzed.
        *   **imports** (List[str]): A list of import statements used within the function's source code.
        *   **context** (FunctionContextInput): An object containing contextual information related to the function analysis.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to structure contextual information about a method within a class. It encapsulates details such as the method's identifier, the methods it calls, the methods that call it, its arguments, and its docstring. This class serves as a standardized way to represent and exchange metadata about method usage and dependencies in a structured format.
*   **Instantiation:** `HelperLLM_evaluation.py` (line 187), `MainLLM_evaluation.py` (line 181), `main.py` (line 248)
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* The class is initialized with a set of predefined attributes including identifier, calls, called_by, args, and docstring. These attributes are typed using Pydantic's type hints and optional types to enforce data integrity.
    *   *Parameters:*
        *   **identifier** (str): A string identifier for the method.
        *   **calls** (List[str]): A list of strings representing the identifiers of methods called by this method.
        *   **called_by** (List[CallInfo]): A list of CallInfo objects representing the methods that call this method.
        *   **args** (List[str]): A list of strings representing the argument names of the method.
        *   **docstring** (Optional[str]): An optional string containing the docstring of the method.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic model designed to structure contextual information about a class being analyzed. It encapsulates three key pieces of information: a list of dependencies, a list of CallInfo objects indicating where the class is instantiated, and a list of MethodContextInput objects detailing the context of each method within the class.
*   **Instantiation:** `HelperLLM.py` (line 369), `HelperLLM_evaluation.py` (line 199), `MainLLM_evaluation.py` (line 193), `main.py` (line 260)
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the ClassContextInput instance with three attributes: dependencies, instantiated_by, and method_context. These attributes are expected to hold lists of strings, CallInfo objects, and MethodContextInput objects respectively.
    *   *Parameters:*
        *   **dependencies** (List[str]): A list of string identifiers representing the dependencies of the class.
        *   **instantiated_by** (List[CallInfo]): A list of CallInfo objects describing where and how the class is instantiated.
        *   **method_context** (List[MethodContextInput]): A list of MethodContextInput objects providing context for each method within the class.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class serves as a structured input model for generating a ClassAnalysis object. It encapsulates all necessary information required for analyzing a Python class, including its source code, import statements, and contextual metadata such as instantiation details and dependencies.
*   **Instantiation:** `HelperLLM.py` (line 338), `HelperLLM_evaluation.py` (line 205), `MainLLM_evaluation.py` (line 199), `main.py` (line 266)
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysisInput instance with fields representing the mode of analysis, the identifier of the class being analyzed, the source code of the class, a list of import statements, and contextual information about how the class is used.
    *   *Parameters:*
        *   **mode** ("class_analysis"): A literal string indicating the mode of analysis, specifically set to "class_analysis".
        *   **identifier** (str): A string identifier for the class being analyzed.
        *   **source_code** (str): The raw source code of the class to be analyzed.
        *   **imports** (List[str]): A list of import statements associated with the class.
        *   **context** (ClassContextInput): An object containing contextual information about the class, such as dependencies and instantiation points.
*   **Methods:**

### File: `backend/File_Dependency.py`

#### Function: `backend.File_Dependency.build_file_dependency_graph`
*   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
*   **Description:** This function constructs a directed graph representing file dependencies within a repository. It takes a filename, an abstract syntax tree (AST), and a repository root path as inputs. It uses a custom visitor class to traverse the AST and extract import dependencies. These dependencies are then added to a NetworkX DiGraph, where nodes represent files and edges represent dependency relationships.
*   **Parameters:**
    *   **filename** (str): The name of the file being analyzed for dependencies.
    *   **tree** (AST): The abstract syntax tree of the file being analyzed.
    *   **repo_root** (str): The root directory path of the repository being analyzed.
*   **Returns:**
    *   **graph** (nx.DiGraph): A NetworkX directed graph representing file dependencies, where nodes are files and edges indicate import relationships.
*   **Usage:** This function is called by the 'build_repository_graph' function in the 'File_Dependency.py' file at line 177.

#### Function: `backend.File_Dependency.build_repository_graph`
*   **Signature:** `def build_repository_graph(repository)`
*   **Description:** This function constructs a dependency graph for all Python files within a given Git repository. It iterates through each Python file, parses its content into an abstract syntax tree (AST), and builds a file-level dependency graph. These individual graphs are then merged into a single global directed graph representing dependencies across the entire repository. The function ensures that only Python files are processed and properly handles nodes and edges in the resulting graph.
*   **Parameters:**
    *   **repository** (GitRepository): The Git repository object containing the files to analyze for dependencies.
*   **Returns:**
    *   **global_graph** (nx.DiGraph): A NetworkX directed graph representing the dependency relationships between Python files in the repository.
*   **Usage:** This function is called by the backend.File_Dependency module at line 200 in File_Dependency.py.

#### Function: `backend.File_Dependency.get_all_temp_files`
*   **Signature:** `def get_all_temp_files(directory)`
*   **Description:** This function retrieves all Python files (.py) from a specified directory and its subdirectories, returning them as relative paths from the given directory. It uses pathlib to resolve the directory path and recursively searches for files with the .py extension.
*   **Parameters:**
    *   **directory** (str): The path to the directory from which to search for Python files.
*   **Returns:**
    *   all_files ("list[pathlib.Path]"): A list of Path objects representing all Python files found in the directory and its subdirectories, relative to the specified directory.
*   **Usage:** This function is called by _resolve_module_name in File_Dependency.py at line 43.

#### Class: `FileDependencyGraph`
*   **Summary:** The FileDependencyGraph class is designed to analyze Python file dependencies by parsing import statements and resolving both absolute and relative imports. It extends NodeVisitor to traverse AST nodes representing import structures, building a dependency graph that maps files to their imported modules. The class handles complex relative imports by resolving module names against the repository structure and checks for symbol existence in package __init__.py files. It maintains a dictionary of import dependencies for each file, which can be used to construct a call graph or visualize module relationships.
*   **Instantiation:** `build_file_dependency_graph` in `File_Dependency.py`
*   **Dependencies:** `networkx`, `os`, `ast.Assign`, `ast.AST`, `ast.ClassDef`, `ast.FunctionDef`, `ast.Import`, `ast.ImportFrom`, `ast.Name`, `ast.NodeVisitor`, `ast.literal_eval`, `ast.parse`, `ast.walk`, `keyword.iskeyword`, `pathlib.Path`, `getRepo.GitRepository`, `callgraph.make_safe_dot`
*   **Constructor:**
    *   *Description:* Initializes the FileDependencyGraph with a filename and repository root path. Sets up the instance variables to track the current file being analyzed and the root directory of the repository for resolving relative paths.
    *   *Parameters:*
        *   **filename** (str): The name of the file being analyzed for dependencies.
        *   **repo_root** (Any): The root directory path of the repository containing the file.
*   **Methods:**
    *   **`_resolve_module_name`**
        *   *Signature:* `def _resolve_module_name(self, node)`
        *   *Description:* Resolves relative import statements by analyzing the import node and mapping it to actual module or symbol names. It determines the correct base directory based on the import level and checks whether the resolved modules or symbols exist in the repository structure. The method supports both direct module file existence checks and symbol resolution through __init__.py files. It raises ImportError if no valid module or symbol can be resolved.
        *   *Parameters:*
            *   **node** (ImportFrom): An AST node representing a relative import statement.
        *   *Returns:*
            *   A list of resolved module or symbol names.
        *   **Usage:** This method calls helper functions 'module_file_exists' and 'init_exports_symbol' to check for module existence and symbol availability in __init__.py files respectively.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node, base_name=None)`
        *   *Description:* Handles import statements by adding the imported module names to the dependency tracking dictionary. It ensures that the current file's dependencies are recorded under its filename key in the import_dependencies dictionary. The method supports both regular imports and those with base names derived from more complex import structures.
        *   *Parameters:*
            *   **node** (Import | ImportFrom): An AST node representing an import statement.
            *   **base_name** (str | None): Optional base name for the imported module, used in complex import cases.
        *   *Returns:*
        *   **Usage:** This method calls generic_visit to continue traversal of the AST.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Processes 'from ... import ...' style import statements by extracting the module name and delegating to visit_Import for handling. For relative imports without explicit module names, it attempts to resolve the module names using _resolve_module_name. If resolution fails, it prints an error message but continues processing.
        *   *Parameters:*
            *   **node** (ImportFrom): An AST node representing a 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method calls '_resolve_module_name' to resolve relative imports and 'visit_Import' to record dependencies.

### File: `backend/main.py`

#### Function: `backend.main.create_savings_chart`
*   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
*   **Description:** Die Funktion erstellt ein Balkendiagramm zur Darstellung des Token-Vergleichs zwischen JSON und TOON Format. Sie verwendet matplotlib zur Erstellung des Diagramms und speichert das Ergebnis in einer Datei. Das Diagramm zeigt die Anzahl der Token für beide Formate sowie den prozentualen Einsparungswert. Die Funktion setzt einen Titel mit dem Einsparungsprozentsatz, fügt eine y-Achsenbeschriftung hinzu und zeigt die Werte über den Balken an.
*   **Parameters:**
    *   **json_tokens** (int): Die Anzahl der Token im JSON-Format.
    *   **toon_tokens** (int): Die Anzahl der Token im TOON-Format.
    *   **savings_percent** (float): Der prozentuale Einsparungswert zwischen den beiden Formaten.
    *   **output_path** (str): Der Dateipfad, unter dem das generierte Diagramm gespeichert wird.
*   **Returns:**
*   **Usage:** Die Funktion wird von der Funktion 'main_workflow' in der Datei 'main.py' aufgerufen.

#### Function: `backend.main.calculate_net_time`
*   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
*   **Description:** The function calculates the net time duration between a start and end time, excluding sleep times caused by rate limits. It specifically adjusts the calculation when the model name starts with 'gemini-', applying a correction based on the number of batches and a fixed sleep interval per batch. If the total items count is zero, it returns zero directly. The result is never negative, ensuring a non-negative net time.
*   **Parameters:**
    *   **start_time** (float or datetime): The starting timestamp or time value.
    *   **end_time** (float or datetime): The ending timestamp or time value.
    *   **total_items** (int): The total number of items processed.
    *   **batch_size** (int): The size of each processing batch.
    *   **model_name** (str): The name of the model being used, which determines whether rate limit adjustments are applied.
*   **Returns:**
    *   **net_time** (float or int): The calculated net time after subtracting sleep durations, ensuring a minimum value of zero.
*   **Usage:** This function is called by the evaluation function in HelperLLM_evaluation.py at lines 249 and 275, and by the main_workflow function in main.py at lines 311 and 342.

#### Function: `backend.main.main_workflow`
*   **Signature:** `def main_workflow(input, api_keys: dict, model_names: dict, status_callback=None)`
*   **Description:** The `main_workflow` function orchestrates a comprehensive code analysis pipeline that processes a GitHub repository input. It begins by extracting API keys and model names, then clones the repository and analyzes its structure. The function performs static analysis on the codebase using various components like AST analyzers, relationship analyzers, and information extractors. It prepares inputs for a helper LLM to analyze functions and classes, and subsequently calls a main LLM to generate a final documentation report. The workflow includes error handling, logging, and performance metrics collection.
*   **Parameters:**
    *   **input**: The input containing the repository URL to be analyzed.
    *   **api_keys** (dict): A dictionary containing API keys for different services such as Gemini, OpenAI, and SCADsLLM.
    *   **model_names** (dict): A dictionary specifying the names of models to be used for helper and main LLMs.
    *   **status_callback** (Callable[[str], None]): An optional callback function to report progress updates.
*   **Returns:**
    *   **report** (str): The final documentation report generated by the main LLM.
    *   **metrics** (dict): Performance metrics including execution times and model names used.
*   **Usage:** This function is called by both 'frontend.Frontend' in 'Frontend.py' at line 489 and 'backend.main' in 'main.py' at line 533.

#### Function: `backend.main.update_status`
*   **Signature:** `def update_status(msg)`
*   **Description:** The function 'update_status' is designed to handle status updates by invoking an optional callback function if one is defined, followed by logging the message using the standard logging module. It serves as a centralized mechanism for reporting status messages throughout the application.
*   **Parameters:**
    *   **msg**: The status message to be processed and logged.
*   **Returns:**
*   **Usage:** This function is called multiple times by the 'main_workflow' function in 'main.py', specifically at lines 81, 134, 158, 167, 175, 185, 195, 205, 301, 333, 336, 409, 412, and 430.

### File: `backend/relationship_analyzer.py`

#### Function: `backend.relationship_analyzer.path_to_module`
*   **Signature:** `def path_to_module(filepath, project_root)`
*   **Description:** The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles cases where the filepath is not under the project root by falling back to the basename of the file. If the resulting path ends with '__init__', it removes the trailing part to correctly represent the package structure.
*   **Parameters:**
    *   **filepath** (str): The absolute or relative path to a Python file.
    *   **project_root** (str): The root directory of the project used to compute the relative path.
*   **Returns:**
    *   **module_path** (str): A dot-separated module path derived from the given file path.
*   **Usage:** This function is called by _collect_definitions and __init__ methods in relationship_analyzer.py.

#### Class: `ProjectAnalyzer`
*   **Summary:** The ProjectAnalyzer class is responsible for analyzing Python project structures by identifying definitions (functions, classes, methods) and tracking their interdependencies through call relationships. It recursively scans a given project root directory to find Python files, parses their Abstract Syntax Trees (ASTs) to extract definitions, and resolves function calls between these definitions. The analyzer maintains internal data structures such as a dictionary of definitions and a call graph to store relationships. After processing, it formats and returns the collected information in a structured output.
*   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
*   **Dependencies:** `ast`, `os`, `logging`, `collections.defaultdict`
*   **Constructor:**
    *   *Description:* Initializes the ProjectAnalyzer with a project root directory. Sets up internal data structures including a dictionary for storing definitions, a defaultdict for maintaining a call graph, and a dictionary for caching ASTs of processed files. Also defines a set of directories to ignore during scanning.
    *   *Parameters:*
        *   **project_root** (str): The absolute path to the root directory of the Python project to be analyzed.
*   **Methods:**
    *   **`analyze`**
        *   *Signature:* `def analyze(self)`
        *   *Description:* The main analysis method that orchestrates the process of finding Python files, collecting definitions from those files, resolving call relationships, and formatting the results. It iterates over all Python files in the project, collects definitions and resolves calls for each file, clears cached ASTs after processing, and finally returns formatted results.
        *   *Parameters:*
        *   *Returns:*
            *   output_list (list): A list of dictionaries containing information about each definition and the callers that reference it.
        *   **Usage:** This method is called by functions in HelperLLM_evaluation.py, MainLLM_evaluation.py, and main.py.
    *   **`_find_py_files`**
        *   *Signature:* `def _find_py_files(self)`
        *   *Description:* Recursively walks through the project root directory and identifies all Python (.py) files while excluding certain directories such as .git, venv, etc. It returns a list of absolute paths to these Python files.
        *   *Parameters:*
        *   *Returns:*
            *   py_files (list): A list of absolute file paths to Python source files found in the project.
        *   **Usage:** This method is called by the `analyze` method.
    *   **`_collect_definitions`**
        *   *Signature:* `def _collect_definitions(self, filepath)`
        *   *Description:* Parses a given Python file's content into an AST and extracts definitions such as functions, classes, and methods. It associates each definition with metadata like file location and line number. It also handles errors during parsing by logging them and marking the file's AST as None.
        *   *Parameters:*
            *   **filepath** (str): The absolute path to the Python file whose definitions need to be collected.
        *   *Returns:*
        *   **Usage:** This method is called by the `analyze` method.
    *   **`_get_parent`**
        *   *Signature:* `def _get_parent(self, tree, node)`
        *   *Description:* Given an AST node and a tree, this method attempts to find the parent node of the specified node by walking the AST. It is used to determine whether a function or method definition belongs to a class.
        *   *Parameters:*
            *   **tree** (ast.AST): The AST tree to search within.
            *   **node** (ast.AST): The AST node for which the parent needs to be found.
        *   *Returns:*
            *   parent (ast.AST or None): The parent AST node of the given node, or None if not found.
        *   **Usage:** This method is called by the `_collect_definitions` method.
    *   **`_resolve_calls`**
        *   *Signature:* `def _resolve_calls(self, filepath)`
        *   *Description:* Resolves function calls within a given Python file by using a CallResolverVisitor to traverse the AST and identify calls. It updates the global call graph with the resolved call relationships. Errors during resolution are logged.
        *   *Parameters:*
            *   **filepath** (str): The absolute path to the Python file whose calls need to be resolved.
        *   *Returns:*
        *   **Usage:** This method is called by the `analyze` method.
    *   **`get_formatted_results`**
        *   *Signature:* `def get_formatted_results(self)`
        *   *Description:* Formats the collected definitions and call relationships into a structured list of dictionaries. Each dictionary contains details about a definition and a list of callers that reference it. Duplicate calls are removed, and the result is sorted by file and line number.
        *   *Parameters:*
        *   *Returns:*
            *   output_list (list): A list of dictionaries representing definitions and their callers, formatted for output.
        *   **Usage:** This method is called by the `analyze` method.

#### Class: `CallResolverVisitor`
*   **Summary:** The CallResolverVisitor class is an AST (Abstract Syntax Tree) visitor designed to analyze Python code and resolve call relationships between functions and methods. It tracks the current execution context (such as class and function names) and records calls made within the code. Additionally, it maintains scope information for imports and resolves qualified names for function calls. It also tracks instance types to determine the class of objects being instantiated.
*   **Instantiation:** This class is instantiated by the `_resolve_calls` function in the `relationship_analyzer.py` file at line 92.
*   **Dependencies:** None explicitly listed in the context.
*   **Constructor:**
    *   *Description:* Initializes the CallResolverVisitor with the file path, project root, and a set of definitions. It sets up internal tracking structures such as scope, instance types, and call records, and determines the module path based on the file path and project root.
    *   *Parameters:*
        *   **filepath** (str): The path to the Python file being analyzed.
        *   **project_root** (str): The root directory of the project, used to compute relative module paths.
        *   **definitions** (dict): A dictionary containing known definitions (functions, classes, etc.) to resolve call targets.
*   **Methods:**
    *   **`visit_ClassDef`**
        *   *Signature:* `def visit_ClassDef(self, node)`
        *   *Description:* Handles the visiting of class definitions in the AST. It updates the current class name context before traversing the class body and restores the previous class name after traversal.
        *   *Parameters:*
            *   **node** (ast.ClassDef): The AST node representing the class definition.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_FunctionDef`**
        *   *Signature:* `def visit_FunctionDef(self, node)`
        *   *Description:* Handles the visiting of function definitions in the AST. It updates the current caller name context to the function name before traversing the function body and restores the previous caller name after traversal.
        *   *Parameters:*
            *   **node** (ast.FunctionDef): The AST node representing the function definition.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_Call`**
        *   *Signature:* `def visit_Call(self, node)`
        *   *Description:* Processes function calls in the AST. It resolves the qualified name of the called function and records the call if the resolved name exists in the definitions. It also tracks the caller's context (module, method, or function) and stores call metadata including file, line number, and caller information.
        *   *Parameters:*
            *   **node** (ast.Call): The AST node representing the function call.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_Import`**
        *   *Signature:* `def visit_Import(self, node)`
        *   *Description:* Handles import statements in the AST. It adds imported names to the current scope, mapping aliases to their actual names for later resolution.
        *   *Parameters:*
            *   **node** (ast.Import): The AST node representing the import statement.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_ImportFrom`**
        *   *Signature:* `def visit_ImportFrom(self, node)`
        *   *Description:* Handles 'from ... import ...' statements in the AST. It computes the full module path for relative imports and maps imported names to their fully qualified names in the scope.
        *   *Parameters:*
            *   **node** (ast.ImportFrom): The AST node representing the 'from ... import ...' statement.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`visit_Assign`**
        *   *Signature:* `def visit_Assign(self, node)`
        *   *Description:* Handles assignment statements in the AST. Specifically, it identifies assignments to instances of classes defined in the project and records the class type associated with the assigned variable.
        *   *Parameters:*
            *   **node** (ast.Assign): The AST node representing the assignment statement.
        *   *Returns:*
        *   **Usage:** This method is called by the generic AST visitor during traversal of the AST.
    *   **`_resolve_call_qname`**
        *   *Signature:* `def _resolve_call_qname(self, func_node)`
        *   *Description:* A helper method that resolves the qualified name of a function call. It handles both simple names and attribute access (e.g., obj.method). For simple names, it checks the scope and constructs a local qualified name. For attribute access, it uses stored instance types or scope mappings to resolve the full path.
        *   *Parameters:*
            *   **func_node** (ast.AST): The AST node representing the function being called.
        *   *Returns:*
            *   qualified_name (str or None): The fully qualified name of the function, or None if it cannot be resolved.
        *   **Usage:** This method is called by the `visit_Call` method.

### File: `schemas/types.py`

#### Class: `ParameterDescription`
*   **Summary:** The ParameterDescription class is a Pydantic BaseModel designed to represent and validate the metadata of a single function parameter. It encapsulates three essential attributes: the parameter's name, its type, and a descriptive explanation. This class serves as a structured way to define and enforce the shape of parameter descriptions, ensuring consistency and type safety when working with function signatures.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* The class is initialized with three required string fields: 'name', 'type', and 'description'. These fields collectively define the essential metadata for describing a function parameter.
    *   *Parameters:*
        *   **name** (str): The name of the function parameter.
        *   **type** (str): The data type of the function parameter.
        *   **description** (str): A human-readable description of the function parameter's purpose or usage.
*   **Methods:**

#### Class: `ReturnDescription`
*   **Summary:** The ReturnDescription class is a Pydantic model designed to represent and validate the description of a function's return value. It encapsulates three key pieces of information about a return value: its name, type, and a textual description. This class ensures data integrity and structure for return value metadata, making it suitable for use in API documentation, code analysis tools, or any system requiring standardized return value specifications.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a ReturnDescription instance with a name, type, and description. This constructor leverages Pydantic's BaseModel functionality to enforce type safety and validation for the attributes.
    *   *Parameters:*
        *   **name** (str): The name of the return value.
        *   **type** (str): The type of the return value.
        *   **description** (str): A textual description of the return value.
*   **Methods:**

#### Class: `UsageContext`
*   **Summary:** The UsageContext class is a Pydantic model designed to represent and validate the calling context of a function, specifically capturing information about what functions are called and by whom. It serves as a structured data container for documenting usage relationships within a codebase.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a UsageContext instance with two string fields: 'calls' and 'called_by'. These fields are intended to store textual descriptions of the functions being called and the entities that call them, respectively.
    *   *Parameters:*
        *   **calls** (str): A string describing the functions or methods that are called within the context.
        *   **called_by** (str): A string describing the entity or function that calls the function in question.
*   **Methods:**

#### Class: `FunctionDescription`
*   **Summary:** The FunctionDescription class is a Pydantic model designed to encapsulate detailed information about a function's purpose, parameters, return values, and usage context. It serves as a structured representation for documenting function signatures and behaviors, making it easier to analyze and communicate function details within a system.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a FunctionDescription instance with fields for overall function description, a list of parameter descriptions, a list of return value descriptions, and usage context information.
    *   *Parameters:*
        *   **overall** (str): A string describing the overall purpose and functionality of the function.
        *   **parameters** (List[ParameterDescription]): A list of ParameterDescription objects detailing each parameter of the function.
        *   **returns** (List[ReturnDescription]): A list of ReturnDescription objects detailing each return value of the function.
        *   **usage_context** (UsageContext): An object providing context on how the function is used within the system.
*   **Methods:**

#### Class: `FunctionAnalysis`
*   **Summary:** The FunctionAnalysis class is a Pydantic model designed to represent the complete JSON schema for a function. It serves as a structured data container that holds essential information about a function, including its identifier, a detailed description, and an optional error field. This class is intended to provide a standardized way to encapsulate function metadata and potential errors in a type-safe manner.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysis model with required fields for the function's identifier and description, along with an optional error field that defaults to None.
    *   *Parameters:*
        *   **identifier** (str): A string identifier for the function.
        *   **description** (FunctionDescription): An instance of FunctionDescription that contains detailed information about the function.
        *   **error** (Optional[str]): An optional string field that can hold error messages related to the function.
*   **Methods:**

#### Class: `ConstructorDescription`
*   **Summary:** The ConstructorDescription class is a Pydantic model designed to represent and validate the description of a class's __init__ method. It encapsulates two key pieces of information: a textual description of the constructor and a list of parameter descriptions that define its inputs. This class serves as a structured way to document and enforce the schema of constructor metadata, making it suitable for use in tools that analyze or generate API documentation, code introspection systems, or automated code generation processes.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a ConstructorDescription instance with a description string and a list of ParameterDescription objects.
    *   *Parameters:*
        *   **description** (str): A textual description of the __init__ method.
        *   **parameters** (List[ParameterDescription]): A list of ParameterDescription objects detailing each parameter of the constructor.
*   **Methods:**

#### Class: `ClassContext`
*   **Summary:** The ClassContext class is a Pydantic model designed to encapsulate information about a class's external dependencies and the entities that instantiate it. It serves as a structured representation of metadata related to class usage and integration within a system.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a ClassContext instance with two string attributes: 'dependencies' and 'instantiated_by'. These fields are intended to store information about the class's external dependencies and the entities responsible for its instantiation.
    *   *Parameters:*
        *   **dependencies** (str): A string describing the external dependencies of the class.
        *   **instantiated_by** (str): A string describing the entities or components that instantiate the class.
*   **Methods:**

#### Class: `ClassDescription`
*   **Summary:** The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It holds information about the class's overall purpose, its constructor details, a list of its methods along with their descriptions, and contextual usage information. This structure serves as a standardized way to represent detailed metadata and analysis of classes within a codebase.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes an instance of the ClassDescription model with specified attributes for overall purpose, constructor description, methods analysis, and usage context.
    *   *Parameters:*
        *   **overall** (str): A string describing the overall purpose and role of the class being analyzed.
        *   **init_method** (ConstructorDescription): An instance of ConstructorDescription that contains detailed information about the class's constructor.
        *   **methods** (List[FunctionAnalysis]): A list of FunctionAnalysis objects, each representing a method within the class and its associated metadata.
        *   **usage_context** (ClassContext): An object providing context on how the class is used or depends on other components.
*   **Methods:**

#### Class: `ClassAnalysis`
*   **Summary:** The ClassAnalysis class serves as the primary data model for representing the complete JSON schema of a class. It encapsulates essential metadata about the class, including its identifier, a detailed description, and an optional error field for capturing any issues during processing. This class is designed to be a structured representation of class information, facilitating consistent serialization and deserialization using Pydantic's validation mechanisms.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysis instance with an identifier string, a ClassDescription object, and an optional error message. The constructor sets up the core attributes required to represent a class's metadata in a standardized format.
    *   *Parameters:*
        *   **identifier** (str): A unique string identifier for the class being analyzed.
        *   **description** (ClassDescription): An object containing detailed descriptive information about the class.
        *   **error** (Optional[str]): An optional string field to store error messages related to class analysis.
*   **Methods:**

#### Class: `CallInfo`
*   **Summary:** The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure for capturing metadata related to code interactions.
*   **Instantiation:** Not instantiated by any components listed in the context.
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes a CallInfo instance with file, function, mode, and line attributes to represent a call event.
    *   *Parameters:*
        *   **file** (str): The file path where the call event occurred.
        *   **function** (str): The name of the function that made the call.
        *   **mode** (str): The mode of the call, such as 'method', 'function', or 'module'.
        *   **line** (int): The line number in the file where the call occurred.
*   **Methods:**

#### Class: `FunctionContextInput`
*   **Summary:** The FunctionContextInput class is a Pydantic model designed to structure contextual information for analyzing a function. It encapsulates two key pieces of information: a list of function names that the analyzed function calls, and a list of CallInfo objects representing the functions that call the analyzed function. This class serves as a data container to facilitate function analysis and dependency tracking within a codebase.
*   **Instantiation:** `HelperLLM_evaluation.py` (line 162), `MainLLM_evaluation.py` (line 156), `main.py` (line 223)
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the FunctionContextInput instance with two attributes: 'calls', which is a list of strings representing function names called by the analyzed function, and 'called_by', which is a list of CallInfo objects representing functions that call the analyzed function.
    *   *Parameters:*
        *   **calls** (List[str]): A list of strings representing the names of functions called by the analyzed function.
        *   **called_by** (List[CallInfo]): A list of CallInfo objects representing the functions that call the analyzed function.
*   **Methods:**

#### Class: `FunctionAnalysisInput`
*   **Summary:** The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates essential metadata and contextual information required for function analysis, including the mode of operation, identifier, source code, imports, and associated context.
*   **Instantiation:** `HelperLLM_evaluation.py` (line 167), `MainLLM_evaluation.py` (line 161), `main.py` (line 228)
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the FunctionAnalysisInput instance with fields defining the analysis mode, identifier, source code, imports list, and context. It sets up the foundational structure needed for function analysis workflows.
    *   *Parameters:*
        *   **mode** ("function_analysis"): A literal string indicating the mode of operation for the analysis, constrained to the value 'function_analysis'.
        *   **identifier** (str): A string identifier for the function being analyzed.
        *   **source_code** (str): The raw source code of the function to be analyzed.
        *   **imports** (List[str]): A list of import statements used within the function's source code.
        *   **context** (FunctionContextInput): An object containing contextual information related to the function analysis.
*   **Methods:**

#### Class: `MethodContextInput`
*   **Summary:** The MethodContextInput class is a Pydantic model designed to structure contextual information about a method within a class. It encapsulates details such as the method's identifier, the methods it calls, the methods that call it, its arguments, and its docstring. This class serves as a standardized way to represent and exchange metadata about method usage and dependencies in a structured format.
*   **Instantiation:** `HelperLLM_evaluation.py` (line 187), `MainLLM_evaluation.py` (line 181), `main.py` (line 248)
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* The class is initialized with a set of predefined attributes including identifier, calls, called_by, args, and docstring. These attributes are typed using Pydantic's type hints and optional types to enforce data integrity.
    *   *Parameters:*
        *   **identifier** (str): A string identifier for the method.
        *   **calls** (List[str]): A list of strings representing the identifiers of methods called by this method.
        *   **called_by** (List[CallInfo]): A list of CallInfo objects representing the methods that call this method.
        *   **args** (List[str]): A list of strings representing the argument names of the method.
        *   **docstring** (Optional[str]): An optional string containing the docstring of the method.
*   **Methods:**

#### Class: `ClassContextInput`
*   **Summary:** The ClassContextInput class is a Pydantic model designed to structure contextual information about a class being analyzed. It encapsulates three key pieces of information: a list of dependencies, a list of CallInfo objects indicating where the class is instantiated, and a list of MethodContextInput objects detailing the context of each method within the class.
*   **Instantiation:** `HelperLLM.py` (line 369), `HelperLLM_evaluation.py` (line 199), `MainLLM_evaluation.py` (line 193), `main.py` (line 260)
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the ClassContextInput instance with three attributes: dependencies, instantiated_by, and method_context. These attributes are expected to hold lists of strings, CallInfo objects, and MethodContextInput objects respectively.
    *   *Parameters:*
        *   **dependencies** (List[str]): A list of string identifiers representing the dependencies of the class.
        *   **instantiated_by** (List[CallInfo]): A list of CallInfo objects describing where and how the class is instantiated.
        *   **method_context** (List[MethodContextInput]): A list of MethodContextInput objects providing context for each method within the class.
*   **Methods:**

#### Class: `ClassAnalysisInput`
*   **Summary:** The ClassAnalysisInput class serves as a structured input model for generating a ClassAnalysis object. It encapsulates all necessary information required for analyzing a Python class, including its source code, import statements, and contextual metadata such as instantiation details and dependencies.
*   **Instantiation:** `HelperLLM.py` (line 338), `HelperLLM_evaluation.py` (line 205), `MainLLM_evaluation.py` (line 199), `main.py` (line 266)
*   **Dependencies:** None outside of the file's imports.
*   **Constructor:**
    *   *Description:* Initializes the ClassAnalysisInput instance with fields representing the mode of analysis, the identifier of the class being analyzed, the source code of the class, a list of import statements, and contextual information about how the class is used.
    *   *Parameters:*
        *   **mode** ("class_analysis"): A literal string indicating the mode of analysis, specifically set to "class_analysis".
        *   **identifier** (str): A string identifier for the class being analyzed.
        *   **source_code** (str): The raw source code of the class to be analyzed.
        *   **imports** (List[str]): A list of import statements associated with the class.
        *   **context** (ClassContextInput): An object containing contextual information about the class, such as dependencies and instantiation points.
*   **Methods:**

---