from sphene.community.sphutils import add_setting_defaults



add_setting_defaults( {
    'board_count_views': True,
    'board_heat_days': 30,
    'board_heat_post_threshold': 10,
    'board_heat_view_threshold': 100,
    'board_heat_calculator': 'sphene.sphboard.models.calculate_heat',

    # Defines if the 'Notify Me' checkbox should be selected by default.
    'board_default_notifyme': True,

    # How long a user is allowed to edit his post in seconds.
    # -1: forever,
    # 0: never
    'board_edit_timeout': -1, #30 * 60,

    # Timeout for the rendered body in the cache
    # Default 6 hours
    'board_body_cache_timeout': 6 * 3600,
    'board_signature_cache_timeout': 6 * 3600,
    'board_authorinfo_cache_timeout': 6 * 3600,

    # See http://code.djangoproject.com/ticket/4789
    # When activating this setting, select_related() will not be used.
    'workaround_select_related_bug': False,


    'board_post_paging': 10,

    # Allow users to attach files to their posts ?
    'board_allow_attachments': True,

    'board_attachments_upload_to': 'var/sphene/sphwiki/attachment/%Y/%m/%d',
    })
