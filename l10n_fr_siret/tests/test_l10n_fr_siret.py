from odoo.exceptions import ValidationError  # type: ignore[import-untyped]
from odoo.tests import TransactionCase  # type: ignore[import-untyped]


class Test(TransactionCase):
    """Test SIRET."""

    def test_invalid_siret(self):
        """Ensure checks operate normally when updating the SIRET."""

        with self.assertRaisesRegex(
            ValidationError,
            "SIRET '5555555560001' is invalid.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "5555555560001"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "SIRET '5555555560001A' is invalid.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "5555555560001A"}
            )

        with self.assertRaises(ValidationError):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "55555555******"}
            )

        with self.assertRaises(ValidationError):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "55555555C*****"}
            )

        with self.assertRaises(ValidationError):
            self.env["res.partner"].create(
                {"name": "Test Partner B", "siret": "555555559*****"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "SIRET '55555555600012' is invalid.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner B", "siret": "55555555600012"}
            )
