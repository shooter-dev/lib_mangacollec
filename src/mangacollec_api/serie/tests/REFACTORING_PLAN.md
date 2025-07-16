# Plan de refactorisation des tests Serie

## Tests redondants identifiés

### 1. Tests de contenu adulte
- ✅ **Converter** : `test_deserialize_serie_with_adult_content`
- ❌ **Entity** : `test_serie_with_adult_content` (redondant)
- ❌ **Endpoint v1** : `test_get_all_series_with_adult_content` (redondant)
- ❌ **Endpoint v2** : `test_get_all_series_v2_with_adult_content` (redondant)

### 2. Tests de compteurs à zéro
- ✅ **Converter** : `test_deserialize_serie_with_zero_counts`
- ❌ **Entity** : `test_serie_with_zero_counts` (redondant)
- ❌ **Endpoint v1** : `test_get_all_series_with_zero_counts` (redondant)
- ❌ **Endpoint v2** : `test_get_all_series_v2_with_zero_counts` (redondant)

### 3. Tests Unicode
- ✅ **Converter** : `test_deserialize_with_unicode_characters`
- ❌ **Entity** : `test_serie_with_unicode_title` (redondant)
- ❌ **Endpoint v1** : `test_get_series_by_id_with_unicode_title` (redondant)
- ❌ **Endpoint v2** : `test_get_all_series_v2_with_unicode_titles` (redondant)

### 4. Tests de grands nombres
- ✅ **Converter** : `test_deserialize_with_large_counts`
- ❌ **Entity** : `test_serie_with_large_counts` (redondant)

### 5. Tests de nombres négatifs
- ✅ **Converter** : `test_deserialize_with_negative_counts`
- ❌ **Entity** : `test_serie_with_negative_counts` (redondant)

## Stratégie de refactorisation

### Principes de responsabilité
1. **Entity tests** : Logique métier pure (méthodes, validation)
2. **Converter tests** : Transformation de données (sérialisation/désérialisation)
3. **Endpoint tests** : Logique API (appels, réponses, erreurs)

### Tests à conserver par couche

#### Entity (test_serie.py)
- ✅ `test_serie_creation` (constructeur de base)
- ✅ `test_serie_equality` (logique d'égalité)
- ✅ `test_serie_repr` (représentation)
- ✅ `test_serie_to_dict` (méthode de conversion)
- ✅ `test_serie_with_kinds_ids` (logique spécifique)
- ✅ `test_serie_field_types` (validation des types)
- ✅ `test_serie_typo_in_str_method` (bug spécifique)
- ❌ Supprimer : adult_content, zero_counts, unicode, large_counts, negative_counts

#### Converter (test_serie_converter.py)  
- ✅ Garder tous les tests de désérialisation (responsabilité principale)
- ✅ Garder tests de cas limites (types incorrects, champs manquants, etc.)

#### Endpoints v1/v2
- ✅ Tests d'appels API et réponses
- ✅ Tests d'erreurs HTTP
- ❌ Supprimer : tests de données spécifiques (adult_content, zero_counts, unicode)
- ✅ Garder : empty_response, not_found, large_dataset (logique API)

## Résultat obtenu ✅
- **Avant** : 53 tests
- **Après** : 42 tests (réduction de 21% - 11 tests supprimés)
- **Bénéfices** : 
  - Temps d'exécution réduit
  - Maintenabilité améliorée 
  - Responsabilités claires entre couches
  - Pas de duplication de logique de test

## Tests supprimés
### Entity (5 tests supprimés)
- ❌ `test_serie_with_adult_content`
- ❌ `test_serie_with_zero_counts` 
- ❌ `test_serie_with_unicode_title`
- ❌ `test_serie_with_negative_counts`
- ❌ `test_serie_with_large_counts`

### Endpoint v1 (3 tests supprimés)
- ❌ `test_get_all_series_with_adult_content`
- ❌ `test_get_all_series_with_zero_counts`
- ❌ `test_get_series_by_id_with_unicode_title`

### Endpoint v2 (3 tests supprimés)
- ❌ `test_get_all_series_v2_with_adult_content`
- ❌ `test_get_all_series_v2_with_zero_counts`
- ❌ `test_get_all_series_v2_with_unicode_titles`

## Tests conservés par responsabilité
- **Converter (16 tests)** : Tous les cas de transformation de données
- **Entity (11 tests)** : Logique métier et méthodes spécifiques
- **Endpoint v1 (7 tests)** : Logique API v1
- **Endpoint v2 (8 tests)** : Logique API v2 avec objets typés