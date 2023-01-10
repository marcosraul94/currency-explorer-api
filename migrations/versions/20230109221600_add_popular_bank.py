"""Add popular bank

Revision ID: 6fca43b9ee38
Revises: c139478f03e2
Create Date: 2023-01-09 22:16:00.317328

"""
from alembic import op
from src.common.bank_ids import bank_ids


# revision identifiers, used by Alembic.
revision = '6fca43b9ee38'
down_revision = 'c139478f03e2'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(f"""
    INSERT INTO bank (id, link)
    VALUES (
    '{bank_ids.popular}',
    'https://popularenlinea.com/personas/Paginas/Home.aspx'
    )
    """)


def downgrade():
    op.execute(f"""
    DELETE FROM bank WHERE id = '{bank_ids.popular}'
    """)
