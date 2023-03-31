"""

create_table_group_key

Revision ID: f592dd3afed9
Creation date: 2023-03-29 18:29:21.480564

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'f592dd3afed9'
down_revision = 'da378f95def6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    
    op.execute(f"""--sql
    CREATE TABLE group_key(
    group_id UUID REFERENCES security_group(group_id) ON DELETE CASCADE,
    key_id UUID REFERENCES access_key(key_id) ON DELETE CASCADE
);
    """)
    


def downgrade() -> None:
    op.execute(f"""--sql
    DROP TABLE IF EXISTS group_key CASCADE;
    """)



