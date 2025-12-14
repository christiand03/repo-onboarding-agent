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

        schemas --> schemas/types.py

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
    -  r e q u e s t s - t o o l b e t = = 1 . 0 . 0 
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
    -  
    ### Setup Guide
    Information not found
    ### Quick Startup
    Information not found

    ## 3. Use Cases & Commands
    This project appears to be a documentation generation pipeline that analyzes code repositories. Key use cases likely include:
    
    *   **Repository Analysis:** Cloning a specified GitHub repository, parsing its codebase, and analyzing its structure and dependencies.
    *   **Code Documentation Generation:** Utilizing large language models (LLMs) such as Google Gemini or OpenAI models to automatically generate documentation for functions and classes within the codebase.
    *   **Format Comparison:** Evaluating the efficiency of different data formats (JSON vs. TOON) for LLM input by comparing token usage and potential savings.
    *   **Frontend Application:** Providing a Streamlit-based user interface for interacting with the documentation generation pipeline, managing user accounts, API keys, and chat history.
    
    The primary command-line interface for this project appears to be the `main.py` script, which orchestrates the entire workflow. Specific commands or arguments are not detailed in the provided information, but the `main_workflow` function suggests a process that takes repository URLs, API keys, and model names as input.

    ## 4. Architecture
    The Mermaid Syntax to visualize Graphs is not set up yet and will be added
    but if there is mermaid syntax in your input json display it here



    ## 5. Code Analysis

    ### File: `backend/AST_Schema.py`

    #### Class: `ASTVisitor`
    *   **Summary:** The ASTVisitor class is designed to traverse an Abstract Syntax Tree (AST) generated from Python source code. It collects information about imports, classes, and functions, organizing them into a structured schema. The visitor maintains context about the current class being processed and builds detailed metadata for each element, including source code segments, line numbers, and documentation strings.
    *   **Instantiation:** `analyze_repository`
    *   **Dependencies:** `ast`
    *   **Constructor:**
        *   *Description:* Initializes the ASTVisitor with source code, file path, and project root. It sets up internal state variables such as module path, schema structure, and current class tracking.
        *   *Parameters:*
            - **source_code** (`str`): The full source code string of the file being analyzed.
            - **file_path** (`str`): The file path of the source code being analyzed.
            - **project_root** (`str`): The root directory of the project.
    *   **Methods:**
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* Handles import nodes in the AST by extracting the names of imported modules and appending them to the schema's imports list. It ensures that all import statements are recorded during traversal.
            *   *Parameters:*
                - **node** (`ast.Import`): An AST node representing an import statement.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* Processes 'from ... import ...' statements by extracting module and alias information and appending them to the schema's imports list. It correctly formats the import path for clarity.
            *   *Parameters:*
                - **node** (`ast.ImportFrom`): An AST node representing a 'from ... import ...' statement.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node)`
            *   *Description:* Handles class definition nodes by creating a structured representation of the class, including its identifier, name, docstring, source code segment, and line numbers. It appends this information to the schema's classes list and tracks the current class for subsequent method processing.
            *   *Parameters:*
                - **node** (`ast.ClassDef`): An AST node representing a class definition.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* Processes function definitions by determining whether they belong to a class or are standalone. For class methods, it creates a method context entry; for standalone functions, it creates a function entry in the schema. It captures essential details like arguments, docstrings, and source code segments.
            *   *Parameters:*
                - **node** (`ast.FunctionDef`): An AST node representing a function definition.
            *   *Returns:*
            *   **Usage:**
        *   **`visit_AsyncFunctionDef`**
            *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
            *   *Description:* Handles asynchronous function definitions by delegating to the standard function definition handler. This allows async functions to be processed similarly to regular functions.
            *   *Parameters:*
                - **node** (`ast.AsyncFunctionDef`): An AST node representing an asynchronous function definition.
            *   *Returns:*
            *   **Usage:**

    #### Class: `ASTAnalyzer`
    *   **Summary:** The ASTAnalyzer class is responsible for analyzing Python repository files by parsing their Abstract Syntax Trees (ASTs) and enriching the resulting schema with call graph information. It merges relationship data into the schema and supports repository-wide analysis by processing multiple files. The class acts as a central component for extracting structural and relational information from Python code.
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** `ast`, `networkx`, `os`, `callgraph.build_filtered_callgraph`, `getRepo.GitRepository`
    *   **Constructor:**
        *   *Description:* Initializes an instance of the ASTAnalyzer class. The constructor currently does not perform any operations.
        *   *Parameters:*
    *   **Methods:**
        *   **`_enrich_schema_with_callgraph`**
            *   *Signature:* `def _enrich_schema_with_callgraph(schema, call_graph, filename)`
            *   *Description:* This static method enriches a given schema with call graph information by updating function and method contexts with details about which functions they call and which functions call them. It iterates over functions and classes in the schema and updates their context fields based on the provided call graph.
            *   *Parameters:*
                - **schema** (`dict`): A dictionary representing the schema of the parsed Python code, containing functions and classes.
                - **call_graph** (`nx.DiGraph`): A NetworkX directed graph representing the call relationships between functions.
                - **filename** (`str`): The filename associated with the schema being enriched.
            *   *Returns:*
            *   **Usage:**
        *   **`merge_relationship_data`**
            *   *Signature:* `def merge_relationship_data(self, full_schema, relationship_data)`
            *   *Description:* "This method merges relationship data (such as called_by information) into a full schema by creating a lookup table from the relationship data and then updating the schema nodes accordingly. It processes both functions and classes, adding relationship information to their respective contexts."
            *   *Parameters:*
                - **full_schema** (`dict`): The complete schema containing file structures and AST nodes.
                - **relationship_data** (`list`): A list of dictionaries containing relationship information for various identifiers.
            *   *Returns:*
                - **full_schema** (`dict`): The updated schema with merged relationship data.
            *   **Usage:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
        *   **`analyze_repository`**
            *   *Signature:* `def analyze_repository(self, files, repo)`
            *   *Description:* "This method performs a comprehensive analysis of a repository by processing a list of files. It constructs a full schema by parsing each Python file's content into an AST, visiting the nodes with an ASTVisitor, and enriching the schema with call graph information. It handles errors during parsing and filters out non-Python files."
            *   *Parameters:*
                - **files** (`list`): A list of file objects containing path and content information.
                - **repo** (`GitRepository`): An object representing the Git repository being analyzed.
            *   *Returns:*
                - **full_schema** (`dict`): A dictionary containing the full schema of the analyzed repository files.
            *   **Usage:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`

    #### Function: `path_to_module`
    *   **Signature:** `def path_to_module(filepath, project_root)`
    *   **Description:** Wandelt einen Dateipfad in einen Python-Modulpfad um.
    *   **Parameters:**
        - **filepath** (`str`): The absolute or relative path to a Python file.
        - **project_root** (`str`): The root directory of the project used to compute the relative path.
    *   **Returns:**
        - **module_path** (`str`): A dot-separated module path derived from the given file path.
    *   **Usage:** Called by the `__init__` method in AST_Schema.py at line 31.

    ### File: `backend/File_Dependency.py`

    #### Function: `build_file_dependency_graph`
    *   **Signature:** `def build_file_dependency_graph(filename, tree, repo_root)`
    *   **Description:** "This function constructs a directed graph representing file dependencies within a repository. It takes an AST representation of a file and uses a custom visitor to extract import dependencies. These dependencies are then added as nodes and edges in a NetworkX DiGraph, where each node represents a file and each edge represents an import relationship. The resulting graph captures the dependency structure of the given file."
    *   **Parameters:**
        - **filename** (`str`): The name of the file being analyzed for dependencies.
        - **tree** (`AST`): The abstract syntax tree representation of the file's source code.
        - **repo_root** (`str`): The root directory path of the repository being analyzed.
    *   **Returns:**
        - **graph** (`nx.DiGraph`): A NetworkX directed graph representing the file dependency relationships.
    *   **Usage:** Called by the `build_repository_graph` function in the File_Dependency.py file.

    #### Function: `build_repository_graph`
    *   **Signature:** `def build_repository_graph(repository)`
    *   **Description:** "This function constructs a directed graph representing the dependencies between Python files within a given Git repository. It iterates through all files in the repository, filters for Python files, parses their content into ASTs, and builds individual file dependency graphs. These are then merged into a global dependency graph. The function uses NetworkX to manage the graph structure and relies on helper functions to process individual files."
    *   **Parameters:**
        - **repository** (`GitRepository`): The Git repository object containing the files to analyze for dependencies.
    *   **Returns:**
        - **global_graph** (`nx.DiGraph`): A NetworkX directed graph representing the overall dependency structure of all Python files in the repository.
    *   **Usage:** Called by the `backend.File_Dependency` module at line 200.

    #### Function: `get_all_temp_files`
    *   **Signature:** `def get_all_temp_files(directory)`
    *   **Description:** "This function retrieves all Python files (.py) from a specified directory and its subdirectories, returning them as relative paths from the given directory. It uses pathlib for path manipulation and recursive globbing to find all matching files."
    *   **Parameters:**
        - **directory** (`str`): The root directory path from which to search for Python files.
    *   **Returns:**
        - **all_files** (`list[pathlib.Path]`): A list of Path objects representing all Python files found in the directory and its subdirectories, relative to the specified root directory.
    *   **Usage:** Called by `_resolve_module_name` in File_Dependency.py at line 43.

    #### Class: `FileDependencyGraph`
    *   **Summary:** "The FileDependencyGraph class is designed to analyze Python file dependencies by traversing AST nodes of import statements. It resolves both absolute and relative imports, identifies module and symbol existence, and builds a dependency graph represented as a dictionary mapping filenames to their imported modules. The class inherits from NodeVisitor to traverse the abstract syntax tree of Python files and processes import statements to construct a mapping of file dependencies."
    *   **Instantiation:** `build_file_dependency_graph`
    *   **Dependencies:** None explicitly listed beyond file imports.
    *   **Constructor:**
        *   *Description:* Initializes the FileDependencyGraph with a filename and repository root path. Sets up the instance variables to track the current file being analyzed and the root directory of the repository.
        *   *Parameters:*
            - **filename** (`str`): The name of the file being analyzed for dependencies.
            - **repo_root** (`Any`): The root directory path of the repository containing the file.
    *   **Methods:**
        *   **`_resolve_module_name`**
            *   *Signature:* `def _resolve_module_name(self, node)`
            *   *Description:* Resolves relative import statements by analyzing the import node and determining the actual module or symbol names that can be resolved. It checks for existing module files or symbols exported via __init__.py files and raises an ImportError if resolution fails.
            *   *Parameters:*
                - **node** (`ImportFrom`): The AST node representing the import statement to resolve.
            *   *Returns:*
                - **`list[str]`**: A list of resolved module or symbol names.
            *   **Usage:** Called by `visit_ImportFrom`.
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node, base_name)`
            *   *Description:* Handles import statements by adding the imported module names to the import_dependencies dictionary. It ensures that the current file's dependencies are tracked correctly based on the import node.
            *   *Parameters:*
                - **node** (`Import | ImportFrom`): The AST node representing the import statement.
                - **base_name** (`str | None`): Optional base name of the module being imported.
            *   *Returns:*
            *   **Usage:** Called by `visit_ImportFrom`.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* Processes import statements of the form 'from module import something' by extracting the module name or resolving relative imports. It delegates to 'visit_Import' to record the dependencies.
            *   *Parameters:*
                - **node** (`ImportFrom`): The AST node representing the relative import statement.
            *   *Returns:*
            *   **Usage:** Called during AST traversal initiated by NodeVisitor.

    ### File: `backend/HelperLLM.py`

    #### Function: `main_orchestrator`
    *   **Signature:** `def main_orchestrator()`
    *   **Description:** "The main_orchestrator function serves as a dummy data and processing loop for testing the LLMHelper class. It defines pre-computed analysis for three example functions ('add_item', 'check_stock', and 'generate_report') and simulates the process of generating documentation for these functions using an LLMHelper instance. The function sets up mock inputs and expected outputs, initializes an LLM helper with specific prompt files, and processes the results to build a final documentation structure."
    *   **Parameters:**
    *   **Returns:**
    *   **Usage:** Called by `backend.HelperLLM` in HelperLLM.py at line 419.

    #### Class: `LLMHelper`
    *   **Summary:** "The LLMHelper class serves as a centralized interface for interacting with various language models, particularly for generating validated documentation for functions and classes. It supports multiple LLM backends including Google Gemini, OpenAI, custom APIs, and Ollama, dynamically configuring settings based on the selected model. The class handles API interactions, batch processing, and structured output validation using Pydantic models."
    *   **Instantiation:** `HelperLLM.py`, `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** None explicitly listed beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes the LLMHelper with configuration parameters including API keys, prompt file paths, and model specifications. It reads system prompts from specified files, configures batch sizes according to the model, and sets up appropriate LLM clients for function and class documentation generation."
        *   *Parameters:*
            - **api_key** (`str`): API key for authenticating with the language model provider.
            - **function_prompt_path** (`str`): Path to the file containing the system prompt for function documentation generation.
            - **class_prompt_path** (`str`): Path to the file containing the system prompt for class documentation generation.
            - **model_name** (`str`): Name of the language model to use, defaults to 'gemini-2.0-flash-lite'.
            - **base_url** (`str`): Base URL for custom API endpoints, optional.
    *   **Methods:**
        *   **`_configure_batch_settings`**
            *   *Signature:* `def _configure_batch_settings(self, model_name)`
            *   *Description:* Configures the batch size for processing requests based on the specified model name. Different models have different recommended batch sizes for optimal performance and rate limiting compliance.
            *   *Parameters:*
                - **model_name** (`str`): Name of the language model for which to configure batch settings.
            *   *Returns:*
            *   **Usage:** Called by the `__init__` method.
        *   **`generate_for_functions`**
            *   *Signature:* `def generate_for_functions(self, function_inputs)`
            *   *Description:* "Processes a batch of function inputs to generate and validate documentation using the configured LLM. It splits inputs into batches, sends them to the LLM, and handles errors gracefully by returning None for failed items while maintaining order."
            *   *Parameters:*
                - **function_inputs** (`List[FunctionAnalysisInput]`): A list of function input models to process for documentation generation.
            *   *Returns:*
                - **result** (`List[Optional[FunctionAnalysis]]`): A list of validated function analysis results or None for failed items.
            *   **Usage:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
        *   **`generate_for_classes`**
            *   *Signature:* `def generate_for_classes(self, class_inputs)`
            *   *Description:* "Processes a batch of class inputs to generate and validate documentation using the configured LLM. Similar to generate_for_functions, it manages batching, sends requests to the LLM, and ensures ordered results even when errors occur."
            *   *Parameters:*
                - **class_inputs** (`List[ClassAnalysisInput]`): A list of class input models to process for documentation generation.
            *   *Returns:*
                - **result** (`List[Optional[ClassAnalysis]]`): A list of validated class analysis results or None for failed items.
            *   **Usage:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`

    ### File: `backend/MainLLM.py`

    #### Class: `MainLLM`
    *   **Summary:** "The MainLLM class serves as the central interface for interacting with various language learning models (LLMs), supporting multiple backends including Google Generative AI, OpenAI-compatible APIs, and Ollama. It initializes with an API key, a prompt file path, and model specifications, dynamically selecting the appropriate LLM client based on the model name. The class provides two core functionalities: synchronous LLM invocation via `call_llm` and streaming responses via `stream_llm`, both utilizing a system prompt loaded from a file."
    *   **Instantiation:** `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** `os`, `logging`, `sys`, `dotenv.load_dotenv`, `langchain_google_genai.ChatGoogleGenerativeAI`, `langchain_ollama.ChatOllama`, `langchain_openai.ChatOpenAI`, `langchain.messages.HumanMessage`, `langchain.messages.SystemMessage`
    *   **Constructor:**
        *   *Description:* "Initializes the MainLLM instance by validating the API key, loading a system prompt from a specified file, and setting up the appropriate LLM client based on the model name. It supports different LLM providers such as Google Generative AI, custom OpenAI-compatible APIs, and Ollama, depending on the model identifier."
        *   *Parameters:*
            - **api_key** (`str`): The API key used for authenticating with the LLM provider.
            - **prompt_file_path** (`str`): The file path to the system prompt used for initializing the LLM.
            - **model_name** (`str`): The name of the model to use, which determines the backend LLM client to instantiate.
            - **base_url** (`str`): Optional base URL for connecting to a local or custom LLM endpoint.
    *   **Methods:**
        *   **`call_llm`**
            *   *Signature:* `def call_llm(self, user_input)`
            *   *Description:* "Synchronously invokes the configured LLM with a user input message, prepending a system prompt to the conversation history. It handles potential exceptions during the call and logs success or failure accordingly, returning the content of the LLM's response or None if an error occurs."
            *   *Parameters:*
                - **user_input** (`str`): The input text provided by the user to be processed by the LLM.
            *   *Returns:*
                - **response_content** (`str`): The content of the LLM's response if the call succeeds, otherwise None.
            *   **Usage:** `MainLLM_evaluation.py`, `main.py`
        *   **`stream_llm`**
            *   *Signature:* `def stream_llm(self, user_input)`
            *   *Description:* Initiates a streaming interaction with the configured LLM using the provided user input. It sends the system prompt and user input as a conversation history to the LLM and yields content chunks as they are received. Errors during the stream process are logged and yielded as error messages.
            *   *Parameters:*
                - **user_input** (`str`): The input text provided by the user to be streamed to the LLM.
            *   *Returns:*
                - **chunk_content** (`str`): Yields content chunks from the LLM's streaming response or an error message if an exception occurs.
            *   **Usage:** Not called by any function in the provided context.

    ### File: `backend/basic_info.py`

    #### Class: `ProjektInfoExtractor`
    *   **Summary:** "The ProjektInfoExtractor class is designed to extract basic project information from common project files such as README.md, pyproject.toml, and requirements.txt. It maintains an internal data structure to store extracted information including project overview details like title, description, status, features, and tech stack, as well as installation-related information such as dependencies, setup instructions, and quick start guides. The class orchestrates the extraction process by prioritizing file types and parsing their contents accordingly."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** Standard Python libraries and typing annotations.
    *   **Constructor:**
        *   *Description:* Initializes the ProjektInfoExtractor with a predefined data structure to hold project information. It sets up placeholders for various project metadata fields and defines a constant for indicating missing information.
        *   *Parameters:*
    *   **Methods:**
        *   **`_finde_datei`**
            *   *Signature:* `def _finde_datei(self, patterns, dateien)`
            *   *Description:* "This private method searches for a file among a list of files based on a set of filename patterns. It performs a case-insensitive search to find the first matching file and returns it, or None if no match is found."
            *   *Parameters:*
                - **patterns** (`List[str]`): A list of filename suffixes or patterns to match against.
                - **dateien** (`List[Any]`): A list of file objects to search through.
            *   *Returns:*
                - **result** (`Optional[Any]`): The first matching file object or None if no match is found.
            *   **Usage:** Called by the `extrahiere_info` method to locate relevant project files.
        *   **`_extrahiere_sektion_aus_markdown`**
            *   *Signature:* `def _extrahiere_sektion_aus_markdown(self, inhalt, keywords)`
            *   *Description:* "This private method extracts a section of text from a markdown document based on a specified heading. It uses regular expressions to find the section under a given heading and returns the content of that section."
            *   *Parameters:*
                - **inhalt** (`str`): The full markdown text to parse.
                - **keywords** (`List[str]`): A list of alternative keywords to match as headings.
            *   *Returns:*
                - **result** (`Optional[str]`): The extracted text section or None if no matching section is found.
            *   **Usage:** Called by the `_parse_readme` method to extract specific sections.
        *   **`_parse_readme`**
            *   *Signature:* `def _parse_readme(self, inhalt)`
            *   *Description:* "This private method parses the content of a README file to extract various project details such as title, description, key features, tech stack, current status, setup instructions, and quick start guide. It updates the internal info dictionary with these values."
            *   *Parameters:*
                - **inhalt** (`str`): The content of the README file to parse.
            *   *Returns:*
            *   **Usage:** Called by the `extrahiere_info` method.
        *   **`_parse_toml`**
            *   *Signature:* `def _parse_toml(self, inhalt)`
            *   *Description:* "This private method parses the content of a pyproject.toml file to extract project metadata such as name, description, and dependencies. It uses the tomllib library to load the TOML content and updates the internal info dictionary accordingly."
            *   *Parameters:*
                - **inhalt** (`str`): The content of the pyproject.toml file to parse.
            *   *Returns:*
            *   **Usage:** Called by the `extrahiere_info` method.
        *   **`_parse_requirements`**
            *   *Signature:* `def _parse_requirements(self, inhalt)`
            *   *Description:* "This private method parses the content of a requirements.txt file to extract dependency information. It only populates the dependencies field if it hasn't already been set by a previous parsing step, such as from a pyproject.toml file."
            *   *Parameters:*
                - **inhalt** (`str`): The content of the requirements.txt file to parse.
            *   *Returns:*
            *   **Usage:** Called by the `extrahiere_info` method.
        *   **`extrahiere_info`**
            *   *Signature:* `def extrahiere_info(self, dateien, repo_url)`
            *   *Description:* "This public method orchestrates the entire information extraction process. It identifies relevant project files, parses them in order of priority (pyproject.toml, requirements.txt, README), and formats the extracted information into a standardized dictionary structure. It also handles final formatting of dependencies and sets the project title based on the repository URL."
            *   *Parameters:*
                - **dateien** (`List[Any]`): A list of file objects representing project files to extract information from.
                - **repo_url** (`str`): The URL of the repository, used to derive the project title.
            *   *Returns:*
                - **info** (`Dict[str, Any]`): A dictionary containing the extracted project information organized under 'projekt_uebersicht' and 'installation' keys.
            *   **Usage:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`

    ### File: `backend/callgraph.py`

    #### Function: `make_safe_dot`
    *   **Signature:** `def make_safe_dot(graph, out_path)`
    *   **Description:** "The function 'make_safe_dot' takes a NetworkX directed graph and a file path as inputs. It creates a safe version of the graph by relabeling all nodes with unique identifiers prefixed by 'n', ensuring node names are safe for visualization. The original node labels are preserved in the 'label' attribute of the new nodes. Finally, it writes the transformed graph to a DOT file at the specified output path."
    *   **Parameters:**
        - **graph** (`nx.DiGraph`): A NetworkX directed graph to be processed and saved in DOT format.
        - **out_path** (`str`): The file path where the DOT representation of the graph will be written.
    *   **Returns:**
    *   **Usage:** Called by 'backend.callgraph' in the file 'callgraph.py' at line 244.

    #### Function: `build_filtered_callgraph`
    *   **Signature:** `def build_filtered_callgraph(repo)`
    *   **Description:** "Die Funktion erstellt einen globalen Call-Graphen basierend auf allen Python-Dateien eines Git-Repositories und filtert diesen anschließend auf Funktionen, die vom Benutzer selbst geschrieben wurden. Sie durchläuft alle Dateien, parst deren Inhalt mit dem Abstract Syntax Tree (AST), extrahiert Funktionsaufrufe und baut einen gerichteten Graphen auf, wobei nur Kanten zwischen eigenen Funktionen erhalten bleiben."
    *   **Parameters:**
        - **repo** (`GitRepository`): "Ein Objekt, das Informationen über ein Git-Repository enthält, insbesondere Zugriff auf alle enthaltenen Dateien."
    *   **Returns:**
        - **global_graph** (`nx.DiGraph`): "Ein gerichteter Graph, der die Aufrufbeziehungen zwischen Funktionen darstellt, gefiltert auf solche, die vom Benutzer implementiert wurden."
    *   **Usage:** Called by `analyze_repository` in `AST_Schema.py` and by `backend.callgraph` in `callgraph.py`.

    #### Class: `CallGraph`
    *   **Summary:** "The CallGraph class is a subclass of ast.NodeVisitor designed to traverse Python AST nodes and construct a call graph representation. It tracks function and class definitions, resolves names of called functions, and builds a directed graph of function calls. The class maintains mappings for local definitions, imports, and function sets to accurately represent inter-function dependencies in Python code."
    *   **Instantiation:** `build_filtered_callgraph`
    *   **Dependencies:** `ast`, `networkx`, `os`, `pathlib.Path`, `typing.Dict`, `getRepo.GitRepository`, `basic_info.ProjektInfoExtractor`, `os`
    *   **Constructor:**
        *   *Description:* "Initializes the CallGraph with a filename and sets up internal data structures including tracking for current function and class, local definitions, a networkx DiGraph for the call graph, import mappings, a set of function names, and a dictionary of edges."
        *   *Parameters:*
            - **filename** (`str`): The name of the file being processed to build the call graph.
    *   **Methods:**
        *   **`_recursive_call`**
            *   *Signature:* `def _recursive_call(self, node)`
            *   *Description:* "Recursively extracts the dotted name components from an AST node representing a function call. It handles different types of AST nodes like ast.Call, ast.Name, and ast.Attribute to build a list of name components that can be used to resolve the full path of a function."
            *   *Parameters:*
                - **node** (`ast.AST`): The AST node to extract the dotted name components from.
            *   *Returns:*
                - **parts** (`list[str]`): A list of strings representing the dotted name components.
            *   **Usage:** Not called by any other methods.
        *   **`_resolve_all_callee_names`**
            *   *Signature:* `def _resolve_all_callee_names(self, callee_nodes)`
            *   *Description:* "Resolves a list of dotted name components into fully qualified names by checking local definitions, import mappings, and constructing names based on the current class context. It processes each component list to determine the correct fully qualified name for each callee."
            *   *Parameters:*
                - **callee_nodes** (`list[list[str]]`): A list of lists containing name components for callees.
            *   *Returns:*
                - **resolved** (`list[str]`): A list of fully qualified names for the callees.
            *   **Usage:** Not called by any other methods.
        *   **`_make_full_name`**
            *   *Signature:* `def _make_full_name(self, basename, class_name)`
            *   *Description:* "Constructs a fully qualified name for a function or method, incorporating the filename, optional class name, and the base name. This helps in uniquely identifying functions within the context of a file and potentially within a class."
            *   *Parameters:*
                - **basename** (`str`): The base name of the function or method.
                - **class_name** (`Optional[str]`): The name of the class if the function is a method.
            *   *Returns:*
                - **full_name** (`str`): The fully qualified name constructed from the filename, class name (if provided), and base name.
            *   **Usage:** Not called by any other methods.
        *   **`_current_caller`**
            *   *Signature:* `def _current_caller(self)`
            *   *Description:* "Determines the current caller's name based on whether there is an active function context. If a function is currently being visited, it returns the function's name; otherwise, it returns a placeholder indicating global scope or the filename."
            *   *Parameters:*
            *   *Returns:*
                - **caller_name** (`str`): The name of the current caller or a placeholder if no function is active.
            *   **Usage:** Not called by any other methods.
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* "Handles the AST node for import statements. It maps imported module names to their actual module names, storing these mappings in the import_mapping dictionary for later resolution of function calls."
            *   *Parameters:*
                - **node** (`ast.Import`): The AST node representing an import statement.
            *   *Returns:*
            *   **Usage:** Not called by any other methods.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* "Handles the AST node for from-import statements. It extracts the module name and maps aliases to their respective modules, updating the import_mapping dictionary accordingly."
            *   *Parameters:*
                - **node** (`ast.ImportFrom`): The AST node representing a from-import statement.
            *   *Returns:*
            *   **Usage:** Not called by any other methods.
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node)`
            *   *Description:* "Processes AST nodes representing class definitions. It temporarily stores the previous class name, updates the current class context, visits the class body, and restores the previous class context after processing."
            *   *Parameters:*
                - **node** (`ast.ClassDef`): The AST node representing a class definition.
            *   *Returns:*
            *   **Usage:** Not called by any other methods.
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* "Processes AST nodes representing function definitions. It records the function's full name in local definitions, adds the function to the call graph, and manages the current function context during traversal."
            *   *Parameters:*
                - **node** (`ast.FunctionDef`): The AST node representing a function definition.
            *   *Returns:*
            *   **Usage:** Not called by any other methods.
        *   **`visit_AsyncFunctionDef`**
            *   *Signature:* `def visit_AsyncFunctionDef(self, node)`
            *   *Description:* "Processes AST nodes representing asynchronous function definitions. It delegates the handling to the visit_FunctionDef method, treating async functions similarly to regular functions."
            *   *Parameters:*
                - **node** (`ast.AsyncFunctionDef`): The AST node representing an async function definition.
            *   *Returns:*
            *   **Usage:** Not called by any other methods.
        *   **`visit_Call`**
            *   *Signature:* `def visit_Call(self, node)`
            *   *Description:* "Handles AST nodes representing function calls. It identifies the caller, resolves the callee names, and records the edge between the caller and callee in the edges dictionary for later graph construction."
            *   *Parameters:*
                - **node** (`ast.Call`): The AST node representing a function call.
            *   *Returns:*
            *   **Usage:** Not called by any other methods.
        *   **`visit_If`**
            *   *Signature:* `def visit_If(self, node)`
            *   *Description:* "Handles AST nodes representing if statements. Specifically, it checks for conditional statements related to '__name__' and temporarily changes the current function context to '<main_block>' while visiting the body of such statements."
            *   *Parameters:*
                - **node** (`ast.If`): The AST node representing an if statement.
            *   *Returns:*
            *   **Usage:** Not called by any other methods.

    ### File: `backend/getRepo.py`

    #### Class: `RepoFile`
    *   **Summary:** "The RepoFile class represents a single file within a Git repository. It implements lazy loading for file metadata such as the blob object, content, and size to optimize performance by only loading data when explicitly accessed. The class provides properties to access these lazily-loaded attributes and includes utility methods like word count analysis and conversion to dictionary format."
    *   **Instantiation:** `get_all_files`
    *   **Dependencies:** `os`, `git.Repo`, `git.GitCommandError`, `logging`, `os`
    *   **Constructor:**
        *   *Description:* "Initializes a RepoFile object with the file path and the commit tree from which the file originates. It sets up internal attributes for lazy loading including placeholders for the blob, content, and size."
        *   *Parameters:*
            - **file_path** (`str`): The path to the file within the repository.
            - **commit_tree** (`git.Tree`): The tree object of the commit from which the file originates.
    *   **Methods:**
        *   **`blob`**
            *   *Signature:* `def blob(self)`
            *   *Description:* "A property that lazily loads and returns the Git blob object associated with the file. If the blob has not yet been loaded, it attempts to retrieve it from the commit tree using the stored file path. If the file is not found in the tree, a FileNotFoundError is raised."
            *   *Parameters:*
            *   *Returns:*
                - **blob** (`git.Blob`): The Git blob object representing the file.
            *   **Usage:** Not called by any other functions according to the provided context.
        *   **`content`**
            *   *Signature:* `def content(self)`
            *   *Description:* "A property that lazily loads and returns the decoded UTF-8 content of the file. If the content has not yet been loaded, it reads the data stream from the blob and decodes it, ignoring encoding errors. The result is cached for subsequent accesses."
            *   *Parameters:*
            *   *Returns:*
                - **content** (`str`): The decoded content of the file.
            *   **Usage:** Not called by any other functions according to the provided context.
        *   **`size`**
            *   *Signature:* `def size(self)`
            *   *Description:* "A property that lazily loads and returns the size of the file in bytes. If the size has not yet been determined, it retrieves the size directly from the blob object. The value is cached for future access."
            *   *Parameters:*
            *   *Returns:*
                - **size** (`int`): The size of the file in bytes.
            *   **Usage:** Not called by any other functions according to the provided context.
        *   **`analyze_word_count`**
            *   *Signature:* `def analyze_word_count(self)`
            *   *Description:* An example analysis method that counts the number of words in the file's content by splitting the content on whitespace and returning the length of the resulting list. This method relies on the content property to ensure the file content is loaded before processing.
            *   *Parameters:*
            *   *Returns:*
                - **word_count** (`int`): The total number of words in the file content.
            *   **Usage:** Not called by any other functions according to the provided context.
        *   **`__repr__`**
            *   *Signature:* `def __repr__(self)`
            *   *Description:* "Provides a string representation of the RepoFile object, useful for debugging and logging purposes. It displays the file path in a readable format."
            *   *Parameters:*
            *   *Returns:*
                - **repr** (`str`): A string representation of the RepoFile object showing its file path.
            *   **Usage:** Not called by any other functions according to the provided context.
        *   **`to_dict`**
            *   *Signature:* `def to_dict(self, include_content)`
            *   *Description:* "Converts the RepoFile object into a dictionary representation, including basic file information such as path, name, size, and type. Optionally, it can also include the full content of the file if requested."
            *   *Parameters:*
                - **include_content** (`bool`): If True, includes the file's content in the returned dictionary.
            *   *Returns:*
                - **data** (`dict`): A dictionary containing file metadata and optionally the content.
            *   **Usage:** Not called by any other functions according to the provided context.

    #### Class: `GitRepository`
    *   **Summary:** "The GitRepository class manages a Git repository by cloning it into a temporary directory and providing access to its files through RepoFile objects. It supports listing all files, retrieving a hierarchical file tree, and cleaning up the temporary resources upon closing. The class implements context manager protocols (__enter__ and __exit__) to facilitate automatic resource management."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** `tempfile`, `shutil`, `git.Repo`, `git.GitCommandError`, `logging`, `os`
    *   **Constructor:**
        *   *Description:* "Initializes a GitRepository instance by cloning the specified repository URL into a temporary directory. It sets up necessary attributes such as the repository URL, temporary directory path, and references to the cloned repository and its latest commit. If cloning fails, it raises a RuntimeError after cleaning up any temporary resources."
        *   *Parameters:*
            - **repo_url** (`str`): The URL of the Git repository to clone.
    *   **Methods:**
        *   **`get_all_files`**
            *   *Signature:* `def get_all_files(self)`
            *   *Description:* Retrieves a list of all files in the repository and creates RepoFile objects for each file. These objects are stored internally and returned. The method uses git ls-files to enumerate files and filters out empty entries.
            *   *Parameters:*
            *   *Returns:*
                - **files** (`list[RepoFile]`): A list of RepoFile instances representing the files in the repository.
            *   **Usage:** Called by the `prepare_shared_input` function in MainLLM_evaluation.py at line 125.
        *   **`close`**
            *   *Signature:* `def close(self)`
            *   *Description:* Deletes the temporary directory and its contents associated with the repository. This method is intended to clean up resources when the repository is no longer needed.
            *   *Parameters:*
            *   *Returns:*
            *   **Usage:** Called by the `prepare_shared_input` function in MainLLM_evaluation.py at line 144.
        *   **`__enter__`**
            *   *Signature:* `def __enter__(self)`
            *   *Description:* "Enables the use of the GitRepository instance in a 'with' statement, returning itself to allow for context-managed usage."
            *   *Parameters:*
            *   *Returns:*
                - **GitRepository**: The GitRepository instance itself.
            *   **Usage:** Called implicitly when entering a 'with' block using this class.
        *   **`__exit__`**
            *   *Signature:* `def __exit__(self, exc_type, exc_val, exc_tb)`
            *   *Description:* "Automatically closes the repository when exiting a 'with' block, ensuring cleanup of temporary resources."
            *   *Parameters:*
                - **exc_type** (`Any`): Exception type, if an exception occurred during execution.
                - **exc_val** (`Any`): Exception value, if an exception occurred during execution.
                - **exc_tb** (`Any`): Exception traceback, if an exception occurred during execution.
            *   *Returns:*
            *   **Usage:** Called implicitly when exiting a 'with' block using this class.
        *   **`get_file_tree`**
            *   *Signature:* `def get_file_tree(self, include_content)`
            *   *Description:* "Constructs a hierarchical representation of the repository's file structure. If no files have been loaded yet, it fetches them first. Then, it builds a nested dictionary structure where directories and files are organized according to their paths."
            *   *Parameters:*
                - **include_content** (`bool`): Flag indicating whether to include file content in the returned dictionary.
            *   *Returns:*
                - **tree** (`dict`): A nested dictionary representing the file tree structure.
            *   **Usage:** Called by the `prepare_shared_input` function in MainLLM_evaluation.py at line 133.

    ### File: `backend/main.py`

    #### Function: `create_savings_chart`
    *   **Signature:** `def create_savings_chart(json_tokens, toon_tokens, savings_percent, output_path)`
    *   **Description:** "Die Funktion erstellt ein Balkendiagramm zur Darstellung des Token-Vergleichs zwischen JSON und TOON Format. Sie verwendet matplotlib, um die Daten zu visualisieren und speichert das Diagramm unter einem angegebenen Pfad. Das Diagramm zeigt die Anzahl der Tokens für beide Formate sowie den Prozentsatz der Einsparung."
    *   **Parameters:**
        - **json_tokens** (`int`): Die Anzahl der Tokens im JSON-Format.
        - **toon_tokens** (`int`): Die Anzahl der Tokens im TOON-Format.
        - **savings_percent** (`float`): Der Prozentsatz der Einsparung zwischen den beiden Formaten.
        - **output_path** (`str`): "Der Dateipfad, unter dem das generierte Diagramm gespeichert wird."
    *   **Returns:**
    *   **Usage:** Called by the `main_workflow` function in the file `main.py`.

    #### Function: `calculate_net_time`
    *   **Signature:** `def calculate_net_time(start_time, end_time, total_items, batch_size, model_name)`
    *   **Description:** "The function calculates the net time duration by subtracting sleep times related to rate limits from the total time elapsed between a start and end timestamp. It specifically handles cases where the model name starts with 'gemini-' and adjusts the calculation based on the number of batches and item count. If the model is not a gemini model, it returns the total duration directly. For zero items, it returns zero. Otherwise, it computes the sleep time based on batch count and subtracts it from the total duration."
    *   **Parameters:**
        - **start_time** (`float or datetime`): The starting timestamp of the operation.
        - **end_time** (`float or datetime`): The ending timestamp of the operation.
        - **total_items** (`int`): The total number of items processed.
        - **batch_size** (`int`): The size of each batch of items.
        - **model_name** (`str`): "The name of the model being used, which determines whether rate limit adjustments apply."
    *   **Returns:**
        - **net_time** (`float or int`): "The calculated net time after subtracting sleep durations, ensuring a non-negative result."
    *   **Usage:** "This function is called by the evaluation function in HelperLLM_evaluation.py at lines 249 and 275, and by the main_workflow function in main.py at lines 311 and 342."

    #### Function: `main_workflow`
    *   **Signature:** `def main_workflow(input, api_keys, model_names, status_callback)`
    *   **Description:** "The `main_workflow` function orchestrates a comprehensive code analysis pipeline that processes a GitHub repository input. It handles API key management, repository cloning, file extraction, and various analytical steps including basic information extraction, file tree construction, relationship analysis, and AST schema creation. The function then prepares inputs for a HelperLLM to analyze functions and classes, followed by a MainLLM to generate a final markdown report. It includes error handling, logging, and performance metrics tracking."
    *   **Parameters:**
        - **input** (`Any`): "The input data, typically a string containing a GitHub repository URL."
        - **api_keys** (`dict`): "A dictionary containing API keys for different services such as Gemini, OpenAI, and SCADsLLM."
        - **model_names** (`dict`): A dictionary specifying the names of models to be used for helper and main LLMs.
        - **status_callback** (`Callable[[str], None]`): An optional callback function to report progress updates.
    *   **Returns:**
        - **report** (`str`): The final markdown report generated by the MainLLM.
        - **metrics** (`dict`): Performance metrics including execution times for helper and main LLMs.
    *   **Usage:** Called by the `frontend.Frontend` function in `Frontend.py` at line 489 and by the `backend.main` function in `main.py` at line 533.

    #### Function: `update_status`
    *   **Signature:** `def update_status(msg)`
    *   **Description:** "The function 'update_status' is designed to handle status updates by invoking an optional callback function if one is defined, followed by logging the message using the standard logging module. It serves as a centralized mechanism for reporting status messages throughout the application."
    *   **Parameters:**
        - **msg** (`Any`): A message to be logged and optionally passed to a status callback function.
    *   **Returns:**
    *   **Usage:** "This function is invoked multiple times within the 'main_workflow' function in 'main.py', specifically at lines 81, 134, 158, 167, 175, 185, 195, 205, 301, 333, 336, 409, 412, and 430."

    #### Class: `schemas.types.ParameterDescription`
    *   **Summary:** "The ParameterDescription class is a Pydantic BaseModel designed to represent and validate the description of a single parameter within a function. It encapsulates three essential attributes: the parameter's name, its type, and a textual description. This class ensures data integrity and provides a standardized structure for parameter metadata, making it suitable for use in API schemas, documentation systems, or any application requiring structured parameter definitions."
    *   **Instantiation:** Not explicitly instantiated by any other component.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* "The constructor initializes a ParameterDescription instance with required fields: name, type, and description. It leverages Pydantic's BaseModel functionality to enforce type safety and validation."
        *   *Parameters:*
            - **name** (`str`): The name of the parameter.
            - **type** (`str`): The data type of the parameter.
            - **description** (`str`): A textual description of the parameter's purpose or usage.
    *   **Methods:**

    #### Class: `schemas.types.ReturnDescription`
    *   **Summary:** "The ReturnDescription class is a Pydantic BaseModel designed to represent and validate the description of a function's return value. It encapsulates three essential attributes: the name of the return value, its type, and a textual description. This class ensures data integrity and structure for return value metadata, making it suitable for use in API documentation, code analysis tools, or any system requiring standardized return value specifications."
    *   **Instantiation:** Not instantiated by any other component.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* "Initializes a ReturnDescription instance with a name, type, and description. These fields are required and must be provided during instantiation to create a valid object."
        *   *Parameters:*
            - **name** (`str`): The name of the return value.
            - **type** (`str`): The type of the return value.
            - **description** (`str`): A textual description of the return value.
    *   **Methods:**

    #### Class: `schemas.types.UsageContext`
    *   **Summary:** "The UsageContext class is a Pydantic model designed to represent and validate the calling context of a function. It encapsulates two string fields: 'calls', which describes what functions or methods are called by the function in question, and 'called_by', which indicates what function or method invokes the function in question. This class serves as a structured way to document and enforce the usage context of functions within a system."
    *   **Instantiation:** Not instantiated by any other component.
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes a UsageContext instance with two required string fields: 'calls' and 'called_by'."
        *   *Parameters:*
            - **calls** (`str`): A string describing the functions or methods called by the function.
            - **called_by** (`str`): A string describing the function or method that calls the function.
    *   **Methods:**

    #### Class: `schemas.types.FunctionDescription`
    *   **Summary:** "The FunctionDescription class is a Pydantic model designed to encapsulate detailed information about a function's purpose, parameters, return values, and usage context. It serves as a structured representation for documenting function signatures and behavior, making it suitable for API documentation, code analysis tools, or automated generation of function descriptions."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** Standard typing constructs and pydantic components.
    *   **Constructor:**
        *   *Description:* "Initializes a FunctionDescription instance with fields for overall function description, a list of parameter descriptions, a list of return value descriptions, and usage context."
        *   *Parameters:*
            - **overall** (`str`): A string describing the overall purpose and functionality of the class being analyzed.
            - **parameters** (`List[ParameterDescription]`): A list of ParameterDescription objects that detail each parameter of the function.
            - **returns** (`List[ReturnDescription]`): A list of ReturnDescription objects detailing the function's return values.
            - **usage_context** (`UsageContext`): An instance of UsageContext providing information on how the function is used.
    *   **Methods:**

    #### Class: `schemas.types.FunctionAnalysis`
    *   **Summary:** "The FunctionAnalysis class is a Pydantic model designed to represent the complete JSON schema for a function. It serves as a structured data container that holds essential information about a function, including its unique identifier, a detailed description, and an optional error field. This class is intended to provide a standardized way to encapsulate function metadata and potential errors in a type-safe manner."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes a FunctionAnalysis instance with a required identifier string, a required FunctionDescription object, and an optional error field that defaults to None."
        *   *Parameters:*
            - **identifier** (`str`): A unique identifier for the function.
            - **description** (`FunctionDescription`): "A detailed description of the function, represented by a FunctionDescription object."
            - **error** (`Optional[str]`): "An optional error message related to the function, defaulting to None."
    *   **Methods:**

    #### Class: `schemas.types.ConstructorDescription`
    *   **Summary:** The ConstructorDescription class is a Pydantic model designed to describe the initialization method (__init__) of a class. It captures a textual description of the constructor's purpose and a list of parameter descriptions that define its inputs.
    *   **Instantiation:** Not explicitly instantiated by any known component.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* Initializes a ConstructorDescription instance with a description of the constructor and a list of ParameterDescription objects detailing its parameters.
        *   *Parameters:*
            - **description** (`str`): A textual description of the constructor's purpose.
            - **parameters** (`List[ParameterDescription]`): "A list of ParameterDescription objects that detail each parameter of the constructor."
    *   **Methods:**

    #### Class: `schemas.types.ClassContext`
    *   **Summary:** The ClassContext class is a Pydantic model designed to encapsulate information about a class's external dependencies and the entities that instantiate it. It serves as a structured representation of metadata related to class usage and integration within a system.
    *   **Instantiation:** Not instantiated by any other component.
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes a ClassContext instance with two string attributes: 'dependencies' and 'instantiated_by'. These fields store information about the class's external dependencies and the entities that create instances of the class, respectively."
        *   *Parameters:*
            - **dependencies** (`str`): A string describing the external dependencies of the class.
            - **instantiated_by** (`str`): A string describing the entities or components that instantiate this class.
    *   **Methods:**

    #### Class: `schemas.types.ClassDescription`
    *   **Summary:** "The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It holds information about the class's overall purpose, its constructor details, a list of its methods along with their descriptions, and contextual usage information."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes a new instance of the ClassDescription class with specified attributes for overall purpose, constructor description, methods analysis, and usage context."
        *   *Parameters:*
            - **overall** (`str`): "A string describing the overall purpose and functionality of the class being analyzed."
            - **init_method** (`ConstructorDescription`): "An instance of ConstructorDescription that details the initialization process and parameters of the class."
            - **methods** (`List[FunctionAnalysis]`): "A list of FunctionAnalysis objects, each representing a detailed breakdown of a method within the class."
            - **usage_context** (`ClassContext`): "An instance of ClassContext providing information on how the class is used and its dependencies."
    *   **Methods:**

    #### Class: `schemas.types.ClassAnalysis`
    *   **Summary:** "The ClassAnalysis class serves as the primary data model for representing the complete JSON schema of a class. It encapsulates essential information about a class including its identifier, a detailed description, and an optional error message. This class is designed to provide a standardized structure for documenting class metadata and associated descriptions."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes a new instance of the ClassAnalysis class with required fields for the identifier and description, and an optional error field."
        *   *Parameters:*
            - **identifier** (`str`): "A string identifier for the class being analyzed."
            - **description** (`ClassDescription`): "An instance of ClassDescription containing detailed information about the class."
            - **error** (`Optional[str]`): "An optional string field to store any error messages related to the class analysis."
    *   **Methods:**

    #### Class: `schemas.types.CallInfo`
    *   **Summary:** "The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure for documenting call relationships within the system."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** None identified for this class.
    *   **Constructor:**
        *   *Description:* "Initializes a CallInfo instance with file, function, mode, and line attributes to represent a call event."
        *   *Parameters:*
            - **file** (`str`): "The file path where the call occurred."
            - **function** (`str`): "The name of the function that made the call."
            - **mode** (`str`): "The mode of the call, such as 'method', 'function', or 'module'."
            - **line** (`int`): "The line number in the file where the call occurred."
    *   **Methods:**

    #### Class: `schemas.types.FunctionContextInput`
    *   **Summary:** "The FunctionContextInput class is a Pydantic model designed to structure contextual information for analyzing a function. It encapsulates two key pieces of information: a list of function names that the analyzed function calls, and a list of CallInfo objects indicating which functions call the analyzed function. This class serves as a data container to facilitate function analysis and dependency tracking within a codebase."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes the FunctionContextInput instance with two attributes: 'calls', a list of strings representing function names called by the analyzed function, and 'called_by', a list of CallInfo objects representing functions that call the analyzed function."
        *   *Parameters:*
            - **calls** (`List[str]`): "A list of strings representing the names of functions called by the analyzed function."
            - **called_by** (`List[CallInfo]`): "A list of CallInfo objects representing the functions that call the analyzed function."
    *   **Methods:**

    #### Class: `schemas.types.FunctionAnalysisInput`
    *   **Summary:** "The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates essential metadata and contextual information required for function analysis, including the mode of operation, identifier, source code, imports, and associated context."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** Standard typing and pydantic components.
    *   **Constructor:**
        *   *Description:* "Initializes a FunctionAnalysisInput instance with fields for mode, identifier, source code, imports, and context. The mode is constrained to the literal value 'function_analysis', ensuring strict adherence to the intended usage pattern."
        *   *Parameters:*
            - **mode** (`Literal["function_analysis"]`): "A literal string indicating the mode of operation, constrained to 'function_analysis'."
            - **identifier** (`str`): "A unique identifier for the function being analyzed."
            - **source_code** (`str`): "The raw source code of the function to be analyzed."
            - **imports** (`List[str]`): "A list of import statements used in the function's source code."
            - **context** (`FunctionContextInput`): "Additional contextual information required for the function analysis."
    *   **Methods:**

    #### Class: `schemas.types.MethodContextInput`
    *   **Summary:** "The MethodContextInput class is a Pydantic model designed to structure contextual information about a method within a class. It encapsulates details such as the method's identifier, the methods it calls, the methods that call it, its arguments, and its docstring. This class serves as a standardized way to represent and exchange method-level metadata in a system."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "The class is initialized with a set of predefined attributes including identifier, calls, called_by, args, and docstring. These attributes are typed using Pydantic's type hints and optional types to enforce data integrity."
        *   *Parameters:*
            - **identifier** (`str`): "A string identifier for the method."
            - **calls** (`List[str]`): "A list of strings representing the identifiers of methods called by this method."
            - **called_by** (`List[CallInfo]`): "A list of CallInfo objects representing the methods that call this method."
            - **args** (`List[str]`): "A list of strings representing the argument names of the method."
            - **docstring** (`Optional[str]`): "An optional string containing the docstring of the method."
    *   **Methods:**

    #### Class: `schemas.types.ClassContextInput`
    *   **Summary:** "The ClassContextInput class is a Pydantic model designed to encapsulate structured context information for analyzing a class. It holds three key pieces of information: a list of dependencies, a list of call information for where the class is instantiated, and a list of method context inputs for each method within the class."
    *   **Instantiation:** `HelperLLM.py`, `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "The constructor initializes the ClassContextInput instance with three attributes: dependencies, instantiated_by, and method_context. These attributes are intended to store contextual metadata about a class being analyzed."
        *   *Parameters:*
            - **dependencies** (`List[str]`): "A list of strings representing the dependencies of the class."
            - **instantiated_by** (`List[CallInfo]`): "A list of CallInfo objects indicating where the class is instantiated."
            - **method_context** (`List[MethodContextInput]`): "A list of MethodContextInput objects describing the context for each method in the class."
    *   **Methods:**

    #### Class: `schemas.types.ClassAnalysisInput`
    *   **Summary:** "The ClassAnalysisInput class serves as a structured input model for generating ClassAnalysis objects. It encapsulates all necessary information required for analyzing a Python class, including its source code, import statements, and contextual metadata such as instantiation details and dependencies."
    *   **Instantiation:** `HelperLLM.py`, `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** Standard typing and pydantic components.
    *   **Constructor:**
        *   *Description:* "Initializes the ClassAnalysisInput instance with fields representing the mode of analysis, the identifier of the class being analyzed, the source code of the class, a list of import statements, and contextual information about how the class is used."
        *   *Parameters:*
            - **mode** (`Literal["class_analysis"]`): "A literal string indicating the mode of analysis, specifically set to 'class_analysis'."
            - **identifier** (`str`): "A string identifier for the class being analyzed."
            - **source_code** (`str`): "The raw source code of the class being analyzed."
            - **imports** (`List[str]`): "A list of import statements associated with the class."
            - **context** (`ClassContextInput`): "An object containing contextual information about the class, such as dependencies and instantiation locations."
    *   **Methods:**

    ### File: `database/db.py`

    #### Function: `encrypt_text`
    *   **Signature:** `def encrypt_text(text)`
    *   **Description:** "The function encrypts a given text string using a Fernet cipher suite. It first checks if the input text is empty or if the cipher suite is not initialized, returning the original text in such cases. Otherwise, it encodes the stripped text, encrypts it, and returns the decrypted result as a string."
    *   **Parameters:**
        - **text** (`str`): The text string to be encrypted.
    *   **Returns:**
        - **encrypted_text** (`str`): "The encrypted version of the input text, returned as a string."
    *   **Usage:** Called by the `update_gemini_key` function in the db.py file.

    #### Function: `decrypt_text`
    *   **Signature:** `def decrypt_text(text)`
    *   **Description:** "The function decrypts a given text using a cipher suite, returning the decrypted string if successful. If the input text is empty or the cipher suite is not available, it returns the original text. In case of decryption failure, it also returns the original text. This function acts as a safe wrapper around the decryption process, ensuring that invalid inputs or errors do not cause crashes."
    *   **Parameters:**
        - **text** (`str`): The encrypted text to be decrypted.
    *   **Returns:**
        - **result** (`str`): "The decrypted text if successful; otherwise, the original input text."
    *   **Usage:** Called by the function `get_decrypted_api_keys` in the file `db.py`.

    #### Function: `insert_user`
    *   **Signature:** `def insert_user(username, name, password)`
    *   **Description:** "The function inserts a new user into the database by creating a user document with the provided username, name, and password. It hashes the password using a hasher utility before storing the user information. The function also initializes additional fields such as API keys and returns the ID of the inserted document."
    *   **Parameters:**
        - **username** (`str`): "The unique identifier for the user, used as the '_id' field in the database."
        - **name** (`str`): The full name of the user to be stored in the database.
        - **password** (`str`): "The plain text password of the user, which gets hashed before storage."
    *   **Returns:**
        - **inserted_id** (`ObjectId`): The unique identifier of the newly inserted user document in the database.
    *   **Usage:** Called by the `frontend.Frontend` class in the `Frontend.py` file at line 294.

    #### Function: `fetch_all_users`
    *   **Signature:** `def fetch_all_users()`
    *   **Description:** "This function retrieves all user documents from a MongoDB collection named 'dbusers'. It performs a database query to find all records in the collection and returns them as a list. The function does not take any parameters and directly accesses the global 'dbusers' variable, which is presumably initialized elsewhere in the codebase."
    *   **Parameters:**
    *   **Returns:**
        - **result** (`list`): A list containing all user documents retrieved from the 'dbusers' MongoDB collection.
    *   **Usage:** Called by the `frontend.Frontend` class in the `Frontend.py` file at line 244.

    #### Function: `fetch_user`
    *   **Signature:** `def fetch_user(username)`
    *   **Description:** The function 'fetch_user' retrieves a user document from a MongoDB collection named 'dbusers' based on the provided username. It performs a lookup operation using the username as the identifier field '_id'. The function assumes that the 'dbusers' collection and the MongoDB connection are properly initialized and accessible within the scope of the function.
    *   **Parameters:**
        - **username** (`str`): "The unique identifier (username) used to locate the specific user document in the 'dbusers' collection."
    *   **Returns:**
        - **result** (`Any`): "The user document retrieved from the 'dbusers' collection, or None if no matching document is found."
    *   **Usage:** Not called by any other functions in the provided context.

    #### Function: `update_user_name`
    *   **Signature:** `def update_user_name(username, new_name)`
    *   **Description:** "This function updates the name field of a user in the database identified by their username. It uses a MongoDB update operation to modify only the 'name' field of the document matching the given username. The function returns the count of modified documents, which indicates whether the update was successful."
    *   **Parameters:**
        - **username** (`str`): "The unique identifier (username) of the user whose name needs to be updated."
        - **new_name** (`str`): The new name value to set for the specified user.
    *   **Returns:**
        - **result.modified_count** (`int`): "The number of documents that were modified as a result of the update operation. This indicates whether the update was applied to any document."
    *   **Usage:** Not called by any other functions according to the provided context.

    #### Function: `update_gemini_key`
    *   **Signature:** `def update_gemini_key(username, gemini_api_key)`
    *   **Description:** "This function updates the Gemini API key for a specified user in the database. It first encrypts the provided API key using a text encryption function, then performs an update operation on the 'dbusers' collection to store the encrypted key under the user's ID. The function returns the count of modified documents, indicating whether the update was successful."
    *   **Parameters:**
        - **username** (`str`): "The unique identifier for the user whose Gemini API key needs to be updated."
        - **gemini_api_key** (`str`): "The new Gemini API key to be stored for the user, which will be stripped of whitespace and encrypted before storage."
    *   **Returns:**
        - **modified_count** (`int`): "The number of documents that were successfully modified as a result of the update operation."
    *   **Usage:** Called by `save_gemini_cb` in `Frontend.py` at line 35 and by `frontend.Frontend` in `Frontend.py` at line 393.

    #### Function: `update_ollama_url`
    *   **Signature:** `def update_ollama_url(username, ollama_base_url)`
    *   **Description:** "This function updates the Ollama base URL for a specified user in the database. It takes a username and a new Ollama base URL as inputs, strips any leading or trailing whitespace from the URL, and performs an update operation on the user document. The function returns the count of modified documents, which should be 1 if the update was successful."
    *   **Parameters:**
        - **username** (`str`): "The unique identifier of the user whose Ollama base URL needs to be updated."
        - **ollama_base_url** (`str`): "The new Ollama base URL to be set for the specified user. Leading and trailing whitespace will be stripped."
    *   **Returns:**
        - **modified_count** (`int`): "The number of documents that were successfully modified by the update operation. Typically 1 if the user exists and the update was applied."
    *   **Usage:** Called by `save_ollama_cb` in `Frontend.py` at line 42 and by `frontend.Frontend` in `Frontend.py` at line 407.

    #### Function: `fetch_gemini_key`
    *   **Signature:** `def fetch_gemini_key(username)`
    *   **Description:** "The function retrieves a Gemini API key associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'gemini_api_key' field. If no matching user is found, it returns None."
    *   **Parameters:**
        - **username** (`str`): "The unique identifier for the user whose Gemini API key is to be retrieved."
    *   **Returns:**
        - **gemini_api_key** (`Optional[str]`): "The Gemini API key associated with the user, or None if the user is not found."
    *   **Usage:** Not called by any other functions according to the provided context.

    #### Function: `fetch_ollama_url`
    *   **Signature:** `def fetch_ollama_url(username)`
    *   **Description:** "The function retrieves the Ollama base URL associated with a given username from a MongoDB collection. It queries the 'dbusers' collection to find a document matching the username and extracts the 'ollama_base_url' field. If no matching user is found, it returns None."
    *   **Parameters:**
        - **username** (`str`): "The unique identifier for the user whose Ollama base URL is to be retrieved."
    *   **Returns:**
        - **ollama_base_url** (`str or None`): "The Ollama base URL associated with the user, or None if the user is not found."
    *   **Usage:** Not called by any other functions according to the provided context.

    #### Function: `delete_user`
    *   **Signature:** `def delete_user(username)`
    *   **Description:** "The function 'delete_user' removes a user document from a MongoDB collection based on the provided username. It performs a deletion operation using the 'delete_one' method and returns the count of deleted documents. The function assumes the existence of a global 'dbusers' variable representing a MongoDB collection."
    *   **Parameters:**
        - **username** (`str`): "The unique identifier (username) of the user to be deleted from the database."
    *   **Returns:**
        - **deleted_count** (`int`): "The number of documents deleted as a result of the operation, typically 0 or 1."
    *   **Usage:** Not called by any other functions according to the provided context.

    #### Function: `get_decrypted_api_keys`
    *   **Signature:** `def get_decrypted_api_keys(username)`
    *   **Description:** "This function retrieves and decrypts API keys for a given username from a database. It first fetches the user document using the username as the identifier. If the user does not exist, it returns two None values. If the user exists, it attempts to decrypt the 'gemini_api_key' field using a decryption function and retrieves the 'ollama_base_url' directly. Both decrypted and plain text values are returned as a tuple."
    *   **Parameters:**
        - **username** (`str`): "The unique identifier for the user whose API keys are to be retrieved."
    *   **Returns:**
        - **gemini_plain** (`str`): "The decrypted Gemini API key for the user, or an empty string if not found."
        - **ollama_plain** (`str`): "The Ollama base URL for the user, or an empty string if not found."
    *   **Usage:** Called by the `Frontend` class in `Frontend.py` at lines 380 and 479.

    #### Function: `insert_chat`
    *   **Signature:** `def insert_chat(username, chat_name)`
    *   **Description:** "The function 'insert_chat' creates a new chat entry in the database with a unique identifier, associated username, chat name, and timestamp. It generates a UUID for the chat ID, records the current datetime as creation time, and inserts the chat document into the 'dbchats' collection. The function returns the ID of the newly inserted chat document."
    *   **Parameters:**
        - **username** (`str`): "The username associated with the chat."
        - **chat_name** (`str`): "The name of the chat."
    *   **Returns:**
        - **result.inserted_id** (`str`): "The unique identifier of the newly inserted chat document."
    *   **Usage:** "This function is called by load_data_from_db in Frontend.py at line 81, handle_delete_chat in Frontend.py at line 122, and frontend.Frontend in Frontend.py at line 344."

    #### Function: `fetch_chats_by_user`
    *   **Signature:** `def fetch_chats_by_user(username)`
    *   **Description:** "Die Funktion fetch_chats_by_user ruft alle Chats eines bestimmten Benutzers aus einer MongoDB-Datenbank ab. Sie verwendet den Benutzernamen als Filterkriterium und sortiert die Ergebnisse nach dem Erstellungsdatum in aufsteigender Reihenfolge. Das Ergebnis ist eine Liste der gefundenen Chat-Dokumente."
    *   **Parameters:**
        - **username** (`str`): "Der Benutzername, dessen Chats abgerufen werden sollen."
    *   **Returns:**
        - **chats** (`list`): "Eine Liste aller Chat-Dokumente des angegebenen Benutzers, sortiert nach Erstellungsdatum."
    *   **Usage:** Called by the `load_data_from_db` function in the `Frontend.py` file.

    #### Function: `check_chat_exists`
    *   **Signature:** `def check_chat_exists(username, chat_name)`
    *   **Description:** "This function checks whether a specific chat entry exists in the database for a given username and chat name. It performs a query using MongoDB's find_one method to locate a document matching both the username and chat name. If such a document is found, the function returns True; otherwise, it returns False."
    *   **Parameters:**
        - **username** (`str`): "The username associated with the chat."
        - **chat_name** (`str`): "The name of the chat to check for existence."
    *   **Returns:**
        - **exists** (`bool`): "True if a chat with the specified username and chat name exists in the database, False otherwise."
    *   **Usage:** Not called by any other functions according to the provided context.

    #### Function: `rename_chat_fully`
    *   **Signature:** `def rename_chat_fully(username, old_name, new_name)`
    *   **Description:** "This function renames a chat and updates all associated exchanges in the database. It first updates the chat entry in the chats collection, then updates all related exchange entries in the exchanges collection to reflect the new chat name. The function returns the number of modified chat documents."
    *   **Parameters:**
        - **username** (`str`): "The username associated with the chat to be renamed."
        - **old_name** (`str`): "The current name of the chat to be renamed."
        - **new_name** (`str`): "The new name to assign to the chat."
    *   **Returns:**
        - **modified_count** (`int`): "The number of chat documents that were successfully modified."
    *   **Usage:** Called by the `frontend.Frontend` function in the `Frontend.py` file at line 462.

    #### Function: `insert_exchange`
    *   **Signature:** `def insert_exchange(question, answer, feedback, username, chat_name, helper_used="", main_used="", total_time="", helper_time="", main_time="")`
    *   **Description:** "This function inserts a new exchange record into a MongoDB collection. It generates a unique ID for the exchange, constructs a dictionary with all the provided details including question, answer, feedback, and metadata, and attempts to insert this document into the database. If the insertion is successful, it returns the generated ID; otherwise, it catches any exceptions, prints an error message, and returns None."
    *   **Parameters:**
        - **question** (`str`): "The question associated with the exchange."
        - **answer** (`str`): "The answer provided in response to the question."
        - **feedback** (`str`): "Feedback related to the exchange."
        - **username** (`str`): "The username of the user involved in the exchange."
        - **chat_name** (`str`): "The name of the chat session."
        - **helper_used** (`str`): "Optional field indicating which helper was used."
        - **main_used** (`str`): "Optional field indicating which main component was used."
        - **total_time** (`str`): "Optional field for the total time taken for the exchange."
        - **helper_time** (`str`): "Optional field for the time taken by the helper component."
        - **main_time** (`str`): "Optional field for the time taken by the main component."
    *   **Returns:**
        - **new_id** (`str`): "The unique identifier of the inserted exchange record, or None if insertion fails."
    *   **Usage:** Called by the `frontend.Frontend` class in `Frontend.py` at line 530.

    #### Function: `fetch_exchanges_by_user`
    *   **Signature:** `def fetch_exchanges_by_user(username)`
    *   **Description:** "This function retrieves all exchange records from a MongoDB collection for a given username, sorted by creation timestamp in ascending order. It uses the pymongo library to query the database and returns the results as a list. The sorting ensures that exchanges are displayed chronologically, which is important for user interface purposes."
    *   **Parameters:**
        - **username** (`str`): "The unique identifier of the user whose exchange records are to be fetched."
    *   **Returns:**
        - **exchanges** (`list`): "A list of exchange records retrieved from the database for the specified user, sorted by creation timestamp in ascending order."
    *   **Usage:** Called by the `load_data_from_db` function in the `Frontend.py` file.

    #### Function: `fetch_exchanges_by_chat`
    *   **Signature:** `def fetch_exchanges_by_chat(username, chat_name)`
    *   **Description:** "This function retrieves a sorted list of exchanges from a MongoDB collection based on a given username and chat name. It queries the 'dbexchanges' collection with specific criteria and orders the results by creation date in ascending order. The function returns the fetched documents as a list."
    *   **Parameters:**
        - **username** (`str`): "The username associated with the exchanges to be retrieved."
        - **chat_name** (`str`): "The name of the chat associated with the exchanges to be retrieved."
    *   **Returns:**
        - **exchanges** (`list`): "A list of exchange documents matching the provided username and chat name, sorted by creation date in ascending order."
    *   **Usage:** Not called by any other functions according to the provided context.

    #### Function: `update_exchange_feedback`
    *   **Signature:** `def update_exchange_feedback(exchange_id, feedback)`
    *   **Description:** "This function updates the feedback field of a document in the 'dbexchanges' collection within a MongoDB database. It takes an exchange ID and a feedback value, then attempts to update the corresponding document with the new feedback value. The function returns the count of modified documents, which indicates whether the update was successful."
    *   **Parameters:**
        - **exchange_id** (`Any`): "The unique identifier of the exchange document to be updated."
        - **feedback** (`int`): "The feedback value to be set in the document."
    *   **Returns:**
        - **modified_count** (`int`): "The number of documents that were modified by the update operation."
    *   **Usage:** Called by `handle_feedback_change` in `Frontend.py` at line 98.

    #### Function: `update_exchange_feedback_message`
    *   **Signature:** `def update_exchange_feedback_message(exchange_id, feedback_message)`
    *   **Description:** "This function updates the feedback message associated with a specific exchange ID in a MongoDB collection. It uses the 'update_one' method to modify a document where the '_id' field matches the provided exchange ID, setting the 'feedback_message' field to the new value. The function returns the count of modified documents, which indicates whether the update was successful."
    *   **Parameters:**
        - **exchange_id** (`Any`): "The unique identifier of the exchange document to be updated."
        - **feedback_message** (`str`): "The new feedback message to be set for the specified exchange."
    *   **Returns:**
        - **modified_count** (`int`): "The number of documents that were modified as a result of the update operation."
    *   **Usage:** Called by `render_exchange` in `Frontend.py` at line 211.

    #### Function: `delete_exchange_by_id`
    *   **Signature:** `def delete_exchange_by_id(exchange_id)`
    *   **Description:** "This function deletes a document from the 'dbexchanges' collection in a MongoDB database based on a provided exchange ID. It performs a deletion operation and returns the count of deleted documents. The function takes a single string parameter representing the unique identifier of the exchange to be deleted."
    *   **Parameters:**
        - **exchange_id** (`str`): "A string representing the unique identifier of the exchange document to be deleted from the database."
    *   **Returns:**
        - **deleted_count** (`int`): "The number of documents successfully deleted from the database, typically 0 or 1."
    *   **Usage:** Called by the `handle_delete_exchange` function in `Frontend.py` at line 102.

    #### Function: `delete_full_chat`
    *   **Signature:** `def delete_full_chat(username, chat_name)`
    *   **Description:** "The function deletes a full chat and all associated exchanges from the database. It first removes all exchange records linked to the specified username and chat name, followed by deleting the chat record itself. The function returns the count of deleted chat documents, ensuring consistency between frontend and backend data."
    *   **Parameters:**
        - **username** (`str`): "The username associated with the chat to be deleted."
        - **chat_name** (`str`): "The name of the chat to be deleted."
    *   **Returns:**
        - **deleted_count** (`int`): "The number of chat documents that were deleted from the database."
    *   **Usage:** Called by the `handle_delete_chat` function in the `Frontend.py` file.

    ### File: `frontend/Frontend.py`

    #### Function: `save_gemini_cb`
    *   **Signature:** `def save_gemini_cb()`
    *   **Description:** "This function handles the saving of a Gemini API key entered by the user in a Streamlit frontend application. It retrieves the key from the session state, updates the database with the new key for the current user, clears the input field, and displays a success message to the user."
    *   **Parameters:**
    *   **Returns:**
    *   **Usage:** Not called by any other function within the provided context.

    #### Function: `save_ollama_cb`
    *   **Signature:** `def save_ollama_cb()`
    *   **Description:** "This function handles the callback for saving an Ollama URL entered by the user in a Streamlit frontend. It retrieves the URL from the session state, updates the database with the new URL associated with the user's username, and displays a success toast message. The function does not return any value."
    *   **Parameters:**
    *   **Returns:**
    *   **Usage:** Not called by any other function within the provided context.

    #### Function: `load_data_from_db`
    *   **Signature:** `def load_data_from_db(username)`
    *   **Description:** "Die Funktion 'load_data_from_db' lädt Chats und Exchanges konsistent aus einer Datenbank für einen bestimmten Benutzer. Sie prüft zunächst, ob der Benutzer bereits geladen wurde, und lädt nur dann neue Daten, wenn dies erforderlich ist. Zunächst werden Chats aus der Datenbank abgerufen und in den Session-Zustand eingefügt. Anschließend werden Exchanges abgerufen und den entsprechenden Chats zugeordnet. Bei Bedarf wird ein Standard-Chat erstellt und als aktiv markiert."
    *   **Parameters:**
        - **username** (`str`): "Der Name des Benutzers, für den die Daten aus der Datenbank geladen werden sollen."
    *   **Returns:**
    *   **Usage:** Called by the `frontend.Frontend` method in `Frontend.py` at line 310.

    #### Function: `handle_feedback_change`
    *   **Signature:** `def handle_feedback_change(ex, val)`
    *   **Description:** "This function updates the feedback value for a given exchange object in the database and triggers a Streamlit rerun to refresh the UI. It takes an exchange dictionary and a new feedback value as inputs, modifies the exchange's feedback field, updates the corresponding record in the database, and then refreshes the Streamlit application."
    *   **Parameters:**
        - **ex** (`dict`): "A dictionary representing an exchange object, expected to contain keys such as 'feedback' and '_id'."
        - **val** (`Any`): The new feedback value to be assigned to the exchange object.
    *   **Returns:**
    *   **Usage:** Called by `render_exchange` in `Frontend.py` at lines 199 and 204.

    #### Function: `handle_delete_exchange`
    *   **Signature:** `def handle_delete_exchange(chat_name, ex)`
    *   **Description:** "This function handles the deletion of an exchange from the database and updates the session state to reflect the removal of the exchange from the specified chat. It first deletes the exchange from the database using its ID, then checks if the exchange exists in the session state for the given chat and removes it if found. Finally, it triggers a rerun of the Streamlit app to update the UI."
    *   **Parameters:**
        - **chat_name** (`str`): "The name of the chat from which the exchange is to be removed."
        - **ex** (`dict`): "A dictionary representing the exchange to be deleted, expected to contain an '_id' key."
    *   **Returns:**
    *   **Usage:** Called by the `render_exchange` function in `Frontend.py` at lines 228 and 234.

    #### Function: `handle_delete_chat`
    *   **Signature:** `def handle_delete_chat(username, chat_name)`
    *   **Description:** "The function handles the deletion of a chat by first removing the chat from the database and then cleaning up the session state. It ensures that the active chat is updated appropriately, either by selecting another existing chat or by creating a new default chat if none remain. Finally, it triggers a rerun of the Streamlit app to reflect the changes."
    *   **Parameters:**
        - **username** (`str`): "The username associated with the chat to be deleted."
        - **chat_name** (`str`): "The name of the chat to be deleted."
    *   **Returns:**
    *   **Usage:** Called by the `frontend.Frontend` class in `Frontend.py` at line 367.

    #### Function: `extract_repo_name`
    *   **Signature:** `def extract_repo_name(text)`
    *   **Description:** "The function 'extract_repo_name' takes a text input and attempts to extract a repository name from any URL present in the text. It uses regular expressions to find a URL, parses it using urllib.parse.urlparse, and then extracts the last segment of the URL path, removing the '.git' suffix if present. If no valid URL is found or if the URL does not contain a usable path, the function returns None."
    *   **Parameters:**
        - **text** (`str`): "A string that may contain a URL from which to extract the repository name."
    *   **Returns:**
        - **repo_name** (`str`): "The extracted repository name from the URL, with '.git' suffix removed if present, or None if no valid URL or path is found."
    *   **Usage:** Called by the `frontend.Frontend` class, specifically at line 442 in the file `Frontend.py`.

    #### Function: `stream_text_generator`
    *   **Signature:** `def stream_text_generator(text)`
    *   **Description:** "The function `stream_text_generator` takes a string of text as input and yields each word in the text followed by a space, with a small delay between each word. This creates a streaming effect where words are produced one at a time. It uses the `time.sleep` function to introduce a brief pause between yielding each word."
    *   **Parameters:**
        - **text** (`str`): "A string containing the text to be streamed word by word."
    *   **Returns:**
    *   **Usage:** Called by the function `render_text_with_mermaid` in the file `Frontend.py` at line 160.

    #### Function: `render_text_with_mermaid`
    *   **Signature:** `def render_text_with_mermaid(markdown_text, should_stream)`
    *   **Description:** "This function processes a markdown text string to identify and render Mermaid diagrams embedded within code blocks. It splits the input text by Mermaid code blocks, rendering regular markdown content normally and Mermaid diagrams using a specialized Mermaid component. If rendering fails, it falls back to displaying the Mermaid code as a plain code block. The function supports streaming output based on a flag."
    *   **Parameters:**
        - **markdown_text** (`str`): "A string containing markdown text that may include Mermaid diagram code blocks enclosed in triple backticks with 'mermaid' language specifier."
        - **should_stream** (`bool`): "A boolean flag indicating whether to stream the rendered markdown text or render it all at once."
    *   **Returns:**
    *   **Usage:** Called by the `render_exchange` method in `Frontend.py` at line 238 and by the `frontend.Frontend` module at line 524.

    #### Function: `render_exchange`
    *   **Signature:** `def render_exchange(ex, current_chat_name)`
    *   **Description:** "The function `render_exchange` renders a chat exchange in a Streamlit interface, displaying a user's question and an assistant's response. It handles both successful responses and error cases, providing interactive elements such as feedback buttons, comment popovers, download options, and delete functionality. The assistant's response can include Mermaid diagrams rendered via a helper function. The function uses various Streamlit components to build a rich UI for managing chat exchanges."
    *   **Parameters:**
        - **ex** (`dict`): "A dictionary representing the exchange, containing keys like 'question', 'answer', 'feedback', 'feedback_message', '_id', etc."
        - **current_chat_name** (`str`): "The name of the current chat session, used for handling deletion operations."
    *   **Returns:**
    *   **Usage:** Called by the `frontend.Frontend` class, specifically at line 429 in `Frontend.py`.

    ### File: `schemas/types.py`

    #### Class: `schemas.types.ParameterDescription`
    *   **Summary:** "The ParameterDescription class is a Pydantic BaseModel designed to represent and validate the description of a single parameter within a function. It encapsulates three essential attributes: the parameter's name, its type, and a textual description. This class ensures data integrity and provides a standardized structure for parameter metadata, making it suitable for use in API schemas, documentation systems, or any application requiring structured parameter definitions."
    *   **Instantiation:** Not explicitly instantiated by any other component.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* "The constructor initializes a ParameterDescription instance with required fields: name, type, and description. It leverages Pydantic's BaseModel functionality to enforce type safety and validation."
        *   *Parameters:*
            - **name** (`str`): The name of the parameter.
            - **type** (`str`): The data type of the parameter.
            - **description** (`str`): A textual description of the parameter's purpose or usage.
    *   **Methods:**

    #### Class: `schemas.types.ReturnDescription`
    *   **Summary:** "The ReturnDescription class is a Pydantic BaseModel designed to represent and validate the description of a function's return value. It encapsulates three essential attributes: the name of the return value, its type, and a textual description. This class ensures data integrity and structure for return value metadata, making it suitable for use in API documentation, code analysis tools, or any system requiring standardized return value specifications."
    *   **Instantiation:** Not instantiated by any other component.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* "Initializes a ReturnDescription instance with a name, type, and description. These fields are required and must be provided during instantiation to create a valid object."
        *   *Parameters:*
            - **name** (`str`): The name of the return value.
            - **type** (`str`): The type of the return value.
            - **description** (`str`): A textual description of the return value.
    *   **Methods:**

    #### Class: `schemas.types.UsageContext`
    *   **Summary:** "The UsageContext class is a Pydantic model designed to represent and validate the calling context of a function. It encapsulates two string fields: 'calls', which describes what functions or methods are called by the function in question, and 'called_by', which indicates what function or method invokes the function in question. This class serves as a structured way to document and enforce the usage context of functions within a system."
    *   **Instantiation:** Not instantiated by any other component.
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes a UsageContext instance with two required string fields: 'calls' and 'called_by'."
        *   *Parameters:*
            - **calls** (`str`): A string describing the functions or methods called by the function.
            - **called_by** (`str`): "A string describing the function or method that calls the function."
    *   **Methods:**

    #### Class: `schemas.types.FunctionDescription`
    *   **Summary:** "The FunctionDescription class is a Pydantic model designed to encapsulate detailed information about a function's purpose, parameters, return values, and usage context. It serves as a structured representation for documenting function signatures and behavior, making it suitable for API documentation, code analysis tools, or automated generation of function descriptions."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** Standard typing constructs and pydantic components.
    *   **Constructor:**
        *   *Description:* "Initializes a FunctionDescription instance with fields for overall function description, a list of parameter descriptions, a list of return value descriptions, and usage context."
        *   *Parameters:*
            - **overall** (`str`): "A string describing the overall purpose and functionality of the class being analyzed."
            - **parameters** (`List[ParameterDescription]`): "A list of ParameterDescription objects that detail each parameter of the function."
            - **returns** (`List[ReturnDescription]`): "A list of ReturnDescription objects detailing the function's return values."
            - **usage_context** (`UsageContext`): "An instance of UsageContext providing information on how the function is used."
    *   **Methods:**

    #### Class: `schemas.types.FunctionAnalysis`
    *   **Summary:** "The FunctionAnalysis class is a Pydantic model designed to represent the complete JSON schema for a function. It serves as a structured data container that holds essential information about a function, including its unique identifier, a detailed description, and an optional error field. This class is intended to provide a standardized way to encapsulate function metadata and potential errors in a type-safe manner."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes a FunctionAnalysis instance with a required identifier string, a required FunctionDescription object, and an optional error field that defaults to None."
        *   *Parameters:*
            - **identifier** (`str`): "A unique identifier for the function."
            - **description** (`FunctionDescription`): "A detailed description of the function, represented by a FunctionDescription object."
            - **error** (`Optional[str]`): "An optional error message related to the function, defaulting to None."
    *   **Methods:**

    #### Class: `schemas.types.ConstructorDescription`
    *   **Summary:** The ConstructorDescription class is a Pydantic model designed to describe the initialization method (__init__) of a class. It captures a textual description of the constructor's purpose and a list of parameter descriptions that define its inputs.
    *   **Instantiation:** Not explicitly instantiated by any known component.
    *   **Dependencies:** `pydantic.BaseModel`
    *   **Constructor:**
        *   *Description:* Initializes a ConstructorDescription instance with a description of the constructor and a list of ParameterDescription objects detailing its parameters.
        *   *Parameters:*
            - **description** (`str`): "A textual description of the constructor's purpose."
            - **parameters** (`List[ParameterDescription]`): "A list of ParameterDescription objects that detail each parameter of the constructor."
    *   **Methods:**

    #### Class: `schemas.types.ClassContext`
    *   **Summary:** The ClassContext class is a Pydantic model designed to encapsulate information about a class's external dependencies and the entities that instantiate it. It serves as a structured representation of metadata related to class usage and integration within a system.
    *   **Instantiation:** Not instantiated by any other component.
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes a ClassContext instance with two string attributes: 'dependencies' and 'instantiated_by'. These fields store information about the class's external dependencies and the entities that create instances of the class, respectively."
        *   *Parameters:*
            - **dependencies** (`str`): "A string describing the external dependencies of the class."
            - **instantiated_by** (`str`): "A string describing the entities or components that instantiate this class."
    *   **Methods:**

    #### Class: `schemas.types.ClassDescription`
    *   **Summary:** "The ClassDescription class is a Pydantic model designed to encapsulate a comprehensive analysis of a Python class. It holds information about the class's overall purpose, its constructor details, a list of its methods along with their descriptions, and contextual usage information."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes a new instance of the ClassDescription class with specified attributes for overall purpose, constructor description, methods analysis, and usage context."
        *   *Parameters:*
            - **overall** (`str`): "A string describing the overall purpose and functionality of the class being analyzed."
            - **init_method** (`ConstructorDescription`): "An instance of ConstructorDescription that details the initialization process and parameters of the class."
            - **methods** (`List[FunctionAnalysis]`): "A list of FunctionAnalysis objects, each representing a detailed breakdown of a method within the class."
            - **usage_context** (`ClassContext`): "An instance of ClassContext providing information on how the class is used and its dependencies."
    *   **Methods:**

    #### Class: `schemas.types.ClassAnalysis`
    *   **Summary:** "The ClassAnalysis class serves as the primary data model for representing the complete JSON schema of a class. It encapsulates essential information about a class including its identifier, a detailed description, and an optional error message. This class is designed to provide a standardized structure for documenting class metadata and associated descriptions."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes a new instance of the ClassAnalysis class with required fields for the identifier and description, and an optional error field."
        *   *Parameters:*
            - **identifier** (`str`): "A string identifier for the class being analyzed."
            - **description** (`ClassDescription`): "An instance of ClassDescription containing detailed information about the class."
            - **error** (`Optional[str]`): "An optional string field to store any error messages related to the class analysis."
    *   **Methods:**

    #### Class: `schemas.types.CallInfo`
    *   **Summary:** "The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure for documenting call relationships within the system."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** None identified for this class.
    *   **Constructor:**
        *   *Description:* "Initializes a CallInfo instance with file, function, mode, and line attributes to represent a call event."
        *   *Parameters:*
            - **file** (`str`): "The file path where the call occurred."
            - **function** (`str`): "The name of the function that made the call."
            - **mode** (`str`): "The mode of the call, such as 'method', 'function', or 'module'."
            - **line** (`int`): "The line number in the file where the call occurred."
    *   **Methods:**

    #### Class: `schemas.types.FunctionContextInput`
    *   **Summary:** "The FunctionContextInput class is a Pydantic model designed to structure contextual information for analyzing a function. It encapsulates two key pieces of information: a list of function names that the analyzed function calls, and a list of CallInfo objects indicating which functions call the analyzed function. This class serves as a data container to facilitate function analysis and dependency tracking within a codebase."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes the FunctionContextInput instance with two attributes: 'calls', a list of strings representing function names called by the analyzed function, and 'called_by', a list of CallInfo objects representing functions that call the analyzed function."
        *   *Parameters:*
            - **calls** (`List[str]`): "A list of strings representing the names of functions called by the analyzed function."
            - **called_by** (`List[CallInfo]`): "A list of CallInfo objects representing the functions that call the analyzed function."
    *   **Methods:**

    #### Class: `schemas.types.FunctionAnalysisInput`
    *   **Summary:** "The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates essential metadata and contextual information required for function analysis, including the mode of operation, identifier, source code, imports, and associated context."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** Standard typing and pydantic components.
    *   **Constructor:**
        *   *Description:* "Initializes a FunctionAnalysisInput instance with fields for mode, identifier, source code, imports, and context. The mode is constrained to the literal value 'function_analysis', ensuring strict adherence to the intended usage pattern."
        *   *Parameters:*
            - **mode** (`Literal["function_analysis"]`): "A literal string indicating the mode of operation, constrained to 'function_analysis'."
            - **identifier** (`str`): "A unique identifier for the function being analyzed."
            - **source_code** (`str`): "The raw source code of the function to be analyzed."
            - **imports** (`List[str]`): "A list of import statements used in the function's source code."
            - **context** (`FunctionContextInput`): "Additional contextual information required for the function analysis."
    *   **Methods:**

    #### Class: `schemas.types.MethodContextInput`
    *   **Summary:** "The MethodContextInput class is a Pydantic model designed to structure contextual information about a method within a class. It encapsulates details such as the method's identifier, the methods it calls, the methods that call it, its arguments, and its docstring. This class serves as a standardized way to represent and exchange method-level metadata in a system."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "The class is initialized with a set of predefined attributes including identifier, calls, called_by, args, and docstring. These attributes are typed using Pydantic's type hints and optional types to enforce data integrity."
        *   *Parameters:*
            - **identifier** (`str`): "A string identifier for the method."
            - **calls** (`List[str]`): "A list of strings representing the identifiers of methods called by this method."
            - **called_by** (`List[CallInfo]`): "A list of CallInfo objects representing the methods that call this method."
            - **args** (`List[str]`): "A list of strings representing the argument names of the method."
            - **docstring** (`Optional[str]`): "An optional string containing the docstring of the method."
    *   **Methods:**

    #### Class: `schemas.types.ClassContextInput`
    *   **Summary:** "The ClassContextInput class is a Pydantic model designed to encapsulate structured context information for analyzing a class. It holds three key pieces of information: a list of dependencies, a list of call information for where the class is instantiated, and a list of method context inputs for each method within the class."
    *   **Instantiation:** `HelperLLM.py`, `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "The constructor initializes the ClassContextInput instance with three attributes: dependencies, instantiated_by, and method_context. These attributes are intended to store contextual metadata about a class being analyzed."
        *   *Parameters:*
            - **dependencies** (`List[str]`): "A list of strings representing the dependencies of the class."
            - **instantiated_by** (`List[CallInfo]`): "A list of CallInfo objects indicating where the class is instantiated."
            - **method_context** (`List[MethodContextInput]`): "A list of MethodContextInput objects describing the context for each method in the class."
    *   **Methods:**

    #### Class: `schemas.types.ClassAnalysisInput`
    *   **Summary:** "The ClassAnalysisInput class serves as a structured input model for generating ClassAnalysis objects. It encapsulates all necessary information required for analyzing a Python class, including its source code, import statements, and contextual metadata such as instantiation details and dependencies."
    *   **Instantiation:** `HelperLLM.py`, `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** Standard typing and pydantic components.
    *   **Constructor:**
        *   *Description:* "Initializes the ClassAnalysisInput instance with fields representing the mode of analysis, the identifier of the class being analyzed, the source code of the class, a list of import statements, and contextual information about how the class is used."
        *   *Parameters:*
            - **mode** (`Literal["class_analysis"]`): "A literal string indicating the mode of analysis, specifically set to 'class_analysis'."
            - **identifier** (`str`): "A string identifier for the class being analyzed."
            - **source_code** (`str`): "The raw source code of the class being analyzed."
            - **imports** (`List[str]`): "A list of import statements associated with the class."
            - **context** (`ClassContextInput`): "An object containing contextual information about the class, such as dependencies and instantiation locations."
    *   **Methods:**

    ### File: `backend/relationship_analyzer.py`

    #### Function: `path_to_module`
    *   **Signature:** `def path_to_module(filepath, project_root)`
    *   **Description:** "The function converts a file path into a Python module path by computing the relative path from the project root, removing the '.py' extension if present, and replacing directory separators with dots. It handles cases where the filepath is not under the project root by falling back to the basename of the file. If the resulting path ends with '__init__', it removes the trailing part to correctly represent the package structure."
    *   **Parameters:**
        - **filepath** (`str`): "The absolute or relative path to a Python file."
        - **project_root** (`str`): "The root directory of the project used to compute the relative path."
    *   **Returns:**
        - **module_path** (`str`): "A dot-separated module path derived from the given file path."
    *   **Usage:** Called by `_collect_definitions` and `__init__` methods in `relationship_analyzer.py`.

    #### Class: `ProjectAnalyzer`
    *   **Summary:** "The ProjectAnalyzer class is designed to analyze Python projects by identifying definitions (functions, classes, methods) and tracking their call relationships across files. It walks through a project directory, parses Python files into Abstract Syntax Trees (ASTs), collects definitions with their metadata, resolves inter-file function calls, and formats the results for further use. The analyzer ignores common directories like .git, venv, and node_modules."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** `ast`, `os`, `logging`, `collections.defaultdict`
    *   **Constructor:**
        *   *Description:* "Initializes the ProjectAnalyzer with a project root directory. Sets up internal data structures including dictionaries for storing definitions, call graphs, and ASTs, as well as a set of directories to ignore during traversal."
        *   *Parameters:*
            - **project_root** (`str`): "The root directory path of the Python project to be analyzed."
    *   **Methods:**
        *   **`analyze`**
            *   *Signature:* `def analyze(self)`
            *   *Description:* "The main analysis method that orchestrates the process of finding Python files, collecting definitions from those files, resolving inter-file calls, and formatting the final results. It clears the stored ASTs after processing to free memory."
            *   *Parameters:*
            *   *Returns:*
                - **output_list** (`list`): "A list of dictionaries containing formatted information about definitions and their callers."
            *   **Usage:** "This method is called by functions evaluation in HelperLLM_evaluation.py at line 120, prepare_shared_input in MainLLM_evaluation.py at line 137, and main_workflow in main.py at line 178."
        *   **`_find_py_files`**
            *   *Signature:* `def _find_py_files(self)`
            *   *Description:* "Recursively finds all Python (.py) files in the project root directory, excluding specified ignored directories such as .git, venv, etc. Returns a list of absolute paths to these files."
            *   *Parameters:*
            *   *Returns:*
                - **py_files** (`list`): List of absolute file paths ending in .py within the project root.
            *   **Usage:** Called by the `analyze` method.
        *   **`_collect_definitions`**
            *   *Signature:* `def _collect_definitions(self, filepath)`
            *   *Description:* "Parses a given Python file into an AST and extracts function and class definitions along with their metadata (file location, line number). It distinguishes between top-level functions and methods inside classes and stores this information in a dictionary indexed by fully qualified names."
            *   *Parameters:*
                - **filepath** (`str`): "The absolute path to the Python file to parse and extract definitions from."
            *   *Returns:*
            *   **Usage:** Called by the `analyze` method.
        *   **`_get_parent`**
            *   *Signature:* `def _get_parent(self, tree, node)`
            *   *Description:* "Given an AST node and a tree, this helper method attempts to find the parent node of the given node by walking the AST. It is used to determine whether a function definition is inside a class."
            *   *Parameters:*
                - **tree** (`ast.AST`): "The full AST of the file being processed."
                - **node** (`ast.AST`): "The AST node whose parent needs to be found."
            *   *Returns:*
                - **parent** (`ast.AST or None`): "The parent AST node of the given node, or None if not found."
            *   **Usage:** Called by the `_collect_definitions` method.
        *   **`_resolve_calls`**
            *   *Signature:* `def _resolve_calls(self, filepath)`
            *   *Description:* "Resolves function calls within a given Python file by using a CallResolverVisitor. It updates the global call graph with the resolved calls, associating caller information with callee identifiers."
            *   *Parameters:*
                - **filepath** (`str`): "The absolute path to the Python file to resolve calls in."
            *   *Returns:*
            *   **Usage:** Called by the `analyze` method.
        *   **`get_formatted_results`**
            *   *Signature:* `def get_formatted_results(self)`
            *   *Description:* "Formats the collected definitions and call relationships into a structured list of dictionaries. Each dictionary contains details about a definition and the list of callers who invoked it, including file, line number, and caller type."
            *   *Parameters:*
            *   *Returns:*
                - **output_list** (`list`): "A list of dictionaries representing definitions and their callers with formatted metadata."
            *   **Usage:** Called by the `analyze` method.

    #### Class: `CallResolverVisitor`
    *   **Summary:** "The CallResolverVisitor class is an AST (Abstract Syntax Tree) visitor designed to analyze Python code and resolve call relationships between functions and methods. It tracks the current execution context (such as class or function scope) and records calls made within the code, associating them with their respective callers. It also handles import resolution and maintains mappings of variable types to aid in resolving qualified names during call analysis."
    *   **Instantiation:** `_resolve_calls`
    *   **Dependencies:** `ast`, `os`, `collections.defaultdict`
    *   **Constructor:**
        *   *Description:* "Initializes the CallResolverVisitor with the file path, project root, and a set of definitions. It sets up internal tracking structures such as scope, instance types, and call records, and determines the module path based on the file path and project root."
        *   *Parameters:*
            - **filepath** (`str`): "The absolute path to the Python file being analyzed."
            - **project_root** (`str`): "The root directory of the project, used to compute relative module paths."
            - **definitions** (`dict`): "A dictionary containing known definitions (functions, classes, etc.) and their associated metadata."
    *   **Methods:**
        *   **`visit_ClassDef`**
            *   *Signature:* `def visit_ClassDef(self, node)`
            *   *Description:* Handles the visitation of class definitions in the AST. It temporarily updates the current class name in the context before visiting child nodes and restores the previous class name afterward.
            *   *Parameters:*
                - **node** (`ast.ClassDef`): "The AST node representing a class definition."
            *   *Returns:*
            *   **Usage:** Invoked by the AST visitor framework when encountering a class definition node.
        *   **`visit_FunctionDef`**
            *   *Signature:* `def visit_FunctionDef(self, node)`
            *   *Description:* Handles the visitation of function definitions in the AST. It temporarily updates the current caller name to the function name before visiting child nodes and restores the previous caller name afterward.
            *   *Parameters:*
                - **node** (`ast.FunctionDef`): "The AST node representing a function definition."
            *   *Returns:*
            *   **Usage:** Invoked by the AST visitor framework when encountering a function definition node.
        *   **`visit_Call`**
            *   *Signature:* `def visit_Call(self, node)`
            *   *Description:* "Processes function or method calls in the AST. It resolves the qualified name of the called function and records the call along with caller information if the function is defined in the provided definitions."
            *   *Parameters:*
                - **node** (`ast.Call`): "The AST node representing a function or method call."
            *   *Returns:*
            *   **Usage:** Calls the private helper method `_resolve_call_qname` to determine the qualified name of the function being called.
        *   **`visit_Import`**
            *   *Signature:* `def visit_Import(self, node)`
            *   *Description:* "Handles import statements in the AST. It adds imported names to the current scope mapping, allowing for later resolution of qualified names."
            *   *Parameters:*
                - **node** (`ast.Import`): "The AST node representing an import statement."
            *   *Returns:*
            *   **Usage:** Invoked by the AST visitor framework when encountering an import node.
        *   **`visit_ImportFrom`**
            *   *Signature:* `def visit_ImportFrom(self, node)`
            *   *Description:* Handles 'from ... import ...' statements in the AST. It resolves the full module path and maps imported names to their qualified names in the current scope.
            *   *Parameters:*
                - **node** (`ast.ImportFrom`): "The AST node representing a 'from ... import ...' statement."
            *   *Returns:*
            *   **Usage:** Invoked by the AST visitor framework when encountering an 'import from' node.
        *   **`visit_Assign`**
            *   *Signature:* `def visit_Assign(self, node)`
            *   *Description:* "Handles assignment statements in the AST. Specifically, it identifies assignments to instances of classes and records the type of the assigned instance for future use in call resolution."
            *   *Parameters:*
                - **node** (`ast.Assign`): "The AST node representing an assignment statement."
            *   *Returns:*
            *   **Usage:** Invoked by the AST visitor framework when encountering an assignment node.
        *   **`_resolve_call_qname`**
            *   *Signature:* `def _resolve_call_qname(self, func_node)`
            *   *Description:* "Resolves the qualified name of a function call based on the AST node representing the function. It checks the scope, local module path, and instance types to determine the fully qualified name of the function."
            *   *Parameters:*
                - **func_node** (`ast.expr`): "The AST node representing the function being called."
            *   *Returns:*
                - **resolved_name** (`str or None`): "The fully qualified name of the function if resolved, otherwise None."
            *   **Usage:** Called by the `visit_Call` method to resolve the qualified name of a function call.

    #### Class: `schemas.types.CallInfo`
    *   **Summary:** "The CallInfo class represents a specific call event from the relationship analyzer, used to track information about function calls including the file, function name, call mode, and line number. It serves as a data structure for documenting call relationships within the system."
    *   **Instantiation:** Not instantiated by any other components.
    *   **Dependencies:** None identified for this class.
    *   **Constructor:**
        *   *Description:* "Initializes a CallInfo instance with file, function, mode, and line attributes to represent a call event."
        *   *Parameters:*
            - **file** (`str`): "The file path where the call occurred."
            - **function** (`str`): "The name of the function that made the call."
            - **mode** (`str`): "The mode of the call, such as 'method', 'function', or 'module'."
            - **line** (`int`): "The line number in the file where the call occurred."
    *   **Methods:**

    #### Class: `schemas.types.FunctionContextInput`
    *   **Summary:** "The FunctionContextInput class is a Pydantic model designed to structure contextual information for analyzing a function. It encapsulates two key pieces of information: a list of function names that the analyzed function calls, and a list of CallInfo objects indicating which functions call the analyzed function. This class serves as a data container to facilitate function analysis and dependency tracking within a codebase."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "Initializes the FunctionContextInput instance with two attributes: 'calls', a list of strings representing function names called by the analyzed function, and 'called_by', a list of CallInfo objects representing functions that call the analyzed function."
        *   *Parameters:*
            - **calls** (`List[str]`): "A list of strings representing the names of functions called by the analyzed function."
            - **called_by** (`List[CallInfo]`): "A list of CallInfo objects representing the functions that call the analyzed function."
    *   **Methods:**

    #### Class: `schemas.types.FunctionAnalysisInput`
    *   **Summary:** "The FunctionAnalysisInput class serves as a structured input model for generating FunctionAnalysis objects. It encapsulates essential metadata and contextual information required for function analysis, including the mode of operation, identifier, source code, imports, and associated context."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** Standard typing and pydantic components.
    *   **Constructor:**
        *   *Description:* "Initializes a FunctionAnalysisInput instance with fields for mode, identifier, source code, imports, and context. The mode is constrained to the literal value 'function_analysis', ensuring strict adherence to the intended usage pattern."
        *   *Parameters:*
            - **mode** (`Literal["function_analysis"]`): "A literal string indicating the mode of operation, constrained to 'function_analysis'."
            - **identifier** (`str`): "A unique identifier for the function being analyzed."
            - **source_code** (`str`): "The raw source code of the function to be analyzed."
            - **imports** (`List[str]`): "A list of import statements used in the function's source code."
            - **context** (`FunctionContextInput`): "Additional contextual information required for the function analysis."
    *   **Methods:**

    #### Class: `schemas.types.MethodContextInput`
    *   **Summary:** "The MethodContextInput class is a Pydantic model designed to structure contextual information about a method within a class. It encapsulates details such as the method's identifier, the methods it calls, the methods that call it, its arguments, and its docstring. This class serves as a standardized way to represent and exchange method-level metadata in a system."
    *   **Instantiation:** `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "The class is initialized with a set of predefined attributes including identifier, calls, called_by, args, and docstring. These attributes are typed using Pydantic's type hints and optional types to enforce data integrity."
        *   *Parameters:*
            - **identifier** (`str`): "A string identifier for the method."
            - **calls** (`List[str]`): "A list of strings representing the identifiers of methods called by this method."
            - **called_by** (`List[CallInfo]`): "A list of CallInfo objects representing the methods that call this method."
            - **args** (`List[str]`): "A list of strings representing the argument names of the method."
            - **docstring** (`Optional[str]`): "An optional string containing the docstring of the method."
    *   **Methods:**

    #### Class: `schemas.types.ClassContextInput`
    *   **Summary:** "The ClassContextInput class is a Pydantic model designed to encapsulate structured context information for analyzing a class. It holds three key pieces of information: a list of dependencies, a list of call information for where the class is instantiated, and a list of method context inputs for each method within the class."
    *   **Instantiation:** `HelperLLM.py`, `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** None beyond file imports.
    *   **Constructor:**
        *   *Description:* "The constructor initializes the ClassContextInput instance with three attributes: dependencies, instantiated_by, and method_context. These attributes are intended to store contextual metadata about a class being analyzed."
        *   *Parameters:*
            - **dependencies** (`List[str]`): "A list of strings representing the dependencies of the class."
            - **instantiated_by** (`List[CallInfo]`): "A list of CallInfo objects indicating where the class is instantiated."
            - **method_context** (`List[MethodContextInput]`): "A list of MethodContextInput objects describing the context for each method in the class."
    *   **Methods:**

    #### Class: `schemas.types.ClassAnalysisInput`
    *   **Summary:** "The ClassAnalysisInput class serves as a structured input model for generating ClassAnalysis objects. It encapsulates all necessary information required for analyzing a Python class, including its source code, import statements, and contextual metadata such as instantiation details and dependencies."
    *   **Instantiation:** `HelperLLM.py`, `HelperLLM_evaluation.py`, `MainLLM_evaluation.py`, `main.py`
    *   **Dependencies:** Standard typing and pydantic components.
    *   **Constructor:**
        *   *Description:* "Initializes the ClassAnalysisInput instance with fields representing the mode of analysis, the identifier of the class being analyzed, the source code of the class, a list of import statements, and contextual information about how the class is used."
        *   *Parameters:*
            - **mode** (`Literal["class_analysis"]`): "A literal string indicating the mode of analysis, specifically set to 'class_analysis'."
            - **identifier** (`str`): "A string identifier for the class being analyzed."
            - **source_code** (`str`): "The raw source code of the class being analyzed."
            - **imports** (`List[str]`): "A list of import statements associated with the class."
            - **context** (`ClassContextInput`): "An object containing contextual information about the class, such as dependencies and instantiation locations."
    *   **Methods:**

---