# AUTOGENERATED DON'T EDIT
# Please make changes to the code generator             (distutils/ccompiler_opt.py)
hash = 2091074878
data = \
{'cache_infile': False,
 'cache_me': {"('cc_test_flags', ['-O3'])": True,
              "('cc_test_flags', ['-Werror'])": True,
              "('cc_test_flags', ['-Werror-implicit-function-declaration'])": True,
              "('cc_test_flags', ['-march=armv8.2-a+dotprod'])": True,
              "('cc_test_flags', ['-march=armv8.2-a+fp16'])": True,
              "('cc_test_flags', ['-march=armv8.2-a+fp16fml'])": True,
              "('cc_test_flags', ['-march=native'])": False,
              "('feature_extra_checks', 'ASIMD')": [],
              "('feature_extra_checks', 'ASIMDDP')": [],
              "('feature_extra_checks', 'ASIMDHP')": [],
              "('feature_extra_checks', 'NEON')": [],
              "('feature_extra_checks', 'NEON_FP16')": [],
              "('feature_extra_checks', 'NEON_VFPV4')": [],
              "('feature_flags', 'ASIMD')": [],
              "('feature_flags', 'ASIMDDP')": ['-march=armv8.2-a+dotprod'],
              "('feature_flags', 'ASIMDFHM')": ['-march=armv8.2-a+fp16+fp16fml'],
              "('feature_flags', 'ASIMDHP')": ['-march=armv8.2-a+fp16'],
              "('feature_flags', 'NEON')": [],
              "('feature_flags', 'NEON_FP16')": [],
              "('feature_flags', 'NEON_VFPV4')": [],
              "('feature_flags', {'NEON_VFPV4', 'NEON', 'NEON_FP16', 'ASIMD'})": [],
              "('feature_is_supported', 'ASIMD', 'force_flags', 'macros', None, [])": True,
              "('feature_is_supported', 'ASIMDDP', 'force_flags', 'macros', None, [])": True,
              "('feature_is_supported', 'ASIMDFHM', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'ASIMDHP', 'force_flags', 'macros', None, [])": True,
              "('feature_is_supported', 'NEON', 'force_flags', 'macros', None, [])": True,
              "('feature_is_supported', 'NEON_FP16', 'force_flags', 'macros', None, [])": True,
              "('feature_is_supported', 'NEON_VFPV4', 'force_flags', 'macros', None, [])": True,
              "('feature_test', 'ASIMD', None, 'macros', [])": True,
              "('feature_test', 'ASIMDDP', None, 'macros', [])": True,
              "('feature_test', 'ASIMDFHM', None, 'macros', [])": False,
              "('feature_test', 'ASIMDHP', None, 'macros', [])": True,
              "('feature_test', 'NEON', None, 'macros', [])": True,
              "('feature_test', 'NEON_FP16', None, 'macros', [])": True,
              "('feature_test', 'NEON_VFPV4', None, 'macros', [])": True},
 'cache_private': {'sources_status'},
 'cc_flags': {'native': [],
              'opt': ['-O3'],
              'werror': ['-Werror-implicit-function-declaration', '-Werror']},
 'cc_has_debug': True,
 'cc_has_native': False,
 'cc_is_cached': True,
 'cc_is_clang': True,
 'cc_is_gcc': False,
 'cc_is_icc': False,
 'cc_is_iccw': False,
 'cc_is_msvc': False,
 'cc_is_nocc': False,
 'cc_march': 'aarch64',
 'cc_name': 'clang',
 'cc_noopt': False,
 'cc_on_aarch64': True,
 'cc_on_armhf': False,
 'cc_on_noarch': False,
 'cc_on_ppc64': False,
 'cc_on_ppc64le': False,
 'cc_on_x64': False,
 'cc_on_x86': False,
 'feature_is_cached': True,
 'feature_min': {'ASIMD', 'NEON', 'NEON_FP16', 'NEON_VFPV4'},
 'feature_supported': {'ASIMD': {'autovec': True,
                                 'implies': ['NEON', 'NEON_FP16', 'NEON_VFPV4'],
                                 'implies_detect': False,
                                 'interest': 4},
                       'ASIMDDP': {'flags': ['-march=armv8.2-a+dotprod'],
                                   'implies': ['ASIMD'],
                                   'interest': 6},
                       'ASIMDFHM': {'flags': ['-march=armv8.2-a+fp16fml'],
                                    'implies': ['ASIMDHP'],
                                    'interest': 7},
                       'ASIMDHP': {'flags': ['-march=armv8.2-a+fp16'],
                                   'implies': ['ASIMD'],
                                   'interest': 5},
                       'NEON': {'autovec': True,
                                'headers': ['arm_neon.h'],
                                'implies': ['NEON_FP16', 'NEON_VFPV4', 'ASIMD'],
                                'interest': 1},
                       'NEON_FP16': {'autovec': True,
                                     'implies': ['NEON', 'NEON_VFPV4', 'ASIMD'],
                                     'interest': 2},
                       'NEON_VFPV4': {'autovec': True,
                                      'implies': ['NEON', 'NEON_FP16', 'ASIMD'],
                                      'interest': 3}},
 'hit_cache': False,
 'parse_baseline_flags': [],
 'parse_baseline_names': ['NEON', 'NEON_FP16', 'NEON_VFPV4', 'ASIMD'],
 'parse_dispatch_names': ['ASIMDHP', 'ASIMDDP'],
 'parse_is_cached': True,
 'parse_target_groups': {'SIMD_TEST': (True, [], [])},
 'sources_status': {}}