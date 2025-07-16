# 📚 MangaCollec API Client

Client Python officiel non affilié pour interagir facilement avec l'API [MangaCollec](https://mangacollec.com), compatible avec les protocoles OAuth2 (`password`, `client_credentials`).

---

## ✨ Fonctionnalités

- 🔐 Authentification OAuth2 (`grant_type=password` ou `client_credentials`)
- 🧾 Appels aux API REST v1 et v2
- 🧱 Client structuré, modulaire et maintenable
- ⚙️ Intégration facile dans tout projet Python
- 🧪 Tests unitaires avec `pytest`
- ✅ Conforme aux standards PEP 8, typé avec `mypy`, formaté avec `black`

---
```
manga_collec_api/
├── pyproject.toml
├── README.md
├── src/
│   └── mangacollec_api/
│       ├── __init__.py
│       ├── client.py         # Client principal
│       ├── exceptions.py     # Exceptions personnalisées
│       ├── endpoints         # Définition centralisée des routes
│       │   ├── volume_endpoint.py
│       │   ├── serie_endpoint.py
│       │   ├── publisher_endpoint.py
│       │   ├── author_endpoint.py
│       │   ├── job_endpoint.py
│       │   ├── genre_endpoint.py
│       │   ├── kind_endpoint.py
│       │   ├── edition_endpoint.py
│       │   └── user_endpoint.py
│       │   
│       └── interfaces/
│           ├── __init__.py
│           ├── endpoints/
│           │   ├── __init__.py
│           │   ├── series_endpoint_interface.py
│           │   ├── volume_endpoint_interface.py
│           │   ├── publisher_endpoint_interface.py
│           │   ├── author_endpoint_interface.py
│           │   ├── job_endpoint_interface.py
│           │   ├── genre_endpoint_interface.py
│           │   ├── kind_endpoint_interface.py
│           │   ├── edition_endpoint_interface.py
│           │   └── user_endpoint_interface.py
│           │  
│           ├── client/
│           │   ├── client.py
│           │   └── 
│           │    
│           └──
├── tests/            
│   ├── __init__.py 
│   ├── test_client.py         
│   └── endpoints/    
│       ├── __init__.py
│       ├── test_serie.py
│       ├── test_volume.py
│       ├── test_publisher.py
│       ├── test_author.py
│       ├── test_edition.py
│       ├── test_job.py
│       ├── test_type.py
│       ├── test_kind.py
│       └── test_user.py

```

---

## 🚀 Installation

### Avec [Poetry](https://python-poetry.org/) (recommandé) :


## AUTH

- [x] POST          https://api.mangacollec.com/oauth/token (client credentials / password)

## V1

- [x] GET           https://api.mangacollec.com/v1/publishers
- [x] GET           https://api.mangacollec.com/v1/publishers/{id} # bdef8c9e-7395-465d-8175-a1b985d4aa92

- [x] GET           https://api.mangacollec.com/v1/amazon_offer/{asin} # 2380712956
- [x] GET           https://api.mangacollec.com/v1/bdfugue_offer/{isbn} # 9782380712957

- [x] GET           https://api.mangacollec.com/v1/volumes/news
- [x] GET           https://api.mangacollec.com/v1/volumes/{id} # 4f99ce2c-3a37-4252-9610-7b04a605d7d5

- [x] GET           https://api.mangacollec.com/v1/series
- [x] GET           https://api.mangacollec.com/v1/series/{id} # a320ac19-4318-4471-9e4e-eb017f4584d5

- [x] GET           https://api.mangacollec.com/v1/types
- [x] GET           https://api.mangacollec.com/v1/jobs/
- [x] GET           https://api.mangacollec.com/v1/kinds

- [x] GET           https://api.mangacollec.com/v1/authors
- [x] GET           https://api.mangacollec.com/v1/authors/{id}

- [x] GET           https://api.mangacollec.com/v2/planning?month={2022}-{09}-{99} #YYYY-MM-DD

- [x] GET           https://api.mangacollec.com/v1/user/{shooterdev}/collection
- [x] GET    [AUTH] https://api.mangacollec.com/v1/users/me/recommendation
- [x] GET    [AUTH] https://api.mangacollec.com/v1/users/me

- [ ] POST   [AUTH] https://api.mangacollec.com/v1/possessions_multiple
- [ ] DELETE [AUTH] https://api.mangacollec.com/v1/possessions_multiple

- [ ] POST   [AUTH] https://api.mangacollec.com/v1/follow_editions/
- [ ] DELETE [AUTH] https://api.mangacollec.com/v1/follow_editions/{id} # b7470d9f-5cdb-4f66-830d-43dac61554f5

- [ ] GET           https://api.mangacollec.com/v1/img_offer/{isbn} # 9782505119234

## V2

- [x] GET           https://api.mangacollec.com/v2/editions/{id} # 333eb14c-5f0a-4130-99fe-d2842cd06349

- [x] GET           https://api.mangacollec.com/v2/user/{shooterdev}/collection
- [x] GET    [AUTH] https://api.mangacollec.com/v2/users/me/collection

- [x] GET           https://api.mangacollec.com/v2/publishers
- [x] GET           https://api.mangacollec.com/v2/publishers/{id} # bdef8c9e-7395-465d-8175-a1b985d4aa92

- [x] GET           https://api.mangacollec.com/v2/volumes/news
- [x] GET           https://api.mangacollec.com/v2/volumes/{id} # 6e22eae9-2afd-45ba-8c26-d10d4224d5bf

- [x] GET           https://api.mangacollec.com/v2/kinds/

- [x] GET           https://api.mangacollec.com/v2/series/
- [x] GET           https://api.mangacollec.com/v2/series/{id} # 56057d0f-86e9-4e55-bfba-3b284af71855

- [x] GET           https://api.mangacollec.com/v2/authors/
- [x] GET           https://api.mangacollec.com/v2/authors/{id} # edad2d63-cc34-42b8-9bc2-ca9e210b670d
- [ ] GET           https://api.mangacollec.com/v2/users/me/ad_native_planning_perso

# V2 Serie item 

``` json
{
    "series": [
        {
            "id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "title": "Demon Slayer",
            "type_id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "adult_content": false,
            "editions_count": 5,
            "tasks_count": 1,
            "kinds_ids": [
                "5f2df76f-b8d1-4db6-9e36-506cabdbb1db",
                "7673ab04-ceca-4388-b52b-7b4d2af58e45",
                "05e9dc5b-bad9-4fb6-be5c-66925d58b911",
                "acd6bec9-507d-46ab-a1de-f18f8b8ca83c",
                "9d6a131c-4b4e-4cf6-a9aa-de78087d672d",
                "4b028255-c92e-4ff7-a732-7754bcf4afe6",
                "d5a3385a-cfcd-45f6-8f82-0c80956b084d"
            ]
        }
    ],
    "types": [
        {
            "id": "106f524e-7283-44b8-aa84-25e9a7fb1f7d",
            "title": "Manga",
            "to_display": false
        }
    ],
    "kinds": [
        {
            "id": "5f2df76f-b8d1-4db6-9e36-506cabdbb1db",
            "title": "Action"
        },
        {
            "id": "7673ab04-ceca-4388-b52b-7b4d2af58e45",
            "title": "Aventure"
        },
        {
            "id": "05e9dc5b-bad9-4fb6-be5c-66925d58b911",
            "title": "Démon"
        },
        {
            "id": "acd6bec9-507d-46ab-a1de-f18f8b8ca83c",
            "title": "Drame"
        },
        {
            "id": "9d6a131c-4b4e-4cf6-a9aa-de78087d672d",
            "title": "Fantastique"
        },
        {
            "id": "4b028255-c92e-4ff7-a732-7754bcf4afe6",
            "title": "Historique"
        },
        {
            "id": "d5a3385a-cfcd-45f6-8f82-0c80956b084d",
            "title": "Shōnen"
        }
    ],
    "tasks": [
        {
            "id": "5c522a92-899f-4c44-b9ef-719b8aa111d7",
            "job_id": "dc7b6062-6aae-49ee-87a2-95d47ab52600",
            "series_id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "author_id": "95919709-c155-4a04-9525-e06d81025a62"
        }
    ],
    "jobs": [
        {
            "id": "dc7b6062-6aae-49ee-87a2-95d47ab52600",
            "title": "Auteur"
        }
    ],
    "authors": [
        {
            "id": "95919709-c155-4a04-9525-e06d81025a62",
            "name": "Gotouge",
            "first_name": "Koyoharu",
            "tasks_count": 15
        }
    ],
    "editions": [
        {
            "id": "a35560db-1d96-4a17-8092-bb487699c51f",
            "title": "Première édition - Les rôdeurs de la nuit",
            "series_id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "parent_edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "volumes_count": 3,
            "last_volume_number": 3,
            "commercial_stop": true,
            "not_finished": true,
            "follow_editions_count": 1222
        },
        {
            "id": "17090559-1f60-478a-9993-98de13643a10",
            "title": "Edition Pilier",
            "series_id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "parent_edition_id": null,
            "volumes_count": 8,
            "last_volume_number": 8,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 6075
        },
        {
            "id": "d65cbaab-54f1-418c-9378-cb698321605c",
            "title": "Edition Collector Noël",
            "series_id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "parent_edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "volumes_count": 1,
            "last_volume_number": null,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 2973
        },
        {
            "id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "title": null,
            "series_id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "parent_edition_id": null,
            "volumes_count": 23,
            "last_volume_number": 23,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 144331
        },
        {
            "id": "b245ee3e-1ab6-427f-aec9-25f47e043ba1",
            "title": "Edition collector",
            "series_id": "a320ac19-4318-4471-9e4e-eb017f4584d5",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "parent_edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "volumes_count": 2,
            "last_volume_number": 23,
            "commercial_stop": false,
            "not_finished": false,
            "follow_editions_count": 27870
        }
    ],
    "publishers": [
        {
            "id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "title": "Panini",
            "closed": false,
            "editions_count": 428,
            "no_amazon": false
        }
    ],
    "volumes": [
        {
            "id": "e8bc74d5-3afb-4eee-a344-421b9c9f4c05",
            "title": null,
            "number": 17,
            "release_date": "2021-05-12",
            "isbn": "9782809496987",
            "asin": "2809496986",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 73486,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51BOH-Ays2L.jpg"
        },
        {
            "id": "4119d951-5d9e-4170-9678-fb9ba0079331",
            "title": null,
            "number": 1,
            "release_date": "2024-11-13",
            "isbn": "9791039131445",
            "asin": "B0D7VB2VZZ",
            "edition_id": "d65cbaab-54f1-418c-9378-cb698321605c",
            "possessions_count": 2615,
            "not_sold": false,
            "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWs0T0RKbE1XSm1OQzFpT1dSaExUUXdaalV0T0RBeVppMHpNR016T0RVeE5UQTJOMk1HT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--07bd888ff3dcd50e63ad0d78ecc43afb6aefbe29/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBPZ2h3Ym1jNkZISmxjMmw2WlY5MGIxOXNhVzFwZEZzSGFRTDBBV2tDOUFFPSIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--4f248cb7a1f96865b50df1fd5e45e7f4a6a9f63e/4119d951-5d9e-4170-9678-fb9ba0079331.webp"
        },
        {
            "id": "bb7fc792-f888-4ed2-b6a1-503c67a4ceb7",
            "title": null,
            "number": 5,
            "release_date": "2024-04-03",
            "isbn": "9791039124362",
            "asin": "B0CMWTZR7L",
            "edition_id": "17090559-1f60-478a-9993-98de13643a10",
            "possessions_count": 1664,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/513VFmBLq9L.jpg"
        },
        {
            "id": "de38b287-9ad7-478e-b989-52bbab1a2db4",
            "title": null,
            "number": 8,
            "release_date": "2024-10-16",
            "isbn": "9791039127110",
            "asin": "B0D44VW7YC",
            "edition_id": "17090559-1f60-478a-9993-98de13643a10",
            "possessions_count": 1249,
            "not_sold": false,
            "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWsxTmpSaU16STROaTAxWXpsbExUUmlORFV0WWpCalpDMHpaakE1TW1JM016azBNREFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--2f9d5835abdac955bbecaf45f9ae79822d24c06d/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/de38b287-9ad7-478e-b989-52bbab1a2db4.jpg"
        },
        {
            "id": "531a00c8-e4f1-4b85-b62e-50d553c56eb8",
            "title": null,
            "number": 23,
            "release_date": "2022-07-06",
            "isbn": "9791039109253",
            "asin": "B09TKNBRS2",
            "edition_id": "b245ee3e-1ab6-427f-aec9-25f47e043ba1",
            "possessions_count": 23549,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51N4OjPpqCL.jpg"
        },
        {
            "id": "7860eed7-63eb-496e-b6ff-a66b11d05b89",
            "title": null,
            "number": 2,
            "release_date": "2023-10-25",
            "isbn": "9791039120814",
            "asin": "B0C9ZCZLVW",
            "edition_id": "17090559-1f60-478a-9993-98de13643a10",
            "possessions_count": 2681,
            "not_sold": false,
            "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWszTVdNM05HSTBZUzB6Tm1abUxUUTVPRGd0WVdFMllTMHhPV1ZsWW1Zd1lUWTVZek1HT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--e87fbba81da8c623dda91324450f52444db3e98e/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/7860eed7-63eb-496e-b6ff-a66b11d05b89.jpg"
        },
        {
            "id": "16c77d02-b604-4a9d-bb77-d0c21a1dfcaf",
            "title": null,
            "number": 6,
            "release_date": "2024-06-19",
            "isbn": "9791039125536",
            "asin": "B0CMWW8DDF",
            "edition_id": "17090559-1f60-478a-9993-98de13643a10",
            "possessions_count": 1524,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51Cg+hlF4FL.jpg"
        },
        {
            "id": "19e697e8-ae5d-4647-86c2-4e8252d8f1dc",
            "title": null,
            "number": 1,
            "release_date": "2022-07-06",
            "isbn": "9791039109260",
            "asin": "B09RZPFG92",
            "edition_id": "b245ee3e-1ab6-427f-aec9-25f47e043ba1",
            "possessions_count": 17825,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51Kw9yox0AL.jpg"
        },
        {
            "id": "91290817-341d-407b-893b-83e479387462",
            "title": null,
            "number": 5,
            "release_date": "2019-11-27",
            "isbn": "9782809477542",
            "asin": "280947754X",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 95694,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/51ivrMligNL.jpg"
        },
        {
            "id": "67be1aaa-3dcc-493d-b6b2-33b0f73b9d47",
            "title": null,
            "number": 15,
            "release_date": "2021-01-13",
            "isbn": "9782809493900",
            "asin": "2809493901",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 74934,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/61GjWhkQK0L.jpg"
        },
        {
            "id": "da22139c-910c-4bdd-8622-20f7122cb60d",
            "title": null,
            "number": 3,
            "release_date": "2019-10-09",
            "isbn": "9782809476132",
            "asin": "2809476136",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 108876,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/515BhxFsJAL.jpg"
        },
        {
            "id": "84bec56a-2b55-4307-8255-e622acab525b",
            "title": null,
            "number": 12,
            "release_date": "2020-10-14",
            "isbn": "9782809490084",
            "asin": "2809490082",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 81529,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51f2TfgVDTL.jpg"
        },
        {
            "id": "7cd71742-5a2a-4a41-9498-bc047abe0ee9",
            "title": null,
            "number": 4,
            "release_date": "2024-02-07",
            "isbn": "9791039122924",
            "asin": "B0CHDZV1TC",
            "edition_id": "17090559-1f60-478a-9993-98de13643a10",
            "possessions_count": 1959,
            "not_sold": false,
            "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt3T0RaaFl6a3pOaTAyTm1Vd0xUUmxZbUV0WWpSaFpDMHpNRGM0TnpBNE9USTROak1HT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--de923c320b466493492b41908b38f603f6031e55/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/7cd71742-5a2a-4a41-9498-bc047abe0ee9.jpg"
        },
        {
            "id": "2df17f69-0994-4017-b7c1-19cf52b16005",
            "title": null,
            "number": 19,
            "release_date": "2021-10-13",
            "isbn": "9791039101400",
            "asin": "B0948LGQRD",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 68630,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51rgn6XON2L.jpg"
        },
        {
            "id": "159680d0-010b-4542-bf3b-0e8ae2f270fa",
            "title": null,
            "number": 7,
            "release_date": "2020-03-04",
            "isbn": "9782809486612",
            "asin": "2809486611",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 88497,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51OUhycyILL.jpg"
        },
        {
            "id": "d9694784-d6a7-4591-969c-6e4dc406514b",
            "title": null,
            "number": 16,
            "release_date": "2021-03-17",
            "isbn": "9782809495430",
            "asin": "2809495432",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 73720,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51QTAB2wwwL.jpg"
        },
        {
            "id": "47e9fa5f-0391-4461-a18c-1387614ff81e",
            "title": null,
            "number": 21,
            "release_date": "2022-03-30",
            "isbn": "9791039105071",
            "asin": "B09HFT3R87",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 61122,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51XjGKUajzL.jpg"
        },
        {
            "id": "08945667-24cb-4f41-bcd3-a51903e60f83",
            "title": null,
            "number": 23,
            "release_date": "2022-07-06",
            "isbn": "9791039107457",
            "asin": "B09TKMYF56",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 53931,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/515WvZqv5QL.jpg"
        },
        {
            "id": "d557e5b2-64a3-4aa7-86ff-36876ab3620b",
            "title": null,
            "number": 8,
            "release_date": "2020-06-17",
            "isbn": "9782809487206",
            "asin": "2809487200",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 87451,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51GgipwTEbL.jpg"
        },
        {
            "id": "14648812-053a-41de-8183-3f0ffe33c9ea",
            "title": null,
            "number": 22,
            "release_date": "2022-05-18",
            "isbn": "9791039106863",
            "asin": "B09TQWCPYL",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 58721,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51hKCk3rs5L.jpg"
        },
        {
            "id": "a0bfce54-5361-42d0-8381-371a541e8c2b",
            "title": null,
            "number": 13,
            "release_date": "2020-12-09",
            "isbn": "9782809491616",
            "asin": "2809491615",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 77800,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51uqFpicHIL.jpg"
        },
        {
            "id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "title": null,
            "number": 1,
            "release_date": "2019-09-18",
            "isbn": "9782809482317",
            "asin": "2809482314",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 123779,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/51Ky6nqMXpL.jpg"
        },
        {
            "id": "4d83a0e2-1bda-4373-b814-af12045535fd",
            "title": null,
            "number": 11,
            "release_date": "2020-09-16",
            "isbn": "9782809489750",
            "asin": "2809489750",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 80580,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51lw20OjGoL.jpg"
        },
        {
            "id": "7d2d3524-8ecc-413e-a565-4f15f262834b",
            "title": null,
            "number": 9,
            "release_date": "2020-07-16",
            "isbn": "9782809487565",
            "asin": "2809487561",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 85174,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/5138icwel1L.jpg"
        },
        {
            "id": "5bff6a01-d5b6-4bf2-9874-8308c9b59ad4",
            "title": null,
            "number": 1,
            "release_date": "2023-09-20",
            "isbn": "9791039120791",
            "asin": "B0C53FMFGN",
            "edition_id": "17090559-1f60-478a-9993-98de13643a10",
            "possessions_count": 3547,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51FEvIk9uWL.jpg"
        },
        {
            "id": "c0b9570f-d6ee-4b6f-adac-782a2b8f7c92",
            "title": null,
            "number": 14,
            "release_date": "2020-12-09",
            "isbn": "9782809492491",
            "asin": "2809492492",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 76175,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51lbyWIVrkL.jpg"
        },
        {
            "id": "9abe2a23-17a1-42ac-8dad-de2760bdef50",
            "title": null,
            "number": 4,
            "release_date": "2019-10-09",
            "isbn": "9782809476903",
            "asin": "280947690X",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 100855,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/515CMRXM5CL.jpg"
        },
        {
            "id": "43c26826-5f2e-4db9-a937-bd0d2f907457",
            "title": null,
            "number": 3,
            "release_date": "2018-01-10",
            "isbn": "9782809468533",
            "asin": "2809468532",
            "edition_id": "a35560db-1d96-4a17-8092-bb487699c51f",
            "possessions_count": 457,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/614PXf9bxHL.jpg"
        },
        {
            "id": "c1101eb0-bb71-46db-9eb3-30d3bb5478b6",
            "title": null,
            "number": 2,
            "release_date": "2017-10-11",
            "isbn": "9782809466089",
            "asin": "2809466084",
            "edition_id": "a35560db-1d96-4a17-8092-bb487699c51f",
            "possessions_count": 599,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/619LK%2Bpfz%2BL.jpg"
        },
        {
            "id": "1981dc8c-247a-405e-af8a-09cfb7445908",
            "title": null,
            "number": 7,
            "release_date": "2024-08-07",
            "isbn": "9791039126656",
            "asin": "B0CY1LJ9WJ",
            "edition_id": "17090559-1f60-478a-9993-98de13643a10",
            "possessions_count": 1377,
            "not_sold": false,
            "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWsxT1RCbE1qbGhNeTFtWW1ObUxUUmpNVFV0T1Rsak9DMHlPVEUzWVRNek56UTBaR0lHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--70dd18c6f99e38db3a9336f6b4e6c628aaadddc9/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/1981dc8c-247a-405e-af8a-09cfb7445908.jpg"
        },
        {
            "id": "cfd7d6e5-0e4f-47b7-8031-6eaab5be7139",
            "title": null,
            "number": 10,
            "release_date": "2020-08-12",
            "isbn": "9782809488289",
            "asin": "2809488282",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 83118,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51KpvC4rrgL.jpg"
        },
        {
            "id": "72f73c6e-3d3d-43ed-9cd6-dabbcfbd6c75",
            "title": null,
            "number": 18,
            "release_date": "2021-07-15",
            "isbn": "9782809498103",
            "asin": "2809498105",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 68924,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51vrKY6Eg4S.jpg"
        },
        {
            "id": "664aa063-8aef-4aea-a6da-44e2effa7134",
            "title": null,
            "number": 2,
            "release_date": "2019-09-18",
            "isbn": "9782809482324",
            "asin": "2809482322",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 115638,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/51pK3xUq1xL.jpg"
        },
        {
            "id": "64e820b5-5d67-446e-8e3f-ce23a0438a68",
            "title": null,
            "number": 1,
            "release_date": "2017-08-23",
            "isbn": "9782809465372",
            "asin": "2809465371",
            "edition_id": "a35560db-1d96-4a17-8092-bb487699c51f",
            "possessions_count": 713,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/61nLX05oXOL.jpg"
        },
        {
            "id": "8f6f0e9f-7c51-4fc0-b9cb-47ecc03b5e07",
            "title": null,
            "number": 3,
            "release_date": "2023-12-06",
            "isbn": "9791039121651",
            "asin": "B0CC8W362C",
            "edition_id": "17090559-1f60-478a-9993-98de13643a10",
            "possessions_count": 2297,
            "not_sold": false,
            "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWsyWmpRMFl6RXpaUzA0WTJRNExUUTBZekF0T0dKa1lTMW1PREZtTUdWbE56a3hOVEFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--0332ce8f104ed381acd609bb80a34c43ca82b21c/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/8f6f0e9f-7c51-4fc0-b9cb-47ecc03b5e07.jpg"
        },
        {
            "id": "134f513c-c65a-40b2-9c03-216123b5f41d",
            "title": null,
            "number": 6,
            "release_date": "2020-01-02",
            "isbn": "9782809478181",
            "asin": "280947818X",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 91664,
            "not_sold": false,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/51NqK9xOY0L.jpg"
        },
        {
            "id": "8d5a245a-0c1d-4b49-80a7-01ea16be798c",
            "title": null,
            "number": 20,
            "release_date": "2022-01-12",
            "isbn": "9791039101707",
            "asin": "B095KN8RBR",
            "edition_id": "56a08fea-5f6b-44ab-8daf-5cee677f6cf2",
            "possessions_count": 62876,
            "not_sold": false,
            "image_url": "https://m.media-amazon.com/images/I/51FDU7dMzbL.jpg"
        }
    ],
    "box_editions": [
        {
            "id": "b6df9e4d-c62c-4314-8460-158f4bfc06b8",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 7182
        },
        {
            "id": "67ffba62-913e-48a3-95c8-82175a609b0d",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 3,
            "adult_content": false,
            "box_follow_editions_count": 1188
        },
        {
            "id": "cbeae4c1-af3e-492d-bf07-5c8a2eb67f33",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 8671
        },
        {
            "id": "9d0f2d77-5829-412e-852b-0a76fdd5b02b",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 8741
        },
        {
            "id": "c3993c87-2bf5-434d-bd62-442a36b2744e",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 4,
            "adult_content": false,
            "box_follow_editions_count": 4033
        },
        {
            "id": "699ee11b-8dfc-43b6-aa1d-9950ebe7a11d",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 937
        },
        {
            "id": "2d011677-903a-4adf-a1b8-abef4882c97b",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 6,
            "adult_content": false,
            "box_follow_editions_count": 859
        },
        {
            "id": "83b63e92-189a-413e-b725-6a6ef4ebdce4",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 7409
        },
        {
            "id": "91801ee0-1bb1-48d6-97ba-e35065522036",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 127
        },
        {
            "id": "2b1c8bb0-ab4d-40d0-b111-76d309c1d507",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 966
        },
        {
            "id": "5c19001c-d260-4b80-82c5-8a1f7cd791ff",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 1,
            "adult_content": false,
            "box_follow_editions_count": 7864
        },
        {
            "id": "a094c234-c896-4a2d-98a2-81ae69ac2b59",
            "title": "Demon Slayer",
            "publisher_id": "df4bb56a-de70-48ed-a507-b946f7ae2c0e",
            "boxes_count": 4,
            "adult_content": false,
            "box_follow_editions_count": 2165
        }
    ],
    "boxes": [
        {
            "id": "5beda4cf-962d-46bd-8918-18484755cce4",
            "title": "Coffret Tomes 13 à 18",
            "number": 3,
            "release_date": "2022-11-16",
            "isbn": "9791039111744",
            "asin": "B0B76GQWPS",
            "commercial_stop": false,
            "box_edition_id": "a094c234-c896-4a2d-98a2-81ae69ac2b59",
            "box_possessions_count": 1354,
            "image_url": "https://m.media-amazon.com/images/I/514MXa+4IFL.jpg"
        },
        {
            "id": "b719c558-fa08-45fe-8b8b-34969455da4d",
            "title": "Coffret Roman jeunesse N°02",
            "number": 2,
            "release_date": "2023-10-04",
            "isbn": "9791039121033",
            "asin": "B0C586RQFD",
            "commercial_stop": false,
            "box_edition_id": "2d011677-903a-4adf-a1b8-abef4882c97b",
            "box_possessions_count": 304,
            "image_url": "https://m.media-amazon.com/images/I/51Q7rDIndSL.jpg"
        },
        {
            "id": "13595d56-cf87-4fe3-9e58-4afc60e476b9",
            "title": "Pack découverte",
            "number": 0,
            "release_date": "2025-01-22",
            "isbn": "9791039133609",
            "asin": "B0DHGCJCN3",
            "commercial_stop": false,
            "box_edition_id": "67ffba62-913e-48a3-95c8-82175a609b0d",
            "box_possessions_count": 66,
            "image_url": "https://m.media-amazon.com/images/I/512s9dwAUWL.jpg"
        },
        {
            "id": "dcdbb967-11aa-481b-8b5b-9ac8d48b1cd6",
            "title": "Coffret collector Tome 22 ",
            "number": 0,
            "release_date": "2022-05-18",
            "isbn": "9791039106887",
            "asin": "B09TSV425C",
            "commercial_stop": false,
            "box_edition_id": "83b63e92-189a-413e-b725-6a6ef4ebdce4",
            "box_possessions_count": 7007,
            "image_url": "https://m.media-amazon.com/images/I/51ZGeiDMg6L.jpg"
        },
        {
            "id": "99d60f7e-7fac-4c8d-82a3-cb31d0a559ed",
            "title": "Coffret Tomes 7 à 12",
            "number": 2,
            "release_date": "2022-11-16",
            "isbn": "9791039111737",
            "asin": "B0B76GXZR6",
            "commercial_stop": false,
            "box_edition_id": "a094c234-c896-4a2d-98a2-81ae69ac2b59",
            "box_possessions_count": 1387,
            "image_url": "https://m.media-amazon.com/images/I/51qtBmVLwYL.jpg"
        },
        {
            "id": "fbe9bed0-0a47-4958-bb8b-82867ce5536e",
            "title": "Pack découverte",
            "number": 0,
            "release_date": "2023-01-18",
            "isbn": "9791039112574",
            "asin": "B0BDDLQN5F",
            "commercial_stop": true,
            "box_edition_id": "67ffba62-913e-48a3-95c8-82175a609b0d",
            "box_possessions_count": 529,
            "image_url": "https://m.media-amazon.com/images/I/51j0GV1-8kL.jpg"
        },
        {
            "id": "50d1e052-00f8-4be4-b853-5db6b4ff4eea",
            "title": "Coffret Tomes 4 à 6",
            "number": 2,
            "release_date": "2021-11-17",
            "isbn": "9791039103169",
            "asin": "B09BGG7KJM",
            "commercial_stop": false,
            "box_edition_id": "c3993c87-2bf5-434d-bd62-442a36b2744e",
            "box_possessions_count": 1944,
            "image_url": "https://m.media-amazon.com/images/I/517j7Le-2uL.jpg"
        },
        {
            "id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "title": "Coffret Intégrale Vide",
            "number": 0,
            "release_date": "2023-11-02",
            "isbn": "9791039118187",
            "asin": "B0CHJZLHT1",
            "commercial_stop": false,
            "box_edition_id": "699ee11b-8dfc-43b6-aa1d-9950ebe7a11d",
            "box_possessions_count": 769,
            "image_url": "https://m.media-amazon.com/images/I/610DfEIDLPL.jpg"
        },
        {
            "id": "dd4b2f93-db1b-4708-8f0a-b57d540745e7",
            "title": "Coffret Roman jeunesse N°03",
            "number": 3,
            "release_date": "2024-03-20",
            "isbn": "9791039122931",
            "asin": "B0CHRCT28C",
            "commercial_stop": false,
            "box_edition_id": "2d011677-903a-4adf-a1b8-abef4882c97b",
            "box_possessions_count": 213,
            "image_url": "https://m.media-amazon.com/images/I/51NVGl7uaWL.jpg"
        },
        {
            "id": "349d077f-f2c0-4bf2-b303-94181746772a",
            "title": "Coffret Roman jeunesse N°06",
            "number": 6,
            "release_date": "2024-11-13",
            "isbn": "9791039127400",
            "asin": "B0D7VDVC5M",
            "commercial_stop": false,
            "box_edition_id": "2d011677-903a-4adf-a1b8-abef4882c97b",
            "box_possessions_count": 105,
            "image_url": "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxrTm1OaE16VmlaaTFrTkRZekxUUTRNbVV0WW1JMlpTMDVZV1ptWW1ZeFlUVTFOMllHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--be8b37f4c1e040d0eddc0316fd92942f2f680aa6/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/9791039127400.jpg"
        },
        {
            "id": "1429de25-05aa-4a4f-89d3-3dfd1172044d",
            "title": "Edition Pilier Tome 1 + plaque métal offerte",
            "number": 0,
            "release_date": "2025-03-12",
            "isbn": "9791039127066",
            "asin": "B0DHRD3VJ7",
            "commercial_stop": false,
            "box_edition_id": "91801ee0-1bb1-48d6-97ba-e35065522036",
            "box_possessions_count": 74,
            "image_url": "https://m.media-amazon.com/images/I/51uJE14fslL.jpg"
        },
        {
            "id": "e2f3a62f-c934-4bd8-a7d4-0996db4876a6",
            "title": "Coffret collector Tome 17 ",
            "number": 0,
            "release_date": "2021-05-12",
            "isbn": "9782809497007",
            "asin": "2809497001",
            "commercial_stop": false,
            "box_edition_id": "5c19001c-d260-4b80-82c5-8a1f7cd791ff",
            "box_possessions_count": 7403,
            "image_url": "https://m.media-amazon.com/images/I/51uo8Zt5QlL.jpg"
        },
        {
            "id": "ab54b3a7-be99-4066-b26c-2732d86f885d",
            "title": "Coffret collector Tome 23 ",
            "number": 0,
            "release_date": "2022-07-06",
            "isbn": "9791039109307",
            "asin": "B09TVQ9D9X",
            "commercial_stop": false,
            "box_edition_id": "b6df9e4d-c62c-4314-8460-158f4bfc06b8",
            "box_possessions_count": 6628,
            "image_url": "https://m.media-amazon.com/images/I/51tSx5VsDaL.jpg"
        },
        {
            "id": "c00b7e0e-dd6d-435c-8266-601de7977400",
            "title": "Coffret Tomes 1 à 6",
            "number": 1,
            "release_date": "2022-11-16",
            "isbn": "9791039111720",
            "asin": "B0B76HDC31",
            "commercial_stop": false,
            "box_edition_id": "a094c234-c896-4a2d-98a2-81ae69ac2b59",
            "box_possessions_count": 1400,
            "image_url": "https://m.media-amazon.com/images/I/51BQyK7y4qL.jpg"
        },
        {
            "id": "9dc9c99f-c87f-4c1f-85ca-7ab001d4eddd",
            "title": "Coffret  Tomes 1 à 3",
            "number": 1,
            "release_date": "2021-11-17",
            "isbn": "9791039103152",
            "asin": "B09BGG6ZHJ",
            "commercial_stop": false,
            "box_edition_id": "c3993c87-2bf5-434d-bd62-442a36b2744e",
            "box_possessions_count": 1843,
            "image_url": "https://m.media-amazon.com/images/I/51WlojplLFL.jpg"
        },
        {
            "id": "ce72600b-6fe9-44c7-9dd3-1a103b3275b2",
            "title": "Coffret Roman jeunesse N°05",
            "number": 5,
            "release_date": "2024-08-21",
            "isbn": "9791039126687",
            "asin": "B0CZ33S8HM",
            "commercial_stop": false,
            "box_edition_id": "2d011677-903a-4adf-a1b8-abef4882c97b",
            "box_possessions_count": 156,
            "image_url": "https://www.bdfugue.com/media/catalog/product/9/7/9791039126687_1_75.jpg"
        },
        {
            "id": "490c9407-78c4-4f6a-a30a-fa670fb7052b",
            "title": "Coffret Roman jeunesse N°04",
            "number": 4,
            "release_date": "2024-06-19",
            "isbn": "9791039124775",
            "asin": "B0CRH36JP6",
            "commercial_stop": false,
            "box_edition_id": "2d011677-903a-4adf-a1b8-abef4882c97b",
            "box_possessions_count": 171,
            "image_url": "https://m.media-amazon.com/images/I/51ocsPaTzwL.jpg"
        },
        {
            "id": "fd555e77-dce3-41a6-818e-3089d1f98a07",
            "title": "Coffret collector Tome 21 ",
            "number": 0,
            "release_date": "2022-03-30",
            "isbn": "9791039105101",
            "asin": "B09P9ZJG63",
            "commercial_stop": false,
            "box_edition_id": "cbeae4c1-af3e-492d-bf07-5c8a2eb67f33",
            "box_possessions_count": 8071,
            "image_url": "https://m.media-amazon.com/images/I/51cEvmqTHzL.jpg"
        },
        {
            "id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "title": "Coffret Intégrale",
            "number": 0,
            "release_date": "2023-11-02",
            "isbn": "9791039118170",
            "asin": "B0CBB2B17M",
            "commercial_stop": false,
            "box_edition_id": "2b1c8bb0-ab4d-40d0-b111-76d309c1d507",
            "box_possessions_count": 618,
            "image_url": "https://m.media-amazon.com/images/I/618hu9kD6jL.jpg"
        },
        {
            "id": "db1625ae-c691-4f38-9fed-0c96702e7c7e",
            "title": "Coffret Roman jeunesse N°01",
            "number": 1,
            "release_date": "2023-07-12",
            "isbn": "9791039120746",
            "asin": "B0C13GC883",
            "commercial_stop": false,
            "box_edition_id": "2d011677-903a-4adf-a1b8-abef4882c97b",
            "box_possessions_count": 487,
            "image_url": "https://m.media-amazon.com/images/I/51r+ScEM-dL.jpg"
        },
        {
            "id": "6b3d25c5-efed-4dff-a600-b9209326711e",
            "title": "Coffret Tomes 19 à 23",
            "number": 4,
            "release_date": "2022-11-16",
            "isbn": "9791039112154",
            "asin": "B0B76JC18P",
            "commercial_stop": false,
            "box_edition_id": "a094c234-c896-4a2d-98a2-81ae69ac2b59",
            "box_possessions_count": 1336,
            "image_url": "https://m.media-amazon.com/images/I/51qmAJyYzML.jpg"
        },
        {
            "id": "f5846cbe-4928-42ad-871d-4a33c599e0ec",
            "title": "Coffret Tomes 1 à 3",
            "number": 1,
            "release_date": "2020-11-25",
            "isbn": "9782809491623",
            "asin": "2809491623",
            "commercial_stop": false,
            "box_edition_id": "c3993c87-2bf5-434d-bd62-442a36b2744e",
            "box_possessions_count": 1060,
            "image_url": "https://m.media-amazon.com/images/I/51jMpYXlozL.jpg"
        },
        {
            "id": "082e582d-6e65-4655-9295-a35e41a3b497",
            "title": "Pack découverte",
            "number": 0,
            "release_date": "2019-09-18",
            "isbn": "9782809482300",
            "asin": "2809482306",
            "commercial_stop": true,
            "box_edition_id": "67ffba62-913e-48a3-95c8-82175a609b0d",
            "box_possessions_count": 475,
            "image_url": "https://images-eu.ssl-images-amazon.com/images/I/612d5QUqXVL.jpg"
        },
        {
            "id": "892225b9-dfa0-47b2-a7a0-6a25230830fa",
            "title": "Coffret collector Tome 19 ",
            "number": 0,
            "release_date": "2021-10-13",
            "isbn": "9791039101424",
            "asin": "B0948KS7BW",
            "commercial_stop": false,
            "box_edition_id": "9d0f2d77-5829-412e-852b-0a76fdd5b02b",
            "box_possessions_count": 8269,
            "image_url": "https://m.media-amazon.com/images/I/51fCKdbw6SL.jpg"
        },
        {
            "id": "02284b39-2b33-41fd-a36c-327819dcc6b8",
            "title": "Coffret Tomes 4 à 6",
            "number": 2,
            "release_date": "2020-11-25",
            "isbn": "9782809492507",
            "asin": "2809492506",
            "commercial_stop": false,
            "box_edition_id": "c3993c87-2bf5-434d-bd62-442a36b2744e",
            "box_possessions_count": 1287,
            "image_url": "https://m.media-amazon.com/images/I/512iAkZGt6L.jpg"
        }
    ],
    "box_volumes": [
        {
            "id": "ef2eb005-6ed9-4958-918f-f0e0b4ba334c",
            "box_id": "c00b7e0e-dd6d-435c-8266-601de7977400",
            "volume_id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "included": true
        },
        {
            "id": "60d768aa-68c1-40e0-a762-adabb089af18",
            "box_id": "c00b7e0e-dd6d-435c-8266-601de7977400",
            "volume_id": "664aa063-8aef-4aea-a6da-44e2effa7134",
            "included": true
        },
        {
            "id": "47fca3ac-8b30-4033-81d7-afc0b78b913c",
            "box_id": "c00b7e0e-dd6d-435c-8266-601de7977400",
            "volume_id": "da22139c-910c-4bdd-8622-20f7122cb60d",
            "included": true
        },
        {
            "id": "c1205fd3-e70c-4763-b72c-c6f0497c7fc1",
            "box_id": "c00b7e0e-dd6d-435c-8266-601de7977400",
            "volume_id": "9abe2a23-17a1-42ac-8dad-de2760bdef50",
            "included": true
        },
        {
            "id": "c9e5e244-4ca1-43e4-9492-4c637265b870",
            "box_id": "c00b7e0e-dd6d-435c-8266-601de7977400",
            "volume_id": "91290817-341d-407b-893b-83e479387462",
            "included": true
        },
        {
            "id": "1503c6b6-dc1d-4454-a539-994df3d86e00",
            "box_id": "c00b7e0e-dd6d-435c-8266-601de7977400",
            "volume_id": "134f513c-c65a-40b2-9c03-216123b5f41d",
            "included": true
        },
        {
            "id": "1a0f4154-d866-42ba-9df5-0993ee4f0bab",
            "box_id": "99d60f7e-7fac-4c8d-82a3-cb31d0a559ed",
            "volume_id": "159680d0-010b-4542-bf3b-0e8ae2f270fa",
            "included": true
        },
        {
            "id": "3afb139a-0c57-4b84-b10b-4249bfaff8d8",
            "box_id": "99d60f7e-7fac-4c8d-82a3-cb31d0a559ed",
            "volume_id": "d557e5b2-64a3-4aa7-86ff-36876ab3620b",
            "included": true
        },
        {
            "id": "747aa82d-e3f9-41b0-bd70-7d83d75891ef",
            "box_id": "99d60f7e-7fac-4c8d-82a3-cb31d0a559ed",
            "volume_id": "7d2d3524-8ecc-413e-a565-4f15f262834b",
            "included": true
        },
        {
            "id": "ab9e42d7-2406-4106-acea-baac9f7bdb3f",
            "box_id": "99d60f7e-7fac-4c8d-82a3-cb31d0a559ed",
            "volume_id": "4d83a0e2-1bda-4373-b814-af12045535fd",
            "included": true
        },
        {
            "id": "0d943ec4-e5f1-4561-83cc-db0ad3b5d6d0",
            "box_id": "99d60f7e-7fac-4c8d-82a3-cb31d0a559ed",
            "volume_id": "cfd7d6e5-0e4f-47b7-8031-6eaab5be7139",
            "included": true
        },
        {
            "id": "c68cec97-aedf-47a3-9502-e16543f772f2",
            "box_id": "99d60f7e-7fac-4c8d-82a3-cb31d0a559ed",
            "volume_id": "84bec56a-2b55-4307-8255-e622acab525b",
            "included": true
        },
        {
            "id": "5970bd7f-8ca0-4916-a326-fa5daaeff78a",
            "box_id": "5beda4cf-962d-46bd-8918-18484755cce4",
            "volume_id": "a0bfce54-5361-42d0-8381-371a541e8c2b",
            "included": true
        },
        {
            "id": "de88c6f5-03d6-43cb-b017-413417dfd976",
            "box_id": "5beda4cf-962d-46bd-8918-18484755cce4",
            "volume_id": "c0b9570f-d6ee-4b6f-adac-782a2b8f7c92",
            "included": true
        },
        {
            "id": "6a6e2586-a2f0-43f8-9b2e-c79d75a6bed3",
            "box_id": "5beda4cf-962d-46bd-8918-18484755cce4",
            "volume_id": "67be1aaa-3dcc-493d-b6b2-33b0f73b9d47",
            "included": true
        },
        {
            "id": "5fffc7ae-9d23-4fe2-b8b0-fb7ff5f9a137",
            "box_id": "5beda4cf-962d-46bd-8918-18484755cce4",
            "volume_id": "d9694784-d6a7-4591-969c-6e4dc406514b",
            "included": true
        },
        {
            "id": "f2bcec42-e1a0-45b6-a2df-e8636ce33d65",
            "box_id": "5beda4cf-962d-46bd-8918-18484755cce4",
            "volume_id": "e8bc74d5-3afb-4eee-a344-421b9c9f4c05",
            "included": true
        },
        {
            "id": "a98829f6-ef57-4b08-bb58-30fb4eba42e3",
            "box_id": "5beda4cf-962d-46bd-8918-18484755cce4",
            "volume_id": "72f73c6e-3d3d-43ed-9cd6-dabbcfbd6c75",
            "included": true
        },
        {
            "id": "40f9809f-4ff2-494b-9261-c7f3a665cae4",
            "box_id": "6b3d25c5-efed-4dff-a600-b9209326711e",
            "volume_id": "2df17f69-0994-4017-b7c1-19cf52b16005",
            "included": true
        },
        {
            "id": "e5d57e47-f057-466a-bde5-0284e941928c",
            "box_id": "6b3d25c5-efed-4dff-a600-b9209326711e",
            "volume_id": "8d5a245a-0c1d-4b49-80a7-01ea16be798c",
            "included": true
        },
        {
            "id": "b267e2b6-d5d0-4d5a-bd8b-15afbaac56a2",
            "box_id": "6b3d25c5-efed-4dff-a600-b9209326711e",
            "volume_id": "47e9fa5f-0391-4461-a18c-1387614ff81e",
            "included": true
        },
        {
            "id": "6300c5f8-cf4f-43ed-885b-cacf198592d2",
            "box_id": "6b3d25c5-efed-4dff-a600-b9209326711e",
            "volume_id": "14648812-053a-41de-8183-3f0ffe33c9ea",
            "included": true
        },
        {
            "id": "ac3b2a87-7195-44c8-bbf3-50217943bb84",
            "box_id": "6b3d25c5-efed-4dff-a600-b9209326711e",
            "volume_id": "08945667-24cb-4f41-bcd3-a51903e60f83",
            "included": true
        },
        {
            "id": "3047e28e-f554-40ad-b1e9-eb6ca6ae12a6",
            "box_id": "082e582d-6e65-4655-9295-a35e41a3b497",
            "volume_id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "included": true
        },
        {
            "id": "9c68583f-a635-4032-9217-4263371019bd",
            "box_id": "082e582d-6e65-4655-9295-a35e41a3b497",
            "volume_id": "664aa063-8aef-4aea-a6da-44e2effa7134",
            "included": true
        },
        {
            "id": "9ef8a973-e458-4a41-bd14-3ad659cf9457",
            "box_id": "e2f3a62f-c934-4bd8-a7d4-0996db4876a6",
            "volume_id": "e8bc74d5-3afb-4eee-a344-421b9c9f4c05",
            "included": true
        },
        {
            "id": "f9c15bb8-4879-4c7b-b658-ac74820274c1",
            "box_id": "892225b9-dfa0-47b2-a7a0-6a25230830fa",
            "volume_id": "2df17f69-0994-4017-b7c1-19cf52b16005",
            "included": true
        },
        {
            "id": "fdec46e7-7c0d-4d48-9eb8-fd054498e2fd",
            "box_id": "dcdbb967-11aa-481b-8b5b-9ac8d48b1cd6",
            "volume_id": "14648812-053a-41de-8183-3f0ffe33c9ea",
            "included": true
        },
        {
            "id": "0406f24f-99c4-4afc-aadd-60167ce0711f",
            "box_id": "fd555e77-dce3-41a6-818e-3089d1f98a07",
            "volume_id": "47e9fa5f-0391-4461-a18c-1387614ff81e",
            "included": true
        },
        {
            "id": "f94e3cf9-6306-4c5a-88a2-5057befbd11f",
            "box_id": "ab54b3a7-be99-4066-b26c-2732d86f885d",
            "volume_id": "08945667-24cb-4f41-bcd3-a51903e60f83",
            "included": true
        },
        {
            "id": "3481e30c-cb64-422e-aa8f-c4de3843c850",
            "box_id": "f5846cbe-4928-42ad-871d-4a33c599e0ec",
            "volume_id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "included": true
        },
        {
            "id": "4e7aa7f5-f085-4f7e-8ad7-5056d2eb5e00",
            "box_id": "f5846cbe-4928-42ad-871d-4a33c599e0ec",
            "volume_id": "664aa063-8aef-4aea-a6da-44e2effa7134",
            "included": true
        },
        {
            "id": "384a2800-2576-47dd-9e80-f1ad72881dc1",
            "box_id": "f5846cbe-4928-42ad-871d-4a33c599e0ec",
            "volume_id": "da22139c-910c-4bdd-8622-20f7122cb60d",
            "included": true
        },
        {
            "id": "ac32f1ec-a9c6-4dc9-acd8-5c31426f4f76",
            "box_id": "02284b39-2b33-41fd-a36c-327819dcc6b8",
            "volume_id": "9abe2a23-17a1-42ac-8dad-de2760bdef50",
            "included": true
        },
        {
            "id": "505642f5-20ef-4db2-9ea1-483f3ce152d7",
            "box_id": "02284b39-2b33-41fd-a36c-327819dcc6b8",
            "volume_id": "91290817-341d-407b-893b-83e479387462",
            "included": true
        },
        {
            "id": "35309580-e887-4b5d-9be7-7d74414ca44c",
            "box_id": "02284b39-2b33-41fd-a36c-327819dcc6b8",
            "volume_id": "134f513c-c65a-40b2-9c03-216123b5f41d",
            "included": true
        },
        {
            "id": "3811466c-57a9-4f58-86f9-126931b05ee3",
            "box_id": "9dc9c99f-c87f-4c1f-85ca-7ab001d4eddd",
            "volume_id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "included": true
        },
        {
            "id": "f16c8e64-56f4-4402-b61b-444b72786b98",
            "box_id": "9dc9c99f-c87f-4c1f-85ca-7ab001d4eddd",
            "volume_id": "664aa063-8aef-4aea-a6da-44e2effa7134",
            "included": true
        },
        {
            "id": "287eb9a7-4f91-4828-8c30-5d68b9c280a3",
            "box_id": "9dc9c99f-c87f-4c1f-85ca-7ab001d4eddd",
            "volume_id": "da22139c-910c-4bdd-8622-20f7122cb60d",
            "included": true
        },
        {
            "id": "c17789d4-9b0d-4ebb-a0c3-b458f4764640",
            "box_id": "50d1e052-00f8-4be4-b853-5db6b4ff4eea",
            "volume_id": "9abe2a23-17a1-42ac-8dad-de2760bdef50",
            "included": true
        },
        {
            "id": "c42e7c09-7f4c-454d-a583-0726a2b9d5c4",
            "box_id": "50d1e052-00f8-4be4-b853-5db6b4ff4eea",
            "volume_id": "91290817-341d-407b-893b-83e479387462",
            "included": true
        },
        {
            "id": "9590fd04-a158-4288-9fb5-679dd14c959d",
            "box_id": "50d1e052-00f8-4be4-b853-5db6b4ff4eea",
            "volume_id": "134f513c-c65a-40b2-9c03-216123b5f41d",
            "included": true
        },
        {
            "id": "6a054037-85a8-4288-beb8-f3aebc108fcd",
            "box_id": "fbe9bed0-0a47-4958-bb8b-82867ce5536e",
            "volume_id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "included": true
        },
        {
            "id": "8734bcd0-2ce0-4ba9-a323-39a084090d89",
            "box_id": "fbe9bed0-0a47-4958-bb8b-82867ce5536e",
            "volume_id": "664aa063-8aef-4aea-a6da-44e2effa7134",
            "included": true
        },
        {
            "id": "8833ec4a-8dcd-4480-b183-b42720e3a05d",
            "box_id": "db1625ae-c691-4f38-9fed-0c96702e7c7e",
            "volume_id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "included": true
        },
        {
            "id": "51e6344e-7f3a-41b2-8304-4420b9154f19",
            "box_id": "b719c558-fa08-45fe-8b8b-34969455da4d",
            "volume_id": "9abe2a23-17a1-42ac-8dad-de2760bdef50",
            "included": true
        },
        {
            "id": "8efaf704-9df9-4de2-ae81-6255ba85f797",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "included": true
        },
        {
            "id": "c0f0296f-5f9d-4ac1-a191-1cb36feb1934",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "664aa063-8aef-4aea-a6da-44e2effa7134",
            "included": true
        },
        {
            "id": "61bf580f-4b77-4111-b0df-20ce41cabcb2",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "da22139c-910c-4bdd-8622-20f7122cb60d",
            "included": true
        },
        {
            "id": "84cca00f-43bc-42c6-ab25-366bcde155fc",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "9abe2a23-17a1-42ac-8dad-de2760bdef50",
            "included": true
        },
        {
            "id": "a0c73e26-cfaf-478a-bb25-014e4623b9a2",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "91290817-341d-407b-893b-83e479387462",
            "included": true
        },
        {
            "id": "d35da6aa-6729-43c1-9777-449f0b997d7c",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "134f513c-c65a-40b2-9c03-216123b5f41d",
            "included": true
        },
        {
            "id": "e147cda8-630e-4df9-b725-dfb7cf7ce91b",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "159680d0-010b-4542-bf3b-0e8ae2f270fa",
            "included": true
        },
        {
            "id": "2af2a254-f5c1-4cc0-9696-7fe777613f17",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "d557e5b2-64a3-4aa7-86ff-36876ab3620b",
            "included": true
        },
        {
            "id": "b5099086-556c-44b5-a1b1-8e4799c8b10e",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "7d2d3524-8ecc-413e-a565-4f15f262834b",
            "included": true
        },
        {
            "id": "3155cf61-70da-45a0-bec9-7dd6812c1013",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "cfd7d6e5-0e4f-47b7-8031-6eaab5be7139",
            "included": true
        },
        {
            "id": "cc326931-cd82-4fff-a996-5564780473fd",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "4d83a0e2-1bda-4373-b814-af12045535fd",
            "included": true
        },
        {
            "id": "580b2718-6932-4ddf-9a9d-f68008c97f10",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "84bec56a-2b55-4307-8255-e622acab525b",
            "included": true
        },
        {
            "id": "24a1976f-4cc5-4935-8849-3cd9b8c4c277",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "a0bfce54-5361-42d0-8381-371a541e8c2b",
            "included": true
        },
        {
            "id": "bdd29447-76af-413d-b07e-85b54cadb257",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "c0b9570f-d6ee-4b6f-adac-782a2b8f7c92",
            "included": true
        },
        {
            "id": "42b7c6ea-501c-4ac7-bb49-1d5cd00c74a4",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "67be1aaa-3dcc-493d-b6b2-33b0f73b9d47",
            "included": true
        },
        {
            "id": "83e0b310-9d97-47ed-b6e6-f7d4d520798e",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "d9694784-d6a7-4591-969c-6e4dc406514b",
            "included": true
        },
        {
            "id": "85c28bd5-d56a-4931-b1d1-44ebb32a0992",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "e8bc74d5-3afb-4eee-a344-421b9c9f4c05",
            "included": true
        },
        {
            "id": "159e0ae5-d39e-4da1-b1cc-f11e4e833d85",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "72f73c6e-3d3d-43ed-9cd6-dabbcfbd6c75",
            "included": true
        },
        {
            "id": "f1d8a483-76fa-4a41-880a-1172eb48fec3",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "2df17f69-0994-4017-b7c1-19cf52b16005",
            "included": true
        },
        {
            "id": "20ad8842-0ba5-424a-af57-b9d8d84a15c7",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "8d5a245a-0c1d-4b49-80a7-01ea16be798c",
            "included": true
        },
        {
            "id": "a9734c54-a455-495f-b766-4d05121343c5",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "47e9fa5f-0391-4461-a18c-1387614ff81e",
            "included": true
        },
        {
            "id": "96fc22ea-cfdc-4a52-b816-f9a385fa8947",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "14648812-053a-41de-8183-3f0ffe33c9ea",
            "included": true
        },
        {
            "id": "4a44d360-fd26-4767-b4c9-7314e6d4471d",
            "box_id": "6ceba79c-da38-43ac-9802-f97c3c5ba36a",
            "volume_id": "08945667-24cb-4f41-bcd3-a51903e60f83",
            "included": true
        },
        {
            "id": "2d5f7cbe-38c7-4a7e-a450-da20495b6dd3",
            "box_id": "dd4b2f93-db1b-4708-8f0a-b57d540745e7",
            "volume_id": "159680d0-010b-4542-bf3b-0e8ae2f270fa",
            "included": true
        },
        {
            "id": "8bd9536d-3ad3-449b-8bee-6c02f7eae3c8",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "included": false
        },
        {
            "id": "beebb98f-e36f-4d87-8cdd-a506f2deca74",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "664aa063-8aef-4aea-a6da-44e2effa7134",
            "included": false
        },
        {
            "id": "51ffdfaa-a8a6-43d6-9fe7-ff9198f227fc",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "da22139c-910c-4bdd-8622-20f7122cb60d",
            "included": false
        },
        {
            "id": "d58599ad-1627-4ded-bf90-0cb5ce21499c",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "9abe2a23-17a1-42ac-8dad-de2760bdef50",
            "included": false
        },
        {
            "id": "568cd38a-72ed-42f0-9038-e4ec079db8d2",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "91290817-341d-407b-893b-83e479387462",
            "included": false
        },
        {
            "id": "639d31f8-5d44-42e5-bbd3-461c7736cdf8",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "134f513c-c65a-40b2-9c03-216123b5f41d",
            "included": false
        },
        {
            "id": "2f3d40bf-d768-4e4f-bd67-e7891679a63e",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "159680d0-010b-4542-bf3b-0e8ae2f270fa",
            "included": false
        },
        {
            "id": "cc5bbef5-cae9-4ace-973e-31450dc72898",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "d557e5b2-64a3-4aa7-86ff-36876ab3620b",
            "included": false
        },
        {
            "id": "b9626b38-61cb-4a72-80c0-729a76eae44f",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "7d2d3524-8ecc-413e-a565-4f15f262834b",
            "included": false
        },
        {
            "id": "c456fbb6-32c9-4b68-9372-9749e7d1c104",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "cfd7d6e5-0e4f-47b7-8031-6eaab5be7139",
            "included": false
        },
        {
            "id": "88bab132-9d07-4619-b826-f6d4b7e778f6",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "4d83a0e2-1bda-4373-b814-af12045535fd",
            "included": false
        },
        {
            "id": "c7c065e0-7766-42ba-88d3-0ead2e0834a7",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "84bec56a-2b55-4307-8255-e622acab525b",
            "included": false
        },
        {
            "id": "79d818e4-04a5-4fdd-b2a9-5b0fe4653cea",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "a0bfce54-5361-42d0-8381-371a541e8c2b",
            "included": false
        },
        {
            "id": "19db8077-18ef-4c60-9b92-b434951f52c7",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "c0b9570f-d6ee-4b6f-adac-782a2b8f7c92",
            "included": false
        },
        {
            "id": "6142d294-a9f2-44ce-a3a9-5604060876df",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "67be1aaa-3dcc-493d-b6b2-33b0f73b9d47",
            "included": false
        },
        {
            "id": "2f06f8b7-137b-441a-8584-37d874af4d86",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "d9694784-d6a7-4591-969c-6e4dc406514b",
            "included": false
        },
        {
            "id": "0b0c6908-cea0-436b-9bd2-7153fd10812a",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "e8bc74d5-3afb-4eee-a344-421b9c9f4c05",
            "included": false
        },
        {
            "id": "69f52aea-debf-4ac9-9421-365c19bebef6",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "72f73c6e-3d3d-43ed-9cd6-dabbcfbd6c75",
            "included": false
        },
        {
            "id": "4995db10-f41a-4b88-9478-8634f49be56d",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "2df17f69-0994-4017-b7c1-19cf52b16005",
            "included": false
        },
        {
            "id": "f8f1f05e-f359-4d93-baa1-7ace4fd358b2",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "8d5a245a-0c1d-4b49-80a7-01ea16be798c",
            "included": false
        },
        {
            "id": "4e9ba7db-895c-4a43-ba34-1282e46fb479",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "47e9fa5f-0391-4461-a18c-1387614ff81e",
            "included": false
        },
        {
            "id": "bd6ae368-66cc-43fb-b77b-ee1abf41eb7b",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "14648812-053a-41de-8183-3f0ffe33c9ea",
            "included": false
        },
        {
            "id": "5e1ddf8d-8673-4a42-9eec-b002dbf62b33",
            "box_id": "ab0976d8-296f-4fd0-b1d1-a12e46af1594",
            "volume_id": "08945667-24cb-4f41-bcd3-a51903e60f83",
            "included": false
        },
        {
            "id": "ec85bfde-a894-4152-9e27-095b73120080",
            "box_id": "490c9407-78c4-4f6a-a30a-fa670fb7052b",
            "volume_id": "7d2d3524-8ecc-413e-a565-4f15f262834b",
            "included": true
        },
        {
            "id": "43de2bd6-522b-49cc-a94a-ea0d4172f304",
            "box_id": "ce72600b-6fe9-44c7-9dd3-1a103b3275b2",
            "volume_id": "84bec56a-2b55-4307-8255-e622acab525b",
            "included": true
        },
        {
            "id": "51a6a0d3-4669-4157-a336-5a1103c572cf",
            "box_id": "349d077f-f2c0-4bf2-b303-94181746772a",
            "volume_id": "67be1aaa-3dcc-493d-b6b2-33b0f73b9d47",
            "included": true
        },
        {
            "id": "59cbd76b-9856-4a99-adca-98445a920d22",
            "box_id": "13595d56-cf87-4fe3-9e58-4afc60e476b9",
            "volume_id": "35240bc6-b618-4a74-9511-3a0f60f2bc2e",
            "included": true
        },
        {
            "id": "28acdb13-c6c8-4996-9207-6257e44385bd",
            "box_id": "13595d56-cf87-4fe3-9e58-4afc60e476b9",
            "volume_id": "664aa063-8aef-4aea-a6da-44e2effa7134",
            "included": true
        },
        {
            "id": "e9d5d22d-0059-4ea5-85d3-8dd7dd1436c9",
            "box_id": "1429de25-05aa-4a4f-89d3-3dfd1172044d",
            "volume_id": "5bff6a01-d5b6-4bf2-9874-8308c9b59ad4",
            "included": true
        }
    ]
}
```