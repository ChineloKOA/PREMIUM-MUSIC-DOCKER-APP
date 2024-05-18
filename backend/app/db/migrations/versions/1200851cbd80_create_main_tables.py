"""create_main_tables

Revision ID: 1200851cbd80
Revises: 
Create Date: 2024-05-18 08:12:35.050450

"""
# ... import statements ...
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '1200851cbd80'
down_revision = None
branch_labels = None
depends_on = None


def create_cleaning_table() -> None:
    op.create_table(
        "cleaning",  # table name changed from 'class' to 'classes'
        sa.Column("id", sa.Integer, primary_key=True),  # primary_key=True, means this will be the key for this table
        sa.Column("name", sa.Text, nullable=False, index=True),  # nullable=false, means this column cannot be null
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
        sa.Column("location", sa.Text, nullable=False)  # 'Location' changed to 'location'
    )


def create_class_table() -> None:
    op.create_table(
        "classes",  # table name changed from 'class' to 'classes'
        sa.Column("id", sa.Integer, primary_key=True),  # primary_key=True, means this will be the key for this table
        sa.Column("name", sa.Text, nullable=False, index=True),  # nullable=false, means this column cannot be null
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
        sa.Column("location", sa.Text, nullable=False)  # 'Location' changed to 'location'
    )


def upgrade() -> None:
    # commands to migrate the database forward
    create_cleaning_table()
    create_class_table()


def downgrade() -> None:
    # commands to revert the previous migration
    op.drop_table("cleaning")
    op.drop_table("classes")


