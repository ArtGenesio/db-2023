"""

create_table_group_resource

Revision ID: b58017e8c44e
Creation date: 2023-03-29 18:34:46.179912

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'b58017e8c44e'
down_revision = 'f592dd3afed9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""--sql
    CREATE TABLE group_resource(
    group_id UUID REFERENCES security_group(group_id) ON DELETE CASCADE,
    resource_id UUID REFERENCES secured_resource(resource_id) ON DELETE CASCADE
);
    """)



def downgrade() -> None:
    op.execute(f"""--sql
    DROP TABLE IF EXISTS group_resource CASCADE;
    """)


