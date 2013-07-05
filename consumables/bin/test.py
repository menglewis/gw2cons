from django.conf import settings

settings.configure()
settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cons.db',                      # Or path to database file if using sqlite3.
    }
}

from ..models import Item

def main():
	i = Item(name="Test", duration=1000, consumable_type="UTIL", slug="Test")
	i.save()

if __name__ == "__main__":
	main()


