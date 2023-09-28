import requests


def get_json_from_api():
    from parsapi.models import CatalogPatrioticMusic
    url = 'https://opendata.mkrf.ru/v2/patriot_music/$?l=100'
    headers = {
        "X-API-KEY": "bf525a9751447849c1f59ec0ba3fe0c357061c924cfc76cc9b87fc696bd2afc8"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    data = data['data']

    for item in data:
        fullname = item['data']['fullname']
        composer = item['data']['composer']
        genre = item['data']['genre']
        theme = item['data']['theme']
        creationyear = item['data'].get('creationyear', ' ')

        catalog_music, created = CatalogPatrioticMusic.objects.get_or_create(
            fullname=fullname,
            defaults={
                'composer': composer,
                'genre': genre,
                'theme': theme,
                'creationyear': creationyear
            }
        )

        if created:
            catalog_music.save()
