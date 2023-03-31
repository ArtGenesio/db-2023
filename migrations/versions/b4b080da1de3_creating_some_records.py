"""

creating_some_records

Revision ID: b4b080da1de3
Creation date: 2023-03-29 18:36:23.847058

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'b4b080da1de3'
down_revision = 'b58017e8c44e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""--sql
    INSERT INTO access_key(name) VALUES ('key 1');
INSERT INTO secured_resource(name) VALUES ('resource 1');
INSERT INTO security_group(name) VALUES ('group 1');
INSERT INTO group_key(group_id, key_id) SELECT group_id, key_id FROM security_group, access_key WHERE security_group.name = 'group 1' AND access_key.name = 'key 1';
INSERT INTO group_resource(group_id, resource_id) SELECT group_id, resource_id FROM security_group, secured_resource WHERE security_group.name = 'group 1' AND secured_resource.name = 'resource 1';
    """)


def downgrade() -> None:
    op.execute(f"""--sql
    DELETE FROM group_resource WHERE resource_id = (SELECT resource_id as r1 FROM secured_resource WHERE name = 'resource 1');
DELETE FROM group_key WHERE key_id = (SELECT key_id as k1 FROM access_key WHERE name = 'key 1');
DELETE FROM security_group WHERE name = 'group 1';
DELETE FROM secured_resource WHERE name = 'resource 1';
DELETE FROM access_key WHERE name = 'key 1';

    """)



