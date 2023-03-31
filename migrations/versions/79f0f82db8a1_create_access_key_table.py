"""

create_access_key_table

Revision ID: 79f0f82db8a1
Creation date: 2023-03-29 18:15:02.180801

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = '79f0f82db8a1'
down_revision = 'e120aeca0fb1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""--sql
            CREATE TABLE access_key(
            key_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
    """)

    


def downgrade() -> None:
     op.execute(f"""--sql
            DROP TABLE IF EXISTS access_key CASCADE;
    """)



