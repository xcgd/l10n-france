from odoo.exceptions import ValidationError  # type: ignore[import-untyped]
from odoo.tests import TransactionCase  # type: ignore[import-untyped]


class Test(TransactionCase):
    """Test SIRET."""

    def test_invalid_siret(self):
        """Ensure checks operate normally when updating the SIRET."""

        with self.assertRaisesRegex(
            ValidationError,
            "The NIC '0004' is incorrect: it must have exactly 5 digits.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "5018274630004"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "The NIC '0004A' is incorrect: it must have exactly 5 digits.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "5018274630004A"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "The SIREN '50182746' is incorrect: it must have exactly 9 digits.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "50182746"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "The SIREN '50182746C' is incorrect: it must have exactly 9 digits.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner A", "siret": "50182746C"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "The SIREN '501827469' is invalid: the checksum is wrong.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner B", "siret": "501827469"}
            )

        with self.assertRaisesRegex(
            ValidationError,
            "The SIRET '50182746300041' is invalid: the checksum is wrong.",
        ):
            self.env["res.partner"].create(
                {"name": "Test Partner B", "siret": "50182746300041"}
            )
