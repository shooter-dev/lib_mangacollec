"""Tests pour le NativeAdVolumeHomeFirstMapper.

This module contains unit tests for the NativeAdVolumeHomeFirstMapper.
"""

from mangacollec.application.mappers import NativeAdVolumeHomeFirstMapper
from mangacollec.domain.entities import NativeAdVolumeHomeFirst


class TestNativeAdVolumeHomeFirstMapper:
    """Tests pour le mapper NativeAdVolumeHomeFirst."""

    def test_from_dict_with_all_fields(self) -> None:
        """Test de conversion d'un dictionnaire complet en NativeAdVolumeHomeFirst."""
        data = {
            "id": "ad-uuid-1234",
            "volume_id": "volume-uuid-5678",
            "title": "Découvrez ce manga exceptionnel!",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
        }

        native_ad = NativeAdVolumeHomeFirstMapper.from_dict(data)

        assert isinstance(native_ad, NativeAdVolumeHomeFirst)
        assert native_ad.id == "ad-uuid-1234"
        assert native_ad.volume_id == "volume-uuid-5678"
        assert native_ad.title == "Découvrez ce manga exceptionnel!"
        assert native_ad.start_date == "2024-01-01"
        assert native_ad.end_date == "2024-12-31"

    def test_from_dict_with_optional_fields_none(self) -> None:
        """Test de conversion avec champs optionnels None."""
        data = {
            "id": "ad-test-id",
            "volume_id": "vol-test-id",
            "title": "Nouveau manga disponible",
        }

        native_ad = NativeAdVolumeHomeFirstMapper.from_dict(data)

        assert native_ad.id == "ad-test-id"
        assert native_ad.volume_id == "vol-test-id"
        assert native_ad.title == "Nouveau manga disponible"
        assert native_ad.start_date is None
        assert native_ad.end_date is None

    def test_to_dict(self) -> None:
        """Test de conversion d'un NativeAdVolumeHomeFirst en dictionnaire."""
        native_ad = NativeAdVolumeHomeFirst(
            id="ad-uuid-1234",
            volume_id="volume-uuid-5678",
            title="Découvrez ce manga exceptionnel!",
            start_date="2024-01-01",
            end_date="2024-12-31",
        )

        result = NativeAdVolumeHomeFirstMapper.to_dict(native_ad)

        assert result == {
            "id": "ad-uuid-1234",
            "volume_id": "volume-uuid-5678",
            "title": "Découvrez ce manga exceptionnel!",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
        }

    def test_to_dict_roundtrip(self) -> None:
        """Test de vérification roundtrip from_dict(to_dict(entity)) == entity."""
        original = NativeAdVolumeHomeFirst(
            id="test-id",
            volume_id="test-volume-id",
            title="Test title",
            start_date=None,
            end_date=None,
        )

        result = NativeAdVolumeHomeFirstMapper.from_dict(NativeAdVolumeHomeFirstMapper.to_dict(original))

        assert result == original
