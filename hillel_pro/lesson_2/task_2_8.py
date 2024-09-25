def create_user_settings():
    settings = {
        'theme': 'default',  # Default
        'language': 'ua',  # Default
        'notifications': True  # Default
    }

    def manage_setting(key=None, value=None):
        if key in settings and key != None:
            settings[key] = value
            return value

    def user_setting():
        return settings

    return manage_setting, user_setting


user_setting, setting = create_user_settings()

print(user_setting('theme', 'dark'))
print(user_setting('language', 'en'))
print(user_setting('notifications', False))
print(setting())
