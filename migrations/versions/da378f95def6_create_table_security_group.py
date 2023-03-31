"""

create_table_security_group

Revision ID: da378f95def6
Creation date: 2023-03-29 18:18:56.568886

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'da378f95def6'
down_revision = '79f0f82db8a1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""--sql
    CREATE TABLE security_group(
    group_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

    """)

    


def downgrade() -> None:
    op.execute(f"""--sql
    DROP TABLE IF EXISTS security_group CASCADE;
    """)


    
