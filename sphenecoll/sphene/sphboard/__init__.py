from sphene.community.sphutils import add_setting_defaults



add_setting_defaults( {
    'board_count_views': True,
    'board_heat_days': 30,
    'board_heat_post_threshold': 10,
    'board_heat_view_threshold': 100,
    'board_heat_calculator': 'sphene.sphboard.models.calculate_heat',

    # Timeout for the rendered body in the cache
    # Default 6 hours
    'board_body_cache_timeout': 6 * 3600,
    'board_signature_cache_timeout': 6 * 3600,
    'board_authorinfo_cache_timeout': 6 * 3600,

    'workaround_select_related_bug': False,
    })
