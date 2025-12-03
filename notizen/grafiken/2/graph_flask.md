```mermaid
graph LR
n0["views::MethodView::__init_subclass__"]
n1["auth::load_logged_in_user"]
n2["db::get_db"]
n3["auth::register"]
n4["auth::login"]
n5["blog::index"]
n6["blog::get_post"]
n7["blog::create"]
n8["blog::update"]
n9["blog::delete"]
n10["db::init_db"]
n11["db::init_db_command"]
n12["test_auth::test_register"]
n13["test_blog::test_author_required"]
n14["test_blog::test_create"]
n15["test_blog::test_update"]
n16["test_blog::test_delete"]
n17["test_db::test_get_close_db"]
n18["blueprints::BlueprintSetupState::add_url_rule"]
n19["scaffold::_endpoint_from_view_func"]
n20["blueprints::Blueprint::__init__"]
n21["blueprints::Blueprint::record_once"]
n22["blueprints::Blueprint::record"]
n23["blueprints::Blueprint::register"]
n24["blueprints::Blueprint::make_setup_state"]
n25["blueprints::Blueprint::extend"]
n26["blueprints::Blueprint::_merge_blueprint_funcs"]
n27["blueprints::Blueprint::add_url_rule"]
n28["blueprints::Blueprint::decorator"]
n29["blueprints::Blueprint::add_app_template_filter"]
n30["blueprints::Blueprint::add_app_template_test"]
n31["blueprints::Blueprint::add_app_template_global"]
n32["blueprints::Blueprint::before_app_request"]
n33["blueprints::Blueprint::after_app_request"]
n34["blueprints::Blueprint::teardown_app_request"]
n35["blueprints::Blueprint::app_context_processor"]
n36["blueprints::Blueprint::app_url_value_preprocessor"]
n37["blueprints::Blueprint::app_url_defaults"]
n38["cli::find_best_app"]
n39["cli::_called_with_wrong_args"]
n40["cli::find_app_by_string"]
n41["cli::locate_app"]
n42["cli::ScriptInfo::__init__"]
n43["helpers::get_load_dotenv"]
n44["cli::ScriptInfo::load_app"]
n45["helpers::get_debug_flag"]
n46["cli::prepare_import"]
n47["cli::decorator"]
n48["cli::AppGroup::decorator"]
n49["cli::with_appcontext"]
n50["cli::AppGroup::command"]
n51["cli::AppGroup::group"]
n52["cli::_env_file_callback"]
n53["cli::load_dotenv"]
n54["cli::FlaskGroup::__init__"]
n55["cli::FlaskGroup::get_command"]
n56["cli::FlaskGroup::_load_plugin_commands"]
n57["cli::FlaskGroup::list_commands"]
n58["cli::FlaskGroup::make_context"]
n59["cli::FlaskGroup::parse_args"]
n60["cli::run_command"]
n61["cli::show_server_banner"]
n62["cli::shell_command"]
n63["cli::routes_command"]
n64["cli::main"]
n65["config::Config::__init__"]
n66["config::Config::__repr__"]
n67["ctx::_AppCtxGlobals::get"]
n68["ctx::_AppCtxGlobals::pop"]
n69["ctx::_AppCtxGlobals::setdefault"]
n70["ctx::_AppCtxGlobals::__repr__"]
n71["ctx::after_this_request"]
n72["ctx::copy_current_request_context"]
n73["ctx::has_request_context"]
n74["ctx::has_app_context"]
n75["ctx::AppContext::push"]
n76["ctx::AppContext::match_request"]
n77["ctx::AppContext::pop"]
n78["ctx::AppContext::__enter__"]
n79["ctx::AppContext::__exit__"]
n80["debughelpers::FormDataRoutingRedirect::__init__"]
n81["debughelpers::newcls::__getitem__"]
n82["debughelpers::explain_template_loading_attempts"]
n83["debughelpers::_dump_loader_info"]
n84["helpers::stream_with_context"]
n85["helpers::generator"]
n86["helpers::decorator"]
n87["helpers::make_response"]
n88["helpers::url_for"]
n89["helpers::redirect"]
n90["helpers::send_file"]
n91["helpers::_prepare_send_file_kwargs"]
n92["helpers::send_from_directory"]
n93["helpers::_split_blueprint_path"]
n94["provider::JSONProvider::dump"]
n95["provider::JSONProvider::dumps"]
n96["provider::JSONProvider::load"]
n97["provider::JSONProvider::loads"]
n98["provider::JSONProvider::response"]
n99["provider::JSONProvider::_prepare_response_obj"]
n100["provider::DefaultJSONProvider::dumps"]
n101["provider::DefaultJSONProvider::loads"]
n102["provider::DefaultJSONProvider::response"]
n103["tag::JSONTag::tag"]
n104["tag::JSONTag::to_json"]
n105["tag::TagDict::to_json"]
n106["tag::PassDict::to_json"]
n107["tag::TagTuple::to_json"]
n108["tag::PassList::to_json"]
n109["tag::TaggedJSONSerializer::tag"]
n110["tag::TagDateTime::check"]
n111["tag::TaggedJSONSerializer::untag"]
n112["tag::TagDateTime::to_python"]
n113["tag::TaggedJSONSerializer::_untag_scan"]
n114["tag::TaggedJSONSerializer::dumps"]
n115["tag::TaggedJSONSerializer::loads"]
n116["logging::create_logger"]
n117["logging::has_level_handler"]
n118["scaffold::Scaffold::__init__"]
n119["helpers::get_root_path"]
n120["scaffold::Scaffold::get"]
n121["scaffold::Scaffold::_method_route"]
n122["scaffold::Scaffold::post"]
n123["scaffold::Scaffold::put"]
n124["scaffold::Scaffold::delete"]
n125["scaffold::Scaffold::patch"]
n126["scaffold::find_package"]
n127["scaffold::_find_package_path"]
n128["sessions::SecureCookieSession::__init__"]
n129["sessions::SecureCookieSession::__getitem__"]
n130["sessions::SecureCookieSession::get"]
n131["sessions::SecureCookieSession::setdefault"]
n132["sessions::SecureCookieSessionInterface::open_session"]
n133["sessions::SecureCookieSessionInterface::get_signing_serializer"]
n134["sessions::SessionInterface::get_cookie_name"]
n135["sessions::SecureCookieSessionInterface::save_session"]
n136["sessions::SessionInterface::should_set_cookie"]
n137["sessions::SessionInterface::get_cookie_httponly"]
n138["sessions::SessionInterface::get_cookie_partitioned"]
n139["sessions::SessionInterface::get_expiration_time"]
n140["sessions::SessionInterface::get_cookie_secure"]
n141["sessions::SessionInterface::get_cookie_samesite"]
n142["sessions::SessionInterface::get_cookie_path"]
n143["sessions::SessionInterface::get_cookie_domain"]
n144["templating::Environment::__init__"]
n145["templating::DispatchingJinjaLoader::_get_source_explained"]
n146["templating::DispatchingJinjaLoader::get_source"]
n147["templating::DispatchingJinjaLoader::_get_source_fast"]
n148["templating::DispatchingJinjaLoader::list_templates"]
n149["templating::render_template"]
n150["templating::_render"]
n151["templating::render_template_string"]
n152["templating::_stream"]
n153["templating::generate"]
n154["templating::stream_template"]
n155["templating::stream_template_string"]
n156["testing::EnvironBuilder::__init__"]
n157["testing::FlaskClient::__init__"]
n158["testing::_get_werkzeug_version"]
n159["testing::FlaskClient::_request_from_builder_args"]
n160["testing::FlaskClient::_copy_environ"]
n161["testing::FlaskClient::open"]
n162["testing::FlaskCliRunner::__init__"]
n163["testing::FlaskCliRunner::invoke"]
n164["wrappers::Request::blueprints"]
n165["wrappers::Request::_load_form_data"]
n166["debughelpers::attach_enctype_error_multidict"]
n167["wrappers::Request::on_json_loading_failed"]
n168["test_async::test_async_route"]
n169["test_async::AsyncMethodView::post"]
n170["test_async::AsyncMethodView::get"]
n171["test_async::test_async_error_handler"]
n172["test_async::test_async_before_after_request"]
n173["test_basic::get"]
n174["test_basic::test_session"]
n175["test_basic::test_session_path"]
n176["test_basic::test_session_using_application_root"]
n177["test_basic::test_session_using_session_settings"]
n178["test_basic::clear"]
n179["test_basic::test_session_using_samesite_attribute"]
n180["test_basic::test_missing_session"]
n181["test_basic::expect_exception"]
n182["test_basic::get_session"]
n183["test_basic::test_session_secret_key_fallbacks"]
n184["test_basic::test_session_expiration"]
n185["test_basic::dump_session_contents"]
n186["test_basic::test_session_stored_last"]
n187["test_basic::test_session_special_types"]
n188["test_basic::bump"]
n189["test_basic::read"]
n190["test_basic::run_test"]
n191["test_basic::test_session_cookie_setting"]
n192["test_basic::setdefault"]
n193["test_basic::expect"]
n194["test_basic::test_session_vary_cookie"]
n195["test_basic::login"]
n196["test_basic::ignored"]
n197["test_basic::test_session_refresh_vary"]
n198["test_basic::test_extended_flashing"]
n199["test_basic::test_request_processing"]
n200["test_basic::test_request_preprocessing_early_return"]
n201["test_basic::test_after_request_processing"]
n202["test_basic::test_teardown_request_handler"]
n203["test_basic::test_teardown_request_handler_debug_mode"]
n204["test_basic::test_teardown_request_handler_error"]
n205["test_basic::test_before_after_request_order"]
n206["test_basic::test_error_handling"]
n207["test_basic::test_error_handling_processing"]
n208["test_basic::test_baseexception_error_handling"]
n209["test_basic::test_before_request_and_routing_errors"]
n210["test_basic::test_user_error_handling"]
n211["test_basic::test_http_error_subclass_handling"]
n212["test_basic::test_errorhandler_precedence"]
n213["test_basic::test_trap_bad_request_key_error"]
n214["test_basic::test_trapping_of_all_http_exceptions"]
n215["test_basic::test_error_handler_after_processor_error"]
n216["test_basic::test_response_types"]
n217["test_basic::test_response_type_errors"]
n218["test_basic::test_static_files"]
n219["test_basic::test_static_url_path"]
n220["test_basic::test_static_url_path_with_ending_slash"]
n221["test_basic::test_static_folder_with_ending_slash"]
n222["test_basic::test_static_route_with_host_matching"]
n223["test_basic::test_server_name_matching"]
n224["test_basic::test_server_name_subdomain"]
n225["test_basic::test_exception_propagation"]
n226["test_basic::run_simple_mock"]
n227["test_basic::add_language_code"]
n228["test_basic::test_url_processors"]
n229["test_basic::test_nonascii_pathinfo"]
n230["test_basic::test_no_setup_after_first_request"]
n231["test_basic::test_route_decorator_custom_endpoint"]
n232["test_basic::test_get_method_on_g"]
n233["test_basic::test_subdomain_basic_support"]
n234["test_basic::test_subdomain_matching"]
n235["test_basic::test_subdomain_matching_with_ports"]
n236["test_basic::test_subdomain_matching_other_name"]
n237["test_basic::test_max_cookie_size"]
n238["test_blueprints::bp_page"]
n239["test_blueprints::template_string"]
n240["test_blueprints::app_page"]
n241["test_cli::test_find_best_app"]
n242["test_cli::test_prepare_import"]
n243["test_cli::test_locate_app"]
n244["test_cli::test_locate_app_raises"]
n245["test_cli::test_locate_app_suppress_raise"]
n246["test_cli::test_get_version"]
n247["cli::get_version"]
n248["test_cli::TestRoutes::test_simple"]
n249["test_cli::TestRoutes::invoke"]
n250["test_cli::TestRoutes::expect_order"]
n251["test_cli::TestRoutes::test_sort"]
n252["test_cli::TestRoutes::test_all_methods"]
n253["test_cli::TestRoutes::test_no_routes"]
n254["test_cli::TestRoutes::test_subdomain"]
n255["test_cli::TestRoutes::test_host"]
n256["test_cli::test_load_dotenv"]
n257["test_cli::test_dotenv_path"]
n258["test_cli::test_dotenv_optional"]
n259["test_cli::test_disable_dotenv_from_env"]
n260["test_cli::test_cli_blueprints"]
n261["test_cli::test_cli_empty"]
n262["test_config::test_config_from_pyfile"]
n263["test_config::common_object_test"]
n264["test_config::test_config_from_object"]
n265["test_config::test_config_from_file_json"]
n266["test_config::test_config_from_file_toml"]
n267["test_config::test_config_from_mapping"]
n268["test_config::test_config_from_class"]
n269["test_config::test_config_from_envvar"]
n270["test_config::test_custom_config_class"]
n271["test_helpers::test_redirect_with_app"]
n272["test_helpers::redirect"]
n273["test_helpers::TestStreaming::index"]
n274["test_helpers::TestStreaming::generate"]
n275["test_helpers::TestStreaming::gen"]
n276["test_helpers::TestStreaming::test_streaming_with_context"]
n277["test_helpers::MyView::get"]
n278["test_helpers::TestStreaming::test_streaming_with_context_as_decorator"]
n279["test_helpers::TestStreaming::test_streaming_with_context_and_custom_close"]
n280["test_helpers::TestStreaming::test_stream_keeps_session"]
n281["test_helpers::TestStreaming::test_async_view"]
n282["test_helpers::Wrapper::close"]
n283["test_helpers::TestHelpers::test_get_debug_flag"]
n284["test_instance_config::test_uninstalled_namespace_paths"]
n285["test_instance_config::create_namespace"]
n286["test_json::default"]
n287["test_json::CustomProvider::loads"]
n288["test_logging::test_has_level_handler"]
n289["test_reqctx::test_context_binding"]
n290["test_reqctx::index"]
n291["test_reqctx::meh"]
n292["test_reqctx::test_manual_context_binding"]
n293["test_reqctx::PathAwareSessionInterface::get_cookie_name"]
n294["test_reqctx::test_session_dynamic_cookie_name"]
n295["test_reqctx::get"]
n296["test_reqctx::get_dynamic_cookie"]
n297["test_reqctx::test_normal_environ_completes"]
n298["test_testing::hello_command"]
n299["test_testing::echo"]
n300["test_user_error_handler::TestGenericHandlers::handle_500"]
n301["test_user_error_handler::TestGenericHandlers::report_error"]
n302["test_user_error_handler::TestGenericHandlers::handle_exception"]
n303["test_views::test_basic_view"]
n304["test_views::common_test"]
n305["test_views::test_method_based_view"]
n306["test_views::test_view_patching"]
n307["test_views::test_view_decorators"]
n308["test_views::Index::get"]
n309["test_views::test_implicit_head"]
n310["test_views::test_explicit_head"]
n311["test_views::Index::head"]
n312["test_views::test_endpoint_override"]
n313["test_views::test_methods_var_inheritance"]
n314["test_views::ChildView::get"]
n315["test_views::test_multiple_inheritance"]
n316["test_views::DeleteView::delete"]
n317["test_views::GetView::get"]
n318["test_views::test_remove_method_from_parent"]
n319["test_views::OtherView::post"]
n320["test_views::test_init_once"]
n321["typing_route::hello_generator"]
n322["typing_route::show"]
n323["typing_route::return_template"]
n324["typing_route::RenderTemplateView::dispatch_request"]

n0 --> n0
n1 --> n2
n3 --> n2
n4 --> n2
n5 --> n2
n6 --> n2
n7 --> n2
n8 --> n6
n8 --> n2
n9 --> n6
n9 --> n2
n10 --> n2
n11 --> n10
n12 --> n2
n13 --> n2
n14 --> n2
n15 --> n2
n16 --> n2
n17 --> n2
n18 --> n19
n18 --> n18
n20 --> n20
n21 --> n22
n23 --> n24
n23 --> n18
n23 --> n23
n25 --> n25
n26 --> n25
n27 --> n22
n27 --> n27
n28 --> n21
n29 --> n21
n30 --> n21
n31 --> n21
n32 --> n21
n33 --> n21
n34 --> n21
n35 --> n21
n36 --> n21
n37 --> n21
n38 --> n39
n40 --> n39
n41 --> n40
n41 --> n38
n42 --> n43
n44 --> n45
n44 --> n46
n44 --> n41
n47 --> n44
n48 --> n49
n48 --> n50
n51 --> n51
n52 --> n53
n54 --> n54
n55 --> n44
n55 --> n56
n55 --> n55
n57 --> n57
n57 --> n44
n57 --> n56
n58 --> n58
n59 --> n59
n60 --> n50
n60 --> n45
n60 --> n44
n60 --> n61
n62 --> n50
n63 --> n50
n64 --> n64
n65 --> n65
n66 --> n66
n67 --> n67
n68 --> n68
n69 --> n69
n70 --> n67
n70 --> n70
n71 --> n67
n72 --> n67
n73 --> n67
n74 --> n67
n75 --> n76
n77 --> n67
n78 --> n75
n79 --> n77
n80 --> n80
n81 --> n81
n82 --> n83
n84 --> n85
n86 --> n84
n87 --> n87
n88 --> n88
n89 --> n89
n90 --> n90
n90 --> n91
n92 --> n92
n92 --> n91
n93 --> n93
n94 --> n95
n96 --> n97
n98 --> n99
n98 --> n95
n100 --> n100
n101 --> n101
n102 --> n99
n102 --> n100
n103 --> n104
n105 --> n103
n106 --> n103
n107 --> n103
n108 --> n103
n109 --> n109
n109 --> n110
n111 --> n112
n113 --> n113
n113 --> n111
n114 --> n109
n114 --> n114
n115 --> n113
n115 --> n115
n116 --> n117
n118 --> n119
n120 --> n121
n122 --> n121
n123 --> n121
n124 --> n121
n125 --> n121
n126 --> n127
n128 --> n128
n129 --> n129
n130 --> n130
n131 --> n131
n132 --> n133
n132 --> n134
n132 --> n130
n135 --> n136
n135 --> n137
n135 --> n138
n135 --> n139
n135 --> n140
n135 --> n141
n135 --> n134
n135 --> n142
n135 --> n143
n135 --> n133
n144 --> n144
n145 --> n82
n145 --> n146
n147 --> n146
n148 --> n148
n149 --> n150
n151 --> n150
n152 --> n84
n152 --> n153
n153 --> n153
n154 --> n152
n155 --> n152
n156 --> n156
n157 --> n158
n157 --> n157
n159 --> n160
n161 --> n160
n161 --> n159
n161 --> n161
n162 --> n162
n163 --> n163
n164 --> n93
n165 --> n166
n165 --> n165
n167 --> n167
n168 --> n169
n168 --> n170
n171 --> n170
n172 --> n170
n173 --> n173
n174 --> n173
n175 --> n173
n176 --> n173
n177 --> n173
n178 --> n178
n179 --> n173
n180 --> n173
n180 --> n181
n182 --> n173
n183 --> n173
n184 --> n173
n185 --> n173
n186 --> n173
n187 --> n173
n188 --> n173
n189 --> n173
n190 --> n173
n191 --> n190
n192 --> n192
n193 --> n173
n194 --> n193
n195 --> n173
n196 --> n173
n197 --> n173
n198 --> n173
n199 --> n173
n200 --> n173
n201 --> n173
n202 --> n173
n203 --> n173
n204 --> n173
n205 --> n173
n206 --> n173
n207 --> n173
n208 --> n173
n209 --> n173
n210 --> n173
n211 --> n173
n212 --> n173
n213 --> n173
n214 --> n173
n215 --> n173
n216 --> n173
n217 --> n173
n218 --> n173
n219 --> n173
n220 --> n173
n221 --> n173
n222 --> n173
n223 --> n173
n224 --> n173
n225 --> n173
n226 --> n173
n227 --> n192
n228 --> n173
n229 --> n173
n230 --> n173
n231 --> n173
n232 --> n173
n233 --> n173
n234 --> n173
n235 --> n173
n236 --> n173
n237 --> n173
n238 --> n239
n240 --> n239
n241 --> n38
n242 --> n46
n243 --> n41
n244 --> n41
n245 --> n41
n246 --> n247
n248 --> n249
n248 --> n250
n251 --> n249
n251 --> n250
n252 --> n249
n253 --> n249
n254 --> n249
n255 --> n249
n256 --> n53
n257 --> n53
n258 --> n53
n259 --> n249
n260 --> n249
n261 --> n249
n262 --> n263
n264 --> n263
n265 --> n263
n266 --> n263
n267 --> n263
n268 --> n263
n269 --> n263
n270 --> n263
n271 --> n272
n273 --> n274
n273 --> n275
n276 --> n277
n278 --> n277
n279 --> n277
n280 --> n277
n281 --> n277
n281 --> n282
n283 --> n45
n284 --> n285
n286 --> n286
n287 --> n287
n288 --> n117
n289 --> n290
n289 --> n291
n292 --> n290
n293 --> n293
n294 --> n295
n295 --> n295
n296 --> n295
n297 --> n295
n298 --> n299
n300 --> n301
n302 --> n301
n303 --> n304
n305 --> n304
n306 --> n304
n307 --> n308
n309 --> n308
n310 --> n308
n310 --> n311
n312 --> n304
n313 --> n314
n315 --> n316
n315 --> n317
n318 --> n319
n318 --> n317
n320 --> n317
n321 --> n322
n323 --> n149
n324 --> n149
``` 
