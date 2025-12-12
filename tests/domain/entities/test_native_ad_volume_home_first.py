"""Tests pour l'entité NativeAdVolumeHomeFirst.

This module contains unit tests for NativeAdVolumeHomeFirst entity.
"""

import pytest

from mangacollec.domain.entities import NativeAdVolumeHomeFirst


class TestNativeAdVolumeHomeFirst:
    """Tests pour l'entité NativeAdVolumeHomeFirst."""

    def test_create_native_ad_with_all_fields(self) -> None:
        """Test de création d'une publicité native avec tous les champs."""
        native_ad = NativeAdVolumeHomeFirst(
            id="ad-uuid-1234",
            volume_id="volume-uuid-5678",
            title="Découvrez ce manga exceptionnel!",
            start_date="2024-01-01",
            end_date="2024-12-31",
        )

        assert native_ad.id == "ad-uuid-1234"
        assert native_ad.volume_id == "volume-uuid-5678"
        assert native_ad.title == "Découvrez ce manga exceptionnel!"
        assert native_ad.start_date == "2024-01-01"
        assert native_ad.end_date == "2024-12-31"

    def test_create_native_ad_with_optional_fields_none(self) -> None:
        """Test de création d'une publicité native avec champs optionnels None."""
        native_ad = NativeAdVolumeHomeFirst(
            id="ad-uuid-1234",
            volume_id="volume-uuid-5678",
            title="Nouveau manga disponible",
            start_date=None,
            end_date=None,
        )

        assert native_ad.id == "ad-uuid-1234"
        assert native_ad.volume_id == "volume-uuid-5678"
        assert native_ad.title == "Nouveau manga disponible"
        assert native_ad.start_date is None
        assert native_ad.end_date is None

    def test_native_ad_is_frozen(self) -> None:
        """Test que l'entité NativeAdVolumeHomeFirst est immuable."""
        native_ad = NativeAdVolumeHomeFirst(
            id="test-id",
            volume_id="test-volume-id",
            title="Test title",
            start_date=None,
            end_date=None,
        )

        with pytest.raises(Exception):
            native_ad.title = "New title"
