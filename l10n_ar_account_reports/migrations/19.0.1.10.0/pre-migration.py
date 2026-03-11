from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    """
    Delete existing inflation adjustment index records before data reload.

    The data file inflation_adjustment_index.xml uses noupdate="1", but during
    migration the records may lack their ir.model.data XML IDs, causing Odoo to
    attempt recreation and hitting the unique-per-month constraint.

    Deleting them here allows the data file to recreate them cleanly.
    """
    if not version:
        return
    env.cr.execute("DELETE FROM inflation_adjustment_index")
