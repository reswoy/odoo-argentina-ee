from odoo.tests.common import TransactionCase


class TestBoardingPermissionDisplayName(TransactionCase):
    def test_display_name_and_search(self):
        country = self.env.ref("base.us")
        permission = self.env["l10n_ar.boarding_permission"].create(
            {
                "number": "POC-BOARDING-001",
                "dst_country": country.id,
            }
        )

        self.assertEqual(
            permission.display_name,
            "POC-BOARDING-001 - %s" % country.display_name,
        )
        self.assertIn(
            (permission.id, permission.display_name),
            self.env["l10n_ar.boarding_permission"].name_search("POC-BOARDING"),
        )
