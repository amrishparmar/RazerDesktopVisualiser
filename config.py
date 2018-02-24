class AppConfig:
    """Configuration information for the application"""

    TITLE = 'DesktopVisualiser'
    DESCRIPTION = 'An application for visualising the user desktop'
    AUTHOR_NAME = 'Amrish Parmar'
    AUTHOR_CONTACT = 'aparm_dev@outlook.com'
    DEVICE_SUPPORTED = ['keyboard']
    CATEGORY = 'application'

    def to_dict(self):
        """Return a dictionary representation of the JSON required by the Razer SDK"""
        return {
            'title': self.TITLE,
            'description': self.DESCRIPTION,
            'author': {
                'name': self.AUTHOR_NAME,
                'contact': self.AUTHOR_CONTACT,
            },
            'device_supported': self.DEVICE_SUPPORTED,
            'category': 'application',
        }
